---
title: Using Deep Learning Models for Content Generation
videoId: fjdcGj86CmA
---

From: [[amiteshanand]] <br/> 

Traditionally, content creators like technical writers on platforms such as dev.to often need to switch between multiple external tools for tasks like image generation or content review <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This includes copying sections of text to platforms like ChatGPT or Claude for AI-powered suggestions, which then require manual application back to the original content <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

However, a new Chrome extension has been developed to streamline this process, allowing users to remain within their writing platform for these tasks <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This extension leverages [[ai_tools_for_content_creation | AI tools for content creation]] to provide integrated functionalities for content review and image generation <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Nebius AI Studio: The Foundation for Integration

The core technology enabling these capabilities is Nebius AI Studio <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This platform hosts various open-source, state-of-the-art deep learning models <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Models Utilized

Nebius AI Studio provides access to a range of models, including:
*   **DeepSeek V3** and **DeepSeek R1**: These models are used for text-to-text operations, specifically for evaluating and providing suggestions for technical content <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. DeepSeek R1, a reasoning model similar to GPT-4o, uses a Chain of Thought approach and is more cost-effective to run <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Flux Schell** and **Stable Diffusion**: These models are primarily used for [[text_and_image_generation_using_nebius_ai_models | text and image generation]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. In the demonstrated example, the Flux model was specifically used for image generation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Nebius AI Studio offers APIs in JavaScript, Python, and cURL, facilitating the development of integrated tools like the Chrome extension <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Integrated Content Creation Workflow

The Chrome extension simplifies content creation by allowing users to perform critical tasks directly within their blog editor.

### Generating Images from Text

To generate an image based on content:
1.  Select a portion of text within the article <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  Use the right-click context menu and select "AI tool" then "generate image from text" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Alternatively, hover buttons appear when text is selected, offering direct options like "Generate Image" <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
3.  The AI generates an image, which can then be easily copied and pasted into the blog post <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Reviewing and Updating Technical Content

For reviewing the technical content of a blog post:
1.  Select the text to be reviewed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  Access the "AI tools" from the right-click menu and select "review the text with AI" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
3.  The AI provides suggestions based on the content <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
4.  Users can then easily apply any of the suggested changes <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, and even choose between different deep learning models for the review <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

>[!INFO] Benefits of Integration
>This [[integrating_ai_tools_for_writing_and_content_planning | integration of AI tools for writing and content planning]] allows creators to remain focused on their blog content without needing to navigate to multiple external applications <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. It significantly enhances the ease of use and efficiency for tasks like [[integrating_ai_tools_for_blogging_efficiency | blogging efficiency]], leveraging deep learning models for both [[text_and_image_generation_using_nebius_ai_models | text and image generation]] and content review <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.