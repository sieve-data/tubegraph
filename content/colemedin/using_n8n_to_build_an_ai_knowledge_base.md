---
title: Using n8n to build an AI knowledge base
videoId: c5dw_jsGNBk
---

From: [[colemedin]] <br/> 

This article describes how to leverage [[n8n_in_creating_ai_agents | n8n]] to build a [[creating_rag_ai_agents_using_n8n | knowledge base]] for [[ai_automation_with_n8n | AI agents]] without writing any code. It focuses on using [[crawl_for_ai | Crawl4AI]] as a web scraper and Superbase as the vector store for RAG (Retrieval Augmented Generation) implementations <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## What is Crawl4AI?
[[crawl_for_ai | Crawl4AI]] is an open-source, LLM-friendly web scraper designed to easily crawl any website and format its content for a RAG [[creating_rag_ai_agents_using_n8n | knowledge base]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Unlike many other web crawling methods, [[crawl_for_ai | Crawl4AI]] is described as fast, intuitive, and completely free, aside from the cost of hosting the crawler in the cloud if not run locally <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a><a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

## Why Use n8n for Building an AI Knowledge Base?
Previously, building an [[creating_rag_ai_agents_using_n8n | AI knowledge base]] with [[crawl_for_ai | Crawl4AI]] involved Python code <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. However, [[n8n_in_creating_ai_agents | n8n]] allows for a no-code approach to scrape sites and implement RAG <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. [[n8n_in_creating_ai_agents | n8n]] cannot directly run `pip install` commands for Python libraries like [[crawl_for_ai | Crawl4AI]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Instead, [[crawl_for_ai | Crawl4AI]] is deployed as an external API endpoint using Docker, which [[n8n_in_creating_ai_agents | n8n]] interacts with via HTTP requests <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a><a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a><a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Deploying Crawl4AI for n8n Integration

To use [[crawl_for_ai | Crawl4AI]] with [[n8n_in_creating_ai_agents | n8n]], it needs to be deployed as an API endpoint <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This can be done in several ways using Docker <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>:

*   **Locally or on the same instance as n8n**:
    *   This option saves costs as it doesn't require a dedicated [[crawl_for_ai | Crawl4AI]] instance <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   It involves pulling the [[crawl_for_ai | Crawl4AI]] Docker image and running it <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    *   However, [[crawl_for_ai | Crawl4AI]] can be resource-intensive due to running a headless browser, potentially slowing down [[n8n_in_creating_ai_agents | n8n]] if hosted on the same machine <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The API endpoint would be `http://localhost:11235` <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.

*   **Dedicated Cloud Instance (e.g., Digital Ocean)**:
    *   Recommended for better performance and to avoid resource conflicts with [[n8n_in_creating_ai_agents | n8n]] <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
    *   Digital Ocean's app platform is a user-friendly option <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
    *   Deployment steps on Digital Ocean:
        1.  Create a new app platform and pull from a container image <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a><a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
        2.  Specify the Docker Hub image: `unclecode/crawl4ai` with the tag `basic-amd64` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a><a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
        3.  Configure resource size (e.g., 4GB RAM may be needed for heavy crawling) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
        4.  Set the container port to `11235` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
        5.  Add an environment variable for security: `CRAWL_FOR_AI_API_TOKEN` with a desired Bearer token value <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
        6.  The app platform automatically provides an SSL-protected HTTPS endpoint <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

## Ethical Scraping Considerations

It is crucial to scrape websites ethically <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   Always check a website's `robots.txt` file (e.g., `youtube.com/robots.txt`) for scraping rules <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   Review the website's terms of use for any restrictions <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## The n8n Workflow for Knowledge Base Creation

The [[n8n_in_creating_ai_agents | n8n]] workflow automates the process of scraping web pages and inserting them into a Superbase vector store <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### 1. Getting URLs to Scrape
For documentation sites or e-commerce stores, `sitemap.xml` files are useful for obtaining a list of available URLs <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   An HTTP Request node can fetch the `sitemap.xml` content <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   A "Convert to JSON" node transforms the XML output into a more manageable JSON format <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

### 2. Processing URLs in n8n
*   A "Split In Batches" node is used to process each URL as a separate item, allowing for iterative scraping <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   The batch size can be adjusted (e.g., to 1 to simplify the workflow and reduce resource usage for [[crawl_for_ai | Crawl4AI]]) <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

### 3. Interacting with Crawl4AI
This involves two main HTTP requests to the [[crawl_for_ai | Crawl4AI]] API endpoint:
*   **Initiating a Scrape Task**:
    *   An HTTP Request node sends a POST request to the `/crawl` endpoint of the [[crawl_for_ai | Crawl4AI]] API <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
    *   Authentication is handled using a "Generic Credential" of type "Header Auth" with the header name `Authorization` and a value formatted as `Bearer YOUR_API_TOKEN` <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.
    *   The request body contains the `urls` (singular URL) and a `priority` <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.
    *   This request returns a `task ID` because scraping can take time <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.

*   **Checking Task Status and Retrieving Data**:
    *   A "Wait" node pauses the workflow for a specified duration (e.g., 5 seconds) <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.
    *   Another HTTP Request node calls the `/task/{task_id}` endpoint to check the status of the scrape task <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.
    *   An "If" node checks if the `status` of the task is "completed" <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
    *   If `false` (still processing), the workflow loops back to the "Wait" node, continuously polling for completion <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>.
    *   If `true` (completed), the request returns the scraped content, including HTML, links, and markdown <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a><a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.

### 4. Storing Data in Superbase (Vector Store)
The final step is to insert the scraped markdown content into a Superbase vector store:
*   An "Embeddings" node (e.g., using OpenAI Text Embedding 3 Small) converts the markdown into vector embeddings <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.
*   A "Text Splitter" node chunks the data (e.g., chunk size of 5000) for RAG <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>.
*   A "Superbase Vector Store" node connects to Superbase using the host URL and service role secret <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>.
*   The Superbase table setup for documents and the `match_documents` function (for RAG retrieval) can be initialized using a provided SQL template <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.
*   Metadata, such as the original page URL, can be added to the chunks for better contextual retrieval <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.

## Building the AI Agent with the Knowledge Base
Once the [[knowledge_base | knowledge base]] is populated, a simple [[ai_automation_with_n8n | AI agent]] can be configured in [[n8n_in_creating_ai_agents | n8n]] to interact with it:
*   A "Chat Message Receive" trigger initiates the agent's response <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>.
*   An "AI Agent" node is configured with:
    *   Superbase chat history.
    *   An LLM model (e.g., GPT-4o Mini) <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.
    *   The Superbase vector store tool for RAG <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>.
*   When a question is asked, the agent uses the vector store retrieval tool to find relevant chunks from the [[knowledge_base | knowledge base]] and provides a response based on that information <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>.

This [[creating_custom_ai_workflows_with_n8n | workflow]] provides a foundational proof-of-concept for [[prototyping_ai_agents_using_n8n | prototyping AI agents]] with no-code tools like [[n8n_in_creating_ai_agents | n8n]] and external services like [[crawl_for_ai | Crawl4AI]] and Superbase <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>. The entire [[n8n_in_creating_ai_agents | n8n]] workflow is available in a GitHub repository for download and customization <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a><a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.