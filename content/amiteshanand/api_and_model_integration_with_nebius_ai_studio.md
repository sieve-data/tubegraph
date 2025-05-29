---
title: API and model integration with Nebius AI Studio
videoId: UGbePdInPVc
---

From: [[amiteshanand]] <br/> 

Nebius AI Studio is a platform designed to serve as an AI model and inference provider, offering a comprehensive solution for integrating various AI models into applications [01:18:20]. It allows users to leverage multiple open Large Language Models (LLMs) and other AI capabilities at competitive rates [01:24:23].

## What is Nebius AI Studio?
[[Features of Nebas AI Studio | Nebius AI Studio]] is presented as a full-stack platform that enables users to access and utilize a wide array of AI models [01:24:26]. It supports:
*   **Open LLMs**: Including models like Quin DC 5, Mistral, and Meta Llama [01:26:31].
*   **Text-to-Text Models**: For generating and processing text [01:31:34].
*   **Embedding Models**: For creating numerical representations of data [01:34:36].
*   **Text-to-Image Models**: Such as Flux and Stable Diffusion, for generating images from text prompts [01:34:36, 01:16:17, 01:19:22]. The platform also plans to launch more text-to-image models [01:31:33].
*   **Vision Models**: Specifically, Quin Vision models were used for image analysis in an example application [01:10:13, 01:12:39].

## Nebius AI Playground
The platform includes a "playground" feature that allows users to test and compare different models [04:02:04, 05:04:07]. This is particularly useful for:
*   **Model Comparison**: Users can compare the performance of various models, such as different Vision models (e.g., Flux Dev vs. Stable Diffusion) or text-to-text models (e.g., Meta Llama 3.1 8B Instruct vs. 2.5 Coder 7B) [04:07:09, 04:12:14].
*   **Parameter Adjustment**: The playground allows users to set parameters and add system prompts for testing models [06:37:39].
*   **Code Snippets**: Once satisfied with a model's performance, users can directly access and copy API code snippets (in Python, Curl, or JavaScript) from the playground for [[Integration of APIs for web searching and processing | integration]] into their applications [09:55:58].

## API Integration
[[API integration with nvs AI Studio for model usage | Integrating Nebius AI Studio models]] into applications is facilitated through its API [09:03:06]. Key aspects of its API integration include:
*   **API Keys**: Users obtain API keys after logging in to access the models [09:20:23].
*   **Programming Languages**: The API can be accessed via Python, Curl, or JavaScript [09:37:39, 09:58:00].
*   **OpenAI Formatting**: The API utilizes OpenAI formatting, which simplifies integration for developers familiar with this standard [10:00:04].

## Example Application: "Do You Know"
An AI-powered app named "Do You Know" (meaning "do you know" in Hindi) was built in approximately 10 minutes using [[Using ThirdParty Tools in AI Development | Lovable]] (an AI app builder) and [[API integration with nvs AI Studio for model usage | Nebius AI Studio's Vision API]] [00:03:06, 00:08:05, 00:46:00, 01:10:13].

*   **Functionality**: The "Do You Know" app allows users to upload images or take pictures, which are then analyzed by the AI to provide interesting facts about the objects depicted [00:18:26, 06:55:58].
*   **Integration Process**: The app was instructed to use a Vision model via the [[API integration with nvs AI Studio for model usage | Nebius AI API]] through a command given to Lovable [09:03:06]. After the app was generated, [[External Tool and Database Integration with Nebius AI and Couchbase | Superbase]] was connected to store recent searches, and the Nebius AI API keys were integrated [08:16:20, 09:16:20].

## Cost-Effectiveness
Nebius AI Studio is presented as a cost-effective alternative to other AI providers, offering models at cheaper rates [10:08:11]. New users can also receive free credits upon signing up to try out the platform [10:23:25].