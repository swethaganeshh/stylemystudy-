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
