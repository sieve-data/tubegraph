---
title: Automation of web tasks using AI web agents
videoId: kjSGc7uwDo8
---

From: [[aidotengineer]] <br/> 

Retriever.com introduces an [[ai_in_workflow_automation | AI-powered solution]] to automate web-based tasks, leveraging an [[ai_agents_using_humanlike_interfaces_and_workflows | AI web agent]] within a Chrome extension <a class="yt-timestamp" data-t="01:20:41">[01:20:41]</a>. The creators, Arin and Bani, suggest that Retriever could be as transformative to the browser as Netscape's initial creation <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## The Problem: Browser as a Workflow Bottleneck

The browser is often a bottleneck for many workflows <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Individuals in full-time jobs spend hours manually copying and pasting information between websites, Google Sheets, or CRMs <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Current solutions present significant challenges:
*   **Offshoring Data Scraping**: Expensive and unreliable third parties are often used for scraping <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **RPA Bots**: Robotic Process Automation (RPA) bots frequently break when websites change <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Data Silos**: Data can be isolated on websites or within APIs, making combination difficult and leading to untapped potential <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Retriever's Solution: An AI Web Agent Chrome Extension

Retriever aims to change these issues by offering a Chrome extension that acts as an [[role_of_ai_agents_in_workflow_automation | AI web agent]] <a class="yt-timestamp" data-t="01:22:15">[01:22:15]</a>. Users can open a side panel and provide natural language prompts for tasks to be performed autonomously across pages, or to extract structured data to sheets <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

### Key Capabilities and Use Cases

Retriever is designed for [[developing_ai_agents_for_productivity | productivity]] and automation, focusing on repetitive, manual tasks <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="01:51:57">[01:51:57]</a>.

#### Autonomous Task Execution
*   **Website Interaction**: The AI web agent can interact with all elements on a page, such as filling out search fields or clicking buttons, based on a natural language prompt <a class="yt-timestamp" data-t="02:02:40">[02:02:40]</a>.
    *   *Example*: Finding and following a specific podcast page on LinkedIn <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. The agent can even recognize if a page is already followed <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   **Multi-Tab and Cross-Page Actions**: Retriever can perform actions across multiple tabs simultaneously or process multiple URLs provided in a Google Sheet column <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
    *   *Example*: Applying to multiple LinkedIn job applications <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
    *   *Example*: Changing a filter (e.g., from "top reviews" to "most recent") on multiple Amazon product pages before extracting data <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.

#### Structured Data Extraction
*   **Export to Google Sheets**: The agent can extract specified data from a page or multiple pages and write it directly to Google Sheets <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a> <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
    *   This approach is highly cost-effective, costing less than a penny for a page extraction <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **Automated Field Identification**: If the prompt is left empty, the [[ai_agents_beyond_chatbots | AI web agent]] can intelligently determine which fields are likely of interest for extraction <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
*   **Deep Search Feature**: Retriever can explore web pages, navigating through multiple sub-pages to find and extract requested data, such as pricing information from company websites <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a> <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.
*   **Complex Data Aggregation and Computation**:
    *   *Example*: Extracting specific financial data (P/E ratio, revenue) for stocks from Yahoo Finance and then computing new data fields like revenue growth directly within the sheet <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. The agent can even correct wrong URLs provided by the user <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

#### Advanced Use Cases
*   **Summarization**: Users can select multiple design documents or PDFs and ask Retriever to extract key points and summaries <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.
*   **Market Research**: Conduct market research on multiple companies by extracting specific data points like strategy, features, and pricing <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.
*   **[[integration_of_thirdparty_tools_with_ai_web_agents | Dynamic Function Calling for Third-Party Integrations]]**: Retriever's function calling feature allows users to integrate with any API or third-party tool by providing its information, rather than relying on a fixed set of connectors <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
    *   *Example*: Sending automated messages to customer phone numbers via WhatsApp integration <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>. This enables automation of social communications across platforms like Instagram, Facebook, and WhatsApp <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.
*   **Graph Generation**: A "graph bot" tool within Retriever can generate dynamic data analysis graphs on the fly from structured data <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>. This leverages LLM capabilities beyond just extraction, to represent data in various formats <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.

## Retriever's Differentiators in the Agentic Landscape

When comparing Retriever to other [[developing_ai_agents_and_agentic_workflows | AI agents]] and browser automation solutions like OpenAI Operator, Anthropic Claude, and Google Mariner <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a> <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>, Retriever highlights several key advantages:

### Text-Based Approach vs. Vision-Based Models
*   Most agents use a vision-based approach, taking screenshots of pages to extract data <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.
*   Retriever uses a text-based approach, leveraging the webpage's underlying text structure <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.
    *   **Reduced Hallucination**: Text-based models are less prone to hallucination because the text is directly in context <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a> <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>.
    *   **Cost-Effective**: Vision-based approaches are expensive, requiring multiple screenshots for single actions <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.

### Client-Side Chrome Extension vs. Cloud-Hosted Browsers
*   Many competitors use browsers hosted on the cloud <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.
*   Retriever is a client-side Chrome extension <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a> <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.
    *   **Personalized Results**: Cloud browsers often provide generic pages, potentially different from what the user sees <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>. Retriever sees exactly what the user sees, including personalized content <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.
    *   **No Proxies**: Cloud solutions require proxies to funnel network requests, which is expensive <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>.
    *   **Enhanced Security**: Retriever does not store user passwords, which is a risk with cloud-hosted browsers <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.
    *   **Access to Restricted Content**: Retriever can access content behind paywalls, login walls, or Cloudflare protections because it operates within the user's logged-in browser session <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a> <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>.
    *   **Multi-Tab Processing**: Retriever can process active and background tabs simultaneously, which is not possible with vision-based approaches that rely on rendered content <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a> <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>. This allows for parallel actions and speed improvements <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>.

### Distributed Subtasks
*   Unlike competitors attempting long-horizon tasks on a single tab, Retriever distributes subtasks to new tabs, significantly reducing failure rates <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a> <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>.

### Extensible Third-Party Integrations
*   Retriever's approach to [[integration_of_thirdparty_tools_with_ai_web_agents | third-party integrations]] allows users to define and share their own function calls, making it much more extensible and scalable than pre-set custom integrations <a class="yt-timestamp" data-t="16:13:00">[16:13:00]</a>.

## Mission and Future Vision

Retriever's mission is to revolutionize data extraction with transparent and efficient AI <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>. A long-term goal is to enable collaborative data set construction by allowing people to volunteer and leverage the extension on their local laptops <a class="yt-timestamp" data-t="16:41:00">[16:41:00]</a>. This could make the creation of large, cost-efficient data sets (e.g., local government events from thousands of websites) feasible <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>.