from flask import Blueprint, request, jsonify
from src.extract import extract_text_from_pdf
from src.gemini import analyze_contract_text
from src.analysis import clean_analysis, format_analysis_for_layman

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        pdf_file = request.files['file']
        if not pdf_file.filename.lower().endswith('.pdf'):
            return jsonify({"error": "Only PDF files are supported"}), 400

        text = extract_text_from_pdf(pdf_file)
        raw_output = analyze_contract_text(text)
        cleaned = clean_analysis(raw_output)
        layman = format_analysis_for_layman(cleaned)

        return jsonify({"result_json": cleaned, "result_text": layman}), 200

    except Exception as e:
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500
