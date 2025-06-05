---
title: Open sourcing and applications in realworld tasks
videoId: b0xlsQ_6wUQ
---

From: [[aidotengineer]] <br/> 

Qwen is a series of large language models and large multimodal models aiming to build a generalist model and agent <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The Qwen team emphasizes open sourcing and applying their models to real-world tasks and development.

## Accessing Qwen Models and Resources

Users can interact with Qwen's latest models through various platforms:
*   **Qwen Chat:** A chat interface at chat.qwen.ai that is easy to use <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. It supports interaction with multimodal models by uploading images and videos, and with omni models using voice and video chat <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Features include webdev and deep research <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Blog:** Technical details about new releases are available on the blog at qwen.github.io <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **GitHub and Hugging Face:** Qwen's codes are available on GitHub, and model checkpoints can be downloaded from Hugging Face, allowing developers to experiment with the models <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Key Features and Capabilities Enabling Applications

### Hybrid Thinking Mode
Qwen 3 introduces a hybrid thinking mode, combining thinking and non-thinking behaviors within a single model <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Thinking Mode:** Before answering, the model reflects, explores possibilities, and then provides a detailed answer, similar to models like 01 and DeepR1 <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Non-thinking Mode:** Functions like a traditional instruction-tuned chatbot, providing near-instant answers without delay <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

This dual-mode capability is controllable via prompts or hyperparameters <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. It also allows for a dynamic thinking budget, which refers to the maximum thinking tokens <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. Performance significantly increases with larger thinking budgets, especially in tasks like math and coding <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. For example, a 32,000-token thinking budget can achieve over 80% in AM 24, compared to just over 40% with a very small budget <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. This allows users to balance accuracy and token usage based on specific task requirements <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Multilingual Support
Qwen 3 supports over 119 languages and dialects, a significant increase from Qwen 2.5's 29 languages <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This expanded linguistic support is beneficial for global applications, particularly for users of open-source models that may not have previously supported many languages well <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Agentic Capabilities and Coding
Qwen models have enhanced capabilities in agents and coding, with specific improvements for MCP <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The models can use tools during their thinking process, make function calls, receive environmental feedback, and continue thinking <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This capability is crucial for [[multiagent_systems_and_their_applications | multiagent systems]] and enables the model to be productive in real-world working life <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. An example includes organizing a desktop by accessing the file system, determining which tools to use, and iteratively thinking and executing <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### Multimodal Models
Beyond large language models, Qwen also develops multimodal models, focusing on vision-language models <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
*   **Qwen 2.5 VL:** Released in January, it achieves competitive performance in vision-language benchmarks like MMU, MathVista, and general VQA <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **Qwen-VQ:** Explores thinking capabilities for vision-language models, showing improved performance in reasoning tasks (like mathematics) with larger thinking budgets <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

The ultimate goal is to build an "omni model" that accepts multiple modalities (text, vision including images and videos, audio) as inputs and generates multiple modalities (text, audio) as outputs <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. While not yet perfect, a 7-billion parameter omni model is capable of voice, video, and text chat, and shows strong performance in audio tasks and even in vision-language understanding compared to Qwen 2.5 VL <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Future improvements aim to recover performance in language and agent tasks <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Qwen's Open Sourcing Philosophy and Benefits
Qwen is committed to [[the_role_of_open_source_models_and_community_in_ai_research | open sourcing]] their models <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Feedback and Improvement:** Open sourcing helps gather feedback from developers, which aids in improving the models <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.
*   **Community Engagement:** Interaction with the open-source community encourages the development of better models <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Diverse Model Sizes:** Qwen provides many model sizes, from very small (0.6 billion parameters) to large (235 billion parameters), catering to various user needs <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Quantized Models:** Quantized models are provided in different formats (GGUF, GGML, AWQ, MOX for Apple) to support diverse deployment scenarios <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
*   **Permissive Licensing:** Most models use the Apache 2.0 license, allowing free use and modification for business purposes without needing permission <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This supports [[commercial_and_enterprise_application_of_open_ai_models | commercial and enterprise application of open AI models]].
*   **Third-Party Framework Support:** Qwen models are widely supported by various third-party frameworks and API platforms <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
*   **Qwen Coders:** Qwen 2.5 Coders are popular for local development, and Qwen 3 Coders are currently being built <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This directly relates to [[application_of_open_ai_models_in_coding_with_agencies_like_copilot | application of open AI models in coding with agencies like copilot]] and [[integration_of_ai_into_development_environments and editors | integration of AI into development environments and editors]].

## Real-World Applications and Products
Qwen is building products to enable interaction with their models and to create agents <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.

*   **Webdev:** This feature allows users to generate and deploy websites from simple prompts <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. Examples include creating a Twitter website or a sunscreen product introduction website <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. It can also generate visually appealing cards based on provided links <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **Deep Research:** Users can ask the model to write comprehensive reports on topics of interest, such as the healthcare industry or artificial intelligence <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. The model first makes a plan, then searches step-by-step, writes parts, and finally delivers a downloadable PDF report <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. Reinforcement learning is being used to fine-tune models specifically for deep research to enhance productivity in working life <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. This capability is related to [[user_problems_and_discovery_in_ai_startups | user problems and discovery in AI startups]] by addressing the need for efficient information gathering.

## Future Directions for Real-World Impact
Qwen's future efforts are geared towards achieving Artificial General Intelligence (AGI) and building better foundation models and agents <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

*   **Training Improvements:** Continued focus on training methods, including incorporating more and better quality multimodal and synthetic data <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. Exploring new pre-training methods beyond next-token prediction, possibly using reinforcement learning in pre-training <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
*   **Scaling Laws:** Shifting focus from scaling model sizes and pre-training data to scaling compute in reinforcement learning <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. Emphasis on long-horizon reasoning with environment feedback, enabling models to become smarter through continuous interaction and thinking (inference time scaling) <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
*   **Context Scaling:** Aiming to scale context window to at least 1 million tokens this year, with aspirations for 10 million tokens and eventually infinite context <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
*   **Modality Scaling:** Increasing capabilities by scaling modalities for both inputs and outputs, even if it doesn't directly increase "intelligence" <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. This includes unifying understanding and generation, like simultaneous image understanding and generation similar to GPT-4 <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>. Vision capability, for instance, is essential for creating GUI agents for computer use <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.

These advancements signify a shift from training models to training agents, especially by integrating reinforcement learning with environment interaction <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. This highlights the ongoing evolution towards [[multiagent_systems_and_their_applications | multiagent systems]] and broader [[implementing_ai_in_enterprises | implementing AI in enterprises]].