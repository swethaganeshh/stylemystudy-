from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="StyleMyStudy - Analogy Agent")

class InputPayload(BaseModel):
    topic: str
    subject: str

@app.post("/process")
async def process_input(payload: InputPayload):
    topic = payload.topic
    subject = payload.subject.lower()

    analogy_response = ""

    if subject == "physics":
        analogy_response = (
            f"Think of {topic} like comparing different cars going down a hill — "
            "no matter their size, they roll at the same pace if friction and air resistance are ignored."
        )
    elif subject == "math":
        analogy_response = (
            f"{topic} is like baking a cake — you follow step-by-step instructions (formulas), "
            "and the outcome is predictable if you do it correctly."
        )
    elif subject == "coding":
        analogy_response = (
            f"{topic} is like teaching someone a recipe — you give clear instructions (code), "
            "and the computer follows them exactly."
        )
    elif subject == "biology":
        analogy_response = (
            f"{topic} is like a city — cells are buildings, DNA is the blueprint, "
            "and proteins are the workers keeping everything running."
        )
    else:
        analogy_response = (
            f"{topic} can be understood by relating it to everyday experiences. "
            "Think of it in simpler terms you already know."
        )

    return {
        "status": "ok",
        "style": "analogy",
        "topic": topic,
        "subject": subject,
        "analogy": analogy_response
    }

# ✅ Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "StyleMyStudy Analogy Agent"}
