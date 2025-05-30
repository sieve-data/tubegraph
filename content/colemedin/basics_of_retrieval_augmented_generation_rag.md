---
title: Basics of retrieval augmented generation RAG
videoId: z_LGan-t2Mo
---

From: [[colemedin]] <br/> 

[[introduction_to_retrieval_augmented_generation_rag | Retrieval Augmented Generation (RAG)]] is a critical strategy for making [[retrieval_augmented_generation_for_ai | AI]] more accurate by enabling models to leverage external knowledge sources <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It is a go-to method for integrating external knowledge into [[retrieval_augmented_generation_rag_in_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## How Basic RAG Works

Basic [[retrieval_augmented_generation | RAG]] involves several key steps to provide external information to [[retrieval_augmented_generation_rag_in_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>:

1.  **Document Corpus**: The process begins with a collection of documents, such as files in Google Drive <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  **Text Extraction**: Text is extracted from these documents <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
3.  **Chunking**: Documents are split into smaller, bite-sized pieces of information called "chunks" to avoid overwhelming the Large Language Model (LLM) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
4.  **Embedding**: An embedding model, such as OpenAI's, is used to create vector representations (embeddings) of these chunks <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
5.  **Vector Database Storage**: These vector representations are then stored in a vector database like Neon Postgres, Supabase, or Qdrant <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This allows the information to be searched efficiently by [[retrieval_augmented_generation_rag_in_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

When a user query is received, it is also embedded <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. This embedded query is then used to match against the vector database to find the most relevant chunks to help the [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] answer the question <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Limitations of Basic RAG

Despite its utility, basic [[retrieval_augmented_generation | RAG]] without additional strategies can be inaccurate <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A significant problem is that it often fails to retrieve the necessary information from the knowledge base to answer a question effectively <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. For example, regular [[retrieval_augmented_generation | RAG]] can have a failed retrieval rate of approximately 9.9% of the time, meaning it doesn't retrieve the proper chunks to aid the agent <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This highlights the need for [[advanced_rag_implementation_techniques | advanced RAG implementation techniques]] to improve accuracy <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

One such strategy, [[Contextual retrieval in RAG | contextual retrieval]], helps the LLM better understand the retrieved information and how it relates to the broader knowledge base, addressing the issue of [[retrieval_augmented_generation_rag_and_its_challenges | RAG's challenges]] with providing a zoomed-out view of the context <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.