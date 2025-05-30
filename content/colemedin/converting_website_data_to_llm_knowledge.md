---
title: Converting website data to LLM knowledge
videoId: FQlCWrsUpHo
---

From: [[colemedin]] <br/> 

Effectively integrating diverse web data into Large Language Models (LLMs) is crucial for enhancing their capabilities, especially for RAG (Retrieval-Augmented Generation) AI agents <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This process allows LLMs to become experts on specific topics, e-commerce stores, or extensive documentation <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Crawl for AI: An Overview

Crawl for AI is an open-source tool designed to crawl almost any website and format its content for LLM knowledge bases <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Its popularity has grown significantly, evident from its 42,000 stars on GitHub <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Key Features and Benefits
*   **AI-Ready Output**: Crawl for AI produces webpage data in markdown format, which is optimal for LLMs to understand pages and extract distinct sections <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Speed and Efficiency**: It is "blazing fast" in scraping the internet and creating knowledge for LLMs <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This speed is attributed to its ability to crawl batches of URLs in parallel <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Applications**: Projects like Context 7 likely use tools like Crawl for AI to constantly scrape up-to-date documentation for AI coding assistants <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. It is also used in Archon, an open-source AI agent builder <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Installation and Basic Usage
Setting up Crawl for AI is straightforward:
1.  Ensure Python is installed <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
2.  Install Crawl for AI via pip: `pip install crawl-for-ai` <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
3.  Run the setup command to install the Playwright browser, enabling the terminal to scrape pages <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

A basic example involves creating an instance of `async web crawler` and providing a URL, such as the Pydantic AI documentation, to scrape it into an LLM-understandable markdown format <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This process transforms raw HTML into structured markdown with headings and subheadings, which is easier for agents and LLMs to parse <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Strategies for Crawling Entire Websites

Crawl for AI offers three main strategies for [[use_of_web_scraping_with_llms | scraping website data]] to create [[using_knowledge_bases_to_enhance_language_models | knowledge bases for LLMs]]:

### 1. Sitemap (sitemap.xml)
Many websites provide a sitemap, typically accessible at `[root_domain]/sitemap.xml` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This structured document lists all available URLs, providing a direct way to access web pages within a site <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This is the primary method for gathering all accessible web pages if available <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### 2. Recursive Scraping via Navigation
When a sitemap is not available, Crawl for AI can start from a homepage and discover other pages through navigation <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This involves "recursive scraping," where the tool traverses pages, finds links, and continues to visit them <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Users can specify the depth of this recursion, determining how many levels deep the crawler should go <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. The crawler identifies "internal links" (links with the same domain) to navigate the website comprehensively <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>. This method dynamically builds a sitemap over time <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

### 3. LLMs.ext Files
Some documentation for frameworks and tools provide an `LLMs.ext` file (e.g., `/llms.ext` or `/llms-full.ext`) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This single page consolidates all documentation into one large markdown document, specifically formatted for LLM knowledge <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This makes it easy to ingest, chunk, and add to a vector database for RAG <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Implementation with Crawl for AI

A dedicated GitHub repository serves as a free resource with examples demonstrating these crawling strategies <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### Crawling Methods
*   **Single Page Crawl**: The most basic use case, demonstrated by scraping the Pydantic AI documentation <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Sequential vs. Parallel Crawling**: While sequential processing is possible (one URL at a time) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, Crawl for AI excels at parallel crawling, processing batches of URLs concurrently for speed <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   For sitemaps, `crawl parallel` function is used, leveraging `A run mini` to get markdown from many pages simultaneously <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
    *   For `LLM.ext` files, the simpler `AUN` function is used as it's a single page <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.
    *   For recursive crawling, `crawl recursive batch` is used with a list of start URLs, dynamically identifying and scraping internal links to build a comprehensive knowledge base <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

### Chunking Strategies
When dealing with large documents like `LLM.ext` files, chunking is essential before feeding data to an LLM <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Markdown documents, with their structured headings and subheadings, allow for effective chunking based on headers, ensuring distinct sections are kept together while preserving contextual information <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

## Demonstration of an AI Agent with Crawled Data

A demonstration showcases an AI agent built with Pydantic AI and using Chroma DB as its local vector database, leveraging data crawled by Crawl for AI <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.

### Knowledge Ingestion Process
The `insert docs` function intelligently determines the URL type (sitemap, LLM.ext, or regular web page) and applies the appropriate crawling strategy <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   **Sitemap Example**: Crawling the Crawl for AI sitemap, it fetched URLs in batches (e.g., 5 at a time) and created 457 chunks inserted into Chroma DB <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The scraping process itself is "blazing fast," often faster than inserting into the database <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
*   **Regular Web Page Example**: Crawling the Pydantic AI documentation as a regular web page involves starting from the homepage, checking navigation, and recursively finding internal links <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. This process resulted in 2,420 chunks inserted into Chroma DB <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **LLM.ext Example**: Crawling the LangGraph `LLMs.ext` file involved pulling a single page, splitting it into 788 chunks, and quickly inserting them into Chroma DB <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

### Agent Querying
After ingesting data, the agent can be queried through a Streamlit interface <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. It successfully answers questions based on the ingested documentation for Pydantic AI, Crawl for AI, and LangGraph, demonstrating its ability to retrieve relevant information from its [[using_knowledge_bases_to_enhance_language_models | knowledge base]] <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. For topics not covered in the crawled documentation (e.g., Superbase), the agent confirms it lacks access to that information <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.