import pdfkit
import os

def generate_pdf(itinerary_text, destination):
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            h1 {{ color: #2E86C1; }}
            pre {{ white-space: pre-wrap; word-wrap: break-word; }}
            iframe {{ width: 100%; height: 300px; border: none; }}
        </style>
    </head>
    <body>
        <h1>Travel Itinerary: {destination}</h1>
        <iframe src="https://www.google.com/maps?q={destination}&output=embed"></iframe>
        <pre>{itinerary_text}</pre>
    </body>
    </html>
    """
    filename = f"itinerary_{destination.replace(' ', '_').lower()}.pdf"
    pdfkit.from_string(html, filename)
    return filename
