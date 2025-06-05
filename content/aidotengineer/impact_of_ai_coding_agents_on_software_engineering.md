---
title: Impact of AI coding agents on software engineering
videoId: Iw_3cRf3lnM
---

From: [[aidotengineer]] <br/> 

AI coding agents, once considered science fiction, are now a reality, with some even contributing to their own development <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These agents are transforming the landscape of software engineering and are predicted to dominate conversations in 2025 regarding how the field is changing <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Evolution of AI in Software Development

The AI Dev tools space is rapidly changing <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:
*   **2023**: Characterized by autocomplete models like GitHub Copilot <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **2024**: Chat models began to penetrate software engineering organizations <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **2025**: AI agents are expected to become the primary focus <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## AI Coding Agents: A Self-Building Capability

A notable aspect of these agents is their capacity for self-improvement. One agent developed by Augment Code, an AI research company, helped build itself, writing over 90% of its approximately 20,000 lines of code with human supervision <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This self-building capability extends to several core features:

### [[integration_of_ai_coding_agents_with_thirdparty_tools | Third-Party Integrations]]
AI agents are designed to interact with various platforms essential for software engineers, such as Slack, Linear, Jira, Notion, Google Search, and codebases <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. For example, an agent was able to add a Google search integration by analyzing the codebase and figuring out the correct file and interface <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. In one instance, when adding a Linear integration, the agent used its previously written Google search integration to look up the Linear API documentation, as the foundation model did not have it memorized <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### [[testing_and_optimization_of_ai_coding_agents | Testing]]
Agents can write unit tests for new integrations or existing code, provided they are given basic process management tools like running subprocesses and handling output <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### [[testing_and_optimization_of_ai_coding_agents | Optimization]]
Beyond writing features and tests, agents can perform optimizations. An agent tasked with profiling itself added print statements, ran sub-copies, and identified a bottleneck involving synchronous loading and hashing of repository files. It then implemented a process pool and stress test to improve performance <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## How Agents Interact with Their Environment

AI agents operate with a "Master Level agent" that plans tasks and utilizes various tools to interact with its environment <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. These tools include:
*   **Google Search**: For external information retrieval <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Retrieval Tool**: To search and navigate the local codebase <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **File Editing Tool**: For making quick and performant edits to files <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Clarify Tool**: To ask users for clarification when encountering missing information, like credentials <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Memory Tool**: Allows the agent to continuously learn from human interactions and store useful information for future use <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

A "super powerful scalable Enterprise-ready context engine" is crucial for agents to function effectively, providing access to diverse context sources such as Slack, Linear, Jira, Notion, and the codebase <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This context, combined with the reasoning capabilities of a best-in-class foundation model and a safe code execution environment, forms the foundation for building effective agents <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## [[challenges_and_insights_in_developing_ai_coding_agents | Challenges and Insights in Developing AI Coding Agents]]

Building these agents has revealed several key lessons:

### [[limitations_of_current_ai_models_in_software_engineering | Assumptions vs. Reality]]
*   **L5 Agents are Here**: Despite impressive Twitter demos, professional software engineering environments are complex and messy <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Agents are not yet at the senior software engineering level, but they are still highly useful <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Agents Take Over Entire Task Categories**: Instead of specializing in tasks like backend or frontend development, this technology is general-purpose. Agents' capabilities are improving across all fronts simultaneously <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **Anthropomorphizing Agents**: Agents possess different strengths and weaknesses than humans. An agent might struggle with math but rapidly implement a frontend feature <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### Onboarding the Agent
Just like human new hires, agents need to be onboarded to an organization's specific tools and practices <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Creating a "knowledge base"—a set of information like markdown files describing tools (e.g., Graphite), tool stacks, test procedures, and style guides—allows the agent to dynamically search and understand information it doesn't already know <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### [[impact_of_ai_on_development_workflow | Impact on Product Development]]
When code becomes "cheap" to write due to agents, the bottleneck shifts from engineering hours to good product insights and design <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This allows product teams to explore more ideas and iterate faster <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### Importance of Context
Good context is critical <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. Agents can understand high-level natural language instructions if they have strong codebase awareness <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Context isn't limited to code; it comes in many forms (e.g., Slack, pull requests) and is multiplicative—access to multiple context sources significantly increases an agent's utility <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

## The Critical Role of [[testing_and_optimization_of_ai_coding_agents | Testing]]

Agents, like humans, make mistakes, especially with complex edge cases like parallel programming and caching <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. The absence of sufficient tests for such scenarios means agents can introduce bugs <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

*   **Better Tests Enable More Autonomy**: Upgrading a foundation model by six months improved a bug-fixing benchmark by 4%, but adding the ability for the agent to run tests, receive feedback, and iterate on fixes led to a 20% gain <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This demonstrates that robust test harnesses are crucial for increasing agent trustworthiness and intelligence <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

## The [[the_future_of_ai_engineering | Future of AI Engineering]]

The [[future of AI in coding | future of AI in coding]] suggests a significant shift in software engineering <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>:
*   AI agents are rapidly improving, with their self-building capabilities accelerating this pace <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   Code will remain important as a specification of systems, but the human relationship with code is changing <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   Good test harnesses are more critical than ever, especially for less well-tested parts of codebases <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
*   The calculus of product development is shifting, with greater emphasis on product work, gathering customer feedback, and building insights as code generation becomes cheaper <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.

This technology is poised to positively transform the software industry <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.