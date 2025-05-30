---
title: Deploying an AI agent using LangServe
videoId: qgH_KFSFMUE
---

From: [[colemedin]] <br/> 

This article outlines the process of [[deploying_and_monitoring_ai_agents | deploying and monitoring an AI agent]] to a scalable cloud API endpoint, allowing it to run 24/7. The method focuses on using LangServe to wrap a LangChain- or LangGraph-built AI agent into a [[using_fastapi_with_langserve_for_ai_deployment | FastAPI endpoint]] for cloud hosting <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach ensures the agent can scale and operate continuously, moving beyond local execution <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## What is LangServe?

LangServe is a tool that automates the creation of an API wrapper around AI agents <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. It can be used with any LangChain chain or LangGraph application <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Key Components and Setup

To deploy an AI agent with LangServe, the following components are typically involved:

*   **LangServe Endpoint Script**: Defines the FastAPI endpoint <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **LangServe Chatbot Script**: Contains the Streamlit UI (frontend), requiring only three lines of code changes to interact with the LangServe endpoint <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This is part of [[setting_up_ai_agents_with_langchain_and_streamlit | setting up AI agents with LangChain and Streamlit]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Runnable (LangGraph/LangChain App)**: The core AI agent logic, often built with LangGraph, including nodes, LLM interactions, and tool calls <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Environment Variable File (`.env`)**: Used for setting API keys and defining the LLM model <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **GitHub Repository**: Provides all necessary code, including the LangServe endpoint and AI agent <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Example AI Agent Overview

The example AI agent discussed is a LangGraph app that uses an OpenAI, Anthropic, or Grok model, depending on the `LLM_MODEL` environment variable <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. It incorporates Asana tools for task and project management, performing CRUD (Create, Read, Update, Delete) operations <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The LangGraph implementation is simple, featuring nodes for model calls and tool handling, with a conditional router for invoking tools or returning responses <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Setting Up the LangServe Endpoint with FastAPI

[[using_fastapi_with_langserve_for_ai_deployment | Using FastAPI with LangServe for AI deployment]] is streamlined. Key steps include:
1.  Importing `FastAPI` and `LangServe` components, along with `Uvicorn` for hosting <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  Importing the function that retrieves the LangGraph runnable <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
3.  Creating a FastAPI app instance <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
4.  Adding Cross-Origin Resource Sharing (CORS) middleware for security policies <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. LangServe supports standard API endpoint security measures <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
5.  Using `LangServe.add_routes` to bind the LangGraph runnable into the FastAPI app <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
6.  Running the app using Uvicorn, typically on `0.0.0.0` with Port `8000` <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

This setup makes it easy to create the API endpoint, which can be run with `python Langserve_endpoints.py` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Modifying the Streamlit Frontend

To make the Streamlit UI interact with the new LangServe endpoint, only three lines of code need to be changed <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:
1.  Import `RemoteRunnable` from LangServe <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
2.  Retrieve the endpoint URL from an environment variable <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
3.  Initialize a `RemoteRunnable` instance with this URL, replacing the direct local runnable <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Cloud Deployment with DigitalOcean

[[configuring_ai_agents_for_cloud_deployment | Configuring AI agents for cloud deployment]] involves several steps on a cloud server like DigitalOcean.

### Creating a Droplet
1.  Access DigitalOcean and navigate to "Droplets" <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
2.  Choose a region (e.g., New York) and keep default data center settings <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
3.  Select Ubuntu as the operating system <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  Opt for a basic plan, with a $7/month option providing 1GB memory and 25GB storage, typically sufficient for this application <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This can be scaled up later if needed <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
5.  Set up authentication using either SSH keys or a strong password <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
6.  Name the droplet and assign tags if desired <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
7.  Create the droplet, which typically spins up in about 20 seconds <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Preparing the Droplet
1.  Access the droplet's console via DigitalOcean <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
2.  Clone the GitHub repository containing the AI agent code <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
3.  Install `python-venv` for creating a virtual environment <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Virtual environments are highly recommended for Python projects <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
4.  Create and activate the virtual environment <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
5.  Navigate to the code directory within the cloned repository <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
6.  Install all required Python packages using `pip install -r requirements.txt --no-cache-dir` <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This process can take several minutes <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
7.  Create a `.env` file and populate it with necessary environment variables, including API keys <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This step is crucial for [[configuring_ai_agents_for_cloud_deployment | configuring AI agents for cloud deployment]].

### Firewall Configuration
To allow external access to the LangServe endpoint, the firewall needs to be configured <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>:
1.  Enable the Uncomplicated Firewall (UFW): `sudo ufw enable` <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
2.  Allow traffic on Port 8000 (or your configured port): `sudo ufw allow 8000` <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
3.  Reload UFW to apply changes: `sudo ufw reload` <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

### Running the LangServe Endpoint
Once the droplet is configured, the LangServe endpoint can be started by running `python Langserve_endpoints.py` <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

## Testing the Deployed AI Agent

[[deploying_and_testing_ai_agents_quickly | Deploying and testing AI agents quickly]] is essential:

1.  **Browser Verification**: Copy the droplet's IPv4 address and navigate to `http://YOUR_IP_ADDRESS:8000/docs` in a browser. This will display the FastAPI documentation page, confirming the LangServe endpoint is live <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
2.  **Frontend Update**: Update the `AGENT_ENDPOINT_URL` environment variable in the frontend's `.env` file with the droplet's IPv4 address and Port 8000 (e.g., `http://YOUR_IP_ADDRESS:8000`) <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. Note that `HTTP` is used for basic setup, not `HTTPS` <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
3.  **Interaction Test**: Use the Streamlit frontend to send a query to the AI agent (e.g., "what projects do I have in Asana?") <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. Verify that the agent responds correctly in the frontend and that the droplet's console shows the execution logs, confirming the API call was processed <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

## Security Considerations

For basic deployment, an unencrypted HTTP endpoint is used without authentication <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. However, LangServe and FastAPI allow for [[secure_deployment_of_ai_agents | secure deployment of AI agents]], including setting up SSL (HTTPS) and various authentication methods, just like any other API endpoint <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.