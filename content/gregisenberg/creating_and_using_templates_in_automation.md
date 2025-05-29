---
title: Creating and using templates in automation
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gum Loop is an AI agent and [[ai_automation_tools_for_workflows | AI automation]] company that enables users to [[automating_business_tasks_with_ai | automate what a junior employee does]] within a business <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This software allows businesses of any size, from solo entrepreneurs to the biggest companies, to automate more tasks <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Understanding Gum Loop Workflows

A Gum Loop workflow is a series of connected steps where data is passed from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This system allows users to build powerful [[building_simple_workflows_for_marketing_automation | AI powered workflows]] that connect directly with their data <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

The platform offers various integrations, similar to [[using_zapier_for_automation_in_web_development | Zapier]] and Make, allowing data to be pulled from services like Slack, Airtable, Outlook, Notion, and Reddit <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The true power emerges when this data is combined with [[ai_automation_tools_for_workflows | AI steps]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Gum Loop's [[ai_tools_and_design_automation | AI tooling]] includes:
*   **Ask AI:** Similar to asking ChatGPT, supporting various LLMs, including custom models deployed on Azure <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Data Extraction:** Specify a schema (e.g., amount, date from a receipt) for AI to extract structured information <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Categorization, Summarization, Scoring:** General [[ai_automation_tools_for_workflows | AI actions]] on data <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Video and Image Analysis:** Leverage LLMs for multimedia analysis <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

By combining these LLM steps with data, users can create fully [[automating_business_tasks_with_ai | AI powered products]] that would typically require an engineer to build <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## The Role of Templates and Reusability

While users can build workflows from scratch on an empty canvas <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, Gum Loop emphasizes reusability and sharing, particularly through [[creating_and_utilizing_templates_in_software_development | templates]].

### Existing Templates and Future Marketplace
Gum Loop features a template directory <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a> and plans to launch a marketplace where users can publish and sell their workflows as [[creating_and_utilizing_templates_in_software_development | templates]] <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This allows users to clone and benefit from complex workflows built by others, for a small fee if sold <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. The long-term vision is for the product's intuitive design to reduce the need for templates, allowing users to build amazing workflows in minutes <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

### Subflows: Reusable Functions
A key feature enabling reusability is "subflows" <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. A subflow is an entirely separate workflow used as a node within another workflow <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This provides the power of a function for programmers: it's reusable, clean, and extensible, meaning co-workers can import and benefit from shared work <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### Custom Nodes: Building Your Own Integrations
Gum Loop allows users to build their own integrations through "custom nodes" <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. By pasting API documentation into the custom node builder, users can generate a functional integration node that can be shared across a workspace <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>. The platform uses AI to understand the context and build the node <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. This empowers non-technical users to create complex tools like Twitter scrapers or integrations with internal data <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>. In the future, users might simply describe the desired integration, and AI will automatically build and test it <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.

## Practical Examples of Automated Workflows

### 1. Lead Enrichment and Outreach
Max demonstrated a [[building_simple_workflows_for_marketing_automation | standard workflow]] used in Gum Loop's early days to generate revenue <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This workflow automates the process of researching new sign-ups and sending personalized emails:
*   **Trigger:** A user signs up (via webhook) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Subflow (Research):** Takes the user's email, extracts the domain, scrapes their website, summarizes their company using Claude 3 Haiku, extracts the company name, and uses enrichment services (e.g., ZoomInfo) to get industry, revenue, country, and other details <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Notifications:** Formats the gathered data and sends a readable notification to the company Slack <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Email Draft:** Drafts a personalized outbound email in the user's Gmail inbox, which can be reviewed and sent later <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

This workflow, built simply, allowed for efficient lead qualification and outreach, turning sign-ups into demo calls <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### 2. Podcast to Blog Post Automation
This workflow takes a YouTube link and generates a blog post from the content <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Input:** A YouTube link <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Subflow (Content Generation):**
    *   Gets the video transcript using Gum Loop's YouTube node or Gemini's speech-to-text <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
    *   Asks the O1 model to digest and remove fluff from the transcript <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   Prompts O1 to write a blog post from the speaker's perspective, including a TLDR and avoiding jargon <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   Formats the content in HTML for easy publishing <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
    *   Extracts a short, snappy title from the podcast's opening using a data extraction node <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
*   **Output:** Publishes the blog post to a CMS (e.g., Ghost), embeds the video, and links socials <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
This workflow exemplifies "loop mode," allowing a single workflow to be run thousands of times over multiple inputs (e.g., YouTube links from a Google Sheet) <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. This enables [[ai_automation_tools_for_workflows | AI content generation]] by repurposing existing work, leading to free visits, sign-ups, and leads through SEO <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

### 3. Competitor Ad Analysis
This workflow provides a weekly analysis of a competitor's ad strategy <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   **Scraping:** Scrapes a competitor's Facebook ads <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **Subflow (Analysis):** Uses Gemini to analyze video ads and images, coming up with an analysis of each ad's objective <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. This runs in loop mode for multiple ads <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.
*   **Overall Strategy:** Feeds all individual ad analyses into a large O1 prompt, asking it to create an overall analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
*   **Output:** Formats the analysis in HTML and sends it to management via email on a scheduled basis (e.g., every Friday morning) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
This workflow acts like a junior ad assistant, providing comprehensive insights at a fraction of the cost of a human employee <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.

### 4. Daily Calendar Briefing
This personal workflow provides a daily overview of meetings <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
*   **Google Calendar Reader:** Specifies start and end times to read calendar events <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>.
*   **Attendee Research:** Researches every person on the attendee list, gathering company and revenue data <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
*   **AI Prompt:** Feeds all data into a prompt that explains who will be met, why they are important, and focuses on key information <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
*   **TLDR and Email:** Creates a three-to-four point TLDR for quick phone viewing and a more thorough email report <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.

### 5. LinkedIn Profile Researcher (Chrome Extension)
This workflow automates the candidate recruitment process <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.
*   **Trigger:** Initiated via a Gum Loop Chrome extension that scrapes the entire content of a LinkedIn profile <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
*   **Data Extraction & Summarization:** Extracts name, title, company, university, location, and summarizes the person's background, highlighting notable details important for recruitment <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
*   **Social Media Discovery:** Finds Twitter and GitHub profiles by searching Google and using AI to pick the most likely socials <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **Output & Outreach:** Dumps data into a Google Sheet for tracking, pings the team on Slack, finds their email via Apollo, and drafts a personalized email in the founder's inbox <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.

## The Power of Automation and Templates

The concept of [[manual_processes_and_opportunities_for_automation | automating business tasks]] is crucial for gaining an unfair advantage and creating superior customer experiences <a class="yt-timestamp" data-t="00:38:48">[00:38:48]</a>. Many companies, even "tech-forward" ones, operate with surprisingly few automations <a class="yt-timestamp" data-t="00:38:12">[00:38:12]</a>. A good exercise is to identify manual, repetitive tasks that can be broken down into steps, as these are prime candidates for automation <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>.

Automation allows founders and executive teams to save time, focusing on high-leverage activities that truly move the needle <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>. By providing individuals the tools to solve their own problems without needing an engineering degree, companies can achieve highly customized and efficient workflows <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.

Gum Loop is free to sign up and use initially, with tutorials offering free credits to explore its capabilities <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Users can also provide their own API keys for services like Apollo or Gemini to reduce Gum Loop credit costs to nearly zero <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.