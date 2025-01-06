import re
from config.auth import get_cloud_storage_client
import base64
from uuid import uuid4

class GcsManager:
    """
    Service class for interacting with Google Cloud Storage (GCS),
    providing helpers for extracting, uploading, and replacing base64-encoded 
    images within file content.
    """

    def __init__(self, bucket_name: str):
        """
        Initializes the GcsManager with a GCS client and a bucket reference.

        Args:
            bucket_name (str): The name of the Google Cloud Storage bucket.
        """
        self.client = get_cloud_storage_client()
        self.bucket_name = bucket_name  # Cloud Storage bucket name
        self.bucket = self.client.bucket(bucket_name)

    def publish_image_assets(self, file_content: str):
        """
        Replaces base64 images in the input content with the corresponding public URLs
        after uploading the image assets to the Google Cloud Storage bucket.

        Args:
            file_content (str): Content containing base64-encoded images to be uploaded to GCS.

        Returns:
            tuple: A tuple containing:
                - Modified content with public URLs in place of base64 data.
                - A list of dictionaries containing original base64 data and public URLs.
        """
        # Regex pattern to match base64 image data in markdown-style image syntax
        image_pattern = r'\[.*?\]:\s*<data:image\/[a-zA-Z]+;base64,([^>]+)>'
        # Split the file content into lines (since each image is expected to be on a new line)
        lines = file_content.split('\n')
        # List to store the image data and their corresponding public URLs
        image_data_with_placeholder = []
        # Iterate through each line and look for base64 matches
        for i, line in enumerate(lines):
            # Search for the image pattern in the current line
            match = re.search(image_pattern, line)
            if match:
                print("Match found: ", line)
                # Extract base64 data from the match
                image_base64 = match.group(1)
                # Generate a unique file name for the image
                file_name = f"images/{uuid4().hex}.png"
                # Decode the base64 image data
                image_data = base64.b64decode(image_base64)
                # Upload the image to GCS
                blob = self.bucket.blob(file_name)
                blob.upload_from_string(image_data, content_type='image/png')
                # Get the public URL for the uploaded image
                public_url = blob.public_url
                # Replace the base64 data with the public URL in the current line
                lines[i] = line.replace(f'<data:image/png;base64,{image_base64}>', f'{public_url}')
                # Append the original base64 data and the public URL to the list
                image_data_with_placeholder.append({
                    "original_base64": image_base64,
                    "public_url": public_url
                })
        # Reassemble the content back into a single string
        modified_content = '\n'.join(lines)
        return modified_content, image_data_with_placeholder

    
if __name__ == "__main__":
    # Test function
    from utils.drive_folders.sample_readme_str import readme_content
    readme_txt = readme_content
    # Initialize the Google Cloud Storage Manager with the bucket name
    assets_manager = GcsManager(bucket_name="gdg-fisk-assets")
    try:
        # Extract images and replace base64 data with public URLs
        modified_content, _ = assets_manager.publish_image_assets(readme_txt)
        print("Modified README Content:")
        print(modified_content)
    except Exception as e:
        print(f"An error occurred: {e}")
