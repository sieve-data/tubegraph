---
title: wind surf IDE features
videoId: bVNNvWq6dKo
---

From: [[aidotengineer]] <br/> 

Wind Surf is introduced as the first AI agent-powered editor, aiming to redefine software development through the integration of advanced artificial intelligence <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Developed by a San Francisco-based product engineering team, Wind Surf believes that agents represent the future of software development <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

The company's mission is to keep developers in their "flow" and unlock their potential, handling "grunt work" such as debugging, modifying source code, and pulling correct documentation versions, allowing developers to focus on shipping products and building features <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Evolution and Vision
Wind Surf emerged from Codium, which was an early adopter of AI autocomplete products after GitHub Copilot's beta release in 2022 <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Codium gained millions of users across various IDE extensions (VS Code, JetBrains, Vim, Emacs) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Recognizing the rapid advancement of AI models, Codium began exploring agents for the future of software development <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Wind Surf officially launched on November 13th <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

The company anticipates a future where traditional copy-pasting from chat interfaces or even frequent tab usage will diminish, and possibly where code isn't primarily written inside IDEs <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Wind Surf is committed to pushing the boundaries of agentic technology <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Core Features and Principles

Wind Surf's functionality is built around three core principles designed to maximize developer productivity and seamlessly integrate AI into the coding workflow. The overarching goal is to enable users to provide minimal explicit input while generating highly correct and production-ready code <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### 1. Trajectories: Reading Your Mind
Wind Surf's agent is deeply integrated into the editor, distinguishing it from other tools like Cursor <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This integration allows the agent to understand user actions and execute tasks on their behalf <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

Key aspects of trajectories include:
*   **"Continue My Work"**: The agent builds an understanding of the user's coding and terminal commands, allowing users to simply prompt "continue my work" to have the agent complete tasks, potentially generating full pull requests or commits <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Unified Timeline**: An agent works in the background, implicitly understanding user actions such as viewing files, navigating codebases, editing files, searching, grepping, and making commits <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This shared timeline prevents the agent from undoing user changes or having outdated file states <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **Terminal Execution Mode**: The agent can automatically use large language models (LLMs) to determine the safety of terminal commands, executing common commands like `git` directly or prompting user confirmation for potentially destructive commands like `rm -rf` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Integrated Terminal**: The terminal is deeply integrated into the agentic timeline, so if a user or the agent installs a new package (e.g., via `npm install` or `pip install`), the agent automatically knows to implement it into the project based on codebase context <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This avoids the need for copy-pasting from the terminal <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **[[Building AI sandboxes | Sandbox Execution]]**: Commands are executed within a sandbox that mirrors the user's actual terminal environment, ensuring consistency and preventing "weirdness" often associated with background shell scripts <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **User Control**: A "stellar UX" with an accept/reject mechanism for changes ensures users remain in control and have confidence in the code pushed to production <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### 2. [[Meta learning in code editors | Meta Learning]]: Adapting to Preferences
Beyond understanding immediate actions, Wind Surf aims to infer understanding of a user's codebase, preferences, and organizational guidelines – a concept referred to as [[meta_learning_in_code_editors | meta learning]] <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. The editor is built to adapt and remember these specifics over time <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

Features supporting [[meta_learning_in_code_editors | meta learning]] include:
*   **Autogenerated Memories**: Wind Surf builds a "memory bank" over time based on user actions, remembering specific preferences (e.g., "remember that I use Tailwind version 4" or "React 19 instead of 18") permanently after being told once <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Custom Tool Integration**: Users can implement custom mCP servers to plug in their favorite tools, allowing the agent to adapt to diverse workflows <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
*   **Command Whitelisting/Blacklisting**: Users can specify commands the agent should or should not run without approval, such as preventing `rm` commands without explicit confirmation <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Inferred Context**: The system automatically learns about a project's architecture, endpoints, and packages by analyzing files (e.g., `package.json`) and looking up corresponding documentation online implicitly <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This eliminates the need for explicit rules files, which are seen as a "crutch" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Personalization**: The long-term goal is for every Wind Surf instance to be personalized to the individual user, requiring minimal explicit instruction <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

### 3. Scale with Intelligence: Adapting to LLM Advances
Wind Surf is designed to scale directly with advancements in LLM technology, meaning as models improve, the product's capabilities automatically enhance <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. This contrasts with earlier approaches (2021-2022) where extensive infrastructure (embedding indices, retrieval heuristics, output validating systems) was built to compensate for less capable models <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

Key features reflecting this principle:
*   **Agent-Only Interaction (No Chat)**: Wind Surf has removed traditional chat interfaces, relying solely on its agent named "Cascade" <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. This paradigm shift leads to higher quality interactions by streamlining the process <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
*   **Dynamic Context Inference (Reduced `@mentions`)**: Unlike older systems that required explicit `@mentions` (e.g., `@file`, `@web`) to provide context, Wind Surf's agent can dynamically infer relationships between code snippets and documents 90% of the time <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. The LLM is intelligent enough to automatically plan and reconstruct necessary context <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   **Human-like Web Search**: The editor includes built-in web search that reads the web like a human would, allowing the LLM to decide which search results to read, which parts of a page to focus on, and then provide an answer <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. This avoids hardcoded rules or potentially low-quality embedding indices <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

## Impact and Future
In its first three months, Wind Surf generated 4.5 billion lines of code <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Users are sending thousands of messages to Cascade daily for tasks like refactoring, writing new features, and building web pages <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Wind Surf has also become one of the largest consumers of Anthropic and OpenAI models <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. An "astonishing number" of 90% of user-written code is now generated with Cascade, a significant increase from autocomplete products which were in the 20-30% range <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

The company anticipates that by 2025, Wind Surf will achieve "no rules files," generating full pull requests and commits <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. As models improve, Wind Surf will continue to perform unsupervised work, generating full pull requests and reading complex documentation <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

Wind Surf offers a free tier for users to experience its capabilities <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.