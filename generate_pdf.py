#!/bin/bash python3 

'''
python3 generate_pdf.py
'''

import pdfkit
from bs4 import BeautifulSoup
from datetime import datetime

# Load the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML and extract the CV tab
soup = BeautifulSoup(html_content, 'html.parser')
cv_tab = soup.find(id="cv") 

if cv_tab:
    # Save the CV tab as a standalone HTML
    cv_html = f"<!DOCTYPE html><html><head><title>CV</title></head><body>{cv_tab}</body></html>"

    # Define custom options for wkhtmltopdf
    options = {
        'no-outline': None,  # Disable outline
        'disable-javascript': None,  # Disable JavaScript
        'no-images': None,  # Optional: Disable images if not needed
        'page-size': 'A4',
        'disable-smart-shrinking': None,  # Disable automatic shrinking of content
        'load-error-handling': 'ignore',  # Ignore load errors
    }
    
    # Convert the HTML to PDF with the options
    filename = f"{datetime.now().strftime('%Y-%m-%d')}_CV.pdf"
    pdfkit.from_string(cv_html, filename, options=options)
    
    print("CV tab saved as PDF.")
else:
    print("CV tab not found.")
