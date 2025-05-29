---
title: AI Workflow Automation with Gum Loop
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gum Loop is an [[ai_agents_and_automation | AI agent and AI automation]] company that enables users to [[automating_business_processes_with_ai | automate what a junior employee does]] through its software platform <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The company recently raised $9 million <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Max, the co-founder and CEO, explains how Gum Loop allows users to build powerful [[ai_coding_workflow_optimization | AI workflows]] and deploy them <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This capability is relevant for businesses of all sizes, from solo entrepreneurs to the largest companies globally <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## How Gum Loop Workflows Operate

A Gum Loop workflow is a series of connected steps, where data is passed from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The platform provides an empty canvas where users add nodes to build their automations <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Integrations and AI Steps

Gum Loop integrates with many existing platforms, similar to no-code automation tools like Zapier and Make <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Users can pull data from services such as Slack, Airtable, Outlook, Notion, and Reddit <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

The true power of Gum Loop emerges when this data is connected with **AI steps** <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. All AI steps are powered by Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

Available AI actions include:
*   **Ask AI:** Similar to asking ChatGPT, allowing users to plug in various LLM models, including their own deployed models on Azure <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Data Extraction:** Users can specify a schema (e.g., amount, date from a receipt) for AI to extract structured data <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Categorization, Summarization, Scoring** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
*   **Video and Image Analysis** <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>

### Advanced Features

*   **Subflows:** These are entirely separate workflows that can be used as a single node within another workflow <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. They function like reusable programming functions, making workflows cleaner and extensible <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Triggering Workflows:** Workflows can be triggered manually, via webhooks (treating any Gum Loop workflow like an API), or on a scheduled basis <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Loop Mode:** This feature allows workflows to process thousands of events concurrently, handling the underlying infrastructure and rate limits <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **Gum Loop Interfaces:** To simplify workflows for non-technical users, interfaces can be built on top of complex flows <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. These interfaces provide a simple, drag-and-drop UI that hides the underlying complexity <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
*   **Custom Nodes:** Users can build their own integrations by providing API documentation to Gum Loop's custom node builder. The AI understands the context and generates the necessary code, making the integration accessible to all team members in a workspace <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
*   **Chrome Extension:** Workflows can be made accessible through a Chrome extension. This allows the workflow to scrape web page content, screenshot, or perform other actions, feeding the data into the workflow seamlessly <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>.

## Practical Use Cases

Max demonstrates several real-world applications of Gum Loop:

*   **Lead Qualification & Enrichment:** Max used a workflow to automate the process of researching new sign-ups for Gum Loop in its early days <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This workflow:
    *   Takes a user's email via webhook when they create an account <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Extracts the domain, scrapes their website, and summarizes their company using AI (e.g., Claude 3 Haiku) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Extracts the company name and enriches data with industry, revenue, country, LinkedIn URL, web traffic, and employee count using various services <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
    *   Formats the data and sends a notification to the company Slack channel <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   Drafts a personalized outbound email in Max's inbox for review <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
    *   This workflow allowed Max to qualify leads quickly and reach out to high-value prospects <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

*   **Podcast-to-Blog Post Automation:** This workflow takes a YouTube link and generates a blog post <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    *   It pulls the video transcript via a YouTube node <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
    *   Feeds the transcript into an AI model (e.g., O1) to create a concise digest, removing conversational "fluff" <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   Uses another AI prompt to write the blog post, including a TLDR summary, avoiding jargon, and writing from a specified perspective <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   Formats the content in HTML, embeds the video, and links to relevant socials <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
    *   An "extract data" node snips the first thousand words to generate a snappy title <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
    *   The final output is published to a CMS like Ghost <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
    *   This workflow can be looped over thousands of YouTube links for mass content generation <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

*   **Daily Calendar Preparation:** A scheduled workflow provides a daily analysis of meetings <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
    *   It reads Google Calendar, researches every attendee (company, revenue, web traffic), and provides an overview of who is being met and why they might be important <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>.
    *   Creates a brief TLDR for phone viewing and a more thorough email report <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>.

*   **Competitor Ad Analysis:** This workflow analyzes competitor Facebook ads and provides insights to management <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
    *   It scrapes a competitor's active Facebook ads (across Facebook, Instagram, WhatsApp) <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
    *   Uses Gemini to analyze video and image ads, generating an ad-by-ad analysis in loop mode <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
    *   Dumps all analyses into a large O1 prompt asking for an overall competitor ad strategy analysis <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
    *   Formats the analysis in HTML and emails it to management on a scheduled basis (e.g., daily or weekly) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

*   **LinkedIn Profile Researcher (Recruitment):** A Chrome extension-triggered workflow assists with recruiting <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.
    *   It scrapes the content of a LinkedIn profile <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
    *   Extracts key details like name, title, company, university, and location <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
    *   Summarizes the person's background, highlighting properties important to the hiring company (e.g., founding engineer) <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
    *   Finds their Twitter and GitHub profiles <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
    *   Dumps information into a Google Sheet for candidate tracking <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
    *   Pings the team on Slack <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
    *   Finds their email with Apollo and drafts a basic message in the recruiter's inbox <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.

## Benefits of AI Workflow Automation

Max emphasizes that [[automating_business_processes_with_ai | automating business processes with AI]] offers significant advantages:
*   **Cost-Effectiveness:** Automating tasks like competitor ad analysis can be significantly cheaper than hiring a junior employee <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
*   **Unfair Advantage:** Implementing tight, automated systems creates a competitive edge, allowing businesses to save time and focus on high-leverage activities <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Efficiency:** Gum Loop dogfoods its own product, automating most internal business processes, which contributes to its efficiency as a lean startup <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.
*   **Empowerment:** The platform allows semi-technical people at companies to solve their own problems without needing engineering resources, leading to hyper-customized solutions <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.
*   **Enhanced Output:** AI can produce more data-enriched and often more personalized communications at scale than manual processes <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.

## Getting Started with Gum Loop

Users can sign up for Gum Loop for free, with no credit card required to start experimenting <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Completing the initial [[tutorial_on_building_ai_powered_workflows | tutorial]] grants 1,000 free credits <a class="yt-timestamp" data-t="00:42:17">[00:42:17]</a>.

### Cost Structure
Gum Loop uses a credit system for workflow runs <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. Users can also provide their own API keys for services like Apollo or Gemini, which can reduce the credit cost to near zero <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. The cheapest plan currently includes 30,000 credits <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.

### Community and Future
Gum Loop offers a Discord community, with a Slack community under development, where users can ask questions and get help <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a>. In the future, the platform plans to launch a marketplace where users can publish and sell their workflow templates <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The goal is to make the user experience so intuitive that templates become less necessary, allowing users to build amazing workflows in minutes <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.