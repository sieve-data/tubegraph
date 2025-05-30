---
title: Open source ecosystem and model specialization
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 

Lynn Chia, co-founder and CEO of Fireworks.ai, a company focused on fast and efficient inference for compound AI systems, shared her insights on the evolving [[the_role_and_potential_of_open_source_models_in_ai | open source ecosystem]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Previously, she was one of the creators of PyTorch at Meta <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Fireworks.ai aims to deliver the best quality, lowest latency, and lowest cost for inference <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## The Vision for Compound AI Systems

Fireworks.ai envisions a future where inference systems are complex, featuring logical reasoning and access to hundreds of small expert models <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Lynn emphasizes that inference is not as simple as a single model as a service <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The problems they are solving go beyond simple API calls <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

The limitations of single models include:
*   **Non-deterministic nature:** Models are probabilistic, which is undesirable for delivering factual and truthful results <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Complexity of business problems:** Many customer problems require assembling multiple models across various modalities <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Multimodality:** Modern applications often process audio, visual, and textual information simultaneously <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Expert models within modalities:** Even within Large Language Models (LLMs), different expert models specialize in tasks like classification, summarization, or tool calling <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Knowledge limitations:** Single models are limited by finite training data, while real-world information resides behind public or proprietary APIs <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

These limitations necessitate a "compound AI system" approach, where multiple models across different modalities, along with various APIs, databases, and knowledge bases, work together to deliver optimal AI results <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## The Rise of Small Expert Models and Customization

Lynn believes the future lies in hundreds of small expert models <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. When a problem is narrowed down, it becomes easier for smaller models to excel and push quality boundaries <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This trend is highly beneficial for the [[the_evolution_and_sustainability_of_open_source_projects_with_ai | open source community]] because [[open_source_models_and_adoption_challenges | open source base models]] offer significant control for customization <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. Many model providers fine-tune and specialize models, contributing back to the [[open_source_vs_closed_source_large_language_models | open source community]] with models highly effective for specific problems <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Enterprises are moving towards having more control and steerability in this multi-model world <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

Fireworks.ai deeply believes in customization <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. The process of customization is not straightforward, but Fireworks.ai is working to make it extremely easy <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. They observe a strong trade-off between prompt engineering and fine-tuning <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

*   **Prompt Engineering:** Many developers start with prompt engineering due to its immediate results and responsiveness <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. However, it can lead to thousands of lines of system prompts, making management and changes difficult <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Fine-tuning:** When prompt engineering becomes unwieldy, fine-tuning is the next step to absorb long system prompts into the model itself <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. This is typically done after the model has proven steerable for the problem <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Fine-tuning results in faster, cheaper, and higher-quality model performance <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

While pre-training is becoming concentrated among hyperscalers <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>, some enterprises do pre-train models for core business reasons <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. However, pre-training is very expensive, and the Return on Investment (ROI) is much stronger with post-training on strong base models, allowing for more agile testing of ideas <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

## Fireworks.ai's Strategic Use of Open Source

Fireworks.ai heavily builds on the [[open_source_versus_closed_source_models_in_ai | open source community]], believing that hundreds of small expert models will emerge from it <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. Their vision aligns with leveraging this energy to build compound AI systems that utilize the best models <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>.

### The F1 Model and Function Calling

Fireworks.ai's F1 model, offered as an API, is a complex logical reasoning inference system that uses multiple models and implements logical reasoning steps <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. Building such a system is complex due to quality control challenges when models interact with each other <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

A critical aspect of compound AI systems is **function calling**, which serves as an extension point for models to call other tools and enhance answer quality <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. Function calling is complex because:
*   Models need to maintain long context in multi-turn chats to influence tool selection <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.
*   They often need to call multiple tools (potentially hundreds) in parallel or sequentially <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   Precision in tool calling and driving composition is crucial <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.

Fireworks.ai's function calling capability handles parallel and sequential complex planning and orchestration <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. They strategically invest in this area, which is a critical ingredient for tying everything together in a compound AI system <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.

### Integration with Other Tools

Fireworks.ai maintains compatibility with imperative agentic tools like LangChain, seeing them as strong partners rather than competitors. This allows Fireworks.ai to simplify the layer above single models by composing multiple models where it makes sense <a class="yt-timestamp" data-t="00:38:17">[00:38:17]</a>.

## The Role of Hyperscalers and Meta's Open Source Strategy

Hyperscalers aim to build vertically integrated stacks, like Apple's iPhone, leveraging massive resources for data centers, power, and machine deployment <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>. Fireworks.ai specializes in problems requiring engineering craftsmanship and deep research, deploying scalable systems on top of GPU clouds <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

Meta is a significant contributor to the [[the_role_and_potential_of_open_source_models_in_ai | open source ecosystem]] through its Llama models and the "Llama Stack" initiative to standardize tools around Llama <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>. Meta's ambition is to create an "Android world" for AI, with standardized, easily pluggable components <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>. Lynn anticipates continuous investment from Meta in training new models like Llama 4 <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>.

The investment in pre-training may slow down when the ROI diminishes, likely due to hitting a "data wall" as common internet and synthetic data sources become exhausted <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. Lynn observes that investment is already shifting from pre-training to post-training and then to inference <a class="yt-timestamp" data-t="00:37:43">[00:37:43]</a>.

## The Impact of Generative AI

The advent of Generative AI (GenAI), particularly [[openais_o1_model_and_systemlevel_innovation | ChatGPT]], fundamentally changed the accessibility of AI technology <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>. Before GenAI, companies needed to hire large machine learning teams to train models from scratch, which was time-consuming and required scarce talent <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>. GenAI's foundation models, which absorb vast amounts of knowledge, allow developers to build on top of them directly or with minimal fine-tuning <a class="yt-timestamp" data-t="00:43:22">[00:43:22]</a>. This drastically lowers the barrier to entry, enabling application and product teams to build without needing large machine learning teams, leading to rapid adoption <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>. The fact that most GenAI models are PyTorch-based also aligned well with Fireworks.ai's expertise in operating complex PyTorch models in production <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.

## Overhyped vs. Underhyped

Lynn considers the perception of GenAI as "magical" and a "recipe for all problems" to be overhyped <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>. She reiterates her belief that no single model can solve all problems in the best or correct way <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>. The underhyped aspect is not explicitly stated but implied through her emphasis on specialized models and compound systems to address the limitations of single, "magical" models.

Lynn also noted a shift in the adoption curve for AI. Initially, she expected startups to lead, followed by digital natives, and then traditional enterprises <a class="yt-timestamp" data-t="00:50:25">[00:50:25]</a>. However, all three are adopting AI simultaneously, with significantly shorter sales cycles and a tremendous appetite for the technology <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

Ultimately, Fireworks.ai's strategy remains anchored in the belief that specialization and customization are the future, regardless of how core model capabilities evolve <a class="yt-timestamp" data-t="00:48:16">[00:48:16]</a>. They provide an inference optimizer that takes workload and customization objectives as input, spitting out optimized deployment configurations and potentially adjusted models, making customization simple and closing the loop for developers <a class="yt-timestamp" data-t="00:48:58">[00:48:58]</a>.