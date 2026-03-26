# Amazon Bedrock AgentCore

* [Amazon Bedrock AgentCore Doc](https://aws.amazon.com/pt/bedrock/agentcore/)
* [Amazon AgentCore Blog](https://aws.amazon.com/pt/blogs/machine-learning/amazon-bedrock-agentcore-is-now-generally-available/)

### Workshop Structure
This workshop provides hands-on experience with AgentCore's services. For each component, you will explore:

Foundational concepts - Understanding the service and it's role in the AgentCore ecosystem
Technical capabilities - Key features and functionality provided
Practical implementation - Hands-on labs and code samples

### Learning Objectives
By the end of this workshop, you will be able to:

Deploy secure, scalable AI agents using AgentCore Runtime
Implement robust authentication and authorization with AgentCore Identity
Integrate external services through AgentCore Gateway
Extend agent capabilities using AgentCore Tools
Manage agent memory and context with AgentCore Memory
Monitor agent performance with AgentCore Observability

----
# Prerequisites

This workshop assumes that you have a good understanding of generative AI and are familiar with solutions like [Retrieval Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) , AWS services like [Amazon Bedrock](https://aws.amazon.com/bedrock/) , [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  and hands on experience with Python  is recommended.

You have two options to run this workshop:

At an AWS event
Self-paced in your own AWS environment
The workshop contains a number of examples of how to work with [AgentCore SDK](https://github.com/aws/bedrock-agentcore-sdk-python).

Notebooks that you will run to execute the workshop will be provided for you, we will use [Amazon SageMaker Studio](https://aws.amazon.com/sagemaker-ai/studio/)  for easier packaging the development environment (AWS event) when using AgentCore you can use any IDE of your choice (self-paced).

Now, click on one of the options above and let's get started!

### Before you start
Log out from all AWS accounts from all browser windows
Review the terms and conditions of the event. Do not upload any personal or confidential information in the account
The AWS account is only be available for the duration of this workshop and you will not be able to retain access after the workshop is complete. Backup any materials you wish to keep access to after the workshop
Workshop deploys all pre-provisioned infrastructure to a specific region. Check what AWS Region is used
All notebooks are available in the public [AgentCore Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/)  GitHub repository

```
git clone https://github.com/awslabs/amazon-bedrock-agentcore-samples.git
```