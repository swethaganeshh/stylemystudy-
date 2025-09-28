from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI(title="StyleMyStudy - Input Agent")

class InputPayload(BaseModel):
    topic: str

def detect_subject(text: str) -> str:
    text_lower = text.lower()
    if any(word in text_lower for word in ["equation", "algebra", "math", "geometry"]):
        return "math"
    elif any(word in text_lower for word in ["gravity", "atom", "force", "physics"]):
        return "physics"
    elif any(word in text_lower for word in ["code", "python", "programming", "loop"]):
        return "coding"
    elif any(word in text_lower for word in ["cell", "biology", "dna", "organism"]):
        return "biology"
    else:
        return "general"

def is_clear(text: str) -> bool:
    # Check for vague inputs
    return len(text.split()) > 2 and not re.match(r"^[\?\.\!]*$", text)

@app.post("/process")
async def process_input(payload: InputPayload):
    topic = payload.topic.strip()
    subject = detect_subject(topic)
    clarity = is_clear(topic)

    if not clarity:
        return {
            "status": "error",
            "message": "Your query seems unclear. Try asking a full question or topic."
        }

    return {
        "status": "ok",
        "topic": topic,
        "subject": subject,
        "clarity": clarity
    }

# ✅ Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "StyleMyStudy Input Agent"}
