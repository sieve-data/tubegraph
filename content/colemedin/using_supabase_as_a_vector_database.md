---
title: Using Supabase as a vector database
videoId: PEI_ePNNfJQ
---

From: [[colemedin]] <br/> 

Supabase is an exceptional database platform that supports vectors for Retrieval Augmented Generation (RAG) using PG Vector <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It can be leveraged to create a robust, production-ready, and cost-effective RAG AI agent with no code, especially when integrated with [[integrating_n8n_and_supabase | n8n]] <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. Supabase is suitable for both chat memory and vector database needs within an AI agent <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

## Why Use Supabase for RAG?
Supabase offers several advantages for RAG applications:
*   **Vector Support**: It natively supports vectors for RAG through the PG Vector extension <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Dual Functionality**: It can serve as both a chat memory store and a vector database simultaneously <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.
*   **Scalability**: Using PostgreSQL with Supabase for chat memory makes an AI agent scalable and production-ready, unlike local memory options that can overload a server <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.
*   **Cost-Effective**: Supabase offers a generous free tier that is sufficient for getting started and is an "incredible" option until significant scaling is required <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

## Setting Up Supabase as a Vector Store for RAG
To configure Supabase for RAG, follow these steps:

1.  **Sign In**: Go to `supabase.com` and sign in, typically using a GitHub account <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
2.  **Retrieve Credentials**:
    *   **Postgres Connection**: In your project settings, navigate to the `Database` section to find credentials like host, database name, port, user, and password for chat memory <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
    *   **API Connection**: Go to the `API` tab to get your custom URL and service role secret, which are needed for the vector database <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.
3.  **Configure PG Vector and Tables**:
    *   Supabase requires specific SQL code to enable PG Vector and set up the necessary tables and functions for RAG <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>. This SQL code can be found in the documentation for [[setting_up_a_superbase_vector_store_for_rag | setting up a Supabase vector store for RAG]] within n8n <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
    *   Copy all the provided SQL code and paste it into the `SQL Editor` in Supabase <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. This will:
        *   Create the PG Vector extension <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.
        *   Create a `documents` table to store knowledge base content, metadata (like Google Drive file ID), and embedding vectors <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>.
        *   Create a function to match documents for RAG <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>.
    *   n8n can automatically create a table for chat history if one doesn't exist <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

## Supabase Integration for AI Projects

### Chat Memory
[[superbase_integration_for_ai_projects | Supabase integration for AI projects]] uses PostgreSQL for chat memory, ensuring scalability <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>. Credentials for this connection include host, database, user, and password obtained from Supabase project settings <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.

### Vector Store
For RAG, Supabase is connected as a vector store using its API host and service role secret <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>. The `documents` table and `match documents` query are used <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>. This table stores the `page content`, `metadata`, and `embedding Vector` for each document in the knowledge base <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

### Handling Document Updates
A crucial aspect of a production-ready RAG system is managing document updates to prevent duplicates in the vector database <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>. When a Google Drive file is updated, the workflow first deletes any old vectors associated with that file ID from the Supabase database <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. This ensures that only the most current version of a document's embedding is stored <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>. The file ID is stored in the metadata of the Supabase record to facilitate this deletion <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>. After deletion, the new, updated document content is inserted as a fresh vector <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>.