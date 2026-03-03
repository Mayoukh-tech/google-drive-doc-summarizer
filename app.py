from flask import Flask, render_template, send_file
from google_drive import list_files, download_file
from parser import extract_text
from summarizer import summarize
from report_generator import generate_csv, generate_pdf

app = Flask(__name__)

FOLDER_ID = "14r8sHj3wjqZyLszS0Yo66lpUEQHS3Hjg"


@app.route("/")
def index():

    files = list_files(FOLDER_ID)
    print("FILES FROM DRIVE:", files)

    results = []

    for file in files:

        name = file["name"]
        file_id = file["id"]
        mime = file["mimeType"]

        path = download_file(file_id, name, mime)

        text = extract_text(path)

        summary = summarize(text)

        link = f"https://drive.google.com/file/d/{file_id}/view"

        results.append({
            "name": name,
            "summary": summary,
            "link": link
        })

    generate_csv(results)
    generate_pdf(results)

    return render_template("index.html", files=results)


@app.route("/download_csv")
def download_csv():
    return send_file("summary_report.csv", as_attachment=True)


@app.route("/download_pdf")
def download_pdf():
    return send_file("summary_report.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)