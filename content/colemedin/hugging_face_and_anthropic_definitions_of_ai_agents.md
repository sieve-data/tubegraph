---
title: Hugging Face and Anthropic definitions of AI agents
videoId: GYFTQU2iV4A
---

From: [[colemedin]] <br/> 

There's a significant difference between actual [[understanding_ai_agents | AI agents]] and workflows that merely incorporate a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Understanding this distinction is crucial because the methods for [[building_ai_agents | building AI agents]] versus workflows, and their respective applications, are entirely different <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This article breaks down what an [[understanding_ai_agents | AI agent]] is, drawing upon definitions from prominent sources like Hugging Face and Anthropic <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Defining AI Agents <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>

Many programs are now called "agents" simply because they integrate an LLM, but the concept is more complex <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A concise definition is essential for anyone involved in [[building_ai_agents | building AI agents]] <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Hugging Face's Perspective

Hugging Face provides a clear starting point for [[defining_ai_agents | AI agents]]:
*   **Initial Definition:** [[defining_ai_agents | AI agents]] are programs where LLM outputs control the workflow <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The key characteristic here is **nondeterministic** behavior; the exact sequence of events in a workflow controlled by an agent is unknown <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. An agent determines what is executed, when, and how many times <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Expanded Definition:** From their [[understanding_ai_agent_frameworks | AI agent course]], Hugging Face further defines [[defining_ai_agents | AI agents]] as "AI models that are given the ability to interact with the environment to achieve a certain goal" <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This highlights that agents are **goal-oriented**, reasoning about how to reach their objectives, unlike workflows which typically follow a linear path <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Anthropic's Perspective

Anthropic's definition of [[defining_ai_agents | AI agents]] aligns closely with Hugging Face's, emphasizing the distinction from chained LLM calls in workflows <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>:
*   **Key Distinction:** While workflows involve chaining a few LLM calls together, an actual [[defining_ai_agents | AI agent]] allows the LLM to decide how many times to run and to continue looping until a resolution is found <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This means the number of steps required to complete a task is unknown, making it non-deterministic <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Examples include a customer support agent interacting with a customer or iterating on code changes <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Core Characteristics of AI Agents

Based on these definitions, key characteristics of [[understanding_ai_agents | AI agents]] include:
*   **Non-deterministic Behavior:** The workflow path is not fixed; the LLM decides the sequence and number of actions <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Goal-Oriented:** Agents are designed to achieve a specific objective and reason about the steps needed <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Interaction with Environment:** Agents are equipped with "tools" (e.g., Google Drive, Slack, APIs, web search, database queries) to interact with their environment and perform actions on behalf of the user <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Observational Loop:** Agents observe the outcome of their actions, and based on these observations, may decide to invoke tools again in a loop until the goal is met <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This feedback loop is central to their non-deterministic nature <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Prior Knowledge:** Agents utilize system prompts for goals/preferences and memory (short-term like conversation history, or long-term like RAG) for prior knowledge <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Visualizing the Agent Architecture

Diagrams help illustrate the flow:
*   An agent receives abilities (tools), goals, preferences (via system prompt), and prior knowledge (memory) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   It performs actions in the environment using these tools (e.g., drafting emails, sending messages, querying databases) <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   The agent then observes the results of these actions and may loop back to interact with the environment again, deciding how many times to do so to achieve its goal <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Tools are functions (e.g., web exploration, API calls, RAG over a knowledge base, calculator) that enable the agent to interact with its environment <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   User input goes to the LLM (the "brain"), which decides what actions (tools) to use. Observations from tool use feed back to the LLM for potential further tool invocation in a non-deterministic loop, before sending final results to the user <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Differentiating Agents from Workflows and Chatbots

Not every process involving an LLM is an [[defining_ai_agents | AI agent]]:
*   **Sequential Workflows (Not Agents):** A workflow that chains LLM calls together in a predetermined, sequential manner is not an [[defining_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. For example, a workflow that creates and posts content to X, LinkedIn, and a blog sequentially, then summarizes it, is valuable but lacks non-determinism <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. There's no decision-making to post twice or omit a platform; it's simply step A, then B, then C <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. While such a workflow could be turned into an agent by giving it tools and asking it to decide, this would introduce unwanted non-determinism (e.g., hallucinating and posting twice) <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Chatbots (Not Agents without Tools):** A chatbot, even if it exhibits non-deterministic conversational flow (e.g., asking follow-up questions until information is gathered), is not an [[defining_ai_agents | AI agent]] if it doesn't interact with the environment using tools <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. The entire conversation is driven solely by a system prompt without invoking external tools <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. ChatGPT, even with web search enabled, primarily functions as a conversational chatbot; it searches the web and provides context to the LLM, but it doesn't typically decide to refine its search or search again if it found wrong information <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

## Examples of True AI Agents

True [[defining_ai_agents | AI agents]] meet the criteria of having tools, being non-deterministic, and working towards a goal:
*   **Google Docs Memory Agent:** An agent that manages long-term memories and notes in Google Docs fits all criteria <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. It has tools to save and fetch notes from Google Docs (interacting with the environment) <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. It's also non-deterministic because it decides whether or not to save information based on the input, and can retrieve information from memory without invoking tools <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   **GitHub Agent:** A GitHub agent that analyzes repository structures and individual files demonstrates non-determinism by picking which files to analyze <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. It interacts with GitHub as its environment <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. For example, it might decide to get the overall structure, then analyze multiple READMEs, and the number of times it invokes these tools can vary <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Windswept/Arcane AI Agent Builder:** Platforms like Wind Surf that allow users to update agents (e.g., changing the LLM used) demonstrate significant decision-making behind the scenes <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. The agent decides which files to analyze and edit, making it highly agentic and non-deterministic <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

While both workflows and [[defining_ai_agents | AI agents]] are valuable, [[ai_agents_and_their_development | AI agents]] unlock significantly more possibilities and power due to their autonomous decision-making and environmental interaction capabilities <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.