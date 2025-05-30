---
title: Use of web scraping with LLMs
videoId: JWfNLF_g_V0
---

From: [[colemedin]] <br/> 

Large language models (LLMs) currently face significant challenges due to their knowledge being too general and limited, especially concerning new information because of training data cut-off dates <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance, asking an LLM like Claude about a new framework such as Pydantic AI would yield no information, and even web-searching LLMs provide only bare-bones details <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

To address this, Retrieval Augmented Generation (RAG) is a crucial approach <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. RAG involves giving external, curated knowledge to an LLM, transforming it into an expert on specific subjects like an AI agent framework, e-commerce store data, or other domain-specific information <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Challenges in Curating Knowledge for LLMs

The process of curating knowledge for RAG can be difficult and slow <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Ingesting an entire website into an LLM's knowledge base quickly is a significant hurdle, as traditional methods can be overly complicated, slow, and resource-intensive <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Introducing Crawl for AI

Crawl for AI is an open-source web crawling framework designed to scrape websites and format their output optimally for LLM comprehension <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. It aims to solve common problems associated with website scraping for LLMs <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Key Features and Advantages
*   **Efficiency**: Super intuitive, very fast, easy to set up, and extremely memory efficient <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **HTML to Markdown Conversion**: Converts raw, messy HTML into clean, human-readable Markdown format, which is much easier for LLMs to understand <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Pasting raw HTML into an LLM prompt can lead to hallucinations <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Advanced Handling**: Manages complex aspects like proxies and session management <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Content Filtering**: Automatically removes irrelevant content such as script tags and redundant information, ensuring the scraped data contains only what is valuable for ingestion into a knowledge base <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Open Source and Deployable**: Completely open source with a Docker deployment option <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Underlying Technology**: Uses Playwright, another open-source tool, for its web scraping functionality <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Getting Started with Crawl for AI
To begin using Crawl for AI, users simply need to install the Python package via `pip install` and run a setup command to install Playwright <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

#### Basic Scraping Example
A simple script can scrape a single page, like the homepage of Pydantic AI documentation, and output its content in Markdown within seconds <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This converted Markdown is ideal for an LLM to understand the page effectively <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Multi-URL Crawling for LLMs

To ingest an entire website, such as comprehensive documentation, it's necessary to efficiently extract and process multiple URLs <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Extracting URLs with Sitemap.xml
Manual copying of URLs is inefficient and not scalable <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. A common solution is to use a website's `sitemap.xml` file, typically found at `/sitemap.xml` on the homepage <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This XML provides the entire structure and all existing pages of a website <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Many websites, especially those built with platforms like Shopify or WordPress, have sitemaps for search engine optimization and crawlers <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

### Ethical Web Scraping Practices
Before scraping, it is crucial to check the website's `robots.txt` file, usually found at `/robots.txt` <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This file outlines the rules and disallowed pages for web scraping <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. For example, YouTube's `robots.txt` allows scraping for any agent but disallows certain pages, while GitHub requires contacting them before crawling <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. [[Ethical web scraping practices]] are essential for responsible data collection <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Efficient Multi-URL Processing
Directly looping through URLs and spinning up a new browser for each is highly inefficient <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. Crawl for AI offers solutions for more efficient processing:

*   **Sequential Processing with Same Browser Session**: Crawl for AI allows using the same browser session for all pages, significantly improving efficiency compared to opening a new browser for each URL <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This method can process many pages in seconds <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Parallel Processing**: For even greater speed, Crawl for AI supports parallel processing, enabling the simultaneous visitation of multiple pages while maintaining a single browser but creating different sessions for each <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. This allows for batch processing of URLs, such as 10 pages at a time <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
    *   This method is remarkably memory-efficient, using only around 119 megabytes of RAM even with a browser running in the background and processing multiple pages concurrently <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
    *   This efficiency is crucial for large-scale operations, like scraping thousands of product pages from an e-commerce store <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

## RAG AI Agent Example

An AI agent was built to be an expert on the Pydantic AI framework, using data curated by Crawl for AI <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. The process involved:
1.  Pulling all Pydantic AI documentation using Crawl for AI <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
2.  Storing this data in a vector database (specifically, PG Vector with Superbase) to form its knowledge base <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
3.  Building a full agent around this knowledge, with a Streamlit frontend <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

This agent can answer specific questions about Pydantic AI, such as supported models or code examples, providing accurate answers and even linking to relevant documentation pages, which general LLMs would typically be unable to do <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. This demonstrates how [[converting_website_data_to_llm_knowledge | converting website data to LLM knowledge]] can create highly specialized AI agents <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Conclusion

Crawl for AI provides a bulletproof and lightning-fast method to scrape any website and feed its data to an LLM as a knowledge base <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. This ability to integrate external website data into LLMs is invaluable for various use cases, making Crawl for AI a game-changer <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. While other methods exist for providing knowledge to LLMs, scraping data from sites into a knowledge base for RAG remains the most common way to make an AI agent an expert <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. [[Using web crawlers and databases in RAG]] significantly enhances LLM capabilities.