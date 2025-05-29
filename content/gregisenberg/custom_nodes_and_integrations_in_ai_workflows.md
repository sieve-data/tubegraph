---
title: Custom nodes and Integrations in AI workflows
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gum Loop, an [[AI agents and automated marketing workflows | AI agent]] and [[AI automation tools for workflows | AI automation company]], provides a platform that allows users to [[building_aipowered_workflows_without_coding | build AI-powered workflows]] and connect them with various data sources and external services. The platform emphasizes the ability to [[integrating_ai_with_existing_frameworks | integrate AI with existing frameworks]] and even create custom integrations without extensive coding knowledge. <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>

## Core Integrations
Gum Loop workflows are described as a series of connected steps, where data is passed from one "node" to another. <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a> The platform offers many integrations similar to no-code automation tools like Zapier and Make. <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

Users can pull data from:
*   Slack <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>
*   Airtable <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
*   Outlook <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   Notion <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   Reddit <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>
*   Gmail <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>
*   Google Calendar <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>
*   Ghost CMS <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>
*   Shopify <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>
*   Webflow <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>

The true power of Gum Loop emerges when this data is connected with AI steps. <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>

## AI Steps and Model Flexibility
Gum Loop's AI steps are powered by Large Language Models (LLMs). <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> Users can "plug and play" with various models, including Open AI models and even custom models deployed on Azure. <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>

Available AI steps include:
*   **Ask AI**: Similar to asking a question to ChatGPT. <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>
*   **Data Extraction**: Specify a schema (e.g., amount, date) for AI to extract specific data from content. <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   **Categorization**: AI can categorize information. <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>
*   **Summarization**: AI can summarize content. <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>
*   **Scoring**: AI can score data. <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>
*   **Video and Image Analysis**: AI can analyze visual content. <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>

Pairing these LLM steps with user data allows for the creation of "fully [[integrating_ai_features_into_mobile_apps | AI-powered products]]" that would typically require an engineer to build. <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>

## Webhooks and API Triggers
Any Gum Loop workflow can be treated as an API trigger, allowing users to initiate workflows from their own products or based on specific events via webhooks. <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a> <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a> This enables users to build their own SaaS products on top of Gum Loop, with the platform handling the backend processing. <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a> Dynamic fields can be passed into workflows through these webhooks, for instance, from a website form. <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>

## Custom Nodes and Integration Building
A standout feature is the ability to build custom integrations (referred to as "custom nodes") directly within the platform. <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>

> [!TIP] Prompt-based Integration Creation
> Users can prompt the AI to build an integration node by simply providing documentation for an external API. The AI understands the context of a Gum Loop integration and generates the necessary code. <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a> <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>

This feature democratizes integration development, allowing non-developers to create complex tools like:
*   Twitter scrapers <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>
*   Blue Sky scrapers for social media analysis <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>
*   Integrations with internal Dev Team endpoints <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>

Custom nodes, once built, become accessible to all team members within a workspace, just like pre-built integrations. <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a> The platform aims to further simplify this by allowing users to describe an integration, and the AI will automatically name it, get an icon, define inputs, write code, and even test it. <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>

## Subflows: Reusable Workflow Components
Subflows are distinct workflows that can be used as nodes within other workflows. <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> They function similarly to programming functions, offering reusability, cleanliness, and extensibility. <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a> This allows users to share complex pieces of automation work with colleagues who can then import and benefit from them. <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>

## Chrome Extension Integration
Gum Loop offers a Chrome extension that integrates with workflows. <a class="yt-timestamp" data-t="00:34:35">[00:34:35]</a> This allows workflows to start with a "Chrome extension node," enabling the flow to interact with the content of the user's browser. <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>

Capabilities of the Chrome extension include:
*   Scraping entire screen content <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>
*   Screenshotting <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>
*   Performing other browser actions <a class="yt-timestamp" data-t="00:35:20">[00:35:20]</a>

This combination of the Chrome extension and custom node builder allows for the creation of "infinitely powerful no-code Chrome extensions." <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>