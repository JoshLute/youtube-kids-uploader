# uploader/auth.py  – change only the marked line
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleapiclient.discovery
import pickle, pathlib

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
TOKEN_PATH = pathlib.Path("token.json")

def get_service():
    creds = None
    if TOKEN_PATH.exists():
        creds = pickle.loads(TOKEN_PATH.read_bytes())
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)

            # OLD → creds = flow.run_console()
            # NEW ↓  opens a browser automatically on an ephemeral port
            creds = flow.run_local_server(port=0, prompt="consent")

        TOKEN_PATH.write_bytes(pickle.dumps(creds))

    return googleapiclient.discovery.build("youtube", "v3", credentials=creds)
