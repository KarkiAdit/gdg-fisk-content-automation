import os

# Path to the service account credentials
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_SERVICE_ACCOUNT_PATH = os.path.join(BASE_DIR, "config", "db_credentials.json")
GENAI_SERVICE_ACCOUNT_PATH = os.path.join(BASE_DIR, "config", "gemini_credentials.json")
CLIENT_TOKEN_PATH = os.path.join(BASE_DIR, "config", "drive_token.pickle")

# Google Cloud Project ID
GOOGLE_CLOUD_PROJECT = "gdg-fisk-content-automation"