from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Import service account OAuth2
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Spreadshet ID: API_YAPE_SENCI
SAMPLE_SPREADSHEET_ID = '15s0iFAmgE3yegdEB9XL7Er3F06AU3ZvqFKVIbj0pWUs'

def main():

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="mensajes!A1:D14").execute()
        print(result)
        values = result.get('values', [])

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()