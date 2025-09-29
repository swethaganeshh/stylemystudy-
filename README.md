# 📚 StyleMyStudy – Personalized AI Learning Assistant  

## 🚀 Problem Statement  
Traditional study material often fails to adapt to diverse learning styles:  
- Some learners prefer **stories**, others need **analogies**, **step-by-step guides**, or even **visual diagrams**.  
- **Language barriers** and lack of contextual knowledge make learning harder.  

---
#MAESTRO AGENT

### 1️⃣ Input Agent  

**Purpose**  
Collects learner queries, validates clarity, and detects the subject to route the request to appropriate agents.  

---

**Endpoints**  

- **POST** `/process`  
Request Body:  
```json
{ "topic": "Why do objects fall at the same rate?" }
```
Deployed Url - [https://maestro-cc8cc268-be67-4eaa-aca8-397ce6b2524f-zcaxlbuauq-uc.a.run.app](https://maestro-cc8cc268-be67-4eaa-aca8-397ce6b2524f-zcaxlbuauq-uc.a.run.app/)

---
### Storytelling Agent

**Purpose**  
Explains concepts using narratives & real-life scenarios.
---

**Endpoints**  

- **POST** `/process`  
Request Body:  
```json
{ "topic": "Gravity", "subject": "physics" }
```
Deployed Url -[ https://maestro-cc8cc268-be67-4eaa-aca8-397ce6b2524f-zcaxlbuauq-uc.a.run.app](https://maestro-cc8cc268-be67-4eaa-aca8-397ce6b2524f-zcaxlbuauq-uc.a.run.app/health)

---
###Analogy Agent

**Purpose**  
Explains concepts using metaphors & analogies.
---

**Endpoints**  

- **POST** `/process`  
Request Body:  
```json
{ "topic": "Equations", "subject": "math" }
```
Deployed Url - https://maestro-cc8cc268-be67-4eaa-aca8-397ce6b2524f-zcaxlbuauq-uc.a.run.app/health
---
###Step-by-Step Agent

**Purpose**  
Provides structured, sequential explanations.
---

**Endpoints**  

- **POST** `/process`  
Request Body:  
```json
{ "topic": "Loops", "subject": "coding" }
```
Deployed Url -https://maestro-cc8cc268-be67-4eaa-aca8-397ce6b2524f-zcaxlbuauq-uc.a.run.app/
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

