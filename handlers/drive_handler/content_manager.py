from config.auth import get_google_drive_service, get_google_docs_service
from utils.file_handler import FileHandler
from googleapiclient.errors import HttpError
import urllib.parse

class DriveContentManager:
    """
    A class to manage files in Google Drive, specifically interacting with
    Google Docs files. This class provides methods to authenticate with Google Drive, 
    retrieve files from specific folders, and perform CRUD operations on Google Docs files.

    Attributes:
        drive_service (Google Drive API service): The authenticated Google Drive service.
        folder_ids (dict): A dictionary mapping folder names to their corresponding Google Drive folder IDs.
        content_identifiers (dict): A dictionary mapping folder names to lists of files within those folders.
        file_handler (FileHandler): An instance of the FileHandler class for handling file operations.
    """
    
    def __init__(self, folder_ids):
        """
        Initializes the DriveContentManager with an authenticated Drive service and a dictionary 
        of folder names and their corresponding Google Drive folder IDs.

        Args:
            folder_ids (dict): A dictionary mapping folder names to their corresponding Google Drive folder IDs.
        """
        self.drive_service = get_google_drive_service()
        self.docs_service = get_google_docs_service()
        self.folder_ids = folder_ids
        self.content_identifiers = {}
        self.file_handler = FileHandler()
        self._refresh_content_identifier()

    def _refresh_content_identifier(self):
        """
        Refreshes the mapping of folder names to lists of files within those folders.

        This function fetches all the files present in the specified folders and
        stores them in the `content_identifiers` attribute for easy access later.
        """
        for folder_name, folder_id in self.folder_ids.items():
            self.content_identifiers[folder_name] = self.get_files_in_folder(folder_id)
        print(self.content_identifiers)

    def get_files_in_folder(self, folder_id):
        """
        Retrieves a dictionary of files inside a specific Google Drive folder using its ID.
        The dictionary will have file IDs as keys and file names as values.

        Args:
            folder_id (str): The ID of the Google Drive folder.

        Returns:
            dict: A dictionary where the key is the file name and the value is the file id.
        """
        query = f"'{folder_id}' in parents and trashed = false"
        results = self.drive_service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get('files', [])
        # Convert list of files into a dictionary with id as key and name as value
        return {file['name']: file['id'] for file in files}

    def get_file_from_folder(self, folder_id, file_name):
        """
        Retrieves a specific Google Docs file by its name from a folder in Google Drive.

        Args:
            folder_id (str): The ID of the folder containing the file.
            file_name (str): The name of the Google Docs file to retrieve.

        Returns:
            dict or None: A dictionary containing the file's 'id' and 'name' if found, or None if not found.
        """
        try:
            # URL encode the file name to handle special characters like spaces or punctuation
            encoded_file_name = urllib.parse.quote(file_name)
            # Construct the query string
            query = f"'{folder_id}' in parents and name = '{encoded_file_name}' and trashed = false and mimeType = 'application/vnd.google-apps.document'"
            # Execute the query
            results = self.drive_service.files().list(q=query, fields="files(id, name)").execute()
            files = results.get('files', [])
            # Handle the case of no files found
            if not files:
                print(f"No files found with name '{file_name}' in folder {folder_id}.")
                return None
            # Handle multiple files found with the same name (optional behavior)
            if len(files) > 1:
                print(f"Warning: Multiple files found with the name '{file_name}'. Returning the first one.")
            # Return the first file if found
            return files[0]
        except HttpError as error:
            print(f"Error retrieving file: {error}")
            return None

    def read_google_docs(self, folder_name, file_name, output_file_name="output.docx", export_format="application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
        """
        Exports a Google Docs file from a specified folder, adds a UUID if necessary, and saves it locally.

        This method uses the Google Drive API to export a Google Docs file into the specified format 
        (e.g., .docx) and saves it to the given output path on the local machine. If the exported file 
        doesn't already contain a UUID, it generates a new one and inserts it into the first paragraph 
        of the document. The updated Google Docs file is then synced with the Google Docs API.

        Args:
            folder_name (str): The name of the folder containing the Google Docs file.
            file_name (str): The name of the Google Docs file to retrieve.
            output_file_name (str): The local file name where the exported file should be saved. Defaults to "output.docx".
            export_format (str, optional): The MIME type to export the file in. Default is "application/vnd.openxmlformats-officedocument.wordprocessingml.document" (i.e., .docx format).

        Returns:
            tuple: A tuple containing two values:
                - str: The local path where the exported file is saved if successful.
                - str: The UUID added to the document (either existing or newly generated).
            
            None: If an error occurs during the export process.

        Raises:
            Exception: If the export request fails, there are issues with the provided file metadata, 
                    or there is a problem with updating the document.
        """
        try:
            # Get file metadata using get_file_from_folder
            if folder_name in self.content_identifiers and file_name in self.content_identifiers[folder_name]:
                file_metadata = self.get_file_from_folder(self.folder_ids[folder_name], file_name)
            else:
                print("No such file or folder found.")
                return None
            # Retrieve the file ID from the metadata
            file_id = file_metadata['id']
            # Make a file request using the Google Drive API to export the file
            request = self.drive_service.files().export_media(fileId=file_id, mimeType=export_format)
            # Execute the request to get the file content in bytes
            file_content = request.execute()
            # Save the file locally using FileHandler
            output_path = self.file_handler.save_file(file_content, output_file_name)
            print(f"Google Docs file saved as {output_path}")
            # Add a UUID to the file if not already present
            uuid, new_uuid_added = self.file_handler.update_file_with_uuid(output_path)
            if new_uuid_added:
                # Update the Google Docs file with the new UUID using the Google Docs API
                self.docs_service.documents().batchUpdate(
                    documentId=file_id,
                    body={
                        "requests": [
                            {
                                "insertText": {
                                    "location": {
                                        "index": 1  # Assuming index 1 is the start of the document
                                    },
                                    "text": f"File Id: \"{uuid}\"\n"
                                }
                            }
                        ]
                    }
                ).execute()
                print(f"UUID '{uuid}' added to the Google Docs file.")
            return output_path, uuid
        except Exception as e:
            # Catch any exceptions and print the error message
            print(f"Error exporting Google Docs to {export_format} format: {e}")
            return None

    def download_md_from_drive(self, folder_name, file_name, local_filename="readme.md"):
        """
        Downloads a Google Docs file as Markdown (.md) from Google Drive and saves it locally.

        Args:
            folder_name (str): The name of the folder containing the file.
            file_name (str): The name of the Google Docs file to retrieve.
            local_filename (str): The local name where the downloaded file should be saved.

        Returns:
            str: The local path of the saved file if successful, None if an error occurs.
        """
        try:
            # Get file metadata using get_file_from_folder
            if folder_name in self.content_identifiers and file_name in self.content_identifiers[folder_name]:
                file_metadata = self.get_file_from_folder(self.folder_ids[folder_name], file_name)
            else:
                print("No such file or folder found.")
                return None
            file_id = file_metadata['id']
            # Export the Google Docs file as Markdown
            request = self.drive_service.files().export_media(fileId=file_id, mimeType='text/markdown')
            file_content = request.execute()
            # Save the file locally using FileHandler
            output_path = self.file_handler.save_file(file_content, local_filename)
            print(f"File downloaded to {output_path}")
            return output_path
        except Exception as e:
            print(f"Error downloading Markdown file: {e}")
            return None

    def remove_file(self, file_id):
        """
        Deletes a Google Docs file by its ID using the Google Drive API.

        Args:
            file_id (str): The ID of the Google Docs file to delete.

        Returns:
            bool: True if the file was successfully deleted, False otherwise.
        """
        try:
            self.drive_service.files().delete(fileId=file_id).execute()
            print(f"File {file_id} deleted successfully.")
            return True
        except HttpError as error:
            print(f"Error removing file: {error}")
            return False
        
# if __name__ == "__main__":
#     # Test function
#     from utils.drive_folders.folder_ids_map import folder_ids
#     drive_c_manager = DriveContentManager(folder_ids)
#     # drive_c_manager.download_md_from_drive("codelabs", "TestCodelab")
#     drive_c_manager.read_google_docs("projects", "TestDocs")
#     drive_c_manager.download_md_from_drive("projects", "TestDocs")
#     # drive_c_manager.file_handler.cleanup()

