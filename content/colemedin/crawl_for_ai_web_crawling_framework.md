---
title: Crawl for AI web crawling framework
videoId: mDikQrVRmtU
---

From: [[colemedin]] <br/> 

[[introduction_to_crawl_for_ai | Crawl for AI]] is an [[opensource_crawl_for_ai_rag_mcp_server | open-source]] web crawling framework designed to address the limitations of Large Language Models (LLMs) regarding specific and current information <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## The Challenge of LLM Knowledge Limitations
Large Language Models often have knowledge that is too general and limited, especially concerning new information due to their training cut-off dates <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. For example, an LLM might not know about recent [[frameworks_and_tools_for_ai_agent_development | AI agent frameworks]] like Pydantic AI <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Even LLMs that can search the web may only provide very basic information <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Retrieval Augmented Generation (RAG)
Retrieval Augmented Generation (RAG) is a method to provide external, curated knowledge to an LLM, transforming it into an expert on a specific topic <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This external knowledge could be about an [[understanding_ai_agent_frameworks | AI agent framework]], an e-commerce store, or other domain-specific information <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. However, the process of curating this external knowledge can be challenging and time-consuming <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Crawl for AI Solution
[[introduction_to_crawl_for_ai | Crawl for AI]] addresses the difficulty of the knowledge curation step in RAG <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Its primary function is to [[strategies_for_website_crawling | scrape websites]] and format the extracted data in a way that is optimally understood by LLMs <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This allows for the efficient collection and structuring of specific documentation or information into a knowledge base for an LLM <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Capabilities and Use Cases
[[crawl_for_ai_tool_features_and_functionality | Crawl for AI's features]] include:
*   Scraping websites <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   Formatting output for LLM comprehension <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   Enabling the creation of expert AI agents by curating specific framework knowledge, such as Pydantic AI documentation <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   The framework can be adapted to curate information from any website <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

[[using_web_crawlers_and_databases_in_rag | Using web crawlers and databases in RAG]] with [[introduction_to_crawl_for_ai | Crawl for AI]] ensures that LLMs can provide spot-on answers to specific questions once their knowledge base is augmented with curated information <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.