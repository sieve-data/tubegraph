---
title: Setting up and using MCP servers
videoId: SS5DYx6mPw8
---

From: [[colemedin]] <br/> 

## What are MCP Servers?

[[mcp_servers_for_ai_coding | MCP servers]] are a method for providing additional tools to an AI IDE, allowing it to perform actions such as web searches with Brave API <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>. They act as connectors, enabling AI applications like Claude Desktop or custom AI agents to interact with services such as Superbase, giving the AI access to tools for database operations <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.

## Key MCP Servers and Their Uses

There are three core [[musthave_mcp_servers_for_ai_coding | MCP servers]] commonly used to enhance an AI coding assistant's capabilities:

1.  **File System Server** <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>
    *   **Purpose**: Allows the AI IDE to interact with the local file system, not just the current project folder <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>.
    *   **Applications**:
        *   Pulling assets (e.g., images) into a project from other folders <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>.
        *   Referencing other projects to learn from previous implementations <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.

2.  **Brave API (Web Search) Server** <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>
    *   **Purpose**: Enables the AI IDE to perform web searches, utilizing Brave API's AI-powered summarization of search results for powerful output <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
    *   **Applications**:
        *   Pulling documentation for tools, libraries, or frameworks <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>.
        *   Finding examples and documentation by searching the internet <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>.

3.  **Git Server** <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>
    *   **Purpose**: Facilitates interaction with Git repositories for version control, backups, and managing different project versions <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.
    *   **Applications**:
        *   Creating Git commits to save the current state of a project <a class="yt-timestamp" data-t="15:10:00">[15:10:10]</a>.
        *   Reverting to a previous working state if the AI IDE introduces issues, preventing "state of hell" scenarios <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.

Other [[mcp_servers_for_ai_coding | MCP servers]] can be used for tasks like long-term memory or [[building_a_new_rag_mcp_server | implementing RAG (Retrieval-Augmented Generation)]] within an AI IDE, such as the Quadrant [[mcp_servers_for_ai_coding | MCP server]] <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.

## Configuring MCP Servers

To configure [[building_mcp_servers | MCP servers]] in an AI IDE (e.g., Windsurf), follow these steps:
1.  Access the configuration settings for [[mcp_servers_for_ai_coding | MCP servers]] (e.g., "Configure MCP" in Windsurf) <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.
2.  Edit the `MCP config.json` file to add the desired servers <a class="yt-timestamp" data-t="16:27:00">[16:27:00]</a>.
3.  Specify the command to your Python executable within the virtual environment and arguments pointing to your server <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>.
4.  Pass environment variables (e.g., API keys, service keys) for secure connections <a class="yt-timestamp" data-t="22:45:00">[22:45:00]</a>.
5.  Restart the AI IDE or associated application (e.g., Claude Desktop) for changes to take effect <a class="yt-timestamp" data-t="22:54:00">[22:54:00]</a>.

## Using MCP Servers in the AI Coding Workflow

[[building_and_using_mcp_servers | MCP servers]] are integrated throughout the AI coding workflow to enhance productivity:

### Initial Project Setup
*   **Planning Phase**: While planning documents can be created using chatbots (e.g., Claude Desktop) <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>, [[mcp_servers_for_ai_coding | MCP servers]] can facilitate the creation and management of these high-level markdown documents (e.g., `planning.md` and `task.md`) by providing context to the LLM <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
*   **Initial Prompt**: When giving the initial prompt to the AI IDE, [[web_search_with_mcp_servers | web search with MCP servers]] (like Brave) can be used to pull documentation, while the file system server can provide examples from other projects <a class="yt-timestamp" data-t="18:04:00">[18:04:00]</a>.

### Iteration and Development
*   **Context Provision**: The AI coding assistant can be prompted to reference planning files, especially at the beginning of new conversations, using the capabilities granted by [[mcp_servers_for_ai_coding | MCP servers]] <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.
*   **Task Management**: The AI can update, create, delete, and mark tasks as done in the `task.md` file, allowing the user to act as a project manager <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
*   **Git Integration**: The Git [[mcp_servers_for_ai_coding | MCP server]] allows the AI to make commits to save the current state of a project, which is crucial for creating backups and reverting to stable versions if the AI introduces issues <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>.
*   **[[managing_databases_with_mcp_servers | Database Management]]**: For example, a Superbase [[mcp_servers_for_ai_coding | MCP server]] allows the AI to interact with a database, performing operations like creating, reading, updating, and deleting records <a class="yt-timestamp" data-t="20:55:00">[20:55:00]</a>.

### Deployment
*   **Docker Integration**: LLMs are proficient at working with Docker due to extensive training data <a class="yt-timestamp" data-t="29:41:00">[29:41:00]</a>. They can help create Docker files to package and deploy applications, including generating necessary build commands <a class="yt-timestamp" data-t="29:51:00">[29:51:00]</a>.

## Benefits and Considerations

*   **Enhanced Productivity**: By providing powerful tools and context, [[mcp_servers_for_ai_coding | MCP servers]] significantly increase the AI's capability, leading to higher quality and more consistent outputs <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
*   **Reduced Hallucinations**: Properly configured [[mcp_servers_for_ai_coding | MCP servers]] that provide specific context help reduce LLM hallucinations, which are more likely with longer, less focused contexts <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
*   **Security**: While [[mcp_servers_for_ai_coding | MCP servers]] enable powerful interactions, users must implement environment variables themselves and not trust the LLM with API keys or database security <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. Understanding the code produced by AI, especially regarding security, is critical <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Complexity**: [[challenges_and_solutions_in_mcp_server_development | Building MCP servers]] from scratch can be complex, and a dedicated video is planned for more in-depth instruction <a class="yt-timestamp" data-t="21:51:00">[21:51:00]</a>.