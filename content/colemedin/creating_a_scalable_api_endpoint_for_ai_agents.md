---
title: Creating a scalable API endpoint for AI agents
videoId: qgH_KFSFMUE
---

From: [[colemedin]] <br/> 

This article details the process of [[transforming_ai_agents_into_api_endpoints | transforming AI agents into API endpoints]] that are scalable and run 24/7 in the cloud <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The core tool used for this is LangServe, which creates an API wrapper around an [[building_ai_agents | AI agent]] built with LangChain or LangGraph <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This method is applicable to any agent built using LangChain <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Why Deploy AI Agents to the Cloud?

Running [[building_ai_agents | AI agents]] locally is not sustainable long-term. Deployment to the cloud ensures 24/7 operation and scalability <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Key Steps to Deployment

The process involves:
1.  Setting up a Fast API endpoint for the agent using LangServe <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  Making minor code changes (three lines) in the front end (Streamlit UI) to interact with the new LangServe endpoint <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
3.  [[Deploying and scaling AI agents with Docker | Deploying the AI agent]] to a dedicated cloud server, such as DigitalOcean <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
4.  Testing the deployed [[building_ai_agents | AI agent]] to ensure functionality <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Code Overview

The code for the LangServe endpoint and the [[building_ai_agents | AI agent]] is available in a GitHub repository <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Key files include:
*   `langserve_chatbot.py`: Contains the Streamlit UI (front end) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   `langserve_endpoints.py`: Defines the LangServe endpoints with Fast API <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   `runnable_pine.py`: Sets up the LangGraph app with defined nodes, LLM interactions, and tool calls <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   `env.example`: Provides a template for setting up API keys and defining the LLM model <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### LangGraph App

The example [[building_ai_agents | AI agent]] uses an OpenAI, Anthropic, or Grok model based on an environment variable <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. It integrates Asana tools for CRUD operations on tasks and projects <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The LangGraph workflow includes nodes for calling the model and handling tool calls, with a conditional router to direct execution <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This simple implementation focuses on demonstrating deployment rather than advanced agent capabilities <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### LangServe Endpoint Setup

LangServe simplifies endpoint creation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. The process involves:
1.  Importing `FastAPI` and `LangServe` (along with `uvicorn` for hosting) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  Creating a `FastAPI` instance <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
3.  Adding CORS middleware (security policies can be tightened) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
4.  Using `add_routes` from LangServe to bind the LangGraph runnable (or any LangChain chain) into the Fast API app <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
5.  Running the app with `uvicorn` on a specified host and port (e.g., `0.0.0.0` with Port `8000`) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
This setup requires only three lines of code <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### Front-End Changes

Only three lines of code are needed in the front end (Streamlit UI) to connect to the new LangServe endpoint <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>:
1.  Import `RemoteRunnable` from LangServe <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
2.  Retrieve the endpoint URL from an environment variable <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
3.  Instantiate `RemoteRunnable` with the endpoint URL instead of directly getting the runnable <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Cloud Deployment with DigitalOcean

DigitalOcean is used to deploy the [[building_ai_agents | AI agent]] to a dedicated cloud server <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Droplet Creation

1.  **Select Droplets**: From the "Create" dropdown, choose "Droplets" <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
2.  **Region & Data Center**: Select the closest region (e.g., New York) and keep the default data center <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
3.  **Operating System**: Ubuntu is a common choice <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  **Plan**: A basic plan is usually sufficient <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
5.  **Droplet Size**: The $7/month option (Premium AMD, 1GB memory, 25GB storage) is suitable for this application and can be scaled later <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Larger options are available for more memory or storage <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
6.  **Authentication**: Passwords are often easier to manage than SSH keys, provided they meet strict security requirements <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
7.  **Name & Tags**: Assign a descriptive name (e.g., "Lang Serve AI agent") <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

The droplet typically spins up within 20 seconds <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Droplet Setup (Linux Instance)

1.  **Access Console**: Click the three dots on the droplet, then "Access Console" to open a new browser tab with the Linux instance <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Log in as `root` <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
2.  **Clone Repository**: Git is pre-installed. Clone the [[building_ai_agents | AI agents]] master class repository <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
3.  **Install `python-venv`**: Install `python-venv` to create a virtual environment, which is highly recommended for Python projects <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
4.  **Create & Activate Virtual Environment**: Create a virtual environment and activate it using the `source` command <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. The command line prefix will change to indicate the active environment <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
5.  **Install Python Packages**: Navigate to the folder containing the code and install all required Python packages using `pip install -r requirements.txt --no-cache-dir`. The `--no-cache-dir` flag is important due to the droplet's 1GB memory <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. This step can take around five minutes <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
6.  **Create `.env` file**: Create a `.env` file using `nano .env` and add all environment variables (e.g., API keys, LLM model) as per `env.example` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Firewall Configuration

Before running the LangServe endpoint, the firewall needs to be opened to allow external access to Port 8000 <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>:
1.  `sudo ufw enable` <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>
2.  `sudo ufw allow 8000` (or your chosen port) <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>
3.  `sudo ufw reload` <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>

### Running the LangServe Endpoint

Execute the LangServe endpoint script: `python langserve_endpoints.py` <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. A successful run will display a LangServe message <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

## Testing the Deployed AI Agent

### Browser Verification

To confirm the endpoint is working, copy the droplet's IPv4 address <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. In a new browser tab, navigate to `http://YOUR_IP_ADDRESS:8000/docs`. This `/docs` endpoint is available for any LangServe runnable and displays documentation, confirming the service is live <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

### Front-End Integration and Testing

1.  **Update `AGENT_ENDPOINT_URL`**: In the front end's `.env` file, update the `AGENT_ENDPOINT_URL` to the droplet's IPv4 address and port (e.g., `http://YOUR_IP_ADDRESS:8000`). Note that this should be `http` (unencrypted) for a basic setup <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
2.  **Run Front End**: Start the front-end application.
3.  **Interact with Agent**: Send a request to the [[building_ai_agents | AI agent]] (e.g., "what projects do I have in Asana?") <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.
4.  **Verify Output**:
    *   The front end will display the agent's response <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.
    *   The DigitalOcean droplet's console will show the standard output from the LangGraph execution, including API calls and print statements, confirming the entire pipeline is functioning <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

## Security Considerations

For a basic deployment, the endpoint is unencrypted HTTP without authentication <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. However, LangServe allows setting up usual API endpoint security like SSL and authentication <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

## Resources

*   GitHub repository with all code for the LangServe endpoint and [[building_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   All commands used for DigitalOcean droplet setup are provided in the video description <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.