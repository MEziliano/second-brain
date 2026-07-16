# Introduction

The "Introduction to AI and Machine Learning on Google Cloud" course simplifies complex AI and machine learning concepts for all skill levels. It covers AI foundations, generative AI (including Gemini, Veo, and Imagen), and the development of autonomous AI agents. Participants learn the complete development workflow, ranging from no-code solutions to code-based approaches using Vertex AI and BigQuery ML.

## Use case
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

## AI On Google Cloud
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

## AI Infrasctructure
Google Cloud’s AI infrastructure is organized into three distinct layers, providing a scalable, efficient foundation for AI development.

### The Three-Layer Infrastructure
* **Networking and Security**: The base layer that supports all applications and infrastructure.

* **Compute and Storage**: These are decoupled to allow independent scaling.

* **Compute**: Google offers various services, ranging from high-control options like **Compute Engine** and **Google Kubernetes Engine (GKE)** to serverless, convenient platforms like **Cloud Run**. To handle specialized AI workloads, Google developed **Tensor Processing Units (TPUs)**—custom chips designed for superior efficiency in tasks like matrix multiplication compared to general-purpose CPUs and GPUs.

* **Storage**: Solutions are selected based on data type. **Cloud Storage** is ideal for unstructured data (e.g., documents, images), while services like **BigQuery**, **AlloyDB**, and **Cloud SQL** manage structured data.

* **Data and AI Products**: The top layer enables users to move from data to insights using an orchestrated workflow: ingest and process, store and analyze, and activate with AI.

### Key Integration
Google Cloud integrates these tools to streamline the "data-to-AI" lifecycle. BigQuery acts as a versatile data warehouse that can analyze structured, semi-structured, and even unstructured data. Vertex AI serves as the central platform for AI development, offering everything from no-code solutions to custom-built models, and it works seamlessly with data products like BigQuery to facilitate advanced training and analysis.

## AI Models

This lesson clarifies key AI and machine learning (ML) terminology and categorizes common ML problems.  
### Key Definitions
* **Artificial Intelligence (AI)**: An umbrella term for computers mimicking human intelligence.  
* **Machine Learning (ML)**: A subset of AI where computers learn from data rather than being explicitly programmed.  
* **Deep Learning/Neural Networks**: A specialized subset of ML that uses multi-layered structures to learn at depth.
* **Generative AI (GenAI)**: A field that creates content and performs tasks using foundation models like large language models.  

### ML Problem Categories
| Category | Data Type | Goal| Examples|
| -------- | -------- | ----| -------| 
| Supervised Learning| Labeled|   Task-driven|  Classification (e.g., cat vs. dog), Regression (e.g., forecasting sales)| 
|Unsupervised Learning|Unlabeled | Data-driven | Clustering (e.g., segmentation), Association, Dimensionality reduction  |


Common ML ModelsClassification: Uses models like logistic regression to predict categorical variables.  Regression: Uses models like linear regression to predict numeric variables.  Clustering: Uses techniques like k-means clustering to group similar data points.  Association: Uses techniques like Apriori to identify relationships between variables.  Dimensionality Reduction: Uses methods like principal component analysis to simplify datasets and improve efficiency.  These models are utilized within tools such as BigQuery ML, AutoML, and custom training environments. 

## BigQuery ML

### Key phases
01. Extract, transform and load data into BigQuery.
02. Select and preprocess feeatures.
03. Create the model inside BigQuery

```SQL
CREATE MODEL
ecommerce.classification
OPTIONS
(
    model_type='logistc_reg', 
    input_label_cols = "will_buy_later"
) AS
/* SQL query with training data*/
```
BigQuery also supports other popular ML models. Include: lineaer regression, k-means, clustering and time series forcasting models. And, in addition to providing different types of Machine Learning models, also supports MLOps

04. Evaluate the performance of the trained model.
05. Use the model to make predictions. 

---
# Generative AI on Goolge Cloud
An advanced field that uses foundation models to generate multimodal content—such as text, code, images, speech, and video—and perform autonomous, goal-oriented actions through AI agents.  

**The Three-Layered Gen AI Stack**
To help users build their own applications, Google Cloud utilizes a simplified architecture:  
* **Foundation Models**: The intelligence layer built on Google’s AI infrastructure that understands language, images, and video.
* **Gen AI Development**: A suite of tools, including Vertex AI Studio, Agent Builder, and Model Garden, designed to prototype applications, deploy agents, and fine-tune models.
* **Gen AI Applications**: Products like Gemini Enterprise and NotebookLM that allow business users to build AI agents without needing to code.  

**Google’s Gen AI History and Commitment**
Google has been a central driver of modern generative AI, beginning with the 2017 introduction of the Transformer architecture, which serves as the foundation for modern generative AI applications. This progress continued with the 2023 launch of Gemini, a multimodal model that advanced the concept of Artificial General Intelligence (AGI) through its ability to process diverse data types.  

# Foundations Models
Foundation models serve as the intelligence backbone of Generative AI, trained on vast datasets to learn complex patterns and store information. Google categorizes these models based on their specific utility and capabilities:
### Google Foundation Model Portfolio
* **Gemini Family:** Ideal for general-purpose, multimodal tasks.
* **Gemini Pro:** Designed for complex reasoning tasks.
* **Gemini Flash:** Optimized for speed and low latency in high-volume applications.
* **Gemini Flash-Lite:** The most cost-effective option for high-volume, non-time-critical tasks.
* **Specialty Models:** Tailored for specific domains, including **Imagen** (image generation), **Veo** (video processing), and **embeddings models** (semantic search and data representation).

### The Significance of Multimodality

A key evolution in AI is the shift toward **multimodal models** like Gemini. Unlike earlier models restricted to a single modality, multimodal AI can process and synthesize information from text, images, audio, and video simultaneously. This enables more human-like reasoning and sophisticated real-world actions, such as extracting information from videos or categorizing expenses from images.

### Model Customization: Pre-trained vs. Fine-tuned

Because general foundation models may lack data for specialized fields like healthcare or finance, they can be customized.

* **Pre-trained Models:** These are "horizontal AI" solutions trained on massive datasets to handle broad tasks like content creation, summarization, and Q&A.
* **Fine-tuned Models:** These are "vertical AI" solutions, created by taking a pre-trained model and training it further on smaller, field-specific datasets to solve niche industry problems.

### Development Approaches

Developers can engage with these models on Google Cloud through three main tiers of flexibility:

* **No-code:** Google Cloud Console **UI** for exploring and testing prompts.
* **Low-code:** Using Gen AI model **APIs** (e.g., Gemini APIs) with tools like cURL.
* **Code-based:** Utilizing **SDKs** for languages like Python and Java, integrated into environments like Vertex AI, Colab, and Workbench.

## Idea to an App
 