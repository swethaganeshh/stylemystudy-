from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI(title="StyleMyStudy - Translation Agent")
translator = Translator()

class InputPayload(BaseModel):
    text: str
    target_language: str  # e.g., "es" for Spanish, "fr" for French, "ta" for Tamil

@app.post("/process")
async def process_input(payload: InputPayload):
    translated = translator.translate(payload.text, dest=payload.target_language)

    return {
        "status": "ok",
        "style": "translation",
        "original_text": payload.text,
        "translated_text": translated.text,
        "target_language": payload.target_language
    }

# ✅ Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "StyleMyStudy Translation Agent"}
