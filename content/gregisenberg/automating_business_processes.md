---
title: Automating business processes
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gum Loop is a leading company in [[ai_agents_for_business_automation | AI agent]] and [[ai_agents_in_business_automation | AI automation]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The software allows users to [[automating_manual_processes_with_ai | automate]] tasks typically performed by a junior employee <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This technology is applicable for businesses ranging from the largest corporations to a solo entrepreneur <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The primary goal is to empower users to [[using_ai_for_business_automation | build powerful AI workflows]] and deploy them to automate more aspects of their business <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## How Gum Loop Automates

At its core, a Gum Loop workflow is a series of interconnected steps where data is passed from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This allows for the creation of powerful [[ai_agents_in_business_automation | AI-powered workflows]] that connect directly with user data <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

Key components enabling automation include:
*   **Integrations** Gum Loop integrates with various services like Gmail, Slack, Airtable, Outlook, Notion, and Reddit to pull and process data <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **AI Steps** The power of Gum Loop comes from connecting data with AI steps. These steps are powered by Large Language Models (LLMs) and include functionalities like:
    *   Asking AI questions (similar to ChatGPT) <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   Data extraction based on specified schemas <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   Categorization <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Summarization <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Scoring <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Video and image analysis <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Subflows** These are entirely separate, reusable workflows that can be used as nodes within a larger workflow, similar to functions in programming. This allows for clean, extensible, and sharable logic <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Webhooks** Any Gum Loop workflow can be treated like an API and triggered via a webhook from an external product or event <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Loop Mode** This feature enables running automations at massive scale, processing thousands of events concurrently by looping a workflow over a list of inputs <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Gum Loop handles the infrastructure and rate limits <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   **Scheduled Runs** Workflows can be scheduled to run at specific times, even with natural language descriptions <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.
*   **Custom Nodes** Users can build their own integrations by providing API documentation, allowing for connection to internal data or unsupported third-party services <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. AI assists in writing the necessary code <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.
*   **Interfaces** For non-technical team members, Gum Loop allows the creation of simple, drag-and-drop user interfaces on top of complex workflows, making them easy to use without understanding the underlying logic <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.
*   **Chrome Extension** Workflows can be accessible via a Chrome extension, allowing them to scrape content, screenshot, and perform actions directly from a web page <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>.

## Examples of Business Process Automation

### Automated Lead Qualification and Outreach
One of the earliest revenue-generating workflows at Gum Loop involved automating lead qualification. This process replaces a manual workflow where an employee would:
1.  Wait for new product sign-ups <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
2.  Research the signer's company and background by Googling their email <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
3.  Determine if they are a high-value lead (e.g., enterprise target) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
4.  Draft a personalized email <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

The automated workflow operates via a webhook, triggering when a user creates an account <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>:
1.  Takes the user's email as input <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  A subflow extracts the domain, scrapes their website, and summarizes their company activities using AI (e.g., Claude 3 Haiku) <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
3.  AI extracts the company name to avoid generic information <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
4.  Enrichment services gather data like industry, revenue, country, LinkedIn URL, web traffic, and employee count <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
5.  All data is formatted for readability <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
6.  A notification is sent to the company Slack with the enriched lead information <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
7.  An outbound email draft is created in the sales team's Gmail inbox for review and sending <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

This workflow takes seconds to run, dramatically reducing manual effort and enabling focused outreach <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

### [[automating_marketing_tasks_using_ai | AI Content Generation]] from Podcasts
A workflow was demonstrated to convert a YouTube podcast link into a blog post automatically:
1.  Takes a YouTube link as input <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
2.  A subflow gets the video transcript <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
3.  AI (e.g., O1 model) digests the transcript, removing fluff and providing informative content <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
4.  Another AI step writes the blog post from a specific perspective, including a TLDR and avoiding jargon <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
5.  The content is formatted into HTML, with AI exceptional at structuring titles, sections, and bolding <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
6.  The workflow extracts a short, snappy title from the podcast's opening content <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
7.  The video's thumbnail is retrieved <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
8.  The complete blog post is published to a CMS (e.g., Ghost), including the embedded video and social links <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

This process enables repurposing existing content for SEO and lead generation on autopilot <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. The content can be directed to Shopify, Webflow, Google Docs, Notion, or other platforms simply by swapping the last step <a class="yt-timestamp" data-t="00:30:32">[00:30:32]</a>.

### Daily Schedule and Meeting Preparation
This workflow provides a daily briefing for meetings:
1.  Scheduled to run every morning <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.
2.  Reads from Google Calendar for the day's events <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.
3.  Researches every person on the attendee list, finding their company, revenue, and web traffic <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.
4.  Feeds all research into an AI prompt asking for an explanation of who is being met and why they might be important <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>.
5.  Another AI prompt creates a concise 3-4 point TLDR for quick review on a phone <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.
6.  A more thorough email report is also sent <a class="yt-timestamp" data-t="00:31:11">[00:31:11]</a>.

### Competitor Ad Analysis
A marketing workflow for competitor analysis:
1.  Scrapes a competitor's Facebook ads (including Instagram and WhatsApp) <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
2.  In Loop mode, Gemini watches each video ad and analyzes its image, providing an ad-by-ad analysis of the company's objectives <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
3.  All analyses are fed into a large O1 prompt, instructing it to act as an expert in ad analysis <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
4.  The AI generates an overall analysis of the competitor's ad strategy, focusing on what they are trying to convey <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.
5.  The analysis is formatted in HTML and sent to management via email on a scheduled basis (e.g., daily or weekly) <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
This acts as a junior ad assistant, saving significant time compared to manual research <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.

### LinkedIn Profile Research for Recruitment
A Chrome extension-based workflow for recruiters:
1.  When activated on a LinkedIn profile, it scrapes the entire screen content <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
2.  Extracts key information like name, title, company, university, and location <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
3.  Summarizes the person's background, highlighting properties important for a candidate (e.g., founding engineer, founder experience) <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
4.  Finds their Twitter and GitHub profiles by searching Google and using AI to pick the most likely social links <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
5.  Dumps all data into a Google Sheet for candidate tracking <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
6.  Pings the team on Slack about the new profile <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
7.  Finds the candidate's email using services like Apollo <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.
8.  Engineers a basic recruitment message, which can be highly customized with company context and example emails <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
9.  Puts the drafted email into the founder's inbox for review and sending <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.

This allows any team member to contribute to recruitment by identifying candidates, with the automation handling the research and initial outreach drafting <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>.

### Niche Outreach for Service Businesses
For a hotelier service company, a workflow was built to:
1.  Scrape a niche directory of hotels <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>.
2.  With a single click, draft personalized emails to each hotel, mentioning their ranking (e.g., "You're ranking third out of 50, we can make you number one") <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>.
This automates hours of personalized outbound sales efforts in seconds <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>.

## Benefits of Automating Business Processes

[[automating_job_responsibilities_with_ai | Automating job responsibilities]] and processes provides significant advantages:
*   **Time-Saving** Automations save significant time by handling repetitive and manual tasks <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.
*   **Efficiency** Businesses become more efficient by automating core processes <a class="yt-timestamp" data-t="00:40:18">[00:40:18]</a>.
*   **Unfair Advantage** [[using_ai_for_business_automation | Implementing AI and automation]] creates a competitive "unfair advantage" in the market <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Scalability** Workflows can run at massive scale, processing thousands of events concurrently <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Cost Reduction** Automation significantly reduces operational costs, especially compared to human labor <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>. For example, a single ad analysis email might cost around $1.62 in credits, vastly less than an hour of a junior employee's time <a class="yt-timestamp" data-t="00:29:59">[00:29:59]</a>.
*   **Higher Quality Results** By breaking down complex tasks into bite-sized AI steps, models listen better and produce much higher quality results <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
*   **Focus on High-Leverage Tasks** Automation allows founders and executive teams to focus on high-leverage activities that truly move the needle for the business <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>.
*   **Empowerment** Giving individuals the tools to solve their own problems directly leads to hyper-customized solutions that work out of the box <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.
*   **Consistency and Personalization** Automated processes, such as email generation, can be highly data-enriched and personalized consistently, which might be difficult for humans to maintain at scale <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>.

## Approach to Automation

The key to identifying tasks for automation is to look for anything that can be described as a list of sequential steps, similar to instructions given to an intern <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. If you can list it, you can 100% automate it <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>.

Even large, "tech-forward" companies often operate with a surprising amount of manual processes <a class="yt-timestamp" data-t="00:38:12">[00:38:12]</a>. A useful exercise for any business is to write down all manual tasks and consider how they can be automated <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.

The future of [[building_automated_businesses_with_ai | building automated businesses]] involves sharing and even selling useful tooling through marketplaces <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. The ultimate goal is that understanding a problem should be the only prerequisite to solving it; users shouldn't need an engineering degree to implement powerful automation <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

Many users are already [[building_a_saas_business_using_ai_and_automation | building SaaS products]] on top of Gum Loop using webhooks, creating private internal dashboards or public services <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.

For those interested in exploring [[automated_agency_and_service_businesses_using_ai_tools | automated agency and service businesses]], Gum Loop offers a free sign-up with no credit card required and provides 1,000 free credits upon completing the tutorial <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.