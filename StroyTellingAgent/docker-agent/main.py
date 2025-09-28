from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="StyleMyStudy - Storytelling Agent")

# Request schema
class StoryPayload(BaseModel):
    topic: str
    subject: str

# Simple storytelling generator (mock version)
def generate_story(topic: str, subject: str) -> str:
    if subject == "physics":
        return (
            f"Once upon a time, a curious child dropped an apple from a tree while "
            f"watching the moon. This made them wonder: {topic}. "
            f"Just like the apple falls due to Earth's pull, the moon is kept in orbit by gravity!"
        )
    elif subject == "math":
        return (
            f"Imagine you're building a tower with blocks. Each block represents a number, "
            f"and stacking them in patterns helps explain {topic}. "
            f"Math is like telling stories with numbers and shapes."
        )
    elif subject == "coding":
        return (
            f"Picture a chef following a recipe. Each line of code is like a step in cooking, "
            f"and if followed carefully, it explains {topic}. "
            f"Coding is the recipe book for computers."
        )
    else:
        return (
            f"Here’s a story: Imagine a traveler who asks endless questions about the world. "
            f"One day, they wondered about {topic}, and by exploring, they found the answer. "
            f"Learning is just another adventure!"
        )

@app.post("/process")
async def storytelling_agent(payload: StoryPayload):
    story = generate_story(payload.topic, payload.subject)
    return {
        "status": "ok",
        "mode": "storytelling",
        "topic": payload.topic,
        "subject": payload.subject,
        "explanation": story
    }

# ✅ Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "StyleMyStudy Storytelling Agent"}
