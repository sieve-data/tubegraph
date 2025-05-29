---
title: Business applications of AI prompting
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

The field of artificial intelligence (AI) is rapidly evolving, with new reasoning models like DeepSeek R1 offering [[impact_of_ai_on_business_efficiency | superhuman capabilities]] for various tasks. Understanding how to effectively prompt these models is crucial for businesses aiming to leverage AI for efficiency and growth <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Introduction to DeepSeek R1 and Reasoning Models

DeepSeek R1 is an advanced AI model developed in China, notable for its reasoning capabilities, allowing it to "think" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It is open-source and freely available on its website, deepseek.com, making it accessible for study and use <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This model is considered on par with OpenAI's 01 reasoning model <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. These advanced models are designed to process complex instructions and spend more time analyzing input, leading to superior outputs compared to earlier versions <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

## Data Privacy and Hosting Options for Businesses

A significant consideration when [[utilizing_ai_for_internal_business_communication | utilizing AI for internal business communication]] is data privacy, especially when using publicly hosted services <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
<br>
> "I would be very careful as far as anything you put into this system as far as if you have any sensitive data because it would not belong to a region that you know you may live in or have control in." <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>

When using deepseek.com directly, data is hosted in China, subject to their regulations <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This poses a risk for sensitive business data <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Alternatives for businesses to maintain data control include:

*   **API Providers**: Using web UIs that connect to API providers like Fireworks AI or Groq, which can host models in regions like North America <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. These providers offer access to models like DeepSeek R1 without sending data directly to the originating host <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Local Hosting**: Running models directly on your machine using tools like Open Web UI and Ollama <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This ensures data never leaves your device, allowing for private business operations, even offline <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Setting up Local AI Models

To run AI models locally and ensure data privacy for business purposes, you can follow these steps <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>:

1.  **Download Docker**: Install Docker Desktop for your operating system (e.g., Apple Silicon for Mac) <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
2.  **Install Open Web UI**: This provides a user-friendly interface similar to ChatGPT <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.
    *   Pull the Open Web UI Docker container <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.
    *   Run the container (use `--gpus all` for NVIDIA GPUs to leverage local processing power) <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
    *   Access the UI via `localhost:3000` <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
3.  **Download Ollama**: Install Ollama to download and manage local AI models <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>.
    *   Once installed, Ollama runs in the background and allows you to pull models like DeepSeek R1 locally <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.
    *   In Open Web UI, configure Ollama as an API connection to access downloaded models <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.

This setup allows businesses to perform complex AI tasks while keeping sensitive data on their own machines, crucial for lawyers, doctors, and other professionals <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Mobile Application for Local AI

The Apollo app allows users to download and run AI models directly on mobile devices <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>. It uses the device's memory to host models, enabling offline usage of reasoning models, even on a phone <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>. This capability could lead to [[innovative_ai_functionalities_in_apps | innovative AI functionalities in apps]] for on-the-go business tasks <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## Practical Business Applications

### Content Generation and Analysis
One powerful [[automating_business_processes_with_ai | business process automation with AI]] is generating content from existing media. For instance, transcribing live streams or videos and then using an AI model to create a blog post <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This is akin to "hiring an admin" to process information and produce marketing materials <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

The quality of output from advanced reasoning models like DeepSeek R1 can be "human level incredible," requiring minimal human intervention <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. Compared to older models like ChatGPT, which might provide a "thought starter" needing significant human "rejigging," DeepSeek R1 can produce a polished blog post, including analysis, geopolitical implications, future predictions, and key takeaways, sometimes even generating graphs <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

### Optimizing AI Prompting
To maximize the utility of these models, particularly for [[using_ai_tools_for_business_growth | business growth]], businesses should focus on [[designing_with_ai_prompt_clarity | designing with AI prompt clarity]].

*   **Chaining Prompts**: [[Sequential prompting with AI tools | Advanced chaining prompts]] allow models to "think through" large amounts of text and perform complex analysis <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This means giving the AI a series of instructions that build upon each other.
*   **Prompt Refinement**: Tools like OpenAI's playground (platform.openai.com) can help reconfigure simple prompts into more detailed, efficient instructions for language models <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. When crafting prompts, consider:
    *   Desired instructions <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>
    *   Expected output format <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>
    *   Undesired outputs <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>
*   **Temperature Settings**: Adjusting the "temperature" parameter influences the model's creativity <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>. Lower temperatures (e.g., 0.8 default to lower) lead to less "hallucination" and better adherence to instructions, ideal for logical tasks like code generation <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. Higher temperatures (e.g., 1) encourage creative, out-of-the-box thinking, suitable for creative writing <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.

## The AI Model Ecosystem and Future Outlook

The performance of AI models is linked to their parameter count; larger models (e.g., 600 billion+ parameters) have more intelligence but take longer to process <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. "Distilled models" are smaller, faster versions, though they may offer less detailed responses <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Businesses should experiment to find the right model for their specific tasks <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

The growing demand for hosting these powerful models is fueling an "AI arms race" for GPUs and hosting services <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. Providers like Fireworks AI and Groq are essential for businesses seeking reliable and regionally compliant hosting <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Pricing models, typically based on tokens, can significantly impact costs as AI [[integration_of_ai_in_business_plan_development | integrates into business workflows]] <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

Future models like OpenAI's 03 and Omni models are expected to bring further breakthroughs, including the ability to understand audio nuances, tone, and micro-expressions, which could revolutionize applications like negotiation assistance <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>. These advancements highlight the potential for new [[use_cases_for_ai_agents_in_business_operations | AI agents in business operations]].

The accessibility of these powerful AI models, even on personal devices, creates an "unfair advantage" for startups and businesses <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. The ability to experiment with different models through platforms like Ollama and user interfaces like Open Web UI empowers individuals to discover specific AI solutions for their needs <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

For individuals new to AI, starting with basic prompting and understanding where data is processed is key <a class="yt-timestamp" data-t="00:50:45">[00:50:45]</a>. The ease of getting started, often requiring only English descriptions, allows users to quickly harness the intelligence of these models <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The ongoing development in the AI space means that what seems complex today will become more efficient and affordable over time <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.