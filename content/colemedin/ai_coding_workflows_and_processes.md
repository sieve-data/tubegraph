---
title: AI coding workflows and processes
videoId: SS5DYx6mPw8
---

From: [[colemedin]] <br/> 

Using an [[ai_coding_assistants | AI coding assistant]] is essential to stay competitive in development today <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, many developers struggle with [[ai_coding_assistants_and_how_to_use_them_effectively | how to use these AI coding assistants effectively]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Without a clear, well-defined process, outputs can be inconsistent, leading to frustration and inefficient development <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A structured workflow ensures high-quality and consistent results when [[using_ai_coding_assistance | using AI to code]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

This article outlines a comprehensive, step-by-step workflow designed to enhance [[ai_coding_assistants_and_their_productivity_benefits | productivity]] when developing with [[ai_coding_assistants | AI]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This process prioritizes simplicity in setup, focuses on building practical and useful examples, and is adaptable to any development project or [[ai_coding_assistants | AI IDE]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Golden Rules for Effective AI Coding <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>

Adhering to specific "golden rules" is foundational for a successful [[ai_coding_assistants | AI coding workflow]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

*   **Utilize High-Level Markdown Documents**
    *   Use markdown files for installation instructions, documentation, planning, and tasks <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   These documents provide crucial context to the Large Language Model (LLM) and can be created and managed with [[ai_coding_assistants | AI]] assistance <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Avoid Overwhelming the LLM**
    *   Longer contexts increase the likelihood of the LLM "hallucinating" <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   Keep all code files under 500 lines <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
    *   Start fresh conversations often, as longer conversations can bog down the LLM <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Request only one new feature or implementation per prompt for better results <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Prioritize Testing**
    *   Ask the [[ai_coding_assistants | AI]] to write tests for its code, ideally after every new feature <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This ensures consistent output <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Be Specific with Requests**
    *   Provide detailed context, including preferred technologies, libraries, and desired output format, rather than just high-level descriptions <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Maintain Documentation and Comments**
    *   Instruct the LLM to constantly update both higher-level documentation files and in-code comments <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This helps both the developer and the [[ai_coding_assistants | AI]] understand the project as it references these files in later conversations <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Handle Environment Variables Manually**
    *   Never trust the LLM with sensitive information like API keys or database security <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Developers must understand and manage these aspects themselves to prevent security breaches <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
    *   *Example*: One user's SAAS product was hacked because he trusted an [[ai_coding_assistants | AI]] to manage environment variables and database security <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Starting a Project: The Planning Phase <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>

Before any coding begins, establish a clear higher-level direction <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

1.  **Create Planning and Task Files:**
    *   **`planning.md`**: Contains the high-level vision, architecture, and constraints, serving as core context for the LLM <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. It helps the LLM quickly grasp the project's scope, especially at the start of new conversations <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
    *   **`task.md`**: Tracks all project tasks, including those completed and those pending <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. The LLM can update, create, or delete tasks, allowing the developer to act as a project manager <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  **Initial Creation with Chatbots**: Use a chatbot like Claude Desktop to generate initial drafts of `planning.md` and `task.md` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. These drafts serve as a good starting point but may require iteration <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
3.  **Leverage Multiple LLMs**: For deeper planning, use platforms like Global GPT that offer access to various LLMs (e.g., Deepseek, Claude) and tools like Deep Research or Perplexity. Combine outputs from different models for a comprehensive plan <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Global Rules: System Prompts for AI Coding Assistants <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>

Global rules function as system prompts, providing high-level instructions to the [[ai_coding_assistants | AI coding assistant]] without needing explicit input in every request <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

*   **Purpose**: They save time by pre-setting behaviors (e.g., "always read the planning file," "write tests for new features," "check off tasks") <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **Setup**: Most [[ai_coding_assistants | AI IDEs]] (like Windsurf, Cursor, Client Root Code) allow configuring global or workspace-specific rules <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Workspace-specific rules are often recommended as project requirements can vary <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Content**: Global rules can dictate how to use markdown files, file size limits (e.g., `< 500` lines), test creation, code style guidelines, and documentation maintenance <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

## Configuring MCP Servers: Expanding AI Capabilities <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>

Model Control Protocol (MCP) servers provide [[ai_coding_assistants | AI IDEs]] with additional tools, extending their functionality <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

*   **Core MCP Servers**:
    *   **File System Server**: Allows the [[ai_coding_assistants | AI IDE]] to interact with the file system beyond the current project directory. This enables pulling assets from other folders or referencing previous projects <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
    *   **Brave API Server**: Facilitates powerful web searches. It uses [[ai_coding_assistants | AI]] to summarize search results, helping the LLM pull documentation for tools, libraries, or frameworks <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
    *   **Git Server**: Crucial for version control. It enables the [[ai_coding_assistants | AI IDE]] to create Git repositories, manage backups, and perform commits, allowing reversion to working states if the project breaks <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Setting Up MCP**: Configuration typically involves editing a `config.json` file within the [[ai_coding_assistants | AI IDE]] to specify the servers and their commands <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

## The Initial Prompt to the AI IDE <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>

The first prompt is critical as it sets the entire starting point for the project <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Despite the existence of planning documents, specificity remains key <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

*   **Provide Extensive Documentation and Examples**:
    *   **Built-in Features**: Many [[ai_coding_assistants | AI IDEs]] have features to pull in documentation directly (e.g., typing `@MCP` in Windsurf to include MCP documentation) <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.
    *   **Web Search**: Use MCP servers for web search (e.g., Brave API) to find relevant documentation or examples online <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
    *   **Manual Provision**: Directly provide links to GitHub repositories or code examples that showcase desired implementations <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   **Specificity in Prompts**: Clearly define what you want the [[ai_coding_assistants | AI]] to build, referencing specific technologies, libraries, and desired outcomes <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.

### Example: Building a Superbase MCP Server <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>

By providing an initial prompt with a GitHub link to an existing Python MCP server implementation and referencing MCP/Superbase documentation, an [[ai_coding_assistants | AI IDE]] like Windsurf can generate a functional Superbase MCP server in a single prompt <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. The [[ai_coding_assistants | AI]] will synthesize information from the example, documentation, and the project's planning/task files <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

*   **Outcome**: A comprehensive implementation (e.g., almost 300 lines of code) with functionalities like creating, reading, updating, and deleting records <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
*   **Verification**: The generated server can be tested by hooking it into a chatbot like Claude Desktop and querying database records, confirming its functionality <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

## Iteration and Testing <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>

After the initial implementation, the workflow focuses on refining the project, adding tests, and maintaining documentation.

*   **One Change at a Time**: Adhere to the golden rule of asking the LLM for only one change or feature implementation per prompt to avoid overwhelming it <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.
*   **Create Tests**:
    *   Instruct the LLM to create unit tests for each implemented feature or tool <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>.
    *   **Best Practices for Testing (Configured in Global Rules)**:
        *   Dedicated test directory <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.
        *   Mock calls to databases and LLMs to ensure fast and free tests <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.
        *   Test successful scenarios, error handling, and edge cases <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.
*   **Maintain Documentation**: Ensure the [[ai_coding_assistants | AI]] updates the `readme` file and other project documentation as new features are added or modified <a class="yt-timestamp" data-t="00:25:59">[00:25:59]</a>.

## Deployment <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>

Once a project reaches a stable and deployable state, the [[ai_coding_assistants | AI coding assistant]] can also assist with packaging and deployment <a class="yt-timestamp" data-t="00:29:25">[00:29:25]</a>.

*   **Docker Integration**: LLMs are proficient at working with Docker due to extensive training data <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>.
*   **Generate Dockerfiles**: Prompt the [[ai_coding_assistants | AI]] to create a Dockerfile for the application, specifying dependencies (e.g., `requirements.txt`) <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **Provide Commands**: The [[ai_coding_assistants | AI]] can also generate the necessary commands to build the Docker container <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.

This end-to-end workflow, from ideation and planning to implementation, testing, documentation, and deployment, demonstrates a comprehensive approach to maximizing the benefits of [[ai_coding_assistants | AI coding assistants]] <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>. While not a one-size-fits-all solution, this structured process significantly enhances efficiency and consistency in AI-assisted development <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.