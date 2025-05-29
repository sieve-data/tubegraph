---
title: Automating content creation with AI
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

[[Automating your marketing with AI | Automating marketing teams]] and content creation with AI agents allows for content to be put on autopilot, potentially saving significant time and improving content performance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach enables businesses to test content angles, hooks, and topics much faster than traditional methods <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Workflow Overview

An end-to-end automation workflow for content creation involves several key stages:
1.  **Data Finding:** Identifying relevant information around a niche or topic <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
2.  **LLM Processing:** Feeding collected data into large language models (LLMs) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
3.  **Content Production:** Generating content based on the processed data <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
4.  **Automated Publishing:** Automatically posting the created content to target platforms <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

This workflow, exemplified by a LinkedIn content generation process, can save approximately 10 to 15 hours per week <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Data Collection and Research

The first stage involves gathering extensive data to provide context for the AI models.
*   **Topic Input:** A keyword is entered to initiate the process, e.g., "inadin" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Scraping YouTube and X:** The system scrapes top-performing videos on YouTube and relevant posts from X (formerly Twitter) for the given topic, focusing on content with high engagement <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This includes transcribing YouTube videos to capture their full content, hooks, and titles <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Tool for Scraping:** [[Automating business processes with AI | Appify]] is used for scraping data from various internet platforms like YouTube, X, Instagram, Amazon, and TikTok, through its open APIs <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Data Consolidation:** All collected data, including transcribed videos and X posts, is merged into one large text block, serving as the research phase to ensure sufficient context for the LLMs <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

This automated research mirrors the manual process a savvy content creator would undertake, but at an accelerated pace, enabling continuous monitoring of content trends <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. It leverages existing high-performing content to shortcut the content creation process <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## Content Idea Generation

After data collection, an AI agent generates fresh content ideas:
*   **Agent Function:** A "content idea generator" agent, linked to an [[using_ai_for_content_generation_and_analysis | OpenAI LLM]], scans the large text block of researched data to find unique content angles and ideas, avoiding mere replication <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   **Prompting for Marketing Focus:** The prompt instructs the AI to create actionable content ideas strictly related to marketing, even if the initial keyword is broader <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Desired Output Elements:** Ideas should include a short and clear title, a scroll-stopping hook, an optimal format, and a unique angle that shows how marketers can scale efforts using AI and specific tools like NAD <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Instructions also specify avoiding excessive technical jargon <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Brand Voice Integration:** The AI also analyzes top-performing X posts from the user's account to identify brand voice, themes, and communication style, ensuring the generated ideas align with the creator's persona <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Content Creation and Refinement

Once ideas are generated, the workflow proceeds to creating the actual content and gathering supporting facts.
*   **Fact and Trend Research:** A "research agent" uses tools like Perplexity to find specific facts, trends, and sources to back up claims and prevent AI hallucination <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. It looks for use cases with real stats, industry insights, marketing use cases, and case studies <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Multi-LLM Access:** Open Router is a helpful tool that allows access to various LLMs (like Perplexity, OpenAI, Claude) through a single node and a unified pricing model, enabling the selection of the best LLM for each specific task within the workflow <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Content Generation for Platforms:** The merged ideas and research are fed into a platform-specific content agent, such as a "LinkedIn content agent" <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
    *   **Preferred LLM:** Claude 3.7 Sonnet is highlighted as the best writing LLM, especially when armed with sufficient context and data <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
    *   **[[Prompting techniques for AIgenerated content | Prompting Techniques]]:**
        *   **Brand Voice:** Instructions include maintaining authentic expertise, direct communication, confidence, and avoiding overly formal language, corporate jargon, and marketing speak <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
        *   **Narrative Structure:** The AI is prompted to create narrative-driven posts with actionable insights <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
        *   **Specific Exclusions:** Instructions to avoid hashtags and emojis are crucial <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
        *   **Format:** A specific output format (e.g., title, content) is defined <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
        *   **Role Framing:** The LLM is framed as a "LinkedIn content strategist and conversion copywriter" to ensure a strong hook, build interest and desire, provide value, and include a clear call to action <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
        *   **Avoiding AI Tells:** Explicitly avoiding "M-dashes" helps make the content feel less AI-generated and more authentic <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   **Image Generation:** The workflow also generates an image for the post, typically using an [[Using AI for content generation and analysis | OpenAI image generation model]] <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## Human-in-the-Loop Review

Although automated, a human review step is included to ensure quality and final approval.
*   **Draft Delivery:** The generated content (and image) is sent as a draft to a Google Doc, with a link provided in Slack <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **Review and Edit:** This allows the user to review the content, make any necessary edits, and ensure it aligns with their preferences before publishing <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   **Image Customization:** While AI can generate images, using personal photos stored in a Google Drive folder can make posts feel more natural and less AI-generated, with the system capable of randomly selecting from such a folder <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

## Automated Publishing and Validation

The final stage is publishing the content and ensuring its effectiveness.
*   **One-Button Publish:** After review, a single button click (e.g., an "approve" button in Slack) can publish the content directly to the desired social platform, like LinkedIn <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
*   **Validated Posts:** A key benefit is that these are "validated social posts" because the ideas and content are derived from scraped, high-performing YouTube videos and X posts, significantly increasing the chances of engagement (likes and comments) <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. This removes guesswork and uses real validation <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Testing and Optimization:** Users can test multiple posts, delete those that don't perform well, and double down on successful ones. This allows for continuous optimization across various channels <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

## Benefits and Best Practices

*   **Time Savings:** Frees up significant time (10-15 hours/week) that would otherwise be spent on manual research and content creation <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Scalability:** Allows for faster testing of content angles, hooks, and topics <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **High-Performing Content:** Produces content with a higher likelihood of engagement due to data-driven insights <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **[[Leveraging AI for content creation and SEO | Business Opportunities]]:** This workflow can serve as a backbone for [[automated_business_creation_using_ai | creating businesses]] like consulting, freelancing, or optimizing agency operations <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Key Principles for [[AI in Content Creation and Marketing | Effective AI Use]]:**
    *   **Context is King:** Provide LLMs with tons of data and context to get the most out of them <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
    *   **Prompt Engineering:** Know what questions to ask and what "good looks like" in terms of desired output <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. AI can also be used to improve initial prompts <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    *   **Strategic LLM Selection:** Utilize the best LLM for each specific task within the workflow <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
    *   **Authenticity:** Aim to make AI-generated content feel as authentic as possible by providing strong brand voice guidelines and avoiding common AI "tells" <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

## Tools Utilized

*   **NADN:** The central platform for building and executing the automation workflow <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Appify:** For scraping data from various online platforms (YouTube, X, etc.) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **OpenAI LLM:** Used for generating content ideas <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Perplexity:** Utilized as a research agent to find facts, trends, and use cases <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Open Router:** Provides access to multiple LLMs (including Perplexity, OpenAI, Claude) through a single node and unified pricing <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Claude 3.7 Sonnet:** Recommended as the best writing LLM for content generation <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **OpenAI Image Gen Model:** For creating images to accompany posts <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Google Docs:** To provide a review point for drafted content <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **Slack:** For receiving notifications and enabling the human-in-the-loop approval process <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

A complete workflow template (JSON file) is available for download at templates.vibemarketer.com/greg, allowing users to upload and customize it in NADN to begin learning and tinkering immediately <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.