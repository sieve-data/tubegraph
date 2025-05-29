---
title: Demo of AI Studio functionalities and its applications
videoId: 6h9y1rLem4c
---

From: [[gregisenberg]] <br/> 

Logan Kilpatrick, the lead Product Manager for Google's [[introduction_to_google_ai_studio_and_its_capabilities | AI Studio]], provides an in-depth walkthrough of the platform, highlighting its capabilities and potential for [[business_opportunities_using_ai_studio_and_machine_learning_models | building businesses using AI]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This episode, featured on the [[tutorial_on_ai_tools_and_startup_ideas | Startup Ideas Podcast]], aims to showcase the power of Google's multi-trillion dollar technology <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Introduction to AI Studio

[[introduction_to_google_ai_studio_and_its_capabilities | AI Studio]] is designed to showcase the full capabilities of Google's AI models <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It is currently free to use, allowing users to explore its differentiated features <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Core Features

*   **Basic Prompting Experience**: Users can interact with the models through a simple left-hand navigation interface <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **Prompt Gallery**: A diverse collection of prompts is available, demonstrating the models' wide range of applications, from generating trip ideas to optimizing code and performing image analysis <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

> [!example] Image Analysis
> The system can analyze an image of a hurricane, performing OCR (Optical Character Recognition) to extract information and context from the visual <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Long Context Use Cases

One of the most impactful features is the ability to handle "long context" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

> [!example] Extracting Information from Long Videos
> [[practical_examples_of_ai_project_development | AI Studio]] can process a 30-minute video, such as a tour of the Natural History Museum, and extract specific information. For instance, it can generate a list of all museum exhibits mentioned throughout the video, processing up to 531,000 tokens for such a video <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This task would be "basically impossible" to do manually without these models <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

> [!info] Business Opportunity
> The ability to extract structured data from long-form media like videos or audio (e.g., podcasts) creates opportunities for [[business_opportunities_using_ai_studio_and_machine_learning_models | building online directories]] or gaining deep intelligence <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Gemini Models and Their Capabilities

The [[gemini_models_and_their_impact_on_ai_studio_user_experience | Gemini models]] are the core technology powering the [[introduction_to_google_ai_studio_and_its_capabilities | AI Studio]] experience <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Users can experiment with various models to find the best fit for their needs <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

*   **Gemini 2.0 Flash**: More powerful and slightly more expensive <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Gemini Flashlight**: Has higher rate limits and is less intelligent but can perform many core tasks <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Gemini Pro**: An experimental variant and the most intelligent model available <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Reasoning Model**: This model represents a "New Frontier" in AI capabilities <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. It's free for developers to use in [[introduction_to_google_ai_studio_and_its_capabilities | AI Studio]] or via an API key <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Reasoning Model in Action

The reasoning model is designed to "think" about different things before generating an output <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

> [!example] Code to SaaS App
> By providing a basic Python code snippet that sends a request to the Gemini API, the reasoning model can be prompted to convert it into a fully-fledged website, landing page, and SaaS application <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The model displays its "thoughts" in the UI, outlining the desired outcomes, code structure, technology stack, landing page optimization, and MVP for SaaS functionality (e.g., user authentication, dashboard, image generation tools) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. This thought process mirrors human outlining before writing code or essays <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. The total runtime for this complex generation was 23 seconds <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

This model can be used freely in tools like Cursor by obtaining an API key from [[introduction_to_google_ai_studio_and_its_capabilities | AI Studio]] <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## Starter Apps

[[introduction_to_google_ai_studio_and_its_capabilities | AI Studio]] offers starter apps to demonstrate the "art of the possible" with different model capabilities <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. The code for all starter apps is available on GitHub for download and modification <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

### Spatial Understanding

This capability allows the model to deeply understand objects and their visual representation within an image <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

> [!example] 2D Bounding Boxes
> An example shows the model dynamically overlaying 2D bounding boxes on items within a picture, identifying their positions <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. This is a demonstration of multimodal capabilities and generic object detection <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

> [!info] Business Applications
> This technology can be applied to:
> *   **Furniture Shopping**: Identifying and cropping specific furniture items from busy images to enable reverse image search <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
> *   **Inventory Management**: Snapping pictures or using real-time video feeds to monitor item utilization <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
> *   **Parking Garages**: Real-time monitoring of utilization <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
> *   **Satellite Analysis**: Bounding specific areas based on criteria, e.g., identifying corn fields for meta-analyses <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
> *   **Automating Service Businesses**: Using technology to automate painful tasks historically done by human agencies or consulting firms <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

### Native Function Calling

[[building_apps_with_ai_tools | AI Studio]] and [[gemini_models_and_their_impact_on_ai_studio_user_experience | Gemini]] can be hooked up to other APIs, creating new experiences through "combinatorial explosion" <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

> [!example] Google Maps GeoGuesser
> An example demonstrates integration with the Google Maps API, creating a thin GeoGuesser experience. The model can interpret prompts like "take me somewhere in ancient history" and display relevant locations with descriptive context <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

This ability to combine disparate products with AI in the middle can quickly lead to real business solutions, with significantly less development work compared to historical SaaS products <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

## Real-time Streaming (Multimodal Live API)

The Multimodal Live API enables real-time streaming, allowing AI to be "co-present" in user experiences by seeing and understanding what the user sees to provide contextual help <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.

> [!example] Real-time Code Debugging
> In a live demo, the model listens to the user, sees their code editor (e.g., a Python file using the Gemini API), and provides real-time debugging assistance. It identifies issues like incorrect file paths or missing API keys based on error messages <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

> [!info] Future Vision
> This technology hints at a future where AI acts as a "senior developer" or tutor, pair programming in an IDE, seeing the entire screen, including browser content, to offer real-time assistance <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>. This could significantly democratize access to learning and problem-solving, helping users at various technical skill levels <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. It's envisioned as the future of work, allowing users to complete tasks 1.5x, 2x, or even 3x faster <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.

Additional features include:
*   **Native Tool Integration**: Pseudo function calls and code execution, which can spin up a Python virtual environment and run code <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
*   **Grounding**: Enables the model to browse the internet to find information, allowing it to provide relevant context without the user leaving the product experience <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.

This real-time multimodal experience is available for free at audio.google.com, with options to change voices and output formats <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

## Accessibility and Economic Burden

Google aims to remove the economic burden for developers and startups wanting to [[building_successful_ai_apps | build cool AI products]] <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>. [[introduction_to_google_ai_studio_and_its_capabilities | AI Studio]] is free, and API keys for [[gemini_models_and_their_impact_on_ai_studio_user_experience | Gemini models]] offer free access to 1.5 billion tokens, including the Multimodal Live experience for prototyping <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>. A path for scaling to production is also available <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>.