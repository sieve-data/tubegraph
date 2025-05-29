---
title: Gum Loop software overview
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gum Loop is an AI agent and automation company that recently raised $9 million, recognized as one of the best-in-class in its field <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Co-founded and led by CEO Max, the software is designed to automate tasks typically performed by a junior employee <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It's suitable for businesses ranging from the largest companies to a solopreneur <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Max emphasizes that by the end of using Gum Loop, users should be able to build and deploy powerful AI workflows and create usable tools that perform various AI actions with their data <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## How Gum Loop Works

A Gum Loop workflow is essentially a series of connected steps, where data is passed from one "node" to another <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Users start with an empty canvas and add these nodes to build their automation <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The platform is often compared to [[creating_software_without_writing_code | no code automation tools]] like Zapier and Make due to its similar integrations <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

The strength of Gum Loop lies in connecting external data with AI steps <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Key Features

*   **Integrations**: Gum Loop offers integrations with various platforms such as Slack, Airtable, Outlook, Notion, Reddit, and Gmail, allowing users to pull data from these sources <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **AI Steps**: The platform incorporates multiple AI steps, all powered by large language models (LLMs) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   **Ask AI**: A basic node similar to asking ChatGPT a question, but compatible with various models including OpenAI models or even user-deployed Azure models <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   **Data Extraction**: Users can specify a schema (e.g., amount and date from a receipt) for AI to extract specific data <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   **Categorization, Summarization, Scoring**: These are other nuanced AI tooling options available <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   **Video and Image Analysis**: The platform can perform analysis on video and image content <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Subflows**: An advanced feature that allows an entire workflow to be used as a node within another workflow, similar to a function in programming <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This promotes reusability, cleanliness, and extensibility <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Webhooks / API Triggers**: Any Gum Loop workflow can be treated as an API that can be triggered from an external product based on an event <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Loop Mode**: This feature enables running automations at massive scale, such as processing thousands of events concurrently. It functions like a "for loop," where a single workflow can be run thousands of times over multiple inputs <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. Gum Loop handles the underlying infrastructure and rate limits for concurrent runs <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
*   **Interfaces**: To simplify workflow usage for non-technical team members, Gum Loop allows users to create a simple, drag-and-drop user interface (UI) on top of complex workflows <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. This makes the automation accessible and easy to use without understanding the underlying flowchart <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.
*   **Custom Nodes**: Users can build their own integrations by providing API documentation to an AI-powered builder <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>. This allows integration with internal data endpoints or unsupported third-party services <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>. Custom nodes are accessible to everyone in a workspace, facilitating collaboration <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.
*   **Chrome Extension**: A Chrome extension node allows workflows to be accessible directly from the browser <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. It can scrape screen content, screenshot, or perform other actions to feed data into a workflow <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
*   **Bring Your Own API Keys**: Users can provide their own API keys for services like Apollo or Gemini, significantly reducing the cost of running workflows on Gum Loop <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

### Example Applications

*   **Sales Lead Qualification and Email Drafting**: Gum Loop was used to automate early revenue generation at YC. It would detect user sign-ups, pass their email to a workflow, research the user's company (domain, website summary, company name, industry, revenue, country), send a Slack notification to the team, and draft a personalized outbound email in Gmail <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Podcast to Blog Post Generation**: A workflow can take a YouTube link of a podcast, extract the transcript, use AI to create a verbose but informative digest, then write a blog post in HTML format with a tldr and embedded video, and publish it to a CMS like Ghost <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This can be looped over thousands of links for mass content generation <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   **Competitor Ad Analysis**: This workflow scrapes a competitor's Facebook ads (including Instagram and WhatsApp), uses Gemini to analyze video and image ads, and generates an overall analysis of the competitor's ad strategy <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. The analysis is formatted in HTML and can be emailed to management on a scheduled basis <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
*   **Daily Calendar Briefing**: A workflow can run every morning to read Google Calendar, research every person involved in meetings (company, revenue, web traffic), and provide a thorough email report with a three- or four-point tldr, detailing who will be met and why they might be important <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>.
*   **LinkedIn Profile Research**: A Chrome extension-triggered workflow can scrape a LinkedIn profile, extract key details (name, title, company, university, location), summarize the person's background focusing on specific traits, find their Twitter and GitHub, track candidates in a Google Sheet, ping the team on Slack, find their email via Apollo, and draft an outbound message in Gmail <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>.
*   **Niche Outreach/Sales**: Users can automate personalized outreach campaigns, such as scraping niche directories (e.g., hotels) and drafting tailored emails that highlight a company's competitive positioning <a class="yt-timestamp" data-t="00:37:11">[00:37:11]</a>.

## Benefits and Philosophy

Gum Loop aims to allow users to build fully AI-powered products that would normally require an engineer to create <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. It provides a "build your own software" sort of platform <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

*   **Automation of Junior Employee Tasks**: The core value proposition is automating repetitive tasks that a junior employee would handle <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. If a task can be described as a list of steps, it can likely be automated <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>.
*   **Efficiency and Unfair Advantage**: Automating workflows creates tight systems that provide an "unfair advantage" in business, helping save time for founders and executive teams to focus on high-leverage activities <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Empowering Non-Technical Users**: The platform enables semi-technical people at companies to build complex automations and integrations without needing an engineering degree <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
*   **Cost-Effectiveness**: Automating tasks with Gum Loop is significantly cheaper than paying a human employee to perform the same work <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>.
*   **User Experience**: The software is designed to be visually appealing and intuitive, described as feeling like "Lego building blocks" with a "Figma feel" <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Templates and Marketplace**: Gum Loop offers a template directory and plans to launch a marketplace where users can publish and sell their workflows, allowing others to clone and benefit from pre-built solutions <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This aligns with the philosophy that understanding a problem should be the only prerequisite to solving it <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Dogfooding**: The Gum Loop team uses its own product to automate nearly all business processes, which helps improve the product's quality and efficiency <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.

## Getting Started with Gum Loop

Gum Loop offers a free sign-up with no credit card required, allowing users to experiment with the platform <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Completing the tutorial grants 1,000 free credits <a class="yt-timestamp" data-t="00:42:17">[00:42:17]</a>. The cheapest paid plan currently includes 30,000 credits <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>. A community and Slack channel are being built for users to ask questions and get help from experts <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a>. The ability to sell and share workflows will also be available soon <a class="yt-timestamp" data-t="00:42:32">[00:42:32]</a>.