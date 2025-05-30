---
title: Building AI agents with Pydantic AI
videoId: zf_D2Eafvk0
---

From: [[colemedin]] <br/> 

This article details the process of transforming an n8n prototype of an AI agent into a production-ready Python agent using the Pydantic AI framework <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This is the third video in a miniseries demonstrating the entire process of [[building_fullscale_ai_agents | building fullscale AI agents]], from planning to prototyping and, ultimately, coding <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Why Pydantic AI?

Pydantic AI is highlighted as a preferred framework for [[building_ai_agents | building agents]] due to the control and customization it offers when working with agent code <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. While other frameworks like LlamaIndex, CrewAI, and LangChain exist, Pydantic AI provides an easy setup while maintaining necessary control <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>. The concepts discussed are generally applicable across different frameworks <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

## The AI Agent Roadmap & N8n Prototype as a Blueprint

The development process follows an [[understanding_ai_agents | AI agent roadmap]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>:
1.  **Plan the Agent**: Define the desired functionality, such as a GitHub code Q&A agent <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  **Prototype with No/Low-Code Tool**: Use tools like n8n, Voiceflow, or Flowise to quickly build a proof of concept <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. The n8n workflow serves as a visual reference and structural guide for the Python coding process <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
3.  **Set up Database**: Manage messages created by the agent (e.g., using Supabase) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
4.  **Transition to Python with Pydantic AI**: Convert the n8n prototype into a Python-based agent <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

Prototyping with n8n simplifies the coding process by breaking down complex problems and providing a clear structure <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:01:03">[00:01:05]</a>. The n8n workflow can even be downloaded as a JSON file and provided to an AI coding assistant (like WindSurf or Cursor) to aid in the coding process <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Key Components of a Pydantic AI Agent

When [[building_ai_agents_from_scratch_with_python | building AI agents from scratch with Python]] using Pydantic AI, three main elements are critical:

1.  **Dependencies**: Define necessary components like an HTTP client and API keys (e.g., GitHub token) that the agent will use when invoking tools <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
2.  **Agent Definition**: Create the agent instance, specifying the large language model (LLM) to use (e.g., DeepSeek V3 through OpenRouter), the system prompt, and handling dependencies <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Pydantic AI includes built-in retry logic for LLM calls <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. The system prompt can be directly copied from the n8n prototype to maintain consistency <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Tools**: Define the functions available to the agent <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
    *   **Decorator**: A standard Python function is transformed into an agent tool by adding the `@agent_name.tool` decorator <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
    *   **Docstring**: A docstring above the function explains to the LLM *when* and *how* to use the tool, including its purpose and arguments <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
    *   **AI Coding Assistants**: AI coding assistants are highly effective for creating these tools, especially when dealing with well-established APIs like the GitHub API. They can leverage the n8n workflow JSON as a reference <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>, <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

## Example: GitHub Code Q&A Agent

The demonstration focuses on a GitHub code Q&A agent capable of consuming entire GitHub repositories for information <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It uses the new DeepSeek V3 LLM via OpenRouter for powerful and cost-effective operation, with the flexibility to switch to other LLMs like Gemini, Claude, or Mistral <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

The agent's tools include:
*   **Get Repository Metadata**: A new tool not present in the initial n8n prototype, allowing the agent to provide information like repository size, number of files, or stars <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>, <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   **Get Repository Structure**: Extracts the organization and repository from a GitHub URL and makes calls to the GitHub API to get the contents of the main branch, with a fallback to the master branch <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>, <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. This provides the LLM with the full structure of the repository, including nested folders and files <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.
*   **Get File Content**: Retrieves the content of a specific file from the repository, also with main/master branch fallback <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

The agent demonstrates intelligent processing by potentially calling multiple tools to answer a single user question, such as first getting the repository structure and then the content of a specific file <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Command Line Interface (CLI)

A simple command-line interface (CLI) is created for immediate interaction with the agent <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. This CLI manages conversation history, allowing the agent to reference previous tool calls (e.g., repo structure) without re-invoking them <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>. The agent can respond to queries about the repository's metadata, structure, and specific file contents <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>, <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

## Advancing AI Agents with Python and Custom Coding

The process of [[advancing_ai_agents_with_python_and_custom_coding | advancing AI agents with Python and custom coding]] provides greater control and customization compared to no-code tools <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This approach establishes a solid foundation for a flexible, powerful, and affordable AI agent <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>.

Future steps in the series will involve:
*   Building a front-end interface for the agent <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.
*   Adding more functionality and features to meet specific needs <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
*   Deploying the agent into production <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.