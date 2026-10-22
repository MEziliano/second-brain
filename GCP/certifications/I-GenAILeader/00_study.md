# Google Cloud Generative AI Study Guide

**Goal:** Pass the Google Cloud Generative AI certification / leadership evaluation.

**Background:** Data Scientist focused on supervised learning / Total beginner in GCP GenAI.

**Schedule:** 4 hours per day, Monday through Saturday (24 hours/week).

---

## 1. Territory Map (Overview)

```
MODULE 1 ──► MODULE 2 ──► MODULE 3 ──► MODULE 4
GenAI         Vertex AI    Prompt Eng.,   Responsible AI,
Fundamentals  Architecture RAG &          Governance &
& GCP         & Apps       Agents         Business Strategy

```

| Module | Module Name | Learning Objective | Interdependence |
| --- | --- | --- | --- |
| **Module 1** | **GenAI Fundamentals & Google Cloud Ecosystem** | Differentiate traditional ML from Generative AI, understand Transformer architecture, attention, embeddings, and identify GCP's model portfolio (Gemini family, Imagen, Codey, Chirp). | *Required foundational knowledge.* |
| **Module 2** | **Practical Applications & Solution Architecture on Vertex AI** | Navigate Vertex AI Studio, leverage Model Garden, evaluate model selection scenarios, and understand adaptation strategies (Prompting vs. Tuning vs. RAG). | *Requires Module 1 (model understanding).* |
| **Module 3** | **Prompt Engineering, RAG & Autonomous Agents** | Design semantic search systems (Vector Search), implement RAG architectures with enterprise grounding, and design intelligent agent workflows using Vertex AI Agent Builder. | *Requires Modules 1 and 2.* |
| **Module 4** | **Responsible AI, Governance, Costs & Business Strategy** | Evaluate hallucination mitigations, bias, enterprise data privacy (GCP data governance), ROI, FinOps for GenAI, and use case prioritization criteria. | *Integrative module (requires Modules 1, 2, and 3).* |

---

## 2. Curated Resources (Where to Learn)

### **Module 1: GenAI Fundamentals & GCP Ecosystem**

* **Official/Technical Source:** Technical Whitepaper: *Attention Is All You Need* (Vaswani et al.) and Official Documentation: *Google Cloud Generative AI Overview*.
* **Conceptual/Educational Source:** Official Google Cloud Courses/Videos: *Introduction to Generative AI* and *Large Language Models Overview* on Google Cloud Skills Boost / YouTube.
* **Practical Source:** Qwiklabs Hands-on Lab: *Generative AI - Language Processing with Vertex AI Getting Started*.

### **Module 2: Vertex AI Applications & Architecture**

* **Official/Technical Source:** Google Cloud Architectural Guide: *Generative AI Architecture Framework* and *Vertex AI Model Garden Documentation*.
* **Conceptual/Educational Source:** Technical blog posts and video series on Google Cloud Blog: *Choosing the right GenAI model for your enterprise workload*.
* **Practical Source:** Qwiklabs Hands-on Lab: *Vertex AI Studio: Prompt Design and Multimodal Prompts with Gemini*.

### **Module 3: Prompts, RAG & Agents**

* **Official/Technical Source:** Technical Documentation: *Vertex AI Vector Search*, *Grounding with Google Search/Enterprise Data*, and *Vertex AI Agent Builder Overview*.
* **Conceptual/Educational Source:** Medium / Google Cloud Blog articles: *RAG Architecture Patterns on GCP* and *Building conversational agents with Gemini*.
* **Practical Source:** Official GitHub Repository: `GoogleCloudPlatform/generative-ai` (specifically the directories covering RAG, Vector Search, and Agent Builder).

### **Module 4: Governance, Costs & Strategy**

* **Official/Technical Source:** Official Policy Guides: *Google’s Responsible AI Practices* and *Data Privacy for Generative AI on Vertex AI*.
* **Conceptual/Educational Source:** McKinsey / Google Frameworks: *Measuring ROI and Business Value in Enterprise GenAI Projects*.
* **Practical Source:** Hands-on Exercise: Building a Governance and Risk Assessment Matrix for an enterprise GenAI project.

---

## 3. Weekly Active Roadmap (4-Week Schedule)

With 24 hours per week available, the goal is to convert strategic and technical theory into **practical, documented artifacts in your GitHub repository**.

### **Week 1: GenAI Fundamentals and the GCP Portfolio**

* **Main Focus:** Structural differences between Traditional ML and GenAI, mechanics of Transformers/Embeddings, and mapping Google's model portfolio (Gemini Flash vs. Pro vs. Ultra, Imagen, etc.).
* **Mandatory Practical Task (GitHub):**
* Create a repository named `gcp-genai-leader-guide`.
* Write a Markdown-based **Model Comparison Matrix**, detailing model type, context window size, modality (text, image, audio, video), latency, relative cost, and ideal business use cases.


* **Completion Signal:** Can you explain in detail why a generative model should not be used for tasks requiring strict determinism, and how the context window impacts solution architecture?

### **Week 2: Vertex AI, Prompt Engineering, and Adaptation Strategies**

* **Main Focus:** Prompting patterns (Zero-shot, Few-shot, Chain-of-Thought, ReAct), inference parameters (Temperature, Top-K, Top-P), and deciding between Prompting, Fine-Tuning, PEFT (LoRA), and RAG.
* **Mandatory Practical Task (GitHub):**
* Design an **Architectural Decision Tree**: *"When to use Prompt Engineering, RAG, or Fine-Tuning?"*.
* Document an *Enterprise Prompt Engineering Playbook* containing 5 structured prompt templates using System Instruction + Context + Few-Shot Examples + Output Format.


* **Completion Signal:** Can you immediately identify which parameter to adjust when a model produces overly repetitive answers versus overly random/creative ones?

### **Week 3: RAG, Vector Search, and Agents (Vertex AI Agent Builder)**

* **Main Focus:** RAG Architecture (Chunking, Embeddings, Vector Databases, Retrieval, Generation), Grounding to eliminate hallucinations, and Autonomous Agents with tool extension (Tool Use / Function Calling).
* **Mandatory Practical Task (GitHub):**
* Draw an architectural diagram (using Mermaid.js or Excalidraw) for a **Customer Support Virtual Assistant using RAG and Agents on GCP**.
* Specify each component: PDF ingestion into Cloud Storage, vectorization in Vertex AI Vector Search, orchestration with Gemini, and grounding checks.


* **Completion Signal:** Can you explain to a C-level executive exactly how RAG prevents proprietary data leaks and addresses LLM hallucinations?

### **Week 4: Responsible AI, Governance, FinOps & Leadership Simulation**

* **Main Focus:** Google's 7 AI Principles, customer data isolation (customer data never trains the base model), GenAI cost estimation (input/output tokens), and use case prioritization by Feasibility vs. Value.
* **Mandatory Practical Task (GitHub):**
* Build a **GenAI Project Evaluation Framework**: a spreadsheet/checklist covering security, privacy, ROI, token cost, and ethical risk criteria to approve or reject enterprise AI initiatives.


* **Completion Signal:** Score over **85% on a comprehensive GenAI leadership practice exam**, justifying every choice based on GCP principles.

---

## 4. Retention Strategy (How Not to Forget)

### **1. Spaced Repetition Techniques:**

* **Socratic Teach-Back Method:** At the end of each study day, record a 3-minute audio explaining a strategic question (e.g., *"Why shouldn't an enterprise train an LLM from scratch for standard use cases?"*).
* **Architectural Mind Maps:** Sketch the connections between products (e.g., *Cloud Storage -> Vertex AI Search -> Gemini API -> Client App*) every 3 days to consolidate data flows.
* **Use Case Decision Journal:** Keep a running log of hypothetical enterprise scenarios and document the correct GCP solution along with your rationale.

### **2. Flashcards vs. GitHub Projects:**

| Flashcards (Anki / Quick Recall) | GitHub Projects (Portfolio / Active Learning) |
| --- | --- |
| Definitions of Temperature, Top-K, Top-P, and Safety Settings. | **Project 1:** Comparative Guide to the GCP Model Portfolio. |
| Concepts of Tokens, Context Window, and Rate Limits. | **Project 2:** Prompt Engineering Playbook & Decision Tree (RAG vs. Tuning). |
| Google’s 7 Responsible AI Principles. | **Project 3:** Architecture Diagram: RAG + Autonomous Agents with Vertex AI. |
| Data Privacy and Security Guarantees in Vertex AI. | **Project 4:** Executive Framework for Governance, ROI, and FinOps in GenAI. |

### **3. Fire Tests (Unassisted Practical Assessments):**

* **Fire Test 1 (End of Week 2):** Given a business scenario (e.g., a hospital network wanting to analyze medical reports with AI), build a complete architecture proposal in 30 minutes without notes, detailing model selection, adaptation technique, and privacy requirements.
* **Fire Test 2 (End of Week 4):** Take a full 50-question practice exam on GenAI leadership under real exam conditions (timed at 60 minutes) aiming for an 85%+ score.

---

## 5. Common Beginner Pitfalls

1. **Confusing Traditional Software/ML Engineering with GenAI Projects:**
* *How to avoid:* Traditional ML trains supervised models for fixed numerical or categorical outputs. GenAI is about **orchestrating and guiding massive pre-trained models** via prompts, context, and external tools. Focus on integration architecture and context quality.


2. **Assuming RAG and Fine-Tuning Serve the Same Purpose:**
* *How to avoid:* Remember this golden rule: **RAG provides updated knowledge and specific/private data** (*where the information is*). **Fine-Tuning alters the style, format, or behavior of the model** (*how it responds*).


3. **Ignoring FinOps, Costs, and Security/Privacy Risks:**
* *How to avoid:* Generative models charge per **million tokens** (input and output). In exams and real life, the correct answer almost always prioritizes the most cost-effective approach (e.g., using a smaller model like Gemini Flash with RAG before attempting fine-tuning or custom training).
