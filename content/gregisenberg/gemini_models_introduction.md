---
title: Gemini models introduction
videoId: 6h9y1rLem4c
---

From: [[gregisenberg]] <br/> 

Gemini models are the core technology powering Google's [[introduction_to_firebase_studio | AI Studio]] and are designed to enable developers to build businesses using artificial intelligence <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. They aim to bring differentiated capabilities to life that may not be possible with other AI models or services <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Overview and Core Capabilities
[[introduction_to_firebase_studio | AI Studio]] is intended to showcase the full capabilities of the Gemini models, allowing users to explore their potential for free <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

Key capabilities highlighted include:
*   **Long Context Processing** One of the significant differentiated features is the ability to handle long contexts <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. For example, a 30-minute video tour can be processed, equating to 531,000 tokens, to extract information like a list of museum exhibits <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This capability is useful for extracting data trapped in various media formats, including long audio files like podcasts <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Multimodal Understanding** Gemini models can process and understand information from multiple modalities, including images and audio <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

## Model Variants
Within [[introduction_to_firebase_studio | AI Studio]], users can access and experiment with various Gemini models, each with different trade-offs in terms of power, cost, and intelligence <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>:
*   **2.0 Flash Model** This model is described as more powerful but also more expensive <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Flashlight Model** Offers higher rate limits and performs many core tasks, though it's slightly less intelligent than the 2.0 Flash model <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Pro Model** An experimental variant considered the most intelligent model available <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Reasoning Model** Represents the "New Frontier" of capabilities, allowing the model to "think" about different things before generating an output <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. In the UI, these thought processes are visible as "thoughts" before the final generation <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. This thinking process can involve outlining desired outcomes, code, structure, technology stack, and even MVP functionality for applications <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. The reasoning model is available for free to developers in [[introduction_to_firebase_studio | AI Studio]] and via API <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Gemma** An open-source version of the models is also available for those who require it <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

## Practical Applications and Demos
Gemini models unlock a wide range of product experiences and business opportunities <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

### Spatial Understanding
This capability allows the model to deeply understand objects and their visual representation within an image <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   It can dynamically overlay 2D bounding boxes to identify and locate items in a picture <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   This is useful for applications like furniture shopping (identifying items in a room image for search/cropping), inventory management, parking garage utilization, or satellite analysis (bounding specific areas) <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   The technology can automate painful tasks traditionally done by service-based businesses, potentially leading to multi-million dollar companies <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

### Native Function Calling
Gemini models can connect with existing products through function calling, enabling new combined experiences <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. An example is integrating with Google Maps API to create a "geoguesser" experience where the AI takes you to locations based on prompts like "take me somewhere in ancient history" <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. This capability greatly reduces the work needed to build historical SaaS product solutions <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

### Real-time Streaming (Multimodal Live API)
The multimodal live API enables real-time AI co-presence, where the AI can see and hear what the user experiences to provide relevant context and assistance <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.
*   In a demo, the model listened to spoken commands and observed a code editor on screen, offering real-time debugging assistance for a Python file <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
*   This allows for scenarios like an AI pair programmer in an IDE, seeing the user's entire screen (including browser) and understanding the full context in real-time <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.
*   It can integrate with native tools, perform code execution in a virtual environment, and use grounding to browse the internet for information, all within the product experience <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
*   This capability aims to democratize access to expertise, helping individuals learn complex skills like coding or video editing, much like having a personal tutor <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.
*   The Multimodal Live API is available for free at `audio.google.com` <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.

## Accessibility and Cost
The intention behind Gemini models and [[introduction_to_firebase_studio | AI Studio]] is to remove economic barriers for developers and startups looking to build AI products <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.
*   [[introduction_to_firebase_studio | AI Studio]] is free to use <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   API keys for Gemini models are also free by default, offering up to 1.5 billion tokens across various models <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>.
*   The starter apps that showcase different model capabilities have their code available on GitHub, allowing users to download, hack, and power them with a free API key <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.