# 7. Generative AI on Google Cloud
SPEAKER: In the previous module, you mastered AI infrastructure and foundations.
Now let's dive into generative AI, the cutting edge of AI advancement.
In this module, you'll explore Google's comprehensive Gen AI development architecture, from foundation models to powerful development tools and exciting applications.
You'll discover everything from chatbots to the latest AI agents and agentic AI.
Curious about what Gen AI can do for you and how Google can help you build your own Gen AI application?
Let's begin with an overview of Gen AI on Google Cloud.
Imagine you're a retail merchandiser needing to quickly generate thousands of personalized product descriptions that resonate with individual customer preferences.
Or you're an automotive engineer who needs to rapidly iterate a novel vehicle design exploring countless combinations to optimize for weight or fuel efficiency.
Or perhaps your financial analyst tasked with creating investment reports tailored to each client's unique portfolio and risk appetite.
Generative AI, also known as Gen AI, can be your new go-to for all these tasks.
Gen AI is transforming how you work and create.
But what exactly is it?
It's a type of artificial intelligence that generates content and takes action for you.
What kind of content?
The generated content can be multimodal, including text, code, images, speech, video, and even 3D.
When given a prompt, which is a question or an instruction, Gen AI can produce images and videos, summarize meeting notes, create research reports, and develop Q&A chatbots.
In addition to content creation, Gen AI, through AI agents, can take autonomous, goal-oriented action on your behalf, a topic you'll explore further in this module.
For instance, Gen AI can automate workflows, plan and book travel, schedule appointments, and assist with clinical diagnoses.
The possibilities are limited only by your imagination.
Here's why you should trust Google as your partner on the Gen AI journey.
Looking back, Google boasts a rich history of breakthroughs in generative AI, from the 2017 introduction of Transformer, a deep-learning neural network architecture that underpins all
modern generative AI applications, to Gemini, a multimodal AI model launched in 2023 that expands the concept of Artificial General Intelligence, AGI, through its multimodal processing capabilities.
Fast-forward to the last 18 months.
The pace of innovation has accelerated dramatically.
Google has released multiple foundation models and launched practical applications like NotebookLM, which lets you use AI to
research and analyze content, and Gemini Enterprise, which allows you to build an AI agent with no code.
You'll explore these models and applications in upcoming lessons.
Looking ahead, how does Google deliver these AI services and help you build your own Gen AI applications?
Let's break it down into a simplified, easy-to-understand three-layered stack.
One-- foundation models. Built on Google's robust AI infrastructure, these powerful models are the intelligence behind all Gen AI applications, understanding language, images, and video. Two-- Gen AI development.
Tools like Vertex AI Studio, Agent Builder, and Model Garden enable you to prototype applications, deploy AI agents, and fine-tune models.
Three-- Gen AI applications.
Products like Gemini Enterprise and NotebookLM help business users build AI agents without code.
You'll get to explore all these exciting models and products in much more detail very soon.

# 8. Foundation Models

Previously, you explored the fascinating world of Gen AI architecture on Google Cloud.
Now let's dive into the foundational layer, foundation models, the true backbone of all Gen AI applications.
Interested in how AI creates content?
Want to learn about Google's foundation models, their differences, the significance of multimodal AI, and how to customize these models for your specific needs?
Let's explore these topics in this lesson.
How does AI generate new content?
It learns from a massive amount of existing content such as text, image, and video.
The process of learning from existing content is called training, which results in the creation of a foundation model.
A foundation model is usually a large model in the sense of a significant number of parameters, vast training data, and high computational power requirements.
The number of parameters generally indicates a model's capacity to learn complex patterns and store information.
To give you a perspective, the number of parameters has dramatically increased from millions to trillions in recent years.
This substantial increase signifies that foundation models are becoming progressively more capable and smarter.
As a pioneering AI company, Google trains foundation models for both general purposes, such as Gemini, and specialized tasks, such as Imagen.
These models empower Google's own products like Google Search and Workspace and provide services for external users.
Gemini family, ideal for general purposes and multi-modal data use cases-- popular options include Gemini Pro, the most capable model ideal for complex tasks requiring advanced reasoning; Gemini Flash, optimized for high speed and low latency-- perfect for high volume, real-time applications like chatbots; Gemini
Flash-Lite, the most cost-effective model suited for high volume tasks where time isn't critical, such as batch translation and content summarization; specialty models designed for specific tasks, for instance Imagen for image generation, Veo for video processing, embeddings models for semantic search, and data representation.
This list is subject to change due to the rapid evolution of foundation models. Always refer to Google documentation for the latest updates. You can find this via the QR code or reading list.
Powered by the foundation models, Gen AI is driving new opportunities to enhance productivity, save operational costs, and create new value.You might have seen these opportunities from the use case about Coffee on Wheels in the previous module
where you used Gen AI capabilities to automate the marketing campaign, generate customer feedback, and optimize truck routes.
Take a moment to pause and reflect.
What could be the use cases for using AI to solve your business problems?
Each model is fine-tuned for optimal performance within its specific domain.
However, Gemini has the potential to replace some of these models due to its general purpose and the ability to process data across multiple modalities, a feature known as multimodal.
A multimodal model, such as Gemini, can process information from various sources, including text, images, and video.
It can also generate content in multiple modalities.
For example, you can prompt Gemini to generate a video walkthrough of a recipe based on a cookie photo.
Multimodal capability marks a significant leap in generative AI's evolution, fundamentally changing how AI perceives and engages with its environment.
Unlike earlier models limited to a singular modality, multimodal AI now processes an array of senses, enabling it to understand and interact using modalities like text, images, audio, and video.
These models seamlessly process and synthesize information from multiple sources simultaneously.
This holistic comprehension enables generative AI to grasp complex contexts, leading to more human-like reasoning and the ability to drive sophisticated, real-world actions.
How can Gemini enhance your business operations?
Here are some notable examples.
Information extraction-- Gemini can read text from images and videos, extracting crucial information for further
processing. Information analysis-- it can analyze information extracted from images and videos based on specific prompts.
For instance, it can categorize expenses from a receipt.
Information seeking-- Gemini can answer questions or generate Q&A based on information extracted from text, images,
and videos. Content creation-- it can create stories or advertisements drawing inspiration from images and videos.
The possibilities are extensive, limited only by your imagination regarding how Gen AI can address your business challenges.
Let's apply this to a challenge.
Assume you need AI to assess home insurance risk effectively by using real estate images, weather histories, property inspection reports and disaster videos.
Which Google AI model is best to process these multimodal data? A, Veo. B, Embeddings. C, Imagen.D, Gemini.
Yes, Gemini is the winner due to its powerful multimodal capabilities.
Let's now consider some practical challenges.
While foundation models generally possess broad capabilities, they often lack sufficient training data when confronting problems in specialized fields like health care or finance.
To address specific challenges, such as generating financial models or providing healthcare consulting, a foundation model can be further trained with new field-specific data sets.
This process yields a new model precisely tailored to your requirements.
This leads to the concept of pre-trained and fine-tuned models.
A foundation model is pre-trained for general purposes using a large data set and then fine-tuned for specific objectives with a much smaller data set.
Consider K-12 education. After 12 years of foundational learning in reading, writing, and arithmetic, individuals become literate and can solve basic problems. However, to become a professional such as a medical doctor, automotive engineer, or financial advisor, additional specialized training and education are necessary. A similar idea applies to pre-trained versus fine-tuned models.
Foundation models like Large Language Models, LLM, fall under the category of horizontal AI, given their broad capabilities.
They address common challenges across industries including content creation-- text, image, audio, video, and code; information synthesis; document abstraction and summarization; and conversation generation, questions and answers.
Conversely, models fine-tuned for specific industries, like retail, finance, and health care are considered vertical AI solutions.
These often target industry niches and solve specialized problems such as disease diagnosis.
In light of these advancements of foundation models like Gemini, how can developers engage with them on Google Cloud and create applications that leverage multimodal capabilities?
There are three main approaches, each accomplishing the same goal with varying degrees of flexibility.
Google Cloud Console UI, or User Interface, a no-code solution perfect for exploring and testing prompts;
Gen AI model Application Programming Interfaces, or APIs, a low-code solution like Gemini APIs, used in conjunction
with command line tools cURL; predefined Software Development Kits or SDKs, a code-based solution available in languages
like Python and Java, used with notebooks like Colab and Workbench, and seamlessly integrated into Vertex AI.
Let's explore how to use AI models with Google in the next few lessons.

# 9. Idea to app
Given that foundation models are the backbone of generative AI development and applications, you may wonder how to interact with them and bring your ideas to applications.

Are there tools available to assist with this process?

Let's look at a use case that may resonate with your real-world problems.

Bea, Ann, and Ian, all work for Cymbal Insurance, a national insurance company with a strong presence in the Western states.

They are looking for Gen AI tools to help them in their everyday work, including conducting research and automating their workflow.

Bea, business analyst-- seeks to quickly prototype a Gen AI app idea that automates risk analysis and report generation, despite lacking

a technical background. Ann, AI developer-- needs a user-friendly development platform for prompt engineering, including drafting, evaluating, refining, and managing prompts.

Ian, ML engineer-- requires a robust, secure, and scalable tool to build pipelines for deploying prompts to production and fine-tuning Gen AI models.

Powered by advanced foundation models like Gemini and an enterprise-ready AI infrastructure, Google offers a variety

of products and services that can help Bea, Ann, and Ian accomplish their Gen AI use cases.

For example, Vertex AI Studio-- easily build, deploy, and scale generative AI applications. Agent Builder and Gemini Enterprise-- design, deploy, and manage AI agents.

NotebookLM-- an AI-powered research and note-taking tool for document interaction and insights.

Let's check out Vertex AI Studio first and then move to AI Agents and NotebookLM later in this course.

What is Vertex AI Studio?

Simply put, Vertex AI Studio is your gateway to generative AI.

Vertex AI Studio provides an intuitive interface between developers and the foundation models.

It enables you to build Gen AI applications in a low-code, or even no-code environment where you can rapidly test and prototype applications,

tune and customize models using your own data, augment them with real-world, up-to-date information, and deploy models efficiently in production environments with auto-generated code.

Envision Vertex AI Studio as a cutting-edge workshop where Gen AI models are your raw materials.

You are the craftsperson, and the Vertex AI Studio toolkit is your arsenal for shaping and refining these models into powerful AI solutions.

Intrigued?

Join Bea, Ann, and Ian to learn how to use this magical tool from prompt to production.

They all understand that the prompt-to-production may involve a comprehensive lifecycle.

Designing, evaluating, and refining prompts, building and testing applications, and monitoring and optimizing generative AI models.

However, Bea, with no technical background, wonders if there's a quicker way to directly turn idea to app.

The journey begins with a prompt, a natural language request to an AI model.

This can be a question, task, or instruction leading the AI to generate text, code, images, videos, music, or more.

The process of creating prompts to get the desired response is called prompt design.

The iterative process of designing, refining, and optimizing prompts to effectively guide an AI model in generating desired and high quality outputs is called prompt engineering.

Think of a prompt as the way to communicate with Gen AI models.

Just as human communication requires clarity, so does prompting AI.

You need to be good at asking questions to get the results you want.

So what makes a good prompt?

Let's begin by examining the anatomy of a prompt.

Generally, a prompt includes one or more of the following key components-- task, context, examples.

Task is required.

This is the core instruction for the model.

For example, "Conduct a risk analysis for an insurance company."

Simple tasks may only require zero-shot prompting, which means providing only the task without any examples.

Context is optional.

This is the background information or system instructions that sets the stage for the AI, such as, "You are a business analyst overseeing risk assessment for an insurance company."

Examples are optional.

These are demonstrations of desired responses, step-by-step instructions or output formats that are useful for complex tasks, such as guiding the AI with a report template.

This is also known as few-shot prompting.

When crafting effective prompts, focus on two key aspects, content and structure.

For content, ensure your prompt includes all relevant information for the task, t, and examples.

For structure, organize the information in a way that the model can understand.

Consider the order, labels, and delimiters.

Here's an example of a well-structured prompt.

You first describe the context.

"You are an IT help desk technician at a university. Your daily job is to help faculty and students solve their technology issues."

You then specify the task by providing a step-by-step instruction, such as, "To complete the task, you will need to follow these steps."

Additionally, you also provide some common Q&A examples.

Tips for effective prompts-- now that you understand the ingredients of a good prompt, here are some tips for crafting effective ones.

Be direct and specific.

State requests clearly, and use keywords.

Use structure.

Break down complex tasks into smaller steps, and use delimiters to organize sections.

Iterate and refine.

Start simple, and improve based on AI output.

Explore advanced techniques.

Consider few-shot prompting, chain-of-thought prompting, or Retrieval Augmented Generation, or RAG, for more complex scenarios.

Some of these advanced techniques will be discussed later in this course.

And remember basics-- avoid jargon, set clear goals, create scenarios, and encourage analysis. As Bea and Ann reflect on their

discovery journey with Vertex AI Studio, they want to create a prompt that utilizes key components and best practices. Which of

the following prompts is the best option? A, provide a risk assessment report. B, conduct a market risk analysis for

a health insurance company in the United States. C, you are an analyst at a regional health insurance provider in the

southeastern United States. Your task is to generate a market risk analysis by following the steps A, B, and C.

Please find the report template that includes 1, 2, and 3. Yes, C is the correct answer. Take a moment to

think about why. What makes C an effective prompt? Compared to A and B, C clearly outlines all three components-- task,

generate a market risk analysis; context, you are an analyst at an insurance company; and examples, such as steps and template.

This detailed instruction will effectively guide the AI.

Excited, Bea and Ann then used Vertex AI Studio to prototype a web-based application.

Bea is a little anxious about her first prompt.

But Vertex AI studios Help me write feature provides AI-assisted prompting, clarifying content, formatting responses, and breaking down complex tasks.

The platform's prompt gallery also offers numerous examples, filtered by modality such as audio, doc, text, image, and video, tasks, such as answer questions, classify, and code, and features.

Ann is particularly impressed by Vertex AI studio's support for multimodal prompts and outputs, allowing embedding

documents, PDFs, images, videos, and YouTube content in prompts and generating responses in similar multimodal formats.

With the AI assistant and prompt gallery's help, Bea drafted her first confident prompt.

"Conduct a risk assessment on housing in southern Los Angeles. You are a business analyst for

Cymbal Insurance. Analyze the articles from the internet, and extract the following information. Risk assessment-- identify potential

risks and rate severity 1 to 5, low to high. Categorization-- classify risks by geography, type, and

sentiment. Impact analysis-- evaluate potential consequences of each risk. And additional insights. Provide relevant observations and recommendations."

Take a moment to reflect on Bea's prompt. Are you able to identify the major components that make up an effective prompt-- task, context and examples?

Do you have any suggestions to improve it?

With a few rounds of experimenting with prompts, Bea and Ann are ready to see their first prototype.

They click on the Build with Code button and Deploy as App.

And voila!

Vertex AI Studio automatically generates a web-based application.

Bea and Ann are amazed at how quickly they were able to prototype an idea and discover the capabilities of Gen AI.

They can't wait to see more options provided by Vertex AI Studio and dive deeper to design, evaluate, and refine prompts.

You'll learn more about this soon.


# Prompt Engineering
This lesson covers the first half of the prompt-to-production lifecycle, prompt engineering from design to evaluation and refinement.

A good prompt, as we learned previously, considers both content-- instructions, context, and examples-- and structure-- order, labels, delimiters.

So how do you engineer a good prompt?

It begins with prompt design, supported by a rich toolkit provided by Vertex AI Studio.

This is your primary playground for crafting prompts.

On the left, specify the context in system instructions, then pose your tasks or questions in the Prompt section.

Need help?

Gemini, the built-in AI assistant, can help you create your prompt.

Powered by multimodal foundation models like Gemini, you can incorporate multimedia data such as documents, images,

and videos from diverse sources, including Google Cloud Storage, Google Drive, your local computer, or a URL.

You can even embed YouTube video links into a prompt.

Guide the AI's output by adding examples using the default input and output features.

Or customize them to question and answer.

Enterprise users can also import example files of their company's data.

Ann is a developer looking for a way to code prompts, perhaps using a function or method with variables to streamline repetitive actions.

Vertex AI Studio's new prompt template feature is the perfect solution.

It uses replaceable variables, allowing you to reuse a prompt by simply changing values.

Imagine a function in coding but using natural language.

The beauty is, you only need to tell GenAI what to do without worrying about how to do it with specific programming languages.

Consider this example.

By clicking Add Variables, you can assign values, just like passing arguments to a function.

For instance, you could ask AI to research Los Angeles tenant vacancy rate and generate a report on real-estate market analysis.

You can also instruct AI to add variables to study annual crime rate and conduct an insurance risk assessment by using the same prompt template with different values.

When your draft is complete, navigate to the right side of the user interface to experiment with various model parameters.

Begin with model selection.

Vertex AI Studio offers a wide selection of Google and third-party models, including Anthropic Claude, Meta Llama, and OpenAI GPT.

A key advantage of Vertex AI Studio, though, is its access to Google's cutting-edge GenAI models, like Gemini.

Choosing the right Google model depends on your task.

In the previous lesson, you were introduced to Google's different foundation models.

To refresh your memory, Gemini family-- example, Gemini Flash and Gemini Pro-- ideal for general purposes and multimodal data use cases, specialty models designed for specific tasks.

For instance, here are a few options when you are in media studio, where you create multimedia with Vertex AI Studio-- Imagen for

image creation, Chirp for voice generation, Veo for video processing, Lyria for music composition. After model selection, the next step is parameter specification, like

temperature, Top P, and Top K. You might find some of these options in the advanced settings. These parameters control the randomness of

the model's responses by adjusting how output tokens are selected. But how do they actually work? Let's look at an example. The garden was

full of beautiful dot, dot, dot. When prompted with this incomplete sentence, language models predict the probability of potential words, like flowers, trees,

herbs, and bugs. The selection strategy impacts the outcome. Always choosing the most probable word can lead to repetitive and potentially biased text, while

random sampling might yield unlikely responses, such as bugs. Adjusting model parameters to control randomness allows you to balance predictability and variety, finding the

ideal strategy for a specific task. Let's explore these parameters in depth. First, temperature-- this number controls the degree of randomness in generated output.

A low temperature setting narrows the range of possible output to high-probability, more typical words.

This is ideal for tasks like question answering and summarization, where a more typical answer with less variability is expected.

A high-temperature setting expands the range to include lower-probability, more unusual words, useful for generating creative or unexpected content.

Another parameter is Top K. Top K allows the model to randomly select a word from the Top K most probable words, where K equals a number.

For example, top two means the model will randomly select either of the two most probable words, such as flowers or trees.

This approach gives high-scoring words an equal chance.

However, if the probability distribution is highly skewed-- example, flowers at 80% and books at 10%-- it can result in strange responses, like the garden was full of beautiful books.

The challenge of selecting the optimal top K value led to Top P, where P stands for probability.

Top P allows the model to return a word from the smallest subset with a sum of likelihoods that exceeds or equals P. For example, a P of 75% means

sampling from a set of words with a cumulative probability greater than 75%-- in this

case, flowers, trees, and herbs. This dynamically adjusts the size of the word set based on

the probability distribution of the next word. And that is an overview of the model parameters-- model type, temperature, Top K, and Top P. Note that you are not required

to adjust them constantly, especially Top K and Top P. After crafting the prompt and

specifying parameters, how can you ensure you've selected the optimal model and parameters for the task?

This is where evaluation and refinement come in.

Vertex AI Studio allows you to compare prompts side by side to see which produces the best results.

This helps you understand how different prompts, models, and/or parameter settings influence the output.

You can even generate your own evaluation metrics by adding ground truth from your field knowledge, your preferred answer to the prompt against which all other model responses are evaluated.

Ready to take your prompt to the next level?

Optimize it in a Colab Enterprise notebook by adding labeled examples to refine the results.

You can perform these tasks' comparison, optimization, and evaluation under the Prompt management menu.

Imagine Prompt management as storage to save and share prompts for future use and collaboration, complete with tools like version control and security.

Beyond general purpose prompts, you can apply these prompt engineering techniques and tools on Vertex AI Studio

to specific tasks, such as generating real-time streaming, creating multimedia content, translating content, and converting speech and text.

Ann has learned so much about what she can do with prompts and is eager

to leverage these tools to create custom prompts using her own data to solve business problems.

She's excited to learn how to deploy the prompt to code, which will be revealed in the next lesson.


# Deploy and model tuning

 In the previous lesson, Ann experimented with the Vertex AI Studio toolkit to design, evaluate, and manage prompts.
Now she's ready to deploy the prompt to an application.
She teams up with Ian, the ML engineer who is responsible for building a pipeline and monitoring performance.
This brings us to the second half of the prompt-to-production lifecycle, integration and deployment, covering stages from build and test to monitor and optimize.
Recall that, early in their journey, Bea and Ann quickly tested their ideas by simply clicking Build with Code and then Deploy as App to build their own application.
However, what if they wanted to customize the application or integrate its features into other applications?
Vertex AI Studio provides this flexibility by automatically generating the code for you.
Besides the User Interface, UI, which requires no code to explore and test prompts, Vertex AI Studio offers other low-code approaches to access AI models.
These are Software Development Kits, or SDKs, in Python, and APIs with cURL.
Simply click Build with Code to find the code describing the prompt and its parameters.
Automated code generation simplifies application development.
Additionally, the integrated development environment with Cloud Run and Cloud Shell streamlines production and removes the need to worry about the underlying cloud architecture that supports application deployment.
After building your application, continuous monitoring and optimization are key to maintaining high performance.
But how do you ensure your Gen AI models deliver accurate, up-to-date results?
One way is through grounding and Retrieval Augmented Generation, or RAG.
Gen AI models are often pretrained, meaning their responses rely on potentially outdated or inaccurate training data.
Grounding connects these models to trusted external data sources, ensuring their answers are verified against the latest information.
RAG is a method for implementing this idea.
Think of grounding as the what and RAG as the how.
When constructing your prompt with Vertex AI Studio, you can choose to ground the results either through Google
real-time search for the most current information or your own data to instruct the AI with field-specific knowledge.
To further your knowledge of these advanced technologies, we recommend our courses Create Embeddings-- vector search and RAG with BigQuery and Vector Search and Embeddings with Vertex AI.
These courses introduce how to implement RAG pipelines with Google's two widely used platforms, BigQuery and Vertex AI, respectively.
You can scan the QR code on the screen or find the link in your reading list.
Other than fact-checking using grounding and RAG, what if you want to improve the quality of content generation itself?
That's where model tuning comes in.
It's another way to enhance Gen AI accuracy, providing the model with a training data set of specific downstream task examples.
While fine tuning refines the model's internal knowledge and abilities, grounding augments its knowledge with external, real-time and reliable information.
Remember the earlier analogy about foundation models versus fine-tuned models?
If K-12 education represents the foundation model, then fine-tuning is specialized professional training like medical school that embeds domain-specific expertise.
Grounding, then, is the ongoing practice of checking the latest research, drug treatments, and medical policies to stay current.
Now let's look at how to tune and customize a Gen AI model with Vertex AI Studio.
You have different options, ranging from less technical methods like prompt design, which require fewer computational resources, to more technical methods that require more computational resources, like full fine-tuning.
You are already familiar with prompt design, which lets you tune a generative AI model with examples and instructions in natural language.
Remember that prompt design does not alter the parameters of the AI model.
Instead, it improves the model's ability to respond appropriately by guiding it on how to react.
One benefit of prompt design is that it enables rapid experimentation and customization of generative AI results.
Another benefit is that it doesn't require specialized machine learning knowledge or coding skills, making it accessible to a wider range of users.
However, for more complex tasks that require tailored results, consider customizing an AI model with either parameter-efficient tuning or full fine-tuning.
Parameter-efficient tuning, also called adapter tuning, enables efficient adaptation of large models to your specific task or domain.
This method also updates a relatively small subset of the model's parameters during the tuning process.
05:02
Full fine-tuning is ideal for highly complex tasks, as it can achieve higher quality results.
However, this method requires more computational resources for both tuning and serving, as it updates all the model's parameters.
Given these techniques and even some variations between them, Vertex AI currently supports supervised fine-tuning to customize foundational models.
Supervised fine-tuning improves model performance by teaching it a new skill.
It uses data containing hundreds of labeled examples to teach the model to mimic a desired behavior or task.
Each labeled example demonstrates the desired model output.
The output of the tuning job is a new model that combines newly learned parameters with the original model.
Supervised fine-tuning is a good option for well-defined tasks with available labeled data.
For example, it can improve model performance for classification, summarization, extraction, and chat tasks.
Supervised fine tuning trains a model with labeled data.
It can be implemented with different techniques like parameter-efficient tuning or full fine-tuning, depending on task complexity and available computational resources.
Now let's move to Vertex AI Studio and see how to start a tuning job.
From the Vertex AI Studio menu, select Tuning, then Create a Tuned Model.
Specify the model details and the tuning data set.
Note that the UI may change as the product progresses.
The tuning data set should be structured as supervised training data in a JSONL file.
Each record or row contains a pair of text data, the input text, which is the prompt, and the output text, which is the expected response from the model.
For example, if the prompts are "This commercial building is architecturally interesting and has a great interior layout."
and "The room was terrible. It needs major rework." the expected sentiment labels would be positive and negative, respectively.
This structure allows the model to learn and adapt to your desired behavior.
You can then start the tuning job and monitor the status in the Google Cloud console.
When the tuning job completes, you'll see the tuned model in the Vertex AI Model registry.
And you can deploy it to an endpoint for serving or further test it in Vertex AI Studio.
That was a lot of information.
Ann and Ian can't wait to explore and start experimenting with Vertex AI Studio themselves.
It's time for you to have some hands-on practice.
This lab will give you the opportunity to create an application directly from a prompt, design effective prompts by
applying best practices, engineer and manage prompts by using features like prompt evaluation, and use multimodal prompts and generate media.
By the end of the lab, you'll be well equipped to use Gemini Multimodal with Vertex AI Studio.

# AI Agents
Let's proceed to the most recent AI application, AI agents.

In previous lessons, you learned about foundation models like Gemini and development tools like Vertex AI Studio for building Gen AI applications.

You might now be wondering how to further leverage these technologies to enable AI to not only chat and research but also take action.

For instance, can AI be used to automate your workflows and make decisions on your behalf?

This is where AI agents and Agentic AI takes center stage.

Join us in this lesson to explore the evolution of Gen AI and then dive into AI agents, discovering how they take action for you.

Think about the applications you've explored so far.

Many are conversational in nature.

You pose a question with a prompt, and the AI delivers an answer.

Think back to the example with Bea and Ann.

They asked Vertex AI Studio to generate an insurance analysis report from a set of instructions.

And voila!

The AI did a fantastic job in mere seconds, saving Ann tremendous time.

Naturally, Bea and Ann wished the AI could automate the subsequent steps, like verification, decision-making, and policy structuring.

However, these tasks require accessing internal documentation and interacting with various existing applications.

This falls outside the scope of foundation models, which base their knowledge on pre-trained data that's often not field-specific and cannot connect to different applications.

An AI agent solves this problem and adds real value to foundation models.

AI agents connect to information and applications outside of foundation models, take action, and observe feedback from the environment to improve over time.

Bea and Ann are amazed by the potential of AI agents.

What if they desire a unified agent system that coordinates multiple agents for insurance, underwriting, and claims?
02:25
This is termed agentic AI, which can be imagined as a more autonomous, complex reasoning and

coordinating system for multi-step tasks involving multiple agents, surpassing the capabilities of a single AI agent.

Gen AI is embarking on a fascinating journey, evolving from simple chatbots to sophisticated AI agents and, ultimately, to proactive Agentic AI.

This progression promises to make AI increasingly practical, empowering us to tackle more complex real-world challenges.

Given the evolution of Gen AI, let's zoom in on an AI agent and discover how it works.

First and foremost, what exactly is an AI agent?

In generative AI, an AI agent is an application that combines AI models for reasoning, tools for external interaction, and sophisticated coordination to achieve a desired goal.

The agent's operation is driven by its logical architecture, which has a few key features.

It is goal-oriented, uses an AI model as its brain, employs tools for action, and has a potential reasoning and decision-making capability that allows it to operate autonomously.

To achieve these attributes, an AI agent coordinates three essential components-- model, tools, and orchestration. First, the model-- the brain.

The model, which can be one or multiple AI foundation models, is the agent's reasoning center.

Like a brain, it acts as the central decision-maker, thinking, planning, and figuring out the steps needed to achieve a goal.

Models are typically general purpose, but can be refined with specific examples to showcase capabilities.

Next the tools-- hands, feet, and senses. Tools are the connectors that allow the agent to

interact with the outside world, often taking the form of APIs, using comments such as GET, POST,

PATCH, DELETE. Like hands and feet, they perform actions such as sending an email. Like senses, they

gather new, external information, such as fetching weather data. And lastly, the orchestration layer-- the nervous system.

The orchestration layer is the central, cyclical process that governs the agent's operation.

Like a nervous system, it acts as the communication network.

It takes the brain's decisions, uses tools to take action, and then carries feedback from that action back to the brain to inform the next step.

To learn more about AI agents, please refer to Google's whitepaper, Agents, accessible via the QR code on the screen and URL in the reading list.

Quiz time-- Bea and Ann learned a lot about an AI agent and how it works with three components. They want to design an AI agent to handle insurance

claims. This agent needs to first access the customer's claim history from an external database. Then the agent needs to validate the claim by checking it against the internal

policy documentation. And finally, send a confirmation email to the customer. Let's match the components from the following list to the questions. Which AI Agent component is responsible for

managing the sequence of actions and decisions which connects to internal and external resources and services? And which comprehends communication and logic-- the model, the tools, or the orchestration layer?

Yes, A, the model, acting as the brain, comprehends communication and logic.

B, the tools, connect to resources and services.

While C, the orchestration layer, manages the sequence of actions and decisions.
In summary, AI agents advance the AI function from conversational, chatbots, to actionable. But how can you create an AI agent on Google Cloud?

# Agent building with Google Cloud

Earlier, you learned about the evolution of GenAI applications, from chatbots to AI agents, and then to agentic AI. You also delved into an AI agent, how it works, with three components-- model, tools, and orchestration layer. Now it's time for a practical guide-- how to create an AI agent on Google Cloud.

Google's GenAI architecture, as discussed at the beginning of this module, provides a comprehensive suite of AI agent tools and products. These offerings span foundation models, development tools, and application products.

From the bottom up, Vertex AI Model Garden provides access to a wide range of Google's foundation models and third-party generative AI models, serving as the brain for your agent.

Moving up to the development layer, a developer can build an AI agent using Vertex AI Agent Builder with either low-code or pro-code options.

This platform offers tools such as Agent Development Kit, or ADK, Agent Engine, and Agent Garden, along with a managed environment to simplify agent development.

It empowers developers, including software and ML engineers, to build AI agents end-to-end, from design to deployment.

The top layer is the application or solution layer, designed for business users or analysts who want to build an AI agent with no code or minimum code.

Gemini Enterprise is the hub for hosting and building AI agents to solve customized business problems.

You can also rely on the Customer Engagement Suite to build conversational agents like customer service chatbots.

How exciting.

You're probably thrilled by the capabilities of AI agents, yet perhaps a bit overwhelmed by the sheer number of tools available.

The big question is, how do you use them efficiently to build an AI agent?

This is the exact challenge Bea, Ann, and Ian faced when they set out to build an AI agent to automate insurance quotes for their customers.

Where to start?

Let's dive deeper into how to use these different tools from an AI agent builder's perspective.

Product choices and development journeys are influenced by two key factors, ease of use and flexibility.

Ease of use ranges from no-code, ready-to-go solutions like Gemini Enterprise, progressing to more comprehensive code-based solutions for building your own.

Flexibility varies from minimal configuration, like Gemini Enterprise, to full customization and high flexibility, like build your own.

Let's focus on Gemini Enterprise and Vertex AI Agent Builder, as these are the tools most people interact with.

Bea, Ann, and Ian want to prototype their ideas using an AI agent to automate insurance quotes.

They turn to Gemini Enterprise, a user-friendly, no-code application designed for business users and analysts.

Imagine a team of expert AI agents, each ready to tackle a specific business challenge, just like hiring a travel agent or general contractor.

That's Gemini Enterprise.

This powerful enterprise platform unites AI, Google-quality search, and your company's proprietary data in one secure space.

Breaking down data silos, Gemini Enterprise makes your enterprise knowledge readily accessible and actionable in a secure manner.

A core capability of Gemini Enterprise is its intelligent, multimodal search.

It allows employees to quickly find contextual, cited answers from all organizational data formats-- documents, images, videos-- within a single interface, streamlining research and boosting productivity.

Beyond search, Agentspace also provides a hub for AI agents that can automate workflows and complete tasks on behalf of users.

It offers pre-built Google agents and a no-code agent designer for creating custom agents tailored to specific business needs.

These agents can perform actions like updating project tickets, sending emails, or analyzing reports, reducing manual overhead and freeing up time for more strategic work.

Among the powerful AI agents in Google Agentspace, NotebookLM stands out.

It's your personal AI research assistant, a learning companion and study tutor designed to quickly help you understand and gain insights from vast amounts of information.

Let's look at a demo on how to get started with NotebookLM, use it as your personal research assistant, and leverage it to discover insights and generate content.

Welcome to NotebookLM, where you can tap into the power of generative AI.

To begin, simply select the Create button to start a new notebook.

The first step is to add your source documents.

NotebookLM is flexible and supports a wide range of formats, including PDFs, text, markdown, and audio files.

You can also pull documents directly from Google Drive, add links from websites or YouTube, or paste in text.

For example, you could upload a report from McKinsey and a white paper from Google Cloud to create a new intelligent workspace.

Once your documents are uploaded, you can start a conversation in the text box at the bottom.

Think of it like talking to a super smart research assistant that uses only the documents you've provided for context.

You can ask NotebookLM to perform a variety of tasks, such as creating a concise summary of your source materials with easy-to-reference citations.

You can also ask specific questions, give it creative assignments, or have it summarize highly complex information.

The right-hand Studio panel offers even more ways to work with your documents.

In the Audio Overview section, NotebookLM can generate a podcast from two hosts based on your source documentation.

In the Notes section, it can automatically create a study guide, a briefing document, an FAQ, or even a timeline.

With these powerful features, it's your turn to explore and unlock the potential of your own data with NotebookLM.

While Gemini Enterprise and NotebookLM are impressive for building AI agents, they fall short when it comes to tailoring agents for unique business needs.

Bea, Ann, and Ian require an agent that can seamlessly integrate with their company's legacy applications and internal databases.

They also need specific response behaviors, such as adhering to industry policies for claim reports while maintaining a warm and empathetic tone for customer communications.

Gemini Enterprise couldn't accommodate these custom requirements, highlighting the need for tools like Vertex AI Agent Builder.

Let's explore the Vertex AI components that facilitate end-to-end AI agent development from design to deployment.

Vertex AI Agent Garden, a resource offering agent samples, customizable blueprints, and source code for various use

cases, like data analysis and customer service, accelerating agent development so you don't have to start from scratch.

Vertex AI Agent Development Kit, or ADK, an open source framework for developers seeking more control over

agent logic, enabling the creation of production-ready agents using Python and seamless integration with Google Cloud Services.

It's the agent version of an SDK, Software Development Kit.

Feel free to check out ADK Quickstart in the Reading List.

Vertex AI Agent Engine, a fully managed runtime for simplified deployment, scaling, and monitoring of agents in production, handling infrastructure so you can focus on capabilities.

To summarize, a simplified decision tree can help navigate Google's AI agent ecosystem, including tools and products.

Please note this is only a brief guide and may change as products evolve.

Out-of-the-box solutions-- Gemini Enterprise and conversational agents are ideal for no-code deployment.

This path is best for business users who need ready-to-use solutions with minimal setup.

Customizable templates-- Agent Garden with Agent Builder offers pre-built sample agents that can be modified.

This low-code approach is best for data scientists and analysts who need a starting point for creating more tailored solutions.

Custom development-- the ADK or building your own solution from scratch is the pro-code path.

This approach offers maximum flexibility and is best for developers like software and ML engineers who need to build highly tailored agents with complex logic and deep integrations.

Armed with these amazing tools, you can now create your very own AI agent.

Now completely free for the general public, and find your AI research assistant, learning companion, or even tutor.