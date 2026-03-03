import csv
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_csv(results):

    with open("summary_report.csv", "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["File Name", "Summary", "Link"])

        for r in results:
            writer.writerow([r["name"], r["summary"], r["link"]])


def generate_pdf(results):

    styles = getSampleStyleSheet()

    data = [["File Name", "Summary", "Link"]]

    for r in results:

        clickable_link = f'<a href="{r["link"]}">Open File</a>'

        data.append([
            Paragraph(r["name"], styles["Normal"]),
            Paragraph(r["summary"], styles["Normal"]),
            Paragraph(clickable_link, styles["Normal"])
        ])

    pdf = SimpleDocTemplate("summary_report.pdf", pagesize=letter)

    table = Table(data, colWidths=[150, 300, 150])

    table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("VALIGN", (0,0), (-1,-1), "TOP")
    ]))

    pdf.build([table])