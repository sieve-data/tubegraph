---
title: Shaping AI agents to meet diverse developer needs
videoId: g_tdb0PHPoA
---

From: [[everyinc]] <br/> 

GitHub has been a significant player in the AI development space, particularly with the launch of GitHub Copilot and its recent expansion into agents. The company continuously reinvents itself to maintain its position in a competitive landscape, emphasizing developer choice and integration into existing workflows <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a> <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

## Evolution of GitHub Copilot

GitHub Copilot was an early [[Applying agency in AI development | AI application]] in the current wave, predating ChatGPT but building on GPT-3 models <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Initially, GitHub explored three concepts:
*   **Code to Text**: Explaining code in natural language <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This was not considered good enough at the time <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Conversational Coding (Chat)**: This was also considered premature due to concerns about model accuracy and developer frustration <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Autocompletion (Text to Code)**: This became the initial focus because it aligned with developers' existing workflows, where they often deal with imperfect code or snippets from external sources <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a> <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This approach aimed to make code suggestions "close enough to the real developer workflow" to provide value <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

This initial success with autocompletion effectively "created this market" for AI coding tools <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Since then, Copilot has evolved significantly to include chat, voice, CLI, customization, and more recently, [[the_role_and_capabilities_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

## The Agent Launch and Market Position

GitHub recently launched Copilot agents, aiming to reposition itself at the forefront of AI coding <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. While Copilot boasts a significant user base (around 15 million users) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, the market has become highly competitive with other players like Cursor and Windsurf emerging <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a> <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. GitHub emphasizes rapid iteration, having shipped over 100 changes for Copilot in 2024 alone <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

The company offers various agent modes:
*   **Agent mode in VS Code**: Allows synchronous work with the agent <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Coding Agent on GitHub**: Assigns issues or tasks to the agent to run in the background, capable of parallel execution <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Code Review Agent**: Reviews code <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Autofix Agent**: Fixes security vulnerabilities <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

These agents can be stitched together, for example, one agent creating a pull request, another reviewing it for security, and a third monitoring cloud resources <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## Architectural and UX Decisions for Copilot Agents

The foundation for GitHub's agents lies in **GitHub Actions** <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a> <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. GitHub Actions are a Continuous Integration/Continuous Deployment (CI/CD) system that allows users to define workflows (in YAML files) triggered by events like commits, new issues, or pull requests <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. These actions run scripts on virtual machines within GitHub's integrated environment <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. The Actions marketplace boasts over 25,000 actions <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

Key advantages of integrating agents into this existing ecosystem include:
*   **Trust and Security**: Developers already trust GitHub's compute layer for their CI/CD, which handles sensitive source code. The virtual machines are isolated and temporary, ensuring intellectual property security <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Seamless Workflow Integration**: Agents operate where developers already work, either within the IDE (VS Code) or on GitHub itself <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a> <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. This means tasks like creating pull requests or adding tests can be delegated to an agent that works in the background and opens a draft pull request <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   **Auditability and Consistency**: The agent's work is recorded in pull requests, session logs, and audit logs, similar to a human co-worker <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a> <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a> <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. This addresses trust concerns with non-deterministic AI models by ensuring transparency and reviewability <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. Developers can review agent-generated code as they would human-generated code <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

## Customizing Agent Behavior

GitHub offers choice in models, including OpenAI models, Anthropic's Claude series, Google Gemini, and "bring your own key" options for other models like DeepSeek <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a> <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This choice is crucial because different models may perform better for specific languages or align with a developer's personal style <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

Beyond model selection, developers can use **custom instructions** or **system prompts** to shape the agent's "personality" or behavior <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. These can be customized through prompt files within the repository <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. For instance, a developer could instruct the agent to provide responses in German while keeping code and comments in English for team collaboration <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This feature helps democratize access to software development by supporting major human languages, unlike the English-centric internet of previous decades <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.

## Serving Diverse Developer Audiences

GitHub serves a broad audience, from large enterprise customers (a significant part of their business revenue) to a larger base of open-source developers and hobbyists using free accounts <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Historically, GitHub prioritized the individual developer, embedding the principle "always put the developer first" in its culture <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>. The company uses its own product internally for all functions, reinforcing this developer-centric approach <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.

While the definition of a "developer" is changing with [[the_future_of_ai_agents_and_user_interaction | AI-first developers]] who may write 90-100% of their code with AI, GitHub believes that understanding the underlying code remains essential for complex projects <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a> <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. Although "low-code/no-code" solutions and AI-generated "micro-apps" for specific tasks will grow <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a> <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>, for businesses where software is core, human understanding, review, and approval of code are vital to prevent security vulnerabilities or functional issues <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.

## The Future of Coding with AI

In the coming year, GitHub expects significant changes alongside enduring fundamentals <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. The presence of coding, code review, security, and CI/CD agents will grow, enabling highly efficient project adjustments <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>. However, traditional coding in IDEs for existing large codebases (e.g., COBOL, C++, Perl) will persist <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>.

GitHub anticipates a future with agents across the entire developer lifecycle: from feature design and prototyping to customer research, competitive analysis, business model generation, implementation, testing, deployment, and monitoring <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>. The "full stack builder" concept, where individuals use agents for comprehensive development, is expected to become more prevalent <a class="yt-timestamp" data-t="00:29:24">[00:29:24]</a>. Yet, millions of professional software developers will continue to write code manually <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>. The IDE will remain central, becoming increasingly agentic, as will the GitHub platform itself <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a> <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>.