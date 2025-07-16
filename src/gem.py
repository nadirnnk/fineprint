import google.generativeai as genai
from config import Config

# Configure Gemini once
genai.configure(api_key=Config.GEMINI_API_KEY)
model = genai.GenerativeModel(Config.GEMINI_MODEL)

def analyze_contract_text(text: str, temperature: float = 0.2) -> str:
    """
    Send text to Gemini with a prompt and return raw output.
    """
    prompt = """
    Assume you are a lawyer, and you are taksed to find the clauses in a contract and categorize them.
    
    Analyze this contract and extract every clause fit into this 41 categories:

    1. Document Name
    2. Parties
    3. Agreement Date
    4. Effective Date
    5. Expiration Date
    6. Renewal Term
    7. Notice to Terminate Renewal
    8. Governing Law
    9. Most Favored Nation
    10. Non-Compete
    11. Exclusivity
    12. No-Solicit of Customers
    13. Competitive Restriction Exception
    14. No-Solicit of Employees
    15. Non-Disparagement
    16. Termination for Convenience
    17. Right of First Refusal, Offer or Negotiation (ROFR/ROFO/ROFN)
    18. Change of Control
    19. Anti-Assignment
    20. Revenue/Profit Sharing
    21. Price Restriction
    22. Minimum Commitment
    23. Volume Restriction
    24. IP Ownership Assignment
    25. Joint IP Ownership
    26. License Grant
    27. Non-Transferable License
    28. Affiliate IP License-Licensor
    29. Affiliate IP License-Licensee
    30. Unlimited/All-You-Can-Eat License
    31. Irrevocable or Perpetual License
    32. Source Code Escrow
    33. Post-Termination Services
    34. Audit Rights
    35. Uncapped Liability
    36. Cap on Liability
    37. Liquidated Damages
    38. Warranty Duration
    39. Insurance
    40. Covenant Not to Sue
    41. Third Party Beneficiary

    Give answer in json as:
    { 
        { 
          Category:
          Clauses:
        }....
    }

    """

    response = model.generate_content(
        prompt + text,
        generation_config={"temperature": temperature}
    )

    return response.text if hasattr(response, 'text') else str(response)


"""Analyze this contract. For each potentially unfair clause:
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