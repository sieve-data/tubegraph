---
title: Automating content creation with AI
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

The concept of [[automating_business_workflows_with_ai | automating business workflows with AI]] within a marketing team, leading to content on autopilot, is becoming a reality <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach aims to create content that not only generates likes and comments but also allows for significant time savings <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. A detailed workflow demonstrates how to achieve an end-to-end automation, potentially saving 10 to 15 hours per week on content creation <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This [[utilizing_ai_tools_for_content_creation_and_marketing | utilization of AI tools for content creation and marketing]] allows for faster testing of content angles, hooks, and topics <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## The N8 Workflow for Content Automation

The described workflow, specifically optimized for LinkedIn content, leverages a platform called N8 (Inaden/Naden) to process data, generate content, and even publish automatically <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The entire workflow can be provided as a downloadable JSON file, serving as a template for users to customize <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### 1. Research and Data Collection

The initial phase involves analyzing top-performing content from platforms like YouTube and X (formerly Twitter) related to a specific niche or topic <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Topic Input:** Users input a keyword (e.g., "Naden") into a chat interface <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Content Scraping:** The system then scrapes the top 20-30 highly engaged videos on YouTube and relevant posts from a user's X account <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Transcription:** YouTube videos are watched and transcribed, accumulating all content from top videos and X posts into one large text block <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Tools:** This scraping is facilitated by Appify, a platform with open APIs for scraping various internet sources like Instagram, Amazon, TikTok, YouTube, and X <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Purpose:** This research phase ensures sufficient context is gathered to feed into Large Language Models (LLMs), mimicking the manual research a savvy content creator would undertake <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. [[Automating_business_workflows_with_ai | Robots and AI]] handle this extensive manual research, freeing up human time <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### 2. Content Idea Generation

After data collection, an AI agent, powered by an OpenAI LLM, processes the large text block to generate fresh content ideas and angles <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Avoiding Replication:** The goal is not to copy but to use the scraped content as inspiration for unique ideas <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Prompting for Marketing:** The prompt guides the AI to create actionable content ideas strictly related to marketing, even if the initial keyword is broader <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Content Structure Requirements:** The AI is instructed to generate a short and clear title, a scroll-stopping hook, an optimal content format, and a unique angle emphasizing how marketers can scale efforts using AI and N8 <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Audience and Brand Voice:** Instructions include avoiding technical jargon, framing the content for a specific audience, and incorporating insights from the user's top-performing X posts to match their speaking style and themes <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Prompt Improvement:** Initial prompts are often refined using other AI tools like ChatGPT, Manis, or Claude, by asking them to improve the prompt based on desired outcomes and example content <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This highlights the importance of knowing "what questions to ask and what good looks like" when using AI <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

### 3. Fact and Trend Research

To ensure content accuracy and prevent AI "hallucinations," a dedicated research agent is employed <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Perplexity Integration:** Perplexity is used to find real stats, use cases, trends, insights, marketing use cases, industry ideas, frameworks, case studies, and popular opinions relevant to the generated content ideas <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Open Router:** Open Router is a valuable tool that allows access to multiple LLMs (like Perplexity Sonar, OpenAI, Claude) through a single node and a unified pricing model, simplifying integration into workflows <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### 4. Content Creation and Optimization

The merged content ideas and research data are fed into a specific content agent, such as a LinkedIn content agent, which can be replicated for any channel <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **LLM Choice:** Claude 3.7 Sonnet is highlighted as the best writing LLM currently available, especially when armed with sufficient context and data <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. The problem often lies in users not providing enough context, leading to subpar results <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Prompting Tips for Content:**
    *   **Brand Voice:** Instructions are given for an authentic, direct, confident, straightforward voice, avoiding overly formal, academic, corporate jargon, or marketing speak <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
    *   **Narrative and Actionability:** The AI is prompted to create narrative-driven posts with actionable insights and positive business impact, using data only when relevant <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
    *   **Format and Style:** Explicit instructions are given to avoid common AI habits like using hashtags and emojis, and to provide a clear output format (e.g., title, content) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. The AI is also told to avoid M-dashes, a common AI writing tell <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
    *   **Role Framing:** The LLM is framed as a "LinkedIn content strategist and conversion copywriter," emphasizing direct response or conversion copywriting to prevent "brand fluff" and ensure the content leads readers through a journey with a strong hook, interest, desire, value, and a clear call to action <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Image Generation:** The workflow includes generating an image for the post using OpenAI's image generation model, capable of dynamic prompts <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. An alternative suggested is to have a Google Drive folder of personal photos for the AI to randomly select from, making the content feel more natural and less AI-generated <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### 5. Human in the Loop and Publishing

Before publishing, a "human in the loop" step allows for review and editing <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
*   **Slack Integration:** The generated content, in a Google Doc format, is sent to a dedicated Slack channel, allowing the user to open and review the draft <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **Approval and Publication:** A simple "approve" button in Slack can directly publish the content to the designated social platform (e.g., LinkedIn) <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
*   **Validated Posts:** A key [[benefits_of_ai_in_content_creation | benefit of AI in content creation]] is that these posts are "validated social posts" because they are derived from scraped, high-engagement content, significantly increasing the chances of them resonating with the audience compared to starting from scratch <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. This removes guesswork and allows for testing multiple variations <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Turing Test:** One such AI-generated post even received a comment from a user, asking if AI wrote it, indicating it passed the Turing test for human-like content <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

## Broader Implications and Future
This workflow represents a significant step in [[creating_and_optimizing_marketing_content_using_ai | creating and optimizing marketing content using AI]], offering potential to [[automating_business_workflows_with_ai | automate business workflows with AI]] across various industries <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. It can serve as a backbone for consulting or freelancing businesses, or for optimizing agency operations <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. By providing a free, downloadable template, users can immediately start experimenting with and optimizing their own automated content creation processes <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. This highlights the [[the_evolving_role_of_ai_in_content_creation | evolving role of AI in content creation]] and its practical applications.