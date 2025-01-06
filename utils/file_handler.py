import os
import tempfile

class FileHandler:
    """
    A utility class for handling file operations in a temporary directory, including saving,
    deleting, and cleaning up files.

    This class creates a temporary folder upon initialization and provides methods for:
    - Saving files with specified filenames.
    - Deleting specific files from the temporary folder.
    - Cleaning up (deleting) all files and the temporary folder itself.

    Attributes:
        temp_folder (str): The path to the temporary directory created for file operations.
    """

    def __init__(self):
        """
        Initializes the FileHandler and creates a temporary folder for file operations.

        This method creates a temporary directory using Python's `tempfile` module. All file operations 
        performed by this class will be contained within this directory.
        """
        self.temp_folder = tempfile.mkdtemp()
        print(f"Temporary folder created: {self.temp_folder}")

    def save_file(self, file_content, output_filename="output.docx"):
        """
        Saves the provided content to a file within the temporary folder.

        Args:
            file_content (str or bytes): The content to save (can be text or binary).
            output_filename (str): The name of the file to save in the temporary folder. Defaults to "output.docx".

        Returns:
            str: The full path to the saved file if successful, None otherwise.
        """
        if not file_content:
            print("Failed to save file: No content provided.")
            return None
        
        file_path = os.path.join(self.temp_folder, output_filename)
        
        try:
            # Determine if the content is text or binary and save accordingly
            if isinstance(file_content, str):
                # Save as text (use "w" mode for writing text files)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(file_content)
            elif isinstance(file_content, bytes):
                # Save as binary (use "wb" mode for writing binary files)
                with open(file_path, "wb") as file:
                    file.write(file_content)
            else:
                print("Unsupported file content type")
                return None
            print(f"File saved at {file_path}")
            return file_path
        except Exception as error:
            print(f"Error saving file: {error}")
            return None

    def delete_file(self, filename):
        """
        Deletes a file with the specified name from the temporary folder.

        Args:
            filename (str): The name of the file to delete from the temporary folder.

        Returns:
            bool: True if the file was successfully deleted, False if the file was not found or an error occurred.
        """
        file_path = os.path.join(self.temp_folder, filename)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File deleted: {file_path}")
                return True
            else:
                print(f"File not found: {file_path}")
                return False
        except Exception as error:
            print(f"Error deleting file: {error}")
            return False

    def cleanup(self):
        """
        Deletes all files in the temporary folder and removes the folder itself.

        This method iterates through all files in the temporary folder, deleting each one, 
        and then removes the folder. Use this method to clean up resources after file operations are complete.

        Returns:
            None
        """
        try:
            # Delete each file in the temporary folder
            for filename in os.listdir(self.temp_folder):
                file_path = os.path.join(self.temp_folder, filename)
                os.remove(file_path)
            os.rmdir(self.temp_folder)
            print(f"Temporary folder {self.temp_folder} and all contents have been deleted.")
        except Exception as error:
            print(f"Error cleaning up temp folder: {error}")
