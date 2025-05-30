---
title: Planning and task management in AI development
videoId: SS5DYx6mPw8
---

From: [[colemedin]] <br/> 

Developing with [[building_applications_with_ai_assistance | AI coding assistants]] necessitates a clear and well-defined process to ensure consistent, high-quality outputs. Without such a process, the effectiveness of large language models (LLMs) can fluctuate significantly, leading to frustration and inefficiency <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This article outlines a comprehensive workflow for leveraging AI in coding, focusing on strategic planning, task management, and best practices to maximize productivity <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Golden Rules for AI-Assisted Coding

A set of fundamental rules underpins effective [[developing_an_effective_ai_tech_stack | AI development]]:

*   **Contextual Markdown Documents**: Utilize higher-level markdown documents for installation instructions, documentation, planning, and tasks. These documents provide essential context to the LLM, aiding in project understanding and management <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Avoid Overwhelming the LLM**:
    *   Keep code files under 500 lines to prevent context overload <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
    *   Start fresh conversations often, as long conversation histories can hinder LLM performance <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Request one new feature or implementation per prompt for better results <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Prioritize Testing**: Ask the AI to write tests for its code, ideally after every new feature implementation, to ensure consistent output <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Be Specific with Requests**: Provide detailed instructions, including desired technologies, libraries, and output formats. Avoid vague high-level descriptions <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Maintain Documentation and Comments**: Instruct the LLM to continuously update documentation in core files and add comments within the code. This improves human understanding and aids the LLM in future references <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Manage Environment Variables Manually**: Do not entrust the LLM with sensitive data like API keys or database security. Manual implementation of environment variables is crucial for project security <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Starting a Project: The Planning Phase

Before writing any code, the planning phase establishes the project's high-level direction <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Creating Planning and Task Files

*   **Planning Document (.md)**: This file outlines the high-level vision, architecture, constraints, and other critical information. It serves as a primary context source for the LLM, especially at the beginning of new conversations <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Task Markdown File (.md)**: Used to track all project tasks, distinguishing between completed and pending items. The LLM can be instructed to update, create, or mark tasks as complete, allowing the developer to act as a project manager <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

These files can be initially generated using a chatbot, such as Claude Desktop <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. For example, when building a Superbase MCP (Multi-Modal Compute Protocol) server, a prompt can generate both `planning.md` and `task.md` files <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. It is common to iterate and refine these initial AI-generated documents to better suit project needs <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Leveraging Multiple LLMs for Planning

For deep and comprehensive planning, consider using multiple LLMs. Platforms like Global GPT allow users to provide the same prompt to various LLMs (e.g., Deepseek, 03, Claude) and then combine the best outputs. Such platforms often integrate [[using_ai_for_research_and_personalized_task_planning | AI for research]] tools like Deep Research or Perplexity, further enhancing the planning process <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Global Rules and System Prompts

Global rules function as system prompts, providing high-level instructions to the [[building_an_ai_agent_for_task_management | AI coding assistant]] without requiring explicit typing in every prompt <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. For instance, a global rule can dictate that the AI always reads the `planning.md` file at the start of a new conversation or consistently writes tests and checks off tasks <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

These rules save time and ensure adherence to best practices. They can be configured in AI IDEs like Windsurf, either as global rules for all projects or as workspace-specific rules for particular projects, which is often recommended due to project-specific technologies and requirements <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

Example components of a global rule set include instructions on:
*   Utilizing markdown files (planning, tasks) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   File length constraints (e.g., no files longer than 500 lines) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   Creating tests for new features <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   Code style guidelines <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   Maintaining the `readme` file for documentation <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

## Initial Prompting and Iteration

With planning documents and global rules in place, the initial prompt to the AI IDE is critical for setting the project's starting point <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. This prompt should be highly specific, providing extensive documentation and examples <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

Ways to provide examples and documentation:
*   **Built-in Documentation Features**: Many AI IDEs can pull in documentation (e.g., using `@MCP` in Windsurf for [[frameworks_and_tools_for_ai_agent_development | MCP documentation]]) <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.
*   **Web Search (MCP Servers)**: Utilizing an MCP server for web search, like the Brave API, allows the AI to find and summarize documentation for tools, libraries, or [[creating_tools_and_dependencies_for_ai_agents | frameworks]] <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Manual Provision**: Directly providing links to GitHub repositories or other examples of existing implementations <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

During initial prompting, the AI will perform actions like searching documentation, analyzing planning and task files, creating directories, and generating code <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. For example, a single, detailed prompt can lead to the successful generation of a complex Superbase MCP server, demonstrating the power of thorough preparation <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.

After the initial implementation, tasks like creating tests and updating the `readme` file are often done in follow-up prompts. Remember the golden rule: ask for one change at a time to avoid overwhelming the LLM <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>. When creating tests, leverage global rules to ensure best practices like dedicated test directories, mocked calls to databases and LLMs, and testing successful scenarios, errors, and edge cases <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

## Version Control with Git

Establishing a Git repository for every project is crucial for version control, backups, and managing different project states <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. Using a Git MCP server or native Git commands in the AI IDE allows the AI to create commits at important milestones. This is vital for reverting to a working state if the AI introduces breaking changes <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

## Deployment

Once a project reaches a stable state, the [[capabilities_of_ai_in_task_creation_and_management | AI coding assistant]] can assist with deployment. Docker or similar services like Podman are highly effective for packaging and deploying applications <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>. LLMs are proficient with Docker due to the vast amount of training data available online. The AI can generate Dockerfiles and provide the necessary commands to build containers and ship applications to the cloud <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>.

By following this comprehensive workflow—from detailed planning and task management to setting up robust global rules, specific prompting, and leveraging version control and deployment assistance—developers can significantly enhance their productivity and achieve consistent, high-quality results when coding with AI <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.