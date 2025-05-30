---
title: Deploying Crawl4AI with Docker
videoId: c5dw_jsGNBk
---

From: [[colemedin]] <br/> 

[[introduction_to_crawl_for_ai | Crawl for AI]] is an open-source, LLM-friendly web scraper designed to easily crawl sites and format data for a RAG (Retrieval Augmented Generation) knowledge base for AI agents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it can be used with Python code <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, integrating it into no-code platforms like n8n requires deploying [[crawl_for_ai_web_crawling_framework | Crawl for AI]] as an API endpoint using [[deploying_and_scaling_ai_agents_with_docker | Docker]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Why [[deploying_and_scaling_ai_agents_with_docker | Docker]] for n8n?
When using n8n, it's not possible to directly install [[crawl_for_ai_web_crawling_framework | Crawl for AI]] as a Python library using `pip install` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Instead, [[crawl_for_ai_web_crawling_framework | Crawl for AI]] needs to be hosted externally as an API endpoint, which can then be called by HTTP Request nodes within n8n workflows <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. [[deploying_and_scaling_ai_agents_with_docker | Docker]] serves as the solution for deploying [[crawl_for_ai_web_crawling_framework | Crawl for AI]] in this manner <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Ethical Scraping Considerations
Before scraping, it's crucial to check a website's `robots.txt` file (e.g., `youtube.com/robots.txt`) and terms of use to ensure ethical scraping practices <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Many websites block scrapers or request that they not be used <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## [[deploying_and_scaling_ai_agents_with_docker | Docker]] Deployment Options
There are several ways to install [[crawl_for_ai_web_crawling_framework | Crawl for AI]] with [[deploying_and_scaling_ai_agents_with_docker | Docker]] <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>:

1.  **Within a Local AI Starter Kit (Future possibility)**: [[crawl_for_ai_web_crawling_framework | Crawl for AI]] could be included as a [[deploying_and_scaling_ai_agents_with_docker | Docker]] image within a local AI starter kit <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
2.  **Locally or on a self-hosted n8n instance**: You can run the [[deploying_and_scaling_ai_agents_with_docker | Docker]] container on your local computer or on the same [[cloud | cloud]] instance where n8n is self-hosted <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This saves costs as you don't need a dedicated instance <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
    *   To do this, pull the image from [[deploying_and_scaling_ai_agents_with_docker | Docker]] and run it <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    *   Optionally, run it with a secret token to protect the endpoint <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   The necessary commands are:
        ```bash
        docker pull uncclecode/crawl4ai:basic-amd64
        docker run -d -p 11235:11235 -e "CRAWL4AI_API_TOKEN=your_secret_token" uncclecode/crawl4ai:basic-amd64
        ```
    *   If hosted locally or alongside n8n, the API endpoint URL would be `http://localhost:11235` <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
3.  **Dedicated Cloud Instance (Recommended)**: [[crawl_for_ai_web_crawling_framework | Crawl for AI]]'s [[deploying_and_scaling_ai_agents_with_docker | Docker]] container can be a resource hog, requiring significant CPU and RAM due to running a headless browser for scraping <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Therefore, hosting it on an entirely separate instance in the [[cloud | cloud]] is recommended to prevent it from slowing down your n8n instance <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Deploying on DigitalOcean's App Platform (Example)
DigitalOcean's App Platform simplifies running [[deploying_and_scaling_ai_agents_with_docker | Docker]] containers as API endpoints <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

1.  **Create New App Platform**: Select "Container Image" as the source <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
2.  **Container Image Details**:
    *   Images are hosted on [[deploying_and_scaling_ai_agents_with_docker | Docker]] Hub <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   **Repository**: `unclecode/crawl4ai` (from creator's GitHub username) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   **Image Tag**: `basic-amd64` (for Linux architecture) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
3.  **Resource Configuration**:
    *   Choose resource size: Plans can start from $5/month <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   **RAM/CPU**: [[crawl_for_ai_web_crawling_framework | Crawl for AI]] may require 4GB of RAM or more, especially when crawling many pages simultaneously <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   **Port**: Change the default port to `11235` (the actual port for [[deploying_and_scaling_ai_agents_with_docker | Docker]]) <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
4.  **Environment Variables (Security)**:
    *   Define `CRAWL4AI_API_TOKEN` as a global environment variable <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
    *   Set its value to your desired Bearer token (e.g., `test_auth`) <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This protects your API endpoint from unauthorized use <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
5.  **Deployment**: Review settings and create the resource <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. DigitalOcean will build the container and provide an SSL-protected HTTPS endpoint within minutes <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
6.  **Verification**: You can visit the provided URL, or append `/health` to check the status (e.g., `status: healthy`) <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Integrating with n8n
Once [[crawl_for_ai_web_crawling_framework | Crawl for AI]] is deployed as an API endpoint, n8n can interact with it using HTTP Request nodes <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

1.  **API Endpoint URL**:
    *   For a DigitalOcean deployment, use the provided HTTPS URL (e.g., `https://your-app.ondigitalocean.app/crawl`) <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
    *   For local/self-hosted [[deploying_and_scaling_ai_agents_with_docker | Docker]], use `http://localhost:11235/crawl` <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
2.  **Authentication**:
    *   Set up a generic credential type in n8n as "Header Auth" <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
    *   The header name must be `Authorization` <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.
    *   The value should be `Bearer ` followed by your `CRAWL4AI_API_TOKEN` (e.g., `Bearer test_auth`) <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
3.  **Request Body**:
    *   The JSON payload for scraping includes `urls` (singular URL) and `priority` <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
    *   Example: `{"urls": "https://example.com", "priority": 10}` <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
4.  **Asynchronous Scraping**:
    *   Initial calls to the `/crawl` endpoint return a `task ID`, not the scraped data directly <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>. This is because scraping can take time <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.
    *   To get the scraped data, ping the `/task/{task_id}` endpoint to check the status <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.
    *   Implement a loop in n8n (e.g., using a "Wait" node and "If" statement) to repeatedly check the task status every few seconds until it's `completed` <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>. Once complete, the response will include HTML, links, and markdown content <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

This integration provides a no-code approach to web scraping for RAG knowledge bases within n8n workflows <a class="yt-timestamp" data-t="00:32:48">[00:32:48]</a>.