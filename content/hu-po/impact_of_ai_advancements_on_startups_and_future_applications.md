---
title: Impact of AI advancements on startups and future applications
videoId: dPonS4kISPM
---

From: [[hu-po]] <br/> 

Recent advancements in AI, particularly with OpenAI's Sora and Google DeepMind's Gemini 1.5, are poised to significantly impact various industries and the landscape for startups. These models represent breakthroughs in generative AI and multimodal understanding, leading to both new opportunities and potential disruptions <a class="yt-timestamp" data-t="01:47:17">[01:47:17]</a>.

## Sora: State-of-the-Art Video Generation
Sora is OpenAI's new state-of-the-art video generation model <a class="yt-timestamp" data-t="03:00:03">[03:00:03]</a>. It is capable of generating longer videos with higher motion quality and overall realism compared to previous models <a class="yt-timestamp" data-t="05:54:55">[05:54:55]</a>. The model achieves this by treating visual data as patches, similar to how large language models use tokens <a class="yt-timestamp" data-t="23:19:00">[23:19:00]</a>. This allows Sora to be trained on videos and images of variable resolutions and generate entire videos in one shot <a class="yt-timestamp" data-t="31:47:04">[31:47:04]</a>, <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

### Key Features of Sora
*   **Video Generation**: Generates high-quality, long-duration videos from text prompts <a class="yt-timestamp" data-t="03:00:03">[03:00:03]</a>.
*   **Patch-Based Representation**: Converts visual data into SpaceTime patches, making it compatible with Transformer architectures that require one-dimensional sequences <a class="yt-timestamp" data-t="26:00:05">[26:00:05]</a>, <a class="yt-timestamp" data-t="23:19:00">[23:19:00]</a>. This enables processing of variable resolutions and video lengths <a class="yt-timestamp" data-t="31:47:04">[31:47:04]</a>.
*   **Data Augmentation**: Leverages GPT to expand short user prompts into longer, more detailed captions for training <a class="yt-timestamp" data-t="35:34:00">[35:34:00]</a>.
*   **Implicit World Understanding**: While not a full "world simulator" due to occasional physics inconsistencies (e.g., a person's legs flipping strangely <a class="yt-timestamp" data-t="42:49:00">[42:49:00]</a>), it demonstrates an implicit understanding of the world within its weights <a class="yt-timestamp" data-t="41:15:00">[41:15:00]</a>, <a class="yt-timestamp" data-t="01:24:06">[01:24:06]</a>.

### Future Applications of Sora
The quality of video generation achieved by Sora indicates a "step function" improvement in [[Future developments and challenges in AIgenerated simulations|3D generative content]] <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. This could lead to a significant boost in generative 3D work, which traditionally relies on pre-trained text-to-image models like Stable Diffusion for intelligence extraction <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. Potential applications include:
*   **Generative 3D Content**: Creating 3D models and environments from text prompts, similar to text-to-image <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.
*   **Robotics**: Using generated video for training and simulation in robotics <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   **Entertainment Industry**: Revolutionizing video creation and 3D content in media and gaming <a class="yt-timestamp" data-t="01:48:53">[01:48:53]</a>.

### Impact of Sora on Startups
Sora is expected to disrupt many startups, particularly those in the video and 3D content creation space <a class="yt-timestamp" data-t="01:48:43">[01:48:43]</a>. While other companies will likely rush to achieve similar capabilities, the significant investment in compute and data by large players like OpenAI creates a high barrier to entry <a class="yt-timestamp" data-t="01:48:46">[01:48:46]</a>, <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.

## Gemini 1.5: Advanced Multimodal Understanding
Gemini 1.5, developed by Google DeepMind, is a highly compute-efficient multimodal mixture of experts model <a class="yt-timestamp" data-t="45:46:00">[45:46:00]</a>. It excels in multimodal understanding and long context recall, capable of processing millions of tokens across different modalities (text, image, audio) <a class="yt-timestamp" data-t="46:53:00">[46:53:00]</a>.

### Key Features of Gemini 1.5
*   **Multimodality**: Converts various raw inputs (images, audio) into tokens that can be interleaved and processed by a single Transformer model <a class="yt-timestamp" data-t="46:06:08">[46:06:08]</a>.
*   **Long Context Window**: Achieves near-perfect recall on long context retrieval tasks, reasoning over up to 10 million tokens <a class="yt-timestamp" data-t="46:53:00">[46:53:00]</a>. This is a generational leap over existing models like GPT-4 Turbo's 128K tokens <a class="yt-timestamp" data-t="47:15:00">[47:15:00]</a>.
*   **Needle in the Haystack Retrieval**: Demonstrates exceptional ability to find specific information (e.g., an image correlating to a text description) within vast amounts of data <a class="yt-timestamp" data-t="48:12:00">[48:12:00]</a>. It can process entire books or movies and answer questions about them <a class="yt-timestamp" data-t="54:48:00">[54:48:00]</a>.
*   **Underlying Architecture (Hypothesized)**:
    *   **Mixture of Experts (MoE)**: The model uses a "mixture of experts" architecture, likely a soft MoE, where input tokens are routed to specific expert networks using a weighted average <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>, <a class="yt-timestamp" data-t="01:14:52">[01:14:52]</a>.
    *   **Ring Attention**: The drastically increased context length is suspected to be enabled by a technique similar to "ring attention," which scales context size without approximation by efficiently shuffling key-value blocks across a ring of GPUs <a class="yt-timestamp" data-t="01:05:27">[01:05:27]</a>, <a class="yt-timestamp" data-t="01:10:52">[01:10:52]</a>.

### Future Applications of Gemini 1.5
The ability of Gemini 1.5 to consume and recall information from extremely long and multimodal contexts has profound [[potential_future_impacts_and_predictions_of_ai_agents|potential future impacts and predictions of AI agents]]:
*   **Contextual AI**: Enables AI assistants to maintain context over entire conversations, personal histories, and vast document libraries.
*   **Research and Analysis**: Revolutionizes research by allowing models to analyze entire datasets, codebases, or complex documents with perfect recall.
*   **Elimination of RAG**: The concept of Retrieval Augmented Generation (RAG) systems, which use complex architectures to pull information from external databases, might become obsolete. If a model can simply ingest all relevant data into its context window, the need for intricate retrieval systems diminishes <a class="yt-timestamp" data-t="01:47:21">[01:47:21]</a>.
*   **Personal AI**: Imagine an AI agent with access to your entire digital life (text, images, audio) in context, offering highly personalized assistance without complex indexing <a class="yt-timestamp" data-t="01:48:11">[01:48:11]</a>.

### Impact of Gemini 1.5 on Startups
Gemini 1.5's capabilities, particularly its extended context window, threaten many startups built around RAG systems and context management <a class="yt-timestamp" data-t="01:47:21">[01:47:21]</a>. If core models can natively handle massive contexts, the need for middleware or specialized databases for retrieval becomes less pressing <a class="yt-timestamp" data-t="01:48:05">[01:48:05]</a>.

## Overall Impact on Startups and the Future
The advancements seen in Sora and Gemini 1.5 highlight a significant trend in [[Challenges and Advancements in AI Research|AI research]]: the increasing importance of scale (compute and data) <a class="yt-timestamp" data-t="01:50:30">[01:50:30]</a>. While innovative architectures and algorithms contribute, the sheer investment in GPU budgets and massive datasets by tech giants like OpenAI and Google is a primary driver of state-of-the-art performance <a class="yt-timestamp" data-t="35:01:02">[35:01:02]</a>.

This concentration of resources means that smaller startups face an uphill battle in competing directly with these foundational models <a class="yt-timestamp" data-t="01:50:37">[01:50:37]</a>. The future landscape suggests:
*   **Disruption of Existing Niches**: Technologies like long-context language models and high-quality video generation will likely "kill a bunch of startups" by integrating previously specialized functionalities directly into core AI models <a class="yt-timestamp" data-t="01:48:43">[01:48:43]</a>.
*   **Shift in Innovation**: Startups may need to pivot towards application layers, niche fine-tuning, or services that leverage these powerful foundation models rather than trying to build competing models from scratch.
*   **Accelerated AGI Timeline**: The rapid progress suggests that AI agents may surpass human capabilities in various tasks by late 2024 or early 2025, potentially leading to a "super intelligence" era <a class="yt-timestamp" data-t="01:50:10">[01:50:10]</a>, <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   **New Human Experience**: Future generations might spend significant portions of their lives in generated worlds, potentially internalizing the physics and realities presented by AI models rather than solely real-world experiences <a class="yt-timestamp" data-t="01:28:45">[01:28:45]</a>.

The strategic timing of releases, like Sora's launch shortly after Gemini 1.5, also demonstrates the competitive nature of the field and the importance of narrative control in AI development <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>, <a class="yt-timestamp" data-t="01:45:02">[01:45:02]</a>. While Gemini 1.5 may be more "technically impressive" for its underlying capabilities, Sora's visual nature made for a "much more appealing demo" and generated significant hype <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>.
[[Meta AI research | Meta]] and other large players, while having good models and platforms (like headsets), may face [[Future trends in machine learning software and hardware|challenges if they lack their own hardware development]] at the scale of Google's TPUs <a class="yt-timestamp" data-t="01:51:05">[01:51:05]</a>.

Ultimately, these advancements suggest a period of rapid change, where the scale of resources deployed by major tech companies will continue to drive breakthroughs, potentially rendering many existing startup models obsolete while opening doors for entirely new applications and ways of interacting with information and generated content.