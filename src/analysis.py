def clean_analysis(raw_text: str) -> dict:
    """
    Parses Gemini's output as contract analysis.
    """
    unfair_clauses = []
    for clause in raw_text.split("\n\n"):
        if clause.strip():
            parts = clause.strip().split("\n")
            unfair_clauses.append({
                "clause": parts[0].strip() if len(parts) > 0 else "Not specified",
                "risk": parts[1].strip() if len(parts) > 1 else "Not specified",
                "fix": parts[2].strip() if len(parts) > 2 else "Not provided"
            })
    return {
        "document_type": "contract",
        "summary": "Contract Analysis Complete",
        "unfair_clauses": unfair_clauses
    }

def format_analysis_for_layman(analysis_result: dict) -> str:
    """
    Turns JSON output into human-readable text.
    """
    output = "This document appears to be a contract.\n\n"
    if analysis_result["unfair_clauses"]:
        output += "**Potentially Problematic Clauses Identified:**\n\n"
        for i, clause in enumerate(analysis_result["unfair_clauses"]):
            output += f"--- Clause {i+1} ---\n"
            output += f"**Quoted Text:** {clause['clause']}\n"
            output += f"**Potential Risk:** {clause['risk']}\n"
            output += f"**Suggested Fix:** {clause['fix']}\n\n"
    else:
        output += "No specific unfair clauses were identified in this initial analysis.\n"
    return output
