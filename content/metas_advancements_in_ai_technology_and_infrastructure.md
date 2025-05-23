---
title: Meta's advancements in AI technology and infrastructure
videoId: rYXeQbTuVl0
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Here is the modified article:

Meta has continued to make significant strides in the field of artificial intelligence, building upon [[llama_3_and_ai_advancements_at_meta | previous successes]] with new model releases, an expanding user base for its AI products, and a focused strategy on infrastructure development and open-source contributions.

## Llama 4 Model Family

Following the launch of Llama 3, Meta has introduced the first versions of its Llama 4 model family <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This new series aims to deliver impressive advances in AI capabilities.

### Initial Llama 4 Releases: Scout and Maverick
Meta announced four models in the Llama 4 series and has released the first two: Scout and Maverick <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   These are categorized as mid-size to small models <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   They are designed to offer high intelligence per cost <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   Key features include being natively multimodal, highly efficient, and capable of running on a single host <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   Their design prioritizes efficiency and low latency, crucial for Meta's internal use cases <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Upcoming Llama 4 Models
*   **"Little Llama"**: An 8 billion parameter model, similar in class to the popular Llama 3 8B model, is expected in the coming months <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Behemoth**: This is slated to be Meta's first "frontier" model, with over 2 trillion parameters <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Its large size necessitates significant infrastructure for post-training <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Meta is exploring how to make such a large model useful for developers, potentially through distillation into smaller, more manageable models <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

Meta plans a roadmap for Llama 4 similar to Llama 3, which saw incremental releases like Llama 3.1 (405 billion model) and Llama 3.2 (introducing multimodal capabilities) throughout the year <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Meta AI Platform

Meta AI has seen significant user adoption, with almost a billion people using it monthly <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The platform is evolving with a strong focus on personalization and new interaction modalities.

### Personalization and Context
A key area of development is enhancing the personalization loop. This involves leveraging:
*   Context from user interests, feed activity, profile information, and social graphs <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   Interactions users have directly with the AI <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
This personalization is expected to make AI interactions more compelling as the AI learns user preferences and can reference past conversations <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.

### Meta AI App and Usage
While Meta AI is most used within WhatsApp, particularly outside the U.S. <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>, a new standalone Meta AI app is being launched <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>, <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>. This app is considered strategically important for providing a first-class experience, especially in the U.S. market where WhatsApp is not the primary messaging system <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

The app includes experimental features like a demo for full-duplex voice, aiming for more natural and conversational interactions <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

## Model Capabilities and Focus

Meta's AI development prioritizes several key capabilities tailored to its product vision.

### Efficiency and Low Latency
For many consumer applications, Meta emphasizes good intelligence per cost and low latency over achieving the absolute highest scores on reasoning benchmarks that might require more compute time <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Llama 4 Scout and Maverick were specifically designed with these attributes in mind to serve Meta's internal use cases efficiently <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This is crucial for applications like responsive voice interactions in Meta's apps and devices <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>.

### Multimodality
Native multimodality is a core feature of the Llama 4 Scout and Maverick models <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This builds on the multimodal capabilities introduced in Llama 3.2 <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. This focus on handling various types of data (text, image, voice) is seen as a leading aspect compared to some text-only models like DeepSeek <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>, <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.

### Reasoning
While prioritizing efficiency for consumer products, Meta acknowledges the importance of reasoning capabilities and is developing a Llama 4 reasoning model <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. There's an observed specialization in the AI field, with some models excelling at tasks like math or coding by consuming more compute at inference time [[reasoning_in_ai_models]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Meta aims to integrate reasoning models with core language models over time <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Coding Agents
Meta is actively working on coding agents, such as the internal tool "MetaMate," to accelerate its own Llama research <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>, <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>, <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. The goal is to create agents that can understand objectives, run tests, improve code, and ultimately write higher quality code than human developers <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. It is predicted that within 12 to 18 months, most code contributing to these AI efforts could be written by AI [[impact_of_ai_on_software_development_and_productivity]] <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

## Benchmarking and Evaluation

Meta approaches AI model benchmarking with a focus on real-world product value rather than solely optimizing for standard industry benchmarks.

*   **Challenges with Standard Benchmarks**: Public benchmarks like Chatbot Arena are seen as potentially skewed towards specific, often niche, use cases that don't reflect typical user interactions within Meta's products [[challenges_and_opportunities_in_deploying_ai_at_scale]] <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Meta's "North Star"**: The primary benchmark for Meta is user value within Meta AI, measured by user feedback, reported wants, and revealed preferences through product usage <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>, <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Gameability of Benchmarks**: It's noted that many benchmarks can be "gamed," and tuning models specifically for these benchmarks might not lead to the best overall product experience <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. For instance, a version of Llama 4 Maverick could be tuned to rank highly on Chatbot Arena, but the released version is untuned for such specific benchmarks <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

## Open Source Strategy

Meta has been a proponent of open-sourcing its large language models, starting with the Llama series, which significantly impacted the [[open_source_ai_models_and_their_implications | open-source AI landscape]] <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>, <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.

### Llama License
The Llama license includes a provision requiring very large companies (those with over 700 million users, like major cloud providers or Apple) to discuss business arrangements with Meta before selling Llama models [[opensource_ai_models_and_licensing_considerations]] <a class="yt-timestamp" data-t="00:40:46">[00:40:46]</a>, <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>, <a class="yt-timestamp" data-t="00:43:15">[00:43:15]</a>. This is not intended to stop usage but to foster a productive relationship, given Meta's substantial investment in developing these models <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>. If the license becomes a deterrent to Llama adoption due to other competitive open-source options, Meta may re-evaluate this strategy <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>.

### Rationale for Open Source
*   **Control and Customization**: Building its own models allows Meta to tailor them precisely to its needs regarding architecture, size, latency, and cost, which is critical at its operational scale <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.
*   **Driving the Ecosystem**: Meta is concerned that if it stops pushing open source, other players who have recently entered the space might revert to closed models, as their initial preference was not open source <a class="yt-timestamp" data-t="00:46:24">[00:46:24]</a>, <a class="yt-timestamp" data-t="00:47:31">[00:47:31]</a>.
*   **Setting Standards with American Models**: There's a belief that AI models encode values and ways of thinking. It's considered important for American models like Llama to help shape these standards, as models can reflect cultural nuances <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>, <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>. An early Llama version translated into French, for example, was perceived by French speakers as sounding like an "American who learned to speak French" rather than a native French speaker, highlighting subtle embedded characteristics <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>.

## Infrastructure and Development

The advancement of AI is heavily reliant on significant infrastructure buildout and innovative development techniques [[challenges_and_methodologies_in_ai_research_and_development]].

### Physical Infrastructure Bottlenecks
*   Developing large-scale compute clusters, such as gigawatt-level facilities, is a time-consuming process involving permits, energy procurement (gas turbines or green energy), building construction, and navigating supply chains <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. These are described as "physical-world, human-time things" <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   There is an ongoing competition, notably with China, regarding the speed of bringing power and data centers online [[china_and_the_uss_race_in_ai_and_superintelligence]] <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>. Streamlining data center construction and energy production in the US is seen as crucial to avoid a disadvantage [[data_center_energy_requirements_and_scaling]] <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>.
*   Export controls on advanced chips impact competitors. For instance, DeepSeek's need to perform extensive low-level optimizations is attributed to using "partially nerfed chips" available in China due to these controls, diverting resources that American labs might use differently <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>, <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>.

### Model Distillation
Distillation has emerged as a powerful technique for AI development <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>, <a class="yt-timestamp" data-t="00:52:20">[00:52:20]</a>.
*   It allows capturing a significant portion (e.g., 90-95%) of a much larger model's intelligence into a substantially smaller model (e.g., 10% of the size), making it practical to run <a class="yt-timestamp" data-t="00:52:30">[00:52:30]</a>. This is particularly relevant for very large models like Behemoth <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   The growing open-source community allows for distillation from multiple sources, potentially combining strengths from different models (e.g., Llama's architecture with another model's coding proficiency) for specific use cases <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>.
*   Security is a key consideration. Distilling language models is considered "fraught" due to embedded values, unless one is willing to adopt the source model's values <a class="yt-timestamp" data-t="00:53:33">[00:53:33]</a>. For verifiable domains like reasoning and coding, distillation can be done more securely by limiting to verifiable problems and using tools like Llama Guard and Code Shield, alongside expert red teaming <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>.

### Co-evolution with Users
AI development is not solely about technical advancements; it also involves a co-evolution with users <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
*   People learning how to use AI assistants and AI assistants learning what people care about creates a crucial feedback loop <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
*   This process builds up a base of context over time, enabling richer and more personalized interactions <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.

## Future Vision and Monetization

Meta envisions AI transforming various aspects of digital interaction and creating new economic opportunities [[impact_of_ai_on_future_technology_and_society]].

### Interactive Content and Personal Assistants
*   The future of content consumption, particularly on platforms like Facebook and Instagram, is expected to shift from passive viewing (e.g., videos) to interactive AI-driven experiences. Users might talk to content, interact with it like a game, or see it change based on their input [[future_of_ai_interaction_in_everyday_life_and_personalization]] <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.
*   AI assistants are anticipated to become seamlessly integrated into daily life, accessible via phones and eventually AI-powered glasses, for continuous interaction throughout the day <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>, <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

### Monetization Strategy
Meta plans a multi-faceted approach to monetizing AI:
*   **Free, Ad-Supported Services**: For broad consumer reach, Meta will likely offer free AI services supported by advertising, similar to its existing social media model <a class="yt-timestamp" data-t="00:55:29">[00:55:29]</a>, <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>. Modern ad systems can add value if ranking is good and there's sufficient advertiser inventory <a class="yt-timestamp" data-t="00:55:48">[00:55:48]</a>.
*   **Premium Services**: For users or businesses requiring significant compute power for advanced AI tasks (e.g., "a thousand software engineering agents"), Meta anticipates offering premium, paid services <a class="yt-timestamp" data-t="00:57:14">[00:57:14]</a>, <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>.
*   **Diverse Business Models**: Different AI applications (e.g., knowledge work, entertainment, enterprise tools) will lend themselves to various business models, not solely ads <a class="yt-timestamp" data-t="00:55:23">[00:55:23]</a>.

### Impact on Work
Contrary to fears of widespread job automation, AI could increase demand in certain sectors. For example, if AI can handle 90% of customer support inquiries, it might become economically feasible for Meta to offer comprehensive voice support for its billions of users, leading to the hiring of more customer support personnel to handle the remaining complex cases <a class="yt-timestamp" data-t="01:11:35">[01:11:35]</a>, <a class="yt-timestamp" data-t="01:13:40">[01:13:40]</a>. Historically, technology has often augmented rather than simply replaced human labor <a class="yt-timestamp" data-t="01:14:06">[01:14:06]</a>.