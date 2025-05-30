---
title: Integration of Swarm with Olama
videoId: 8jpVeUTNExI
---

From: [[colemedin]] <br/> 

[[openai_swarm_ai_tool | OpenAI]] recently released an experimental tool called [[openai_swarm_ai_tool | Swarm]], which simplifies the creation of AI agents that collaborate to achieve tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. By default, [[openai_swarm_ai_tool | Swarm]] utilizes [[openai_swarm_ai_tool | OpenAI]] models like GPT-4o <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. However, it's possible to integrate [[ai_agent_orchestration_with_swarm | Swarm]] with Olama to run swarms of agents [[local_ai_agents_with_olama | locally on your machine]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This integration allows for cost-free operation, as opposed to the expenses associated with using GPT for function calling in agents, which consumes a significant number of tokens <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Initial testing with [[local_ai_agents_with_olama | smaller local models]] has shown good results <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Why Olama?

Olama supports function calling in the exact same format as [[openai_swarm_ai_tool | OpenAI]] models <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Running [[ai_agent_orchestration_with_swarm | Swarm]] with Olama is completely free, unlike using [[openai_swarm_ai_tool | OpenAI]]'s GPT, which can be expensive due to token usage for function calls <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Additionally, Olama offers a wide range of models (dozens to hundreds of options) that can be used for different agents within a swarm, providing more flexibility than [[openai_swarm_ai_tool | OpenAI]]'s limited model choices <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Olama's [[openai_swarm_ai_tool | OpenAI]] Compatibility

Olama added tool support on July 25th, allowing for [[openai_swarm_ai_tool | OpenAI]] compatibility <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This means a request can be sent as if to GPT, but the base URL for the API call is overridden to point to Olama instead of [[openai_swarm_ai_tool | OpenAI]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

To achieve this, the [[openai_swarm_ai_tool | OpenAI]] library is imported, and the chat completion is set up as usual, but the `base_url` is changed to `http://localhost:11434`, which is Olama's default host port <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This `base_url` can be adjusted if Olama is hosted on a different port or external machine <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Implementing the Integration

The default [[openai_swarm_ai_tool | Swarm]] setup instantiates an [[openai_swarm_ai_tool | OpenAI]] client without parameters, causing it to use the `OPENAI_API_KEY` environment variable and connect to the [[openai_swarm_ai_tool | OpenAI]] API <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. To integrate with Olama, the `base_url` and `api_key` (which isn't needed for Olama, so it can be an empty string) parameters must be passed when instantiating the [[openai_swarm_ai_tool | OpenAI]] client <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

Instead of modifying the [[openai_swarm_ai_tool | Swarm]] code directly, a custom client is passed when instantiating the swarm <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>:

```python
# Set up the OpenAI instance referencing a new base URL and API key for Olama
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="anything" # API key is not needed for Olama, but a value must be supplied
)

# Instantiate the Swarm, passing in the custom Olama client
swarm_instance = Swarm(client=client)
```
<a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>

This allows the existing [[ai_agent_orchestration_with_swarm | Swarm]] code to work with [[local_ai_agents_with_olama | local Olama models]] with minimal changes <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### SQL AI Agent Swarm Example

An example SQL AI agent swarm, previously built for [[openai_swarm_ai_tool | Swarm]], was adapted to work with Olama <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The code is available on GitHub <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

Key changes for this example:
*   **Environment Variable File**: An `.env` file is used to define the default model for agents, for example, `Qwen 2.5 Coder` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Olama does not require an API key <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Model Assignment**: Agents can use the default model from the environment variable, or specific models can be hardcoded for individual agents <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. For instance, a lightweight router agent might use a 3 billion parameter model, while other agents use a 7 billion parameter model <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Demo: SQL AI Agent Swarm with Local LLMs

The demo showcases an [[ai_agent_orchestration_with_swarm | AI agent swarm]] interacting with an RSS feed database <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The swarm is designed to query the database for analytics and user engagement information <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

The swarm architecture involves:
*   **Router Agent**: Takes initial user requests and directs them to specialized agents <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Specialized Agents**:
    *   **RSS Feed Agent**: Creates SQL queries for RSS feed-related questions <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    *   **Analytics Agent**: Handles analytics-related questions, potentially involving complex joins <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
    *   **User Agent**: Responds to user-related queries.

Each agent can be instructed to behave differently, allowing for customized responses based on the query type <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Demo Results

The demo utilized [[local_llms_for_ai_agent_swarms | local LLMs]]: Qwen 2.5 3B for the router agent and Qwen 2.5 Coder 7B for the SQL-writing agents <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

*   **Query 1: "How many users are on the platform?"**
    *   The router agent correctly routed the request to the user agent <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   The user agent generated a simple `COUNT` query and returned the answer: "There are currently five users on the platform" <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   This took about 15 seconds on a laptop with a 3060 GPU <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

*   **Query 2: "Do some analytics for me. I want to know what the most popular RSS feed is."**
    *   The request was transferred to the analytics agent <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
    *   A more complex `SELECT` statement with a `JOIN` on the `feeds` view was generated <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
    *   The correct response was given: "The most popular RSS feed is ml weekly with six views" <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
    *   This took about 10 seconds <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

Despite using [[local_llms_for_ai_agent_swarms | smaller local models]], the performance was noted as "kicking butt," demonstrating that 7 billion parameter models can perform well for SQL agent tasks <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. A laptop with a 3060 GPU was sufficient for running 7 billion and 3 billion parameter models quickly <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Larger models, like 32 billion parameter Code Llama, might require more powerful hardware (e.g., 3080 or 3090 graphics card) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

## Setup Guide for [[local_ai_agents_with_olama | Local AI Agents with Olama]]

To run this setup yourself from scratch:

1.  **Install Olama**:
    *   Go to `olama.com` and click the download button <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
    *   Olama is available for Mac, Linux, and Windows <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

2.  **Prerequisites**:
    *   Ensure Python and Git are installed on your machine <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

3.  **Clone the Git Repository**:
    *   Use `git clone [repository_url]` to clone the `AI Agents Master Class` repo <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
    *   Navigate into the `local-swarm-agent` folder: `cd local-swarm-agent` <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

4.  **Create and Activate a Python Virtual Environment**:
    *   Create the virtual environment: `python -m venv venv` <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
    *   Activate on Windows: `./venv/Scripts/activate` <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
    *   Activate on Linux/Mac: `source venv/bin/activate` <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
    *   Using virtual environments is crucial for isolating project dependencies and avoiding conflicts <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

5.  **Install Requirements**:
    *   Install the necessary packages from `requirements.txt`: `pip install -r requirements.txt` <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
    *   This will install [[openai_swarm_ai_tool | Swarm]] from the [[openai_swarm_ai_tool | OpenAI]] Git repository and other dependencies <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

6.  **Configure `.env` File and Pull Olama Models**:
    *   Rename the `env_example` file in the repo to `.env` <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
    *   Set the `LLM_MODEL` variable in the `.env` file to your desired Olama model <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
    *   To find compatible models, visit `olama.com/search` and go to the "Tools" tab <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. **Only models with the "tool" label support tool calling, which is essential for [[ai_agent_orchestration_with_swarm | Swarm]] agents** <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
    *   Select the desired parameter size (e.g., 7 billion or below for weaker computers) <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
    *   Pull the chosen model using the Olama command line: `olama pull [model_id]` (e.g., `olama pull qwen2.5:3b`) <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. These models are typically several gigabytes in size <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
    *   Once pulled, the model ID is added to the `.env` file as the default Olama model <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. You can also specify different models manually for individual agents within your code <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.

After these steps, you can run the `run.py` script to test your [[local_llms_for_ai_agent_swarms | local AI agent swarms]] <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

## Conclusion

The ability to run [[ai_agent_orchestration_with_swarm | AI agent swarms]] with [[local_llms_for_ai_agent_swarms | local LLMs]] using Olama is a significant advancement <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. While proprietary models like GPT may still offer better performance, the gap with open-source models is rapidly closing <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. This provides an exciting and accessible way to experiment with [[ai_agent_orchestration_with_swarm | AI agent orchestration]] without high costs <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>.