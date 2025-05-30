---
title: Limitations of large language models
videoId: JWfNLF_g_V0
---

From: [[colemedin]] <br/> 

One of the significant [[challenges_with_large_language_models | challenges with large language models]] (LLMs) is their general knowledge and limited understanding of new or very specific information due to their training data cut-off <a class="yt-timestamp" data-t="00:00:03"></a>.

For instance, an [[ai_agents_and_large_language_models | AI agent]] framework like Pydantic AI is unknown to general LLMs such as Claude <a class="yt-timestamp" data-t="00:00:11"></a>. Even [[large_language_models | LLMs]] that can search the web provide only "bare bones" information for new topics <a class="yt-timestamp" data-t="00:00:20"></a>.

## Knowledge Gaps
[[large_language_models | LLMs]] struggle with:
*   **General Knowledge:** Their knowledge base is broad but lacks depth in niche or recently developed areas <a class="yt-timestamp" data-t="00:00:03"></a>.
*   **Training Cut-off:** Information that emerged after their last training update is unknown to them <a class="yt-timestamp" data-t="00:00:05"></a>.
*   **Specific Information:** They may not have detailed knowledge on specific frameworks, products, or highly specialized domains <a class="yt-timestamp" data-t="00:00:16"></a>.

## Data Ingestion and Understanding
[[large_language_models | LLMs]] also face difficulties when presented with unformatted or complex data:
*   **Raw HTML:** It is challenging for humans to extract useful information from raw HTML, and it is even harder for an [[large_language_models | LLM]] <a class="yt-timestamp" data-t="00:03:00"></a>.
*   **Hallucination:** Pasting unformatted data, like raw HTML with many tags, directly into an [[large_language_models | LLM]] prompt can lead to the model "hallucinating" or providing inaccurate responses <a class="yt-timestamp" data-t="00:06:43"></a>.

## Addressing Limitations with RAG and Web Scraping
To overcome these limitations, methods like Retrieval Augmented Generation (RAG) are crucial <a class="yt-timestamp" data-t="00:00:39"></a>. RAG involves providing external, curated knowledge to an [[large_language_models | LLM]] to make it an expert in a specific domain <a class="yt-timestamp" data-t="00:00:45"></a>.

A common approach for RAG is to scrape data from websites and provide it as a knowledge base <a class="yt-timestamp" data-t="00:18:24"></a>.

### Challenges in Data Curation
The process of curating this external knowledge can be difficult and slow <a class="yt-timestamp" data-t="00:00:58"></a>. Ingesting an entire website into a knowledge base efficiently requires specialized tools <a class="yt-timestamp" data-t="00:01:03"></a>.

### Crawl for AI: A Solution for Data Preparation
Crawl for AI is an open-source web crawling framework designed to address these data curation challenges <a class="yt-timestamp" data-t="00:01:16"></a>. It scrapes websites and formats the output optimally for [[large_language_models | LLMs]] <a class="yt-timestamp" data-t="00:01:22"></a>.

Key benefits of Crawl for AI include:
*   **Efficiency:** It is fast, intuitive, and memory-efficient, overcoming common issues like slowness, over-complication, and resource intensity in typical website scraping systems <a class="yt-timestamp" data-t="00:01:34"></a>.
*   **HTML to Markdown Conversion:** It converts raw HTML into a clean, human-readable Markdown format, which is much easier for an [[large_language_models | LLM]] to understand for RAG <a class="yt-timestamp" data-t="00:03:20"></a>.
*   **Advanced Features:** It handles complex underlying processes such as proxies and session management <a class="yt-timestamp" data-t="00:03:53"></a>.
*   **Content Filtering:** It removes irrelevant content like script tags or redundant information, ensuring only useful data is ingested into the knowledge base <a class="yt-timestamp" data-t="00:04:26"></a>.
*   **Ease of Use:** It is easy to set up and deploy, with a Docker option available <a class="yt-timestamp" data-t="00:04:08"></a>. It uses Playwright under the hood for web scraping <a class="yt-timestamp" data-t="00:04:58"></a>.

#### Efficient URL Extraction
For comprehensive website ingestion, [[ai_agents_and_large_language_models | AI agents]] need an efficient way to extract all URLs from a website <a class="yt-timestamp" data-t="00:07:29"></a>. This can be achieved using a website's `sitemap.xml` file, which provides the entire structure and all existing pages <a class="yt-timestamp" data-t="00:07:54"></a>.

#### Ethical Considerations
Before web scraping, it is important to check a website's `robots.txt` file, which outlines the rules and disallowed pages for web scraping, ensuring ethical practices <a class="yt-timestamp" data-t="00:09:08"></a>.

#### Optimizing Multi-URL Crawling
To efficiently process multiple URLs, Crawl for AI offers:
*   **Same Browser Session:** Using the same browser session for all visited pages significantly improves efficiency compared to spinning up a new browser for each URL <a class="yt-timestamp" data-t="00:11:06"></a>.
*   **Parallel Processing:** The framework supports parallel processing, allowing multiple pages to be visited simultaneously, further accelerating the data extraction process <a class="yt-timestamp" data-t="00:13:16"></a>. This significantly reduces processing time, especially for large websites with hundreds or thousands of pages <a class="yt-timestamp" data-t="00:15:00"></a>.

### Real-world Application: Pydantic AI Expert Agent
Using Crawl for AI, it is possible to build an [[ai_agents_and_large_language_models | AI agent]] that is an expert in a specific domain, such as the Pydantic AI framework <a class="yt-timestamp" data-t="00:15:22"></a>. By pulling all Pydantic AI documentation and integrating it into a vector database for RAG, an [[ai_agents_and_large_language_models | AI agent]] can answer specific questions about the framework, including complex code examples, which general [[large_language_models | LLMs]] would not know <a class="yt-timestamp" data-t="00:16:09"></a>.