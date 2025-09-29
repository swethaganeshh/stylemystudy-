# 📚 StyleMyStudy – Personalized AI Learning Assistant  

## 🚀 Problem Statement  
Traditional study material often fails to adapt to diverse learning styles:  
- Some learners prefer **stories**, others need **analogies**, **step-by-step guides**, or even **visual diagrams**.  
- **Language barriers** and lack of contextual knowledge make learning harder.  

---

## 💡 Solution  
**StyleMyStudy** is a **multi-agent AI system** built with **Maestro** that adapts explanations into multiple styles:  

- 📝 **Input Agent** → Validates queries & detects subject.  
- 📖 **Storytelling Agent** → Narratives and real-life stories.  
- 🔗 **Analogy Agent** → Metaphors & comparisons.  
- 📑 **Step-by-Step Agent** → Sequential breakdowns.  
- 🌍 **Knowledge Agent** → Extra facts & enrichment.  
- 🌐 **Translation Agent** → Explanations in multiple languages.  
- 🎨 **Visualization Agent** → Diagrams & flowcharts.  

---

## 🏗️ Architecture  
- **Framework:** Maestro (multi-agent orchestration)  
- **Agents:** Each agent is an independent microservice  
- **Deployment:** Google Cloud Run  

```mermaid
flowchart TD
    A[User Query] --> B[Input Agent]
    B --> C[Storytelling Agent]
    B --> D[Analogy Agent]
    B --> E[Step-by-Step Agent]
    B --> F[Knowledge Agent]
    B --> G[Translation Agent]
    B --> H[Visualization Agent]
    C & D & E & F & G & H --> I[Personalized Explanation]




1️⃣ Input Agent

Purpose: Collects input, validates clarity, detects subject.

POST /process

{ "topic": "Why do objects fall at the same rate?" }


GET /health → Health check

Deployed URL:
https://maestro-cc8cc268-be67-4eaa-aca8-397ce6b2524f-zcaxlbuauq-uc.a.run.app

2️⃣ Storytelling Agent

Purpose: Explains using narratives & real-life scenarios.

POST /process

{ "topic": "Gravity", "subject": "physics" }


GET /health

3️⃣ Analogy Agent

Purpose: Explains using metaphors & analogies.

POST /process

{ "topic": "Equations", "subject": "math" }


GET /health

4️⃣ Step-by-Step Agent

Purpose: Provides structured, sequential explanations.

POST /process

{ "topic": "Loops", "subject": "coding" }


GET /health

5️⃣ Knowledge Agent

Purpose: Enriches explanation with extra facts.

POST /process

{ "topic": "Gravity" }


GET /health

6️⃣ Translation Agent

Purpose: Translates text into the learner’s preferred language.

POST /process

{
  "text": "Objects fall at the same rate regardless of mass.",
  "target_language": "es"
}


GET /health

7️⃣ Visualization Agent

Purpose: Generates diagrams & flowcharts.

POST /process

{
  "topic": "Free Fall",
  "steps": [
    "Step 1: Object starts at rest",
    "Step 2: Gravity pulls downward",
    "Step 3: Acceleration increases",
    "Step 4: Object reaches the ground"
  ]
}


GET /health

🧪 Testing the Agents
✅ Health Check (any agent)
curl https://<agent-url>/health


Response:

{ "status": "healthy", "service": "StyleMyStudy <Agent>" }

📖 Example: Storytelling Agent
curl -X POST https://<storytelling-agent-url>/process \
-H "Content-Type: application/json" \
-d '{"topic":"Gravity","subject":"physics"}'


Response:

{
  "status": "ok",
  "style": "storytelling",
  "topic": "Gravity",
  "explanation": "Once upon a time, an apple fell from a tree..."
}

🛠️ Tech Stack

Framework: Maestro (Multi-agent orchestration)

Backend: Python (FastAPI)

Deployment: Google Cloud Run

Visualization: Mermaid (Flowcharts & Diagrams)

🔮 Future Enhancements

Personalized learning profiles

LMS integration

Offline support for low-connectivity environments
