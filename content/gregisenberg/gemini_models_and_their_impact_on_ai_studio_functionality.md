---
title: Gemini models and their impact on AI Studio functionality
videoId: 6h9y1rLem4c
---

From: [[gregisenberg]] <br/> 

[[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] is designed to showcase the full capabilities of Google's Gemini models <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Logan Kilpatrick, Lead PM for Google's [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]], emphasizes that Gemini models are the core technology bringing the [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] experience to life <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The platform aims to demonstrate differentiated features that are not possible with other AI models or services <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Developers and businesses can leverage this multi-trillion dollar technology to [[building_apps_with_ai_tools | build businesses]] and applications <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Core Capabilities Powered by Gemini

Gemini models enable a range of advanced functionalities within [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]]:

### Long Context Understanding
One of the significant advantages of Gemini models is their "long context" capability <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This allows the models to process and understand very long inputs, such as a 30-minute video or extended audio files <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

For example, a 30-minute video tour of the Natural History Museum can be fed into the model (representing 531,000 tokens), and the model can then extract specific information, such as a list of all museum exhibits mentioned in the video <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This capability makes it feasible to extract trapped data from various media, opening opportunities for [[applications_and_business_opportunities_with_ai_studio | building online directories]] or other data-driven businesses <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Multimodal Experiences
Gemini models are inherently multimodal, meaning they can process and understand different types of data (text, images, video, audio) simultaneously <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>, <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

*   **Image Analysis and Spatial Understanding:** The models can deeply understand objects and their visual representation within images <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. A demonstration shows the model identifying items in a picture and dynamically overlaying 2D bounding boxes, providing coordinates of objects <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>, <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. This generic object detection can be used for [[applications_and_business_opportunities_with_ai_studio | business ideas]] like furniture shopping websites (identifying furniture in user-uploaded room images for reverse image search) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>, inventory management (snapping pictures to track utilization) <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>, or even satellite analysis (bounding specific areas like corn fields based on criteria) <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. This capability enables automation of tasks typically handled by service-based businesses <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

*   **Real-time Streaming and AI Co-presence:** The Multimodal Live API, powered by Gemini, allows for real-time interaction where the AI can "see" and "hear" what the user is experiencing <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>, <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. This enables an "AI co-presence" where the model provides context-aware assistance <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
    *   An example shows the AI assisting a user with coding in an IDE, understanding the code, identifying errors (like "no such file or directory" or "API key not valid"), and suggesting changes in real-time <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>, <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.
    *   This capability envisions a future of work where an AI partner provides intelligence and value, making work 1.5x to 3x faster <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>, <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>. It could democratize access to learning by acting as a "senior developer" or tutor, helping individuals learn to code, edit videos, or navigate complex software <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>, <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>, <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>.

### Reasoning Models
Gemini includes "reasoning models" that are capable of complex problem-solving by simulating a "thinking process" before generating a final output <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>, <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

*   These models can go beyond simple first answers, allowing for more nuanced and structured responses <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   In [[building_apps_with_ai_tools | code generation]], a reasoning model can take a basic Python snippet and, after an internal "thought" process, generate a fully-fledged plan for a website, landing page, and SaaS app, including desired outcomes, technology stack, structure, and MVP functionalities like user authentication and dashboards <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>, <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. This thinking process, visible in the [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] UI, mirrors the outlining or planning stages a human engineer might undertake <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   The reasoning model is available for free for developers in [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] and via API key <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

### Tool and Function Calling
Gemini models support native [[tool_and_function_calling_in_ai_applications | tool and function calling]] capabilities, allowing them to connect with existing products and APIs <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>, <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.

*   An example shows [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] and Gemini integrated with the Google Maps API to create a "geoguesser" experience, where the model can respond to prompts like "take me somewhere in ancient history" by using the Maps API to display and describe relevant locations <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   This feature allows for a "combinatorial explosion" of [[innovative_ai_functionalities_in_apps | innovative AI functionalities in apps]] by merging historically separate products using AI as the bridge <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
*   Other [[tool_and_function_calling_in_ai_applications | tool integrations]] include code execution (spinning up a virtual environment and running code) <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a> and grounding (browsing the internet to find information) <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>, enabling the model to pull external context without leaving the product experience <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.

## Gemini Model Variants
[[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] provides access to various Gemini models, each with different trade-offs in power, cost, and rate limits <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>, <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **2.0 Flash Model:** More powerful and slightly more expensive <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Flashlight Model:** Higher rate limits, less intelligent but performs core tasks <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Pro Model:** An experimental variant and the most intelligent model available <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Reasoning Model:** Available for free for developers <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Gemma:** An open-source version of the models is also available <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Accessibility for Developers and Startups
Google aims to remove the economic burden for developers and startups to [[building_apps_with_ai_tools | build cool AI products]] <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

*   [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] is free to use <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   API keys are free by default, offering up to 1.5 billion tokens across Gemini models <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>.
*   The Multimodal Live experience can be prototyped for free using the API <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
*   Starter apps demonstrating various Gemini capabilities (like spatial understanding and [[tool_and_function_calling_in_ai_applications | function calling]]) have their code openly available on GitHub for download and use <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
*   Users can power experiences in other tools, such as Cursor, using their own Gemini API key obtained from [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>, <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. This enables developers to use Gemini models in their preferred [[comparison_of_ai_coding_tools | AI coding tools]] <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.