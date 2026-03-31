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

## Start SageMaker AI Studio


After signing into the AWS account, follow Launch [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html)  instructions to open Studio.

Here are the instructions if you are in an AWS-led workshop event:

1. Federate into Amazon SageMaker console from the Open AWS console link in the workshop left panel:

2. In AWS console navigate to Amazon SageMaker AI console, you can do this by simply starting to type SageMaker AI in the search box at the top.
3. On the left in the Applications and IDEs section select Studio.

4. In the Get started box, make sure the agentcoreuser is selected and select Open Studio.
5. A pop-up will appear. Select Launch shared Studio to open JupyterLab in a new browser tab.

### Start the workshop
The public GitHub repository with Bedrock AgentCore Samples  contains all source code.

If you're participating in an AWS-led workshop, the workshop content is cloned into the space volume automatically, no action required from you. If you use your own domain and user profile, you need to clone the repository first. To do this select Terminal in the Launcher window or select File > New > Terminal to open up a terminal and run the git clone:
```git clone https://github.com/awslabs/amazon-bedrock-agentcore-samples.git```

This will clone the repository into the local JupyterLab file system.

Every lab specifies the required packages needed to run the lab, Please install the requirements.txt using the command below:

````pip install --force-reinstall -U -r requirements.txt --quiet````

### Selecting the Kernel
The first time you open up a notebook, you may need to select a kernel. Below are the steps shown for one of the lab:

In the JupyterLab file explorer UI on the left side of your screen, open up the first notebook by navigating to: ``amazon-bedrock-agentcore-workshop/01-AgentCore-runtime/01-hosting-agent/01-strands-with-bedrock-model/runtime_with_strands_and_bedrock_models.ipynb.``

Once this notebook is opened up, select the kernel selector button (shown in red).
Ensure that the ``Python 3 (ipykernel)`` is selected. If not, select it as shown below.

# Amazon Bedrock AgentCore Fundamentals
Welcome to the Amazon Bedrock AgentCore Workshop! This workshop will give you an overview of AgentCore, with in-depth explanations alongside code samples in Jupyter notebooks.

The need to innovate quickly has become paramount. Within just a few years, we've seen the evolution of foundation models (FMs) and generative AI workflows - from being used primarily to generate a response to a user’s prompt (like answering a question or summarizing a document), to powering robust AI agents solutions that leverage FMs to reason, plan, act, learn, adapt, and orchestrate multi-agent collaboration in pursuit of user-deﬁned goals with little human oversight. This new wave of agentic AI is further propelled by the emergence of standardized protocols such as [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro)  and [Agent2Agent (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)  that simplify and standardize how agents connect with tools and systems.

Building AI agents that can reliably perform complex tasks has become increasingly accessible thanks to open source frameworks like [Strands Agents](https://strandsagents.com/) , [LangGraph](https://www.langchain.com/langgraph) , [CrewAI](https://crewai.com/) , and [LlamaIndex](https://www.llamaindex.ai/) . However, moving from a promising proof-of-concept to a production-ready agent that can scale to thousands of users presents significant challenges. Instead of being able to focus on the core features of the agent, developers and AI engineers have to spend months building foundational infrastructure for session management, identity controls, memory systems, and observability - while at the same time supporting security and compliance.

**So what is Bedrock AgentCore?**
Here's where AgentCore comes in. [Amazon Bedrock AgentCore](https://aws.amazon.com/pt/bedrock/agentcore/) is an enterprise-grade suite of services designed to accelerate moving your agentic applications from POC to Production. AgentCore enables you to deploy and operate agents securely, at scale. AgentCore services can be used together or independently and work with any framework including Strands Agents, LangGraph, CrewAI, and LlamaIndex, as well as any foundation model in or outside of Amazon Bedrock, giving you the ultimate flexibility. It serves developers and enterprises who need 1) robust, secure, and scalable infrastructure to support dynamic execution paths at runtime, 2) controls to monitor behavior, 3) powerful tools to enhance agents, and 4) the flexibility to adapt as the landscape evolves. Amazon Bedrock AgentCore services are composable and work with popular open-source frameworks and any model, so you don’t have to choose between open-source flexibility and enterprise-grade security and reliability.

**Amazon Bedrock AgentCore** eliminates the undifferentiated heavy lifting of building specialized agent infrastructure, and was designed to give you:

* **Faster time to value**: Accelerate from prototype to production with fully-managed services that eliminate infrastructure complexity, so you can bring groundbreaking agentic solutions to market faster.

* **Flexibility and choice**: Build agents your way using any framework, model, or tool — while maintaining complete control over how your agents operate and integrate with existing systems.

* **Security and trust**: Deploy with confidence using enterprise-grade security, complete session isolation, and comprehensive controls that help your agents operate reliably and securely at scale.

### Key Components of Amazon Bedrock AgentCore
Amazon Bedrock AgentCore includes the following modular services that you can use together or independently:

![IMAGE]("second-brain\AWS\Bedrock AgentCore\images\bedrock-agent-core.png")

### Amazon Bedrock AgentCore Runtime
AgentCore Runtime is a **secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools** using any open-source framework (including Strands Agents, LangGraph, and CrewAI), any protocol, and any model. Runtime was built to work for agentic workloads with industry-leading extended runtime support, fast cold starts, true session isolation, built-in identity, and support for multi-modal payloads. Developers can focus on innovation while Amazon Bedrock AgentCore Runtime handles infrastructure and security—accelerating time-to-market.

## Amazon Bedrock AgentCore Identity
**AgentCore Identity provides a secure, scalable agent identity and access management capability** accelerating AI agent development. It is compatible with existing identity providers, eliminating needs for user migration or rebuilding authentication flows. AgentCore Identity's helps to minimize consent fatigue with a secure token vault and allows you to build streamlined AI agent experiences. Just-enough access and secure permission delegation allow agents to securely access AWS resources and third-party tools and services.

### Amazon Bedrock AgentCore Gateway
AgentCore Gateway provides a **secure way for agents to discover and use tools** along with easy transformation of APIs, Lambda functions, and existing services into agent-compatible tools. Gateway eliminates weeks of custom code development, infrastructure provisioning, and security implementation so developers can focus on building innovative agent applications. AgentCore Gateway's powerful built-in semantic search capability helps agents effectively search tools to find the most appropriate ones for specific contexts, allowing agents to take advantage of thousands of tools while minimizing prompt size and reducing latency.

### Amazon Bedrock AgentCore Code Interpreter
The AgentCore Code Interpreter tool enables agents to securely execute code in isolated sandbox environments. It offers advanced configuration support and seamless integration with popular frameworks. Developers can build powerful agents for complex workflows and data analysis while meeting enterprise security requirements.

### Amazon Bedrock AgentCore Browser
The AgentCore Browser tool provides a **fast, secure, cloud-based browser** runtime to enable AI agents to interact with websites at scale. It provides enterprise-grade security, comprehensive observability features, and automatically scales— all without infrastructure management overhead.

### Amazon Bedrock AgentCore Memory
AgentCore Memory makes it easy for developers to **build context aware agents** by eliminating complex memory infrastructure management while providing full control over what the AI agent remembers. Memory provides industry-leading accuracy along with support for both short-term memory for multi-turn conversations and long-term memory that can be shared across agents and sessions.

### Amazon Bedrock AgentCore Observability
AgentCore Observability helps developers **trace, debug, and monitor agent performance in production** through unified operational dashboards. With support for OpenTelemetry compatible telemetry and detailed visualizations of each step of the agent workflow, AgentCore enables developers to easily gain visibility into agent behavior and maintain quality standards at scale.

### Amazon Bedrock AgentCore Evaluations( Preview)
Monitors the quality of your agents based on real-world behavior using built-in evaluators for dimensions such as correctness and helpfulness, plus custom evaluators for business-specific requirements. AgentCore Evaluations is a fully managed service that helps you continuously monitor and analyze agent performance based on real-world behavior. With AgentCore Evaluations, you can use built-in evaluators for common quality dimensions such as correctness, helpfulness, tool selection accuracy, safety, goal success rate, and context relevance. You can also create custom model-based scoring systems configured with your choice of prompt and model for business-tailored scoring while the service samples live agent interactions and scores them continuously.

### Amazon Bedrock AgentCore Policy( Preview)
Defines clear boundaries for agent actions by intercepting AgentCore Gateway tool calls before they run using policies with fine-grained permissions. Policy gives you control over the actions agents can take and are applied outside of the agent’s reasoning loop, treating agents as autonomous actors whose decisions require verification before reaching tools, systems, or data. It integrates with AgentCore Gateway to intercept tool calls as they happen, processing requests while maintaining operational speed, so workflows remain fast and responsive.

Let's dive into them one-by-one!

**Resources**

* [Introducing Amazon Bedrock AgentCore: Securely deploy and operate AI agents at any scale (preview)](https://aws.amazon.com/pt/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
* [Amazon Bedrock AgentCore Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) 
* [Amazon Bedrock AgentCore Starter Toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit)
* [Amazon Bedrock AgentCore FAQs](https://aws.amazon.com/pt/bedrock/agentcore/faqs/)

---

## AgentCore Runtime 

**Overview**
Amazon Bedrock AgentCore Runtime provides a secure, serverless and purpose-built hosting environment for deploying and running AI agents or tools, shortening the time to value from experiments to production-grade agents.

**How it works**

![Works]("C:\Users\murilo.eziliano\Documents\GitHub\second-brain\AWS\Bedrock AgentCore\images\runtime_overview.png")

1. **Container ingestion** - The developer pushes an ARM64 container image to Amazon ECR. Runtime stores the image digest alongside metadata describing required ports (8080 for HTTP, 8000 for MCP).

2. **Runtime creation** - ``CreateAgentRuntime`` registers the image, assigns a workload identity, and stamps Version 1. A ``DEFAULT`` endpoint is generated that targets V1.

3. **Session bootstrap** - On the first ``InvokeAgentRuntime`` with a new ``runtimeSessionId``, the control plane provisions an isolated execution environment. The bootstrap time is minimized through cached image digests and lazy layer extraction.

4. **Invocation handling** - The request payload (up to 100 MB) is streamed into the container. The agent produces either a JSON document or a Server‑Sent Events stream. Runtime relays those bytes directly to the caller while simultaneously capturing observability data.

5. **Health negotiation** - AgentCore Runtime polls the ``/ping`` route. The agent replies with ``Healthy`` when idle or ``HealthyBusy`` while processing background tasks—allowing long‑running workflows to persist across await points.

6. **Credential exchange** - If the agent calls an external tool requiring OAuth, it exchanges its workload token for a scoped access token via AgentCore Identity. Tokens are short‑lived and bound to the invoking user where applicable.

7. **Termination** - After 15 minutes of inactivity or eight hours total runtime, the environment is terminated. Memory pages are wiped, temporary storage is discarded, and the session ID no longer maps to that environment.

8. **Version update** - Publishing a new image triggers Version n+1. Updating an endpoint redirects new sessions to the new version while existing sessions on the previous version continue until they naturally terminate.

[Learn more about how AgentCore Runtime works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html)

### Labs:
In the following labs, you'll learn how to:

* **[Lab: Hosting Runtime Agent](https://catalog.us-east-1.prod.workshops.aws/event/dashboard/en-US/workshop/20-AgentCore-Runtime/21-hosting-agent/)** - Deploy and invoke your agent in AgentCore Runtime without managing infrastructure
* **[Lab: Hosting MCP Server](https://catalog.us-east-1.prod.workshops.aws/event/dashboard/en-US/workshop/20-AgentCore-Runtime/22-hosting-mcp-server)** - implement an MCP Server and deploy it in AgentCore Runtime
* **[Lab: Advanced Concepts](https://catalog.us-east-1.prod.workshops.aws/event/dashboard/en-US/workshop/20-AgentCore-Runtime/23-advanced-concepts/)** - Implement streaming responses, manage agent session and context, and process large multi-modal payloads
---
## Hosting Runtime Agent

**Overview**

[Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)  enables developers to deploy and run AI Agents in a secure and scalable serverless environment. The Bedrock AgentCore Runtime provides a secure, serverless hosting environment necessary for deploying and running AI agents and tools without managing infrastructure. By offering a framework-agnostic and model-flexible runtime, the AgentCore Runtime enables organizations to leverage their existing agent code and models, rather than being limited to a specific development framework or AI architecture.

**How it works**

The Amazon Bedrock AgentCore Python SDK acts as a wrapper that:

* **Transforms** your agent code into AgentCore's standardized protocols
* **Handles** HTTP and MCP server infrastructure automatically
* **Lets you focus** on your agent's core functionality
* **Supports** two protocol types:
    * **HTTP Protocol**: Traditional request/response REST API endpoints
    * **MCP Protocol**: Model Context Protocol for tools and agent servers

**High Level Architecture**

When hosting agents, the SDK automatically:

* Hosts your agent on port 8080
* Provides two key endpoints:
    * /invocations: Primary agent interaction (JSON input → JSON/SSE output)
    * /ping: Health check for monitoring

![Architecture](second-brain\AWS\Bedrock AgentCore\images\4hosting_agent_python_sdk.png)  

**Getting Started**

First, you need to implement an AI Agent using the framework of your choice. In this example, we implement a simple AI Agent using the [Strands Agent](https://strandsagents.com/latest/)  framework:

```Python  
from strands import Agent, tool
from strands_tools import calculator
import argparse
import json
from strands.models import BedrockModel

@tool
def weather():
    """ Get the weather """
    return "sunny"

model_id = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
model = BedrockModel(
    model_id=model_id,
)
agent = Agent(
    model=model,
    tools=[calculator, weather],
    system_prompt="You're a helpful assistant. You can perform simple math calculations and tell the weather."
)

def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("payload", type=str)
    args = parser.parse_args()
    response = strands_agent_bedrock(json.loads(args.payload))
    print(response)
```

**Prepare the Agent for AgentCore Runtime**

The [Amazon Bedrock AgentCore Python SDK](https://github.com/aws/bedrock-agentcore-sdk-python)  provides a lightweight wrapper that helps you deploy your agent functions as HTTP services compatible with Amazon Bedrock AgentCore.

You can convert **your existing agent function** into an Amazon Bedrock AgentCore-compatible service with just **four steps**:

1. Import the Runtime App with ``from bedrock_agentcore.runtime import BedrockAgentCoreApp``
2. Initialize the App in our code with ``app = BedrockAgentCoreApp()``
3. Decorate the invocation function with the `@app.entrypoint` decorator
4. Let AgentCoreRuntime control the running of the agent with `app.run()`

**Invoke your Agent**

You can invoke the agent using the ``InvokeAgentRuntime`` operation:

```Python 
import boto3
import json

# Initialize the Bedrock AgentCore client
agent_core_client = boto3.client('bedrock-agentcore', region_name="us-east-1")


# Prepare the payload
payload = json.dumps({"prompt": prompt}).encode()

# Invoke the agent
response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    runtimeSessionId=session_id,
    payload=payload
)
```

**Try it Out**
**At an AWS Events**
In the JupyterLab UI, navigate to ``01-AgentCore-runtime/01-hosting-agent/01-strands-with-bedrock-model``

**Self-paced**
Here's are notebooks that lets you try out the above and extend the patterns to other frameworks and models

|Example| 	Framework| 	Model| 	Description| 
| -- | -- | --| --|
|[strands-with-bedrock-model](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/01-hosting-agent/01-strands-with-bedrock-model/runtime_with_strands_and_bedrock_models.ipynb) |  	Strands Agents| 	Amazon Bedrock| 	Basic agent hosting with AWS native models| 
|[langgraph-with-bedrock-model](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/01-hosting-agent/02-langgraph-with-bedrock-model)|  	LangGraph| 	Amazon Bedrock| 	LangGraph agent workflows| 
|[strands-with-openai-model](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/01-hosting-agent/03-strands-with-openai-model/runtime_with_strands_and_openai_models.ipynb)|  	Strands Agents|	OpenAI| 	Integration with external LLM providers|


### Hosting MCP Server

**Overview**

[Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-getting-started-toolkit.html)  lets you deploy Model Context Protocol (MCP) servers without managing infrastructure. This guide covers how to host MCP tools using the [Amazon Bedrock AgentCore Python SDK](https://github.com/aws/bedrock-agentcore-sdk-python).

The SDK wraps your agent functions as MCP-compatible servers, handling protocol details so you can focus on logic. It supports both HTTP and MCP protocols for tool and agent interaction.

For tool hosting, the SDK uses **Stateless Streamable HTTP** with the ``Mcp-Session-Id`` header for session isolation . Servers must run on ``0.0.0.0:8000`` and expose ``/mcp``.

AgentCore automatically adds ``Mcp-Session-Id`` to support stateless, session-aware communication. The ``InvokeAgentRuntime`` API passes through all payloads, enabling seamless MCP message proxying.

**High Level Architecture**
We will use a very simple MCP server with 3 tools: a ``dd_numbers``, ``multiply_numbers`` and ``greet_users``
![HighArchitecture]("C:\Users\murilo.eziliano\Documents\GitHub\second-brain\AWS\Bedrock AgentCore\images\5hosting_mcp_server.png")

1. **Agent Initialization**: The agent starts and is configured to interact with the configured tools via the MCP Server hosted on AWS using the AgentCore Runtime.

2. **Tool Discovery or Invocation**: The agent sends a request to the MCP Server (using streamable-HTTP) to either list available tools or invoke a specific tool (e.g., add_numbers, multiply_numbers, or greet_users).

3. **Tool Execution**: The MCP Server, running inside the AgentCore Runtime, processes the request and routes it to the appropriate tool implementation.

4. **Tool Response Returned**: Once the selected tool completes its logic (e.g., performs a computation or generates a greeting), the MCP Server returns the response to the agent.

5. **Agent Processes Result**: The agent receives the result from the MCP Server and uses it to continue its reasoning or return a final response to the user or system.

**Getting Started**

**Environment Requirements**
Before starting this lab, ensure you have:

* **Python 3.10+** installed on your system
* **AWS credentials** configured with appropriate permissions
* **Docker** running for containerization
* **Amazon Bedrock AgentCore SDK** installed
* **Strands Agents** framework installed

**Create MCP Server**

**Key MCP Server Components Explained:**

* **FastMCP**: Creates an MCP server that can host your tools
* **@mcp.tool()**: Decorator that turns your Python functions into MCP tools
* **stateless_http=True**: Required for AgentCore Runtime compatibility
* **Tools**: Three simple tools demonstrating different types of operations

**Create Local Testing**
<details>
<summary>Code Snippet</summary>

```Python
%%writefile my_mcp_client.py
import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    mcp_url = "http://localhost:8000/mcp"
    headers = {}

    async with streamablehttp_client(mcp_url, headers, timeout=120, terminate_on_close=False) as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tool_result = await session.list_tools()
            print("Available tools:")
            for tool in tool_result.tools:
                print(f"  - {tool.name}: {tool.description}")

if __name__ == "__main__":
    asyncio.run(main())
```
</details>

**Testing Locally**

To test your MCP server locally:
1. **Terminal1**: Start the MCP server

```
python amazon-bedrock-agentcore-workshop/01-AgentCore-runtime/02-hosting-MCP-server/mcp_server.py
```
2. **Terminal 2**: Run the test client
``` 
python amazon-bedrock-agentcore-workshop/01-AgentCore-runtime/02-hosting-MCP-server/my_mcp_client.py
```
You should see your three tools listed in the output.

**Setting up Amazon Cognito for Authentication**
AgentCore Runtime requires authentication. We'll use Amazon Cognito to provide JWT tokens for accessing our deployed MCP server. We also modify the Python path so that modules in the parent directory can be imported. It imports utility functions used to set up the Cognito user pool and IAM role

The code below is the helper function to create and configure a Cognito user pool. The result is stored in cognito_config, which contains values such as ``user_pool_id``, `client_id`, and `discovery_url`.

<details>
<summary>Code Snippet</summary>

```Python 
import sys
import os

# Get the current notebook's directory
current_dir = os.path.dirname(os.path.abspath('__file__' if '__file__' in globals() else '.'))

utils_dir = os.path.join(current_dir, '..')
utils_dir = os.path.abspath(utils_dir)

# Add to sys.path
sys.path.insert(0, utils_dir)

from utils import create_agentcore_role, setup_cognito_user_pool
```
</details>
<br>

**Create IAM Execution role for the AgentCore Runtime**

This code snippet creates an IAM role specifically for the MCP server. This role is required for deploying to AgentCore Runtime and is tied to the tool_name.
<details>
<summary>Code Snippet</summary>

```Python 
tool_name = "mcp_server_ac"
agentcore_iam_role = create_agentcore_role(agent_name=tool_name)
```
</details>
<br>

**Configuring AgentCore Runtime Deployment**

This sets up the AWS SDK session, determines the current region, and checks for the required files (`mcp_server.py`, `requirements.txt`). If files are missing, it raises an error.
<details>
<summary>Code Snippet</summary>

```Python
from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session
import time
import os

boto_session = Session()
region = boto_session.region_name

required_files = ['mcp_server.py', 'requirements.txt']
for file in required_files:
    if not os.path.exists(file):
        raise FileNotFoundError(f"Required file {file} not found")
```
</details>

Next, we initialize the ``Runtime`` instance and set up authentication configuration using Cognito. This ensures only valid tokens from the user pool can invoke the MCP server.
<br>

<details>
<summary>Code Snippet</summary>

```Python
<details>
<summary>Code Snippet</summary>

```Python
agentcore_runtime = Runtime()

auth_config = {
    "customJWTAuthorizer": {
        "allowedClients": [
            cognito_config['client_id']
        ],
        "discoveryUrl": cognito_config['discovery_url'],
    }
}
```
</details>
Here, we configure the MCP runtime using this script as the entry point. It creates an ECR repository automatically and prepares the runtime to deploy the MCP server using the defined IAM role and authentication.
<details>
<summary>Code Snippet</summary>

```Python
response = agentcore_runtime.configure(
    entrypoint="mcp_server.py",
    execution_role=agentcore_iam_role['Role']['Arn'],
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region=region,
    authorizer_configuration=auth_config,
    protocol="MCP",
    agent_name=tool_name
)
```
</details>

>!Documentation Note
We use the provided [starter toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit) to configure the AgentCore Runtime with an entrypoint, execution role, and requirements file. It will also auto-create the Amazon ECR repository during setup. A Dockerfile will be generated from your application code as part of this step.

**Launch MCP Server to AgentCore Runtime**

This next script initializes a Bedrock AgentCore ``Runtime`` session using the Runtime class. It sets the AWS region, checks for the required source files, and defines a custom JWT authentication configuration using Amazon Cognito credentials. The ``configure()`` method sets up the runtime deployment with all necessary parameters—such as IAM role, Python entrypoint, and required libraries—preparing it for launch.
<details>
<summary>Code Snippet</summary>

```Python
from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session
import time
import os

boto_session = Session()
region = boto_session.region_name

required_files = ['mcp_server.py', 'requirements.txt']
for file in required_files:
    if not os.path.exists(file):
        raise FileNotFoundError(f"Required file {file} not found")

agentcore_runtime = Runtime()

auth_config = {
    "customJWTAuthorizer": {
        "allowedClients": [
            cognito_config['client_id']
        ],
        "discoveryUrl": cognito_config['discovery_url'],
    }
}

response = agentcore_runtime.configure(
    entrypoint="mcp_server.py",
    execution_role=agentcore_iam_role['Role']['Arn'],
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region=region,
    authorizer_configuration=auth_config,
    protocol="MCP",
    agent_name=tool_name
)
```
</details>


Now, we launch the configured runtime, deploying the MCP server to Amazon Bedrock AgentCore Runtime. The result includes identifiers like ``agent_arn`` and ``agent_id``.
```python
launch_result = agentcore_runtime.launch()
```

With the Dockerfile ready, we deploy the MCP server to AgentCore Runtime. This step creates both the Amazon ECR repository and the AgentCore Runtime environment. Lets wait for about 20 seconds for the AgentCore runtime status to be ready before we store the configurations for remote access.

Before we can invoke our deployed MCP server, let's store the Agent ARN and Cognito configuration in AWS Systems Manager Parameter Store and AWS Secrets Manager for easy retrieval:

<details>
<summary>Code Snippet</summary>

```Python
import boto3
import json

ssm_client = boto3.client('ssm', region_name=region)
secrets_client = boto3.client('secretsmanager', region_name=region)

try:
    cognito_credentials_response = secrets_client.create_secret(
        Name='mcp_server/cognito/credentials',
        Description='Cognito credentials for MCP server',
        SecretString=json.dumps(cognito_config)
    )
except secrets_client.exceptions.ResourceExistsException:
    secrets_client.update_secret(
        SecretId='mcp_server/cognito/credentials',
        SecretString=json.dumps(cognito_config)
    )

agent_arn_response = ssm_client.put_parameter(
    Name='/mcp_server/runtime/agent_arn',
    Value=launch_result.agent_arn,
    Type='String',
    Description='Agent ARN for MCP server',
    Overwrite=True
)
```
</details>

**Creating Remote Testing Client**
This snippet will create a test client that will retrieve the necessary credentials from AWS and connect to the deployed server.
**Testing**
Here are a few ways to test your config:

1. Testing Your Deployed MCP Server
```Python
print("Testing deployed MCP server...")
print("=" * 50)
!python my_mcp_client_remote.py```
2. Invoking MCP Tools Remotely
This is an advanced client that goes beyond listing tools. It will also invokes them to showcase the full capabilities of the MCP system.
<details>
<summary>Code Snippet</summary>

```Python
%%writefile invoke_mcp_tools.py
import asyncio
import boto3
import json
import sys
from boto3.session import Session

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    boto_session = Session()
    region = boto_session.region_name
    
    print(f"Using AWS region: {region}")
    
    try:
        ssm_client = boto3.client('ssm', region_name=region)
        agent_arn_response = ssm_client.get_parameter(Name='/mcp_server/runtime/agent_arn')
        agent_arn = agent_arn_response['Parameter']['Value']
        print(f"Retrieved Agent ARN: {agent_arn}")

        secrets_client = boto3.client('secretsmanager', region_name=region)
        response = secrets_client.get_secret_value(SecretId='mcp_server/cognito/credentials')
        secret_value = response['SecretString']
        parsed_secret = json.loads(secret_value)
        bearer_token = parsed_secret['bearer_token']
        print("✓ Retrieved bearer token from Secrets Manager")
        
    except Exception as e:
        print(f"Error retrieving credentials: {e}")
        sys.exit(1)
    
    encoded_arn = agent_arn.replace(':', '%3A').replace('/', '%2F')
    mcp_url = f"https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"
    headers = {
        "authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    print(f"\nConnecting to: {mcp_url}")

    try:
        async with streamablehttp_client(mcp_url, headers, timeout=120, terminate_on_close=False) as (
            read_stream,
            write_stream,
            _,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                print("\n🔄 Initializing MCP session...")
                await session.initialize()
                print("✓ MCP session initialized")
                
                print("\n🔄 Listing available tools...")
                tool_result = await session.list_tools()
                
                print("\n📋 Available MCP Tools:")
                print("=" * 50)
                for tool in tool_result.tools:
                    print(f"🔧 {tool.name}: {tool.description}")
                
                print("\n🧪 Testing MCP Tools:")
                print("=" * 50)
                
                try:
                    print("\n➕ Testing add_numbers(5, 3)...")
                    add_result = await session.call_tool(
                        name="add_numbers",
                        arguments={"a": 5, "b": 3}
                    )
                    print(f"   Result: {add_result.content[0].text}")
                except Exception as e:
                    print(f"   Error: {e}")
                
                try:
                    print("\n✖️  Testing multiply_numbers(4, 7)...")
                    multiply_result = await session.call_tool(
                        name="multiply_numbers",
                        arguments={"a": 4, "b": 7}
                    )
                    print(f"   Result: {multiply_result.content[0].text}")
                except Exception as e:
                    print(f"   Error: {e}")
                
                try:
                    print("\n👋 Testing greet_user('Alice')...")
                    greet_result = await session.call_tool(
                        name="greet_user",
                        arguments={"name": "Alice"}
                    )
                    print(f"   Result: {greet_result.content[0].text}")
                except Exception as e:
                    print(f"   Error: {e}")
                
                print("\n✅ MCP tool testing completed!")
                
    except Exception as e:
        print(f"❌ Error connecting to MCP server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
```
</details>

**Try it out**
**At an AWS Event**
If you are following the workshop via workshop studio, go to JupyterLab in SageMaker Studio. In the JupyterLab UI navigate to [01-AgentCore-runtime/02-hosting-MCP-server](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/02-hosting-MCP-server).

**Self-paced**
Here's a notebook that lets you try out the above: [hosting_mcp_server.ipynb](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/02-hosting-MCP-server/hosting_mcp_server.ipynb) .

