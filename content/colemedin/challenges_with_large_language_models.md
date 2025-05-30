---
title: Challenges with large language models
videoId: mDikQrVRmtU
---

From: [[colemedin]] <br/> 

One of the significant challenges currently faced with [[limitations_of_large_language_models | large language models]] (LLMs) is that their knowledge is often too general <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Their information base is limited for new topics due to a training cut-off date <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

For instance, an LLM like Claude might not know about a new framework such as Pydantic AI, even if it's a recent development for building [[ai_agents_and_large_language_models | AI agents]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Even LLMs capable of searching the web may only provide very basic information about new topics <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Retrieval Augmented Generation (RAG) as a Solution

To address the limitations of [[reasoning_large_language_models_and_their_impact | large language models]] regarding specific or new knowledge, Retrieval Augmented Generation (RAG) is a widely discussed method <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

RAG involves providing external, curated knowledge to an LLM <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This process transforms the LLM into an expert on subjects it wasn't previously trained on, such as specific [[ai_agents_and_large_language_models | AI agent]] frameworks, e-commerce stores, or other specialized domains <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, if Pydantic AI framework documentation is used to create a knowledge base for an LLM, the LLM can provide accurate and detailed answers about it <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Challenge in RAG: The Curation Step

Despite its benefits, the "curate" step in RAG can be very difficult and slow <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### Crawl for AI: A Tool for Data Curation

Crawl for AI is an open-source web crawling framework designed to scrape websites and format the output optimally for LLMs to understand <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This tool simplifies the curation process for RAG applications.

A practical application of Crawl for AI is demonstrated by building a RAG [[ai_agents_and_large_language_models | AI agent]] that specializes in the Pydantic AI framework. This is achieved by using Crawl for AI to gather and curate the framework's knowledge into a dedicated knowledge base for the LLM <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The approach taken with Crawl for AI can be applied to curate knowledge from any website <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.