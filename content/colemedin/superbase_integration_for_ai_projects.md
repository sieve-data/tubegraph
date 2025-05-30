---
title: Superbase integration for AI projects
videoId: iOZpiXLT7iY
---

From: [[colemedin]] <br/> 

AI agents are designed to behave more like humans, making decisions on the fly and acting on a user's behalf, which is why they are considered a crucial use case for LLMs <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. However, these agents often suffer from poor memory <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. While Retrieval Augmented Generation (RAG) helps agents learn from documents, it doesn't provide true long-term memory from conversations <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. To achieve personalization and human-like behavior, AI agents need the ability to learn from interactions, remembering user goals, preferences, instructions, and corrections <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

This article details how to build self-learning AI agents with long-term memory by integrating [[using_supabase_for_ai_agents | Supabase]] as a vector database and for authentication, using the open-source Python library MemZero <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## The Challenge of AI Agent Memory

Without long-term memory, AI chatbots like Gemini 2.0 Flash cannot recall previous conversations <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For example, if a user describes their tech stack in one chat session, a new session will not retain that information, forcing the user to repeat important details <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This lack of persistent memory makes interactions super annoying <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Introducing MemZero for Long-Term Memory

MemZero is an [[open_source_ai_tools_for_database_management | open-source]] Python library designed to build knowledge, or memories, about individual users as they interact with an agent <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It can be installed via `pip install Memzero AI` <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. MemZero offers both a hosted platform and a completely free self-hosting option <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Basic MemZero Implementation

A basic implementation of MemZero involves:
*   **Configuration**: Setting up the LLM (e.g., GPT-4 Mini) used by MemZero to extract or search memories <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Client Initialization**: Creating OpenAI and MemZero clients <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **`chat_with_memories` function**: This function takes the current message and a user ID (to segregate memories) <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   It retrieves the most relevant memories using the `search` function, limiting to three <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
    *   These memories are incorporated into the system prompt for the LLM <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
    *   The LLM generates a response based on the latest user message and retrieved memories, *without* maintaining conversational history <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   The user message and AI response are then passed to MemZero's `add` function to extract and store key memories for the specific user <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

Initially, memories are stored in memory within the script <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Despite no conversation history, the agent can recall preferences based on long-term memory <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## [[using_supabase_as_a_vector_database_for_ai_agents | Using Supabase as a Vector Database for AI Agents]]

Integrating [[using_supabase_for_ai_agents | Supabase]] allows for persistent storage of memories, moving beyond in-memory storage <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Configuration**: The `MemZero` client configuration is updated to specify [[using_supabase_as_a_vector_database_for_ai_agents | Supabase]] as the vector store <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Connection String**: A [[using_postgres_and_superbase_for_ai_chat_memory | Supabase]] connection string (found in the Project Settings -> Database -> Connection String) is used <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Memory Storage**: MemZero automatically creates a `memories` table within the `vex` schema in your [[using_supabase_for_ai_agents | Supabase]] instance <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Persistence**: Memories, including vectorized text and metadata (like user ID and timestamp), are stored in [[using_supabase_for_ai_agents | Supabase]] and persist even if the script is restarted <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## [[superbase_authentication_integration_in_ai_apps | Superbase Authentication Integration in AI Apps]]

To handle user-specific memories, [[superbase_authentication_integration_in_ai_apps | Supabase authentication]] is used to obtain unique user IDs <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   **Streamlit UI**: A simple Streamlit user interface is created to demonstrate this <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   **User Session State**: User information, including the user ID, is stored in the UI's session state after signup or login through [[superbase_authentication_integration_in_ai_apps | Supabase authentication]] <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Dynamic User ID**: The fetched user ID from [[superbase_authentication_integration_in_ai_apps | Supabase]] is passed to the `chat_with_memories` function, ensuring that memories are segregated by individual users <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. This prevents accidental retrieval of memories from different users <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
*   **Demonstration**: By logging in with different accounts, the agent recalls distinct memories for each user, proving the effective segregation of data <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

The integrated agent can be tried out at `studio.automator.ai` where a [[integration_with_tools_like_superbase_and_pyantic_ai | Pyantic AI]] Mem agent is available <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Behind the Scenes: How MemZero Works

MemZero performs sophisticated operations to manage long-term memory:

### Adding Memories
Messages from a conversation are fed into a large language model (LLM) that is specifically prompted to extract key memories <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>. These new memories are then added to a vector database, creating a RAG-like knowledge base for each user <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. MemZero also handles conflict resolution to avoid duplicating similar existing memories <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.

### Searching Memories
Before the primary AI agent processes a query, an LLM intelligently rewrites the query to extract the most relevant information from the vector database <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. The relevant memories are then fed into the AI agent, providing it with long-term memory capabilities <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. MemZero implements advanced RAG techniques such as reranking relevant scores and including metadata and timestamps to ensure robust long-term memory <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

MemZero offers significant customization and control through its Python and Node SDKs, allowing developers to tailor memory addition and search functions to specific use cases <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. It can be integrated with any agent framework <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.