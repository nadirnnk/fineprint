import os

class Config:
    # You can extend this to load from .env or other sources
    GEMINI_API_KEY = os.getenv("Fineprint")
    GEMINI_MODEL = "gemini-2.5-flash"
