import google.generativeai as genai
from config import Config

# Configure Gemini once
genai.configure(api_key=Config.GEMINI_API_KEY)
model = genai.GenerativeModel(Config.GEMINI_MODEL)

def analyze_contract_text(text: str, temperature: float = 0.2) -> str:
    """
    Send text to Gemini with a prompt and return raw output.
    """
    prompt = """Analyze this contract. For each potentially unfair clause:
    1. [EXACT QUOTE] - Copy the full clause text
    2. [RISK] - Explain the legal/business risk (1-2 sentences)
    3. [FIX] - Suggest specific alternative wording

    Example:
    1. "Consultant may not replace staff without approval"
    2. Risk: Creates operational inflexibility if key staff leave
    3. Fix: "Consultant may replace staff with equally qualified personnel, with notice to Commission"

    Pay special attention to:
    - Termination clauses with unequal notice periods
    - Overly broad indemnification language
    - Intellectual property ownership clauses
    - Insurance requirements that may be excessive
    """

    response = model.generate_content(
        prompt + text,
        generation_config={"temperature": temperature}
    )

    return response.text if hasattr(response, 'text') else str(response)
