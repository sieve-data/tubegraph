---
title: Automation of manual workflows with AI web agents
videoId: kjSGc7uwDo8
---

From: [[aidotengineer]] <br/> 

Retriever.com aims to be as transformative to the browser as Netscape was at its creation <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The browser often acts as a bottleneck for many workflows <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Many individuals spend hours daily manually copying and pasting information between websites, Google Sheets, or CRMs <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Other common challenges include:
*   Offshoring data scraping to third parties, which is expensive and unreliable <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   Setting up RPA Bots that frequently break when website layouts change <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   Data silos where some data is only available on websites and other data via APIs, creating a hassle for users to combine <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
These issues lead to untapped potentials for leveraging data <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Retriever.com: An AI Web Agent Chrome Extension

Retriever addresses these problems as a Chrome extension that leverages being an [[role_of_ai_agents_in_planning_and_executing_tasks | AI web agent]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Users can open a side panel and provide tasks for the agent to perform autonomously across web pages, as well as extract structured data to sheets <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Key Capabilities and Use Cases

Retriever's [[ai_in_workflow_automation_and_augmentation | AI in workflow automation and augmentation]] facilitates various tasks:

*   **Autonomous Task Execution:**
    *   Users can provide natural language prompts, such as "find and follow the latent space podcast page," and the [[role_of_ai_agents_in_planning_and_executing_tasks | AI web agent]] will interact with the page to complete the task autonomously, including filling search fields and interacting with page elements <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

*   **Structured Data Extraction:**
    *   A built-in feature allows users to extract data to Google Sheets with prompts like "for every article on the page extract this data and click this export button" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This approach is highly cost-effective, potentially costing less than a penny per page extraction <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

*   **Multi-Tab Actions and Extractions:**
    *   Retriever can perform actions across multiple tabs <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. It can take a Google Sheet column of URLs, open them, interact with them, and extract data <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   Complex use cases include extracting specific fields from the first five PDFs on an archive search page, breaking them down into subtasks, opening them as new tabs, and processing them simultaneously <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
    *   When comparing product pages (e.g., Amazon products), the agent can automatically determine relevant fields to extract without a specific prompt, allowing for effective product comparison <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   It can even extract URLs, such as image source URLs for visual comparison <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   Actions can be performed on tabs *before* extraction, such as changing a review sort order from "top reviews" to "most recent" across multiple pages simultaneously, and then extracting the details <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

*   **Advanced Research and Summarization:**
    *   Users can select multiple design documents and prompt Retriever to "extract key points and summary," which it will then process and provide a concise summary for each document <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This works across Google Docs, PDFs, and Google Sheets <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
    *   For market research, users can ask Retriever to visit company homepages (e.g., Retriever, Browse AI), navigate to pricing pages, and extract data like company strategy, features, and pricing into a sheet <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This "deep search" feature allows the agent to explore and navigate multiple pages to find requested data <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Retriever is noted as one of the first to implement this deep search <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   More complex financial market research can involve selecting a Google Sheet with stock information and asking for data like P/E ratio from Yahoo Finance and revenue for the last two years, and even computing new data fields like revenue growth <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. The agent can correct user errors, such as navigating to Yahoo Finance even if a company's website URL was incorrectly provided <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

*   **Dynamic Function Calling and Third-Party Integrations:**
    *   A key feature is dynamic function calling, allowing users to define and integrate any API or third-party tool <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
    *   An example given is WhatsApp integration to send messages to customer phone numbers listed in a Google Sheet, enabling automated social communications across platforms like Instagram, Facebook, and WhatsApp <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. This demonstrates the [[integration_of_ai_coding_agents_with_thirdparty_tools | integration of AI coding agents with third-party tools]] for seamless workflows.

*   **Graph Generation:**
    *   Retriever includes a "graph bot" tool, a mini-agent within Retriever Agent Studio, that can generate dynamic data analysis graphs from existing data on the fly <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This leverages LLMs' capability to represent data in various formats <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

### Retriever's Advantages and Approach

Retriever's approach offers several [[benefits_and_challenges_of_using_ai_in_workflow | benefits and challenges of using AI in workflow]] compared to other agents in the landscape (e.g., OpenAI Operator, Anthropic Claude, Google Mariner):

*   **Text-Based Approach:** Unlike many agents that use vision-based approaches (taking screenshots), Retriever uses a text-based approach by leveraging the web page's underlying structure <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. This results in less hallucination and is less expensive than taking multiple screenshots for every action <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   **Client-Side Chrome Extension:** Most competitors use browsers on the cloud, which leads to non-personalized results and requires expensive proxies to funnel network requests <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. Retriever's client-side extension is cheaper infrastructurally and allows access to local or login-protected sites <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Enhanced Security:** With Retriever, users do not need to share or store passwords, as the agent sees exactly what the user is logged into <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. Cloud-hosted browsers often require password storage, posing security risks, and may struggle with paywalls or Cloudflare protections <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Multi-Tab Parallel Processing:** The text-based approach enables processing active and background tabs, or multiple tabs at once, which is not possible with vision-based methods as background tabs are not rendered <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This significantly speeds up performance <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Focus on Productivity and Automation:** Retriever prioritizes [[applications_of_ai_in_productivity_and_automation | productivity and automation]] use cases, recognizing that AI excels at automating manual and repetitive tasks <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   **Distributed Subtasks:** For long-horizon tasks, Retriever distributes subtasks as new tabs, reducing failure rates compared to competitors that attempt one long action on a single tab <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **Extensible Function Calling:** Users can define and share function calls, making it much more extensible and scalable than custom third-party integrations <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. This represents an advanced form of [[integration_of_ai_agents_into_existing_infrastructure | integration of AI agents into existing infrastructure]].

### Mission and Future Vision

Retriever's mission is to revolutionize data extraction with transparent and efficient AI <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. The long-term goal is to allow people to collaboratively construct cost-efficient datasets by leveraging the extension to volunteer and extract data from potentially hundreds or thousands of websites (e.g., local government events) <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. This collaborative data set construction represents an exciting new future for [[evaluating_and_optimizing_ai_agents_and_workflows | evaluating and optimizing AI agents and workflows]] and [[integrating_ai_into_natural_workflows | integrating AI into natural workflows]] <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.