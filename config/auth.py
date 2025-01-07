from google.cloud import firestore, storage
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import vertexai
from vertexai.generative_models import GenerativeModel
from config.settings import DB_SERVICE_ACCOUNT_PATH, GENAI_SERVICE_ACCOUNT_PATH, CLIENT_TOKEN_PATH, GOOGLE_CLOUD_PROJECT, GEMINI_MODEL, GEMINI_MODEL_LOCATION
import os, pickle

def get_firestore_cloud_client():
    """
    Returns a Firestore client authenticated with the service account.
    """
    # Firestore client
    firestore_client = firestore.Client.from_service_account_json(
        DB_SERVICE_ACCOUNT_PATH,
        project=GOOGLE_CLOUD_PROJECT
    )
    return firestore_client

def get_cloud_storage_client():
    """
    Returns a Cloud Storage client authenticated with the service account.
    """
    # Google Cloud Storage client
    storage_client = storage.Client.from_service_account_json(
        DB_SERVICE_ACCOUNT_PATH,
        project=GOOGLE_CLOUD_PROJECT
    )
    return storage_client

def get_gemini_model():
    """
    Configures and returns a Gemini Generative AI model client authenticated with a service account.
    """
    # Only initialize the Vertex AI client with service account credentials
    credentials = service_account.Credentials.from_service_account_file(GENAI_SERVICE_ACCOUNT_PATH)
    vertexai.init(project=GOOGLE_CLOUD_PROJECT, location=GEMINI_MODEL_LOCATION, credentials=credentials)
    # Initialize and return the Generative Model client
    model = GenerativeModel(GEMINI_MODEL)
    return model

def get_oauth_client_token():
    """
    Authenticates and returns valid credentials for accessing Google APIs, 
    using a .pickle token file to store and refresh the credentials as needed.
    """
    creds = None
    # Load existing credentials from the pickle file
    if os.path.exists(CLIENT_TOKEN_PATH):
        with open(CLIENT_TOKEN_PATH, 'rb') as token_file:
            creds = pickle.load(token_file)
    # If no valid credentials are available, raise an error or exit
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh the credentials if expired
            creds.refresh(Request())
            # Save the refreshed credentials back to the pickle file
            with open(CLIENT_TOKEN_PATH, 'wb') as token_file:
                pickle.dump(creds, token_file)
        else:
            raise RuntimeError(
                "Token file is missing or invalid. Please ensure the token file is present at: "
                f"{CLIENT_TOKEN_PATH}"
            )
    return creds

def get_google_drive_service():
    """
    Builds and returns an authenticated Google Drive API service.
    """
    return build('drive', 'v3', credentials=get_oauth_client_token())

# if __name__ == "__main__":
#     # Test the function
#     firestore_client = get_firestore_cloud_client()
#     print("Firestore Client: ", firestore_client)
#     gcs_client = get_cloud_storage_client()
#     print("Storage Client: ", gcs_client)
#     gen_ai_model = get_gemini_model()
#     print("Gemini 1.5 Flash Model: ", gen_ai_model)
#     drive_service = get_google_drive_service()
#     print(drive_service)
#     docs_service = get_google_docs_service()
#     print(docs_service)