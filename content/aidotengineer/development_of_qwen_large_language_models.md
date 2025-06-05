---
title: Development of Qwen large language models
videoId: b0xlsQ_6wUQ
---

From: [[aidotengineer]] <br/> 

Qwen is a series of large language models (LLMs) and large multimodal models (LMMs) with a stated dream of building a generalist model and agent <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Qwen Resources and Products

Qwen offers several resources for interaction and development:
*   **Qwen Chat:** A chat interface available at chat.qwen.ai <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This platform allows users to interact with the latest models, including multimodal models via image and video uploads, and omni models through voice and video chat <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Blog:** Technical details and new releases are shared on the Qwen blog at qwen.github.io <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **GitHub:** Qwen maintains open-source code repositories on GitHub <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Hugging Face:** Model checkpoints are available on Hugging Face, allowing developers to download and experiment with the models <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Evolution of Qwen Models

### Qwen 2.5 Max
Released just before the Spring Festival, Qwen 2.5 Max is a large instruction-tuned model that serves as a strong foundation for larger language models <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. It demonstrated competitive performance against state-of-the-art models like Collab 3.5, GPT-4o, and DCB v3 <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The developers found that [[finetuning_of_language_models_using_quen_models | reinforcement learning]] significantly improved its performance, especially in reasoning tasks such as math and coding, with consistent gains <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. For example, a 32-billion parameter model saw its performance on AM 24 increase from approximately 65 to 80 <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Qwen 3
Qwen 3 is the latest generation of large language models, featuring multiple sizes of dense and mixture-of-experts (MoE) models <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

#### Flagship Models
*   **Qwen 3 Auto:** A MoE model with 235 billion total parameters, activating only 22 billion parameters <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It is both efficient and effective, closely trailing top-tier models like Gemini 2.5 Pro <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Largest Dense Model:** This model also exhibits very competitive performance <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

#### Smaller, Efficient Models
*   **Fast MoE Model:** A relatively small MoE model with 30 billion total parameters, activating only 3 billion <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. It can even outperform the Qwen 32 billion dense model in some tasks <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **4 Billion Parameter Model:** Despite its small size, this model incorporates advanced distillation techniques to transfer knowledge from larger models <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. It shows competitive reasoning capabilities, even comparable to the flagship Qwen 2.5 72B model <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, and can be deployed on mobile devices <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

#### Key Features of Qwen 3

*   **Hybrid Thinking Mode:** This feature allows a single model to switch between "thinking" and "non-thinking" behaviors <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   **Thinking Mode:** The model reflects, explores possibilities, and prepares a detailed answer before providing it, similar to models like Q1 and DeepR1 <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   **Non-Thinking Mode:** Functions as a traditional instruction-tuned chatbot, providing near-instant answers without a thinking delay <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   This combination, controllable via prompts or hyperparameters, is presented as a first in the open-source community <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Dynamic Thinking Budget:** A feature derived from the hybrid thinking mode, allowing users to define the maximum number of thinking tokens (e.g., 32,000 tokens) <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. Performance increases significantly with a larger thinking budget; for instance, on AM 24, performance can rise from just over 40 with a small budget to over 80 with a 32,000-token budget <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Multilingual Support:** Qwen 3 supports over 119 languages and dialects, a substantial increase from Qwen 2.5's 29 languages <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This aims to enhance global application and accessibility of [[building_and_deploying_large_language_models | large language models]] <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Enhanced Agent and Coding Capabilities:** Specific improvements have been made to support agents and coding, including enhanced support for MCP <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The models can use tools during their thinking process, receive feedback from the environment, and continue thinking, which is beneficial for inference time scaling <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Examples include using tools for calculations and organizing a desktop by accessing file systems <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. The goal is for models to be productive agents beyond simple chatbots <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

#### Open-Weighted Models
Qwen has open-weighted many models, including MoE models (30B total/3B activated, 235B total/22B activated) and six dense models <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Smaller models can be used for testing and drafting, while the 4-billion parameter model is suitable for mobile device deployment <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. The 32-billion parameter model is noted for its strength and competitiveness, suitable for [[finetuning_of_language_models_using_quen_models | reinforcement learning]] and local deployment <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. The developers believe MoE models represent a future trend <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

## Multimodal Models

Beyond LLMs, Qwen is also developing multimodal models, with a strong focus on vision-language models (VLMs) <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

### Qwen-VL and Qwen 2.5 VL
Qwen 2.5 VL, released in January, achieved competitive performance in various vision-language benchmarks, including understanding benchmarks like MMU, math benchmarks like MathVista, and general VQA benchmarks <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. Similar to LLMs, Qwen-VL models also benefit from "thinking" capabilities, showing improved performance in reasoning tasks like mathematics with a larger maximum thinking length (equivalent to thinking budget) <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### Omni Model
The long-term goal for multimodal models is to build an "omni model" capable of accepting and generating multiple modalities (text, vision, audio) <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. A current attempt is a 7-billion parameter model that accepts text, vision (images and videos), and audio inputs, and can generate text and audio outputs <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This model is used in voice, video, and text chats <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. It achieves state-of-the-art performance in audio tasks for its size and surprisingly outperforms Qwen 2.5 VL 7B in vision-language understanding tasks <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Future work includes recovering performance drops in language and agent tasks and improving data quality and training methods <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Open Sourcing and Support

Qwen is committed to open sourcing, believing it helps improve models through developer feedback and fosters community interaction <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. They offer various open-sourced models, including LLMs and coders like Qwen 2.5 coders, which are popular for [[integration_of_large_language_models_in_development | local development]] <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. Qwen 3 coders are also under development <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

Models are provided in various sizes (from 0.6 billion to 235 billion parameters) and quantized formats (GUM, GBQ, AWQ, MOX for Apple) to serve diverse user needs <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. Most models use the Apache 2.0 license, allowing free use and modification for business purposes without requiring special permission <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. Qwen models are widely supported by third-party frameworks and API platforms <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

## Applications and Products

Qwen is building products and agents to facilitate interaction with their models:

*   **WebDev:** A feature that allows users to generate and deploy websites by providing simple prompts, such as "create a Twitter website" or "create a sunscreen product introduction website" <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. It also supports creating visual cards based on links and information <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **Deep Research:** Users can prompt the model to write comprehensive reports on topics like the healthcare or artificial intelligence industry <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. The model plans its research, searches step-by-step, writes parts sequentially, and provides a downloadable PDF report <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. [[finetuning_of_language_models_using_quen_models | Reinforcement learning]] is being used to fine-tune models specifically for deep research <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.

## Future Directions

Qwen's future efforts focus on achieving AGI and building advanced foundation models and agents:

*   **Training Improvements:** There is still significant room for improvement in pre-training, including incorporating more and cleaner multimodal data, utilizing synthetic data, and exploring new training methods beyond next-token prediction, possibly involving [[finetuning_of_language_models_using_quen_models | reinforcement learning]] in pre-training <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
*   **Scaling Laws:** The focus of scaling is shifting from model sizes and pre-training data to compute in [[finetuning_of_language_models_using_quen_models | reinforcement learning]] <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. Emphasis is on long-horizon reasoning with environmental feedback, allowing models to become smarter through inference-time scaling <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
*   **Context Scaling:** Plans include scaling context length to at least 1 million tokens this year for most models, with a goal of reaching 10 million tokens and eventually infinite context <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.
*   **Modality Scaling:** While not directly increasing intelligence, scaling modalities (inputs and outputs) enhances model capability and productivity <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. This is crucial for developing agents, such as GUI agents, that require vision capabilities <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. The aim is to unify understanding and generation across modalities, such as simultaneous image understanding and generation, similar to GPT-4o <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>.

Ultimately, Qwen is moving from an era of training models to an era of training agents, focusing on [[building_and_deploying_large_language_models | scaling]] with pre-training and [[finetuning_of_language_models_using_quen_models | reinforcement learning]], especially within environments <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.