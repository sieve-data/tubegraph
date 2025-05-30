---
title: Effective use of AI coding assistants
videoId: SS5DYx6mPw8
---

From: [[colemedin]] <br/> 

While it is widely known that not [[using_ai_coding_assistance | using AI coding assistance]] can cause a developer to fall behind, regardless of what they are developing, many people struggle with how to use these [[ai_coding_assistants | AI coding assistants]] effectively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Simply providing an [[ai_coding_assistants | AI IDE]] like Windsurf or Cursor with any request might yield good results sometimes, but a clear process is essential for consistent high-quality outputs <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Without a refined workflow, the Large Language Model (LLM) can produce frustrating results, such as deleting code, implementing unwanted features, or maxing out API usage <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

This guide outlines a comprehensive, step-by-step workflow for developing with [[ai_coding_assistants | AI]], aiming to significantly boost productivity <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This process avoids overly complicated setups, focuses on building practical and useful examples, and is adaptable to any development project or [[ai_coding_assistants | AI IDE]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Golden Rules for AI-Assisted Coding

A set of "golden rules" dictates much of the effective workflow for [[ai_coding_assistants_and_how_to_use_them_effectively | using AI to code]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:

*   **Utilize Higher-Level Markdown Documents**
    *   Create documents like `planning.md` and `tasks.md` to provide context for installation instructions, documentation, planning, and tasks to the LLM <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. These documents can be created and managed with AI assistance <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Avoid Overwhelming the LLM**
    *   Longer contexts increase the likelihood of the LLM hallucinating <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   Keep code files under 500 lines <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
    *   Start fresh conversations often, as longer conversations can bog down the LLM <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Ask the LLM to do only one new feature or implement one new thing per prompt <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Requesting too many things simultaneously leads to poor results <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Write Tests**
    *   It is crucial to ask the [[ai_coding_assistants | AI]] to write tests for its code, ideally after every new feature implemented, to ensure consistent output <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Be Specific with Requests**
    *   Provide extra context and specific details about desired technologies, libraries, and output format. Avoid high-level descriptions <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Write Docs and Comments As You Go**
    *   The LLM should constantly update documentation in higher-level files and add comments within the code itself <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This aids both the user's understanding and the LLM's future references <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Implement Environment Variables Yourself**
    *   Never trust the LLM with API keys, database security, or other sensitive environment variables <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Understanding and securing these aspects of your project is paramount, even when using [[ai_coding_assistants | AI]] to generate code <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

## Workflow Steps

### 1. Planning Phase

The planning phase involves creating foundational documents before any coding begins to provide high-level direction <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

*   **`planning.md`**: This document should contain the project's high-level vision, architecture, and constraints <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The LLM can reference this file for context, especially at the start of new conversations, to quickly understand the project <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **`tasks.md`**: This Markdown file tracks all tasks, indicating what has been completed and what still needs to be done <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. The LLM can update, create, delete, and mark tasks as done, allowing the user to manage the [[ai_coding_assistants | AI coding assistant]] effectively <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

These files can initially be created using a chatbot (e.g., Claude Desktop) outside of an [[ai_coding_assistants | AI IDE]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. It's often beneficial to iterate on these documents and use multiple LLMs for planning by giving the same prompt to each and combining the results <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### 2. Global Rules

Global rules act as system prompts for the [[ai_coding_assistants | AI coding assistant]], providing high-level instructions that don't need to be typed explicitly with every prompt <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

For instance, a global rule can instruct the [[ai_coding_assistants | AI coding assistant]] to always read the `planning.md` file at the start of a new conversation or to write tests for all new features <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. It is generally recommended to use workspace-specific rules, as requirements like technology stacks often vary by project <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

### 3. Configuring MCP Servers

MCP (Model-Controller-Program) servers provide additional tools to an [[ai_coding_assistants | AI IDE]], enabling it to perform tasks like web searches <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

Core MCP servers commonly used include:

*   **File System Server**: Allows the [[ai_coding_assistants | AI IDE]] to interact with the broader file system, including other folders on the computer, to pull assets or reference past projects <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **Brave Search API**: Provides powerful web search capabilities, often using [[ai_coding_assistants | AI]] to summarize search results, useful for pulling documentation for tools, libraries, or frameworks <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   **Git Server**: Crucial for version control, allowing the [[ai_coding_assistants | AI IDE]] to manage backups and different versions of projects <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This is vital for reverting to a working state if the [[ai_coding_assistants | AI]] breaks the project after multiple requests <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

### 4. Initial Prompt

Even with planning documents, the initial prompt to the [[ai_coding_assistants | AI IDE]] must be highly specific, as it sets the entire starting point for the project <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

Examples and documentation can be provided in three ways:

*   **Built-in features**: Many [[ai_coding_assistants | AI IDEs]] (e.g., Windsurf with `@MCP`) can pull in documentation, using Retrieval Augmented Generation (RAG) to augment the LLM's answer <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.
*   **Web search via MCP server**: Ask the [[ai_coding_assistants | AI]] to find documentation online for specific libraries or tools <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Manual links**: Provide links to GitHub repositories or other resources that contain example implementations or documentation <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

By combining specific instructions, documentation, and examples, the [[ai_coding_assistants | AI]] can produce much better initial results, like a functional Superbase MCP server built in a single prompt <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.

### 5. Iteration and Testing

After the initial implementation, the process moves to iteration and rigorous testing:

*   **One Change at a Time**: Adhere to the golden rule of asking for only one change or feature implementation per prompt to avoid overwhelming the LLM <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.
*   **Create Tests**: Request the LLM to create unit tests for each feature or tool it has developed <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.
    *   Best practices for testing, which can be included in global rules, involve creating a dedicated test directory, mocking calls to databases and LLMs for fast and free tests, and testing successful, error-handling, and edge-case scenarios <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.
*   **Version Control**: Utilize Git (via an MCP server or native commands) to commit changes and save working states of the project <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. This allows for reverting to previous, stable versions if the [[ai_coding_assistants | AI]] introduces breaking changes <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>.
*   **Maintain Documentation**: Continuously update `tasks.md` and `planning.md` to ensure the [[ai_coding_assistants | AI]] has the most current context, especially when starting new conversations <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>. Also, generate and maintain a `readme.md` file for project documentation <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.

### 6. Deployment

Once the project is stable and ready, [[ai_coding_assistants | AI coding assistants]] can aid in the deployment process:

*   **Docker**: LLMs are proficient at working with Docker due to the extensive training data available for it <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. The [[ai_coding_assistants | AI]] can help create a `dockerfile` to package and deploy the application, even providing the necessary commands <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **Readme for Deployment**: Ensure the `readme.md` file includes full instructions for running the deployed project, including installation and configuration details <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.

By following this comprehensive workflow, developers can leverage [[ai_coding_assistants | AI coding assistants]] from ideation through implementation, testing, documentation, and deployment, achieving a complete end-to-end development process <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.