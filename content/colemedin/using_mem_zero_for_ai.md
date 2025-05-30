---
title: Using Mem Zero for AI
videoId: iOZpiXLT7iY
---

From: [[colemedin]] <br/> 

[[understanding_ai_agents | AI agents]] are considered a crucial use case for Large Language Models (LLMs) due to their ability to act more like humans, making decisions on the fly and performing actions on behalf of users <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, a significant [[challenges_of_ai_memory_retention | challenge of AI memory retention]] is their often "terrible memory" <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. While Retrieval-Augmented Generation (RAG) using documents is important for teaching [[understanding_ai_agents | AI agents]], it doesn't address true memory based on conversations <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

[[implementing_long_term_memory_in_ai | Implementing long-term memory in AI]] allows [[understanding_ai_agents | AI agents]] to learn from interactions, remembering user goals, preferences, instructions, and corrections <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This capability elevates [[understanding_ai_agents | AI agents]] to a new level of personalization and human-like behavior <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Mem Zero, an open-source Python library, offers a solution for [[implementing_long_term_memory_in_ai | building self-learning agents]] that acquire knowledge (memories) about individual users through interactions <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## The Problem: Limited AI Memory

Traditional LLMs or chatbots often lack long-term memory across conversations <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, a chatbot like Gemini 2.0 Flash, without [[implementing_long_term_memory_in_ai | long-term memory]], will not remember previous discussions about a user's tech stack (e.g., Redis, Superbase) when a new chat is started <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This forces users to repeat important details from past conversations <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Mem Zero: The Solution for Persistent Memory

Mem Zero enables [[understanding_ai_agents | AI agents]] to retain information across conversations, providing a much more tailored and personal experience <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The Pyantic AI mem agent, for instance, demonstrates this capability by recalling specific user tech stacks in new conversations <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This allows [[understanding_ai_agents | AI agents]] to build a user-specific knowledge base <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Getting Started with Mem Zero

Mem Zero is easy to set up <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Installation is done via `pip install Memzero AI` <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It is 100% open-source, allowing for self-hosting <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Basic Implementation (Version 1)

A basic implementation of Mem Zero involves:
*   **Initialization**: Setting up configuration for the LLM (e.g., GPT-4 Mini) used by Mem Zero to extract and search memories <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. An OpenAI client and a Mem Zero client are created <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **`chat_with_memories` Function**: This function takes the current user message and a `user_ID` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The `user_ID` is critical for segregating memories between different users, ensuring that an agent doesn't fetch a memory from another user <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   **Retrieving Memories**: `memzero client search` is used with the latest message and `user_ID` to retrieve the most relevant memories (e.g., top three) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. These are then formatted as a string to be passed into the system prompt <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    *   **Generating Response**: The system prompt (including relevant memories) and the user's latest message are sent to the OpenAI client to get a response <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. It's important to note that this initial setup does *not* build up traditional conversation history, proving that Mem Zero's memory is distinct <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
    *   **Adding Memories**: After the agent responds, the user message and AI response are passed to the `memzero client add` function. This function extracts key memories for the specific user and stores them <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Persistence**: In this basic version, memories are initially stored in script memory <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

Even without conversation history, an agent using Mem Zero can recall user preferences based on stored long-term memories <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The number of intervening messages or conversations does not affect the ability to retrieve these stored memories <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Integration with Superbase for Persistent Storage (Version 2)

To persist memories beyond a single script run, Mem Zero can be integrated with Superbase <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This is achieved by changing the Mem Zero client configuration to use Superbase as the vector store <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. The Superbase connection string is provided via an environment variable <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

Mem Zero automatically creates a `memories` table within the `VEX` schema in your Superbase instance <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Memories are stored as embeddings, along with metadata like the vectorized text, `user_ID`, and a timestamp <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This allows memories to persist even if the script is quit and restarted <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

### Advanced User Authentication with Superbase (Version 3)

For real-world applications, robust user authentication is essential. This can be demonstrated using a simple Streamlit user interface integrated with Superbase authentication <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Superbase Authentication**: Superbase URL and key are used to authenticate users <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. The authenticated user's details, including their `user_ID`, are stored in the user interface's session state <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **Dynamic `user_ID`**: The `user_ID` from the signed-in user is dynamically passed to the `chat_with_memories` function, replacing the default placeholder value <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. This ensures that memories are stored and retrieved separately for each authenticated user <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

This setup guarantees that an agent will not accidentally reference a memory from a different user, as memories are segregated by their unique `user_ID` in the Superbase database <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.

## How Mem Zero Works Behind the Scenes

Mem Zero provides a powerful version of [[implementing_long_term_memory_in_ai | long-term memory]] by handling complex processes behind the scenes <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. It integrates with any [[understanding_ai_agents | agent framework]] <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. Its core functionalities are adding and searching for memories <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

### Adding Memories
*   Messages from a conversation are fed into a separate LLM component within the Mem Zero system <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   This LLM is specifically prompted to extract key memories from the conversation <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
*   These new memories are then added to a vector database, creating a RAG-like knowledge base for each individual user <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
*   Mem Zero also performs advanced functions like conflict resolution, preventing the duplication of similar memories <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
*   It supports more advanced use cases like a graph knowledge implementation for storing entities and relations <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.

### Searching Memories
*   Before the primary [[understanding_ai_agents | AI agent]] processes a query, an LLM within Mem Zero intelligently rewrites the query to extract the most relevant information from the vector database <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
*   The relevant memories retrieved from the vector database are then supplied to the [[understanding_ai_agents | AI agent]], granting it [[implementing_long_term_memory_in_ai | long-term memory capability]] <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.
*   Mem Zero implements advanced RAG techniques, such as reranking relevant scores and including metadata and timestamps, to ensure robust long-term memory retrieval <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

While platforms like ChatGPT integrate similar memory concepts, Mem Zero provides a high level of customization and control through its Python and Node SDKs, allowing developers to tailor how memories are added and searched to fit specific use cases <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.