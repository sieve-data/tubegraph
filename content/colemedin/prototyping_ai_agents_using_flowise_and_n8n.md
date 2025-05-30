---
title: Prototyping AI agents using Flowise and n8n
videoId: 23s2N3ug8B8
---

From: [[colemedin]] <br/> 

The future of AI is moving towards running everything locally, including Large Language Models (LLMs), Retrieval Augmented Generation (RAG) pipelines, and workflow automations <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This approach is demonstrated by the `local_ai_starter_kit` developed by the [[n8n_in_creating_ai_agents | n8n]] team, which provides a proof of concept for local AI needs <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. While open-source LLMs are still catching up to closed-source ones, the gap is rapidly diminishing <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

Recently, Open Web UI was added to the `local_ai_starter_kit` for interacting with [[n8n_in_creating_ai_agents | n8n]] agents via a locally hosted UI <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Now, Flowise is being integrated to enhance the `prototyping_ai_agents_using_n8n` process <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Why Flowise and n8n?

[[n8n_in_creating_ai_agents | n8n]] remains a preferred no-code AI automation platform due to its integration capabilities with hundreds of applications <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. However, [[n8n_in_creating_ai_agents | n8n]] can have a steeper learning curve, especially when [[building_ai_agents_with_n8n | building AI agents]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Flowise, a low/no-code AI automation tool, is free, open-source, and built on LangChain <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It simplifies the process of `prototyping_ai_agents_using_n8n`, making it a go-to platform for quickly creating AI agents <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The beauty of Flowise is its speed in building <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### The Perfect Combination

The combination of Flowise and [[n8n_in_creating_ai_agents | n8n]] is ideal for `prototyping_ai_agents_using_n8n` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. While anything achievable in Flowise can technically be done in [[n8n_in_creating_ai_agents | n8n]], Flowise excels at rapid `prototyping_ai_agents_using_n8n` <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Flowise can be integrated with [[n8n_in_creating_ai_agents | n8n]] by using [[n8n_in_creating_ai_agents | n8n]] workflows as agent tools to interact with services like Slack and Google Drive <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Setting Up the Environment

The entire setup can be done within the `local_ai_starter_kit` <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Prerequisites
*   GitHub Desktop <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>
*   Docker Desktop <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>

### Installation and Running
1.  Clone the `local_ai_package` repository using `git clone` <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
2.  Navigate into the `Local AI package` directory <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
3.  Rename `env.example` to `.env` and configure `n8n_in_creating_ai_agents` encryption settings and PostgreSQL <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
4.  Run `docker compose up -d` to start all services defined in the `docker-compose.yml` file <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This file defines services like Flowise and [[n8n_in_creating_ai_agents | n8n]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   Flowise typically runs on Port 3001, while Open Web UI uses Port 3000, and [[n8n_in_creating_ai_agents | n8n]] uses Port 5678 <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Building an AI Agent in Flowise with n8n Tools

A "Tool Agent" node is used as the starting point in Flowise <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Core Components of a Flowise Agent
*   **Memory**: Start with a simple "Buffer Memory" or use PostgreSQL, which is part of the `local_ai_starter_kit` <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Chat Model**: Use an `Ollama` model (e.g., `llama2.5-coder-32b`) <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
    *   **Base URL**: To reference `Ollama` running on the host machine from within a Flowise container, use `host.docker.internal` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. If `Ollama` is running in its own container within the `local_ai_starter_kit`, reference it by its container name (e.g., `ollama`) <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
    *   **Context Window Size**: It's crucial to increase the default context window size (e.g., to 32,000 tokens) to prevent truncation of conversation history or tool outputs <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **Cache**: An in-memory cache can be used, but Redis is recommended for more robust solutions <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Tools**: Agents require tools. An initial tool can be a web search API like Brave Search API <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. Credentials for tools can be set up centrally in Flowise <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

### Integrating n8n Workflows as Custom Tools
To integrate [[n8n_in_creating_ai_agents | n8n]] workflows, they are set up as "Custom Tools" in Flowise <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

#### n8n Workflow Setup
*   Every [[n8n_in_creating_ai_agents | n8n]] tool workflow starts with a "Webhook" trigger (GET or POST) and ends with a "Respond to Webhook" node <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   Authentication (e.g., Bearer token) can be set up for webhooks <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   Workflows must be active to be callable via their production URL <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   When one container talks to another (e.g., Flowise to [[n8n_in_creating_ai_agents | n8n]]), the container name (e.g., `n8n`) should be used in the URL instead of `localhost` <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

#### Custom Tool Definition in Flowise
*   **Name and Description**: Provide a name and a descriptive text for the tool. The description helps the LLM determine when to use the tool <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
*   **Input Schema**: Define the properties (name, type, description) the tool expects as input. This tells the LLM how to call the tool <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
*   **Code**: Use basic JavaScript to make an API request to the [[n8n_in_creating_ai_agents | n8n]] workflow's production URL <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
*   **Variables**: Sensitive information like bearer tokens should be set up as variables outside the tool code and referenced using `$` `vars.variable_name` <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

### Examples of n8n Tools and their Integration
1.  **Get PostgreSQL Tables**: Queries tables in the PostgreSQL database hosted within the `local_ai_starter_kit` <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. The [[n8n_in_creating_ai_agents | n8n]] workflow references the PostgreSQL service by its container name <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
2.  **Summarize a Slack Conversation**: Fetches messages from Slack and summarizes them using an LLM (e.g., GPT-4 mini) <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>. This requires an [[n8n_in_creating_ai_agents | n8n]] instance hosted with HTTPS and a real domain, as slack credentials cannot be set up on `localhost` <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
3.  **Create a Google Doc**: Creates a Google Drive file based on provided text and title <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>. Similar to Slack, this often requires an [[n8n_in_creating_ai_agents | n8n]] instance hosted on a domain <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.
4.  **Send a Message in Slack**: Sends a message to a specific Slack channel <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>. The channel can be hardcoded or made a parameter for the agent to determine dynamically <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

## Demonstration of Combined Power

The combined Flowise and [[n8n_in_creating_ai_agents | n8n]] agent can perform complex tasks requiring multiple tool calls:
*   **Summarize Slack & Web Search**: An agent can summarize a Slack conversation and then use a web search tool to find information related to the conversation's problem <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>.
*   **Create Google Doc with Findings**: After researching, the agent can create a concise Google Doc outlining its findings, automatically determining the title and content <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
*   **Send Slack Message with Link and Summary**: The agent can then send a Slack message containing the link to the newly created Google Doc and a summary of its findings <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.

This seamless integration of Flowise and [[n8n_in_creating_ai_agents | n8n]] allows for the rapid `prototyping_ai_agents_using_n8n` and deployment of powerful AI agents that can interact with various applications and perform non-trivial tasks <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.