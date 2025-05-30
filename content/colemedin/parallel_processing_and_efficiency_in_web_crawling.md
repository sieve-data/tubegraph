---
title: Parallel processing and efficiency in web crawling
videoId: JWfNLF_g_V0
---

From: [[colemedin]] <br/> 

When working with Large Language Models (LLMs), a significant challenge is that their knowledge is often too general and limited, especially for new information due to training cut-offs <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. To make an LLM an expert in a specific domain, such as an e-commerce store or a new AI agent framework, external knowledge must be curated and provided, often through [[using_web_crawlers_and_databases_in_rag | Retrieval Augmented Generation (RAG)]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. However, this data curation process, particularly when ingesting an entire website, can be very difficult and slow <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Introducing Crawl for AI

[[crawl_for_ai_web_crawling_framework | Crawl for AI]] is an open-source web crawling framework designed to address these inefficiencies by scraping websites and formatting the output optimally for LLM comprehension <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Unlike typical website scraping systems that are often slow, overly complicated, and resource-intensive, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] is noted for being intuitive, very fast, easy to set up, and extremely memory efficient <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Efficiency in Practice

One of the main inefficiencies in web scraping is the process of repeatedly spinning up a new browser for every URL visited <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. [[crawl_for_ai_web_crawling_framework | Crawl for AI]] offers solutions to significantly improve this efficiency:

#### Single Browser Session
Instead of initiating a new browser for each page, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] can use the same browser session for all pages being visited and pulled <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This drastically reduces overhead and speeds up sequential crawling, allowing dozens of pages to be processed in seconds <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

#### Parallel Processing
To achieve even greater speed, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] supports parallel processing. This allows the system to visit multiple pages simultaneously, pull the markdown for all of them, and then combine the results into a single list <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. This is achieved by creating different sessions that run concurrently within a single browser instance <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. For example, it can visit 10 pages at the exact same time, get their markdown, and then move on to the next set of 10 <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

#### Memory Efficiency
Despite running an entire browser in the background and visiting multiple pages in parallel, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] demonstrates remarkable memory efficiency. For instance, processing batches of pages might only incur a peak RAM usage of around 119 megabytes <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## Underpinning Technology
[[crawl_for_ai_web_crawling_framework | Crawl for AI]] utilizes Playwright, another open-source tool, under the hood to perform its web scraping functionality by running a browser in the background <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## Importance of Efficiency
For large-scale data ingestion, such as an e-commerce store with hundreds or thousands of products, processing information sequentially becomes a significant drag <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. The efficiencies provided by [[crawl_for_ai_web_crawling_framework | Crawl for AI]], including its fast processing, memory efficiency, and support for parallel crawling, are crucial for rapidly building knowledge bases for LLMs <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

## Related Concepts

### Sitemap.xml for URL Discovery
To efficiently identify all URLs on a website for crawling, many websites provide a `sitemap.xml` file. This XML file offers the entire structure of the website and lists all existing pages <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. By parsing this sitemap, a web crawler can extract all relevant URLs programmatically, avoiding manual collection and ensuring scalability <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

### Ethical Considerations
Before scraping any website, it is important to consider [[ethical_web_scraping_practices | ethical web scraping practices]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Most websites have a `robots.txt` file (e.g., `youtube.com/robots.txt` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>) that outlines their rules for web scraping, specifying which agents are allowed and which pages are disallowed <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Always check this file to ensure compliance and ethical data collection <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.