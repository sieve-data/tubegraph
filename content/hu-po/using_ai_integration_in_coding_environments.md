---
title: Using AI integration in coding environments
videoId: uvZBlufZHP4
---

From: [[hu-po]] <br/> 

AI integration in coding environments aims to streamline the development process by bringing Large Language Model (LLM) functionality directly into the Integrated Development Environment (IDE) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This approach seeks to overcome the inefficiencies of switching between a browser tab for an AI chatbot and the IDE for development, copying and pasting code back and forth <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Cursor IDE

Cursor is a startup product designed as an IDE that deeply integrates GPT-4 functionality <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. It functions similarly to VS Code, possibly running its own instance of VS Code with Cursor's features built in <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Core Functionality and Features

Cursor leverages OpenAI's API, primarily GPT-4, to provide various code assistance capabilities <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

*   **Edit and Write Code (`Ctrl+K`/`Command+K`):** Users can select code and use a command to initiate AI-powered edits or generation <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   **Adding Documentation:** It can add docstrings to functions, improving code readability <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
    *   **Modifying Logging:** Cursor can refactor code to use consistent logging practices, for example, switching from `print` statements to a shared logger object <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>, <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>.
*   **Chat (`Ctrl+Shift+L`/`Command+Shift+L`):** A dedicated chat interface allows users to ask questions about their code or broader programming concepts <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:39:45">[00:39:45]</a>.
    *   **Codebase-wide Understanding:** One powerful feature allows the AI to analyze the entire codebase to answer questions or provide context <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This is advertised to become more useful as the code base size increases <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
    *   **Refactoring:** Users can request the AI to refactor code into object-oriented patterns, such as creating a `Robot` class to manage multiple servos and their shared communication handlers <a class="yt-timestamp" data-t="00:49:01">[00:49:01]</a>.
*   **`@` Symbols:** Typing `@` within the chat or `Ctrl+K` command provides a dropdown of files and code symbols, enabling AI to generate code with specific dependencies or ask about a file <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>.
*   **Auto-Debug:** This agent aims to fix errors by analyzing terminal output. It provides suggestions for resolving issues, such as missing modules or incorrect function arguments <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>, <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.
*   **Fix Lints:** Cursor can help resolve linting errors, suggesting changes like explicitly importing modules instead of using `import *` and adhering to naming conventions <a class="yt-timestamp" data-t="00:56:41">[00:56:41]</a>, <a class="yt-timestamp" data-t="00:57:23">[00:57:23]</a>.
*   **Docs Integration (`@library_name`):** This feature enhances the AI's understanding of third-party libraries. Users can add custom documentation by providing a URL, allowing the AI to answer questions or generate code based on that specific library's API <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>, <a class="yt-timestamp" data-t="01:31:45">[01:31:45]</a>. For instance, it can understand and suggest code for the Dynamixel SDK <a class="yt-timestamp" data-t="00:46:12">[00:46:12]</a>.

### Limitations and Criticisms

Despite its features, Cursor has several notable limitations:

*   **File Manipulation:** The AI cannot directly manipulate files (e.g., move directories) even if it can suggest a better directory structure <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>, <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.
*   **Codebase Context:** Initially, the "with codebase" feature seemed limited to only one folder deep, requiring new chat sessions or specific file references to gain context <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
*   **Subscription Model:** Cursor operates on a paid subscription (e.g., $20/month) that includes a limit on GPT-4 requests (e.g., 500 requests per month) <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>, <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>. There was an initial perception that users could not use their own OpenAI API key, implying a monetization strategy where Cursor pays OpenAI per request <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>, though later it was suggested custom API keys *are* supported <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.
*   **Speed and Clunkiness:** Users reported the AI's response time to be slow, sometimes slower than manual typing or traditional autocomplete <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>, <a class="yt-timestamp" data-t="01:10:38">[01:10:38]</a>. The user interface for interacting with the AI, such as accepting changes, can feel clunky <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>, <a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a>.
*   **IDE Features:** Unlike standard VS Code, Cursor did not automatically highlight syntax errors in the editor, making it harder to spot issues before running code <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>.
*   **Environment Management:** The AI struggles with tasks like creating or activating specific Conda environments, or correctly identifying the Python interpreter path <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>, <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.
*   **Generative Quality:** While it uses GPT-4, the quality of generated code or suggestions can sometimes be less intuitive or require more hand-holding than expected, like generating boilerplate or non-ideal string functions <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>, <a class="yt-timestamp" data-t="00:43:13">[00:43:13]</a>. It also sometimes includes unnecessary `for` loops in bulk operations <a class="yt-timestamp" data-t="00:53:10">[00:53:10]</a>.

## Comparison to GitHub Copilot

Cursor's functionality invites comparison with GitHub Copilot, another prominent AI coding assistant.

*   **Tab Autocomplete:** GitHub Copilot excels at real-time, context-aware tab autocompletion, which users find more seamless and intuitive for rapid coding <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>, <a class="yt-timestamp" data-t="01:32:33">[01:32:33]</a>.
*   **Copilot X and Copilot Voice:** GitHub is actively developing advanced versions like Copilot X, which incorporates chat functionalities, and Copilot Voice, allowing users to interact with the IDE using speech <a class="yt-timestamp" data-t="01:25:40">[01:25:40]</a>, <a class="yt-timestamp" data-t="01:26:09">[01:26:09]</a>. This suggests a future where users can literally talk to their IDE for coding tasks <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>.
*   **Code Brushes:** Copilot also explores "code brushes" for applying formatting or refactoring by hovering over code <a class="yt-timestamp" data-t="01:26:34">[01:26:34]</a>.

## Open Interpreter

[[opensource_ai_and_its_implications | Open Interpreter]] is another tool that allows an AI to run code directly on the user's computer, enabling tasks like file manipulation that Cursor currently cannot perform <a class="yt-timestamp" data-t="00:10:04">[0:10:04]</a>, <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. While powerful, concerns were raised about trusting an AI with direct access to the local file system <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. It functions by executing shell commands using `subprocess.Popen` <a class="yt-timestamp" data-t="01:22:03">[01:22:03]</a>. This highlights a broader point about [[open_source_artificial_intelligence | open source AI]] and the trade-offs between using third-party libraries versus implementing functionality from scratch to avoid dependencies and potential security vulnerabilities <a class="yt-timestamp" data-t="01:23:11">[01:23:11]</a>.

## Future Outlook for AI in Coding

The landscape of AI-integrated coding environments is rapidly evolving. While startups like Cursor offer valuable early integrations, larger tech companies like Microsoft (with GitHub Copilot) are likely to develop more refined and deeply integrated AI features within their established IDEs <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>, <a class="yt-timestamp" data-t="01:32:55">[01:32:55]</a>. The existence of dedicated teams like "GitHub Next" focusing on advanced AI features suggests that major players will likely replicate and surpass current AI IDE capabilities <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>, <a class="yt-timestamp" data-t="01:26:58">[01:26:58]</a>. This could lead to a future where startups in this space might face acquisition or be outcompeted by more comprehensive offerings <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>. The core [[evaluation_of_ai_coding_through_benchmarks | evaluation of AI coding through benchmarks]] will continue to be how effectively these tools can enhance developer productivity across different coding tasks.