---
title: Integrating AI agents with live platforms
videoId: 56D91EcaUnM
---

From: [[colemedin]] <br/> 

The Live Agent Studio is a community-driven platform designed to host and showcase various AI agents <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. It is part of the larger Automator platform <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The primary goal of the Live Agent Studio is to serve as a central hub for open-source agents, fostering learning and growth within the AI community <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.

All agents on the Live Agent Studio are open source, allowing users to:
*   **Try them out** <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Users receive 100 free tokens upon signing up to test agents <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **View the source code** <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This includes n8n workflow JSON files or Python code <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Download and run agents** <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Access extensive documentation** for each agent <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

## Building Agents for the Live Agent Studio

To ensure all agents can be hosted on a single frontend and operate uniformly, a standardization process is required <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. This involves standardizing how agents accept input, output information, and manage conversation history <a class="yt-timestamp" data-t="01:48:02">[01:48:02]</a>. A detailed developer guide and video tutorials are available to assist in making agents compatible <a class="yt-timestamp" data-t="01:50:01">[01:50:01]</a>.

### Standardization Requirements
An [[understanding_ai_agents | AI agent]] must be configured to:
*   **Act as an API endpoint**: This is typically achieved using a webhook trigger within platforms like [[integrating_ai_agents_with_services_like_slack | n8n]] <a class="yt-timestamp" data-t="01:49:41">[01:49:41]</a>.
*   **Handle specific input parameters**: The agent needs to process parameters like `query`, `user ID`, `request ID`, and `session ID` <a class="yt-timestamp" data-t="01:52:20">[01:52:20]</a>. The `session ID` is crucial for linking messages to a specific conversation <a class="yt-timestamp" data-t="01:52:26">[01:52:26]</a>.
*   **Manage conversation history**: The Live Agent Studio's chat memory is compatible with PostgreSQL, often used via Superbase <a class="yt-timestamp" data-t="01:50:30">[01:50:30]</a>. The AI agent node in n8n can automatically create the necessary messages table in a PostgreSQL database <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>.
*   **Standardize output**: The workflow should output a simple JSON indicating `success` as `true` or `false` <a class="yt-timestamp" data-t="01:57:01">[01:57:01]</a>. All AI messages and responses are stored directly in the database <a class="yt-timestamp" data-t="01:57:36">[01:57:36]</a>. This allows for real-time reporting of agent actions to the user interface <a class="yt-timestamp" data-t="01:55:11">[01:55:11]</a>.

### Prototyping and Tool Integration with n8n

n8n is a recommended no/low-code tool for building and prototyping AI agents <a class="yt-timestamp" data-t="01:56:01">[01:56:01]</a>. It allows for quick development without focusing on the frontend or database initially <a class="yt-timestamp" data-t="02:05:15">[02:05:15]</a>.

A prototype for a GitHub assistant agent was built using n8n and Gemini 2.0 Flash <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>:
*   **AI Agent Node**: The core component is the AI agent node in n8n, which supports attaching chat models, memory, and tools <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
*   **Chat Model**: Gemini 2.0 Flash was chosen for its speed, especially when processing large outputs <a class="yt-timestamp" data-t="01:57:46">[01:57:46]</a>. API keys for Gemini can be obtained from the Google AI Studio <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
*   **Memory**: For prototyping, a window buffer memory is sufficient as it uses local storage for conversation history <a class="yt-timestamp" data-t="02:19:50">[02:19:50]</a>. For production, PostgreSQL/Superbase or Redis are recommended for persistent memory <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>.
*   **System Prompt**: A system message is crucial for defining the agent's role and expected behavior <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>. For the GitHub assistant, it outlines that the agent is a coding expert with GitHub access and should begin responses with the repository link for continuous context <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.
*   **Tool Calling**:
    *   **"Get Repo Structure" Tool**: This tool calls an n8n sub-workflow to retrieve the entire file structure of a GitHub repository <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>. It extracts the organization and repository name from the URL using JavaScript with regular expressions <a class="yt-timestamp" data-t="00:57:28">[00:57:28]</a>. The GitHub API is then used to fetch the file tree <a class="yt-timestamp" data-t="00:59:11">[00:59:11]</a>.
    *   **"Get File Content" Tool**: This tool retrieves the content of specific files within a GitHub repository <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>. It combines the repository URL with the file path to access the raw file content via the GitHub API <a class="yt-timestamp" data-t="01:12:27">[01:12:27]</a>.
*   **Workflow Triggering**: A single `Execute Workflow` trigger can be used for multiple tools within a sub-workflow by manually specifying an "action" parameter in the tool call and using a switch node to branch the workflow <a class="yt-timestamp" data-t="01:06:48">[01:06:48]</a>.
*   **Authentication**: GitHub access tokens are required for API calls, and n8n provides clear documentation for setting up credentials <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>.

### Supported Platforms and Technologies
The Live Agent Studio supports a variety of platforms for building agents:
*   [[integrating_ai_agents_with_services_like_slack | n8n]]: A no/low-code workflow automation tool <a class="yt-timestamp" data-t="01:14:11">[01:14:11]</a>.
*   **Python Frameworks**: Including Pydantic AI, LangChain, or custom code using APIs like OpenAI or Anthropic <a class="yt-timestamp" data-t="01:59:32">[01:59:32]</a>. For integration with n8n, Python agents can call n8n workflows exposed as webhooks/API endpoints <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
*   Voiceflow: A no-code platform specifically good for knowledge-based agents with RAG <a class="yt-timestamp" data-t="02:00:28">[02:00:28]</a>. It offers a custom integration with the Live Agent Studio, simplifying API and database management <a class="yt-timestamp" data-t="02:00:37">[02:00:37]</a>.
*   **Docker Containers**: Allows for agents built in any language (Go, Rust, etc.) to be hosted, provided they handle API requests and conversation memory within the container <a class="yt-timestamp" data-t="02:01:22">[02:01:22]</a>.
*   **Frontend Development**: For client-facing chatbots or internal tools, [[integrating_ai_chatbots_on_websites | AI coding assistants]] like Bolt.DIY or Lovable can help build React frontends quickly <a class="yt-timestamp" data-t="02:06:40">[02:06:40]</a>. Streamlit is also a good Python UI library for creating LLM chatbots <a class="yt-timestamp" data-t="02:06:54">[02:06:54]</a>.

## Community and Development
The Live Agent Studio encourages community participation through initiatives like:
*   **Hackathon Competition**: A coding competition with a $5,000 prize pool <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>. Participants build [[understanding_ai_agents | AI agents]] compatible with the Live Agent Studio <a class="yt-timestamp" data-t="01:10:18">[01:10:18]</a>. Registration is free <a class="yt-timestamp" data-t="01:12:25">[01:12:25]</a>.
*   **Open-Source Resources**: The platform's GitHub repository contains all agent source codes and extensive documentation to guide development <a class="yt-timestamp" data-t="01:30:15">[01:30:15]</a>. This includes examples for n8n, Python, and Docker <a class="yt-timestamp" data-t="01:59:51">[01:59:51]</a>.

Future plans for the Live Agent Studio include implementing user authorization for agents that interact with personal services like Slack or Gmail <a class="yt-timestamp" data-t="00:51:56">[00:51:56]</a>.