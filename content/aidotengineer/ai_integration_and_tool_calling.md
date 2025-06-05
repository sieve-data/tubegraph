---
title: AI integration and tool calling
videoId: z4zXicOAF28
---

From: [[aidotengineer]] <br/> 

The field of Artificial Intelligence (AI) is undergoing a significant revolution, moving beyond hype to real-world applications and widespread adoption <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>. This shift is powered by technologies that enable AI models to interact with the outside world, perform complex tasks, and integrate seamlessly into existing workflows. Key to this evolution are concepts like tool calling and the development of robust AI application frameworks.

## The Real Revolution of AI

Unlike past technologies like blockchain or NFTs, AI is demonstrating tangible impact through widespread user adoption and significant revenue generation <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.

*   **ChatGPT** achieved 100 million users faster than any consumer product in tech history, with millions using it daily to accomplish tasks <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **GitHub Copilot** boasts millions of subscribers and is integrated into Microsoft 365, reaching 84 million everyday consumers <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.
*   **Azure AI** is being adopted by enterprises, generating an annual revenue of $13 billion <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.
*   The AI Engineer World's Fair in 2025 hosted over 3,000 attendees, nearly twice as many as the previous year, all actively building and using AI technologies <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

### Evolution of AI Engineering

The field of AI engineering has matured rapidly. In 2023, discussions centered on the three types of AI engineers, evolving to a focus on multi-disciplinary approaches in 2024 with the introduction of multiple conference tracks <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>. By 2025, the focus shifted to [[ai_application_frameworks_and_architecture | agent engineering]] <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. Initially, AI engineering and "GPT wrappers" were derided, but now engineers in this space are thriving <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.

A consistent lesson is the importance of not overcomplicating solutions <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>. The field is still early, with significant "alpha to mind" <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

## Standard Models in AI Engineering

The industry is seeking a "standard model" for [[ai_application_frameworks_and_architecture | AI engineering]], similar to established concepts like ETL, MVC, CRUD, or MapReduce in traditional software engineering <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.

### Candidates for Standard Models:

*   **The MOS (Model, Optimizer, and System)**: Initially proposed by Karpathy in 2023, it has been updated for 2025 to include multimodality, standard toolsets, and [[integration_of_mcp_with_ai_applications | MCP]] as a default external communication protocol <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.
*   **LLM SDLC (Software Development Life Cycle)**: Early parts of the LLM SDLC, such as LLMs themselves, monitoring, and RAG (Retrieval-Augmented Generation), are becoming commoditized or available through free tiers <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>. Real value is generated when focusing on evaluations, security orchestration, and doing the "hard engineering work" <a class="yt-timestamp" data-t="00:29:58">[00:29:58]</a>. This pushes [[ai_implementation_and_best_practices | AI engineering]] from demos to production <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>.
*   **Building Effective Agents**: This is becoming the received wisdom for how to build an agent, although definitions continue to iterate <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>. Instead of arguing about definitions, the focus should be on the ratio of human input to valuable AI output <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. This includes understanding intent, control flow, memory planning, and [[using_tools_and_function_calls_with_ai_sdk | tool use]] <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.
*   **S.P.A.D.E. (Sync, Plan, Analyze, Deliver, Evaluate)**: A generalized model for building AI-intensive applications involving thousands of AI calls <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>. This includes processing data into knowledge graphs, generating structured outputs, and creating code artifacts <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

## The Agentic Web and Tooling

The emergence of diverse reasoning models and their increased efficiency are giving rise to the "agentic web" <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. This is a world where agents interact with tools, models, and other agents across different clouds, companies, and devices <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.

Key forces in [[ai_application_frameworks_and_architecture | AI engineering]] within the agentic web include:
*   Transitioning from pair programming to peer programming, with tools like Copilot becoming active teammates <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>.
*   Moving from a software factory to an agent factory, focusing on shipping behaviors rather than just binaries <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>.
*   Models increasingly residing on devices, enabling local execution and low latency <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.

### Platforms and Tools for Agent Development

Microsoft's core AI platform aims to empower users to shape the world with AI <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>.

*   **Foundry**: This platform enables building agents that can retrain, redeploy, and change post-deployment <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. It supports an "agent factory" with baked-in trust and security, and seamless cloud-to-edge operation <a class="yt-timestamp" data-t="00:38:53">[00:38:53]</a>.
*   **Signals Loop**: A continuous loop emerging in agent development, where fine-tuning models to personalize outcomes leads to better results, observed in applications like Dragon, a healthcare Copilot <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>.
*   **Intelligent Routing**: Foundry offers a switchboard for intelligent routing, providing access to 10,000 open and proprietary models, backed by security and data residency <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>.
*   **Agentic RAG**: An improvement over traditional RAG, offering multi-shot iteration and evaluation, leading to a 40% improvement in accuracy on complex queries <a class="yt-timestamp" data-t="00:47:37">[00:47:37]</a>.
*   **Tooling as Infrastructure**: [[using_tools_and_function_calls_with_ai_sdk | Tooling]] is becoming infrastructure, requiring code and containers. Platforms like Foundry provide over 1500 tools and were early adopters of [[integration_of_mcp_with_ai_applications | MCP]] and A2A (Agent-to-Agent) protocols <a class="yt-timestamp" data-t="00:47:53">[00:47:53]</a>.
*   **Accountability**: Aggressive efforts are being made in evaluation SDKs and red teaming agents, with continuous observability through integration with OpenTelemetry <a class="yt-timestamp" data-t="00:48:07">[00:48:07]</a>.

Over 50,000 agents are built daily using these platforms <a class="yt-timestamp" data-t="00:48:29">[00:48:29]</a>.

### Examples of AI-Powered Development Tools:

*   **GitHub Copilot spaces**: Allows users to create a Copilot space grounded in specific files, enabling it to answer questions about a project's facts <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.
*   **Copilot for task automation**: Can be assigned tasks, such as writing a README file, and can run tests until complete <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>.
*   **Extending Copilot with other agents**: GitHub Copilot within VS Code can communicate with other agents, like "Amaly MLE" (machine learning engineer agent), to reason about code and write new code <a class="yt-timestamp" data-t="00:43:43">[00:43:43]</a>.

## Focus on [[integration_of_mcp_with_ai_applications | MCP]]

The Model Context Protocol (MCP) is highlighted as a foundational shift in the internet's economy, where tool calls are becoming the new clicks <a class="yt-timestamp" data-t="02:31:05">[02:31:05]</a>.

### Origin and Evolution of [[integration_of_mcp_with_ai_applications | MCP]]

The genesis of [[integration_of_mcp_with_ai_applications | MCP]] stemmed from the need to address "copy and paste hell," where AI was disconnected from the rest of the world <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Anthropic's co-creators conceived of [[integration_of_mcp_with_ai_applications | MCP]] from the observation that engineers were constantly copying context from external sources (like Slack or error logs) into LLM context windows <a class="yt-timestamp" data-t="02:33:20">[02:33:20]</a>.

The core idea was to enable models to "climb out of their box" and interact with the outside world, giving them model agency <a class="yt-timestamp" data-t="02:33:48">[02:33:48]</a>. This led to the conclusion that an open-source, standardized protocol was necessary for scalability <a class="yt-timestamp" data-t="02:34:21">[02:34:21]</a>. [[integration_of_mcp_with_ai_applications | MCP]] was open-sourced in November 2023 <a class="yt-timestamp" data-t="02:36:08">[02:36:08]</a>.

Early on, many questioned the need for a new open-source protocol <a class="yt-timestamp" data-t="02:36:40">[02:36:40]</a>. A turning point was when Cursor and other coding tools adopted [[integration_of_mcp_with_ai_applications | MCP]], giving builders hands-on experience and demonstrating its utility <a class="yt-timestamp" data-t="02:37:18">[02:37:18]</a>. More recently, major players like Google, Microsoft, and OpenAI have also adopted [[integration_of_mcp_with_ai_applications | MCP]], cementing its status as a standard <a class="yt-timestamp" data-t="02:37:50">[02:37:50]</a>.

### Key Principles and Features of [[integration_of_mcp_with_ai_applications | MCP]]

*   **Model Agency**: The protocol is designed to give models the intelligence to choose actions and decide what to do, similar to how humans delegate tasks <a class="yt-timestamp" data-t="02:39:14">[02:39:14]</a>.
*   **Server Simplicity**: Optimizing for server simplicity means that when trade-offs are necessary between client and server complexity, the complexity is pushed to the client, as it is believed there will be significantly more servers than clients <a class="yt-timestamp" data-t="02:40:23">[02:40:23]</a>.
*   **Streamable HTTP**: Recent support for streamable HTTP enables more bidirectionality, crucial for agents to communicate with each other <a class="yt-timestamp" data-t="02:39:57">[02:39:57]</a>.
*   **OAUTH Fixes**: Initial issues with OAuth implementation were resolved through community contributions, demonstrating the value of open-source collaboration <a class="yt-timestamp" data-t="02:41:23">[02:41:23]</a>.
*   **Elicitation**: Allows servers to request more information from end-users, enabling better-tailored responses (e.g., clarifying "best flight" means cheapest or fastest) <a class="yt-timestamp" data-t="02:42:30">[02:42:30]</a>.
*   **Registry API**: Aims to make it easier for models to discover [[integration_of_mcp_with_ai_applications | MCP]]s that were not given to them upfront, further enhancing model agency <a class="yt-timestamp" data-t="02:43:08">[02:43:08]</a>.
*   **Debugging Tools**: Inspector is highlighted as an underutilized debugging tool for [[integration_of_mcp_with_ai_applications | MCP]] servers <a class="yt-timestamp" data-t="02:42:14">[02:42:14]</a>.

### Building with [[integration_of_mcp_with_ai_applications | MCP]]

Theo from Anthropic suggests key areas for building in the [[integration_of_mcp_with_ai_applications | MCP]] ecosystem:
1.  **More and Higher-Quality Servers**: A significant opportunity exists to build more servers, particularly for verticals beyond developer tools like sales, finance, legal, and education <a class="yt-timestamp" data-t="02:45:17">[02:45:17]</a>. Servers should be designed with three users in mind: the end-user, the client developer, and the model itself, ensuring tools exposed to the model enable correct responses <a class="yt-timestamp" data-t="02:45:58">[02:45:58]</a>.
2.  **Simplifying Server Building**: Tooling that makes it easier for enterprises and indie hackers to build servers is crucial, including hosting, testing, evaluation, and deployment tools <a class="yt-timestamp" data-t="02:46:52">[02:46:52]</a>.
3.  **Automated [[integration_of_mcp_with_ai_applications | MCP]] Server Generation**: A moonshot for the future, where models become so adept at writing code that they can generate their own [[integration_of_mcp_with_ai_applications | MCP]]s on the fly <a class="yt-timestamp" data-t="02:47:44">[02:47:44]</a>.
4.  **AI Security, Observability, and Auditing**: As AI applications gain access to real-world data, security and privacy implications increase, making tooling in this area essential <a class="yt-timestamp" data-t="02:48:23">[02:48:23]</a>.

### [[integration_of_tool_calling_in_agent_frameworks | Implementation of Tool Calling]] and [[integration_of_mcp_with_ai_applications | MCP]] at Scale

Anthropic, through John, shared experiences in [[integration_of_tool_calling_in_agent_frameworks | implementing MCP clients]] and talking to remote [[integration_of_mcp_with_ai_applications | MCP]] at scale <a class="yt-timestamp" data-t="02:50:10">[02:50:10]</a>.

*   **Integration Chaos**: The rapid proliferation of custom endpoints for every [[ai_workflow_automation | use case]] led to duplication of functionality and inconsistent integrations <a class="yt-timestamp" data-t="02:51:25">[02:51:25]</a>.
*   **Standardization**: Standardizing on [[integration_of_mcp_with_ai_applications | MCP]] internally helps streamline processes, allows engineers to focus on unique problems, and provides solutions for unforeseen issues like billing models and token limits <a class="yt-timestamp" data-t="02:54:11">[02:54:11]</a>.
*   **MCP Gateway**: Anthropic designed a shared infrastructure service, the [[integration_of_mcp_with_ai_applications | MCP]] gateway, as a single point of entry. It handles credential management, centralized rate limiting, and observability, making it easy for engineers to connect to [[integration_of_mcp_with_ai_applications | MCP]] services <a class="yt-timestamp" data-t="02:58:07">[02:58:07]</a>.
*   **Portable Credentials**: The gateway enables portable credentials, so batch jobs or internal services don't require re-authentication <a class="yt-timestamp" data-t="03:01:37">[03:01:37]</a>.

### Hidden Capabilities and Challenges of [[integration_of_mcp_with_ai_applications | MCP]]

Harold from VS Code discussed the lesser-known aspects of [[integration_of_mcp_with_ai_applications | MCP]], aiming to unlock its full potential for rich, stateful interactions <a class="yt-timestamp" data-t="03:04:04">[03:04:04]</a>.

*   **"MCP is just another API wrapper" syndrome**: Many implementations only leverage [[using_tools_and_function_calls_with_ai_sdk | tools]], neglecting other powerful features like dynamic discovery, persistent resources, and rich interactions <a class="yt-timestamp" data-t="03:05:39">[03:05:39]</a>.
*   **Tool Quality over Quantity**: Too many tools or tools across too many domains can confuse AI models <a class="yt-timestamp" data-t="03:07:45">[03:07:45]</a>. Client-side controls like per-chat tool selection and user-defined tool sets can help manage this <a class="yt-timestamp" data-t="03:08:21">[03:08:21]</a>.
*   **Dynamic Tool Discovery**: Allows servers to dynamically provide tools based on the current context, such as a "battle" tool appearing only when a monster is present in a game <a class="yt-timestamp" data-t="03:09:41">[03:09:41]</a>.
*   **Resources**: Enable the server to return references to files or data rather than the full content, allowing the LLM or user to follow up <a class="yt-timestamp" data-t="03:10:26">[03:10:26]</a>. This can also customize responses based on the user's environment (e.g., React vs. Svelte setup) <a class="yt-timestamp" data-t="03:11:06">[03:11:06]</a>.
*   **Sampling**: Allows the server to request LLM completions from the client, enabling features like summarizing resources or formatting web content <a class="yt-timestamp" data-t="03:11:51">[03:11:51]</a>.
*   **Developer Experience**: Tools like VS Code's dev mode provide direct debugging and logging for [[integration_of_mcp_with_ai_applications | MCP]] servers, improving the development process <a class="yt-timestamp" data-t="03:13:15">[03:13:15]</a>.
*   **Community Registry**: Efforts are underway to create a community registry for [[integration_of_mcp_with_ai_applications | MCP]] servers to ease discovery and collaboration <a class="yt-timestamp" data-t="03:15:32">[03:15:32]</a>.

### Practical Considerations for [[integration_of_mcp_with_ai_applications | MCP]] Implementation

David from Sentry provided a "rant" on the practical challenges and learnings from building an [[integration_of_mcp_with_ai_applications | MCP]] server for a B2B SaaS company <a class="yt-timestamp" data-t="03:19:05">[03:19:05]</a>.

*   **Focus on Remote [[integration_of_mcp_with_ai_applications | MCP]]**: For cloud services, the remote [[integration_of_mcp_with_ai_applications | MCP]] interface with OAuth 2.1 is key, rather than standard IO, due to security, iteration speed, and existing infrastructure advantages <a class="yt-timestamp" data-t="03:27:46">[03:27:46]</a>.
*   **Beyond Open API**: [[integration_of_mcp_with_ai_applications | MCP]] is not a simple wrapper for existing APIs <a class="yt-timestamp" data-t="03:26:04">[03:26:04]</a>. Developers must design tools specifically for AI models, massaging data and focusing on how an agent would use context <a class="yt-timestamp" data-t="03:26:18">[03:26:18]</a>. Returning structured Markdown is often more effective than raw JSON <a class="yt-timestamp" data-t="03:29:42">[03:29:42]</a>.
*   **Client Support**: Early adoption faces challenges with inconsistent client support for [[integration_of_mcp_with_ai_applications | MCP]] features like OAuth <a class="yt-timestamp" data-t="03:26:36">[03:26:36]</a>.
*   **Security Risks**: Allowing random [[integration_of_mcp_with_ai_applications | MCP]] tools in an organization is dangerous due to prompt injection and data exfiltration risks <a class="yt-timestamp" data-t="03:28:40">[03:28:40]</a>. Trust and vetting are essential.
*   **Cost Management**: The cost of tool calls can escalate rapidly with large token counts <a class="yt-timestamp" data-t="03:31:52">[03:31:52]</a>. Thoughtful design to limit token usage is necessary.
*   **Continuous Evolution**: [[integration_of_mcp_with_ai_applications | MCP]] implementations are not "set and forget"; continuous updates and tweaks are required <a class="yt-timestamp" data-t="03:32:29">[03:32:29]</a>.
*   **Focus on Agents**: The true value unlock is in building agents and exposing them through the [[integration_of_mcp_with_ai_applications | MCP]] architecture <a class="yt-timestamp" data-t="03:33:38">[03:33:38]</a>. Controlling the agent provides control over the prompt, tool results, and even the model itself <a class="yt-timestamp" data-t="03:33:11">[03:33:11]</a>.

Ultimately, while [[integration_of_mcp_with_ai_applications | MCP]] and [[ai_application_frameworks_and_architecture | agent architecture]] introduce new terms, they represent familiar software engineering challenges and solutions, albeit with a new "coat of paint" <a class="yt-timestamp" data-t="03:34:58">[03:34:58]</a>. The core opportunity lies in reimagining experiences and building "thick" workflow wrappers that enhance user value <a class="yt-timestamp" data-t="01:16:44">[01:16:44]</a>.