---
title: Building a Chrome Extension for Blogging
videoId: fjdcGj86CmA
---

From: [[amiteshanand]] <br/> 

For [[creating_content_online | technical writers]] and bloggers working on platforms like Dev.to, the process of [[integrating_ai_tools_for_blogging_efficiency | creating content online]] often involves switching between multiple external tools [00:00:00] [00:00:05]. Typically, users might copy sections of their blog post, open a new website like ChatGPT or Claude, and then paste the content to receive suggestions or generate images [00:00:14]. This manual process of copying, pasting, and then reapplying changes can be time-consuming [00:00:22].

## An Integrated Solution with a Chrome Extension

A custom [[chrome_extension_development_with_javascript_apis | Chrome extension]] has been developed to streamline the blogging workflow, allowing users to perform these tasks without leaving their writing platform [00:00:26]. This extension integrates capabilities for both content review and on-the-fly image generation directly within the blogging environment [00:00:30].

## Leveraging Nebius AI Studio

The foundation of this [[chrome_extension_development_with_javascript_apis | Chrome extension]] is Nebius AI Studio, a platform that hosts various open-source, state-of-the-art AI models [00:00:38] [00:00:40].

Key models utilized include:
*   **Deeps V3 and Deeps R1**: Used for text-to-text processing, particularly for evaluating and reviewing technical content [00:00:43] [00:00:52]. Deeps R1 is a reasoning model, similar to GPT-4o, and is more cost-effective to run [00:01:57] [00:02:01].
*   **Flux Shell and Stable Diffusion models**: Employed for text-to-image generation [00:00:48] [00:00:50]. The Flux model is specifically used for generating images in this demonstration [00:00:57].

Nebius AI Studio provides APIs in JavaScript, Python, and cURL requests, which were used to build the [[chrome_extension_development_with_javascript_apis | Chrome extension]] [00:01:00] [00:01:01].

## Extension Capabilities in Action

The extension offers two primary functionalities:

### Image Generation from Text
To generate an image, a user simply selects a portion of their blog post text [00:01:12]. They can then right-click, select "AI tool," and click on "generate image from text" [00:01:16]. The extension processes the text and generates a relevant image that can be easily copied and pasted directly into the blog post [00:01:20] [00:01:22]. This functionality can also be accessed via hovering buttons that appear when text is selected [00:02:09] [00:02:16].

### AI-Powered Content Review
For reviewing technical content, the user selects the desired text [00:01:37] [00:01:40]. Similar to image generation, they right-click, choose "AI tools," and then "review the text with AI" [00:01:42] [00:01:44]. The AI provides suggestions based on the content, which can then be easily applied [00:01:46] [00:01:50].

## Benefits

This [[chrome_extension_development_with_javascript_apis | Chrome extension]] offers significant ease of use, empowering bloggers by allowing them to focus on the content itself [00:02:37] [00:02:39]. By integrating these [[integrating_ai_tools_for_blogging_efficiency | AI tools]] directly into the writing environment, it eliminates the need to navigate between multiple platforms for image generation or content review, thereby streamlining the entire blogging process [00:02:27] [00:02:43].