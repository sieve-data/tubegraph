---
title: DeepSeek V3 and R1 for Technical Content Evaluation
videoId: fjdcGj86CmA
---

From: [[amiteshanand]] <br/> 

Technical writers often require external tools for tasks such as generating images or reviewing blog post content before submission <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Traditionally, this involves copying sections of text, opening a new website like ChatGPT or Claude, using an LLM for review, and then manually applying suggestions <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

A [[building_a_chrome_extension_with_deepseek_and_flux | Chrome extension]] has been developed to streamline this process, allowing users to review content and generate images directly within the platform where they are writing, such as Dev.to <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This functionality is enabled by Nebulas AI Studio <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Nebulas AI Studio and Model Integration
Nebulas AI Studio is a platform that hosts several open-source, state-of-the-art AI models <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. For text-to-text operations, it includes the latest models such as [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3]] and [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek R1]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. For text-to-image generation, models like FLUX-Schell or Stable Diffusion are available <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The platform provides APIs in JavaScript, Python, or C-requests for integration <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## DeepSeek V3 and R1 for Content Evaluation
In the context of the [[building_a_chrome_extension_with_deepseek_and_flux | Chrome extension]], [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek V3]] and [[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek R1]] are specifically utilized for evaluating technical content and providing suggestions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The user has the option to choose between these models for content review <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### DeepSeek R1 Capabilities
[[using_deepseek_v3_and_r1_models_in_boltdiy | DeepSeek R1]] is a reasoning model that leverages the Chain of Thought method <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. It is described as very similar to GPT-401 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. A significant advantage of [[deepseek_r10528_model_capabilities | DeepSeek R1]] is that it is much cheaper to run compared to GPT-401 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Workflow Example
When writing an article, such as one on integrating fast LLM inferencing with Vector search, a user can select a part of the text <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Through a right-click menu or hover items, AI tools become available <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

*   **Content Review**: Selecting "review the text with AI" will prompt the AI to analyze the selected content and provide suggestions that can be easily applied <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Image Generation**: The "generate image from text" option uses the selected text to create a relevant image, which can then be copied and pasted directly into the blog post <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

This integrated approach eliminates the need for technical writers to leave their platform, allowing them to focus on the blog content itself without switching between multiple applications <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.