---
title: Using Postgres and Superbase for AI chat memory
videoId: 56D91EcaUnM
---

From: [[colemedin]] <br/> 

When building AI agents, especially for production environments, establishing robust chat memory is crucial. While simple [[setting_up_and_optimizing_chat_memory_for_ai_agents | window buffer memory]] suffices for prototyping, a more persistent and scalable solution is needed for production use cases <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>. Postgres, often integrated with [[superbase_integration_for_ai_projects | Supabase]], emerges as a recommended choice for this purpose <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>.

## Why Use Postgres with Supabase for Chat Memory?
For production AI agents, options like Postgres or Redis are preferred for chat memory <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>. [[superbase_integration_for_ai_projects | Supabase]] is a particularly convenient choice because it leverages Postgres, allowing for a unified database solution. With [[superbase_integration_for_ai_projects | Supabase]], you can manage your SQL database and use its PG Vector extension for Retrieval Augmented Generation (RAG), keeping all data on a single platform <a class="yt-timestamp" data-t="00:52:45">[00:52:45]</a>. This simplifies the architecture compared to managing separate databases for different functionalities.

## Setting up Supabase for Chat Memory in n8n
When using n8n's AI Agent node, integrating with [[superbase_integration_for_ai_projects | Supabase]] for chat memory is straightforward. The AI Agent node can automatically create the necessary "messages" table in your Postgres database (hosted via [[superbase_integration_for_ai_projects | Supabase]]) once connected with the correct credentials <a class="yt-timestamp" data-t="01:53:59">[01:53:59]</a>. This table stores the conversation history, allowing the agent to remember past interactions.

### Obtaining Supabase Credentials
To connect n8n to your [[superbase_integration_for_ai_projects | Supabase]] Postgres database:
1.  Navigate to your [[superbase_integration_for_ai_projects | Supabase]] dashboard <a class="yt-timestamp" data-t="01:52:42">[01:52:42]</a>.
2.  Go to **Project Settings** <a class="yt-timestamp" data-t="01:52:44">[01:52:44]</a>.
3.  Click on the **Database** tab <a class="yt-timestamp" data-t="01:53:12">[01:53:12]</a>.
4.  Find **Project Connection Details** by clicking "Connect" in the top bar <a class="yt-timestamp" data-t="01:53:24">[01:53:24]</a>.
5.  This section provides all the necessary information: host, port, database name, and user credentials for connecting to your Postgres database <a class="yt-timestamp" data-t="01:53:34">[01:53:34]</a>.
6.  Enter these details into the PostgreSQL credentials setup in n8n <a class="yt-timestamp" data-t="01:53:44">[01:53:44]</a>.

### Managing Conversation Context
The AI Agent node in n8n allows you to specify the "context window length" for the chat memory <a class="yt-timestamp" data-t="02:17:21">[02:17:21]</a>. This setting determines how many past interactions the model will consider as context. Setting this value appropriately, e.g., to 20, can help prevent the agent from "hallucinating" or forgetting previous messages in the conversation <a class="yt-timestamp" data-t="02:17:34">[02:17:34]</a>.

### Live Reporting of Agent Actions
Beyond storing conversation history, Postgres in [[superbase_integration_for_ai_agents | Supabase]] can be used to provide real-time updates on what the AI agent is doing. By inserting AI messages directly into the messages table, you can stream updates to the user as the agent processes information or performs actions <a class="yt-timestamp" data-t="01:55:01">[01:55:01]</a>. For example, an agent might report "I'm getting the contents of this file..." before providing the actual content <a class="yt-timestamp" data-t="01:55:36">[01:55:36]</a>. This provides visibility into the agent's internal workings and enhances the user experience.

### Integration with RAG Pipelines
[[superbase_integration_for_ai_projects | Supabase]]'s ability to handle both standard SQL data and vector embeddings (via PG Vector) makes it a strong contender for [[using_supabase_as_a_vector_database_for_ai_agents | RAG pipelines]] alongside chat memory <a class="yt-timestamp" data-t="00:52:45">[00:52:45]</a>. This allows agents to retrieve and process information from a knowledge base to answer questions, all within the same [[superbase_integration_for_ai_projects | Supabase]] environment. A [[building_a_local_ai_package_with_supabase | local AI package]] can be built that includes [[superbase_integration_for_ai_projects | Supabase]] for both chat memory and RAG, offering a comprehensive solution for AI agent development <a class="yt-timestamp" data-t="01:32:09">[01:32:09]</a>.