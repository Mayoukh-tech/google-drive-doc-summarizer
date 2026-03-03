# Drive Document Summarizer

A Flask app that reads files from a Google Drive folder, extracts text, summarizes each file with Gemini, and generates downloadable CSV/PDF reports.

## Prerequisites

- Python 3.10+
- A Google AI Studio API key (Gemini)
- Google Drive OAuth client credentials (`credentials.json`)

## Project Setup

1. Clone the repository and move into it.

```bash
git clone <repo-url>
cd Drve_Doc_Summarizer
```

2. Create and activate a virtual environment.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Add Gemini API key in `.env`.

```env
GOOGLE_API_KEY= api_key_here
```

5. Add Google Drive OAuth credentials.

- Create a folder named `credentials` in the project root (if not present).
- Download OAuth client file from Google Cloud Console.
- Place it at: `credentials/credentials.json`

6. Set target Drive folder ID in `app.py`.

```python
FOLDER_ID = "google_drive_folder_id"
```

## Run the App

```bash
python app.py
```

Open: `http://127.0.0.1:5000`

On first run, Google OAuth login opens in browser and creates `token.pickle`.

## Output Files

After processing, the app generates:

- `summary_report.csv`
- `summary_report.pdf`
- Downloaded originals in `downloads/`

## Notes

- Supported file types: `.pdf`, `.docx`, `.txt`
- Make sure the authenticated Google account has access to the Drive folder.
