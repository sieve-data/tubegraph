---
title: N8N in creating AI agents
videoId: GYFTQU2iV4A
---

From: [[colemedin]] <br/> 

There is a significant distinction between true AI agents and workflows that merely incorporate a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While both are valuable, they solve different problems <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This article clarifies what constitutes an AI agent, particularly in the context of [[building_ai_agents_with_nocode_tools | no-code tools]] like n8n <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Defining an AI Agent

A precise definition of an AI agent is crucial for understanding its capabilities and how it differs from a standard workflow <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Key Characteristics

*   **LLM Control over Workflow** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>: AI agents are programs where LLM outputs dictate the workflow <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Non-Determinism** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>: The specific steps and outcomes of an agent-controlled workflow are not predetermined <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The agent decides what is executed, when, and how many times <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Interaction with Environment** <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>: AI agents are models capable of interacting with their environment to achieve a specific goal <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Goal-Oriented** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>: Unlike linear workflows, agents have a goal in mind and reason about how to reach it <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Iterative Looping** <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>: An agent allows the LLM to decide how many times to run, continuously looping until a resolution is found <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This means the number of steps required is unknown beforehand <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Components of an AI Agent

An AI agent is typically given:
*   **Abilities/Tools**: Functions to interact with services like Google Drive, Slack, web search, APIs, or a knowledge base for [[creating_rag_ai_agents_using_n8n | RAG]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Goals and Preferences**: Defined through the system prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Prior Knowledge**: Through short-term memory (conversation history) or long-term memory (like [[n8n_rag_ai_agent | RAG]]) <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

The agent then performs actions, observes the outcomes, and decides whether to continue interacting with the environment in a non-deterministic loop until its goal is achieved <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Workflows vs. Agents in n8n

n8n's visual workflow builder helps illustrate the difference between sequential workflows and true AI agents <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Examples of "Not an Agent" Workflows in n8n

1.  **Sequential Social Media Posting Workflow**:
    *   **Description**: This workflow takes a user prompt, crafts a post for X (formerly Twitter), posts it, then does the same for LinkedIn and a blog, finally summarizing the actions <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Why it's not an agent**: It's a workflow chaining LLM calls together <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. It is sequential; there's no non-determinism <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The workflow never posts twice to X or decides not to post to the blog, demonstrating a lack of LLM control over the flow <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Such workflows are valuable for their predictability <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
2.  **Tech Stack Expert Chatbot**:
    *   **Description**: This n8n chat window example acts as a tech stack expert, asking questions about desired application features (frontend, backend, database, users, AI coders) and then recommending technologies <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   **Why it's not an agent**: The entire conversation is driven by a single LLM with a sophisticated system prompt, without invoking any external tools to interact with an environment <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Although it is non-deterministic (the conversation length can vary) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>, it doesn't interact with an environment, which is a key criterion for an agent <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Examples of Actual AI Agents in n8n

1.  **Google Docs Memory Manager Agent**:
    *   **Description**: This agent manages long-term memories and notes using Google Docs <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
    *   **Why it is an agent**: It has tools to interact with Google Docs (its environment) to save and fetch notes <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. It is non-deterministic, as the agent decides whether to save anything to notes based on user input <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. For example, a "Hi" message won't trigger the save tool, but an explicit request to remember something will <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>, <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. It can also fetch information from the Google Doc when asked <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
2.  **GitHub Agent**:
    *   **Description**: This agent, built for [[building_ai_agents | building AI agents]], takes a GitHub repository URL, analyzes its structure, and decides which individual files to examine <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
    *   **Why it is an agent**: It interacts with GitHub, which is its environment <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. It is highly non-deterministic because it autonomously decides which files to look at and how many times to invoke its analysis tools <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. For instance, it can first get the overall repo structure, then analyze multiple README files for different versions of a project, demonstrating the LLM's control over tool invocation <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

### Real-World Comparisons

*   **ChatGPT.com**: Generally considered a conversational chatbot <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. Even with web search enabled, it simply feeds search results as context to the LLM; it doesn't decide to search again to refine results if the initial information is incorrect <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. While it makes a basic decision (to search or not to search), it lacks the deeper decision-making complexity of a true agent <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.
*   **Windsurf**: This platform is described as very "agentic" <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. When asked to update an agent's model, Windsurf makes numerous complex decisions behind the scenes, such as analyzing files and invoking tools to edit files, all within a single flow <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. This demonstrates a much higher level of non-deterministic decision-making compared to a standard chatbot <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

## Conclusion

Understanding the difference between AI agents and LLM-enhanced workflows is essential <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. While both have their uses, AI agents, with their non-deterministic nature and ability to interact with environments, unlock a vast array of possibilities <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. This distinction is vital for anyone [[prototyping_ai_agents_using_n8n | prototyping AI agents using n8n]] or considering [[using_n8n_for_api_workflows_in_ai_agents | using n8n for API workflows in AI Agents]] and aiming for [[tips_for_scalable_ai_agents_in_n8n | scalable AI agents in n8n]] or [[integrating_ai_agents_in_n8n_using_open_web_ui | integrating AI Agents in n8n using Open Web UI]].