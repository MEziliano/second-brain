# Introduction

The "Introduction to AI and Machine Learning on Google Cloud" course simplifies complex AI and machine learning concepts for all skill levels. It covers AI foundations, generative AI (including Gemini, Veo, and Imagen), and the development of autonomous AI agents. Participants learn the complete development workflow, ranging from no-code solutions to code-based approaches using Vertex AI and BigQuery ML.

# Use case
01. A use case
02. AI on Google Cloud
03. AI Infrasctructure
04. AI Models
05. BigQuery ML
06. Summary 

> "AI is shifting from a tool for efficiency to a powerhouse of innovation",

Module 1, "AI Foundations," introduces how Google Cloud addresses real-world business challenges through a comprehensive architecture ranging from infrastructure to AI-powered applications. Using the "Coffee on Wheels" case study, the module demonstrates how AI and machine learning can optimize operations by:

* Solving Complex Challenges: Applying predictive AI for location and route optimization, sales forecasting, and real-time monitoring.

* Driving Innovation: Using generative AI to automate marketing campaigns, generate content, and create operational reports.

* Integrating Technologies: Leveraging tools like BigQuery for analytics, Vertex AI for model development, and Gemini for multimodal data processing.

* Providing Practical Experience: Offering hands-on labs where participants build ML models and use AI code assistants to debug and generate code.

# AI On Google Cloud
Google supports your AI journey by providing a robust architecture built on three layers:

AI Infrastructure: The foundational layer featuring advanced compute, network, and storage technologies.

Development Layer: Centered on Vertex AI, an end-to-end platform that integrates with data products like BigQuery to guide users from design to deployment.

Applications and Solutions: Out-of-the-box options designed for business users and analysts to rapidly prototype ideas.

To maximize effectiveness, Google distinguishes between two primary types of AI based on your business needs:

|**AI Type**| **Function**| **Best For**|
|--------| -------| --------| 
|**Predictive AI**|Analyzes existing data to classify information or forecast outcomes.|Forecasting, predictions, and identifying customer segments.|
|**Generative AI**|Creates new content (text, images, video) and takes action.|Multimodal content generation and automation.|

The most powerful results often come from combining both, such as using predictive AI to identify customer segments and generative AI to create personalized marketing content for them. Google underscores this approach with a commitment to responsible AI development, innovation, and collaboration.

# AI Infrasctructure
Google Cloud’s AI infrastructure is organized into three distinct layers, providing a scalable, efficient foundation for AI development.

### The Three-Layer Infrastructure
* **Networking and Security**: The base layer that supports all applications and infrastructure.

* **Compute and Storage**: These are decoupled to allow independent scaling.

* **Compute**: Google offers various services, ranging from high-control options like **Compute Engine** and **Google Kubernetes Engine (GKE)** to serverless, convenient platforms like **Cloud Run**. To handle specialized AI workloads, Google developed **Tensor Processing Units (TPUs)**—custom chips designed for superior efficiency in tasks like matrix multiplication compared to general-purpose CPUs and GPUs.

* **Storage**: Solutions are selected based on data type. **Cloud Storage** is ideal for unstructured data (e.g., documents, images), while services like **BigQuery**, **AlloyDB**, and **Cloud SQL** manage structured data.

* **Data and AI Products**: The top layer enables users to move from data to insights using an orchestrated workflow: ingest and process, store and analyze, and activate with AI.

### Key Integration
Google Cloud integrates these tools to streamline the "data-to-AI" lifecycle. BigQuery acts as a versatile data warehouse that can analyze structured, semi-structured, and even unstructured data. Vertex AI serves as the central platform for AI development, offering everything from no-code solutions to custom-built models, and it works seamlessly with data products like BigQuery to facilitate advanced training and analysis.

# AI Models

This lesson clarifies key AI and machine learning (ML) terminology and categorizes common ML problems.  
### Key Definitions
* **Artificial Intelligence (AI)**: An umbrella term for computers mimicking human intelligence.  
* **Machine Learning (ML)**: A subset of AI where computers learn from data rather than being explicitly programmed.  
* **Deep Learning/Neural Networks**: A specialized subset of ML that uses multi-layered structures to learn at depth.
* **Generative AI (GenAI)**: A field that creates content and performs tasks using foundation models like large language models.  

### ML Problem Categories
| Category | Data Type | Goal| Examples|
| -------- | -------- | ----| -------| 
| Supervised Learning| Labeled|   Task-driven|  Classification (e.g., cat vs. dog), Regression (e.g., forecasting sales)|  |Unsupervised Learning|Unlabeled | Data-driven | Clustering (e.g., segmentation), Association, Dimensionality reduction  |
