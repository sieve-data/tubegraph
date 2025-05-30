---
title: Transitioning from no code to custom code in AI projects
videoId: zf_D2Eafvk0
---

From: [[colemedin]] <br/> 

This article explores the process of building full-scale AI agents, specifically focusing on the transition from a no-code prototype to a production-ready agent using custom Python code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach aims to make the development process more straightforward and manageable <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## The AI Agent Roadmap: From Planning to Production

The development of an AI agent typically follows a roadmap:
1.  **Planning the Agent**: Defining the desired functionality, such as a GitHub code Q&A agent <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a><a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
2.  **Prototyping with No-Code**: Rapidly building a proof of concept using a no-code/low-code tool <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a><a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This step is crucial for breaking down complex problems into smaller, more manageable steps <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a><a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a><a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
3.  **Database Setup**: Setting up a database, like Supabase, to manage message tables for the AI agent <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a><a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
4.  **Transition to Custom Code**: Converting the no-code prototype into a full production-ready agent using a programming framework like Pydantic AI <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a><a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
5.  **Front-End Development**: [[building_and_deploying_custom_ai_front_ends | Building a front end]] for the agent to provide a user interface <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>.
6.  **Adding Functionality and Features**: Enhancing the agent with more capabilities to meet specific needs <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
7.  **Deployment**: [[deploying_ai_applications_without_coding | Deploying the agent into production]] <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

### The Role of No-Code Prototyping

No-code tools like n8n, Voiceflow, and Flowise are excellent for quickly building initial versions of AI agents <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a><a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a><a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. They provide a visual representation of the workflow <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a><a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a><a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a> and can serve as a direct blueprint for custom coding <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

A key benefit of starting with a no-code prototype is that the structure of the agent (e.g., in n8n) can directly guide the custom coding process, making it surprisingly straightforward <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a><a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. It also helps to keep the development process clear by separating the planning and prototyping from the actual coding <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a><a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a><a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

Furthermore, no-code workflows can be downloaded as JSON representations <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a><a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, which can then be provided to [[using_ai_coding_assistance | AI coding assistants]] like Windsurf or Cursor. This gives the assistant a clear understanding of what needs to be built <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a><a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a><a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Why Transition to Custom Code?

While no-code tools are valuable for rapid prototyping, transitioning to custom coding often becomes necessary for greater control and customization <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a><a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a><a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This allows for building truly production-grade agents that fit specific needs <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a><a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.

## Building with Pydantic AI: A Custom Code Example

The process of [[advancing_ai_agents_with_python_and_custom_coding | advancing AI agents with Python and custom coding]] using Pydantic AI involves three main steps:

### 1. Setting Up Dependencies
Dependencies for the agent include HTTP clients for API interactions and API keys for authorization (e.g., GitHub token) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a><a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a><a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a><a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a><a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. Environment variables are loaded for API keys and the choice of Large Language Model (LLM) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a><a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a><a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **LLM Configuration**: Pydantic AI allows flexible LLM selection, enabling users to choose between models like Deepseek V3, Gemini, Claude, Cohere, or Mistral by overriding the base URL and API key to use services like OpenRouter <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a><a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a><a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a><a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a><a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

### 2. Defining the Agent Instance
The core agent instance is defined by:
*   **System Prompt**: Directly copied from the no-code prototype (e.g., n8n's system message) to avoid reinventing the wheel <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a><a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Model**: The configured LLM (e.g., Deepseek V3 via OpenRouter) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Dependencies**: The previously defined dependencies are passed to the agent <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Retry Logic**: Pydantic AI includes built-in retry logic to handle common issues like rate limit errors when calling LLMs <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a><a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a><a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

### 3. Setting Up Tools for the Agent
Pydantic AI simplifies tool creation by using Python decorators (`@agent.tool`) on regular Python functions <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a><a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a><a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a><a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Docstrings**: A docstring (comment at the top of the function) is used to tell the LLM when and how to use the tool, including its purpose and expected arguments <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a><a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a><a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Leveraging [[using_ai_coding_assistance | AI coding assistants]]**: While AI coding assistants might not be experts in specific agent frameworks, they excel at creating tool functions that interact with well-established APIs like the GitHub API <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a><a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a><a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a><a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a><a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. By providing them with the JSON of the no-code workflow, they can understand the required functionality <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a><a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a><a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a><a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a><a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

For a GitHub code Q&A agent, examples of tools include:
*   **`get_repo_metadata`**: Retrieves information like repository size, number of files, and stars <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a><a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a><a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
*   **`get_repo_structure`**: Extracts the organization and repository from a URL and makes API calls to get the content of the main (or master) branch, returning the entire structure of the repository, including nested folders and files <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a><a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a><a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a><a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a><a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
*   **`get_file_content`**: Fetches the contents of a specific file path within a GitHub repository <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a><a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a><a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.

### Managing Conversation History and Tool Calls
It is important to include tool calls and their responses in the conversation history <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a><a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>. This allows the LLM to reference previous tool outputs without needing to invoke the same tool again, making the agent more efficient <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a><a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a><a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

## Framework Choice and Best Practices

While Pydantic AI is a preferred framework for its ease of setup and control <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a><a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>, many other frameworks like LlamaIndex, CrewAI, and LangChain are also available <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a><a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. The general concepts and best practices discussed, such as managing conversation history and API keys, are applicable across different frameworks <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a><a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a><a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Conclusion

By starting with a simple concept, prototyping with no-code tools like n8n, and then transitioning to a custom-coded Python agent using Pydantic AI, it's possible to build a flexible, powerful, and affordable AI agent <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a><a class="yt-timestamp" data-t="00:28:31">[00:28:31]</a><a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a><a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a><a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a><a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a><a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. This layered approach provides a solid foundation for further development, including [[building_and_deploying_custom_ai_front_ends | building a front end]] and ultimately [[deploying_ai_applications_without_coding | deploying the agent into production]] <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a><a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a><a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.