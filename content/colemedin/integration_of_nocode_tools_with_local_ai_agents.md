---
title: Integration of nocode tools with local AI agents
videoId: 23s2N3ug8B8
---

From: [[colemedin]] <br/> 

The future of AI is moving towards running everything locally, including LLMs, RAG pipelines, and workflow automations <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This shift empowers users by keeping all necessary AI capabilities on their personal computers <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. While open-source LLMs are not yet as powerful as closed-source alternatives, the gap is rapidly diminishing <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Local AI Starter Kit
The Local AI Starter Kit, developed by the [[n8n_in_creating_ai_agents | n8n]] team, provides a proof of concept for running AI needs locally <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This kit previously integrated Open Web UI to interact with [[n8n_in_creating_ai_agents | n8n]] agents via a locally hosted UI <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, and now includes Flowise <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The primary prerequisites for the Local AI Starter Kit and Flowise are GitHub Desktop and Docker Desktop <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## Flowise: A Nocode AI Automation Tool
Flowise is a free, open-source, low-code/[[nocode_ai_automation_platforms | nocode AI automation platform]] built on LangChain <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It is particularly effective for rapid prototyping of AI agents <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a> <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Flowise can be easily installed using `npm` or Docker <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, with the Docker Compose file used to integrate it into the Local AI Starter Kit <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. By default, Flowise runs on Port 3000, but it can be configured to run on Port 3001 to avoid conflicts with Open Web UI <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## [[n8n_in_creating_ai_agents | n8n]]: A Nocode AI Automation Platform
[[n8n_in_creating_ai_agents | n8n]] remains a preferred [[nocode_ai_automation_platforms | nocode AI automation platform]] due to its extensive integration capabilities with hundreds of applications <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. While it has a steeper learning curve, especially for [[building_ai_agents_with_nocode_tools | building AI agents]], it offers powerful workflow automation <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Combining Flowise and [[n8n_in_creating_ai_agents | n8n]] for AI Agent Development
The combination of Flowise and [[n8n_in_creating_ai_agents | n8n]] offers a robust approach to [[building_ai_agents_with_nocode_tools | building AI agents]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
Flowise excels at quickly prototyping AI agents, while [[n8n_in_creating_ai_agents | n8n]] workflows can serve as custom agent tools for interaction with various applications like Slack and Google Drive <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Setting up the Agent in Flowise
An agent in Flowise starts with a "Tool Agent" node, which connects to memory, a chat model, and caching <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

*   **Memory**: Options include basic buffer memory or more robust solutions like PostgreSQL, which is part of the Local AI Starter Kit <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Chat Model**: Ollama can be used as the local LLM <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. When configuring Ollama:
    *   The base URL `host.docker.internal` references Ollama running on the host computer, useful for avoiding model reinstallation within containers <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   Alternatively, `olama` (the container name) can be used to reference the Ollama instance running within the Local AI Starter Kit container <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
    *   It is crucial to increase the context window size (e.g., to 32,000 tokens) from the default 2048 to prevent truncation of conversation history or tool outputs, which can lead to poor performance and hallucinations <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Caching**: In-memory caching can be used, with Redis being a recommended option for more robust applications <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

### [[creating_tools_and_dependencies_for_ai_agents | Creating Tools and Dependencies for AI Agents]]
Tools are required for a Flowise tool agent <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

*   **Brave Search API**: This can be integrated as a web search tool, requiring an API key stored as a credential within Flowise <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **[[n8n_in_creating_ai_agents | n8n]] Workflows as Custom Tools**:
    *   **Workflow Setup**: [[n8n_in_creating_ai_agents | n8n]] workflows must start with a Webhook trigger (GET or POST) and end with a "Respond to Webhook" node <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Authentication (e.g., Bearer token) can be configured <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
    *   **Custom Tool Code (Flowise)**: A "Custom Tool" node in Flowise uses basic JavaScript to make API requests to the [[n8n_in_creating_ai_agents | n8n]] workflows <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
        *   The tool needs a descriptive name and description, which tells the LLM when to use the tool <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
        *   An input schema defines the properties (e.g., database name, message content) the LLM needs to provide for the tool <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
        *   The `workflowUrl` in the custom tool code must reference the [[n8n_in_creating_ai_agents | n8n]] container name (e.g., `n8n`) instead of `localhost` when containers are communicating <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.
        *   Credentials like bearer tokens should be stored as variables in Flowise and referenced in the custom tool code using `$.vars.variableName` to avoid hardcoding <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
    *   **Examples of Integrated [[n8n_in_creating_ai_agents | n8n]] Tools**:
        *   **Querying PostgreSQL Tables**: An [[n8n_in_creating_ai_agents | n8n]] workflow can query a locally hosted PostgreSQL database (part of the Local AI Starter Kit) to retrieve table names <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
        *   **Summarizing Slack Conversations**: An [[n8n_in_creating_ai_agents | n8n]] workflow can fetch Slack messages and summarize them using an LLM (e.g., GPT-4 mini) <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Note: For Slack and Google Drive integrations, [[n8n_in_creating_ai_agents | n8n]] often requires an HTTPS-enabled domain, not just `localhost` <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
        *   **Creating Google Docs**: An [[n8n_in_creating_ai_agents | n8n]] workflow can create Google Drive files based on text and a title provided by the AI agent <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
        *   **Sending Slack Messages**: An [[n8n_in_creating_ai_agents | n8n]] workflow can send messages to a specific Slack channel <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>.

### Demonstrating Agent Capabilities
By combining these tools, an AI agent can perform complex tasks requiring multiple tool calls and reasoning:

*   Summarizing a Slack conversation and then researching a problem identified in the summary (e.g., Elon Musk's net worth using Brave Search) <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
*   Creating a Google Doc summarizing findings from web research <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
*   Sending a Slack message with the Google Doc link and a summary of findings <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.

This demonstrates the power of using [[n8n_in_creating_ai_agents | n8n]] and Flowise together to [[integrating_mcp_with_ai_agents | build AI agents]] and rapidly prototype solutions <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.