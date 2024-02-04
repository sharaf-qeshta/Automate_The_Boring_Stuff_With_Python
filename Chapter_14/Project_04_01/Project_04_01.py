"""
Downloading Google Forms Data
Google Forms allows you to create simple online forms that make it easy
to collect information from people. The information they enter into the
form is stored in a Google Sheet. For this project, write a program that can
automatically download the form information that users have submitted.
Go to https://docs.google.com/forms/ and start a new form; it will be blank.
Add fields to the form that ask the user for a name and email address. Then
click the Send button in the upper right to get a link to your new form,
such as https://goo.gl/forms/QZsq5sC2Qe4fYO592/. Try to enter a few example
responses into this form.
On the “Responses” tab of your form, click the green Create
Spreadsheet button to create a Google Sheets spreadsheet that will hold the
responses that users submit. You should see your example responses in the
first rows of this spreadsheet. Then write a Python script using EZSheets to
collect a list of the email addresses on this spreadsheet.


@author Sharaf Qeshta
"""

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1L-cLedr3O0r09w9WjpjAxSQXl6Ejq8SaQbW2KWPUoJE"

def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        emails = []
        index = 2
        current_email = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="C2:C2").execute()
        while len(current_email) > 2:
            index += 1
            emails.append(current_email.get("values")[0][0])
            current_email = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"C{index}:C{index}").execute()

        print(emails)
    except HttpError as error:
        print(error)

main()