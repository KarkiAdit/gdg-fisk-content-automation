import logging
from google.cloud import firestore
from config.auth import get_firestore_cloud_client
from models import ProjectsPageResponse, CodelabsPageResponse, CulturePageResponse, HomePageResponse, VideoContent
from dataclasses import asdict

# Set up logging
logging.basicConfig(level=logging.INFO)

DEFAULT_CULTURE_VIDEO = VideoContent(
    title="Code, Laugh, Conquer: The GDG Way",
    imgUrl="https://storage.googleapis.com/gdg-fisk-assets/images/culture-video-img.png",
    videoUrl="/",
    genres=["SARCASM", "COLLABORATIVE LEARNING", "PASSION"]
)
HOME_VIDEO_URL = "/"

class FirestoreManager:
    """
    Service class for interacting with the Firestore database,
    providing helpers for CRUD operations and ensuring required documents
    are present in the 'gdg-fisk-content' collection.
    """

    def __init__(self):
        """
        Initializes the FirestoreManager class by setting up a Firestore client,
        the collection name, and ensuring required documents are present.
        """
        self.client = get_firestore_cloud_client()
        self.collection_name = "gdg-fisk-content"
        self.documents = {
            "ProjectsPageResponse": ProjectsPageResponse(projects=[]),
            "CodelabsPageResponse": CodelabsPageResponse(codelabs=[]),
            "CulturePageResponse": CulturePageResponse(culturePageVideo=DEFAULT_CULTURE_VIDEO, testimonials=[], metrics=[]),
            "HomePageResponse": HomePageResponse(homeVideoUrl=HOME_VIDEO_URL, projectSummaries=[], testimonials=[])
        }
        self._initialize_documents()

    def _initialize_documents(self):
        """
        Ensures that all required documents are present in the Firestore collection.
        If a document does not exist, it is created with default data.
        """
        for doc_name, default_instance in self.documents.items():
            doc_ref = self.client.collection(self.collection_name).document(doc_name)
            try:
                if not doc_ref.get().exists:
                    logging.info(f"Document '{doc_name}' does not exist. Creating...")
                    doc_ref.set(self._convert_to_dict(default_instance))
                else:
                    logging.info(f"Document '{doc_name}' already exists.")
            except Exception as e:
                logging.error(f"Error initializing document '{doc_name}': {e}")

    def _convert_to_dict(self, data):
        """
        Converts an object to a dictionary if it is a dataclass, otherwise returns it as is.
        Args:
            data: The data to convert.
        Returns:
            dict: The converted dictionary or the original data.
        """
        if hasattr(data, "__dataclass_fields__"):
            return asdict(data)
        return data

    def update_document(self, doc_name: str, data: dict | object):
        """
        Updates or creates a document in the Firestore collection.
        Args:
            doc_name (str): The name of the document to update or create.
            data (dict | object): The data to update the document with.
        """
        doc_ref = self.client.collection(self.collection_name).document(doc_name)
        try:
            data = self._convert_to_dict(data)
            data["last_updated"] = firestore.SERVER_TIMESTAMP
            if doc_ref.get().exists:
                doc_ref.update(data)
                logging.info(f"Document '{doc_name}' updated successfully.")
            else:
                doc_ref.set(data)
                logging.info(f"Document '{doc_name}' created successfully.")
        except Exception as e:
            logging.error(f"Error updating document '{doc_name}': {e}")

    def append_doc_field_list(self, doc_name: str, field_name: str, new_data: any):
        """
        Appends data to a list field in a Firestore document.
        Args:
            doc_name (str): The name of the document to update.
            field_name (str): The name of the list field to append data to.
            new_data (any): The data to append. Can be a single object or a list.
        """
        try:
            field_data = self.read_field(doc_name, field_name)
            if not isinstance(field_data, list):
                raise TypeError(f"Field '{field_name}' is not a list.")
            if hasattr(new_data, "__dataclass_fields__"):
                new_data = self._convert_to_dict(new_data)
            if isinstance(new_data, list):
                new_data = [self._convert_to_dict(item) for item in new_data]
            field_data.extend(new_data)
            self.update_field(doc_name, field_name, field_data)
            logging.info(f"Data appended to list field '{field_name}' in document '{doc_name}'.")
        except Exception as e:
            logging.error(f"Error appending to list field '{field_name}' in document '{doc_name}': {e}")

    def update_field(self, doc_name: str, field_name: str, value: any):
        """
        Updates a specific field in a Firestore document.
        Args:
            doc_name (str): The name of the document to update.
            field_name (str): The name of the field to update.
            value (any): The new value for the field.
        """
        doc_ref = self.client.collection(self.collection_name).document(doc_name)
        try:
            data = {
                field_name: value,
                "last_updated": firestore.SERVER_TIMESTAMP
            }
            if doc_ref.get().exists:
                doc_ref.update(data)
                logging.info(f"Field '{field_name}' updated successfully in document '{doc_name}'.")
            else:
                doc_ref.set(data)
                logging.info(f"Document '{doc_name}' created and field '{field_name}' added successfully.")
        except Exception as e:
            logging.error(f"Error updating field '{field_name}' in document '{doc_name}': {e}")

    def read_document(self, doc_name: str) -> dict | None:
        """
        Reads a document from the Firestore collection.
        Args:
            doc_name (str): The name of the document to read.
        Returns:
            dict: The data of the document, or None if it does not exist.
        """
        doc_ref = self.client.collection(self.collection_name).document(doc_name)
        try:
            doc = doc_ref.get()
            if doc.exists:
                logging.info(f"Document '{doc_name}' fetched successfully.")
                return doc.to_dict()
            else:
                logging.warning(f"Document '{doc_name}' does not exist.")
                return None
        except Exception as e:
            logging.error(f"Error reading document '{doc_name}': {e}")
            return None

    def read_field(self, doc_name: str, field_name: str) -> any:
        """
        Reads a specific field from a Firestore document.
        Args:
            doc_name (str): The name of the document to read.
            field_name (str): The name of the field to fetch.
        Returns:
            Any: The value of the field, or None if the document or field does not exist.
        """
        doc_ref = self.client.collection(self.collection_name).document(doc_name)
        try:
            doc = doc_ref.get()
            if doc.exists:
                doc_data = doc.to_dict()
                if field_name in doc_data:
                    logging.info(f"Field '{field_name}' in document '{doc_name}' fetched successfully.")
                    return doc_data[field_name]
                else:
                    logging.warning(f"Field '{field_name}' does not exist in document '{doc_name}'.")
                    return None
            else:
                logging.warning(f"Document '{doc_name}' does not exist.")
                return None
        except Exception as e:
            logging.error(f"Error reading field '{field_name}' in document '{doc_name}': {e}")
            return None

# if __name__ == "__main__":
#     """
#     Demonstrates the usage of FirestoreManager methods to interact with Firestore.
#     """
#     firestore_manager = FirestoreManager()
#     sample_project = {"title": "Sample Project", "description": "A test project for demonstration."}
#     sample_codelab = {"title": "Sample Codelab", "description": "A test codelab for learning."}
#     sample_testimonial = {"author": "John Doe", "content": "This is a testimonial."}
#     # Demonstrate updating a document
#     print("Updating 'ProjectsPageResponse' document...")
#     firestore_manager.update_document("ProjectsPageResponse", {"projects": [sample_project]})
#     # Demonstrate reading a document
#     print("\nReading 'ProjectsPageResponse' document...")
#     projects_doc = firestore_manager.read_document("ProjectsPageResponse")
#     print("Document data:", projects_doc)
#     # Demonstrate updating a field
#     print("\nUpdating 'homeVideoUrl' field in 'HomePageResponse' document...")
#     firestore_manager.update_field("HomePageResponse", "homeVideoUrl", "/new-home-video-url")
#     # Demonstrate reading a specific field
#     print("\nReading 'homeVideoUrl' field from 'HomePageResponse' document...")
#     home_video_url = firestore_manager.read_field("HomePageResponse", "homeVideoUrl")
#     print("Home Video URL:", home_video_url)
#     # Demonstrate appending data to a list field
#     print("\nAppending a new testimonial to 'testimonials' field in 'CulturePageResponse' document...")
#     firestore_manager.append_doc_field_list("CulturePageResponse", "testimonials", sample_testimonial)
#     # Read the updated 'CulturePageResponse' document
#     print("\nReading 'CulturePageResponse' document after appending to 'testimonials'...")
#     culture_doc = firestore_manager.read_document("CulturePageResponse")
#     print("Document data:", culture_doc)
#     # Empty "CodelabsPageResponse"
#     firestore_manager.update_document("CodelabsPageResponse", {"codelabs": []})
