import io
import os
import pickle

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

service = None


def authenticate():
    global service

    if service:
        return service

    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:

        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials/credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("drive", "v3", credentials=creds)

    return service


def list_files(folder_id):

    service = authenticate()

    query = f"'{folder_id}' in parents"
    # query = f"""
    #     '{folder_id}' in parents and
    #     (mimeType='application/pdf' or
    #     mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document' or
    #     mimeType='text/plain')
    #     """

    results = service.files().list(
        q=query,
        fields="files(id,name,mimeType)"
    ).execute()

    return results.get("files", [])


def download_file(file_id, filename, mimeType):

    service = authenticate()

    os.makedirs("downloads", exist_ok=True)

    if mimeType == "application/vnd.google-apps.document":

        request = service.files().export_media(
            fileId=file_id,
            mimeType="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        filename += ".docx"

    else:
        request = service.files().get_media(fileId=file_id)

    filepath = os.path.join("downloads", filename)

    fh = io.FileIO(filepath, "wb")

    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    return filepath