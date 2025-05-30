---
title: Pantic AI framework
videoId: mDikQrVRmtU
---

From: [[colemedin]] <br/> 

[[pantic_ai_features_and_implementation | Pantic AI]] is described as a "new shiny framework" for [[building_ai_agents_with_pantic_ai_and_mcp | building AI agents]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Challenges with Large Language Models (LLMs)

One of the significant challenges with LLMs is their generally broad and limited knowledge, especially concerning new information due to training cut-off dates <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance, if asked about [[pantic_ai_features_and_implementation | Pantic AI]], LLMs like Claude currently have "no clue" <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Even LLMs capable of web searches provide "very Bare Bones" information <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Enhancing LLM Knowledge with Retrieval Augmented Generation (RAG)

To overcome the knowledge limitations, a method called Retrieval Augmented Generation (RAG) is used <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. RAG involves providing external, curated knowledge to an LLM, essentially making it an expert on specific topics <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

For example, by taking all the framework documentation for [[pantic_ai_features_and_implementation | Pantic AI]] and placing it in a knowledge base for an LLM, subsequent queries about [[pantic_ai_features_and_implementation | Pantic AI]] yield "spot on" answers <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This allows the LLM to become an expert on subjects it wasn't previously familiar with, such as an [[understanding_ai_agent_frameworks | AI agent framework]] like [[pantic_ai_features_and_implementation | Pantic AI]], or an e-commerce store <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Curating Knowledge for RAG

The process of curating knowledge for RAG can be difficult and slow <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Crawl for AI, an open-source web crawling framework, addresses this by specifically designing its output to be optimally formatted for LLM comprehension <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Practical Application

A RAG [[building_ai_agents_with_pantic_ai_and_mcp | AI agent]] can be built to specialize in the [[pantic_ai_features_and_implementation | Pantic AI]] framework <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This involves using Crawl for AI to gather all the necessary framework knowledge and integrate it into the agent's knowledge base <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This approach can be applied to any website to create a specialized knowledge agent <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.