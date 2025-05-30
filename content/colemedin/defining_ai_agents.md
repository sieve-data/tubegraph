---
title: Defining AI agents
videoId: GYFTQU2iV4A
---

From: [[colemedin]] <br/> 

The term "AI agent" is often used loosely, with many programs incorporating a Large Language Model (LLM) being labeled as such, but a significant distinction exists between true [[Understanding AI agents | AI agents]] and simple workflows that happen to contain an LLM <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Understanding this difference is crucial because the methods for [[Building AI Agents | building agents]] versus workflows, and their respective applications, are entirely different <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Both are valuable but solve separate problems <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## What is an AI Agent?

A concise definition of an [[Understanding AI agents | AI agent]] helps clarify its nature <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Definitions from Experts

*   **Hugging Face**:
    *   "[[Understanding AI agents | AI agents]] are programs where LLM outputs control the workflow" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. A key characteristic derived from this is "nondeterministic," meaning the exact sequence of events in a workflow controlled by an agent is not predetermined <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. An agent decides what is executed, when, and how many times <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
    *   "[[Understanding AI agents | AI agents]] are AI models that are given the ability to interact with the environment to achieve a certain goal" <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This highlights that [[Understanding AI agents | agents]] are goal-oriented and must reason about how to achieve their objectives <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

*   **Anthropic**:
    *   Anthropic distinguishes between workflows, which are chained LLM calls, and [[Understanding AI agents | agents]], where the LLM determines how many times to run, continuously looping until a resolution is found <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This means the number of steps an [[Understanding AI agents | agent]] takes to complete a task is unknown <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Core Components and Behavior

An [[Understanding AI agents | AI agent]] operates by being given:
*   **Abilities/Tools**: These allow it to interact with its environment, such as Google Drive, Slack, APIs (like a weather API), or perform RAG (Retrieval-Augmented Generation) over a knowledge base <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a> <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a> <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Goals and Preferences**: Defined through a system prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Prior Knowledge**: Acquired through short-term memory (conversation history) or long-term memory (e.g., using RAG) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

The process involves a loop: the agent performs actions, observes the results of those actions in the environment, and then decides whether to perform more actions to achieve its goal. This iterative decision-making, where the number of iterations is not fixed, is the "non-deterministic" behavior <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. The LLM acts as the "brain," deciding what actions to take from its "tool belt" based on user input and observations <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## AI Agents vs. Workflows and Chatbots

It's important to differentiate true [[Understanding AI agents | AI agents]] from simpler constructs.

### Workflows (Not Agents)

A workflow, often built with tools like n8n, Make, or Zapier, is characterized by its sequential and deterministic nature <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a> <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. Even if it incorporates LLM calls, it's not an [[Understanding AI agents | AI agent]] if it follows a predefined path <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

*   **Example**: A workflow that takes a user prompt, crafts a social media post for X (formerly Twitter), posts it, then does the same for LinkedIn and a blog, and finally summarizes the posts, is not an [[Understanding AI agents | AI agent]] <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This is because it always follows the sequence: create X post, post X, create LinkedIn post, post LinkedIn, etc. <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. There is no non-determinism; it would never decide to post twice to X or skip posting to the blog <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. While valuable for its specific purpose, it's a fixed, sequential process <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. In some cases, a simple workflow is actually better than an [[Understanding AI agents | AI agent]], especially when non-determinism is undesirable (e.g., an agent hallucinating and posting twice) <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Chatbots (Not Agents)

A chatbot, even if it uses a sophisticated system prompt to guide a conversation, is not an [[Understanding AI agents | AI agent]] if it doesn't interact with external environments via tools <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a> <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

*   **Example**: A "tech stack expert" chatbot that asks a series of questions about an application and then recommends technologies is not an [[Understanding AI agents | AI agent]] <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. Even if the conversation path is non-deterministic (meaning the number of turns might vary), it's driven solely by the LLM's internal reasoning based on its system prompt, without invoking external tools to gather information or perform actions in an environment <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a> <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **ChatGPT.com**: While powerful, ChatGPT is considered a conversational chatbot <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. Even with web search enabled, it typically searches once, feeds the context to the LLM, and provides a final answer. It doesn't decide to search again to refine its query if the initial results are unsatisfactory <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. The decision to search or not search is very basic and doesn't involve the complex, iterative tool invocation characteristic of an [[Understanding AI agents | AI agent]] <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.

### Actual AI Agents

True [[Understanding AI agents | AI agents]] exhibit both non-determinism and interaction with their environment using tools to achieve a specific goal.

*   **Google Docs Memory Manager Agent**: This agent manages long-term memories and notes using Google Docs <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. It is non-deterministic because it decides whether to save something to notes or memory based on the conversation <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. It interacts with the Google Docs environment via "save notes" and "fetch notes" tools <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **GitHub Agent**: This agent analyzes the structure of a GitHub repository given its URL <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. It is non-deterministic, as it can decide which files to look at and how many times to analyze different `README` files to achieve its goal of describing different versions of a project <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a> <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. It interacts with GitHub, which serves as its environment <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   **Windsurf**: This is presented as a highly "agentic" system <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. When asked to update a model, Windsurf makes numerous decisions behind the scenes, such as analyzing files, invoking tools (like an [[ai_agents_and_their_development | AI agent]] builder), and deciding which files to edit, all within a single flow <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. This complex, non-deterministic decision-making process sets it apart from a simple chatbot <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

## Conclusion

Understanding the difference between [[Understanding AI agents | AI agents]] and simpler LLM-infused workflows is vital <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. While both have their place, [[Understanding AI agents | AI agents]] unlock significantly more possibilities due to their goal-oriented, non-deterministic nature and ability to interact with and reason about their environment using tools <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.