---
title: Creating AIpowered automation workflows
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 
This article discusses **creating AI-powered automation workflows** using Gumloop, a software designed to [[automating_business_workflows_with_ai | automate tasks]] typically performed by a junior employee <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The platform recently raised $9 million and is considered one of the leading AI agent and [[aipowered_workflow_and_task_management | AI automation]] companies <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Gumloop: An Overview
Gumloop allows users to [[building_aidriven_workflows_for_business_ideas | build powerful AI workflows]] and deploy them to manage and process data efficiently <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. These workflows are structured as a series of connected steps, passing data from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The platform is often compared to [[nocode_ai_tools_for_workflow_automation | no-code automation tools]] like Zapier and Make due to its similar integrations <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Core Components
1.  **Nodes**: These are individual steps in a workflow.
    *   **Integrations**: Gumloop offers integrations with various platforms, allowing users to pull data from sources like Slack, Airtable, Outlook, Notion, Reddit, and Gmail <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   **AI Steps**: The true power of Gumloop comes from connecting data with AI steps, all powered by Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
        *   **Ask AI**: Similar to asking a question to ChatGPT, but it supports various models, including Open AI models and those deployed on Azure <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
        *   **Nuanced AI Tooling**: Beyond basic questions, Gumloop offers specific AI actions:
            *   **Data Extraction**: Specify a schema (e.g., amount, date from a receipt) for AI to extract structured information <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
            *   **Categorization** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
            *   **Summarization** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
            *   **Scoring** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
            *   **Video and Image Analysis** <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
2.  **Connecting Data**: Data flows between nodes, allowing for complex [[aipowered_workflow_and_task_management | AI-powered workflows]] <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Key Features and Workflow Examples

### 1. Automated Lead Enrichment
This workflow automates the process of researching and engaging with new sign-ups <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Trigger**: Activated via a webhook when a user creates an account, passing their email to the workflow <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Subflows**: An "entirely separate workflow used as a node" that handles the research <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. It functions like a reusable, extensible function <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   Extracts the domain from the email <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Scrapes the company's website and summarizes its activities using Claude 3 Hau <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   Extracts the company name <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   Uses enrichment services to gather data like industry, revenue, country, LinkedIn URL, monthly web traffic, total funding, and number of employees <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Output**: The collected information is formatted for readability and sent as a notification to the company's Slack <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. An outbound email, personalized with the research, is drafted in the user's Gmail inbox for review <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Benefits**: This workflow drastically reduces manual research time, allowing for rapid, personalized outreach to high-value leads <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. It can be extended to include more research, CRM enrichment, or other actions <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### 2. AI Content Generation (Podcast to Blog Post)
This workflow can [[automating_content_creation_with_ai | automatically generate a blog post]] from a YouTube podcast link <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Input**: A YouTube video link <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Subflow**: Extracts the transcript from the YouTube video <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. It can also use a Gemini node for speech-to-text or direct video analysis <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **AI Processing**:
    *   Uses O1 to digest the transcript, removing "fluff" and providing concise, informative content <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Breaking down prompts into bite-size steps ensures higher quality results <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
    *   Generates a blog post from the digest, adopting a specific perspective (e.g., Greg's), including a TLDR, and avoiding jargon <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   Formats the content in HTML, automatically creating headers and bolding text <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
    *   Extracts a short, snappy title from the podcast's opening using an "extract data" node <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
    *   Automatically generates a thumbnail link <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Output**: The generated blog post is published live on a CMS like Ghost <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>, with the original video embedded and social links included <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. The content can also be routed to Shopify, Webflow, Google Docs, or Notion <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>.
*   **Loop Mode**: This feature allows the workflow to be run at massive scale, processing thousands of YouTube links concurrently from a Google Sheet <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. Gumloop handles the infrastructure and rate limits <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   **Benefits**: Repurposes existing content for SEO, driving free visits, sign-ups, and leads on autopilot <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

### 3. Competitor Ad Analysis
This workflow provides regular insights into competitors' advertising strategies <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   **Process**:
    *   Scrapes competitor's Facebook ads (including Instagram and WhatsApp ads) <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
    *   Feeds ads into a subflow wrapped in an "AI shield" to skip errors <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
    *   Gemini watches video ads and analyzes images, providing an ad-by-ad analysis <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
    *   All analyses are fed into a large O1 prompt, which acts as an expert in ad analysis, generating an overall analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
    *   The analysis is formatted in HTML and sent to management via email <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Scheduling**: Can be scheduled to run daily or weekly <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **Scalability**: Can analyze multiple competitors simultaneously if used as a subflow <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.
*   **Cost**: Significantly cheaper than hiring a human, costing approximately $1.62 per email with standard pricing, and even less if users provide their own API keys <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.

### 4. Daily Calendar Summary
This workflow provides a personalized daily briefing based on one's Google Calendar <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
*   **Process**:
    *   Reads Google Calendar events <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
    *   Researches every meeting attendee, gathering information like their company, revenue, and monthly web traffic to gauge potential customer value <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
    *   An AI prompt summarizes who will be met, why they might be important, and what information the user cares about <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
    *   Another AI prompt creates a TLDR (three or four-point summary) for quick review on a phone <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>, along with a more thorough email report <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>.
*   **Scheduling**: Workflows can be scheduled using natural language (e.g., "every second day of every 4th month at 9:00 a.m.") <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.

### 5. LinkedIn Profile Researcher
This workflow automates the process of researching potential recruitment candidates <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.
*   **Trigger**: Initiated via a Chrome extension, which scrapes the entire content of a LinkedIn profile <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
*   **Process**:
    *   Extracts key information: name, title, company, university, and location <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
    *   Summarizes the person's background, highlighting notable details relevant to a candidate's profile (e.g., founding engineer, founder experience) <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
    *   Finds Twitter and GitHub profiles by Googling their name and using AI to identify likely social media links <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
    *   Dumps all data into a Google Sheet for candidate tracking <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
    *   Pings the team on Slack to encourage adding the candidate on LinkedIn <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
    *   Finds the candidate's email using Apollo <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.
    *   Drafts a basic outreach message in the user's inbox <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
*   **Benefits**: Allows team members, even interns, to identify interesting candidates and initiate personalized outreach from a founder's inbox, streamlining recruitment efforts <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>.

## Enhancing Workflow Creation and Accessibility

### User Interfaces (UIs)
Gumloop allows users to build simple, intuitive interfaces on top of complex workflows using a drag-and-drop UI builder <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. This simplifies usage for co-workers who don't need to understand the underlying flowchart, making workflows accessible to a wider audience <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

### Custom Nodes
This feature enables users to build their own integrations for third-party services not natively supported or for internal endpoints <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.
*   Users can paste API documentation into the custom node builder <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.
*   AI assists in generating the code for the integration, inferring inputs and outputs, and even adding comments <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.
*   Custom nodes are accessible to everyone in a workspace, facilitating team collaboration <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.

### Chrome Extension
Gumloop offers a Chrome extension that allows workflows to be triggered directly from the browser <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. This enables seamless scraping of screen content (e.g., LinkedIn profiles) and other actions, integrating workflows directly into a user's browsing experience <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>. When combined with custom node building, it allows for the creation of infinitely powerful no-code Chrome extensions <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.

## Conclusion
[[Utilizing_AI_for_scaling_and_automation | Automating workflows with AI]] using tools like Gumloop provides a significant [[using_ai_for_business_automation | unfair advantage for businesses]] of all sizes, from solo entrepreneurs to large enterprises <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a> <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. By identifying repetitive manual tasks and building automated, AI-powered solutions, companies can save time, boost sales, and focus on high-leverage activities <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a> <a class="yt-timestamp" data-t="00:40:09">[00:40:09]</a>. Gumloop aims to make this process accessible, allowing individuals to solve their own problems without needing extensive engineering knowledge <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.