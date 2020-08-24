"""Handle session management for connections to the google photos library."""

import os
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow  # pylint: disable=import-error
from googleapiclient.discovery import build, Resource  # pylint: disable=import-error

_SCOPES = [
    "https://www.googleapis.com/auth/photoslibrary.readonly",
    "https://www.googleapis.com/auth/photoslibrary.sharing",
]


class SessionManager:
    """Local object to keep track of the session with google photos library."""

    def __init__(self, secrets_file: str, credentials_file: str) -> None:
        """Initialize Session Manager.

        :param secrets_file:      Google app credentials (See README)
        :param credentials_file:  Local storage file for session credentials
        """
        self._secrets_file = secrets_file
        self._credentials_file = credentials_file

    def client(self) -> Resource:
        """Start a session with google photos library."""
        return build("photoslibrary", "v1", credentials=self._credentials())

    def _credentials(self) -> Credentials:
        """Get the necessary credentials for a session.

        If valid credentials are not stored locally in the credentials file, create new credentials.
        """
        credentials = None
        if os.path.exists(self._credentials_file):
            with open(self._credentials_file, "rb") as token_file:
                credentials = pickle.load(token_file)

        if credentials is None or not credentials.valid:
            if credentials is not None and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self._secrets_file, _SCOPES)
                credentials = flow.run_local_server(port=0)

            with open(self._credentials_file, "wb") as token_file:
                pickle.dump(credentials, token_file)
        return credentials
