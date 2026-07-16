# 1. Introduction

SPEAKER 1: It feels like AI is everywhere now.

It's incredible, but, honestly, it's a bit overwhelming (very heavy).

And it feels like it's changing every day.

As soon as I thought I had wrapped my mind around generative AI, I heard about agentic AI.

What's next?

SPEAKER 2: I used to feel the exact same way.

It's like this kitchen.

It's easy to get overwhelmed when you see all the incredible tools at your disposal, just like you can get overwhelmed at all things AI can do.

But think of AI as just another powerful kitchen tool, waiting for you to pick it up and create

something amazing, and that's exactly what this course, Introduction to AI and Machine Learning on Google Cloud, helps you do.

It takes you from, huh, to, I can build that.

You start with the basics in module 1, laying the groundwork like gathering all your ingredients and tools before a complicated recipe.

You'll explore AI foundations, what AI looks like on Google Cloud, discover the infrastructure, and even get hands on with powerful tools like BigQuery ML.

SPEAKER 1: Ingredients-- so not just throwing everything into a blender and hoping for the best.

SPEAKER 2: Exactly.

You understand the why before the how, setting a strong stage for everything that comes next.

Then you dive into the really exciting realm, generative AI on Google Cloud.

This is where AI learns to create brand-new content.

SPEAKER 1: Ah, yes, gen AI.

I've been using it almost daily, but I haven't ventured beyond Gemini and don't really know much about how it works.

SPEAKER 2: Well, you're in luck.

The course dives into foundation models like Gemini, Veo for videos, and Imagen for images.

You'll also learn about prompt engineering and multimodality.

Oh, and agents.

I'm sure you've heard of AI agents.

SPEAKER 1: Sounds familiar.

It's like having an AI sidekick?

SPEAKER 2: It's more than that.

Imagine a fully autonomous assistant that generates content and takes actions for you.

SPEAKER 1: Wow.

I'm kind of speechless.

SPEAKER 2: Yeah, it's next-level stuff.

And after you learn about agents, you'll get into how to actually build and deploy these intelligent systems.

You'll explore various AI development options, understanding when to use Gemini Enterprise and AutoML for no-code solutions, progress

to pretrained APIs for low-code options, and leverage BigQuery ML and custom training with Vertex AI for code-based approaches.

SPEAKER 1: I didn't even realize there were multiple available tools for development.

And I don't need to be a coding genius to get started with building things?

SPEAKER 2: Absolutely not.

You'll learn the entire AI development workflow, from data preparation through to model development and, finally, model serving.

SPEAKER 1: That's super exciting.

I always thought this stuff was just for super geniuses, and I'd need years of experience.

SPEAKER 2: Nope.

This course breaks down complex AI topics into simple, relatable steps, making it accessible to everyone.

Whether you're simply curious, looking to expand your professional skills, or just want to understand the future

unfolding around us, this Introduction to AI and Machine Learning on Google Cloud is your perfect starting point.

You'll gain a solid, practical understanding of both generative and predictive AI and truly unlock the power of these transformative technologies.

SPEAKER 1: I'm in.

This sounds like exactly what I need to finally get AI.

SPEAKER 2: Fantastic.

Come join us, and turn your curiosity into capability.

Your journey starts now.

# 2. A use case
SPEAKER: Welcome to the first module of this course, AI Foundations.

You start your journey by exploring a real-world use case where AI addresses familiar daily challenges, revealing its profound capabilities and potential.

Next, understand how Google Cloud empowers your AI vision by solving both generative-AI and traditional AI

challenges with a comprehensive AI architecture, from infrastructure to development platforms and then applications and solutions.

Then, a brief introduction to AI infrastructure will familiarize you with Google Cloud's Compute, Storage, Data, and AI products.

Following this, delve into AI models essential for understanding AI development.

Subsequently, get practical with a deep dive into BigQuery ML, connecting data and AI.

You conclude this module with a hands-on lab where you build your first ML model and leverage AI code assistants to explain, generate, and debug code.

AI is shifting from a tool for efficiency to a powerhouse of innovation.

Let's dive into a use case to see it in action.

Did you have your morning coffee today?

If not, maybe you can use Coffee on Wheels, an international company that sells coffee on trucks in cities like London, New York, San Francisco, and Tokyo.

They provide a compelling case study.

Coffee on Wheels is facing three main challenges-- location, selection, and route optimization; predicting popular locations for truck placement and optimizing routes based on weather and

traffic conditions; sales forecast and real-time monitoring; forecasting sales and monitoring performance in real time; marketing campaign automation, automating marketing campaigns to increase efficiency and effectiveness.

Recognizing the potential of AI, Coffee on Wheels sought assistance from Data Beans, a digital-native company, to leverage data and AI technologies to resolve their business challenges.

Let's take a tour of the demo.

Choose one of the four current locations, such as London.

The dashboard displays overall statistics across cities, including revenue, operating margin, and the number of trucks.

This information is generated by data tools like BigQuery and Looker, as well as AI tools and models like Gemini and Vertex AI.

On the right, you can view the final data for London with the summary.

It shows how London's revenue compares to the average and provides insights into revenue per truck and customer loyalty.

In the top-left corner, the dashboard displays the weather and generates route suggestions based on weather conditions.

For example, if lower temperatures are forecasted, it might suggest a new itinerary that focuses on covered areas.

You can click Show Updated Route and Publish Route to implement these changes.

By clicking on a specific time on the timeline, you can see route suggestions based on city events.

For example, if there's a football game happening, it might suggest rerouting trucks to avoid congestion.

Clicking on the Truck sign provides a detailed dashboard with information such as street view and revenue forecast.

To monitor the performance of the business in real time, you can access a dashboard by clicking Show Menu.

If an item is underperforming, you can click the Generate button to get suggestions for a new item.

Additionally, you have the option to generate marketing campaigns by selecting Yes to save the suggestion.

This feature enables you to automatically create campaigns that include both text and images.

You can further streamline your marketing efforts by sending campaign emails to targeted customers with just a click of the Post button.

Finally, you can generate an operational report and export the insights to any format, such as Google Slides.

To customize the application using code, click How It's Made.

This reveals the tools and technologies, including BigQuery, Gemini, and Vertex AI, that were used to create the app.

You can also click Open In Notebook to access the sample code in the code development environment.

Isn't it remarkable?

The process is actually straightforward.

Multimodal input-- this involves incorporating various forms of data such as text, customer reviews, images, like coffee and dessert pictures, and videos, like real-time street view.

Prediction and generation-- this is powered by predictive AI, like sales forecasting, and generative AI, like marketing campaign automation. Visual

output-- the insights and reports are then presented visually, empowering businesses to make real-time, data-driven decisions and optimize their operations.

Behind the scenes, many Google products collaborate to make this application possible.

For example, Gemini Multimodal enables data acquisition.

BigQuery provides data analytics.

Vertex AI handles ML development, and AI agents connect with various applications to enact decisions, such as interacting with Looker to visualize resulting insights.

You'll explore these tools in depth later in this course.

By leveraging the application, Coffee on Wheels enhanced efficiency by streamlining and automating business processes.

This opened the door for continuous innovation in providing customers with immersive coffee experiences.

You can do the same for your business by using AI.

Let's find out how Google can help you achieve your AI vision in the next lesson.

# 3. AI on Google Cloud
Let's explore how Google can help you turn your own AI-powered ideas into reality.

So why Google?

First, Google has a long history of leveraging AI to power its products, from Google Search to popular tools like Google Maps and Workspace.

Google is eager to share its experience to empower you, whether an individual or an organization, in realizing your AI ambitions.

Second, Google leads an AI in ML innovations, particularly with recent generative AI breakthroughs.

Technologies and products like Gemini, Vertex AI, and NotebookLM exemplify Google's commitment to delivering powerful AI services for your projects.

Third, Google believes in responsible AI.

Google wants to collaborate with you to foster bold innovation, responsible development and deployment, and collaborative progress.

Explore Google's responsible AI principles in the reading to learn more.

And while this all sounds fantastic, you may be wondering, what is the current landscape of AI problems?

To simplify, let's categorize the problems.

Recall the Coffee on Wheels use case presented earlier in this module.

What problems could AI solve for them?

One type of problem is prediction, exemplified by sales forecasting and route optimization through traffic prediction.

This is known as predictive AI.

The other type is creation, such as generating customer responses and automating marketing campaigns.

This is called generative AI.

Let's delve deeper into predictive and generative AI, comparing them and determining their optimal applications.

So what are predictive AI and generative AI?

Predictive AI, also known as traditional or discriminative AI, uses existing data to classify information or predict future outcomes based on historical patterns.

It excels at learning from what's already there to make informed decisions, much like using tried-and-true methods to and forecast.

Generative AI, on the other hand, expands these capabilities to create summaries, uncover complex correlations, or generate new content.

This includes text, images, or videos that mirror the style and patterns within the training data.

It doesn't just analyze, it creates.

To put it simply, predictive AI analyzes and predicts.

Generative AI creates new content and takes action.

Now, when you should use them is based on your use case.

Here's a simplified decision tree.

For forecasting and predictions, a predictive AI model might be your go-to.

And for multimodal content generation-- text, image, video, and automation-- generative AI is ideal.

However, there's no clear line between these two.

And sometimes, the best approach is to use both.

You can use the output from a predictive AI model as part of the prompt for a generative AI model.

For example, use predictive AI to forecast customer churn.

Then use generative AI to power a chatbot that helps your sales team explore these predictions.

Or use predictive AI to identify customer segments.

Then use generative AI to create personalized marketing content for each segment.

By prioritizing business outcomes and user needs, you can maximize the benefits of both types of AI.

You can think of the Google Cloud infrastructure in terms of three layers.

It all starts with a robust AI infrastructure featuring advanced compute, network, and storage technologies.

This foundational layer provides the solid ground for building your AI realm.

Next, we move up to the development layer, where the real magic happens.

Google's Vertex AI, an end-to-end AI development platform, guides you from design to deployment.

Powering Vertex AI are Google's foundational models like Gemini and streamlined deployment pipelines.

Vertex AI also seamlessly integrates with data products like BigQuery, ensuring a smooth journey from data to AI.

This AI development layer is truly the ultimate playground for developers, engineers, and data scientists.

And what if you're not a technical professional?

At the top layer of applications and solutions, Google provides out-of-the box options for business users and analysts to rapidly prototype their ideas.

So how does this course help you comprehend Google's AI architecture?

You'll delve into AI infrastructure and the data tools in this module.

Both lay the foundation for AI development and applications.

Module 2 kicks off your AI project journey by focusing on building gen AI.

You'll learn about gen AI foundational models and the tools needed to build AI projects at both development and application levels.

And don't worry.

We haven't forgotten about predictive AI.

In module 3, you explore different options to train an ML model.

And then, in module 4, you build an ML model end to end, from data preparation to model training and deployment.

# 4. AI Infrasctructure
Building on the previous lesson where you explored Google's three-layered AI architecture, including AI infrastructure,

AI development, and AI applications and solutions, you'll now delve into the foundational layer, AI infrastructure.

Since its inception in 1998, Google has been dedicated to data and AI.

A decade later, in 2008, Google Cloud was introduced to offer secure and flexible cloud computing and storage solutions.

You can think of the AI infrastructure in terms of three layers.

At the base layer is networking and security, which lays the foundation to support all of Google's infrastructure and applications.

On the next layer, sit compute and storage.

Google Cloud separates, or decouples, as it's technically called, compute and storage, so they can scale independently based on need.

The top layer includes data and AI products, which enable you to perform tasks to ingest, store, process, and deliver business insights, data pipelines and ML models.

Thanks to Google Cloud technology, these tasks can be accomplished without needing to manage and scale the underlying infrastructure.

However, understanding some essentials about Google Cloud compute and storage can help you grasp the higher level data and AI products.

Let's begin with compute.

Organizations with growing data needs often require lots of compute power to run data and AI jobs.

And as organizations design for the future, the need for compute power only grows.

Google offers a range of computing services, from flexible infrastructure to fully managed serverless platforms, balancing control and convenience.

For example, Compute Engine-- high control, like managing a physical server; Google Kubernetes Engine, GKE-- control over containerized apps with orchestration benefits; Cloud Run-- serverless convenience.

Google manages infrastructure.

You might be familiar with the container platform GKE and serverless options like Cloud Run.

For more details, check out Google Documentation in the reading list.

Where does the processing power come from?

It's from the hardware, computer chips.

However, traditional computer chips like Central Processing Units, or CPUs, and even the more recent Graphics

Processing Units, or GPUs, may no longer scale to adequately reach the rapid demand for AI.

To help overcome this challenge, in 2016, Google introduced the Tensor Processing Unit, or TPU.

TPUs are Google's customized application-specific chips to accelerate AI workloads.

TPUs act as domain-specific hardware, as opposed to general-purpose hardware like CPUs and GPUs.

This allows for higher efficiency by tailoring the architecture to meet the computation needs in a domain, such as the matrix multiplication in machine learning.

Cloud TPUs, faster and more energy efficient than GPUs and CPUs for AI ML, are integrated across Google products, offering state-of-the-art supercomputing technology to Google Cloud customers.

Let's now examine storage.

For proper scaling capabilities, compute and storage are decoupled.

That is one major difference between Cloud and desktop computing.

With cloud computing, compute and storage can scale separately.

Most applications need a database and storage solution of some kind.

Your best option depends on your data type and business needs.

For unstructured data like documents, images, and audio files, cloud storage is your ideal choice.

Alternatively, if your data is structured, organized in tables, rows, and columns, you have options like BigQuery, AlloyDB for PostgreSQL, and others.

Note that BigQuery, Google's flagship data warehouse, is particularly versatile.

It's built for structured data and also highly optimized for semi-structured data like JSON.

It can even query unstructured data, such as log files or images stored in cloud storage, by creating an external table that provides a structured reference to that data.

This leads to the top layer of the Google Cloud infrastructure, data and AI products.

As you explored earlier, Google Cloud offers a comprehensive suite of data and AI tools.

How do you piece them together?

To build a data-to-AI project, you orchestrate these products through a data-to-AI workflow-- ingest and process, store and analyze, and activate with AI.

First, ingest and process data from diverse sources, both real-time and batch, using tools like Pub/Sub, Dataflow, Dataproc, and Cloud Data Fusion.
05:11
Next, store your data in solutions like Cloud Storage.

Then analyze it with various tools.

Use BigQuery, AlloyDB, Cloud SQL, and Spanner for SQL databases.

Use Bigtable and Firestore for NoSQL databases.

Use Looker for visualization.

Finally, activate your insights with AI.

Train predictive models for forecasting, or leverage Gen AI for content creation and action.

Vertex AI is the central AI development platform, offering products like Vertex AI Studio, Agent Builder, AutoML, and notebooks for AI projects ranging from out-of-the-box solutions to custom builds.

These tools are seamlessly integrated on Google Cloud, enabling data scientists and AI developers to efficiently transition from data to AI.

For example, BigQuery offers embedded SQL commands to train an ML model, a feature you'll explore later.

Additionally, within a Vertex AI notebook, you can easily pull data directly from BigQuery using SQL for advanced model training.

Don't let the variety of options overwhelm you.

You'll focus on BigQuery, the primary data warehouse, and Vertex AI, the AI development platform, later in this course.

But before that, let's get you ready with another fundamental topic, AI models, in the next lesson.

# 5. AI Models
Before you dive in to more practical topics and build your own machine learning model, let's prepare you with foundational knowledge and explore the AI model categories.

First, let's pause to clarify two terms, artificial intelligence and machine learning.

You may note that people often use the terms interchangeably, but they do have some differences.

Artificial intelligence, or AI, is an umbrella term that includes anything related to computers mimicking human intelligence.

Some examples of AI applications include robots and self-driving cars.

Machine learning is a subset of artificial intelligence that allows computers to learn without being explicitly programmed.

This is in contrast to traditional programming, where the computer is told explicitly what to do.

Machine learning mainly includes supervised and unsupervised learning.

You might also hear the terms deep learning or deep neural networks.

This is a subset of machine learning that adds layers in between input data and output results to make a machine learn at much depth.

You'll learn more about neural networks and deep learning later in the course.

Finally, generative AI, or GenAI, creates content and performs tasks based on requests.

GenAI uses foundation models like large language models, a type of deep learning model, to predict, interpret, and interact with language.

You'll delve deeper into GenAI models in the next module.

So what's the difference between supervised and unsupervised learning?

Imagine two types of problems.

In problem one, you are asked to classify dogs and cats from a very large set of pictures.

You already know the difference between dogs and cats, so you label each picture and pass the labeled pictures to a machine.

By learning from the data, in this case, pictures with the answers or labels, supervised learning is being

enacted, allowing the machine to tell if a new picture represents a dog or cat in the future.

In problem two, you are asked to classify breeds of dogs.

Unfortunately, this time, you don't know many of them and are not able to label the pictures.

So you send these unlabeled pictures to a machine.

In this case, the machine learns from the data without the answers and finds underlying patterns to group the animals.

This is an example of unsupervised learning.

Put simply, supervised learning deals with labeled data, is task-driven, and identifies a goal.

Unsupervised learning, however, deals with unlabeled data, is data-driven, and identifies a pattern.

An easy way to distinguish between the two is that supervised learning provides each data point with a label or an answer, while unsupervised learning does not.

There are two major types of supervised learning.

The first is classification, which predicts a categorical variable, such as determining whether a picture shows a cat or a dog.

In ML, you use models like a logistic regression model to solve classification problems.

The second type of supervised learning is regression, which predicts a numeric variable like forecasting sales for a product based on its past sales.

You use ML models like a linear regression model to solve regression problems.

There are three major types of unsupervised learning.

The first is clustering, which groups together data points with similar characteristics and assigns them to clusters, like using customer demographics to determine customer segmentation.

You use ML models like k-means clustering to solve clustering problems.

The second type is association, which identifies underlying relationships like a correlation between two products to place them closer together in a grocery store for a promotion.

You use association rule techniques and algorithms like Apriori to solve association problems.

And the third type of unsupervised learning is dimensionality reduction, which reduces the number of dimensions or features in a data set to improve the efficiency

of a model, for example, combining customer characteristics like age, driving violation history, or car type, to create a simplified rule for calculating an insurance quote.

You use ML techniques like principal component analysis to solve these problems.

# 6. BigQuery ML
With the different types of ML models in your mind, let's apply concept to practice.

In this lesson, you explore BigQuery ML and walk through the steps to build an ML model with SQL commands.

You learned about BigQuery, the primary data analytics tool on Google Cloud, from the previous lesson.

BigQuery provides two services in one.

It's a fully managed storage facility to load and store data sets and a fast, SQL-based analytical Engine.

The two services are connected by Google's high-speed, internal network.

It's this super-fast network that allows BigQuery to scale both storage and compute independently, based on demand.

Although BigQuery started out solely as a data warehouse, over time, it has evolved to provide features that

support the data-to-AI lifecycle, meaning you can perform both data analytics and build predefined ML models within BigQuery.

In this lesson, you explore BigQuery's capabilities to build ML models and walk through the steps and key SQL commands to do so.

If you've worked with ML models before, you know that building and training them can be very time-intensive.

You must first import and prepare the data.

Then, experiment with different ML models and tune the parameters.

To improve model performance, you also need to go back and forth to train the model with new data and features.

And finally, you need to deploy the model to make predictions.

This is an iterative process that requires a lot of time and resources.

Now, with BigQuery ML, you can manage tabular data and execute ML models in one place with just a few steps.

BigQuery ML tunes the parameters for you and helps you manage the ML workflow.

Let's walk through the phases of a machine learning project and the key SQL commands.

In phase 1, you extract, transform, and load data into BigQuery if it isn't there already.

If you're already using other Google products, like YouTube, for example, look out for easy connectors to get that data into BigQuery before you build your own pipeline.

You can enrich your existing data warehouse with other data sources by using SQL joins.

In phase 2, you select and preprocess features.

You can use SQL to create the training data set for the model to learn from.

BigQuery ML does some of the preprocessing for you, like one-hot encoding of your categorical variables.

One-hot encoding converts your categorical data into numeric data that is required by a training model.

In phase 3, you create the model inside BigQuery.

This is done by using the CREATE MODEL command.

In this example, you want to create an ML model to predict customer purchasing behavior, specifically if they will buy this product in the future.

You give the model a name, ecommerce.classification.

You then specify the model type.

Remember the previous lesson about ML model types?

If you want to predict whether a customer will buy or not, which ML model should you use?

That's right.

A logistic regression model is the answer because you are solving a classification problem.

Apart from the logistic regression model to solve the classification problem, BigQuery ML also supports other popular ML models.

They include regression models, such as linear regression, and other models, such as k-means clustering and time series forecasting models.

In addition to providing different types of machine learning models, BigQuery ML supports MLOps, Machine Learning Operations.

MLOps turns your ML experiment to production and helps deploy, monitor, and manage the ML models.

You'll learn more about MLOps later in this course.

You're recommended to start with simple options, such as logistic regression and linear regression, and use the results as a benchmark to

compare against more complex models, such as DNN, Deep Neural Networks, which take more time, and computing resources to train and deploy.

After specifying the model type, you also need to define the label column.

Why?

Remember the two major categories of ML models, supervised and unsupervised?

The former deals with labeled data and predicts a goal, whereas, the latter handles unlabeled data and identifies a hidden pattern.

Is this a supervised or unsupervised model?

Of course, it's a supervised classification problem.

Thus, a labeled column.

From there, you can run the query.

In phase 4, after your model is trained, you can execute an ML.EVALUATE query to evaluate the performance of the trained model on your evaluation data set.

It's here that you specify which evaluation metrics the model will assess, such as accuracy, precision, and recall.

You'll explore these metrics later in this course.

Finally, in phase 5, when you're happy with your model performance, you can then use it to make predictions.

To do so, invoke the ML.PREDICT command on your newly trained model to return with predictions and the model's confidence in those predictions.

With the results, your label field will have "predicted" added to the field name.

This is your model's prediction for that label.

Ready for hands-on practice?

Let's apply these steps and build your first ML model in BigQuery.

In the upcoming lab, you'll use real e-commerce data from the Google Merchandise Store to predict whether a visitor will make future purchases.

You'll gain valuable experience creating data sets, training and evaluating ML models, and using them for predictions.

Don't worry if SQL isn't your strong suit.

Gemini Code Assist will be your 24/7 tutor, helping you explain, create, and debug code throughout the lab.

Let's get started.

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