---
title: Qwen 3 features and advancements
videoId: b0xlsQ_6wUQ
---

From: [[aidotengineer]] <br/> 

Qwen is a series of large language models (LLMs) and large multimodal models (LMMs) with a vision of building a generalist model and agent <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The latest release, Qwen 3, represents significant progress in AI model capabilities <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Qwen 3 Models and Performance
Qwen 3 is the latest generation of large language models <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, featuring multiple sizes of dense and Mixture-of-Experts (MoE) models <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The development team believes that MoE models represent a future trend in AI <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Key Models
*   **Flagship MoE Model**: A 235 billion parameter model that only activates 22 billion parameters, making it computationally efficient yet effective <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It achieves competitive performance compared to top-tier models like GPT-3.5 and is only slightly behind Gemini 2.5 Pro <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Fast MoE Model**: A relatively smaller model with a total of 30 billion parameters, activating only 3 billion parameters <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This model can even outperform the Qwen 32 billion dense model in some tasks <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **4 Billion Parameter Model**: A very small model that utilizes advanced distillation techniques to transfer knowledge from larger models <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. Despite its size, it exhibits strong thinking capabilities and can be competitive with previous flagship models like Qwen 2.5 72B <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This model is capable of deployment on mobile devices <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **32 Billion Parameter Dense Models**: These models are strong and competitive, suitable for local deployment and reinforcement learning tasks <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

### Benchmarking
In multiple benchmarks, Qwen 2.5 Max, a precursor, achieved competitive performance against state-of-the-art models like ColossalChat 3.5, GPT-4, and DCB v3 <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The integration of reinforcement learning significantly boosts performance, especially in reasoning tasks such as math and coding, showing consistent improvement <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Core Features of Qwen 3

### Hybrid Thinking Mode
A standout feature of Qwen 3 is its hybrid thinking mode, which allows a single model to exhibit both "thinking" and "non-thinking" behaviors <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Thinking Mode**: The model reflects on itself and explores possibilities before providing a detailed answer, similar to models like GPT-4 or DeepMind's AlphaGo <a class="yt="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Non-Thinking Mode**: Functions as a traditional, near-instant chatbot without the reflective delay <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

This is presented as potentially the first time in the open-source community that these two modes are combined in a single model, controllable via prompts or hyperparameters <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

#### Dynamic Thinking Budget
Within the hybrid thinking mode, Qwen 3 introduces a dynamic thinking budget, which refers to the maximum thinking tokens allowed <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. Performance increases significantly with a larger thinking budget, especially in complex tasks like those in AM 24, where it can jump from 40% to over 80% accuracy with increased tokens <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. This allows users to balance accuracy needs with token usage efficiency <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Multilingual Support
Qwen 3 dramatically expands its language capabilities, supporting over 119 languages and dialects, a significant increase from Qwen 2.5's 29 languages <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This broad support aims to make large language models more accessible globally <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Enhanced Agent and Coding Capabilities
Qwen 3 shows specific improvements in agent and coding tasks, with enhanced support for [[future_developments_and_roadmap_for_mcp | mCP]], which has recently gained popularity <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. The model demonstrates the ability to use tools during its thinking process, making function calls, receiving environmental feedback, and continuing to think <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Examples include:
*   **Tool Use in Thinking**: The model can integrate tool usage with its thinking capabilities, receiving feedback and continuously refining its process <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This is good for inference time scaling <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Desktop Organization**: The model can access file systems, think about which tools to use, execute them, and adapt based on feedback to complete tasks like organizing a desktop <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
These advancements aim to transform the model from a simple chatbot into a productive agent in daily working life <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## Multimodal Advancements

### Qwen 2.5 VL
Qwen 2.5 VL, released in January, achieved very competitive performance in vision-language benchmarks, including understanding, math, and general VQA tasks <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. The team also explored thinking capabilities for vision-language models, finding similar inverse time scaling with larger thinking lengths <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### Qwen Omni Model
A significant step towards building a truly omni model is Qwen's 7 billion parameter model, capable of accepting multiple modalities as input and generating multiple modalities as output <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
*   **Inputs**: Accepts text, vision (images and videos), and audio <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Outputs**: Capable of generating text and audio <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **Performance**: Achieves state-of-the-art performance in audio tasks for its size and surprisingly better performance in vision-language understanding compared to Qwen 2.5 VL 7B <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
Future goals include generating high-quality images and videos to become a truly omni model <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. While there's some performance drop in language and agent tasks, the team believes this can be recovered through data quality and training method improvements <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Open-Source Philosophy and Accessibility
The Qwen team is committed to open-sourcing its models, which fosters community feedback and encourages further development <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   **Resources**: Codes are available on GitHub <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, and checkpoints are on Hugging Face <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Technical details are shared via their blog <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Model Variety**: Offers many model sizes, from 0.6 billion to 235 billion parameters, catering to a wide range of users and applications <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Quantized Models**: Provides quantized models in various formats (GGUF, GGML, AWQ, MOX for Apple) to facilitate deployment <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
*   **Licensing**: Most models are released under Apache 2.0 license, allowing free use and modification for business purposes without requiring special permissions <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
*   **Third-Party Support**: Qwen models are supported by a wide array of third-party frameworks and API platforms due to their growing popularity <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

## Product Features on Qwen Chat
Qwen also develops products to allow users to interact with their models and agents <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.
*   **WebDev**: Allows users to create websites or cards with simple prompts. For instance, inputting "create a Twitter website" generates the code and artifacts for deployment <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. Users can deploy the sites and share URLs <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. This feature enables quick creation of product introduction websites or visually appealing cards based on links <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. This showcases [[advancements_in_ai_generated_assets_and_3d_modeling | advancements in AI generated assets and 3D modeling]].
*   **Deep Research**: Users can ask the model to write comprehensive reports on specific industries or topics <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. The model plans, searches step-by-step, writes parts, and provides a downloadable PDF report <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. The team is continuously improving its quality through reinforcement learning <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.

## [[future_developments_and_roadmap_for_mcp | Future Developments and Roadmap]]
Qwen's future efforts are geared towards achieving Artificial General Intelligence (AGI) and building robust foundation models and agents <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. This represents a broader trend in [[AI technological advancements | AI technological advancements]].

### Core Areas of Focus
*   **Improved Training**: Continued belief in significant room for improvement in training, including better data cleaning, integration of multimodal data, and exploration of new training methods beyond next-token prediction, possibly incorporating reinforcement learning in pre-training <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. This relates to [[advancements_in_ai_model_technology_and_performance | advancements in AI model technology and performance]].
*   **Scaling Laws**: Shifting focus on scaling compute in reinforcement learning for long-horizon reasoning with environmental feedback <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. Models capable of interacting with the environment and continuously thinking will become smarter through inference time scaling <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.
*   **Context Scaling**: Aiming to scale context window to at least 1 million tokens this year for most models, with a long-term goal of 10 million and eventually infinite context <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   **Modality Scaling**: Increasing model capabilities and productivity by scaling modalities, particularly in vision-language understanding for creating GUI agents and enabling computer use <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. The goal is to unify understanding and generation, similar to models that generate high-quality images from text <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>.

### Training Agents
The overall strategic shift is from training models to training agents <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. This involves scaling not only with pre-training but also with reinforcement learning, especially in interaction with the environment, ushering in an "era of agents" <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>. These [[advancements_in_ai_and_future_implications | advancements in AI and future implications]] point towards more autonomous and interactive AI systems.