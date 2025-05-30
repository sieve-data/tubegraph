---
title: Introduction to Crawl for AI
videoId: JWfNLF_g_V0
---

From: [[colemedin]] <br/> 

Large Language Models (LLMs) currently face significant challenges due to their general and limited knowledge, especially concerning new information not present in their training data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance, an LLM like Claude has no knowledge of new frameworks such as Pydantic AI <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Even LLMs with web search capabilities often provide only "bare bones" information <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

To address this, Retrieval Augmented Generation (RAG) is employed, which involves providing external, curated knowledge to an LLM to make it an expert in a specific domain <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. However, the curation step, especially ingesting an entire website into a knowledge base, can be difficult and slow <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This is where [[crawl_for_ai_web_crawling_framework | Crawl for AI]] becomes a crucial solution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## What is [[crawl_for_ai_web_crawling_framework | Crawl for AI]]?

[[crawl_for_ai_web_crawling_framework | Crawl for AI]] is an [[opensource_crawl_for_ai_rag_mcp_server | open-source web crawling framework]] specifically designed to scrape websites and format the output in an optimal way for LLMs to understand <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Unlike typical website scraping systems that can be slow, overly complicated, and resource-intensive, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] is noted for being <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>:
*   Super intuitive <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>
*   Very fast <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
*   Easy to set up <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>
*   Extremely memory efficient <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>

The core purpose of [[crawl_for_ai_web_crawling_framework | Crawl for AI]] is to transform the messy, raw HTML extracted from websites into a clean, human-readable, and LLM-understandable Markdown format <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This conversion is crucial because if raw HTML is difficult for humans to understand, it's even harder for an LLM <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Key Capabilities

[[crawl_for_ai_web_crawling_framework | Crawl for AI]] handles several complex aspects of web scraping under the hood <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>:
*   **Proxy and Session Management:** It manages these difficult tasks automatically <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Irrelevant Content Removal:** It intelligently removes elements like script tags and redundant information that are not useful for LLMs, ensuring that the extracted content is focused on what matters for the knowledge base <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Docker Deployment:** [[crawl_for_ai_web_crawling_framework | Crawl for AI]] is also available via Docker for easy deployment <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Getting Started with [[crawl_for_ai_web_crawling_framework | Crawl for AI]]

Getting started is straightforward. It involves installing the Python package and then running a setup command <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Installation:** `pip install` the Python package <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Setup:** Run a setup command to install Playwright, the underlying tool [[crawl_for_ai_web_crawling_framework | Crawl for AI]] uses to scrape websites by running a browser in the background <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Playwright is an open-source tool also used for web application testing <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

A basic script to scrape a single page is very simple and can extract an entire page's content in Markdown format within seconds <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This Markdown output is significantly better for an LLM compared to raw HTML, which often leads to hallucinations <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Advanced Usage: Multi-URL Crawling

To make [[crawl_for_ai_web_crawling_framework | Crawl for AI]] truly useful for LLMs, it's necessary to ingest multiple pages, such as an entire website's documentation <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Manually copying URLs is inefficient and not scalable <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### Leveraging Sitemaps for URL Extraction

A highly efficient solution is to use a website's sitemap. Most websites provide a sitemap, typically accessible at `/sitemap.xml`, which outlines the entire structure and all pages of the site <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This is common practice for Search Engine Optimization (SEO) and to facilitate crawlers <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### Ethical Web Scraping with `robots.txt`

Before scraping any website, it's essential to consider ethical guidelines <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Websites often have a `robots.txt` file (e.g., `youtube.com/robots.txt`) which specifies rules for web scraping, indicating which agents are allowed and which pages are disallowed <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Adhering to these rules is highly recommended <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Efficient Multi-URL Crawling

[[crawl_for_ai_web_crawling_framework | Crawl for AI]] offers efficient methods for crawling multiple URLs <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>:

1.  **Sequential Crawling with Same Browser Session:** Instead of spinning up a new browser for each URL, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] allows using the same browser session for all pages, significantly improving efficiency <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. This method can process many pages in seconds <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

2.  **Parallel Processing:** To achieve even greater speed, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] supports parallel processing, allowing it to visit multiple pages simultaneously and pull their Markdown content <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. This involves using a single browser but creating different sessions that operate in parallel <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. For example, it can process pages in batches (e.g., 10 pages at a time) <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This method is also remarkably memory efficient, with peak RAM usage remaining very low (e.g., 119 megabytes) even when a browser is running and visiting multiple pages concurrently <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

These efficiencies are vital, especially for large datasets like e-commerce stores with hundreds or thousands of products, where sequential processing would be a significant drag <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

## Integration with RAG AI Agents

The ability to quickly and efficiently scrape data makes [[crawl_for_ai_web_crawling_framework | Crawl for AI]] perfect for RAG <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The scraped Markdown content is ready to be placed in a vector database for use with an LLM <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

For example, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] can be used to curate the documentation for a framework like Pydantic AI. This curated knowledge can then be integrated into an [[building_ai_agents | AI agent]] to make it an expert on the framework <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. Such an agent can answer specific questions that a general LLM would not know, and even provide links to the source documentation for reference <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

While other methods exist for providing knowledge to LLMs (manual curation, advanced concepts like KAG), scraping data from a site and providing it to a knowledge base for RAG remains the most common way to make an [[understanding_ai_agents | AI agent]] an expert in a specific area <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.

> [!NOTE]
> The full code for a [[building_a_nocode_rag_ai_agent | RAG AI agent]] built using [[crawl_for_ai_web_crawling_framework | Crawl for AI]] is available in a GitHub repository. It includes the crawling process, insertion into a vector database (e.g., PG Vector with Supabase), and a Streamlit interface for the Pydantic AI agent <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. A detailed guide on [[step_by_step_process_for_building_ai_agents | building AI agents]] like this is covered in subsequent videos <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>, <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

## Conclusion

[[crawl_for_ai_web_crawling_framework | Crawl for AI]] provides a "bulletproof, lightning-fast way to scrape any site and give it to your LLM as a knowledge base" <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. Its efficiency and specialized formatting for LLMs make it a "game changer" for integrating external web data into LLMs, regardless of the use case <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.