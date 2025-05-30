---
title: Using Flowise and n8n for local AI automation
videoId: 23s2N3ug8B8
---

From: [[colemedin]] <br/> 

The future of AI is expected to involve running everything locally, including LLMs, RAG pipelines, and [[workflow_automation_with_n8n | workflow automations]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This approach makes it possible to have all necessary AI power on your computer <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. While open-source LLMs are not yet as powerful as closed-source ones, this gap is quickly diminishing <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Local AI Starter Kit
A few months prior to this video, the speaker covered the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]] developed by the [[ai_automation_with_n8n | n8n]] team, which served as a proof of concept for running AI needs locally <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This video became the most viewed on the channel <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. More recently, Open Web UI was added to the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]] to allow interaction with [[ai_automation_with_n8n | n8n]] agents via a beautiful, locally hosted UI <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Flowise has now been integrated into this kit <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Flowise Overview
Flowise is a free, open-source, low/no-code AI automation tool built on LangChain <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It excels at quickly [[prototyping_ai_agents_using_flowise_and_n8n | prototyping AI agents]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Flowise is backed by Y Combinator and is easy to install via npm or Docker <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The project's GitHub repository provides instructions for running it with Docker and setting up environment variables, including user authentication <a class="yt-timestamp" data-t="00:02:58">[00:03:00]</a>.

## n8n Overview
[[ai_automation_with_n8n | n8n]] is a favored no-code AI automation platform, particularly for its integration with hundreds of applications <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. It has a steeper learning curve, especially when building AI agents <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## The Perfect Combo: Flowise and n8n
Flowise pairs very well with [[ai_automation_with_n8n | n8n]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Flowise's simplicity makes it ideal for rapidly [[prototyping_ai_agents_using_flowise_and_n8n | prototyping AI agents]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. These agents are integrated with [[ai_automation_with_n8n | n8n]] because [[ai_automation_with_n8n | n8n]] workflows serve as agent tools to interact with services like Slack and Google Drive <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This combination allows for building AI agents quickly that can perform a wide range of tasks <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Anything that can be done in Flowise can technically be done in [[ai_automation_with_n8n | n8n]], but Flowise simplifies rapid building <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Setting Up the Local AI Starter Kit
To get started with Flowise and [[ai_automation_with_n8n | n8n]] together within the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]], the prerequisites are GitHub Desktop and [[docker_setup_for_flowise_and_n8n | Docker Desktop]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Installation Steps
1.  **Clone the repository:** Perform a `git clone` of the starter kit repository <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
2.  **Navigate to the directory:** Change into the `Local AI package` directory <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
3.  **Configure environment variables:** Rename the `env.example` file to `.env` and adjust PostgreSQL settings or [[ai_automation_with_n8n | n8n]] encryption settings as needed <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
4.  **Start Docker Compose:** Run `docker compose up` (or `docker-compose` on Linux) with appropriate flags for GPU or CPU <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This will pull necessary images and spin up services like [[ai_automation_with_n8n | n8n]], Quadrant, PostgreSQL, and Flowise <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Accessing Services
*   **Docker Desktop:** Provides real-time logs and the ability to execute commands within containers, useful for debugging <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Flowise:** Accessible via `localhost:3001` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **n8n:** Accessible via `localhost:5678` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Open Web UI:** Accessible via `localhost:3000` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

> [!NOTE]
> When one container needs to communicate with another (e.g., Flowise to [[ai_automation_with_n8n | n8n]]), you must reference the container name (e.g., `n8n`) instead of `localhost` <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. Similarly, to reference the host machine (e.g., for a locally running Olama instance), use `host.docker.internal` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## Building an AI Agent with Flowise and n8n

The demonstration focuses on [[creating_custom_ai_workflows_with_n8n | creating custom AI workflows with n8n]] as tools for a Flowise agent, all within the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]] <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Flowise Agent Setup
1.  **Start a Chat Flow:** Begin with a classic chat flow in Flowise <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
2.  **Add Tool Agent Node:** Drag in a `Tool Agent` node, which acts as the core of the agent <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
3.  **Configure Memory:** Add a `Buffer Memory` node (PostgreSQL can also be used if part of the kit) and connect it to the agent <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
4.  **Set up Chat Model (Olama):**
    *   Add a `Chat Olama` node and connect it to the agent <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   Set the **Base URL** to `host.docker.internal` if Olama is running on the host machine, or the container name (`olama`) if it's within the Docker container <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   Specify the **Model Name** (e.g., `qwen:2.5-coder-32b`), which can be found using `olama list` in the terminal <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
    *   Adjust **Context Window Size**: It's crucial to increase the default 2048 tokens to prevent truncation of conversation history or tool outputs, recommending a size like 32,000 <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
5.  **Add Caching (Optional):** An in-memory cache can be added; Redis is recommended for robust builds <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Integrating Tools
The agent needs tools, marked as required by a red asterisk <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

1.  **Web Search Tool (Brave Search API):**
    *   Add a `Brave Search API` node and connect it <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
    *   Set up credentials by providing a Brave Search API key. These credentials can be managed globally in Flowise <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
    *   Test the agent: A query like "Search the web and tell me Elon Musk's Net Worth" should trigger the tool and provide a current answer <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Flowise shows which tool was used, its input, and output <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

2.  **[[using_n8n_for_api_workflows_in_ai_agents | n8n Workflows as Custom Tools]]:**
    *   [[ai_automation_with_n8n | n8n]] workflows serve as API endpoints for Flowise agents <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. All [[ai_automation_with_n8n | n8n]] tools start with a Webhook trigger and end with a Respond to Webhook node <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
    *   **Custom Tool Node:** In Flowise, add a `Custom Tool` node for each [[ai_automation_with_n8n | n8n]] workflow <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   **Tool Definition:** Provide a descriptive name and description for the tool. The description helps the LLM decide when to use the tool <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. Define the input schema (properties, types, descriptions) to guide the LLM on *how* to call the tool <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
    *   **Code for API Request:** Use basic JavaScript to make an API request to the [[ai_automation_with_n8n | n8n]] workflow. Reference the [[ai_automation_with_n8n | n8n]] container name (`n8n`) and port (`5678`) for locally hosted instances <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
    *   **Variables:** Sensitive information like Bearer tokens should be set up as variables outside the tool code using the "Variables" tab in Flowise, then referenced using `$vars.variableName` <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

#### Example [[ai_automation_with_n8n | n8n]] Tools:

*   **Get PostgreSQL Tables:**
    *   This tool queries tables in a locally hosted PostgreSQL database (part of the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]]) <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
    *   Test query: "What postgress tables do I have?" <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

*   **Summarize Slack Conversation:**
    *   This tool fetches messages from a Slack conversation and summarizes them using an LLM (e.g., GPT-4 Mini) <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.
    *   > [!WARNING]
        > Slack and Google Drive integrations with [[ai_automation_with_n8n | n8n]] require an HTTPS-enabled instance, meaning a hosted domain is necessary, not just `localhost` <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.

*   **Create Google Doc:**
    *   This tool creates a Google Drive file based on provided text and title, determined by the AI agent <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.

*   **Send Message in Slack:**
    *   This tool sends a message to a specific Slack channel (e.g., `flowise-n8n`) <a class="yt-timestamp" data-t="00:25:22">[00:25:22]</a>.

### Multi-Tool Execution Demonstration
A complex request can test the agent's ability to use multiple tools: "Summarize the slack conversation [channel name] and do some research on the problem given there" <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>. This triggers the Slack summarization tool, followed by the Brave Search tool <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.

Further interaction can chain tools: "Now create a concise Google doc with your findings" <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>. This prompts the agent to reason about parameters (like document title and text) for the Google Doc creation tool <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. Finally, "Send a message in slack with this link and a summary of your findings" <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a> demonstrates sending the generated link and summary to Slack <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.

## Conclusion
Combining Flowise and [[ai_automation_with_n8n | n8n]] allows for the rapid [[prototyping_ai_agents_using_flowise_and_n8n | prototyping of powerful AI agents]] <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>. This integration, especially within the [[setting_up_a_local_ai_starter_kit_with_flowise | local AI starter kit]], enables local AI automation with complex, chained tool actions <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. New sections for [[ai_automation_with_n8n | n8n]] and local AI have been opened in the Automator Think Tank Community, and a collaboration with Zuar on his AI Workshop YouTube channel is planned to focus on [[ai_automation_with_n8n | n8n]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.