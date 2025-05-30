---
title: Using FastAPI with LangServe for AI deployment
videoId: qgH_KFSFMUE
---

From: [[colemedin]] <br/> 

Imagine having the full capabilities of a custom-coded AI agent running continuously behind a scalable API endpoint in the cloud [00:00:00]. This article details how to achieve this by deploying an AI agent built with [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] and LangGraph to the cloud as an API endpoint using LangServe [00:00:13].

LangServe is a tool that creates an API wrapper around AI agents, making them accessible via a single endpoint [00:00:23]. This is crucial for moving AI agents off local computers and deploying them to the cloud for 24/7 operation and scalability [00:00:41].

## LangServe as an API Wrapper

LangServe can wrap any [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] chain or LangGraph application [00:00:31]. The process of integrating a [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] agent with a LangServe endpoint requires only three lines of code changes in the frontend Streamlit UI [00:00:53].

## Setting up the FastAPI Endpoint with LangServe

The first step is to set up a FastAPI endpoint for the agent using LangServe [00:01:06]. The primary files involved include:
*   `langserve_chatbot.py`: The Streamlit UI frontend [00:02:02].
*   `langserve_endpoints.py`: Defines the LangServe endpoints with FastAPI [00:02:09].
*   `runnable.py`: Contains the LangGraph application with defined nodes and interactions [00:02:14].

### LangGraph App Overview

The example LangGraph app uses an AI agent configured to interact with either OpenAI, Anthropic, or Grok models based on an environment variable [00:03:01]. This agent is equipped with various Asana tools for task and project management, including CRUD operations (create, read, update, delete) for tasks and projects [00:03:11].

The LangGraph implementation includes:
*   A node for calling the model with bound tools [00:03:44].
*   A node for handling tool calls [00:03:48].
*   A conditional router that directs to the tool node if the agent wants to invoke a tool, otherwise it returns the response directly to the user [00:03:50].

This basic LangGraph executable is then bound into the FastAPI endpoint to be served with LangServe [00:04:18].

### Defining LangServe Endpoints with FastAPI

Setting up the LangServe endpoints is straightforward [00:04:37]:
1.  **Imports:** Import `FastAPI` and `langserve` packages, along with `uvicorn` for hosting [00:04:41].
2.  **FastAPI Instance:** Create a `FastAPI` application instance [00:04:58].
3.  **Middleware:** Add CORS middleware to handle cross-origin requests [00:05:04]. LangServe allows for standard API endpoint security configurations [00:05:14].
4.  **Add Routes:** Utilize LangServe's `add_routes` function to integrate the LangGraph runnable into the FastAPI application, binding the routes [00:05:27].
5.  **Run with Uvicorn:** The final step involves using `uvicorn` to run the FastAPI app, typically hosted on `0.0.0.0` with port `8000` [00:05:41].

This setup creates the API endpoint, which can be run with `python langserve_endpoints.py` [00:06:03].

## Frontend Integration with LangServe Endpoint

To enable the frontend to interact with the new LangServe endpoint, only three lines of code need to be changed in the Streamlit UI [00:01:11]:
1.  Import `RemoteRunnable` from `langserve` [00:06:17].
2.  Retrieve the endpoint URL from an environment variable [00:06:19].
3.  Instead of directly getting the runnable, set up a `RemoteRunnable` instance using the obtained URL [00:06:23].

## [[Deploying an AI agent using LangServe | Deploying the AI Agent to the Cloud]] using DigitalOcean

The article provides a step-by-step guide to [[deploying an AI agent using LangServe | deploying the AI agent]] to a dedicated cloud server using DigitalOcean for approximately $7 per month [00:01:19].

### DigitalOcean Droplet Setup
1.  **Create Droplet:** In DigitalOcean, select "Create" -> "Droplets" [00:07:12].
2.  **Region and OS:** Choose the closest region (e.g., New York) and keep Ubuntu as the operating system [00:07:22].
3.  **Plan:** Select the "Basic plan" and the "Premium AMD" option for $7 a month [00:07:33]. Larger options are available for more memory or storage if needed [00:07:44].
4.  **Authentication:** Choose either an SSH key or a password for authentication. Passwords are generally easier to manage but must meet strict security requirements [00:08:14].
5.  **Naming:** Give the droplet a descriptive name (e.g., "Lang Serve AI Agent") [00:08:42].
6.  **Create:** Click "Create Droplet." The droplet should spin up within about 20 seconds [00:08:51].

### Accessing the Droplet and Setup
1.  **Access Console:** Click the three dots next to the droplet and select "Access Console" to log in as root [00:09:07].
2.  **Clone Repository:** Git is pre-installed. Clone the AI agents masterclass Git repository containing the code [00:09:24].
3.  **Install Python Virtual Environment:** Install `python-venv` to create a virtual environment [00:09:53].
    *   `sudo apt update`
    *   `sudo apt install python3.10-venv`
4.  **Create and Activate Virtual Environment:** Create a virtual environment and then activate it [00:10:16].
    *   `python3 -m venv ai_agent_venv`
    *   `source ai_agent_venv/bin/activate`
5.  **Install Python Packages:** Navigate into the specific folder of the Git repo containing `runnable.py`, `langserve_endpoints.py`, and `langserve_chatbot.py` [00:10:59]. Then, install all required Python packages from `requirements.txt` [00:11:10]. This process can take around five minutes [00:11:47].
    *   `pip install -r requirements.txt --no-cache-dir`
6.  **Create `.env` File:** Create a `.env` file (e.g., using `nano .env`) and populate it with environment variables such as API keys and the LLM model to be used [00:12:09].
7.  **Set up Firewall:** Open up port `8000` in the droplet's firewall to allow external connections [00:12:39].
    *   `sudo ufw enable`
    *   `sudo ufw allow 8000`
    *   `sudo ufw reload`
8.  **Run LangServe Endpoint:** Execute the `langserve_endpoints.py` script to start the API endpoint [00:13:31].
    *   `python langserve_endpoints.py`

## Testing the Deployed AI Agent

### Verifying the Endpoint
To verify the endpoint is working, copy the droplet's IPv4 address from DigitalOcean, paste it into a browser, and append `:8000/docs` [00:13:51]. A documentation page should appear, confirming the LangServe runnable is operational [00:14:10].

### Connecting Frontend and Testing
1.  **Update Frontend `.env`:** In the local frontend code's `.env` file, update the `AGENT_ENDPOINT_URL` to reference the droplet's IPv4 address and port (e.g., `http://YOUR_IPV4:8000`) [00:14:48]. It's important to note that for this basic setup, `http` is used, not `https` [00:15:05].
2.  **Run Frontend:** Start the Streamlit frontend.
3.  **Make Request:** Pose a query to the AI agent (e.g., "What projects do I have in Asana?") [00:15:49].
4.  **Observe Output:** The response will be displayed in the frontend, and the DigitalOcean droplet's console will show the standard output from the LangGraph execution, including tool calls and print statements [00:16:11].

This confirms that the AI agent is deployed, running 24/7 in the cloud, and accessible via the API endpoint [00:16:29].

### Security Considerations
The basic setup outlined here uses an unencrypted HTTP endpoint without authentication [00:15:23]. However, LangServe and FastAPI allow for setting up full security policies, including SSL and authentication, just like any other API endpoint [00:05:09].

## Resources
All code for the LangServe endpoint and the AI agent, along with the commands used for DigitalOcean deployment, are available in a GitHub repository [00:01:37].