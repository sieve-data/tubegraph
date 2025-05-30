---
title: Creating tools and dependencies for AI agents
videoId: zf_D2Eafvk0
---

From: [[colemedin]] <br/> 

This article, the third in a miniseries on [[building_ai_agents | building AI agents]], focuses on transforming an n8n prototype into a production-ready Python agent using Pydantic AI. The process emphasizes creating essential tools and managing dependencies for a robust agent capable of consuming GitHub repositories for code Q&A <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## AI Agent Development Roadmap: From Prototype to Code

The development process typically follows a roadmap that includes planning, prototyping, and then moving to custom code <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

1.  **Planning the Agent:** The initial step involves defining the agent's purpose, such as a GitHub code Q&A agent <a class="yt-timestamp" data-t="02:15:30">[02:15:30]</a>.
2.  **Prototyping with No-Code Tools:** Prototyping with no-code or low-code tools like n8n, Voiceflow, or Flowise allows for rapid development and definition of the agent's structure <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. This prototype serves as a visual blueprint that guides the coding process <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
3.  **Transition to Custom Code:** While not always necessary, transitioning to custom code, especially with frameworks like Pydantic AI, provides greater control and customization over the agent <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. This step also involves setting up a database, such as Superbase, to manage message history <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

## Pydantic AI: A Preferred Framework

Pydantic AI is highlighted as a favorite [[frameworks_and_tools_for_ai_agent_development | framework for building agents]] due to its ease of setup and comprehensive control <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a> <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Other viable [[frameworks_and_tools_for_ai_agent_development | frameworks]] include LlamaIndex, CrewAI, and LangChain <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. The concepts discussed, such as managing conversation history and API keys, are broadly applicable across different [[frameworks_and_tools_for_ai_agent_development | frameworks]] <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

### Core Components of a Pydantic AI Agent

When setting up an agent with Pydantic AI, three main aspects are crucial:

1.  **Dependencies:** These include necessary components like an HTTP client for external interactions and API keys for authorization <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. These are defined and passed into the agent upon execution <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.
    *   **Example:** For a GitHub agent, dependencies include an HTTP client to interact with the GitHub API and a GitHub token for authorization <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.
2.  **Agent Definition:** This involves specifying the model to be used (e.g., DeepSeek V3 via OpenRouter) and the system prompt <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. Pydantic AI also includes built-in retry logic for handling common issues like rate limit errors from LLMs <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
    *   **Model Flexibility:** OpenRouter allows easy switching between various large language models (LLMs) such as DeepSeek V3, Gemini, Claude, or Mistral, preventing vendor lock-in <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a> <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.
3.  **Tools:** Tools are defined as regular Python functions with a special decorator (`agent.tool`) that makes them available to the LLM <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>. A docstring at the top of each function explains to the LLM when and how to use the tool, including its arguments and purpose <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.

## Leveraging No-Code Prototypes and AI Coding Assistants for Tool Creation

The n8n prototype, while a no-code solution, serves as an invaluable blueprint for coding the agent's tools <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. Its structured workflow simplifies the problem by breaking it into smaller, manageable steps <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

Additionally, the JSON representation of the n8n workflow can be downloaded and provided to AI coding assistants like Windsurf or Cursor. This enables the assistant to understand the required functionality and generate the Python code for the tools <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a> <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>. While AI assistants may not be proficient with agent [[frameworks_and_tools_for_ai_agent_development | frameworks]], they excel at creating tools that interact with well-established APIs like the GitHub API <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.

### Example Tools for a GitHub Agent

For a GitHub code Q&A agent, the following tools are essential:

*   **Get Repository Metadata:** This tool retrieves information about a GitHub repository, such as its size, number of files, and stars, by parsing the GitHub URL and making a request to the GitHub API <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
*   **Get Repository Structure:** This tool fetches the entire file and folder structure of a GitHub repository, including nested elements, from the main or master branch <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. The output is formatted into a single string for the LLM's context <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.
*   **Get File Content:** This tool retrieves the contents of a specific file within a GitHub repository, enabling the agent to analyze its content <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>.

Each tool function utilizes regular expressions to extract the repository owner and name from the GitHub URL, and makes authenticated HTTP requests to the GitHub API <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a> <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a> <a class="yt-timestamp" data-t="19:57:00">[19:57:00]</a>. Error handling is included to inform the LLM if a tool fails <a class="yt-timestamp" data-t="16:53:00">[16:53:00]</a>.

## Managing Conversation History and Tool Calls

Effective conversation history management is crucial for an intelligent agent. When the agent calls a tool, both the LLM's request to use the tool and the tool's response are included in the conversation history <a class="yt-timestamp" data-t="23:12:00">[23:12:12]</a>. This ensures that the LLM can reference previous tool outputs and avoid redundant calls, making the conversation more efficient and coherent <a class="yt-timestamp" data-t="23:56:00">[23:56:00]</a>.

## Next Steps

With a solid foundation for the AI agent established, future steps in the series will involve building a front-end interface, adding more functionalities, and eventually deploying the agent into production <a class="yt-timestamp" data-t="28:51:00">[28:51:00]</a>.