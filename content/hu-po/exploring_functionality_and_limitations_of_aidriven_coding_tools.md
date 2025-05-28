---
title: Exploring functionality and limitations of AIdriven coding tools
videoId: uvZBlufZHP4
---

From: [[hu-po]] <br/> 

AI-driven coding tools, such as Cursor IDE, aim to integrate artificial intelligence deeply into the development environment to enhance productivity. These tools leverage large language models (LLMs) to assist with various coding tasks, from generating and editing code to understanding complex codebases and debugging.

## Cursor IDE: An AI-First Development Environment

Cursor is an IDE developed by a startup, serving as a mimic or extension of VS Code, designed to integrate AI functionality directly into the coding workflow <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. It is built upon the VS Code framework, appearing visually similar but running its own instance with Cursor-specific features <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### [[features_of_cursor_ide_compared_to_vs_code_and_other_coding_environments | Core AI Features of Cursor]]

Cursor integrates [[using_ai_integration_in_coding_environments | ChatGPT functionality]] more deeply into the environment compared to manually switching between a browser tab and the IDE <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. It uses OpenAI's API, specifically GPT-4 <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

Key features include:
*   **Edit and Write Code (Ctrl+K)**: Allows users to select code and provide instructions for the AI to modify or generate <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This feature can add documentation (docstrings) <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a> or specific logging <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.
*   **Chat (Command+Shift+L)**: A dedicated chat interface within the IDE to ask questions about the code, similar to [[ai_benchmarks_and_evaluation | conversational AI]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Codebase-Wide Understanding**: A more powerful tool that allows the AI to consider the entire codebase as context when answering questions <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This is activated by typing "with code base" in the chat <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **[[ai_benchmarks_and_evaluation | Auto Debug]]**: A feature designed to help fix errors after a terminal error occurs <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.
*   **Fix Lints**: Helps quickly resolve linting errors by hovering over them and clicking a fix button <a class="yt-timestamp" data-t="00:56:44">[00:56:44]</a>.
*   **Documentation (at-symbols)**: Improves the AI's understanding of third-party libraries. Users can type `@library_name` in the chat or command+K to have Cursor crawl custom documentation. This feature is considered impressive as it allows the AI to learn from external documentation, such as the Dynamixel SDK <a class="yt-timestamp" data-t="01:31:45">[01:31:45]</a>.

## [[experiments_and_challenges_in_aidriven_workflows | Functionality and Limitations in Practice]]

During a coding stream focused on a robotic cat toy project involving servos and a Raspberry Pi, several aspects of Cursor's functionality and limitations were observed.

### Strengths:
*   **Codebase Context**: The ability to ask the AI to understand the entire repository proved useful for gaining an overview of the project's purpose and file structure <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Refactoring Assistance**: Cursor successfully suggested a better directory structure for the project <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Targeted Code Edits**: The "edit with AI" feature effectively added documentation to specific functions <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a> and converted print statements to logging using a shared logger object <a class="yt-timestamp" data-t="01:09:51">[01:09:51]</a>, demonstrating its utility for maintaining code style and consistency.
*   **Documentation Integration**: The ability to provide external documentation (e.g., Dynamixel SDK API reference) allowed the AI to understand and generate correct code for complex tasks like bulk reading and writing to multiple servos <a class="yt-timestamp" data-t="00:46:09">[00:46:09]</a>, <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>. This was considered a "coolest feature" <a class="yt-timestamp" data-t="01:32:16">[01:32:16]</a>.
*   **Object-Oriented Design**: The AI was able to design a `Robot` class that correctly shared port and packet handlers across multiple servo objects, addressing an efficiency issue <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.

### Limitations and Challenges:
*   **File Manipulation**: Despite being able to suggest directory structures, Cursor could not directly manipulate files or move them around the file system <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This is a significant gap compared to manual drag-and-drop actions within the IDE itself <a class="yt-timestamp" data-t="01:18:45">[01:18:45]</a>.
*   **Context Invalidation**: After restructuring the codebase, the AI struggled to find files that were more than one folder deep, requiring a new chat session to re-establish context <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
*   **Lack of Proactive Error Detection**: Unlike standard VS Code, Cursor did not automatically highlight syntax errors or undefined variables, requiring code execution to discover issues <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>.
*   **Auto Debug Effectiveness**: While Auto Debug could identify the nature of an error (e.g., missing argument), it often required manual intervention to apply the fix, sometimes suggesting changes without directly implementing them <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>.
*   **Speed and Clunkiness**: The AI's response time for code edits and suggestions was often slow, leading to a feeling of waiting for the AI, similar to compile times in other languages <a class="yt-timestamp" data-t="01:10:38">[01:10:38]</a>, <a class="yt-timestamp" data-t="01:32:38">[01:32:38]</a>. The user felt they could type faster than the AI could generate <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   **Repetitive Output**: The AI often copied the entire code block or class definition even for small modifications, making the output unnecessarily long <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>, <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>.
*   **Python Environment Management**: Cursor struggled with Python environment detection, defaulting to system Python instead of a preferred Conda environment, requiring manual configuration <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>.

## [[comparison_of_direct_coding_prompts_to_multi_agent_frameworks | Comparison with Other Tools]]

*   **VS Code (Vanilla)**: Offers proactive syntax error highlighting, which Cursor lacks <a class="yt-timestamp" data-t="00:29:59">[00:29:59]</a>.
*   **GitHub Copilot**: Often provides more seamless tab-autocomplete suggestions for test cases and boilerplate code compared to Cursor's chat-based approach <a class="yt-timestamp" data-t="01:01:54">[01:01:54]</a>. Copilot's "Copilot Voice" feature also suggests a future where direct speech interaction with the IDE is possible <a class="yt-timestamp" data-t="01:25:41">[01:25:41]</a>.
*   **Open Interpreter**: This tool offers the ability for an AI to run code on the user's computer, including moving files around, addressing a key limitation of Cursor <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. However, concerns about trust and security were raised, as such a tool can perform arbitrary shell commands <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. The core of Open Interpreter's file manipulation capability is based on `subprocess.Popen` calls, which can be implemented manually <a class="yt-timestamp" data-t="01:22:01">[01:22:01]</a>.

## Business Model and Future Outlook

Cursor offers a paid subscription (e.g., $20/month), which covers its usage of OpenAI's API and applies limits on GPT-4 requests <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. This model suggests they act as a reseller of OpenAI's services <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.

The long-term viability of startups like Cursor is questioned given that larger players like Microsoft and GitHub (with their "GitHub Next" research team) are actively developing similar and potentially superior integrated AI features for their established IDEs like VS Code <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>, <a class="yt-timestamp" data-t="01:26:58">[01:26:58]</a>. An acquisition by a larger company might be Cursor's most likely exit strategy, especially if they have a strong team and a clean cap table <a class="yt-timestamp" data-t="01:06:52">[01:06:52]</a>.