---
title: Choosing large language models for n8n
videoId: Nsu9BzQv5C4
---

From: [[colemedin]] <br/> 

When [[building_ai_agents_using_n8n | AI agents]] and [[creating_powerful_ai_workflows_with_n8n | workflows]] within n8n, a common question arises regarding the choice of [[reasoning_large_language_models_and_their_impact | large language models]] (LLMs). The optimal choice largely depends on the specific use case <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. However, some general recommendations can help users get started quickly <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Chat Models

For chat models, n8n offers various options <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:

*   **Absolute Best**: For the highest performance currently, Anthropic's Claude 3.5 Sonnet is recommended <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Fastest**: If speed is the primary concern and extreme power isn't necessary, Groq's Llama models are a good choice <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Affordable & Strong**: For a very cost-effective yet capable model, OpenAI's GPT-4o mini is suggested <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Embedding Models for RAG

For [[creating_rag_ai_agents_using_n8n | RAG]] (Retrieval Augmented Generation) purposes, the embedding model plays a crucial role <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>:

*   **Recommendation**: OpenAI's `text-embedding-3-small` model is highly recommended for embeddings <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Processing RAG Chunks

The model used to process the chunks retrieved by [[creating_rag_ai_agents_using_n8n | RAG]] should generally be the same as the chat model selected for the workflow <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

More content on n8n, including its use for [[working_with_local_large_language_models | local AI projects]], will be released soon <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.