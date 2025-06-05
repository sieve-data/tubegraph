---
title: Data extraction from web pages to Google Sheets
videoId: kjSGc7uwDo8
---

From: [[aidotengineer]] <br/> 

Retriever.com aims to transform browser functionality, addressing the current bottleneck of manual data handling. Many professionals spend hours daily copying and pasting information between websites, Google Sheets, or CRM systems <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Traditional methods like offshored scraping are expensive and unreliable, while RPA bots often break with website changes <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Retriever resolves these issues by providing an AI web agent in the form of a Chrome extension <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Core Capabilities

Retriever, as a Chrome extension, offers an AI web agent that can perform tasks autonomously across pages and extract structured data directly into sheets <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Autonomous Actions and Data Extraction
Users can provide natural language prompts, and the AI web agent will interact with the page to complete tasks and extract data. For example, it can fill search fields, interact with page elements, and export information to Google Sheets <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Structured Data Export** Users can prompt the agent to "extract this data for every article on the page and click this export button," and Retriever will write all the data to Google Sheets <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Combined Tasks** The agent can perform an action on a page, and then extract data, supporting various combinations of tasks and extractions <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Cost-Effectiveness** This approach is highly cost-effective, potentially costing less than a penny per page extraction <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Multi-Page and Multi-Tab Processing
Retriever can perform actions and extractions across multiple tabs <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **URL List Processing** It can take a Google Sheet column of URLs, open them, interact with them, and extract data <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Complex Use Cases** For instance, from an archive search, Retriever can break down requests (e.g., "for the first five PDFs extract these fields") into subtasks, open them as new tabs, process them simultaneously, and write the data to sheets <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **Automated Comparisons** Users can select multiple tabs (e.g., Amazon product pages) and, even with an empty prompt, the AI web agent will identify and extract relevant fields for comparison into Google Sheets <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Pre-Extraction Actions** The agent can perform actions on tabs before extraction, such as changing review sorting from "top reviews" to "most recent" and then extracting details of the most recent review across all selected tabs simultaneously <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Advanced Research and Data Transformation
Retriever goes beyond basic extraction to support complex research and data manipulation.
*   **Summarization** It can summarize content from multiple design documents, PDFs, or Google Sheets open in the browser, extracting key points and summaries <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Market Research** For market research on companies, users can ask Retriever to extract specific information like company strategy, features, and pricing. It will generate a schema, navigate to relevant pages (e.g., pricing pages) on the target websites, and extract the data into sheets <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This includes a "deep search" feature to explore multiple pages to find requested data <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Complex Data Fields and Computation** Users can provide a Google Sheet with initial data (e.g., stock tickers) and ask Retriever to extract complex financial data (e.g., P/E ratio from Yahoo Finance, revenue for the last two years) and even compute new data fields (e.g., revenue growth) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Error Correction** The agent can correct user errors, such as navigating to Yahoo Finance even if given a company's main website URL, to find the requested financial data <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### [[Integration of thirdparty tools with AI web agents | Third-Party Integrations]] and Data Visualization
*   **Dynamic Function Calling** Retriever allows users to define and set up dynamic function calls to integrate with any API or third-party tool (e.g., WhatsApp, Discord, Slack) by providing information about the tool <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. This enables [[Automation of web tasks using AI web agents | automating communications]] across platforms like Instagram, Facebook, and WhatsApp <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Graph Generation** Retriever includes a "graph bot tool" that acts as a mini-agent, capable of generating dynamic data analysis graphs on the fly from extracted data. This leverages the LLM's ability to not only extract but also represent data in various formats <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

## Retriever's Unique Approach

Retriever differentiates itself from other AI agents in several key ways:

*   **[[Difference between textbased and visionbased data extraction | Text-Based Approach]] vs. Vision-Based**
    *   Most other agents (e.g., OpenAI Operator, Anthropic Claude, Google Mariner) use a vision-based or hybrid approach, taking screenshots to extract data <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
    *   Retriever uses a text-based approach, leveraging the web page's underlying structure (DOM) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. This results in less hallucination because the text is directly in context for the model <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
    *   Vision-based models are more prone to hallucination and are highly expensive, requiring multiple screenshots for a single action <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

*   **Client-Side Chrome Extension vs. Browser-on-the-Cloud**
    *   Many competitors use a browser-on-the-cloud model <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This leads to non-personalized results as the content might differ from what the user sees, and incurs higher costs due to proxies needed to funnel network requests <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
    *   Retriever is a client-side Chrome extension, operating directly within the user's browser <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. This approach is cheaper infrastructure-wise <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a> and offers significant advantages:
        *   **Content Access** It can access local, login-wall, or subscribed content because it sees exactly what the user is logged into <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. Unlike cloud-hosted browsers, it doesn't require storing or giving passwords, mitigating security risks and issues with paywalls or Cloudflare protections <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
        *   **Multi-Tab Processing** With a text-based approach and being an extension, Retriever can process active and background tabs, or multiple tabs at once, which is not feasible with vision-based approaches that require rendering <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This enables multi-tab contextual actions and parallel performance speed-ups <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

*   **Focus and Failure Rate**
    *   Unlike competitors focusing on consumer applications (e.g., booking flights), Retriever concentrates on [[Leveraging AI Tools for Efficiency and Scalability | productivity and automation use cases]], targeting manual and repetitive tasks <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
    *   For long-horizon tasks, Retriever distributes subtasks as new tabs, significantly reducing failure rates compared to approaches that attempt one long action on a single tab <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

*   **Extensible Integrations**
    *   Retriever's approach to [[Integration of thirdparty tools with AI web agents | third-party integrations]] is unique: users can define and set up function calls, making it much more extensible and scalable than custom, pre-set integrations offered by competitors <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

## Mission and Future Vision
Retriever's mission is to revolutionize data extraction with transparency and efficiency <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. A long-term goal is to enable [[Collaboration and data set construction using browser extensions | collaborative data set construction]]. This would allow individuals to volunteer and use the extension on their local machines to collaboratively build cost-efficient data sets, such as gathering information on local government events from thousands of websites, which is currently not feasible <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

To experience the future of AI agents in the browser, visit retriever.com <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.