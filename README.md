# Google Drive Document Summarizer

A Flask-based web application that retrieves files from a Google Drive
folder, extracts their content, generates summaries, and displays them
in a web interface. The summaries can also be downloaded as CSV or PDF
reports.

------------------------------------------------------------------------

## Features

-   Fetch files directly from a Google Drive folder
-   Supports:
    -   Google Docs
    -   Images
-   Extracts text from documents
-   Generates summaries automatically
-   Displays results in a clean HTML table
-   Downloadable reports:
    -   CSV
    -   PDF (with clickable links)
-   Simple Flask web interface

------------------------------------------------------------------------

## Project Structure

Drive_Doc_Summarizer │ ├── app.py ├── google_drive.py ├── parser.py ├──
summarizer.py ├── report_generator.py │ ├── templates │ └── index.html │
├── downloads ├── requirements.txt └── README.md

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

git clone https://github.com/yourusername/drive-doc-summarizer.git cd
drive-doc-summarizer

### 2. Create a virtual environment

python -m venv .venv

Activate it

Windows: .venv`\Scripts`{=tex}`\activate`{=tex}

Mac/Linux: source .venv/bin/activate

------------------------------------------------------------------------

### 3. Install dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## Google Drive API Setup

1.  Go to Google Cloud Console
2.  Create a new project
3.  Enable the Google Drive API
4.  Create OAuth credentials
5.  Download credentials.json
6.  Place it in the project root

Example:

Drive_Doc_Summarizer │ ├── credentials.json

------------------------------------------------------------------------

## Configure Google Drive Folder

Inside app.py set your folder ID:

FOLDER_ID = "YOUR_GOOGLE_DRIVE_FOLDER_ID"

Example Drive folder link:

https://drive.google.com/drive/folders/FOLDER_ID

------------------------------------------------------------------------

## Run the Application

python app.py

Open in browser:

http://127.0.0.1:5000

------------------------------------------------------------------------

## Download Reports

The application generates:

-   summary_report.csv → CSV report of summaries
-   summary_report.pdf → PDF report with clickable links

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Flask
-   Google Drive API
-   ReportLab
-   HTML/CSS
-   CSV module

------------------------------------------------------------------------

## Security Note

Do not upload these files to GitHub:

credentials.json token.json .venv summary_report.csv summary_report.pdf

These should be included in .gitignore.

------------------------------------------------------------------------

## Future Improvements

-   AI powered summarization
-   Support for PDFs
-   Better UI
-   Background processing
-   Search and filtering

------------------------------------------------------------------------

## Author

Flask + Google Drive API project for automated document summarization.
