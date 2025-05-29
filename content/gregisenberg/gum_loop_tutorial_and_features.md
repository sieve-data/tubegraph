---
title: Gum Loop tutorial and features
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gum Loop is an AI agent and AI automation company that recently raised $9 million <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It provides software designed to automate tasks typically performed by a junior employee <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The platform is designed to be applicable for businesses of all sizes, from solo entrepreneurs to the largest companies in the world <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Core Concept: Building AI Workflows

A Gum Loop workflow is a series of interconnected steps where data is passed from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This allows users to build powerful AI-powered workflows that directly interact with their data <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

To begin, users are presented with an empty canvas where they can add nodes <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Gum Loop offers integrations similar to no-code automation tools like Zapier and Make, allowing data to be pulled from services such as Slack, AirTable, Outlook, Notion, and Reddit <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

The true power of Gum Loop emerges when this data is connected with AI steps <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Key Features

### AI Steps
Gum Loop offers various AI steps, all powered by Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:
*   **Ask AI**: Similar to asking a question to ChatGPT, but it supports various models beyond OpenAI, including Azure-deployed models <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Data Extraction**: Allows users to specify a schema (e.g., amount, date from a receipt) for AI to extract structured data <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Categorization, Summarization, Scoring**: Specialized AI tasks <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Video and Image Analysis**: Enables AI to process visual content <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

Connecting these LLM steps with user data results in fully AI-powered products that would normally require an engineer to build <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Subflows
Subflows allow an entire workflow to be used as a single node within another workflow <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This feature provides the reusability, cleanliness, and extensibility of a function in programming <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### Webhooks and API Triggers
Any Gum Loop workflow can be treated like an API and triggered via a webhook from an external product or event <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This enables seamless integration with existing systems <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Loop Mode
Loop mode allows for thousands of events to be processed concurrently <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. Users can kick off a run that loops their automation over massive scales, with Gum Loop handling the underlying infrastructure and rate limits <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. For example, a workflow designed for a single YouTube link can be looped over a thousand YouTube links by connecting it to a Google Sheet <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

### Gum Loop Interfaces
This feature simplifies complex workflows by allowing users to create a simple, impossible-to-mess-up user interface on top of a flow <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. This means co-workers can utilize powerful workflows without understanding the underlying flowchart logic <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. The interface builder offers a drag-and-drop experience <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.

### Custom Nodes
Custom nodes allow users to build their own integrations, even for internal data endpoints or unsupported third-party services <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>. By pasting API documentation into the custom node builder, AI can generate the necessary code, and the custom node becomes accessible to everyone in the workspace <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>. This enables semi-technical users to build complex tools like Twitter scrapers or integrations with their development team without being a developer <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.

### Chrome Extension
The Gum Loop Chrome extension allows workflows to be initiated directly from a web browser <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. It can scrape screen content, take screenshots, and perform other actions, feeding the data into a workflow <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>. This allows users to experience the value of a powerful tool without needing to understand its underlying complexity <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.

## Practical Applications and Use Cases

*   **Lead Qualification and Outbound Email Drafting**: Gum Loop was used in the early days of Y Combinator to automate lead research. When a user signed up, their email was passed into a workflow that:
    *   Extracted the company domain <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Scraped and summarized their website using Claude 3 Haiku <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   Extracted the company name and enriched it with industry, revenue, and country data using other services <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   Sent a Slack notification to the team with enriched company details <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   Drafted a personalized outbound email in Gmail for the founder to review and send <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
    This workflow emulated a manual process that generated significant early revenue <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

*   **YouTube Video to Blog Post Conversion**: A workflow can take a YouTube link as input and generate a blog post on a CMS (like Ghost) <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This process involves:
    *   Getting the video transcript via a YouTube node or using a [[gemini_models_demo | Gemini]] node for speech-to-text or direct video analysis <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
    *   Feeding the transcript into an AI (e.g., O1 model for longer content) to create a concise digest, removing fluff <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   Asking AI to write the blog post from a specific perspective, including a TLDR and avoiding jargon <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   Formatting the output in HTML with headers and sections <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
    *   Automatically picking a short, snappy title using an extract data node <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
    *   Embedding the video and linking to the original source <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
    This repurposes existing content for SEO and lead generation <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.

*   **Competitor Ad Analysis**: This workflow automates competitive intelligence for marketing teams <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>:
    *   Scrapes a competitor's active Facebook, Instagram, and WhatsApp ads <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
    *   Uses [[gemini_models_demo | Gemini]] to watch and analyze each video ad, providing an ad-by-ad analysis in loop mode <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
    *   Feeds all individual ad analyses into a large O1 prompt for an overall analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
    *   Formats the analysis in HTML and sends a scheduled email report to management <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
    This effectively acts as a "junior ad assistant" <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.

*   **Daily Calendar Summary and Meeting Prep**: A personal automation that:
    *   Reads the user's Google Calendar for the day <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
    *   Researches every person the user is meeting, finding company, revenue, and web traffic <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.
    *   Feeds this information into an AI prompt to explain who is being met, why they are important, and what the user cares about <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
    *   Generates a TLDR summary for quick mobile viewing and a more thorough email report <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>.
    This workflow can be scheduled with natural language <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.

*   **LinkedIn Profile Researcher for Recruitment**: Activated via a Chrome extension, this workflow automates recruiter tasks <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>:
    *   Scrapes the entire content of a LinkedIn profile <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
    *   Extracts name, title, company, university, and location <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
    *   Summarizes the person's background, highlighting notable details relevant to a candidate <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
    *   Finds their Twitter and GitHub profiles by using AI to look at Google search results <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
    *   Dumps all data into a Google Sheet for tracking candidates <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
    *   Pings the team on Slack about the new profile <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
    *   Finds their email with Apollo and drafts a basic message in the user's inbox <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.

## Benefits of Automation

Gum Loop facilitates the automation of repetitive tasks, allowing individuals and businesses to focus on high-leverage activities <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. If a task can be broken down into a list of steps, it can likely be automated <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. This approach provides an "unfair advantage" in business, leading to increased sales, improved customer experience, and time savings <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

Automating processes also means that business leaders who deeply understand a problem can directly build hyper-custom solutions without needing to rely on engineering teams, which often leads to "half-baked solutions" <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.

For Gum Loop itself, dogfooding its product by automating internal business processes allows the company to remain efficient and focus on core aspects like engineering, product, and marketing <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.

## Cost and Pricing

The cost of running a workflow depends on the number of AI queries and external API calls (e.g., Gemini queries, ad analyses) <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. While specific conversion rates for Gum Loop credits were not provided, an example analysis email was estimated to cost around $1.62 using Gum Loop's credit system <a class="yt-timestamp" data-t="00:29:59">[00:29:59]</a>.

A key benefit is the ability to provide your own API keys for services like Apollo or [[gemini_models_demo | Gemini]] <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. This can significantly reduce the cost on Gum Loop's platform, sometimes dropping it to near zero, especially for large customers who already pay for these services <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>. The cheapest plan reportedly comes with 30,000 credits <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.

## Getting Started with Gum Loop

Gum Loop offers a free sign-up with no credit card required to begin experimenting <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Completing the tutorial grants users 1,000 free credits to explore the platform's capabilities <a class="yt-timestamp" data-t="00:42:17">[00:42:17]</a>.

Gum Loop also supports a community, including a Slack community, where users can ask questions and receive assistance <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a>. In the future, a marketplace will allow users to publish and even sell their workflow templates <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.