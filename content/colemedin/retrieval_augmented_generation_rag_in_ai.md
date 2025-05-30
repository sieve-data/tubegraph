---
title: Retrieval augmented generation RAG in AI
videoId: JWfNLF_g_V0
---

From: [[colemedin]] <br/> 

## Introduction to RAG

Large Language Models (LLMs) currently face significant challenges due to their general and limited knowledge, especially concerning new information not present in their training data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For instance, an LLM like Claude may not recognize a newer framework like Pydantic AI <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Even LLMs capable of web searches may return only basic information <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

[[retrieval_augmented_generation | Retrieval Augmented Generation (RAG)]] addresses this by allowing external, curated knowledge to be fed into an LLM <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This method transforms a general LLM into an expert on specific topics, such as an AI agent framework or an e-commerce store <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. By providing Pydantic AI's framework documentation to an LLM, it can give accurate answers to specific questions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Challenges in RAG Data Curation

A significant hurdle in [[retrieval_augmented_generation | RAG]] is the process of curating external knowledge, which can be difficult and slow <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Ingesting an entire website into an LLM's knowledge base efficiently poses a challenge <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Crawl for AI: A Solution for Data Ingestion

Crawl for AI is an open-source web crawling framework designed to scrape websites and format the output optimally for LLM comprehension <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. It tackles common issues with traditional website scraping systems, which are often slow, overly complicated, and resource-intensive <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Key Features of Crawl for AI

Crawl for AI offers several advantages:
*   **Intuitive and Fast**: It is super intuitive, very fast, and easy to set up <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Memory Efficient**: It is extremely memory efficient <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, using only a peak of 119 megabytes of memory even when visiting multiple pages concurrently <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   **HTML to Markdown Conversion**: Raw HTML is difficult for humans and LLMs to understand <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Crawl for AI converts this "ugly HTML" into a clean, human-readable Markdown format that LLMs can better process for [[retrieval_augmented_generation | RAG]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Handles Complexities**: It manages underlying complexities like proxies and session management <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Removes Irrelevant Content**: It automatically removes redundant or useless information such as script tags and other unhelpful data, ensuring the output contains only valuable content for the knowledge base <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Open-Source and Deployable**: Crawl for AI is completely open-source and easy to deploy, with Docker options available <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Getting Started with Crawl for AI

To begin using Crawl for AI, you can install the Python package via `pip install` and run a setup command to install Playwright, the underlying tool used for web scraping <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. A simple script can scrape a single page and output its markdown in seconds <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This provides a significantly cleaner and more understandable format for LLMs compared to raw HTML <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### Multi-URL Crawling for Comprehensive Knowledge Bases

For a truly useful LLM knowledge base, it's necessary to ingest multiple pages from a documentation site or an entire e-commerce store <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

#### Efficient URL Extraction with Sitemaps

Manually copying URLs is inefficient and not scalable <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. A robust solution is to use a website's sitemap, typically found at `/sitemap.xml` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This XML file provides the entire structure of the website and lists all existing pages <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Many websites, especially those built with platforms like Shopify or WordPress, include sitemaps for search engine optimization and crawlers <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

#### Ethical Web Scraping

Before scraping any website, it is crucial to check its `robots.txt` file, usually located at `/robots.txt` <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This file specifies the rules for web scraping, indicating which agents are allowed to scrape and which pages are disallowed <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Some websites, like GitHub, may require contact before crawling <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Adhering to these rules is vital for ethical web scraping <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

#### Optimized Multi-URL Processing

Sequentially processing each URL by spinning up a new browser session is inefficient <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. Crawl for AI provides solutions for efficient multi-URL crawling:
*   **Same Browser Session**: It allows reusing the same browser session for all pages, significantly improving efficiency <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Even processing dozens of pages sequentially with this method can take only seconds <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **Parallel Processing**: For even greater speed, Crawl for AI supports parallel processing, visiting multiple pages concurrently within the same browser <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. For example, it can process batches of 10 pages simultaneously, retrieving their markdown and combining the results <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This is especially useful for large sites like e-commerce stores with hundreds or thousands of products <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

## Example: Pydantic AI Expert Agent

Using Crawl for AI, it is possible to build a full [[retrieval_augmented_generation_rag_in_ai_agents | RAG AI agent]] that acts as an expert on a specific framework, such as Pydantic AI <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. By pulling all Pydantic AI documentation, putting it into a vector database for its knowledge base, and building an agent around it with a front end, the agent can answer specific queries and even provide links to relevant documentation pages <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. For example, it can accurately answer questions about supported models or provide complex code examples, such as a weather agent example, much faster and more reliably than a general LLM <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. This agent utilizes PG Vector with Supabase for the vector database <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

## Importance of Crawl for AI in RAG

Crawl for AI is considered a "game-changer" for its ability to rapidly and reliably scrape any website for LLM knowledge bases <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. While other methods exist for providing knowledge to LLMs, such as manual curation or advanced concepts like KAG, scraping data from sites and providing it to a knowledge base for [[retrieval_augmented_generation | RAG]] remains the most common way to make an [[enhancing_ai_agents_with_rag_technology | AI agent]] an expert in a particular domain <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.