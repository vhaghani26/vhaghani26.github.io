#!/bin/bash python3 

'''
python3 generate_pdf.py
'''

import requests
from bs4 import BeautifulSoup
import pdfkit
from datetime import datetime

# URL of the page to convert
url = 'https://vhaghani26.github.io/#cv'

# Get the content of the page
response = requests.get(url)
response.raise_for_status() 

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract relevant parts (e.g., main content)
main_content = soup.find('body') 

# Create a clean HTML document
html = f"""
<html>
<head><meta charset='utf-8'></head>
<body>
{main_content.prettify()}
</body>
</html>
"""

# Output to PDF
filename = f"{datetime.now().strftime('%Y-%m-%d')}_CV.pdf"

# Output to PDF
pdfkit.from_string(html, filename)

print(f"PDF created as '{filename}'")