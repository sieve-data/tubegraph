---
title: Gemini models in AI Studio
videoId: 6h9y1rLem4c
---

From: [[gregisenberg]] <br/> 

[[google_ai_studio_demonstration_and_features | Google's AI Studio]] is a platform designed to showcase the full capabilities of Google's multi-trillion dollar AI technology, particularly the Gemini models <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It is led by Logan Kilpatrick, Lead PM for [[google_ai_studio_demonstration_and_features | Google's AI Studio]] and an early hire at OpenAI <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The platform aims to demonstrate differentiated features possible with Gemini that are not available with other AI models or services <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## What is AI Studio?

[[google_ai_studio_demonstration_and_features | AI Studio]] is a free-to-use platform <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a> where users can sign in with their Google account <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Its core intent is to highlight the models' capabilities <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Features include a basic prompting experience and a prompt gallery with a wide range of applications, from trip ideas to code optimization <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Gemini Models Overview

The core of the [[google_ai_studio_demonstration_and_features | AI Studio]] experience is powered by Gemini models <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Users can explore various Gemini models and find the best fit for their needs <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Different models offer trade-offs in power, cost, rate limits, and intelligence <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>:
*   **2.0 Flash model**: More powerful but more expensive <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Flashlight model**: Higher rate limits and slightly less intelligent, but capable of many core tasks <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Pro model**: An experimental variant and currently the most intelligent model available <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Gemma**: An open-source version of the models is also available <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Key Capabilities and Demos

### Long Context Processing
One of the most impressive capabilities is long context processing, which allows the models to analyze and extract information from extended media <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. For example, it can process a 30-minute video tour of a museum (531,000 tokens) to list all museum exhibits <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This capability can be used by startup builders to extract data from trapped media, for instance, to create online directories <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. It also works with long audio, enabling extraction of intelligence from podcasts <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Reasoning Models
Reasoning models allow the AI to "think" about different aspects of a prompt before generating a final output <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This thinking process, shown as "thoughts" in the UI, mimics human outlining and planning <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. For instance, a reasoning model can take a Python code snippet and generate a plan for a fully-fledged website, landing page, and SaaS application, including desired outcomes, code structure, technology stack, and MVP functionality <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This process took 23 seconds in the demo <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

*   **Accessibility**: The reasoning model is available for free for developers in [[google_ai_studio_demonstration_and_features | AI Studio]] and via API key <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Users can get an API key in [[google_ai_studio_demonstration_and_features | AI Studio]] to use the reasoning model for free in tools like Cursor <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

### Spatial Understanding (Multimodal Capabilities)
This capability allows the model to deeply understand and visually represent different objects within an image <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. It can provide 2D bounding boxes for items in a picture, dynamically overlaying them to identify objects and their coordinates <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

*   **Business Applications**: This feature unlocks applications like:
    *   Identifying furniture in a room for online shopping or reverse image search <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
    *   Inventory management by snapping pictures or using real-time video feeds to track utilization <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
    *   Real-time monitoring of parking garage utilization <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
    *   Satellite analysis to bound different areas based on criteria, such as identifying corn fields <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

### Function Calling
Function calling allows [[AI models]] to connect and interact with existing products and APIs <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. An example shown is integrating Gemini with the Google Maps API to create a "geoguesser" experience, where the model can take users to locations based on prompts like "take me somewhere in ancient history" <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. This capability enables a "combinatorial explosion" of new business opportunities by bringing together multiple disparate products with AI at their core <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

### Real-time Streaming (Multimodal Live API)
The Multimodal Live API powers real-time AI co-presence, allowing the AI to see what the user sees and gain context to provide assistance <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. In a demonstration, the model could "see" a user's code editor, understand the file name and content, and provide [[troubleshooting_and_consulting_multiple_ai_models | troubleshooting]] suggestions in real-time as the user encountered errors <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.

*   **Future of Work**: This technology represents the future of work, where an AI partner can see what a user sees (e.g., an IDE, a browser, or an entire screen) and provide real-time value and intelligence <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. It can act as a senior developer pair-programming alongside a user <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
*   **Accessibility and Democratization**: This capability can help bridge the gap in technological capabilities, assisting users who are less familiar with technology, such as learning to code or editing videos <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. It democratizes access to expert assistance <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>.
*   **Tool Integration**: The API also supports native tool integration, allowing for pseudo-function calls, code execution (spinning up a Python virtual environment), and grounding (browsing the internet for information) <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>. This creates a unified experience by bridging the outside world into the product <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
*   **Availability**: The Multimodal Live API experience is free to use <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a> via audio.google.com, where users can experiment with different voices and output formats <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

## Business Opportunities and Accessibility

The powerful capabilities of Gemini models in [[google_ai_studio_demonstration_and_features | AI Studio]] present immense opportunities for building businesses <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. They enable the automation of painful tasks traditionally performed by service-based businesses, agencies, and consulting firms, potentially leading to multi-million dollar ventures <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. The platform encourages exploration and playing with models to discover new business ideas <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.

*   **Free Resources**: [[google_ai_studio_demonstration_and_features | AI Studio]] is free to use <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.
*   **Free API Keys**: Users can get 1.5 billion tokens across various Gemini models for free today <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>. The entire multimodal live experience can be prototyped for free using the API <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   **Open Source Code**: Starter apps in [[google_ai_studio_demonstration_and_features | AI Studio]] have their code available on GitHub, allowing users to download, hack, and use them as a starting point for their own products <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
*   **Reduced Economic Burden**: The goal is to remove economic barriers for developers and startups to build AI products, with a clear path for scaling to production <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.