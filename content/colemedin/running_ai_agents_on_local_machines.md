---
title: Running AI agents on local machines
videoId: 8jpVeUTNExI
---

From: [[colemedin]] <br/> 

OpenAI recently released an experimental tool called Swarm, which simplifies the creation of multiple [[Building AI Agents | AI agents]] that work collaboratively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, Swarm defaults to using OpenAI models like GPT-4o <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. For those interested in [[Running AI locally with n8n and Open WebUI | running AI locally]], it's possible to use Ollama to create swarms of agents on your machine <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

A significant advantage of using Ollama is that it supports function calling in the same format as OpenAI models <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This allows for free local execution, avoiding the costs associated with using GPT models, which can be expensive due to token usage <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Initial tests show promising results even with smaller models <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Integrating Ollama with OpenAI Swarm

Ollama added tool support recently, on July 25th, 2024 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This update included a crucial feature: OpenAI compatibility <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This means you can send requests as if they were going to GPT, but override the API URL to point to Ollama, which typically runs on `localhost:11434` <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

To achieve this, you import the OpenAI library and set up the `ChatCompletion` as usual, but modify the `base_url` parameter <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The default Swarm setup instantiates an OpenAI client without parameters, relying on environment variables for authentication and directing calls to the OpenAI API <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. To use Ollama, you simply change the `base_url` and provide an `api_key` (even a dummy one for Ollama) when instantiating the OpenAI client object that you then pass to the Swarm instance <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This means no changes to the core Swarm code are needed <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Code Changes for Local Swarm Agents

To adapt an existing Swarm project, such as a SQL [[Building AI Agents | AI agent]] swarm, for local Ollama execution, only a few simple changes are required <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

*   **Environment Variables**: Create an `.env` file. Since Ollama doesn't require an API key, you can define an environment variable for the default model, for example, `LLM_MODEL=Quen 2.5 Coder 7B` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This model is well-suited for tasks like generating SQL statements <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Agent Model Configuration**: Within your agent definitions, you can set the `model` parameter for each agent. Agents can use the default `LLM_MODEL` from your environment variable <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Alternatively, you can specify different models for specialized agents, such as using a lightweight `Quen 2.5 3B` model for a router agent <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This flexibility allows agents in a swarm to use various local models like Mistral or other Quen versions <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Swarm Instantiation**: In your `run.py` script where the Swarm instance is created, you establish the OpenAI client with the Ollama base URL and a dummy API key:
    ```python
    client = openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="your-api-key" # Can be a dummy value for Ollama
    )
    swarm_instance = swarm.Swarm(client=client)
    ```
    This single change directs all agent communications to your local Ollama instance <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## SQL AI Agent Swarm Example

This example demonstrates an [[understanding_ai_agents | AI agent]] swarm designed to query an RSS feed database <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The database stores articles, user information, and feed details <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Instead of a single agent handling all queries, the task is split among multiple specialized agents to improve performance <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

The swarm consists of:
*   **Router Agent**: Takes initial user requests and directs them to the most appropriate specialized agent <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. For example, a request about RSS feeds would go to the RSS Feed Agent <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **RSS Feed Agent**: Creates SQL queries to retrieve information from the RSS feed database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Analytics Agent**: Handles analytics-related questions, potentially involving complex queries and table joins <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **User Agent**: Answers questions specifically about users on the platform <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

Each agent can be instructed with unique behaviors or tones <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Testing Local Models

Running the `run.py` script kicks off the Swarm instance using the Ollama base URL <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. The router agent can then receive questions and direct them <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

For testing:
*   The router agent uses `Quen 2.5 3B` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   The SQL query agents use `Quen 2.5 Coder 7B` <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

**Example 1: Simple User Query**
A query like "how many users are on the platform" is routed to the User Agent <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. The agent runs a simple count query and responds, e.g., "There are currently five users on the platform" <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This process took about 15 seconds on a laptop with a 3060 GPU <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

**Example 2: Analytics Query with Joins**
A more complex query, "what the most popular RSS feed is," is routed to the Analytics Agent <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This requires the agent to generate a SQL query with joins on different tables <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>. The agent successfully generated a more complicated select statement with a join and provided the correct answer, e.g., "The most popular RSS feed is ML Weekly with six views" <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This took about 10 seconds <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

Even smaller models like a 7 billion parameter model can perform well for SQL agents <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. A laptop with a 3060 GPU can run 7 billion and 3 billion parameter models quickly <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Larger models, like 32 billion parameter Code Llama, would likely require more powerful hardware, such as a 3080 or 3090 graphics card <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

## Setting Up Your Local AI Agent Swarm

To get your Ollama Swarm agents up and running from scratch:

1.  **Install Ollama**:
    *   Go to `ollama.com` and click the download button <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
    *   Ollama supports Mac, Linux, and Windows <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

2.  **Clone the Repository**:
    *   Ensure you have Python and Git installed <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
    *   Clone the AI Agents Master Class repository:
        ```bash
        git clone [repository_URL]
        ```
    *   Change your directory into the `local-swarm-agent` folder:
        ```bash
        cd local-swarm-agent
        ```

3.  **Create and Activate a Python Virtual Environment**:
    *   Create a virtual environment:
        ```bash
        python -m venv venv
        ```
    *   Activate the virtual environment:
        *   **Windows**:
            ```bash
            .\venv\Scripts\activate
            ```
        *   **Linux/Mac**:
            ```bash
            source venv/bin/activate
            ```
    *   Using a virtual environment isolates project packages, preventing conflicts with other Python projects <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

4.  **Install Dependencies**:
    *   Install packages listed in `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```
    *   This installs Swarm from the OpenAI Git repository and other necessary dependencies, ensuring your setup matches the demo <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

5.  **Configure Environment Variables and Pull Ollama Models**:
    *   Rename `env.example` to `.env` <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
    *   **Find and Pull Ollama Models**:
        *   Visit `ollama.com/search` and go to the "Tools" tab <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
        *   Select models that have the "Tool" label, as these support tool calling necessary for Swarm agents <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
        *   Choose a model based on your system's capabilities (e.g., 7 billion parameters or below for weaker computers) <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.
        *   Copy the model ID <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.
        *   Pull the model using the Ollama command line:
            ```bash
            ollama pull [model_ID]
            ```
            Models are typically several gigabytes and will take time to download <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
    *   Set the `LLM_MODEL` variable in your `.env` file to the model ID you pulled <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
    *   You can also manually set different models for specific agents in your code <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.

Once these steps are completed, you can run the `run.py` script and begin interacting with your local [[Deploying and testing AI agents quickly | AI agents]] <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. While GPT models may still offer better performance, the gap between open-source and closed-source models is rapidly shrinking, making local LLMs a compelling option <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.