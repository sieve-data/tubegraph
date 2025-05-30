---
title: Local LLMs for AI agent swarms
videoId: 8jpVeUTNExI
---

From: [[colemedin]] <br/> 

OpenAI recently released an experimental tool called [[OpenAI Swarm AI Tool | Swarm]], which simplifies the creation of collaborative [[understanding_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. By default, [[OpenAI Swarm AI Tool | Swarm]] utilizes OpenAI models like GPT-4o <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. However, it's possible to use [[Local AI agents with Olama | Ollama]] to run [[AI Agent Orchestration with Swarm | swarms of agents]] locally on your machine <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

Using [[OpenAI Swarm AI Tool | Swarm]] with GPT models can be expensive due to token consumption, especially with function calling <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. In contrast, using [[Local AI agents with Olama | Ollama]] is completely free <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Initial testing with smaller models running locally has shown good results <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Ollama's OpenAI Compatibility
[[Local AI agents with Olama | Ollama]] supports function calling in the exact same format as OpenAI models <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This compatibility was added around July 25th <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The key feature is "OpenAI compatibility," which allows users to send requests as if they were targeting GPT, but override the API's base URL to point to a local [[Local AI agents with Olama | Ollama]] instance <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This is achieved by importing the OpenAI library and setting up chat completion as usual, but changing the `base_url` parameter to `http://localhost:11434` (the default [[Local AI agents with Olama | Ollama]] host) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This URL can be modified if [[Local AI agents with Olama | Ollama]] is hosted on a different port or external machine <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Integrating Ollama with Swarm
The default [[OpenAI Swarm AI Tool | Swarm]] setup instantiates an OpenAI client without parameters, relying on an `OPENAI_API_KEY` environment variable and connecting to the OpenAI API directly <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. To use [[Local AI agents with Olama | Ollama]], the only necessary change is to implement the `base_url` override and provide an API key (even a placeholder since [[Local AI agents with Olama | Ollama]] doesn't require one) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

This modification is done when instantiating the [[AI Agent Orchestration with Swarm | Swarm]] client, rather than forking or changing the core [[OpenAI Swarm AI Tool | Swarm]] code itself <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. By passing a custom [[Local AI agents with Olama | Ollama]] client to the [[AI Agent Orchestration with Swarm | Swarm]] instance, it will use local models <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Code Changes for Ollama Integration
1.  **Environment Variable File**: An `.env` file can be used to define the default model for agents <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Since [[Local AI agents with Olama | Ollama]] doesn't need an API key, this file primarily defines the `LLM_MODEL` (e.g., `qwen:2.5b-coder`) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  **Agent Model Definition**: While a default model can be set via environment variable, individual agents can also be configured to use specific models <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, a router agent might use a lightweight model like `qwen:0.5b` (3 billion parameters), while other agents use a more capable one like `qwen:2.5b-coder` (7 billion parameters) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This allows for diverse model usage (e.g., Qwen, Mistral) within the same swarm <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
3.  **Swarm Instance Creation**: In the `run.py` script where the [[AI Agent Orchestration with Swarm | Swarm]] instance is created, the `openai` instance needs to be established with the new `base_url` and a placeholder `api_key` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This customized client is then passed to the `Swarm` constructor <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

```python
# Example of client setup (simplified from transcript)
from openai import OpenAI

# Set up Ollama client with OpenAI compatibility
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="anything" # API key is not required for Ollama, but some value is needed
)

# Pass the custom client when instantiating the Swarm
swarm = Swarm(client=client)
```
<a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>

## SQL AI Agent Swarm Demonstration
A previously built SQL [[understanding_ai_agents | AI agent]] swarm is used to demonstrate local LLM integration <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This swarm interacts with an RSS feed database, storing articles, user information, and feed data <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The swarm's purpose is to query the database for analytics or user engagement information <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. To avoid overwhelming a single LLM, the task is split among multiple agents:
*   **Router Agent**: Takes the initial user request and determines which specialized agent can best create a SQL query (SELECT statement) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **RSS Feed Agent**: Creates queries related to RSS feeds, such as retrieving articles <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Analytics Agent**: Handles analytics-related questions, potentially performing joins on multiple tables <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **User Agent**: Responds to user-related queries. <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>

Each agent can be instructed with different behaviors, allowing for specialized responses tailored to their function <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Demonstration Queries and Results
*   **"How many users are on the platform?"** <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>
    *   Response time: ~15 seconds (on a laptop with a 3060 GPU) <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    *   Router agent directed to the user agent <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   Result: "There are currently five users on the platform" <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   **"Do some analytics for me. I want to know what the most popular RSS feed is."** <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>
    *   Response time: ~10 seconds <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   Transferred to the analytics agent <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
    *   Generated a more complex SQL select statement with a join on the `feeds` view <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
    *   Result: "The most popular RSS feed is ml weekly with six views" <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

The local models, even smaller ones like the 7-billion parameter Qwen, performed well for SQL agent tasks <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. A laptop with a 3060 GPU can quickly run 7-billion and 3-billion parameter models <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Larger models like 32-billion parameter Code Llama might require more powerful hardware, such as a 3080 or 3090 graphics card <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

## Setup Guide for Local Swarm Agents
To run your own [[Local AI agents with Olama | Ollama]] [[AI Agent Orchestration with Swarm | Swarm]] agents:

### 1. Install Ollama
*   Download [[Local AI agents with Olama | Ollama]] from [ollama.com](https://ollama.com/) <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. It supports Mac, Linux, and Windows <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

### 2. Prepare Environment
*   **Prerequisites**: Ensure Python and Git are installed <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
*   **Clone Repository**:
    ```bash
    git clone [repository_url_for_AI_agents_Master_Class]
    ```
    <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>
*   **Navigate to Project Directory**:
    ```bash
    cd local-swarm-agent-folder
    ```
    <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>
*   **Create Virtual Environment**:
    ```bash
    python -m venv venv
    ```
    <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>
*   **Activate Virtual Environment**:
    *   **Windows**:
        ```bash
        ./venv/Scripts/activate
        ```
        <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>
    *   **Linux/Mac**:
        ```bash
        source venv/bin/activate
        ```
        <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>
*   **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>
    This installs [[OpenAI Swarm AI Tool | Swarm]] from the OpenAI Git repository and other necessary packages <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

### 3. Configure Ollama Models and Environment Variables
*   **Find Tool-Calling Models**: Visit [ollama.com/search](https://ollama.com/search) and go to the "Tools" tab <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
    *   Select a model that has the "tool" label, as these support tool calling necessary for [[OpenAI Swarm AI Tool | Swarm]] agents <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
    *   Choose a model based on your computer's capabilities (e.g., 7 billion parameters or below for weaker computers, 32 or 72 billion for powerful GPUs) <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Pull Models**:
    ```bash
    ollama pull [model_id_e.g._qwen:2.5b-coder]
    ```
    <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>
    *   This may take a while as models are typically multiple gigabytes <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   **Configure `.env` file**:
    *   Rename the `env.example` file in the repository to `.env` <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
    *   Set the `LLM_MODEL` variable to the ID of the [[Local AI agents with Olama | Ollama]] model you pulled (e.g., `LLM_MODEL=qwen:2.5b-coder`) <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. This will be the default model for your agents <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
    *   Individual agents can still be hardcoded to use different specific models <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.

## Future of Local LLMs
While GPT models still offer better performance compared to local models like Qwen, the gap between open-source and proprietary large models is rapidly diminishing <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. The ability to run complex [[AI Agent Orchestration with Swarm | AI agent swarms]] with smaller local models is a significant development <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.