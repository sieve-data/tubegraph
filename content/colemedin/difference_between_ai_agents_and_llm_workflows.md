---
title: Difference between AI agents and LLM workflows
videoId: GYFTQU2iV4A
---

From: [[colemedin]] <br/> 

While many programs incorporating a Large Language Model (LLM) are colloquially referred to as "agents," there is a significant distinction between actual [[defining_ai_agents | AI agents]] and a workflow that merely contains an LLM <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This difference is crucial for [[building_ai_agents | building AI agents]] versus workflows, as each solves entirely separate problems <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[understanding_ai_agents | Understanding AI Agents]]

A concise definition of an [[understanding_ai_agents | AI agent]] involves its ability to control a workflow in a non-deterministic way, interact with an environment, and pursue a specific goal <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Key Definitions

*   **Hugging Face**:
    *   [[defining_ai_agents | AI agents]] are programs where LLM outputs control the workflow <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The key characteristic is "nondeterministic," meaning one does not know exactly what will happen in the workflow, as the agent determines what is executed, when, and how many times <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   [[defining_ai_agents | AI agents]] are AI models given the ability to interact with the environment to achieve a certain goal <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This highlights that agents are goal-oriented, reasoning about how to reach their objective, unlike linear workflows <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Anthropic**:
    *   An [[understanding_ai_agents | agent]] is where the LLM decides how many times to run and continues to loop until it finds a resolution <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This applies to scenarios where the number of steps to complete a task (e.g., customer support, iterating on code) is unknown <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Core Components of an AI Agent

An [[understanding_ai_agents | AI agent]] typically has:
*   **Abilities (Tools)**: Functions given to the agent to interact with external environments or services (e.g., Google Drive, Slack, web search, APIs, calculators) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Goals and Preferences**: Defined through the system prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Prior Knowledge**: Gained from short-term memory (conversation history) or long-term memory (e.g., Retrieval Augmented Generation or RAG) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Action Loop**: The agent performs actions in the environment, observes the results, and then decides whether to take further actions in a non-deterministic loop until its goal is achieved <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. The LLM acts as the "brain," deciding what it needs to do to achieve the goal using its available tools <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## Workflows with LLMs (Not Agents)

A workflow that incorporates an LLM but is not an [[understanding_ai_agents | AI agent]] is often characterized by its sequential nature and lack of non-deterministic decision-making or environment interaction <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Characteristics

*   **Sequential Steps**: Follows a predefined, linear path (e.g., step A, then step B, then step C) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Deterministic**: The flow of operations is predictable, and there's no LLM output controlling the workflow's path or the number of times steps are executed <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Chained LLM Calls**: May involve multiple LLM calls linked together, but without the LLM deciding the overall process flow <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## [[examples_of_ai_agents_and_workflows | Examples of AI Agents and Workflows]]

### Not an AI Agent (Sequential Workflow)

Consider a workflow designed to take a user prompt for a topic, craft a post for Platform X, post it, then do the same for LinkedIn and a blog, and finally summarize what was posted for the user <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Why it's not an agent**: This is a sequential process <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. There is no non-determinism; it would never post twice to X or decide not to post to the blog <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. The LLM is used for content generation for each platform, but it doesn't control the flow <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This type of workflow is valuable when a predictable, predefined output is desired <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Not an AI Agent (Chatbot without Tools)

A "tech stack expert" chatbot that asks questions about application requirements (front end, back end, users) and then recommends technologies is not an [[understanding_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Why it's not an agent**: Although the conversation might be non-deterministic (the number of steps can vary depending on user input) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>, this chatbot does not interact with an external environment using tools <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. The entire conversation is driven solely by a sophisticated system prompt within the LLM <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **ChatGPT.com**: Similarly, ChatGPT.com is primarily a conversational chatbot <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. Even with web search enabled, it typically performs a search once, uses that context for the LLM, and doesn't decide to re-search or refine its search if the information is inadequate <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. The decision to search or not is very basic, making it different from a fully [[understanding_ai_agents | agentic]] system <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.

### Actual AI Agents

*   **Google Docs Long-Term Memory Agent**: This agent manages long-term memories and notes using Google Docs <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
    *   **Why it's an agent**: It has tools to interact with the Google Docs environment <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. It is non-deterministic; sometimes it decides to save information to notes, and other times it doesn't, or it might fetch information from notes without invoking other tools <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Its goal is to answer questions using information stored in the environment <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   **GitHub Agent**: Given a GitHub repository URL, this agent can analyze the repo's structure and decide to look at individual files <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
    *   **Why it's an agent**: It is highly non-deterministic, as it picks which files to look at <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. It interacts with GitHub, which is its environment <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. For example, it might invoke a tool to get the overall structure of a repo and then decide to analyze specific `readme` files multiple times based on its understanding <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Windsurf with Pydantic AI**: This system can update the model used for an [[understanding_ai_agents | agent]], involving complex decisions <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
    *   **Why it's an agent**: It decides to analyze files, invoke tools, and makes numerous decisions in a single flow, such as which files to edit, without a predetermined sequence <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

## Conclusion

Both [[agentic_workflows_and_ai_technology | agentic workflows and AI technology]] and simpler LLM-based workflows are valuable <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. However, [[understanding_ai_agents | AI agents]] offer more possibilities and power due to their non-deterministic nature, goal-oriented behavior, and ability to interact with environments, suggesting a significant future for this approach <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.