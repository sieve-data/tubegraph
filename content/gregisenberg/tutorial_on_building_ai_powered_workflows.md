---
title: Tutorial on Building AI Powered Workflows
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

GumLoop is a software company specializing in [[automating_business_processes_with_ai | AI agent]] and [[automating_business_processes_with_ai | AI automation]], having recently raised $9 million <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This platform is designed to automate tasks typically performed by a junior employee <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, making it relevant for businesses of all sizes, from solo entrepreneurs to the largest companies <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. By the end of this tutorial, users should be able to [[building_apps_using_ai_tools | build super powerful AI workflows]] and deploy them <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## What is a GumLoop Workflow?

A GumLoop workflow is a series of interconnected steps that pass data from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This allows users to [[building_apps_using_ai_tools | build powerful AI-powered workflows]] that directly connect with their data <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The interface is described as intuitive, resembling "Lego building blocks" and having a "Figma feel" <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Key Features for Building Workflows

*   **Integrations**: GumLoop offers integrations with various platforms like Slack, AirTable, Outlook, Notion, Reddit, and Gmail <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. These allow pulling data from different sources into your workflow <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **AI Steps**: The core power of GumLoop comes from connecting collected data with AI steps <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   **Ask AI**: Similar to asking ChatGPT, this node can plug and play with various LLMs, including OpenAI models or models deployed on Azure <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   **Nuanced AI Tooling**: Beyond basic questions, GumLoop offers specialized AI steps for data extraction (e.g., amount and date from a receipt) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, categorization, summarization, scoring, and video/image analysis <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Subflows**: An "entirely separate workflow used as a node" <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, subflows function like reusable programming functions. They are clean, extensible, and can be shared <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Triggers**: Workflows can be triggered manually <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, via webhooks (treating any workflow like an API) <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>, or on a scheduled basis using natural language for cron job creation <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **Loop Mode**: This feature allows running automations at scale, processing thousands of events concurrently <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. GumLoop handles the infrastructure and rate limits for these large runs <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   **Custom Nodes**: Users can [[building_apps_using_ai_tools | build their own integrations]] by copying API documentation into the custom node builder. The AI understands the context and generates the necessary code, making it accessible even for semi-technical users <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>. These custom nodes can be shared across a workspace <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.
*   **Chrome Extension**: Workflows can be made accessible directly through a Chrome extension <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. This allows users to trigger workflows that scrape screen content or take screenshots with a single click <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.

## Practical Applications and Workflow Examples

GumLoop facilitates [[automating_business_processes_with_ai | automating business processes with AI]] across various domains:

*   **Lead Enrichment and Outbound Email Automation**:
    *   This workflow monitors new user sign-ups (via webhook) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   A subflow researches the user's company by scraping their website, summarizing their activities, and extracting company details like revenue and industry from enrichment services <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   This enriched data is then sent as a notification to the company's Slack <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   Finally, it drafts a personalized outbound email in the user's Gmail inbox, ready to be sent <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
    *   This automation replaced a manual process of Googling and emailing high-value leads <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

*   **Podcast to Blog Post Automation**:
    *   Takes a YouTube link as input <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    *   A subflow retrieves the podcast transcript via a YouTube node <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
    *   It uses AI (e.g., O1 for longer content) to digest and remove fluff from the transcript <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   Another AI step drafts a blog post in a specified perspective (e.g., "Greg's perspective") with a tldr and without jargon <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   The content is formatted into HTML, with a title extracted by AI and the original video embedded <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
    *   The final blog post is published to a CMS like Ghost <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
    *   This workflow can be looped over thousands of links to generate content at scale, offering free SEO visits and lead generation opportunities <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. The output content can also be directed to Shopify, Webflow, Google Docs, or Notion <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>.

*   **Competitor Ad Analysis**:
    *   Scrapes a competitor's Facebook ads <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
    *   Uses Gemini to analyze each video ad and its images in loop mode, creating an ad-by-ad analysis <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
    *   An O1 prompt summarizes the overall ad strategy across all active ads <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
    *   The analysis is formatted in HTML and sent to management via email on a scheduled basis (e.g., every Friday morning) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
    *   This workflow can be configured through a simple interface, allowing non-technical team members to use it easily <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.

*   **Daily Calendar Analysis**:
    *   Reads Google Calendar events <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
    *   Researches every meeting attendee, including company details, revenue, and web traffic <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
    *   Feeds this information into a prompt to explain who is being met and why they are important <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
    *   Generates a concise "tldr" summary for quick review on a phone <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>.
    *   Provides a more thorough email report <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>.

*   **LinkedIn Profile Researcher for Recruiting**:
    *   Activated via a Chrome extension <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.
    *   Scrapes the entire LinkedIn profile content <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
    *   Extracts key details like name, title, company, university, and location <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
    *   Summarizes the person's background, highlighting notable details relevant to candidate properties <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
    *   Finds their Twitter and GitHub profiles using a subflow that Googles their name and uses AI to select the most likely social links <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
    *   Dumps all data into a Google Sheet for tracking <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
    *   Pings the team on Slack to add the candidate on LinkedIn <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
    *   Finds their email via Apollo and drafts a basic message in the user's inbox <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>.

*   **Niche Outreach**:
    *   Can scrape entire pages (e.g., a directory of hotels) <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>.
    *   Draft personalized emails to each entry based on their positioning (e.g., "You're ranking third out of 50, we could make you number one") <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>.
    *   This [[use_of_ai_agents_and_workflows_in_marketing | automates hours of personalized outbound sales]] in seconds <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>.

### Building Scalable Businesses with AI

GumLoop enables [[building_automated_businesses_with_ai | building automated businesses with AI]] and [[building_businesses_with_ai_tools | building businesses with AI tools]] by allowing users to create their own "Software as a Service" (SaaS) products <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. Workflows can be triggered via API using webhooks, allowing custom forms on websites to initiate complex processes <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>. This means users can [[building_ai_startup_using_ai_tools | build an AI startup using AI tools]] without extensive engineering knowledge <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.

## Tips for Using AI Tools Effectively in Workflows

*   **Break Down Tasks**: When designing prompts for AI, break down complex tasks into "bite-sized steps" <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. This [[sequential_prompting_for_ai_workflows | sequential prompting for AI workflows]] helps the model "listen to you a lot better" and yields higher quality results <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. The quality of subsequent AI steps cascades from previous outputs <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
*   **Understand the Problem**: The only prerequisite to solving a problem should be understanding it, not having an engineering degree <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Identify Manual Processes**: A good exercise is to write down all manual tasks performed in a business and consider how they can be automated <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>. If a task can be listed as a series of steps for an intern, it can be automated <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>.

## GumLoop Platform Details

*   **Templates and Marketplace**: GumLoop plans to launch a marketplace where users can publish and sell their workflow templates <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, [[creating_a_marketplace_for_aidriven_workflows | creating a marketplace for AI-driven workflows]]. This allows users to easily clone and benefit from complex flows built by others <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **UI/UX**: The platform's user interface is designed to be visually appealing and easy to use, resembling "Lego building blocks" and having a "Figma feel" <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This focus on [[tips_for_using_ai_tools_effectively_in_design_workflows | design workflows]] aims to make building complex automations simple <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Cost-Effectiveness**: While GumLoop uses a credit system, users can provide their own API keys for services like Apollo or Gemini, significantly reducing the cost to near zero <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. This makes running workflows at massive scale highly affordable compared to human labor <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
*   **Community**: GumLoop is building a Slack community where users can ask questions and get help from experts <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a>.

## Getting Started

GumLoop is free to sign up and use initially, requiring no credit card to play around <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Completing the tutorial grants 1,000 free credits <a class="yt-timestamp" data-t="00:42:17">[00:42:17]</a>. Users are encouraged to "mess around" with the tools to learn what works best for them <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.