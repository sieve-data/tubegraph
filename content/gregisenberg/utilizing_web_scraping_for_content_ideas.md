---
title: Utilizing web scraping for content ideas
videoId: m9iaJNJE2-M
---

From: [[gregisenberg]] <br/> 

Automating marketing content with [[utilizing_ai_tools_for_content_creation_and_marketing | AI agents]] and web scraping allows for content to be put on autopilot, generating likes and comments [00:00:06]. This process offers a comprehensive workflow for creating content automatically [00:00:16].

## The Vibe Marketing Workflow
The described workflow demonstrates an end-to-end automation process designed to save 10 to 15 hours per week [00:01:30]. It enables faster testing of content angles, hooks, and topics by providing extensive context and information to [[automating_content_creation_with_ai | AI models]], resulting in top-performing content [00:02:09]. The workflow can also generate images and post automatically, though a human review step is included for refinement [00:02:27].

## Data Collection and Research
The initial phase of the workflow involves analyzing YouTube and X (formerly Twitter) for relevant content around a given topic [00:03:37].

### Web Scraping with [[automation_with_appify_and_data_scraping | Appify]]
The system scrapes top-performing YouTube videos [00:04:07] and X posts related to the chosen topic, focusing on content with a high degree of engagement [00:04:16]. It then transcribes YouTube videos and collects content from X posts, merging all data into a single text block [00:04:42]. This process leverages [[automation_with_appify_and_data_scraping | Appify]], a platform that offers APIs for scraping various internet sources like Instagram, Amazon, TikTok, YouTube, and X [00:05:07].

This automated research phase eliminates the need for manual, time-consuming research, allowing users to find content that is already performing well [00:06:27]. It helps in understanding existing positioning and identifying opportunities [00:06:20].

## Content Idea Generation
After data collection, an [[developing_unique_and_entertaining_content_with_ai_insights | AI agent]] acts as a content idea generator, plugging into an OpenAI LLM to scan the aggregated text for fresh angles and content ideas [00:07:15]. The goal is not to replicate existing content but to use it as inspiration [00:07:39].

### Prompting Strategy
The AI is instructed to create actionable content ideas strictly related to marketing, extracting relevant concepts from broader topics [00:08:11]. Specific requirements for content ideas include:
*   **Short and clear title** [00:08:39]
*   **Scroll-stopping hook** [00:08:42]
*   **Optimal format** [00:08:49]
*   **Unique angle**: A unique point of view on how marketers can scale efforts using AI and workflow automation [00:08:53]

Additionally, the prompts guide the AI to avoid technical jargon, frame content for a specific audience, and analyze the user's top-performing X posts to identify brand voice and themes [00:09:06]. Prompts can be improved by using other AI tools like ChatGPT, Manis, or Claude, by providing examples of desired content and clarifying what "good looks like" [00:09:51].

## Research and Fact-Checking
To ensure accuracy and relevance, a research agent utilizes Perplexity (accessed via Open Router) to find specific facts, trends, and sources to back up content claims [00:10:43]. This prevents the model from hallucinating and generates content with real stats, use cases, industry insights, and popular opinions [00:10:36].

### Open Router
[[exploration_of_aidriven_design_and_analytics_tools_for_content_creators | Open Router]] is a tool that allows access to various LLMs (e.g., Perplexity, OpenAI, Claude) through a single node and API key, simplifying the integration of different models within a workflow [00:11:51].

## Content Creation and Publishing
The ideas and research are then fed into a content agent designed for specific platforms, such as LinkedIn [00:13:07].

### LinkedIn Content Agent
Claude 3.7 Sonnet is preferred for content creation due to its writing capabilities [00:13:27]. Effective prompting is crucial, providing the AI with ample context and data to generate powerful content [00:14:18].

**Prompting Tips for Content Creation**:
*   **Brand Voice**: Include guidelines for an authentic, direct, confident, and straightforward tone, avoiding overly formal language, corporate jargon, and marketing speak [00:14:29].
*   **Narrative Focus**: Instruct the AI to create narrative-driven posts with actionable insights and takeaways that positively impact business [00:15:11].
*   **Data Usage**: Emphasize using data only if relevant and tied to the context [00:15:20].
*   **Format and Structure**: Define the desired output format, including title and content structure [00:15:42].
*   **Avoid AI Traits**: Explicitly instruct the AI not to use common AI-generated elements like hashtags [00:15:37] or M-dashes [00:16:34].
*   **Role-Playing**: Frame the LLM as a "LinkedIn content strategist and conversion copywriter" to encourage direct response and conversion-focused content, including strong hooks, building interest and desire, actionable value, and clear calls to action [00:15:52].

### Image Generation
The workflow also includes an OpenAI image generation model to create accompanying visuals for posts [00:17:41]. It's possible to integrate personal photos stored in a Google Drive to make the content feel more natural and less AI-generated [00:19:47].

### Human-in-the-Loop and Publishing
Before publishing, a "human-in-the-loop" step allows for review and editing. The system sends a link to the drafted Google Doc via Slack [00:18:27]. Users can approve the content directly from Slack, which then automatically publishes it to the desired social platform [00:20:18].

This entire process ensures that the generated social posts are "validated" because they are based on data scraped from high-performing content on YouTube and X [00:21:08]. This significantly increases the chances of creating content that resonates with the audience, removing guesswork [00:21:29]. The AI-generated content has been noted to pass the "Turing test" for authenticity [00:22:09].

## Workflow Template Availability
A complete JSON file containing this workflow is available for download, allowing users to upload it into Inaden and customize it for their own needs [00:22:46]. This provides a free starting template for learning and tinkering with [[challenges_in_ai_and_content_automation | AI content automation]] [00:23:01]. This workflow could also serve as an interesting backbone to [[ai_startup_ideas_using_usergenerated_content_ads | power a consulting or freelancing business]], or to optimize agency operations [00:11:37].