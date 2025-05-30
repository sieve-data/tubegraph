---
title: How to use n8n for web scraping without code
videoId: c5dw_jsGNBk
---

From: [[colemedin]] <br/> 

This article outlines how to integrate Crawl4AI, an open-source, LLM-friendly web scraper, with [[workflow_automation_with_n8n | n8n]] to perform web scraping and build a knowledge base without writing any code <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The process demonstrates deploying Crawl4AI with Docker and leveraging it within [[workflow_automation_with_n8n | n8n]] workflows to scrape website pages in seconds <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Why Use Crawl4AI with [[workflow_automation_with_n8n | n8n]]?

While there are many ways to crawl websites, and even options within [[workflow_automation_with_n8n | n8n]] itself, Crawl4AI is highlighted as superior due to its speed, intuitiveness, and open-source nature <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The only potential cost is hosting the crawler on a cloud machine <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Deploying Crawl4AI with Docker

To use Crawl4AI within [[workflow_automation_with_n8n | n8n]], it must be deployed as an API endpoint, which is facilitated by Docker <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Unlike Python where Crawl4AI can be imported as a library, [[workflow_automation_with_n8n | n8n]] requires an external API call <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

### Deployment Options

There are several ways to install Crawl4AI with Docker:

*   **Including in a Local AI Starter Kit**: This is a viable option that could be covered in future content <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Running Locally or on the Same [[workflow_automation_with_n8n | n8n]] Cloud Instance**:
    *   This method is cost-effective if you already have an [[workflow_automation_with_n8n | n8n]] instance or local machine <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   However, Crawl4AI can be a resource hog (CPU and RAM) as it runs a headless browser, so hosting it separately is often recommended to prevent [[workflow_automation_with_n8n | n8n]] slowdowns <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
    *   Commands to run locally (assuming Docker is installed):
        ```bash
        docker pull uncodecraw4ai
        docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token uncodecraw4ai
        ``` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
*   **Dedicated API Endpoint in the Cloud (e.g., DigitalOcean)**:
    *   DigitalOcean's App Platform is recommended for ease of use <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
    *   **Steps for DigitalOcean App Platform**:
        1.  Create a new app platform and select "Container Image" <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
        2.  Pull from Docker Hub; the repository is `unclecode/crawl4ai` and the image tag for DigitalOcean is `basic-amd64` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
        3.  Configure resource size: be mindful of RAM and CPU needs (up to 4GB RAM for heavy crawling) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
        4.  Set the port to `11235` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
        5.  Add an environment variable for security: `CRAWL4AI_API_TOKEN` with your desired Bearer token value (e.g., `test_auth`) <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
        6.  Create the resource; DigitalOcean automatically provides an SSL-protected HTTPS endpoint <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
    *   The health endpoint (e.g., `your-app-url/health`) can be checked to confirm deployment status <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Building the [[workflow_automation_with_n8n | n8n]] Workflow for [[Extracting and processing data in n8n | Web Scraping]]

The example workflow builds an [[ai_automation_with_n8n | AI agent]] that becomes an expert on Pydantic AI documentation by scraping its pages and storing the data in a Superbase vector store <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Ethical Scraping Guidelines

Always scrape ethically <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Before scraping, check:
*   `robots.txt` file (e.g., `youtube.com/robots.txt`) for rules on crawling <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   The website's terms of use <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Workflow Steps

1.  **Get URLs from `sitemap.xml`**:
    *   Many documentation pages and e-commerce sites provide a `sitemap.xml` (e.g., `pydantic-ai.com/sitemap.xml`) which lists most available web pages <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   Use an HTTP Request node to fetch the sitemap XML <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
2.  **Convert XML to JSON**: Use an XML to JSON node for easier processing within [[workflow_automation_with_n8n | n8n]] <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.
3.  **Split Items for Looping**:
    *   The XML-to-JSON conversion might result in a single item in [[workflow_automation_with_n8n | n8n]]. Use a "Split Out Items" node based on the `urlset.url` value to turn each URL into an individual item <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
    *   This allows [[workflow_automation_with_n8n | n8n]] to loop over each URL <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
    *   **Batch Size**: The batch size in the loop can be adjusted (e.g., 1 URL at a time) to manage resource usage, especially given Crawl4AI's CPU/RAM demands <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
4.  **Make API Request to Crawl4AI**:
    *   Within the loop, use an HTTP Request node to interact with the deployed Crawl4AI endpoint <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
    *   **URL**: Use the DigitalOcean app URL (e.g., `your-app-url/crawl`) or `http://localhost:11235/crawl` if self-hosting <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
    *   **Authentication**: Set up a "Generic Credential" with type "Header Auth". The "Name" should be `Authorization`, and the "Value" should be `Bearer <your_secret_token>` (e.g., `Bearer test_auth`) <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.
    *   **Request Body (JSON)**:
        *   `urls`: Provide the single URL to scrape (e.g., `{{ $json.location }}`) <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
        *   `priority`: Optional, for managing task queues (e.g., `10`) <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.
5.  **Handle Asynchronous Scraping (Polling)**:
    *   Crawl4AI's `/crawl` endpoint returns a `task_id` because scraping can take time <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.
    *   Use a "Wait" node (e.g., 5 seconds) after the initial crawl request <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.
    *   Make a second HTTP Request to the `/task` endpoint with the `task_id` (e.g., `your-app-url/task/{{ $json.task_id }}`) to check the status <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.
    *   Use an "If" node to check if the `status` is `completed` <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
    *   If `false` (still processing), loop back to the "Wait" node and try again, creating a polling mechanism <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>.
    *   If `true` (completed), the response will contain the scraped HTML, links, and markdown <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
6.  **Insert into Superbase Knowledge Base**:
    *   Use the "Superbase Vector Store" node <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.
    *   **Embedding Model**: Connect your OpenAI API key and select a model like "OpenAI Text Embedding 3 Small" <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.
    *   **Data Loader**: Use the default data loader.
    *   **Data**: Input the markdown content from the Crawl4AI response (e.g., `{{ $json.res.markdown }}`) <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.
    *   **Metadata**: Optionally include the source URL (e.g., `{{ $json.url }}`) to track where chunks came from <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
    *   **Splitter**: Use a text splitter with a defined chunk size (e.g., 5000 characters) <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>.
    *   **Superbase Credentials**: Provide your Superbase URL (host) and Service Role Secret <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.
    *   **Superbase Table Setup**:
        *   In Superbase, go to the SQL Editor.
        *   Copy the SQL code for creating the `documents` table and `match_documents` function from the [[workflow_automation_with_n8n | n8n]] Superbase Vector Store node's quickstart documentation (excluding the `vector` extension enablement, which is default) <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>.
        *   Paste and run the SQL query to create the table and function <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>.
    *   After execution, the scraped content will be chunked and inserted into the Superbase `documents` table with their embeddings <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.

## Building a [[ai_automation_with_n8n | ChatGPT Style App with n8n and Open Web UI | Simple AI Agent for RAG]]

Once the knowledge base is populated, a basic [[ai_automation_with_n8n | AI agent]] can be built in [[workflow_automation_with_n8n | n8n]] to interact with it:
*   Use a "Chat Message Receive" trigger <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>.
*   Add an "AI Agent" node <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.
*   Configure chat history (e.g., Superbase chat history) <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.
*   Select an LLM (e.g., GPT-4o Mini) <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>.
*   Hook in the "Superbase Vector Store" tool for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>.

This setup allows the [[ai_automation_with_n8n | AI agent]] to answer questions by retrieving relevant information from the scraped knowledge base <a class="yt-timestamp" data-t="00:31:25">[00:31:25]</a>.

This approach provides a no-code method for [[creating_powerful_ai_workflows_with_n8n | creating powerful AI workflows with n8n]] by combining web scraping with RAG, laying a foundation for more advanced [[ai_automation_with_n8n | AI automation with n8n]] <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.