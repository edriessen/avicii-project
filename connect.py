from google.cloud import language
from google.oauth2 import service_account
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
SCOPES = ['https://www.googleapis.com/auth/cloud-language']
SERVICE_ACCOUNT_FILE = 'credentials.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = language.LanguageServiceClient(
    credentials=credentials
)