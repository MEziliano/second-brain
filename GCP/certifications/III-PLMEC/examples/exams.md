# Questions

<details><summary>1.</summary>

You are training an object detection machine learning model on a dataset that consists of three million X-ray images, each roughly 2 GB in size. You are using Vertex AI Training to run a custom training application on a Compute Engine instance with 32-cores, 128 GB of RAM, and 1 NVIDIA P100 GPU. You notice that model training is taking a very long time. You want to decrease training time without sacrificing model performance. What should you do?
- A. Increase the instance memory to 512 GB and increase the batch size
- B. Enable early stopping in your Vertex AI Training Job
- C. Replace the NVIDIA P100 GPU  with a v3-32 TPU  in the training job
- D. Use the tf.distribute.Strategy API and run a distributed training job 

<details><summary>ANSWER</summary>

- **D**

> Obs.: 
</details> </details>

--- 

<details><summary>2. You are an ML engineer at a travel company. You have been researching customers’ travel behavior for many years, and you have deployed models that predict customers’ vacation patterns. You have observed that customers’ vacation destinations vary based on seasonality and holidays; however, these seasonal variations are similar across years. You want to quickly and easily store and compare the model versions and performance statistics across years. What should you do?</summary>

- Create version of your models for each season per year in Vertex AI. Compare the perfomance statistics across the models in the Evaluate tab of the Vertex AI UI.
- Store the performance statistics of each version of your models using seasons and years as events in Vertex ML Metadata. COmpare the results across the slices..
- Store the perfomance statistics in Cloud SQL. Query that database to compare the performance statistics across the model versions. 
- Store the performance statistics of each pipeline run in Kuberflow under an experient for each season per year. Compare the results across th experiments in the Kuberflow UI. 

<details><summary>ANSWER</summary>

- **B**

> Obs.: ? Compare the models performances across the years.
! https://cloud.google.com/vertex-ai/docs/model-registry/versioning <br>

Model versioning lets you create multiple versions of the same model. With model versioning, you can organize your models in a way that helps navigate and understand which changes had what effect on the models. With Vertex AI Model Registry you can view your models and all of their versions in a single view. You can drill down into specific model versions and see exactly how they performed. <br>
!! Store the performance statistics of each version of your models using seasons and years as event in Vertex Metadata. Compare the results across the slices.
</details> </details>

---

<details><summary>3.  You built a custom ML model using scikit-learn. Training time is taking longer than expected. You decide to migrate your model to Vertex AI Training, and you want to improve the model’s training time. What should you try out first?</summary>

- A.Train your model using vertex AI Training with GPU. 
- B. Train your model in a distributed mode using multiple Compute Engine VMs
- C. Migrate your model to TensorFlow, and train it using Vertex AI Training
- D. Train your model with DVLM images on Vertex AI, and ensure that your code utilizes NumPy and SciPy internal methods whenever possible. 

<details><summary>ANSWER</summary>

- **D** 

>Obs.: ? How to improve the perfomance in a Scikit-learn model? Scikit-Learn uses NumPy as bases

! DLVM are typically designed for deep learning workloads and do not provide as much benefit for scikit-learn training. Utilizing GPUs for acceleration is best, as scikit-learn can benefit from GPU-accelerated libraries.
!! Train your model with DVLM images on Vertex AI, and ensure that your code utilizes NumPy and SciPy internal methods whenever possible. 

</details> </details>

----
<details><summary>4. You are developing an ML model that uses sliced frames from video feed and creates bounding boxes around specific objects. You want to automate the following steps in your training pipeline: ingestion and preprocessing of data in Cloud Storage, followed by training and hyperparameter tuning of the object model using Vertex AI jobs, and finally deploying the model to an endpoint. You want to orchestrate the entire pipeline with minimal cluster management. What approach should you use?</summary>

- A. Use Vertex AI Pipelines with TensorFlow Extended (TFX) SDK.
- B. Use Vertex AI Pipelines with Kubeflow Pipelines SDK.
- C. Use Cloud Composer for the orchestration.
- D. Use Kubeflow Pipelines on Google Kubernetes Engine.

<details><summary>ANSWER</summary>

- **B**

</details> </details>

---
<details><summary>5. You are a data scientist at an industrial equipment manufacturing company. You are developing a regression model to estimate the power consumption in the company's manufacturing plants based on sensor data collected from all of the plants. The sensors collect tens of millions of records every day. You need to schedule daily training runs for your model that use all the data collected up to the current date. You want your model to scale smoothly and require minimal development work. What should you do?</summary>

- A. Develop a custom scikit-learn regression model, and optimize it using Vertex AI Training.
- B. Develop a custom TensorFlow regression model, and optimize it using Vertex AI Training.
- C. Train a regression model using AutoML Tables.
- D. Develop a regression model using BigQuery ML.

<details><summary>ANSWER</summary>

- **D**

</details></details>

---
<details><summary>6. You are a lead ML engineer at a retail company. You want to track and manage ML metadata in a centralized way so that your team can have reproducible experiments by generating artifacts. Which management solution should you recommend to your team?</summary>

- A. Store your tf.logging data in BigQuery
- B. Store all ML Metadata in GCP Operation Suite
- C. Manage your ML Workflows with Vertex ML Metadata
- D. Manage all relational entities in the Hive Metastore

<details><summary>ANSWER</summary>

- **C**

</details></details>

---
<details><summary>7. You have been given a dataset with sales predictions based on your company's marketing activities. The data is structured and stored in BigQuery, and has been carefully managed by a team of data analysts. You need to prepare a report providing insights into the predictive capabilities of the data. You were asked to run several ML models with different levels of sophistication, including simple models and multilayered neural networks. You only have a few hours to gather the results of your experiments. Which Google Cloud tools should you use to complete this task in the most efficient and self-serviced way?</summary>

- A. Use Vertex AI Workbench user-managed notebooks with scikit-learn code for a variety of ML algorithms and performance metrics.
- B. Train a custom TensorFlow model with Vertex AI, reading the data from BigQuery featuring a variety of ML algorithms.
- C. Use BigQuery ML to run several regression models, and analyze their performance.
- D. Read the data from BigQuery using Dataproc, and run several models using SparkML.

<details><summary>ANSWER</summary>

- **C**

</details></details>

---
<details><summary>8. You are an ML engineer at a bank. You have developed a binary classification model using AutoML Tables to predict whether a customer will make loan payments on time. The output is used to approve or reject loan requests. One customer's loan request has been rejected by your model, and the bank's risks department is asking you to provide the reasons that contributed to the model's decision. What should you do?</summary>

- A. Use local feature importance from the predictions
- B. Vary features independently to identify the threshold per feature that changes the classification
- C. Use the feature importance percentages in the model evaluation page.
- D. Use the correlation with target values in the data summary page

<details><summary>ANSWER</summary>

- **A**

</details></details>
---

<details><summary>9. You work for a magazine distributor and need to build a model that predicts which customers will renew their subscriptions for the upcoming year. Using your company's historical data as your training set, you created a TensorFlow model and deployed it to AI Platform. You need to determine which customer attribute has the most predictive power for each prediction served by the model. What should you do?</summary>

- A. Use the What-If tool in Google Cloud to determine how your model will perform when individual features are excluded. Rank the feature importance in order of those that caused the most significant performance drop when removed from the model.
- B. Stream prediction results to BigQuery. Use BigQuery's CORR(X1, X2) function to calculate the Pearson correlation coefficient between each feature and the target variable.
- C. Use AI Platform notebooks to perform a Lasso regression analysis on your model, which will eliminate features that do not provide a strong signal.
- D. Use the AI Explanations feature on AI Platform. Submit each prediction request with the 'explain' keyword to retrieve feature attributions using the sampled Shapley method.

<details><summary>ANSWER</summary>

- **D**

</details>
</details>

<details><summary>10. You are developing ML models with AI Platform for image segmentation on CT scans. You frequently update your model architectures based on the newest available research papers, and have to rerun training on the same dataset to benchmark their performance. You want to minimize computation costs and manual intervention while having version control for your code. What should you do?</summary>

- A. Use the gcloud command-line tool to submit training jobs on AI Platform when you update your code.
- B. Create an automated workflow in Cloud Composer that runs daily and looks for changes in code in Cloud Storage using a sensor.
- C. Use Cloud Build linked with Cloud Source Repositories to trigger retraining when new code is pushed to the repository.
- D. Use Cloud Functions to identify changes to your code in Cloud Storage and trigger a retraining job.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>11. You are working on a binary classification ML algorithm that detects whether an image of a classified scanned document contains a company's logo. In the dataset, 96% of examples don't have the logo, so the dataset is very skewed. Which metrics would give you the most confidence in your model?</summary>

- A. RMSE
- B. F-Score where recall is weighed more than precision
- C. F-score where precision is weighed more than recall
- D. f1 score

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>12. You work on the data science team for a multinational beverage company. You need to develop an ML model to predict the company's profitability for a new line of naturally flavored bottled waters in different locations. You are provided with historical data that includes product types, product sales volumes, expenses, and profits for all regions. What should you use as the input and output for your model?</summary>

- A. Use latitude, longitude, and product type as features. Use profit as model output.
- B. Use product type and the feature cross of latitude with longitude, followed by binning, as features. Use revenue and expenses as model outputs.
- C. Use product type and the feature cross of latitude with longitude, followed by binning, as features. Use profit as model output.
- D. Use latitude, longitude, and product type as features. Use revenue and expenses as model outputs.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>13. You work as an ML engineer at a social media company, and you are developing a visual filter for users' profile photos. This requires you to train an ML model to detect bounding boxes around human faces. You want to use this filter in your company's iOS-based mobile phone application. You want to minimize code development and want the model to be optimized for inference on mobile phones. What should you do?</summary>

- A. Train a custom TensorFlow model and convert it to TensorFlow Lite (TFLite)
- B. Train a model using AutoML Vision and use the "export for Core ML" option
- C. Train a model using AutoML Vision and use the "export for TensorFlow.js" option
- D. Train a model using AutoML and use the "export for Coral" option

<details><summary>ANSWER</summary>

- **B**

</details>
</details>

<details><summary>14. You have been asked to build a model using a dataset that is stored in a medium-sized (~10 GB) BigQuery table. You need to quickly determine whether this data is suitable for model development. You want to create a one-time report that includes both informative visualizations of data distributions and more sophisticated statistical analyses to share with other ML engineers on your team. You require maximum flexibility to create your report. What should you do?</summary>

- A. Use Vertex AI Workbench user-managed notebooks to generate the report
- B. Use the Google Data Studio to create the report
- C. Use the output from TensorFlow Data Validation on DataFlow to generate the report
- D. Use Dataprep to create the report.

<details><summary>ANSWER</summary>

- **A**

</details>
</details>

<details><summary>15. You work on an operations team at an international company that manages a large fleet of on-premises servers located in few data centers around the world. Your team collects monitoring data from the servers, including CPU/memory consumption. When an incident occurs on a server, your team is responsible for fixing it. Incident data has not been properly labeled yet. Your management team wants you to build a predictive maintenance solution that uses monitoring data from the VMs to detect potential failures and then alerts the service desk team. What should you do first?</summary>

- A. Develop a simple heuristic (e.g., based on z-score) to label the machines' historical performance data. Test this heuristic in a production environment.
- B. Train a time-series model to predict the machines' performance values. Configure an alert if a machine's actual performance values significantly differ from the predicted performance values.
- C. Implement a simple heuristic (e.g., based on z-score) to label the machines' historical performance data. Train a model to predict anomalies based on this labeled dataset.
- D. Hire a team of qualified analysts to review and label the machines' historical performance data. Train a model based on this manually labeled dataset.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>16. You are developing an ML model that uses sliced frames from video feed and creates bounding boxes around specific objects. You want to automate the following steps in your training pipeline: ingestion and preprocessing of data in Cloud Storage, followed by training and hyperparameter tuning of the object model using Vertex AI jobs, and finally deploying the model to an endpoint. You want to orchestrate the entire pipeline with minimal cluster management. What approach should you use?</summary>

- A. Use Kuberflow Pipelines on Google Kubernetes Engine
- B. Use Vertex AI Pipelines with Kuberflow Pipelines SDK
- C. Use Vertex AI Pipeline with TensorFlow Extended (TFX) SDK
- D. Use Cloud Composer for the orchestration.

<details><summary>ANSWER</summary>

- **B**

</details>
</details>

<details><summary>17. You are a data scientist at an industrial equipment manufacturing company. You are developing a regression model to estimate the power consumption in the company's manufacturing plants based on sensor data collected from all of the plants. The sensors collect tens of millions of records every day. You need to schedule daily training runs for your model that use all the data collected up to the current date. You want your model to scale smoothly and require minimal development work. What should you do?</summary>

- A. Develop a custom Scikit-learn regression model, and optimize it using Vertex AI Training.
- B. Develop a custom TensorFlow regression model, and optimize it using Vertex AI Training
- C. Develop a regression model using BigQueryML
- D. Train a Regression model using AutoML Tables.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>18. You built a custom ML model using scikit-learn. Training time is taking longer than expected. You decide to migrate your model to Vertex AI Training, and you want to improve the model's training time. What should you try out first?</summary>

- A. Train your model in a distributed model using multiple Compute Engine VMs
- B. Train your model with DLVM images on Vertex AI, and ensure that your code utilizes NumPy and SciPy internal methods whenever possible
- C. Train your model using Vertex AI Training with GPUs
- D. Migrate your model to TensorFlow, and train it using Vertex AI Training.

<details><summary>ANSWER</summary>

- **D**

</details>
</details>

<details><summary>19. You are an ML engineer at a travel company. You have been researching customers' travel behavior for many years, and you have deployed models that predict customers' vacation patterns. You have observed that customers' vacation destinations vary based on seasonality and holidays; however, these seasonal variations are similar across years. You want to quickly and easily store and compare the model versions and performance statistics across years. What should you do?</summary>

- A. Create versions of your models for each season per year in Vertex AI. Compare the performance statistics across the models in the Evaluate tab of the Vertex AI UI.
- B. Store the performance statistics of each version of your models using seasons and years as events in Vertex ML Metadata. Compare the results across the slices.
- C. Store the performance statistics in Cloud SQL. Query that database to compare the performance statistics across the model versions.
- D. Store the performance statistics of each pipeline run in Kubeflow under an experiment for each season per year. Compare the results across the experiments in the Kubeflow UI.

<details><summary>ANSWER</summary>

- **A**

</details>
</details>

<details><summary>20. You're building a BigQuery ML model to identify fraudulent credit card transactions. This model needs to handle a constantly evolving landscape of fraudulent activity. Which BigQuery ML model type is best suited for this adaptive learning?</summary>

- A. Time Series Forecasting Linear
- B. Regression Matrix
- C. Boosted Tree Classifier
- D. Matrix Factorization

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>21. You're using Vertex AI AutoML for time series forecasting. What's a key advantage of AutoML over building a custom forecasting model from scratch?</summary>

- A. AutoML always outperforms custom models in terms of forecasting accuracy
- B. AutoML can ingest data from any data source format.
- C. AutoML requires less historical data for training compared to custom models.
- D. AutoML automates feature selection and model training, reducing development time.

<details><summary>ANSWER</summary>

- **D**

</details>
</details>

<details><summary>22. Your team is building a mobile application that allows users to search for and purchase furniture based on images. Which Google Cloud Machine Learning API would be most useful to categorize and tag objects within user-uploaded images for furniture identification?</summary>

- A. Translation API
- B. Natural Language API
- C. Cloud Vision API
- D. Cloud Vision API Intelligence API

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>23. You have been tasked with building a classification model. A team of subject matter experts worked with a data engineer to prepare a data pipeline that provides you what they believe to be the most relevant features out of many possible features available in a database. You imported the prepared data into a dataset and triggered a training job using AutoML in Vertex AI. However, your initial training results show poor model accuracy. What should you try first to improve your results?</summary>

- A. Build a custom model in order to tune the hyperparameters yourself.
- B. Ask the data engineer to modify the pipeline to include all of the features that were not selected from the database.
- C. Do exploratory data analysis on the dataset to examine the relationship between features and consider creating additional features combining one or more existing features.
- D. Increase the model's training budget and re-train.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>24. You're building a real-time translation feature within your application. Users can upload video content, and your application needs to translate the spoken language within the video to captions in a user-selected language. Which combination of Google Cloud Machine Learning APIs would best achieve this functionality?</summary>

- A. Natural Language API with Cloud Text-to-Speech API
- B. Cloud Vision API and Natural Language API
- C. Cloud Speech-to-Text API in conjunction with Translation API
- D. Cloud Spanner with Cloud Translation API

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>25. Your team is building a BigQuery ML model to recommend products to users based on their purchase history. Which BigQuery ML model type would be most effective in capturing the complex relationships between users and items?</summary>

- A. Time Series Forecasting
- B. Boosted Tree Classifier
- C. Linear Regression
- D. Matrix Factorization

<details><summary>ANSWER</summary>

- **D**

</details>
</details>

<details><summary>26. During the Vertex AI AutoML forecasting process, what happens if the provided time series data contains missing values?</summary>

- A. AutoML requires manual imputation of missing values before training the model.
- B. AutoML automatically removes all data points with missing values.
- C. AutoML can impute missing values using appropriate techniques, depending on the data characteristics.
- D. AutoML treats missing values as zeros, which may not be appropriate for all forecasting scenarios.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>27. You're tasked with creating a time series forecast for your company's monthly sales data. Which of the following data preparation steps is MOST crucial for ensuring optimal performance of the AutoML forecasting model?</summary>

- A. Standardize all numerical feature values within the data to have a mean of 0 and a standard deviation of 1.
- B. Ensure your data is formatted as a single table with a datetime column and a target sales column.
- C. Split your data into separate training, validation, and testing sets for model evaluation.
- D. Remove any outliers or missing values present within the sales data.

<details><summary>ANSWER</summary>

- **B**

</details>
</details>

<details><summary>28. You're building a low-code image classification model using AutoML Vision to identify flowers in images by their family (for example 'lily' which is a family of flowers that contains 610 different species). When preparing your data for training, which of the following actions is MOST important to ensure the accuracy of your model?</summary>

- A. Manually removing any blurry or low-quality images from the dataset.
- B. Labeling all images by the flower's species and subspecies if possible.
- C. Splitting your data into training, validation, and testing sets.
- D. Resizing all images to a uniform dimension.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>29. You're building a time series forecast for daily website traffic using AutoML. After the initial training, you realize the model consistently underestimates peak traffic days. Which approach should you try first to improve the model's ability to predict peak traffic?</summary>

- A. Switch to a different machine learning algorithm outside of AutoML for time series forecasting.
- B. Gather user feedback on peak traffic patterns and incorporate that into the model.
- C. Manually adjust the model's output to increase predicted values on anticipated peak days.
- D. Re-train the AutoML model with additional historical data that contains more peak traffic periods.

<details><summary>ANSWER</summary>

- **D**

</details>
</details>

<details><summary>30. You're developing a sentiment analysis application to monitor social media brand mentions. During model training, you include a balanced dataset of positive and negative reviews. However, after deployment, the model struggles to accurately classify highly sarcastic tweets. What's the most effective technique to improve the model's ability to detect sarcasm within social media text?</summary>

- A. Increase the model's overall complexity by adding more layers
- B. Utilize a pre-trained NLP model specifically designed for sentiment analysis.
- C. Reduce the number of features used in the model.
- D. Collect and incorporate additional sarcastic text data into the training dataset.

<details><summary>ANSWER</summary>

- **D**

</details>
</details>

<details><summary>31. You are working on a machine learning project that requires rapid experimentation with different model architectures and hyperparameters. You need a way to easily track differences between runs and compare results. Which Google Cloud service is best suited for this task?</summary>

- A. Vertex AI Online predictions
- B. Vertex AI Experiments
- C. Vertex AI Vizier
- D. Vertex AI Pipelines

<details><summary>ANSWER</summary>

- **B**

</details>
</details>

<details><summary>32. During training of production models in Vertex AI Workbench, a team encounters memory limitations due to large datasets. Which approach is most effective to overcome this challenge?</summary>

- A. Utilize data streaming techniques with libraries like tf.data in TensorFlow.
- B. Train the model on a subset of data and then fine-tune it on the remaining data.
- C. Reduce the size of the dataset by sampling or aggregating.
- D. Use a larger machine type with your Workbench Instance

<details><summary>ANSWER</summary>

- **A**

</details>
</details>

<details><summary>33. A healthcare organization is utilizing Apache Spark on Google Cloud to process Protected Health Information (PHI) for a machine learning model. What's the primary concern when sharing the aggregated model results with external researchers?</summary>

- A. Choosing the most suitable Apache Spark cluster configuration for faster model training.
- B. Optimizing data transfer speed to external researchers using gsutil.
- C. Ensuring PHI is de-identified or anonymized before sharing to comply with HIPAA regulations.
- D. Granting researchers broad access to the raw PHI data for transparency.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>34. Which Vertex AI feature allows for rapid iteration of Machine Learning (ML) model experimentation without complex infrastructure management?</summary>

- A. Vertex AI Workbench Instances
- B. Vertex AI Pipelines
- C. Vertex AI Online Predictions
- D. Vertex AI Datasets

<details><summary>ANSWER</summary>

- **A**

</details>
</details>

<details><summary>35. Your machine learning model, which predicts customer churn, has suddenly started underperforming in production. After investigation, you suspect a data poisoning attack. Which of the following actions should you do FIRST to mitigate this security risk?</summary>

- A. Implement stricter access controls on the data pipeline and model artifacts.
- B. Retrain the model on a new dataset collected over a longer period.
- C. Quarantine the affected model version and revert to a known good version.
- D. Deploy an anomaly detection system to identify and flag unusual input data.

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>36. Your machine learning project involves developing a complex model with multiple stages and dependencies. You need an environment that allows you to orchestrate the entire workflow, including data preprocessing, model training, and model evaluation. Which Google Cloud service is the most appropriate for this scenario?</summary>

- A. Vertex AI Feature Store
- B. Vertex AI TensorBoard
- C. Vertex AI Pipelines
- D. Vertex AI Model Registry

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>37. Your team is developing a machine learning model in a Jupyter notebook using PySpark on a large dataset. The model training process is computationally intensive and time-consuming. To speed up development and experimentation, what strategy should you employ?</summary>

- A. Cache the entire dataset in memory before starting the training process.
- B. Increase the number of executors in your Spark cluster.
- C. Switch to a single-node Spark configuration for faster processing.
- D. Utilize a smaller sample of the dataset during development and testing.

<details><summary>ANSWER</summary>

- **D**

</details>
</details>

<details><summary>38. Your team is working on a computer vision model to classify different flower species in images stored in Cloud Storage. How can you best organize this data for efficient training and evaluation?</summary>

- A. Create a separate BigQuery table for each flower type and store image references within the table.
- B. Organize images into subfolders based on flower types as labeled by human experts.
- C. Randomly sample images from Cloud Storage and use them directly for training without any specific organization.
- D. Rely on image metadata associated with each image file for classification purposes.

<details><summary>ANSWER</summary>

- **B**

</details>
</details>

<details><summary>39. Your company is migrating its on-premises Apache Hadoop cluster to Google Cloud. You need to choose a service that allows you to run Spark jobs on the existing Hadoop data stored in HDFS. Which Google Cloud service best meets this requirement?</summary>

- A. DataFlow
- B. BigQuery
- C. Dataproc
- D. Cloud Storage

<details><summary>ANSWER</summary>

- **C**

</details>
</details>

<details><summary>40. You're developing a sentiment analysis application that analyzes product reviews. The application utilizes the Cloud Natural Language API to categorize reviews as positive, negative, or neutral. However, the initial results include a high number of misclassified reviews. Which approach would MOST effectively improve the accuracy of the sentiment analysis?</summary>

- A. Increase the size of the training data used by the Cloud Natural Language API.
- B. Leverage a pre-trained sentiment analysis model.
- C. Utilize a different Cloud Natural Language API aspect, like entity recognition.
- D. Train a custom Machine Learning model on a labeled dataset of product reviews.

<details><summary>ANSWER</summary>

- **D**
</details></details>

---
<details><summary>41. You work for a large retailer, and you need to build a model to predict customer churn. The company has a dataset of historical customer data, including customer demographics, purchase history, and website activity. You need to create the model in BigQuery ML and thoroughly evaluate its performance. What should you do?</summary>

- A. Create a linear regression model in BigQuery ML, and register the model in Vertex AI Model Registry. Use Vertex AI to evaluate the model performance.
- B. Create a logistic regression model in BigQuery ML, and register the model in Vertex AI Model Registry. Use ML.ARIMA_EVALUATE function to evaluate the model performance.
- C. Create a linear regression model in BigQuery ML. Use the ML.EVALUATE function to evaluate the model performance.
- D. Create a logistic regression model in BigQuery ML. Use the ML.CONFUSION_MATRIX function to evaluate the model performance.

<details><summary>ANSWER</summary>

- **D**
</details></details>

<details><summary>42. You are building an ML model to detect anomalies in real-time sensor data. You will use Pub/Sub to handle incoming requests. You want to store the results for analytics and visualization. How should you configure the pipeline?</summary>

- A. 1=Dataflow, 2=AI Plataform,  3=BigQuery
- B. 1=DataProc, 2= AutoML,       3= Cloud Bigtable
- C. 1=BigQuery, 2=AutoML,        3=Cloud Functions
- D. 1=BigQuery, 2= AI Plataform, 3= Cloud Storage 

<details><summary>ANSWER</summary>

- **A**

> Obs.: **Dataflow** is a tool design to handle Pub/Sub. 
</details></details>