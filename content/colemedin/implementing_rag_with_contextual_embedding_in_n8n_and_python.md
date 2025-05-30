---
title: Implementing RAG with contextual embedding in N8N and Python
videoId: z_LGan-t2Mo
---

From: [[colemedin]] <br/> 

This guide provides a practical approach to enhancing [[enhancing_ai_agents_with_RAG_technology | Retrieval Augmented Generation (RAG)]] accuracy using [[contextual_retrieval_in_RAG | contextual retrieval]], a strategy introduced by Anthropic [00:00:08]. Understanding such strategies is crucial for [[building_ai_agents_with_n8n | building AI agents]] that can effectively leverage external knowledge, such as documents [00:00:20].

## Basic RAG Explained

A basic [[building_a_nocode_RAG_ai_agent | RAG]] [[building_ai_agents_with_n8n | AI agent]] involves several steps:
1.  **Document Source**: Files are watched for creation or updates (e.g., in Google Drive) [00:00:38].
2.  **Text Extraction**: Text is extracted from the documents [00:00:44].
3.  **Vector Database Storage**: The extracted text is inserted into a vector database (e.g., Neon Postgres, Superbase, Quadrant) [00:00:46]. This allows efficient searching by [[building_ai_agents_with_n8n | AI agents]] [00:01:01].
4.  **Query and Lookup**: When a user asks a question, the [[building_ai_agents_with_n8n | AI agent]] uses a tool to perform a lookup in the vector database, retrieving relevant information to answer the question [00:01:05].

However, without additional strategies like [[contextual_retrieval_in_RAG | contextual retrieval]], this basic process can be inaccurate, often failing to retrieve necessary information [00:01:53].

## The Power of [[contextual_retrieval_in_RAG | Contextual Retrieval]]

[[contextual_retrieval_in_RAG | Contextual retrieval]] significantly improves [[enhancing_ai_agents_with_RAG_technology | RAG]] accuracy by helping the Large Language Model (LLM) better understand the retrieved information and its relation to the overall knowledge base [00:02:10].

### Evaluation Results
Anthropic's evaluations demonstrate the impact of [[contextual_retrieval_in_RAG | contextual retrieval]]:
*   **Basic [[enhancing_ai_agents_with_RAG_technology | RAG]]**: Has a failed retrieval rate of 9.9%, meaning it fails to retrieve proper chunks about 10% of the time [00:03:00].
*   **With Strategies Combined**: When [[contextual_retrieval_in_RAG | contextual retrieval]] and other strategies are combined, the failure rate drops to less than 3%, meaning 97% of the time, the [[enhancing_ai_agents_with_RAG_technology | RAG]] lookup retrieves the correct information [00:03:30].
*   **Focus on Contextual Embedding**: [[contextual_retrieval_in_RAG | Contextual embedding]] is highlighted as the most important strategy, forming the backbone for these improved metrics [00:04:09].

### How Contextual Embedding Works
[[contextual_retrieval_in_RAG | Contextual retrieval]] builds upon basic [[enhancing_ai_agents_with_RAG_technology | RAG]] by providing additional context to help the LLM understand what chunks represent and how they fit within the larger knowledge base [00:05:12].

The process is as follows:
1.  **Chunking**: Documents are first split into bite-sized pieces (chunks) [00:05:42].
2.  **Context Generation**: For every chunk, a prompt is run against an LLM. The prompt provides the *entire document* and the *current chunk*, asking the LLM to generate a short, succinct context that situates the chunk within the document [00:05:47]. This context helps the LLM understand the chunk's purpose and how it aids in answering user questions [00:06:13].
3.  **Context Prepending**: The generated extra context is prepended to the content of the chunk, typically separated by a triple dash [00:06:36].
4.  **Embedding**: These newly contextualized chunks are then embedded normally into vector representations [00:06:40].

This "zooming out" helps overcome a common limitation of basic [[enhancing_ai_agents_with_RAG_technology | RAG]], which can be too directed [00:05:24]. Even one or two sentences of added context can significantly improve results [00:06:26].

## Implementing [[contextual_retrieval_in_RAG | Contextual Retrieval]] in [[building_ai_agents_with_n8n | n8n]]

[[building_ai_agents_with_n8n | n8n]] offers a visual way to implement [[contextual_retrieval_in_RAG | contextual retrieval]], requiring only an extra LLM call compared to basic [[enhancing_ai_agents_with_RAG_technology | RAG]] [00:08:06].

### Workflow Steps in [[building_ai_agents_with_n8n | n8n]]
1.  **Google Drive Trigger**: Watches for new or updated files in a specified Google Drive folder [00:08:31]. It handles multiple files by looping through them [00:08:51].
2.  **Metadata Setting**: Sets important file metadata like ID, type, title, and URL [00:09:07].
3.  **Delete Existing Records**: Clears any previous records for the file in the database to ensure a clean slate, especially if the trigger was an "updated file" event [00:09:13].
4.  **Download File**: Downloads the file from Google Drive to extract its text [00:09:42].
5.  **Custom Chunking**: Instead of the default text splitter node, custom JavaScript code is used to chunk the document (e.g., every 400 characters with no overlap) [00:10:03]. This allows for the later addition of custom context [00:10:20].
6.  **Data Massaging**: The list of chunks is transformed into individual items within the [[building_ai_agents_with_n8n | n8n]] workflow [00:11:18].
7.  **LLM Call for Context**: Each chunk is sent to an LLM with the full document and a specific prompt to generate its context [00:11:43].
    *   **Cost Efficiency**:
        *   **Prompt Caching**: LLM providers like OpenAI (default enabled), Gemini, and Anthropic offer prompt caching, reducing the cost for repeating tokens in a prompt (e.g., the full document) [00:12:28]. OpenAI offers a 50% reduced cost, while Anthropic and Gemini offer ~90% [00:13:11].
        *   **Small, Cheap LLM**: A small and inexpensive LLM (e.g., GPT 4.1 Nano) can be used for this step, as significant reasoning power is not required [00:13:36].
8.  **Postgres Node (Data Loader)**:
    *   A custom chunk is created by prepending the LLM-generated context to the original chunk content, using a triple dash separator [00:14:53].
    *   Metadata (file ID, title, URL) is included so the LLM can cite its sources [00:15:16].
    *   The `character text splitter` node is present but configured with a large chunk size (e.g., 2000) to ensure it doesn't re-chunk the already processed data [00:15:27].
9.  **Embedding Model**: The `text embedding three small` OpenAI embedding model is used to create the vector representations of the contextualized chunks [00:15:53].

## Database Choice: Neon vs. Superbase

While Superbase is frequently covered, Neon is also an excellent choice for Postgress under the hood, offering interchangeability [00:16:30].

Key advantages of Neon:
*   **Serverless Postgress**: Provides autoscaling, meaning the database infrastructure adjusts to the load automatically, unlike platforms requiring manual instance size management [00:17:10].
*   **Database Branching**: Easily manage and test different database schema changes across environments (dev, test, prod) [00:17:32].
*   **MCP Server (AI Coding Assistance)**: Enables natural language management of the database for creating tables, managing records, and performing migrations [00:17:43].
*   **Strong Foundation**: Powers companies like Vzero, Replet, and Highkey, with a co-founder contributing to Postgress for over 20 years [00:18:07].

## [[building_ai_agents_with_n8n | AI Agent]] Implementation in [[building_ai_agents_with_n8n | n8n]]

The [[building_ai_agents_with_n8n | AI agent]] itself remains a basic [[enhancing_ai_agents_with_RAG_technology | RAG]] implementation, but it benefits significantly from the better-quality chunks produced by the [[contextual_retrieval_in_RAG | contextual retrieval]] pipeline [00:18:41].

Agent setup details:
*   **Chat Trigger**: Initiates the chat interface [00:18:57].
*   **AI Agent Node**: Uses a simple system prompt and an LLM (e.g., OpenAI) [00:19:01].
*   **Chat Memory**: Postgress is used for chat memory, similar to document storage [00:19:15].
*   **RAG Tool**:
    *   Uses the `Postgress retrieve documents tool`, referencing the `documents_pg` table where the contextualized chunks are stored [00:19:19].
    *   A description guides the agent on when and how to use the tool [00:19:33].
    *   Limits retrieval to a specified number of relevant chunks (e.g., four) [00:19:37].
    *   Includes metadata (title, URL) to enable source citation [00:19:46].
*   **Embedding Model**: Crucially, the *same* embedding model (e.g., `text embedding three small` OpenAI model) must be used by both the agent and the [[creating_rag_ai_agents_using_n8n | RAG pipeline]] [00:20:01].

## Implementing [[contextual_retrieval_in_RAG | Contextual Retrieval]] in Python

[[contextual_retrieval_in_RAG | Contextual retrieval]] can also be implemented in Python for [[prototyping_ai_agents_using_n8n | AI agents]] [00:23:14]. An example is provided in an open-source MCP (Master Control Program) server [00:24:19].

The Python implementation logic for generating contextual embeddings:
*   A function takes the full document and the current chunk as parameters [00:24:28].
*   It constructs the same prompt used in [[building_ai_agents_with_n8n | n8n]] [00:24:33].
*   An OpenAI call is made to generate the context [00:24:43].
*   The final string is built by concatenating the extra context, a triple dash separator, and the chunk itself [00:24:46].
*   This data is then added to the knowledge base (e.g., self-hosted Superbase running Postgress) [00:23:59].

## Further Enhancements

While [[contextual_retrieval_in_RAG | contextual embedding]] significantly improves [[enhancing_ai_agents_with_RAG_technology | RAG]], other strategies can further boost accuracy:
*   **BM25**: For hybrid [[enhancing_ai_agents_with_RAG_technology | RAG]] combining keyword search with semantic search [00:23:35].
*   **Re-ranking**: To refine the order of retrieved chunks [00:22:42].
*   **Query Expansion**: To generate multiple perspectives on a user's query [00:25:48].
*   **Agentic [[enhancing_ai_agents_with_RAG_technology | RAG]]**: Combining multiple strategies for a more powerful system [00:25:49].

These advanced strategies will continue to be explored to build even more accurate [[building_ai_agents_with_n8n | RAG agents]] [00:22:51].