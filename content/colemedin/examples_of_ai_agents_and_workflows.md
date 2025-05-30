---
title: Examples of AI agents and workflows
videoId: GYFTQU2iV4A
---

From: [[colemedin]] <br/> 

It is crucial to understand the distinction between actual [[defining_ai_agents | AI agents]] and [[creating_custom_ai_workflows_with_n8n | workflows]] that incorporate a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While both are valuable, they solve different sets of problems <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. [[Building AI Agents | Building]] an agent versus a workflow requires different approaches <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[Understanding AI agents | Defining AI Agents]]

Many programs are now being called "agents" simply because they include an LLM <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, a concise definition is necessary for clarity <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Key Characteristics

*   **LLM Control**: [[defining_ai_agents | AI agents]] are programs where LLM outputs control the workflow <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Non-Deterministic**: A key characteristic is that their behavior is non-deterministic <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This means the exact sequence of actions is not predefined; the agent determines what is executed, when, and how many times <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Interaction with Environment**: [[defining_ai_agents | AI agents]] are [[understanding_ai_agents | AI models]] that are given the ability to interact with their environment to achieve a specific goal <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Goal-Oriented**: Unlike linear workflows, agents have a goal in mind and reason about how to achieve it <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. They continue to loop until a resolution is found, taking an unknown number of steps <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Agent Structure

[[defining_ai_agents | An agent]] is typically provided with:
*   **Abilities (Tools)**: Functions to interact with services like Google Drive, Slack, web search, APIs, or databases <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Goals and Preferences**: Defined through the system prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Prior Knowledge**: Through short-term memory (conversation history) or long-term memory (e.g., RAG) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

The agent then performs actions in the environment and observes the results <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. This creates a loop where the agent might decide to interact with the environment again based on its observations, repeating actions an unknown number of times until its goal is achieved <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. The LLM acts as the "brain," deciding what to do to achieve the user's goal <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## Examples of Workflows (Not [[defining_ai_agents | AI Agents]])

### 1. Social Media Content Generator (n8n)

This workflow takes a user prompt, crafts a post for X (formerly Twitter), then for LinkedIn, and finally for a blog <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. An LLM might be used to summarize the output for the user <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

*   **Why it's not an agent**: It is a sequential workflow where LLM calls are chained together <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. There is no non-determinism; it always follows the same steps (create X post, post it, then LinkedIn, then blog) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The system would never post twice to X or decide not to post to the blog <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Value**: This is a valuable workflow, often built in tools like Make, [[using_n8n_for_api_workflows_in_ai_agents | n8n]], and Zapier, as it allows for crafting platform-specific messages <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. In this scenario, a simple workflow is actually better than an agent because the non-determinism of an agent could lead to undesirable outcomes like hallucinating and posting twice, or not posting when intended <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### 2. Tech Stack Expert Chatbot (n8n)

This example features a chatbot designed to act as a tech stack expert, asking questions about an application to recommend technologies for front-end, back-end, and database <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

*   **Why it's not an agent**: The entire conversation is driven by a single LLM and a "fancy system prompt" <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The key element missing is interaction with the environment via tools <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. While it is non-deterministic (the number of conversational steps might vary), it does not meet the criteria of interacting with the environment beyond acting as a normal chatbot <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

### 3. ChatGPT

ChatGPT.com, even with web search enabled, is primarily a conversational chatbot <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

*   **Why it's not an agent**: When it searches the web, it feeds that information as context to the LLM to provide a final answer <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. It's not an agent that can decide to search the web again to refine its search if the initial information is incorrect <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. While it can decide whether or not to search, this is a very basic decision compared to the complex decision-making of a true agent <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.

## [[Realworld use cases for AI agents | Examples of AI Agents]]

### 1. Google Docs Memory Manager (n8n)

This agent manages long-term memories and notes using Google Docs <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

*   **Why it is an agent**:
    *   **Tools**: It has tools to interact with the Google Docs environment <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
    *   **Non-Deterministic**: The agent decides whether to save anything to notes or long-term memory <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. It might invoke tools or not, and the number of times it invokes them is not fixed <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
    *   **Goal-Oriented**: Its goal is to answer questions using the environment (Google Docs) <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. It can fetch information from Google Docs based on a query <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

### 2. GitHub Agent (n8n)

This agent can analyze the structure of a GitHub repository given its URL <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. It can then decide to look at individual files <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

*   **Why it is an agent**:
    *   **Interaction with Environment**: It interacts with GitHub, which is its environment <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
    *   **Non-Deterministic**: It is highly non-deterministic, as it can pick which files to look at and how many times to invoke its tools <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>, <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. For example, it might get the overall structure and then make multiple calls to analyze specific READMEs <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
    *   **Goal-Oriented**: It is goal-oriented, aiming to describe different versions of a project by analyzing its repository <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

### 3. Windsurf

Windsurf is a real-world example of a highly [[agentic_workflows_and_ai_technology | agentic]] system <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

*   **Why it is an agent**: When given a prompt, such as to update the model used for an agent, Windsurf makes many complex decisions behind the scenes <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. It decides what files to analyze and what files to edit, invoking tools to interact with the environment to achieve its goal <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. The user has no idea how many steps it will take or which specific actions it will perform <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

Both [[agentic_workflows_and_ai_technology | AI agents]] and [[creating_custom_ai_workflows_with_n8n | workflows]] are valuable <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>. However, [[voice_ai_agents | AI agents]] offer significantly more possibilities and power due to their ability to make independent decisions and interact with complex environments <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.