---
title: Strategies for website crawling
videoId: FQlCWrsUpHo
---

From: [[colemedin]] <br/> 

[[introduction_to_crawl_for_ai | Crawl for AI]] is an open-source tool designed to crawl websites and format content for [[use_of_web_scraping_with_LLMs | LLM knowledge]], particularly for [[using_web_crawlers_and_databases_in_rag | RAG]] AI agents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It has gained significant popularity, with its GitHub repository having 42,000 stars, indicating its effectiveness in scraping the internet to create knowledge for [[use_of_web_scraping_with_LLMs | LLMs]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

[[crawl_for_ai_web_crawling_framework | Crawl for AI]] is noted for its blazing speed and ability to produce AI-ready webpage data in markdown format, which is optimal for [[use_of_web_scraping_with_LLMs | LLMs]] to understand and extract distinct sections <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This tool is leveraged by projects like [[opensource_crawl_for_ai_rag_mcp_server | Context 7]] for continuously updated documentation for AI coding assistants <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

To install [[crawl_for_ai_web_crawling_framework | Crawl for AI]], users need Python installed, then can `pip install crawl-for-ai`, and run a setup command to install the Playwright browser, enabling the terminal to scrape pages <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Core Website Crawling Strategies

There are three primary strategies for crawling websites using [[crawl_for_ai_web_crawling_framework | Crawl for AI]] to gather [[use_of_web_scraping_with_LLMs | LLM knowledge]] <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>:

### 1. Leveraging Sitemaps
Many websites provide a sitemap, typically accessible at `/sitemap.xml`, which is a structured document listing all available URLs <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. This is the most convenient method for accessing all web pages on a given website <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. [[crawl_for_ai_web_crawling_framework | Crawl for AI]] can take batches of these URLs and extract markdown in [[parallel_processing_and_efficiency_in_web_crawling | parallel]] <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### 2. Recursive Website Crawling
When a sitemap is not available, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] can start from a homepage and recursively find other pages through navigation <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This involves traversing links found on pages, focusing on "internal links" (links within the same domain) <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>. Users can specify a "depth" to control how many levels deep the crawler goes <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. This method dynamically builds a sitemap over time <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

### 3. The LLM.ext Format
Some frameworks and tools provide an `LLMs.ext` (or `llms-full.ext`) file, which combines all their documentation into a single page specifically formatted for [[use_of_web_scraping_with_LLMs | LLM knowledge]] in markdown <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This format is ideal for direct ingestion into a program for chunking and adding to a vector database for [[using_web_crawlers_and_databases_in_rag | RAG]] <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Practical Implementation and Examples

A free GitHub repository is provided as a resource, containing code examples for each strategy <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

*   **Crawling a Single Page**: A basic example demonstrates scraping a single URL and transforming its HTML into markdown format for better [[use_of_web_scraping_with_LLMs | LLM]] comprehension <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Crawling in [[parallel_processing_and_efficiency_in_web_crawling | Parallel]]**: [[crawl_for_ai_web_crawling_framework | Crawl for AI]] excels at processing batches of URLs concurrently, making it blazingly fast <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This is achieved using the `A_run_many` function for multiple URLs simultaneously <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Chunking Strategies**: For larger documents, especially `LLMs.ext` files, chunking strategies are important to split the content into manageable pieces for [[use_of_web_scraping_with_LLMs | LLMs]] <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Strategies can include splitting based on markdown headers and subsections <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

## Building a [[using_web_crawlers_and_databases_in_rag | RAG]] Agent with Crawled Data

The GitHub repository also includes an AI agent that combines all three crawling strategies <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. This agent intelligently determines whether a given URL is a sitemap, an `LLM.ext` file, or a regular webpage, and applies the appropriate crawling strategy <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

The agent uses a [[using_web_crawlers_and_databases_in_rag | RAG]] approach with [[use_of_web_scraping_with_LLMs | Pydantic AI]] and Chroma DB as its local vector database <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. After crawling, the extracted markdown is chunked and inserted into the Chroma DB, enabling the agent to search and retrieve knowledge from the scraped websites <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

Demonstrations show that the scraping process with [[crawl_for_ai_web_crawling_framework | Crawl for AI]] is extremely fast, often taking less time than inserting the chunks into the vector database <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. The agent can then answer questions based on the ingested documentation, for example, verifying access to documentation for [[use_of_web_scraping_with_LLMs | Pydantic AI]], [[crawl_for_ai_web_crawling_framework | Crawl for AI]], or LangGraph <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

### Future [[using_web_crawlers_and_databases_in_rag | RAG]] Content

Future content will cover advanced [[using_web_crawlers_and_databases_in_rag | RAG]] strategies such as hierarchical [[using_web_crawlers_and_databases_in_rag | RAG]], contextual retrieval, query expansion, and re-ranking, which complement the web crawling capabilities of [[crawl_for_ai_web_crawling_framework | Crawl for AI]] <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.