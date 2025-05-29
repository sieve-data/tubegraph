---
title: Building nocode AI agents
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gumloop is a leading company specializing in [[using_ai_agents_in_software_development | AI agent]] and AI automation software, which recently raised $9 million <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This software can automate tasks typically performed by a junior employee <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, making it relevant for businesses of all sizes, from large corporations to solo entrepreneurs <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. By the end of a demonstration, users should be able to [[orchestrating_and_deploying_ai_agents | build powerful AI workflows and deploy them]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## How Gumloop Workflows Function

A Gumloop workflow is a series of connected steps where data is passed from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This process allows users to build powerful AI-powered workflows that connect directly with their data <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Building a Workflow from Scratch

Users start with an empty canvas and add nodes to it <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Gumloop offers many integrations similar to no-code automation tools like Zapier and Make <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. These integrations allow data to be pulled from sources such as Slack, Airtable, Outlook, Notion, and Reddit <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The true power emerges when this data is connected with AI steps <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### AI Steps

Gumloop includes various AI steps, all powered by large language models (LLMs) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
The most basic AI step is "Ask AI," similar to asking ChatGPT a question, but it supports various models, including user-deployed models on Azure <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

Beyond basic inquiries, Gumloop offers more nuanced AI tooling for tasks such as:
*   **Data extraction:** Users can specify a schema (e.g., amount, date) for AI to extract structured data from content like receipts <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Categorization** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
*   **Summarization** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
*   **Scoring** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
*   **Video and image analysis** <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>

By pairing LLM steps with data, users can create fully AI-powered products that would typically require an engineer to build <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## Example Workflows and Features

### Lead Enrichment and Sales Automation
Gumloop used an internal workflow to generate early revenue for their company <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This workflow automates the process of researching and reaching out to high-value leads after they sign up for the product <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

Key features demonstrated by this workflow:
*   **Webhooks:** Workflows can be triggered via webhooks, allowing them to run in the background based on events in other products (e.g., a user signing up) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Subflows:** Entirely separate workflows can be used as nodes within a larger workflow, similar to functions in programming. This promotes reusability and clean architecture <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. The lead research subflow takes an email, extracts the domain, scrapes the website, summarizes the company using an LLM (e.g., Claude 3 Haiku), extracts the company name, and then uses enrichment services to gather data like industry, revenue, and country <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Automated Communication:** The gathered information is formatted and sent as a readable notification to a company Slack channel <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. It also drafts a personalized outbound email in the user's inbox for review and sending <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Extensibility:** The workflow can be extended to include more research (e.g., using Perplexity, Google searches), or to integrate with CRMs like Airtable <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

This type of automation provides an "unfair advantage" for businesses by creating tight, automatic systems that save time and accelerate sales <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### YouTube to Blog Post Creation (Content Generation)
This workflow takes a YouTube podcast link and automatically writes a blog post about it <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This is an example of [[building_an_ai_content_agent_with_n8n_and_claude | AI content generation]] that repurposes existing hard work <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. The blog post includes a TLDR of main points, detailed explanations, an embedded video, and links to relevant socials <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

Components of the workflow:
1.  **YouTube Node:** Dynamically gets the transcript of the video <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. A Gemini node can also be used for speech-to-text or direct video analysis <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
2.  **Prompt Chaining:** The transcript is first fed into an LLM (e.g., O1) to create a concise, informative digest by removing conversational "fluff" <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. Breaking down prompts into bite-sized steps leads to higher quality results <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
3.  **Blog Post Generation:** A subsequent AI prompt (e.g., using O1 for its long-form critical thinking ability <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>) writes the blog post from the digest, adhering to specified perspectives, including a TLDR, and avoiding jargon <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
4.  **HTML Formatting:** The content is then formatted into HTML by AI, which excels at structuring content with headers, sections, and bolding <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
5.  **Dynamic Title and Thumbnail:** The workflow picks a snappy title by extracting data from the first thousand words of the podcast <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. It also generates a thumbnail link <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
6.  **CMS Integration:** The final blog post content is published to a CMS like Ghost <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. The output destination is fully configurable (e.g., Shopify, Webflow, Google Docs, Notion) <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>.

#### Loop Mode
This workflow, designed for a single YouTube link, can be scaled using "loop mode" <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. By linking it to a Google Sheet with thousands of YouTube links, the workflow can run a thousand times concurrently, with Gumloop handling the infrastructure and rate limits <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. This enables users to generate mass content quickly, leading to potential SEO benefits and free visits, sign-ups, and leads on autopilot <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

### Competitor Ad Analysis
This workflow demonstrates [[integrating_ai_agents_for_competitive_analysis | competitive analysis]] by scraping a competitor's Facebook ads <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.
*   It feeds all active ads into a subflow, where Gemini analyzes each video and image ad, generating an analysis of the company's ad strategy <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.
*   All individual ad analyses are compiled and fed into a large LLM prompt (e.g., O1) for an overall analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
*   The analysis is then formatted in HTML and sent via email to management on a scheduled basis (e.g., daily or weekly) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   Multiple competitors can be analyzed simultaneously by linking this workflow as a subflow <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>. This acts like having a junior ad assistant <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.

### Daily Calendar Summary (Personal Assistant)
An example of [[developing_personal_assistant_ai_agents | a personal assistant AI agent]], this workflow sends a daily text and email summary of the user's entire day <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
*   It reads the Google Calendar, researches every person the user is meeting (company, revenue, web traffic), and feeds this into a prompt <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>.
*   The AI explains who the user will meet, why they might be important, and creates a TLDR summary for quick mobile viewing, followed by a more thorough email report <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
*   Workflows can be scheduled using natural language (e.g., "every second day of every 4th month at 9:00 a.m.") <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.

### LinkedIn Profile Researcher (Recruitment Automation)
This Chrome extension-based workflow automates the process of researching LinkedIn profiles for recruitment <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.
*   It takes the entire content of a LinkedIn profile page <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
*   The workflow extracts key details (name, title, company, university, location), summarizes the person's background, and identifies notable details relevant to a candidate <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
*   It finds their Twitter and GitHub profiles by Googling their name and using AI to pick the most likely social links <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   All data is dumped into a Google Sheet for candidate tracking <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
*   It pings the team on Slack about new profiles <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
*   It finds the candidate's email using Apollo and drafts a basic message, which is saved as a draft in the user's inbox <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.

## Advanced Features

### Interfaces
Gumloop allows users to create simple, user-friendly interfaces on top of complex workflows <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>. This simplifies the user experience, allowing non-technical teammates to use powerful tools without understanding the underlying flowchart <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>. These interfaces are built with a drag-and-drop UI builder <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>.

### Custom Nodes
Users can [[overcoming_coding_challenges_with_ai | build their own integrations]] using the custom node builder <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. By pasting API documentation into the builder, Gumloop's AI can generate the code for a new node that can interact with internal endpoints or unsupported third-party services <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>. These custom nodes are accessible to everyone in the user's workspace <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>. This feature enables semi-technical users to build complex tools like Twitter scrapers or integrations with their development team, essentially [[using_ai_to_build_software_applications | building software applications]] with AI assistance <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.

### Chrome Extension
The Gumloop Chrome extension allows workflows to be initiated directly from a web page <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. Workflows starting with a Chrome extension node can scrape content, screenshot, or perform other actions on the current page <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. This enables infinitely powerful no-code Chrome extensions by combining with the custom node builder <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.

## Benefits of Automation with Gumloop

*   **Efficiency:** Gumloop enables businesses to automate repetitive tasks that can be broken down into a list of steps, freeing up time for high-leverage activities <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>. This makes companies more efficient and helps them focus on engineering, product, and marketing <a class="yt-timestamp" data-t="00:40:18">[00:40:18]</a>.
*   **Accessibility:** By providing tools for non-technical individuals (e.g., SDRs, marketing, growth personnel) to solve their own problems, Gumloop eliminates the "broken telephone" effect often seen when explaining automation needs to engineering teams <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>.
*   **Scalability:** Workflows can be built once and run thousands of times, compounding benefits like free visits and leads <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   **Cost-Effectiveness:** Automating tasks with Gumloop is significantly cheaper than hiring a human employee for the same work <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>. Users can also provide their own API keys for LLMs and other services, further reducing costs on Gumloop <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

> "If you can list it as a a list of steps like for an intern you would hand off a little sticky note being like you do these 15 things in a row and that's the entire workflow then you can 100% automate it" <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>

## Getting Started

Gumloop is free to sign up and use initially, requiring no credit card to play around <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Completing the tutorial grants 1,000 free credits <a class="yt-timestamp" data-t="00:42:17">[00:42:17]</a>. Gumloop also fosters a community via Discord and Slack, where users can ask questions and get help <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a>. A marketplace will soon allow users to publish and sell their templates <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

> "If you're not automating stuff in 2025 like you should be" <a class="yt-timestamp" data-t="00:42:44">[00:42:44]</a>
> "It's a there is like a learning curve in terms of like okay now I understand what I could automate and from that you can just layer on more and more automation" <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>