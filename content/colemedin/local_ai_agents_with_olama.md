---
title: Local AI agents with Olama
videoId: 8jpVeUTNExI
---

From: [[colemedin]] <br/> 

OpenAI's experimental tool, Swarm, allows users to easily create collaborative [[defining_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While Swarm defaults to OpenAI models like GPT-4o, it's possible to create agent swarms that run entirely locally using Olama <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This approach offers significant cost savings, as running Swarm with GPT can be expensive due to token usage, whereas using Olama is free <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Initial testing with smaller Olama models has shown good results <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Olama's OpenAI Compatibility for Agent Swarms

Olama supports function calling in the same format as OpenAI models <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. A key feature is Olama's OpenAI compatibility, which allows requests to be sent to Olama's local server by overriding the API's base URL <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This means the OpenAI library can still be used, but the `base_url` parameter is changed to point to `localhost:11434` (Olama's default host) instead of OpenAI's API <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This simple change eliminates the need for an OpenAI API key for authentication when running locally <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Integrating Olama with Swarm

The core modification to integrate Swarm with Olama involves instantiating the Swarm with a custom OpenAI client configured to use Olama's base URL <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
Previously, the Swarm setup would instantiate an OpenAI client without parameters, relying on an `OPENAI_API_KEY` environment variable and OpenAI's default API <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. To use Olama, the `base_url` is explicitly set to `http://localhost:11434/v1` and the `api_key` can be set to "ollama" (or any placeholder, as no actual key is needed) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This client is then passed to the Swarm instance <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Flexible Model Selection
[[running_ai_agents_on_local_machines | Running AI agents on local machines]] with Olama offers significant flexibility in choosing models <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Unlike OpenAI's limited model options (e.g., GPT-4o mini, GPT-4o), Olama provides access to dozens, even hundreds, of open-source models like Qwen and Mistral <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Users can define a default model (e.g., `qwen:2.5b-coder`) via an environment variable <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a> and assign different models to [[specialized_ai_agents | specialized AI agents]] within the swarm <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Example: SQL AI Agent Swarm

An example application of [[building_ai_agents | building AI agents]] with Olama is a SQL agent swarm designed to query an RSS feed database <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This swarm addresses the complexity of having a single [[understanding_ai_agents | AI agent]] handle diverse SQL queries by splitting tasks among multiple [[specialized_ai_agents | specialized AI agents]] <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

The swarm consists of:
*   **Router Agent:** Takes initial user requests and directs them to the appropriate [[specialized_ai_agents | specialized agent]] <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. For example, a lightweight 3 billion parameter model might be used for the router, as it doesn't make tool calls <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **RSS Feed Agent:** Creates SQL queries to retrieve information from the RSS feed database <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Analytics Agent:** Handles analytics-related questions, potentially performing joins across multiple tables to generate complex queries <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Each [[ai_agents_and_their_development | agent]] can be instructed with specific behaviors, allowing for tailored responses based on their specialization <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Demo Results
In a demonstration using Qwen 2.5 3B for the router and Qwen 2.5 Coder 7B for the SQL-writing agents, the system performed well <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Simple Query:** When asked "How many users are on the platform?", the router successfully routed the request to the user agent, which executed a simple count query and returned the correct answer within ~15 seconds <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Complex Query:** For "What is the most popular RSS feed?", the request was routed to the analytics agent, which generated a more complex SQL query involving table joins. This was completed within ~10 seconds and provided the correct analytic result <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

The performance on a laptop with a 3060 GPU running 7 billion and 3 billion parameter models was "really, really quickly" <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Larger models like a 32 billion parameter Code Llama might require more powerful hardware (e.g., 3080 or 3090 graphics card) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>, but smaller models run well on most computers <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

## Setting up Local Olama Swarm Agents

To run your own Olama Swarm agents locally, follow these steps:

1.  **Install Olama:**
    *   Download Olama from `ollama.com` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. It's available for Mac, Linux, and Windows <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

2.  **Clone the Repository:**
    *   Ensure Python and Git are installed <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
    *   Clone the AI Agents Master Class repository: `git clone [repository URL]` <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
    *   Change directory into the `local_swarm_agent` folder <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

3.  **Create and Activate a Virtual Environment:**
    *   Create a virtual environment: `python -m venv venv` <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
    *   Activate the virtual environment:
        *   **Windows:** `.\venv\Scripts\activate` <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>
        *   **Linux/Mac:** `source venv/bin/activate` <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>

4.  **Install Dependencies:**
    *   Install Python packages from `requirements.txt`: `pip install -r requirements.txt` <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. This ensures the correct versions of Swarm and other dependencies are installed <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

5.  **Configure Olama Models:**
    *   Go to `ollama.com/search` and select the "Tools" tab <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. Only models with the "Tool" label support tool calling, which is essential for Swarm agents <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
    *   Select your desired model size (e.g., 7 billion parameters or below for weaker computers, 32 or 72 billion for powerful setups) <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
    *   Copy the model ID (e.g., `qwen:2.5b-coder`) <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
    *   Pull the model using Olama: `ollama pull [model_ID]` <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. Models can be multiple gigabytes and take time to download <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

6.  **Set Environment Variables:**
    *   Rename the `env.example` file in the repository to `.env` <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
    *   Set the `LLM_MODEL` variable in the `.env` file to the Olama model ID you pulled (e.g., `LLM_MODEL=qwen:2.5b-coder`) <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. This will be the default model for your agents <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
    *   Optionally, you can hardcode specific models for different agents within your Python code (e.g., `router_llm` and `agent_llm`) <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.

7.  **Run the Swarm:**
    *   Execute the `run.py` script: `python run.py` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This will start the Swarm instance, allowing you to interact with your [[ai_agents_and_their_development | AI agents]] running on [[local_llms_for_ai_agent_swarms | local LLMs]] <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

The ability to run [[local_llms_for_ai_agent_swarms | local LLMs]] for [[ai_agents_and_their_development | AI agents]] demonstrates a promising future, with the performance gap between open-source models and proprietary models like GPT rapidly diminishing <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. This makes [[running_ai_agents_on_local_machines | running AI agents on local machines]] an exciting and accessible frontier <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>.