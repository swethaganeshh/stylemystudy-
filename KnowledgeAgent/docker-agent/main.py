from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI(title="StyleMyStudy - Knowledge Agent")

class InputPayload(BaseModel):
    topic: str

@app.post("/process")
async def process_input(payload: InputPayload):
    topic = payload.topic
    summary = ""

    try:
        summary = wikipedia.summary(topic, sentences=2)
    except Exception:
        summary = f"Could not fetch extra knowledge for {topic}. Try a different query."

    return {
        "status": "ok",
        "style": "knowledge",
        "topic": topic,
        "extra_info": summary
    }

# ✅ Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "StyleMyStudy Knowledge Agent"}
