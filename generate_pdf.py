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
    
    # Convert the HTML to PDF
    filename = f"{datetime.now().strftime('%Y-%m-%d')}_CV.pdf"
    pdfkit.from_string(cv_html, filename)  # Use cv_html instead of html
    
    print("CV tab saved as PDF.")
else:
    print("CV tab not found.")