---
title: OpenAIs Swarm tool
videoId: 8jpVeUTNExI
---

From: [[colemedin]] <br/> 

[[OpenAI Swarm AI Tool | Swarm]] is a new experimental tool recently released by OpenAI that simplifies the creation of multiple [[ai_agent_orchestration_with_swarm | AI agents]] designed to work collaboratively on complex tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. By default, [[OpenAI Swarm AI Tool | Swarm]] utilizes OpenAI models like GPT-4o <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Integrating [[OpenAI Swarm AI Tool | Swarm]] with Local LLMs via [[integration_of_swarm_with_olama | Olama]]

The primary focus of this content is to demonstrate how to run [[AI agent orchestration with Swarm | Swarm]] with [[integration_of_swarm_with_olama | Olama]], allowing all [[AI agent orchestration with Swarm | agents]] to run locally on a machine <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This approach makes it possible to create [[ai_agent_orchestration_with_swarm | AI agent swarms]] with [[local_llms_for_ai_agent_swarms | local LLMs]] <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### The [[integration_of_swarm_with_olama | Olama]] Advantage
Using [[integration_of_swarm_with_olama | Olama]] with [[OpenAI Swarm AI Tool | Swarm]] offers significant benefits:
*   **Cost-effectiveness** Function calling in [[AI agent orchestration with Swarm | agents]] can consume many tokens, making [[OpenAI Swarm AI Tool | Swarm]] with GPT expensive; however, with [[integration_of_swarm_with_olama | Olama]], it is completely free <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   **Performance** Initial testing has shown good results even with smaller models <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Model Variety** [[integration_of_swarm_with_olama | Olama]] allows for the use of dozens, even hundreds, of different models for [[AI agent orchestration with Swarm | agents]], such as Quen or Mistol, unlike OpenAI's more limited options (e.g., GPT-4o mini vs. GPT-4o) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Function Calling Compatibility** [[integration_of_swarm_with_olama | Olama]] supports function calling in the exact same format as OpenAI models <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This compatibility was added around July 25th <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a> and means [[integration_of_swarm_with_olama | Olama]] can act like it's sending a request to GPT, but with the URL overridden to use [[integration_of_swarm_with_olama | Olama]] instead <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Technical Implementation
To make [[OpenAI Swarm AI Tool | Swarm]] work with [[integration_of_swarm_with_olama | Olama]], only a few simple changes are required <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>:
*   The `openai` library is still imported, and chat completion is set up as usual <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   The `base_url` for the OpenAI API client needs to be changed to `http://localhost:11434` (the default [[integration_of_swarm_with_olama | Olama]] host port) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This can be adjusted if [[integration_of_swarm_with_olama | Olama]] is on a different port or hosted externally <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   The `api_key` can be set to an arbitrary value (e.g., "ollama") since [[integration_of_swarm_with_olama | Olama]] doesn't require an API key <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   When instantiating the [[OpenAI Swarm AI Tool | Swarm]] instance, the custom [[integration_of_swarm_with_olama | Olama]] client is passed in <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>, overriding the default OpenAI setup <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This avoids needing to fork or change the core [[OpenAI Swarm AI Tool | Swarm]] code <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

An environment variable file (`.env`) can be used to define the default model for [[AI agent orchestration with Swarm | agents]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Models like Quen 2.5 coder (7 billion parameters) are suitable for generating SQL statements <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. Agents can also be configured to use different models; for instance, a lightweight router agent might use a 3 billion parameter model like Quen 2.5 3B <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## Demo: SQL AI Agent Swarm

The demo showcases a SQL [[AI agent orchestration with Swarm | AI agent swarm]] designed to query an RSS feed database <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. The database stores articles from news sources, user information, and feed details <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Agent Architecture Overview
To avoid overwhelming a single LLM with diverse SQL query requirements, the system is split into multiple specialized [[AI agent orchestration with Swarm | agents]] <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>:
*   **Router Agent** Takes the initial user request and determines which specialized agent can best create a SQL `SELECT` statement to answer the question <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **RSS Feed Agent** Creates queries related to RSS feeds, retrieves responses, and answers the user <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Analytics Agent** Handles analytics-related questions, potentially joining multiple tables for more complex queries <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **User Agent** Handles user-related questions like counting users <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

Each agent can be instructed with a specific behavior or tone <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Performance with Local Models
The demo uses Quen 2.5 3B for the router and Quen 2.5 coder 7B for the SQL-writing [[AI agent orchestration with Swarm | agents]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Simple Query Example** A query like "how many users are on the platform" is routed to the user agent, which generates a simple count query and responds (took ~15 seconds) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Complex Query Example** A query like "what the most popular RSS feed is" is routed to the analytics agent, which generates a more complicated SQL query involving table joins and correctly identifies the most popular feed (took ~10 seconds) <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

These [[local_llms_for_ai_agent_swarms | local models]] (7 billion parameter model being "tiny" compared to GPT) perform very well <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. The demonstration was run on a laptop with a 3060 G CPU, capable of running these models quickly <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Larger models like a 32 billion parameter Code Llama would likely require more powerful hardware (e.g., 3080 or 3090 graphics card) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. Smaller models can run on almost any computer <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Setting Up Your Own Local [[OpenAI Swarm AI Tool | Swarm]] [[AI agent orchestration with Swarm | Agents]]

To replicate the setup and run [[OpenAI Swarm AI Tool | Swarm]] with [[integration_of_swarm_with_olama | Olama]] locally:

### Prerequisites
*   Install [[integration_of_swarm_with_olama | Olama]] from `ollama.com` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. It supports Mac, Linux, and Windows <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   Ensure Python and Git are installed <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Cloning the Repository
Clone the AI agents Master Class GitHub repository, which contains the SQL agents code <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
```bash
git clone <repository_url>
cd local-swarm-agent # or relevant directory
```

### Python Virtual Environment
Create and activate a Python virtual environment to isolate project dependencies <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### Installing Dependencies
Install the required Python packages and their specific versions using the `requirements.txt` file from the repository <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
```bash
pip install -r requirements.txt
```
This will install [[OpenAI Swarm AI Tool | Swarm]] from the OpenAI Git repository and other dependencies <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

### Configuring [[local_llms_for_ai_agent_swarms | Olama]] Models
1.  Rename `env.example` to `.env` <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
2.  Set the `OLLAMA_MODEL` environment variable to the desired [[local_llms_for_ai_agent_swarms | Olama]] model <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
3.  Pull the chosen [[local_llms_for_ai_agent_swarms | Olama]] model that supports "tool calling" (identified by the "tool" label on `ollama.com/search`) <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
    ```bash
    ollama pull <model_id> # e.g., ollama pull quen:2.5-3b
    ```
    Models can be selected based on parameter size according to machine capabilities <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
4.  Optionally, specific models can be manually set for individual [[AI agent orchestration with Swarm | agents]] in the code, or multiple environment variables can be used <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.

Once configured, the `run.py` script can be executed to start the [[OpenAI Swarm AI Tool | Swarm]] instance with [[local_llms_for_ai_agent_swarms | local models]] <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

## Conclusion

The future of [[local_llms_for_ai_agent_swarms | local LLMs]] is promising, enabling complex tasks with smaller models running on personal computers <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. While GPT models still offer better performance, the gap between open-source and massive closed-source models is rapidly closing <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.