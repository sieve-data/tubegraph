---
title: Improving RAG accuracy with additional strategies
videoId: z_LGan-t2Mo
---

From: [[colemedin]] <br/> 

Retrieval Augmented Generation (RAG) is a crucial strategy for equipping AI agents with external knowledge, such as documents, effectively <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While basic RAG provides a way to incorporate external information into AI agents, it often suffers from inaccuracies <a class="yt-timestamp" data-t="01:51:53">[01:51:53]</a>. Strategies beyond basic RAG are essential for building reliable AI agents that can leverage documents effectively <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Limitations of Basic RAG Systems
A common issue with basic RAG is its inaccuracy, often failing to retrieve the necessary information from the knowledge base to answer questions effectively <a class="yt-timestamp" data-t="02:00:03">[02:00:03]</a>. This means the Large Language Model (LLM) may not fully understand the retrieved information or how it relates to the broader knowledge base <a class="yt-timestamp" data-t="02:10:59">[02:10:59]</a>. For instance, basic RAG can have a failed retrieval rate of 9.9%, meaning about 10% of the time it doesn't retrieve the proper chunks to aid the agent in answering a question correctly <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

## Enhancing RAG AI Agent Accuracy with Contextual Retrieval

One significant strategy to [[improving_rag_ai_agent_accuracy | improve RAG accuracy]] is **Contextual Retrieval**, introduced by Anthropic <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This technique significantly reduces failure rates for RAG, bringing them down to less than 3% when combined with other strategies <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. Specifically, contextual embedding, a core component of contextual retrieval, can reduce RAG failure rates by up to 35% <a class="yt-timestamp" data-t="04:09:11">[04:09:11]</a>.

### How Contextual Retrieval Works
Contextual retrieval builds upon the basic RAG process by providing additional context to help the LLM understand what retrieved chunks represent and how they fit within the larger knowledge base <a class="yt-timestamp" data-t="05:10:12">[05:10:12]</a>.

The process involves:
1.  **Chunking Documents**: Documents are split into bite-sized pieces of information <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
2.  **Generating Contextual Embeddings**: For each chunk, a prompt is run against an LLM, providing the entire original document and the current chunk being processed <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. The LLM is asked to provide a short, succinct context that situates the chunk, describing where it fits within the document or a brief overview <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>. This extra context (even just one or two sentences) significantly improves results <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>.
3.  **Prepending Context**: This generated context is then prepended to the content of the chunk, often separated by a distinct delimiter (e.g., "---") <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>.
4.  **Embedding**: The combined text (context + chunk content) is then embedded normally into vector representations for storage in a vector database <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.

When the LLM retrieves a record, it now has both the additional context and the chunk content, making the entire process more accurate <a class="yt-timestamp" data-t="16:19:00">[16:19:00]</a>.

### Cost Considerations
While sending the entire document for each chunk might seem expensive, it is mitigated by:
*   **Prompt Caching**: Most LLM providers (like OpenAI, Gemini, Anthropic) offer prompt caching, where repeating tokens in a prompt come at a reduced cost (e.g., 50% for OpenAI, 90% for Anthropic/Gemini) <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.
*   **Cheaper LLMs**: A small, inexpensive LLM (e.g., GPT-4.1 Nano) can be used for generating the contextual sentences, as it does not require significant reasoning power <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.

### Implementation Example (N8N)
A practical example of [[rag_ai_agent_development | RAG AI agent development]] with contextual embedding in N8N involves:
1.  **Google Drive Trigger**: Watching for new or updated files in Google Drive <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
2.  **File Processing Loop**: Handling multiple files, setting metadata (ID, type, title, URL), and deleting existing records for updated files to ensure a clean slate <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.
3.  **Text Extraction**: Downloading files and extracting text <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.
4.  **Custom Chunking**: Instead of standard text splitters, custom JavaScript code splits the document (e.g., every 400 characters with no overlap), allowing for custom information to be added to each chunk <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.
5.  **LLM Call for Context**: An LLM (e.g., OpenAI's smallest model) is called for each chunk, using the full document and the current chunk to generate the contextual text <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
6.  **Data Loading**: The generated context is prepended to the chunk content with a separator, and then this combined text, along with metadata (file ID, title, URL), is loaded into a vector database <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.
7.  **Embedding Model**: An embedding model (e.g., `text-embedding-3-small` from OpenAI) creates the vector representations <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>. It's crucial to use the same embedding model for both the pipeline and the AI agent's lookups <a class="yt-timestamp" data-t="20:01:00">[20:01:01]</a>.

The AI agent then uses a simple tool to search the knowledge base, where the retrieved chunks are now enhanced with the prepended contextual information, making them more useful <a class="yt-timestamp" data-t="18:41:00">[18:41:00]</a>.

### Database Considerations
For storing vector embeddings, databases like Neon Postgress or Supabase are suitable as they both run Postgress under the hood <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. Neon, for example, offers serverless Postgress with autoscaling, database branching, and an AI coding assistance feature that allows natural language management of the database <a class="yt-timestamp" data-t="17:10:00">[17:10:00]</a>.

### Python Implementation
Contextual retrieval can also be implemented in Python. An example includes generating contextual embeddings by passing the full document and chunk to an LLM, then prepending the generated context with a separator to the chunk content <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>. This code is open-source and can be used as an example for [[enhancing_ai_agents_with_rag_technology | enhancing AI agents with RAG technology]] <a class="yt-timestamp" data-t="24:19:00">[24:19:00]</a>.

## Beyond Contextual Retrieval
While contextual retrieval is a powerful [[advanced_rag_implementation_techniques | advanced RAG implementation technique]], other strategies can further [[improving_rag_ai_agent_accuracy | improve RAG accuracy]]:
*   **Hybrid RAG (BM25)**: Combining keyword search (BM25) with semantic search <a class="yt-timestamp" data-t="22:35:00">[22:35:00]</a>.
*   **Re-ranking**: Re-ordering retrieved documents based on relevance <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>.
*   **Query Expansion**: Rewriting or expanding the user's query to improve retrieval <a class="yt-timestamp" data-t="25:46:00">[25:46:00]</a>.
*   **[[Agentic RAG strategy and implementation | Agentic RAG]]**: Creating a more powerful system by combining multiple strategies <a class="yt-timestamp" data-t="25:48:00">[25:48:00]</a>. This is part of the broader discussion on [[agentic_rag_advantages_and_future_applications | Agentic RAG advantages and future applications]].

These advanced methods build upon foundational techniques like contextual retrieval to create even more accurate and robust RAG systems.