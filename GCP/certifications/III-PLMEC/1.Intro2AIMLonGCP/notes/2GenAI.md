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

# Idea to an App

Google provides a suite of tools, with **Vertex AI Studio** serving as the primary gateway for generative AI development.

### Key Google Cloud Tools for Gen AI

* **Vertex AI Studio:** An intuitive, low-code/no-code environment for prototyping, tuning, and deploying Gen AI applications. It features tools like "Help me write" for AI-assisted prompting and a prompt gallery for exploring examples.

* **Agent Builder & Gemini Enterprise:** Tools designed to design, deploy, and manage intelligent AI agents.

* **NotebookLM:** A specialized tool for AI-powered research and interacting with documents to gain insights.

### Best Practices for Prompt Engineering

Effective interaction with foundation models relies on **prompt engineering**—the iterative process of refining requests to achieve high-quality outputs. A high-quality prompt typically includes three key components:

1. **Task:** The core instruction (**required**).
2. **Context:** Background information or a persona to set the stage.
3. **Examples:** Demonstrations or templates for complex tasks (also known as few-shot prompting).

### Tips for Effective Prompting

* **Be Direct and Specific:** Use clear language and keywords.
* **Use Structure:** Break complex tasks into steps and use delimiters to organize different sections of the prompt.
* **Iterate and Refine:** Start with a simple prompt and improve it based on the AI's output.
* **Leverage Multimodality:** Vertex AI Studio allows for multimodal prompts that include various file types, such as PDFs, images, videos, and YouTube content.

Once a prompt is optimized, users can leverage the **"Build with Code"** and **"Deploy as App"** features within Vertex AI Studio to automatically generate web-based applications, allowing non-technical users to quickly prototype and test their ideas.

## Prompt engineering

To refine and optimize prompt engineering, **Vertex AI Studio** provides an integrated environment for design, evaluation, and management.

### Key Prompt Engineering Tools in Vertex AI Studio

* **Prompt Templates:** Allows developers to create reusable prompts using replaceable variables, similar to coding functions, to streamline repetitive tasks.
* **Multimodal Integration:** Enables the inclusion of documents, images, videos, and YouTube links directly into prompts to leverage Google’s multimodal foundation models.
* **Model Selection:** Offers access to Google’s Gemini family (Flash, Pro) for general tasks, as well as specialty models like **Imagen** (images), **Chirp** (voice), **Veo** (video), and **Lyria** (music).
* **Prompt Management:** Provides a centralized hub for version control, security, and collaborative sharing of prompts.

### Controlling Model Output

Users can balance the predictability and creativity of AI responses by adjusting advanced model parameters:

* **Temperature:** Controls randomness; lower settings result in more typical, focused outputs (e.g., summarization), while higher settings increase variety and creativity.
* **Top K:** Restricts the model to randomly selecting from the top *K* most probable words.
* **Top P:** Dynamically adjusts the word selection set based on a cumulative probability threshold, offering a more flexible alternative to Top K.

### Evaluation and Refinement

To ensure optimal performance, Vertex AI Studio supports an iterative lifecycle:

* **Side-by-Side Comparison:** Users can evaluate different prompts, models, and parameter settings simultaneously.
* **Ground Truth Metrics:** Users can establish "ground truth" (preferred answers) to quantitatively evaluate model responses against their own field knowledge.
* **Optimization:** Further refinement can be performed in **Colab Enterprise notebooks** by adding labeled examples.

Would you like to explore how to deploy these engineered prompts into production code in the next lesson?


## Deploy 