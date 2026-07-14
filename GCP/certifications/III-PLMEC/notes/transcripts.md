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

