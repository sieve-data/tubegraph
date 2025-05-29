---
title: Demonstration of AI Studio features and use cases
videoId: 6h9y1rLem4c
---

From: [[gregisenberg]] <br/> 

Google [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] is a platform designed to showcase the full capabilities of Google's advanced AI models, particularly the [[gemini_models_and_their_impact_on_ai_studio_functionality | Gemini models]]. It allows users to experiment with AI tools and develop [[applications_and_business_opportunities_with_ai_studio | business opportunities using AI]] by leveraging Google's multi-trillion dollar technology [00:00:07].

Logan Kilpatrick, the lead Product Manager for Google's [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]], describes the platform as a way to appreciate the differentiated capabilities of Gemini and to explore future AI "co-presence" experiences [00:01:25]. The goal is to remove economic barriers for developers and startups to build cool AI products [00:29:07].

## Getting Started

Users can sign into [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] for free using their Google account [00:02:34]. There are no costs involved with using the platform to explore its differentiated features [00:02:45].

## Key Features and Demonstrations

### Basic Prompting and Prompt Gallery

The platform features a basic prompting experience with a left-hand navigation [00:02:57]. A "Prompt Gallery" offers a wide range of examples, from generating trip ideas to optimizing code [00:03:09]. It can also perform tasks like Optical Character Recognition (OCR) by extracting information from images, such as analyzing a hurricane image to pull out context [00:03:28].

### Long Context Capabilities

One of the significant capabilities of [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] is its handling of long context [00:02:52].

*   **Demonstration**: A 30-minute video of a Natural History Museum tour was uploaded to the platform [00:04:00]. The model was then prompted to "write me a list of all the museum exhibits throughout this video" [00:04:07]. The video required 531,000 tokens for processing [00:04:53].
*   **Use Cases**: This capability can be leveraged to create online directories by extracting trapped data from various media formats [00:05:11]. It can also extract intelligence from long audio, such as podcasts, for platforms [00:06:01].

### Gemini Models Overview

[[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] primarily utilizes [[gemini_models_and_their_impact_on_ai_studio_functionality | Gemini models]], including the open-source Gemma versions [00:07:17]. Different models offer various trade-offs:
*   **2.0 Flash Model**: More powerful and slightly more expensive [00:07:39].
*   **Flashlight Model**: Has higher rate limits and is less intelligent but capable of core functions [00:07:43].
*   **Pro Model**: An experimental variant and the most intelligent model available [00:07:49].

### Reasoning Models

[[gemini_models_and_their_impact_on_ai_studio_functionality | Reasoning models]] represent "New Frontier capabilities" [00:08:04] and are available for free to developers within [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] or via API key [00:08:07].

*   **Demonstration**: A basic Python code snippet for sending a request to the Gemini API was provided [00:09:05]. The model was prompted to "turn this code snippet into a fully fledged website plus Landing Page Plus SAS app that is called [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]]" [00:09:10].
*   **Thinking Process**: Before generating the final output, the model displayed its "thoughts" in the UI [00:10:16]. This thinking process involved outlining desired outcomes, code, structure, technology stack, landing page optimization (subheaders, features, CTA, visuals), and an MVP for SaaS functionality including user authentication, a dashboard, and image generation tools [00:10:52]. This detailed planning mimics a human engineer's approach [00:10:37]. The total runtime for this process was 23 seconds [00:12:15].
*   **Output**: The model provided fully-fledged content and code, although some details like HTML and CSS might be omitted, which can be requested through follow-up prompts [00:11:55].
*   **Accessibility**: Users can obtain a free API key from [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] to use the reasoning model in other tools like Cursor [00:12:50].

## Starter Apps for Use Cases

[[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] provides three simple starter apps to demonstrate various model capabilities, with all code available on GitHub for download and modification [00:13:26], [00:19:38].

### Spatial Understanding

This capability allows the model to deeply understand objects and their visual representation within images [00:13:50].

*   **Demonstration**: A UI experience prompts the model to identify the position of items in a picture using 2D bounding boxes [00:14:09]. The model dynamically overlays these bounding boxes and provides the coordinates of objects [00:14:20].
*   **[[applications_and_business_opportunities_with_ai_studio | Business Opportunities]]**:
    *   **[[using_ai_tools_for_design | Furniture Shopping]]**: Identifying and cropping furniture items from busy images to facilitate reverse image searches [00:14:39].
    *   **Inventory Management**: Snapping pictures or using real-time video feeds to monitor the utilization of items in inventory [00:15:56].
    *   **Parking Garages**: Real-time monitoring of parking space utilization [00:16:16].
    *   **Satellite Analysis**: Bounding specific areas based on criteria, such as identifying corn fields for meta-analyses [00:16:28].
    *   **Service Automation**: Automating painful, labor-intensive tasks for service-based businesses, such as agencies or consulting firms, that historically required human effort [00:16:52].

### Native Function Calling

This feature allows [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] and [[gemini_models_and_their_impact_on_ai_studio_functionality | Gemini models]] to connect with existing products through APIs.

*   **Demonstration**: A "thin Geoguesser experience" was built by hooking [[overview_of_google_ai_studio_and_links | AI Studio]] to the Google Maps API [00:18:18]. When prompted to "take me somewhere in ancient history," the model showed an isolated island and provided contextual information about its biodiversity, trade routes, and archaeological remains [00:18:41].
*   **[[applications_and_business_opportunities_with_ai_studio | Business Opportunities]]**: Combining two historically separate products with AI in the middle can lead to a "combinatorial explosion" of new business opportunities with relatively little work compared to historical SaaS solutions [00:19:09].

### Real-time Streaming (Multimodal Live API)

The multimodal live API enables AI to be "co-present" in user experiences, seeing what the user sees and providing relevant context [00:20:11].

*   **Demonstration**: The model listened to the user's speech and simultaneously analyzed a shared screen displaying a Python code editor [00:20:35]. The AI identified the file (`f.py`), its use of the Gemini API [00:20:52], and then troubleshooted errors as the user attempted to run the code. It accurately identified issues like "no such file or directory" due to being in the wrong directory and "API key not valid" due to placeholder text [00:21:13].
*   **[[applications_and_business_opportunities_with_ai_studio | Business Opportunities]]**:
    *   **[[developing_a_user_interface_using_ai_tools | AI Pair Programmer]]**: An AI co-present in an Integrated Development Environment (IDE) that provides real-time assistance, like a senior developer, seeing the entire screen (browser, etc.) [00:23:24].
    *   **Automated Assistance**: Helping users, even those with limited technical familiarity (like a mom learning to code or edit video in Adobe Premiere), by providing real-time guidance and democratizing access to learning [00:24:14], [00:27:18].
    *   **Future of Work**: An [[use_cases_for_ai_agents_in_business_operations | AI partner]] that sees what you're seeing, providing value and intelligence to accelerate work efficiency (1.5x, 2x, 3x faster) [00:24:52], [00:25:17].
*   **Additional Capabilities**: The real-time console supports native tool integrations, pseudo function calls, code execution in a Python virtual environment, and "grounding" for internet browsing [00:25:32]. This allows the model to provide information from the outside world without leaving the product experience [00:26:16].

## Accessibility and Cost

Google aims to remove the economic burden for developers and startups [00:29:07]. [[overview_of_google_ai_studio_and_its_capabilities | AI Studio]] is free to use [00:02:45], and API keys are also free, offering up to 1.5 billion tokens across various [[gemini_models_and_their_impact_on_ai_studio_functionality | Gemini models]] [00:28:49]. The entire multimodal live experience can be prototyped for free today [00:28:57]. This provides a path for scaling to production when needed [00:29:22].