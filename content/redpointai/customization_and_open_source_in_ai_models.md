---
title: Customization and open source in AI models
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 

Fireworks, an inference-focused generative AI platform, envisions a future where AI systems are complex, involving logical reasoning and access to hundreds of small, expert models <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. The company aims to deliver the best quality, lowest latency, and lowest cost inference <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Limitations of Single AI Models

Traditional single AI models have several inherent limitations:
*   They are probabilistic by nature, making them undesirable for delivering consistently factual or truthful results <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Solving complex business problems often requires assembling capabilities from multiple models across different modalities <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   Even within the same modality, such as Large Language Models (LLMs), there are many expert models specializing in tasks like classification, summarization, multi-turn chats, or tool calling, each with slight differences <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   Single models are limited by their training data, which is finite and not infinite <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Much real-world information exists behind APIs, both public and proprietary, which models cannot access directly <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

To overcome these limitations, the industry needs to move [[enterprise_use_of_ai_and_model_specialization | beyond single-model-as-a-service]] to "compound AI systems" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. These systems involve multiple models across various modalities, integrated with different APIs that hold knowledge from databases, storage systems, and knowledge bases, all working together to deliver optimal AI results <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

## The Role of Customization

Fireworks believes deeply in customization <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. The nature of model training means that no single model fits all problems <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Training is an iterative process where developers pick specific problem subsets to optimize, devoting significant resources to data acquisition and quality in those areas <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Consequently, a model will excel at certain tasks but perform poorly at others <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

The future of AI models is seen as hundreds of small, expert models <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. When a problem is narrowed down, it becomes easier for smaller, specialized models to achieve high quality <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Customization Strategies

1.  **Prompt Engineering**: Many enterprises start with prompt engineering due to its immediate, responsive, and interactive nature <a class="yt-timestamp" data-t="00:10:58">[00:11:00]</a>. However, this approach can become cumbersome with thousands of lines of system prompts, making further steerability difficult <a class="yt-timestamp" data-t="00:11:16">[00:11:22]</a>.
2.  **Fine-tuning**: When prompt engineering becomes unmanageable, [[building_custom_ai_models_for_enterprises | fine-tuning]] is the prime time to absorb lengthy system prompts into the model itself <a class="yt-timestamp" data-t="00:12:00">[00:12:02]</a>. This means the model has already proven its ability to solve the problem and follow instructions <a class="yt-timestamp" data-t="00:12:07">[00:12:12]</a>. Fine-tuning allows the model to run faster, cheaper, and with higher quality <a class="yt-timestamp" data-t="00:12:30">[00:12:35]</a>.
3.  **Pre-training**: While some enterprises pre-train models for core business reasons, it is very expensive in terms of money and human resources <a class="yt-timestamp" data-t="00:12:54">[00:13:16]</a>. The Return on Investment (ROI) is much stronger with [[open_source_models_versus_proprietary_ai_models | post-training (fine-tuning) on top of strong base models]], as it allows for more agile testing of ideas <a class="yt-timestamp" data-t="00:13:36">[00:13:43]</a>. The industry is currently seeing investment shift from pre-training to post-training and then to inference, indicating a "soft wall" in data availability for pre-training <a class="yt-timestamp" data-t="00:37:43">[00:37:52]</a>.

## The Role of [[open_source_ai_models_and_limitations | Open Source Models]]

[[impact_of_open_source_models_in_ai_development | Open source models]] play a crucial role in enabling customization <a class="yt-timestamp" data-t="00:09:15">[00:09:20]</a>. They provide control and allow model providers to focus on post-training or fine-tuning, delivering specialized models back to the community that are highly effective at solving specific problems <a class="yt-timestamp" data-t="00:09:28">[00:09:39]</a>.

Meta, through its Llama models and the Llama Stack standard, is working to standardize tools around Llama models, fostering an "Android world" where components are easily pluggable and adoptable <a class="yt-timestamp" data-t="00:36:00">[00:36:07]</a>. This continuous investment from Meta (e.g., Llama 4 is expected) is driven by the ROI in pre-training, which will continue until a data wall is hit <a class="yt-timestamp" data-t="00:36:45">[00:37:27]</a>.

## Fireworks' Approach to Complex AI Systems

Fireworks builds its offerings on top of [[open_source_ai_models_and_limitations | open source models]] <a class="yt-timestamp" data-t="00:23:55">[00:23:57]</a>, believing that hundreds of small expert models will emerge from the open-source community <a class="yt-timestamp" data-t="00:24:01">[00:24:05]</a>. Their strategic investment is in the "compound AI system" layer, which focuses on composing these small expert models to solve complex business tasks efficiently <a class="yt-timestamp" data-t="00:24:10">[00:24:20]</a>.

### F1: A Compound AI System

Fireworks developed F1, a model API that functions as a complex logical reasoning inference system <a class="yt-timestamp" data-t="00:19:32">[00:19:41]</a>. Underneath, F1 comprises multiple models and implements logical reasoning steps <a class="yt-timestamp" data-t="00:19:52">[00:20:02]</a>. Building such a system is more complex than a single-model-as-a-service inference <a class="yt-timestamp" data-t="00:20:04">[00:20:10]</a>, involving significant challenges in quality control when models communicate with each other <a class="yt-timestamp" data-t="00:20:20">[00:20:34]</a>.

### Function Calling for Agents

A critical component of compound AI systems and agents is function calling <a class="yt-timestamp" data-t="00:21:10">[00:21:14]</a>. This allows models to call external tools to enhance answer quality <a class="yt-timestamp" data-t="00:21:40">[00:21:44]</a>. Function calling is complex, often requiring the model to:
*   Maintain a long context of conversation in multi-turn chats <a class="yt-timestamp" data-t="00:21:57">[00:22:05]</a>.
*   Select from potentially hundreds of tools <a class="yt-timestamp" data-t="00:22:14">[00:22:17]</a>.
*   Execute multiple tools in parallel or sequentially, requiring complex coordination and planning <a class="yt-timestamp" data-t="00:22:25">[00:22:30]</a>.
*   Possess strong capability to understand when and how to use a tool, driving precision <a class="yt-timestamp" data-t="00:23:14">[00:23:20]</a>.

Fireworks has invested in function calling capabilities for about a year <a class="yt-timestamp" data-t="00:23:26">[00:23:29]</a>, recognizing its strategic importance in tying everything together within a compound AI system <a class="yt-timestamp" data-t="00:24:48">[00:24:50]</a>.

## Evolution of Product Development and Go-to-Market Strategy

Initially, Fireworks catered to developers needing to train models from scratch <a class="yt-timestamp" data-t="00:43:07">[00:43:09]</a>. However, the advent of generative AI, particularly with foundational models like ChatGPT, fundamentally changed accessibility <a class="yt-timestamp" data-t="00:43:12">[00:43:26]</a>. Now, companies don't need large machine learning teams to curate data and train models from scratch <a class="yt-timestamp" data-t="00:43:16">[00:43:22]</a>. Instead, they can build directly on existing foundation models or fine-tune them with thousands of samples <a class="yt-timestamp" data-t="00:43:28">[00:43:33]</a>. This increased accessibility led Fireworks to laser-focus on generative AI, leveraging their expertise in PyTorch <a class="yt-timestamp" data-t="00:43:57">[00:44:17]</a>.

The adoption curve for AI technology has changed dramatically, with startups, digital natives, and even traditional enterprises adopting it concurrently <a class="yt-timestamp" data-t="00:50:41">[00:50:47]</a>. This differs from traditional sequential adoption models <a class="yt-timestamp" data-t="00:50:25">[00:50:27]</a>. The sales cycle is shorter, and procurement processes are more open to new thinking <a class="yt-timestamp" data-t="00:51:35">[00:51:43]</a>.

While startups often prefer access to low-level abstractions to assemble components, traditional enterprises typically desire higher-level abstractions that hide complex details <a class="yt-timestamp" data-t="00:51:57">[00:52:30]</a>. Fireworks offers multiple abstraction layers to cater to these different needs <a class="yt-timestamp" data-t="00:52:33">[00:52:46]</a>.