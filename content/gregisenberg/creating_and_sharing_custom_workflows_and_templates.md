---
title: Creating and sharing custom workflows and templates
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gumloop is an AI agent and automation company that allows users to [[automating_workflows_and_integrations_with_zapier | automate workflows]] that mimic tasks typically performed by a junior employee <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It's designed for businesses of all sizes, from solo entrepreneurs to the largest companies <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The platform emphasizes building powerful AI workflows and deploying usable tools <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Building Workflows

A Gumloop workflow is a series of connected steps where data is passed from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Users start with an empty canvas and add nodes <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Key Components
*   **Integrations**: Gumloop offers integrations with various platforms like Slack, Airtable, Outlook, Notion, and Reddit, similar to other no-code automation tools like Zapier and Make <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **AI Steps**: The core power comes from connecting data with AI steps <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   **Ask AI**: A basic node similar to asking ChatGPT a question, but it supports various LLM models, including plugging in custom Azure-deployed models <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   **Nuanced AI Tooling**: Beyond basic questions, Gumloop offers specific AI actions such as data extraction (e.g., from receipts by specifying a schema), categorization, summarization, scoring, and video/image analysis <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Connecting Nodes**: Data flows are connected by linking nodes <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This allows for building complex AI-powered products that would typically require an engineer <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Subflows**: These are entire separate workflows used as a node within a larger workflow, providing reusability, cleanliness, and extensibility, similar to functions in programming <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. They can be shared with coworkers <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Workflow Execution
*   **Manual Runs**: Any workflow can be run manually, providing a step-by-step breakdown with viewable inputs and outputs <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   **API Triggers (Webhooks)**: Workflows can be treated as APIs and triggered by events from external products via webhooks <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This enables integration with websites and other platforms, potentially for building SaaS products <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.
*   **Scheduled Runs**: Workflows can be scheduled using natural language (e.g., "every Friday morning at 9:00 a.m. PST") <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **Loop Mode**: For large-scale operations, loop mode allows a workflow to run thousands of events concurrently (e.g., processing a thousand YouTube links), with Gumloop handling the underlying infrastructure and rate limits <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

### Custom Nodes
Users can build their own integrations (custom nodes) for internal data or unsupported third-party services <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. This is done by pasting API documentation into a custom node builder, and AI understands the context to generate the integration <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>. These custom nodes are accessible to everyone in a user's workspace <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.

## Example Workflows

### 1. [[creating_and_managing_custom_signup_flows_and_automations | Automated Lead Qualification and Outreach]]
This workflow, used by Gumloop in its early YC days, automates the process of researching new sign-ups and drafting personalized outreach emails <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Trigger**: A new user signs up for the product (via webhook) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **Process**:
    *   Takes the user's email <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   A subflow researches the company by extracting the domain, scraping the website, and summarizing their operations using AI <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   It extracts the company name (avoiding imprecise information from other services) <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   Enrichment services gather data like industry, revenue, country, LinkedIn URL, web traffic, and funding <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   This data is formatted into a readable notification <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   **Output**:
    *   Sends a detailed ping to the company Slack within 5 seconds of signup <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
    *   Drafts an outbound email in the user's Gmail inbox for review before sending <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### 2. [[workflow_automation_for_content_marketing | Content Creation Frameworks]]
This workflow generates blog posts from YouTube podcast links, enabling efficient content repurposing <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Trigger**: User pastes a YouTube link <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Process**:
    *   A subflow gets the transcript from the YouTube video <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
    *   It uses AI (specifically O1 for its critical thinking with longer content) to create a concise, informative digest, removing fluff <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
    *   Another AI step drafts the blog post content from the digest, incorporating specific instructions like writing in a particular perspective, including a TLDR, and avoiding jargon <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   The content is formatted into HTML by AI, which excels at structuring headers and sections <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
    *   An AI data extraction node picks a short, snappy title from the podcast's opening <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
    *   The video thumbnail is retrieved <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Output**:
    *   Publishes a blog post to a CMS (e.g., Ghost), including a TLDR, detailed points, embedded video, and links to relevant socials <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
    *   This can be looped over thousands of links by connecting to a Google Sheet and running in loop mode <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

### 3. [[automating_marketing_workflows | Competitor Ad Analysis]]
This workflow automates the daily or weekly competitor analysis for marketing teams <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   **Trigger**: Can be scheduled (e.g., every morning or Friday morning) <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **Process**:
    *   Scrapes a competitor's Facebook ads (including Instagram and WhatsApp ads) <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
    *   Each ad is fed into a subflow that uses Gemini to analyze the video and image content, providing an analysis of the company's ad objectives <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
    *   All individual ad analyses are compiled into a large O1 prompt that acts as an expert in ad analysis, generating an overall analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
    *   The analysis is formatted in HTML <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Output**:
    *   Sends an email to management with a beautifully formatted analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
    *   This workflow can be extended to analyze multiple competitors by using it as a subflow <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.

### 4. Daily Meeting Briefing
This workflow provides a daily text and email summary of calendar events and meeting attendees <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
*   **Trigger**: Scheduled every morning at 9:00 a.m. <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
*   **Process**:
    *   Reads the user's Google Calendar for the day <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
    *   Researches every person the user is meeting, including finding their company, revenue, and monthly web traffic <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
    *   Feeds all research into an AI prompt to explain who the user is meeting and why they are important <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
    *   Another AI prompt creates a short TLDR for quick phone viewing <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>.
*   **Output**:
    *   Sends a text message and a more thorough email report <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>.

### 5. LinkedIn Profile Researcher (Chrome Extension)
This workflow allows users to research LinkedIn profiles directly from their browser <a class="yt-timestamp" data-t="00:34:35">[00:34:35]</a>.
*   **Trigger**: Starts with a Chrome extension node, allowing it to be accessed via the Gumloop Chrome extension <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>.
*   **Process**:
    *   Takes the entire content of the LinkedIn profile screen (or can screenshot) <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
    *   Extracts key information like name, title, company, university, and location <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
    *   Summarizes the person's background, highlighting notable details important for recruitment <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
    *   Finds Twitter and GitHub profiles by searching Google and using AI to pick the most likely social media links <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
    *   Finds the person's email using Apollo <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.
    *   Engineers a basic outreach message <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
*   **Output**:
    *   Dumps all collected data into a Google Sheet for candidate tracking <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
    *   Pings the team on Slack to add the candidate on LinkedIn <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
    *   Puts a drafted email in the user's inbox for review <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.

## Sharing and Collaboration

### Templates and Marketplace
Gumloop offers a template directory and plans to launch a marketplace where users can publish and even sell their workflows <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This allows users to clone and adapt existing workflows, fostering a community of shared tooling <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The goal is for anyone to solve a problem if they understand it, without needing an engineering degree <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

### Gumloop Interfaces
To make complex workflows accessible to non-technical team members, Gumloop allows users to create simple, user-friendly interfaces on top of their workflows <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. These interfaces simplify inputs and execution, hiding the underlying flowchart complexity <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.

### Chrome Extension
Workflows starting with a Chrome extension node can be accessed and triggered directly from the Gumloop Chrome extension, allowing for seamless integration with browser-based tasks like research or data scraping <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. This enables the creation of "infinitely powerful no-code Chrome extensions" <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>.

## The Philosophy of Automation
The key to identifying what to automate is to consider any task that can be broken down into a list of steps, similar to instructions given to an intern <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. Automating repetitive tasks frees up time for high-leverage activities and can provide an "unfair advantage" in business <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. Gumloop aims to empower non-technical roles like SDRs, marketers, or growth specialists to build precise, custom solutions without needing to translate their needs to an engineering team <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.