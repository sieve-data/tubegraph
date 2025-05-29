---
title: Building a Chrome Extension with DeepSeek and FLUX
videoId: fjdcGj86CmA
---

From: [[amiteshanand]] <br/> 

A new Chrome extension has been developed to streamline the workflow for technical writers, allowing them to perform tasks like content review and image generation directly within their writing platform, such as dev.to <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This eliminates the need to switch between multiple external tools, improving efficiency <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## The Traditional Workflow Challenge

Previously, technical writers often had to copy sections of their blog posts to external tools like ChatGPT or Claude to get a quick review or generate content suggestions <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Similarly, generating images based on blog content typically required access to separate external image generation tools <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This fragmented process involved manual copying, pasting, and re-applying suggestions <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## The Solution: A Unified Chrome Extension

The new Chrome extension allows users to stay on their writing platform and perform these tasks seamlessly <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It integrates functionalities for:
*   Reviewing blog post content <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   Generating images on the fly based on the content <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

This [[using_chrome_extension_for_blog_post_enhancements | Chrome extension for blog post enhancements]] was built by leveraging APIs provided by Nebulas AI Studio <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Powered by Nebulas AI Studio

Nebulas AI Studio is a platform that hosts several state-of-the-art open-source models <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The extension utilizes specific models for different tasks:
*   **Content Evaluation (Text-to-Text)**: [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek V3]] and [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] models are used <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] is a reasoning model that employs Chain of Thought, similar to GPT-4o1, and is more cost-effective to run <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Image Generation (Text-to-Image)**: FLUX and Stable Diffusion models are available <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. For the demonstrated example, the FLUX model was used <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Nebulas AI Studio provides APIs in JavaScript, Python, and cURL requests, which were used to build the Chrome extension <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## In Action: Practical Use Cases

### Generating Images from Text

To generate an image, a user can simply select a part of their text, right-click, and choose "AI tool" then "generate image from text" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The extension then generates an image that can be easily copied and pasted directly into the blog post <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Alternatively, hovering buttons appear when text is selected, offering the "generate image" option directly <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Reviewing Technical Content with AI

For content review, users select the text, right-click, and choose "AI tools" then "review the text with AI" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The AI provides suggestions based on the content, which can then be easily applied <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Users can choose between [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek V3]] and [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] models for review <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

This tool significantly enhances the ease of use for technical writers, allowing them to focus on the content of their blog posts without interruptions <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.