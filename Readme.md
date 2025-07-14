# Contract Analyzer MVP

A simple Flask app that:
- Accepts a PDF file upload
- Extracts text from the PDF
- Sends the text to Google Gemini for contract analysis
- Parses and returns structured results and a layman summary

## 📦 How to run locally

1. Install dependencies  
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
