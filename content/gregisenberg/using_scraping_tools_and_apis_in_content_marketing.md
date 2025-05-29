---
title: Using scraping tools and APIs in content marketing
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

Automating a marketing team with [[ai_powered_content_automation | AI agents]] and creating content on autopilot is achievable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach involves leveraging [[ai_tools_for_content_creation_and_marketing | AI tools]] and workflow automation platforms to significantly reduce manual effort <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## The Automated Content Workflow

An end-to-end automation workflow can help save an estimated 10 to 15 hours per week <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This specific workflow, demonstrated for LinkedIn content creation, focuses on automating content generation, from data gathering to publishing <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Phase 1: Data Collection & Research

The process begins with analyzing social platforms to identify popular topics and content <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Scraping YouTube and X:** The workflow scrapes top-performing videos on YouTube and posts on X (formerly Twitter) for a given topic or keyword <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This includes finding videos with high engagement and posts relevant to workflow automation and AI <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Transcribing Video Content:** The system watches and transcribes YouTube videos, capturing content from top-performing sources <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **Leveraging Appify:** Appify is used as a platform to scrape data from various internet sources like Instagram, Amazon, TikTok, YouTube, or X <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Its open APIs allow integration into workflows to process data <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Merging Data:** All collected data, including transcribed video content, hooks, titles, and X posts, is merged into one large text block for comprehensive context <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This research phase ensures sufficient context for the subsequent [[ai_tools_for_content_creation_and_marketing | Large Language Models]] (LLMs) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Phase 2: Content Idea Generation

After data collection, an [[creating_content_with_ai_tools | AI agent]] generates content ideas:
*   **Fresh Angles:** The content idea generator, plugged into an OpenAI LLM, scans the collected text to find fresh content angles that don't simply replicate existing research <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. The goal is to use the research as inspiration to create unique ideas <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Prompting for Specificity:** Prompts are designed to create actionable content ideas strictly related to a specific niche, such as marketing with Inaden <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Instructions specify desired output format, including a short and clear title, a "scroll-stopping" hook, optimal content format, and a unique angle <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. The AI is also instructed to avoid technical jargon and consider the target audience <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Brand Voice Integration:** The system analyzes top-performing X posts to identify the speaker's tone, themes, and overall brand voice, ensuring generated content aligns with it <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### Phase 3: Factual Research & Validation

To ensure accuracy and relevance, the workflow incorporates a research agent:
*   **Perplexity for Data:** A research agent uses Perplexity to find real stats, use cases, trends, insights, and case studies related to the marketing angles <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. This prevents the LLM from hallucinating or generating random, nonsensical content <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   **Open Router for LLM Access:** Open Router is highlighted as a helpful tool that allows access to various LLMs (like Perplexity, OpenAI, Claude) through a single node and a unified price, simplifying integration and experimentation <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Phase 4: Content Creation & Optimization

The refined ideas and research are then fed into a content creation agent:
*   **Claude 3.7 Sonnet for Writing:** Claude 3.7 Sonnet is chosen as the LLM for [[creating_content_with_ai_tools | content generation]] due to its strong writing capabilities <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>, <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. Its power is maximized when provided with extensive context and data <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   **Prompting for LinkedIn:** For LinkedIn posts, specific prompting tips include:
    *   **Brand Voice:** Instructions to write with authentic expertise, direct communication, confidence, and to avoid overly formal or corporate jargon <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
    *   **Narrative & Value:** The content agent is prompted to create narrative-driven posts that offer actionable insights and positive business impact, using data only when relevant <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
    *   **Formatting Control:** Instructions are given to avoid common AI tendencies like excessive hashtags or emojis, and to output content in a specified format (e.g., title, content) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   **Conversion Copywriting:** The LLM is framed as a "LinkedIn content strategist and conversion copywriter" to ensure the content leads readers through a journey with a strong hook, builds interest and desire, provides value, and includes a clear call to action <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Tips also include avoiding M-dashes, which can make content feel inauthentic <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

### Phase 5: Image Generation & Publishing

The final stages involve creating a visual element and preparing for publication:
*   **OpenAI Image Generation:** The workflow generates an image for the post using the OpenAI image generation model <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. This can involve dynamic prompts based on the post topic or simpler instructions like creating a 3D image representing an AI system <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
*   **Human-in-the-Loop Review:** To ensure quality before publishing, the generated post is sent to a Google Doc, and a link to this doc is sent to Slack <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>, <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. This allows for human review and editing <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>, <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
*   **Automated Publishing:** Once approved via a button in Slack, the content can be automatically published directly to the desired social platform, such as LinkedIn <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. The image can also be dynamically selected from a Google Drive folder of personal photos to enhance authenticity <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>, <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.

## Benefits of this Approach

*   **Accelerated Testing:** This workflow allows for much faster testing of content angles, hooks, and topics compared to manual methods <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Top-Performing Content:** By incorporating context and information from high-engagement sources, the system generates top-performing content <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Reduced Manual Research:** Automation frees up time that would otherwise be spent on manual research, allowing creators to focus on other tasks <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Validated Social Posts:** The content is validated by scraping top-performing YouTube videos and X posts, significantly increasing the chances of engagement <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. This removes guesswork and allows for testing and refinement <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Authenticity:** Despite [[ai_powered_content_automation | AI automation]], the goal is to make the content feel as authentic as possible, capable of passing a "Turing test" in terms of human-like writing <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>, <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.

## Key Tools Mentioned

*   **Inaden:** A workflow automation platform used to build and manage the entire content creation process <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Appify:** A platform for scraping data from various internet sources via APIs <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Open Router:** A tool that provides access to multiple LLMs through a single node and subscription, simplifying integration <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Perplexity:** An LLM used as a research agent to find facts, trends, and use cases <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **OpenAI LLM:** Used for generating content ideas and images <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>, <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Claude 3.7 Sonnet:** Regarded as a top writing LLM for generating narrative-driven content <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Slack:** Used for the human-in-the-loop review step, where draft content links are sent for approval <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   **Google Docs:** Output destination for the drafted content, allowing for easy review and editing <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

## Prompting Tips for LLMs

To get the most out of [[ai_tools_for_content_creation_and_marketing | AI tools]] for content creation, it's crucial to:
*   **Understand Questions and Desired Output:** Know what questions to ask the AI and what "good" content looks like for your specific needs <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Iterate on Prompts with AI:** Use [[ai_tools_for_content_creation_and_marketing | AI]] itself to improve your initial prompts <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Provide Extensive Context:** Feed the model with "tons of data and tons of context" (e.g., scraped content, brand voice guidelines) to maximize its output quality <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Define Brand Voice and Guard Rails:** Explicitly instruct the AI on the desired tone, style, and communication approach to avoid "fluff" or overly formal language <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   **Specify Output Format and Role:** Clearly define the desired output format (e.g., title, content) and "frame" the LLM by assigning it a specific role (e.g., "LinkedIn content strategist") <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>, <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Focus on Conversion:** For marketing content, include instructions for direct response or conversion copywriting to ensure the content guides the reader through a journey with a strong call to action <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

## Accessing the Workflow Template

A complete JSON file of this workflow is available for free download. Users can upload this file into Inaden, customize it, and begin experimenting with [[automating_marketing_tasks_using_ai | AI-powered content automation]] <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.