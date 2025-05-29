---
title: Building an AIpowered app without coding
videoId: UGbePdInPVc
---

From: [[amiteshanand]] <br/> 

It is possible to build an AI-powered application in minutes without writing a single line of code <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This can be achieved by leveraging specialized AI app builders and AI model providers.

## The "Do You Know" App: A Case Study

An example of such an application is "Do You Know," an AI-powered app designed to provide interesting facts about objects or things depicted in uploaded images <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. For instance, uploading an image of the Statue of Liberty results in a description of it as an iconic symbol of freedom <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Similarly, an image of the Red Fort led to information about its historical significance in Delhi, India <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

The initial version of this app was ready in under 10 minutes, from a prompt given at 11:42 PM to being almost ready by 11:50 PM <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Subsequent modifications included image analysis updates using the NVUS Vision API, [[improving_ui_and_ux_with_ai_tools | UI improvements]], and integration with Supabase to store the five most recent searches <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Future planned features for the app include user authentication and a streak-tracking feature to maintain a record of learned facts <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

## Tools Used

Two primary tools were utilized to build the "Do You Know" app:

### 1. [[using_lovable_ai_app_builder | Lovable AI App Builder]]

Lovable is an AI app builder that generates applications from simple text prompts <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

*   **Key Features**:
    *   Handles basic CRUD (Create, Read, Update, Delete) operations <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
    *   Connects with Supabase as a database <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   Generates full functionality from a single command <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Allows export of projects via Git <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   Supports publishing and deploying projects <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Cost**: Offers a free plan with five messaging credits daily <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, with paid plans available at approximately $20 <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

**Demonstration**:
A demonstration involved prompting Lovable to "create a note paper with lean minimalist UI to save quick notes on web page" <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The platform generated a basic note-taking app that allowed users to add and delete notes <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### 2. NVUS AI Studio

NVUS AI Studio is an inference provider for AI models, offering access to various [[open_source_alternatives_for_ai | open LLMs]] (Large Language Models) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The "Do You Know" app specifically used Quin Vision models by NVUS for its AI features <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

*   **Model Availability**: Provides a wide range of models, including text-to-text, embedding, and text-to-image models like Quin DC5, Mistral, and Meta Llama <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Playground Feature**: Users can compare different models in the NVUS playground to assess performance for specific use cases <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   **Vision Model Comparison**: Testing Flux Dev against Stable Diffusion for image generation, for example, generating "an image of Eiffel Tower on Mars" or "a boy dancing underwater" <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
    *   **Text-to-Text Model Comparison**: Comparing Meta Llama 3.18B Instruct and Coder 7B models for explaining basic JavaScript code with examples, relevant for an [[ai_coding_copilot_use_case | AI coding copilot use case]] or general [[using_ai_models_for_coding_assistance | AI coding assistance]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **API Access**: Provides easily accessible API documentation and code snippets (Python, cURL, JavaScript) from the playground for integration into apps <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Cost**: NVUS AI Studio is noted for offering cheaper rates compared to other AI providers <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>, with free credits available upon sign-up <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

By combining the rapid app development capabilities of Lovable with the diverse and cost-effective AI models from NVUS AI Studio, it's possible to quickly build and deploy AI-powered applications without extensive coding <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.