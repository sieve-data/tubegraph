---
title: Challenges and insights in developing AI coding agents
videoId: Iw_3cRf3lnM
---

From: [[aidotengineer]] <br/> 

Developing AI coding agents, which might sound like science fiction, is rapidly becoming a reality <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Augment Code, an AI research company specializing in AI-powered developer tools, has been on a journey to build such agents, noticing a shift from autocomplete models (2023) and chat models (2024) to AI agents dominating the software engineering conversation by 2025 <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. A significant insight from their experience is that an AI coding agent can help build itself, with over 90% of a 20,000-line codebase for their agent written by the agent itself with human supervision <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

## Capabilities of the AI Coding Agent

The AI coding agent demonstrates a range of capabilities that mimic a software engineer:

*   **Implementing Core Features** The agent can integrate with third-party services like Slack, Linear, Jira, Notion, and Google search. For instance, when asked to add a Google search integration, it could locate the correct file, determine the interface, and add the feature <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. A notable example involved the agent using its pre-written Google search integration to look up Linear API documentation when adding a Linear integration, as the foundation model didn't have it memorized <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
*   **Writing Tests** The agent can generate unit tests for features it implements, like the Google search integration, by using basic process management tools such as running subprocesses and handling output <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
*   **Performing Optimizations** The agent can profile its own performance. When the team noticed the agent was slow, they asked it to profile itself. It added print statements to its own codebase, ran sub-copies of itself, analyzed the output, identified synchronous file loading and hashing as a bottleneck, and then added a process pool to speed it up, confirming the fix with a stress test <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
*   **Learning from User Feedback** The agent continuously learns from human interactions. When it couldn't find Google credentials, it clarified with the user. After being told the location, it used a "memory tool" to save this information for future use, highlighting the importance of a good context engine <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
*   **Tasks Beyond Code Writing** The agent can perform non-coding tasks within the software development lifecycle, such as analyzing recent Pull Requests (PRs) to generate and post announcement summaries to Slack <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>. It can even generate plots of its own code growth over time <a class="yt-timestamp" data-t="13:29:00">[13:29:00]</a>.

## Foundational Elements for Success

The rapid development of this agent, completed in just a couple of months, was built on key foundational elements:

*   **Powerful, Scalable Enterprise-Ready Context Engine** This engine provides access to various context sources, including Slack, Linear, Jira, Notion, search, and the codebase <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. Good context is critical and its utility is multiplicative; having access to both codebase and Slack, for example, is four times as useful as having access to just one <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
*   **Reasoning Capabilities from a Best-in-Class Foundation Model** <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>
*   **Safe Code Execution Environment** This allows the agent to run commands securely within a customer's environment <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.

## Assumptions and Realities: [[Design challenges for AI agents | Challenges]] and Misconceptions

Developing AI agents often involves addressing common misconceptions:

*   **"L5 agents are here"**: While Twitter demos might suggest AI agents can write entire websites independently, professional software engineering environments are much messier. Agents aren't yet at the level of senior software engineers, but they are still incredibly useful <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.
*   **Agents taking over entire categories of tasks**: Instead of building agents for specific task categories (e.g., backend, frontend, testing), it's more effective to think about levels of complexity. AI agent technology is general-purpose, allowing for simultaneous improvements across various fronts like frontend, backend, and security <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.
*   **Anthropomorphizing agents**: Agents have different strengths and weaknesses compared to humans. An agent might struggle with basic math but implement a complex frontend feature much faster than any human <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.

## Key Lessons and Insights in [[Developing and optimizing AI agents | Developing and Optimizing AI Agents]]

Several hard-learned lessons provide valuable insights into building effective AI coding agents:

*   **Onboarding the Agent to Your Organization is Crucial**: Just like a new human hire, an agent needs to be onboarded to understand an organization's specific tools, processes, and style guides. This involves creating a "knowledge base"—a set of information (e.g., Markdown files describing version control tools like Graphite, tool stacks, style guides) that the agent can dynamically search when it encounters something it doesn't understand <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>.
*   **When Code is Cheap, Explore More Ideas**: If AI agents make code incredibly inexpensive to write, the bottleneck shifts from engineering hours to good product insights and design. This changes the calculus of product management, allowing teams to quickly gather customer feedback and build more ideas <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.
*   **Sufficient Tests are Critical**: Agents make mistakes, especially in hard-to-test scenarios involving parallel programming or caches. A lack of tests means the agent can mess up <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>. The ability for an agent to run tests, receive feedback, and iterate on fixes (suggesting a fix, running tests, observing feedback, and repeating) led to a 20% gain in a bug-fixing benchmark, far exceeding the 4% gain from a 6-month foundation model upgrade <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>. Better tests enable more autonomy and make agents smarter <a class="yt-timestamp" data-t="15:49:00">[15:49:00]</a>.

## The Future of Software Engineering with Agents

The capabilities of AI agents are rapidly improving, with a compounding effect as they begin to help build themselves <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. While code remains essential as a specification for systems, the relationship between developers and code is changing <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. Good test harnesses are more important than ever, especially for less-tested parts of codebases <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. The shift in product development focus towards rapid customer feedback and insights, due to the low cost of code, is set to positively transform the industry <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>.