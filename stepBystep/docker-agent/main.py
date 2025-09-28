from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="StyleMyStudy - Step-by-Step Agent")

class InputPayload(BaseModel):
    topic: str
    subject: str

@app.post("/process")
async def process_input(payload: InputPayload):
    topic = payload.topic
    subject = payload.subject.lower()

    steps = []

    if subject == "physics":
        steps = [
            "Step 1: Identify the force acting on the object (gravity).",
            "Step 2: Understand that gravity accelerates all objects equally.",
            "Step 3: Ignore air resistance for this explanation.",
            "Step 4: Conclude that all objects fall at the same rate regardless of mass."
        ]
    elif subject == "math":
        steps = [
            "Step 1: Write down the problem clearly.",
            "Step 2: Identify known variables and unknowns.",
            "Step 3: Apply the appropriate formula or rule.",
            "Step 4: Simplify and calculate step by step.",
            "Step 5: Verify your final answer."
        ]
    elif subject == "coding":
        steps = [
            "Step 1: Define the problem clearly.",
            "Step 2: Break the problem into smaller parts (functions or modules).",
            "Step 3: Write code for each part with clear logic.",
            "Step 4: Test each part individually.",
            "Step 5: Combine and run the full program."
        ]
    elif subject == "biology":
        steps = [
            "Step 1: Identify the biological concept (e.g., cell structure).",
            "Step 2: Break it into components (nucleus, mitochondria, etc.).",
            "Step 3: Describe the role of each part.",
            "Step 4: Show how the parts work together in the organism."
        ]
    else:
        steps = [
            "Step 1: Understand the topic.",
            "Step 2: Break it into smaller ideas.",
            "Step 3: Explain each idea simply.",
            "Step 4: Put it all together for the big picture."
        ]

    return {
        "status": "ok",
        "style": "step-by-step",
        "topic": topic,
        "subject": subject,
        "steps": steps
    }

# ✅ Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "StyleMyStudy Step-by-Step Agent"}
