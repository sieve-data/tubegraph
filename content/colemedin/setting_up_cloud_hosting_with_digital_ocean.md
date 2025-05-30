---
title: Setting up cloud hosting with Digital Ocean
videoId: qgH_KFSFMUE
---

From: [[colemedin]] <br/> 

This article outlines the process of [[deploying_ai_applications_to_the_cloud | deploying AI applications to the cloud]] using [[using_digital_ocean_for_cloud_deployment | Digital Ocean]], specifically focusing on how to host a custom-coded [[configuring_ai_agents_for_cloud_deployment | AI agent]] behind a scalable API endpoint using LangServe. The goal is to have the agent running 24/7 in a cloud environment <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Overview of the Deployment Process
The deployment process involves:
1.  Setting up a Fast API endpoint for the agent using LangServe <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
2.  Modifying the front-end Streamlit UI to interact with the new LangServe endpoint <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Deploying the [[configuring_ai_agents_for_cloud_deployment | AI agent]] to a dedicated cloud server on [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
4.  Testing the deployed [[configuring_ai_agents_for_cloud_deployment | AI agent]] to ensure functionality <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Preparing the LangServe Endpoint and Front-End
The code for the LangServe endpoint and [[configuring_ai_agents_for_cloud_deployment | AI agent]] is available in a GitHub repository <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Key files include:
*   `langserve_chatbot.py`: Contains the Streamlit UI (front-end) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   `langserve_endpoints.py`: Defines LangServe endpoints with FastAPI <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   `runnable.py`: Sets up the LangGraph application with defined nodes, LLM interactions, and tool calls <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   `.env.example`: Provides a template for setting up API keys and defining the LLM model <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

The [[configuring_ai_agents_for_cloud_deployment | AI agent]] example uses Asana tools for task and project management (CRUD operations) and can utilize OpenAI, Anthropic, or Grok models <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Setting up the LangServe Endpoint
LangServe simplifies the creation of API endpoints <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. The core setup involves:
*   Importing `FastAPI`, `LangServe`, and `Uvicorn` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   Creating a `FastAPI` instance <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   Adding CORS middleware (for security policies) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Retrieving the LangGraph runnable (or any LangChain chain) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   Using `add_routes` from LangServe to bind the runnable to the FastAPI application <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   Running the app with Uvicorn, typically hosted on `0.0.0.0` with Port 8000 <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Modifying the Front-End (Streamlit UI)
Only three lines of code need to be changed in the Streamlit UI to connect to the new LangServe endpoint <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>:
1.  Import `RemoteRunnable` from LangServe <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
2.  Get the endpoint URL from an environment variable (`AGENT_ENDPOINT_URL`) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
3.  Set up a `RemoteRunnable` instance using this URL, replacing the direct import of the local runnable function <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Deploying to Digital Ocean

### Creating a Digital Ocean Droplet
A Droplet is a flexible Linux-based virtual machine (VM) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
1.  **Login/Sign Up**: Create an account and a new project within [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
2.  **Create Droplet**: Click "Create" then "Droplets" <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Region**: Select a region closest to you (e.g., New York) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
4.  **Operating System**: Choose `Ubuntu` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
5.  **Plan**: Select "Basic" <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
6.  **Droplet Size**: For this application, a "Premium AMD" Droplet at $7/month with 1GB memory and 25GB storage is sufficient <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This can be scaled later if needed <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
7.  **Authentication**:
    *   **SSH Key**: Recommended for security.
    *   **Password**: Easier to manage, but ensure it meets strict security requirements <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
8.  **Finalize**: Give the Droplet a name (e.g., "Lang Serve [[configuring_ai_agents_for_cloud_deployment | AI agent]]") and optionally add tags <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
9.  **Create**: Click "Create Droplet". It typically spins up in about 20 seconds <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Logging into the Droplet
1.  From the [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] dashboard, click the three dots next to your Droplet.
2.  Select "Access Console" <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
3.  Log in as `root` (you can change this user later) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Setting up the Environment on the Droplet
Once logged into the Linux instance:
1.  **Clone Repository**: Git is pre-installed. Clone the [[configuring_ai_agents_for_cloud_deployment | AI agent]]s master class GitHub repository <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```
2.  **Install `python-venv`**: This is for creating virtual environments, which is highly recommended <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
    ```bash
    sudo apt update
    sudo apt install python3-venv
    ```
3.  **Create and Activate Virtual Environment**:
    ```bash
    python3 -m venv ai_agent_venv
    source ai_agent_venv/bin/activate
    ```
    You'll know it's active when your command line prompt starts with `(ai_agent_venv)` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
4.  **Install Python Packages**: Navigate into the specific folder of the cloned repository that contains the code <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. Install dependencies using `pip` from `requirements.txt`.
    ```bash
    cd <code_folder>
    pip install -r requirements.txt --no-cache-dir
    ```
    The `--no-cache-dir` flag is important for Droplets with limited memory (1GB) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. This step can take around five minutes <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
5.  **Create `.env` file**: Create a `.env` file in the same directory and populate it with your environment variables (e.g., API keys, LLM model) <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
    ```bash
    nano .env
    # Paste your environment variables here, e.g.,
    # OPENAI_API_KEY=your_key
    # LLM_MODEL=openai
    # AGENT_ENDPOINT_URL=
    # Press Ctrl+X, then Y, then Enter to save and exit.
    ```

### Configuring the Firewall
To allow external machines to connect to the LangServe endpoint, open Port 8000 in the firewall <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
1.  **Enable UFW (Uncomplicated Firewall)**:
    ```bash
    sudo ufw enable
    ```
2.  **Allow Port 8000**:
    ```bash
    sudo ufw allow 8000
    ```
    If you changed the default port for LangServe, use that port instead <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
3.  **Reload UFW**:
    ```bash
    sudo ufw reload
    ```
    This applies the new firewall configuration <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

### Running the LangServe Endpoint
Execute the LangServe endpoint script:
```bash
python langserve_endpoints.py
```
A success message from LangServe indicates it's running <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

### Verifying the Endpoint
You can verify the endpoint is working before updating your front-end:
1.  Copy the IPv4 address of your [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] Droplet <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
2.  Open a web browser and navigate to `http://<YOUR_DROPLET_IPV4>:8000/docs` <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
3.  A documentation page will appear if the LangServe endpoint is correctly exposed <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

### Connecting the Front-End to the Deployed Agent
Update the `AGENT_ENDPOINT_URL` environment variable in your front-end's `.env` file to reference the Droplet's IPv4 address <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>:
```
AGENT_ENDPOINT_URL=http://<YOUR_DROPLET_IPV4>:8000/
```
*Note*: For simplicity, this setup uses HTTP, not HTTPS <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. Advanced tutorials might cover [[setting_up_ssl_and_dns_for_secure_access | setting up SSL and DNS]] and authentication, which can be implemented like any other API endpoint <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

## Testing the Deployed Agent
Run your Streamlit UI locally after updating the `.env` file <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. Interact with the [[configuring_ai_agents_for_cloud_deployment | AI agent]] through the UI (e.g., "What projects do I have in Asana?") <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. You should observe the output of the [[configuring_ai_agents_for_cloud_deployment | AI agent]]'s execution, including tool calls and print statements, directly on your [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] Droplet's console, confirming the agent is running in the cloud <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

The [[configuring_ai_agents_for_cloud_deployment | AI agent]] is now deployed and running 24/7 in the cloud behind an API endpoint <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

### Resources
*   GitHub repository with code for the LangServe endpoint and [[configuring_ai_agents_for_cloud_deployment | AI agent]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   Commands used for [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] Droplet setup are provided in the video description <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.