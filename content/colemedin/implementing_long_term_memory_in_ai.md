---
title: Implementing long term memory in AI
videoId: iOZpiXLT7iY
---

From: [[colemedin]] <br/> 

[[understanding_ai_agents | AI agents]] are designed to function more like humans than traditional workflows or automations, making decisions dynamically and acting on a user's behalf. This capability is why [[understanding_ai_agents | AI agents]] are considered a crucial application for Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, despite their human-like aspirations, many AI agents often suffer from poor memory retention <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, presenting significant [[challenges_of_ai_memory_retention | challenges of AI memory retention]].

Current efforts often focus on teaching [[understanding_ai_agents | AI agents]] through documents using [[retrieval_augmented_generation_rag_in_ai | Retrieval Augmented Generation (RAG)]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. While important, this approach isn't true memory <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Effective [[implementing_longterm_and_shortterm_memory_in_ai_agents | implementing long-term and short-term memory in AI agents]] requires the ability to learn not only from documents but also from ongoing conversations <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This allows [[understanding_ai_agents | AI agents]] to remember user goals, preferences, instructions, and corrections, leading to a higher level of personalization and human-like behavior <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

A solution for this is [[using_mem_zero_for_ai | Mem Zero]], an open-source Python library designed to build self-learning agents by accumulating knowledge, or memories, about individual users as they interact with the agent <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## The Problem: AI Without Long-Term Memory

To illustrate the [[challenges_of_ai_memory_retention | challenges of AI memory retention]], consider a chat with an LLM lacking [[implementing_longterm_and_shortterm_memory_in_ai_agents | long-term memory]].

### Case Study: Gemini 2.0 Flash
When interacting with a chatbot like Gemini 2.0 Flash, which does not have [[implementing_longterm_and_shortterm_memory_in_ai_agents | long-term memory]], it fails to retain information across new chat sessions <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. For example:
*   A user describes their tech stack (e.g., Redis, Superbase) to the chatbot <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   In a new chat, if asked about database considerations, the chatbot does not recall the previously mentioned tech stack. Instead, it might list irrelevant services like MongoDB or Oracle, indicating a lack of persistent memory <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   This necessitates the user to constantly re-provide important details from previous conversations, making the interaction cumbersome <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## The Solution: AI With Long-Term Memory via Mem Zero

In contrast, an [[understanding_ai_agents | AI agent]] integrated with [[using_mem_zero_for_ai | Mem Zero]] can maintain [[implementing_longterm_and_shortterm_memory_in_ai_agents | long-term memory]] across interactions.

### Case Study: Pyantic AI Mem Agent
An agent built with [[using_mem_zero_for_ai | Mem Zero]], such as the Pyantic AI Mem Agent, demonstrates effective memory retention:
*   The agent acknowledges a user's tech stack <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   When a new conversation is started, the agent can recall the user's previously stated technologies (e.g., Superbase, PostgreSQL, Redis) and provide tailored considerations <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   Unlike agents without memory, it only references technologies the user is actually using, leading to a much more personalized and useful response <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   This capability allows [[understanding_ai_agents | AI agents]] to build a user-specific knowledge base by remembering past interactions <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Getting Started with Mem Zero

[[using_mem_zero_for_ai | Mem Zero]] is designed for ease of use, with a GitHub repository available for installation and setup <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Installation and Hosting
*   **Installation:** Simply use `pip install memzero-ai` if Python is installed on your machine <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Hosting:** [[using_mem_zero_for_ai | Mem Zero]] can be self-hosted completely for free as it is 100% open-source, or you can use their platform to host it <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Basic Implementation Steps

#### 1. Configuration
Initialize the [[using_mem_zero_for_ai | Mem Zero]] client and OpenAI client. The configuration for the LLM used by [[using_mem_zero_for_ai | Mem Zero]] (e.g., GPT-4 Mini) is set to extract memories or perform searches <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

#### 2. Chat with Memories Function
This function takes the current user message and a `user_ID` to segregate memories between different users <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Retrieve Relevant Memories:** Use `mem_zero_client.search()` with the latest message and `user_ID`, limiting results to the most relevant ones (e.g., top three) <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **System Prompt Integration:** The retrieved memories are converted to a string and passed into a system prompt (e.g., "Answer based on the user's latest message and the memories we are giving") <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **LLM Request:** An array of messages (system prompt + latest user message) is sent to the LLM (e.g., GPT-4 Mini). This setup deliberately excludes conversation history to demonstrate that memory is derived from stored long-term data, not chat logs <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Add New Memories:** After the LLM provides a response, the user message and AI response are used by `mem_zero_client.add()` to extract and store key memories for the specific user <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

#### 3. Testing Basic Long-Term Memory
In a basic implementation, even without conversation history, an agent can remember past interactions. For instance, if a user states a food preference, the agent can recall it later, proving that the information is stored in a long-term knowledge base, not just short-term conversation context <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

### Integrating Superbase for Persistent Storage and User Authentication
To store memories persistently and handle user authentication, Superbase can be integrated.

#### 1. Connecting Superbase
The [[using_mem_zero_for_ai | Mem Zero]] client's configuration is updated to use Superbase as the vector store instead of the default in-memory method <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. This requires setting a Superbase connection string as an environment variable <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. [[using_mem_zero_for_ai | Mem Zero]] conveniently creates the necessary 'vex' schema and 'memories' table in Superbase automatically <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

#### 2. Storing Memories in Superbase
When a user interacts with the agent, [[using_mem_zero_for_ai | Mem Zero]] vectorizes the extracted memories and stores them in the Superbase 'memories' table. Each memory includes metadata like the vectorized text, `user_ID`, and a timestamp <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. These memories persist even if the script is restarted <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

#### 3. User Authentication with Superbase
For personalized memory management, Superbase authentication can be used to dynamically assign `user_ID`s to memories:
*   A simple Streamlit user interface can be built for user sign-up and sign-in <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   The Superbase URL and key are used for authentication <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   The authenticated user's ID from Superbase is stored in the UI's session state <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   This dynamic `user_ID` is then passed to the `chat_with_memories` function, ensuring that memories are segregated and linked to the correct user <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

This setup guarantees that the agent will not accidentally reference memories from a different user, even if the information for different users is contradictory <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. This means the agent consistently provides responses based on the individual user's stored knowledge base <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

## How Mem Zero Works Behind the Scenes

[[using_mem_zero_for_ai | Mem Zero]] provides powerful [[advanced_architecture_for_ai_agents | advanced architecture for AI agents]] for [[implementing_longterm_and_shortterm_memory_in_ai_agents | long-term memory]], even with basic implementations <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. Its core functionalities are adding and searching for memories, which can be integrated with any agent framework <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

### Adding Memories
1.  **Message Ingestion:** Messages from a conversation are received <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
2.  **Memory Extraction:** A dedicated LLM, separate from the main agent, is prompted to extract key memories from the conversation <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.
3.  **Vector Database Storage:** These new memories are added to a vector database, creating a [[retrieval_augmented_generation_for_ai | RAG]] setup or knowledge base for each individual user <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
4.  **Conflict Resolution:** [[using_mem_zero_for_ai | Mem Zero]] manages new memories, performing conflict resolution to prevent duplication and ensure efficiency when similar memories already exist <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
5.  **Graph Knowledge (Advanced):** For more advanced use cases, [[using_mem_zero_for_ai | Mem Zero]] can store entities and relationships in a graph knowledge implementation to enhance its power <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.

### Searching Memories
1.  **Pre-processing Query:** Before the primary [[understanding_ai_agents | AI agent]] processes a query, [[using_mem_zero_for_ai | Mem Zero]] executes its search function <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.
2.  **Intelligent Query Rewriting:** An LLM intelligently rewrites the user query to extract the most relevant information from the vector database <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
3.  **Memory Retrieval:** Relevant memories are pulled from the vector database (or knowledge graphs in advanced setups) <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.
4.  **Agent Integration:** These retrieved memories are then fed into the [[understanding_ai_agents | AI agent]] to provide it with [[implementing_longterm_and_shortterm_memory_in_ai_agents | long-term memory]] capabilities <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.
5.  **Advanced RAG Techniques:** [[using_mem_zero_for_ai | Mem Zero]] employs [[retrieval_augmented_generation_for_ai | advanced RAG techniques]] such as reranking relevant scores and including metadata and timestamps to ensure robust long-term memory <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

While platforms like ChatGPT integrate similar memory functionalities, [[using_mem_zero_for_ai | Mem Zero]] offers a higher level of customization and control through its Python and Node SDKs, allowing developers to tailor memory addition and search functions to specific use cases <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. This provides a strong foundation for [[setting_up_and_optimizing_chat_memory_for_ai_agents | setting up and optimizing chat memory for AI agents]] and taking them to production <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.