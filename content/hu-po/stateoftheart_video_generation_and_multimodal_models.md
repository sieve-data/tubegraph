---
title: Stateoftheart video generation and multimodal models
videoId: dPonS4kISPM
---

From: [[hu-po]] <br/> 

The field of artificial intelligence recently saw significant advancements with the release of two prominent models: OpenAI's Sora and Google DeepMind's Gemini 1.5. While serving different primary functions—video generation and multimodal understanding, respectively—their introductions ignited considerable discussion about the direction and capabilities of modern AI. The timing of their releases, with Sora following Gemini 1.5, also sparked debate about strategic narrative control in the competitive AI landscape <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

A common challenge in understanding these new models is the lack of detailed technical papers. Both OpenAI and Google DeepMind opted for "technical reports" or high-level overviews rather than comprehensive papers, omitting crucial information about datasets, training recipes, and data augmentation techniques <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>, <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. This secrecy is attributed to concerns about intellectual property, replication, and potential lawsuits over training data <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>, <a class="yt-timestamp" data-t="53:15:00">[53:15:00]</a>.

## Sora: State-of-the-Art Video Generation

Sora is OpenAI's new state-of-the-art video generation model <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. It produces significantly longer videos and demonstrates higher quality in motion and overall realism compared to competitors like Runway, Pika, and Stable Video <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>, <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>, <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.

### Impact on Generative 3D

Beyond generating 2D video content, Sora's quality represents a "step function" improvement that enables its use in [[video_diffusion_models_in_generative_3d | generative 3D applications]] <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>. Previously, generative 3D models relied on pre-trained text-to-image models like Stable Diffusion to extract necessary intelligence <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. With Sora, a similar integration is expected to lead to significant advancements in text-to-3D and generative 3D within approximately six months <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>, <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

### Key Contributors

Sam Altman, CEO of OpenAI, specifically highlighted three individuals responsible for Sora:
*   **Tim Brooks**: A research scientist at OpenAI and a UC Berkeley PhD <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. His most cited work is "InstructPix2Pix," an image editing diffusion model that uses GPT-3 to create paired image-text datasets for fine-tuning <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>, <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
*   **Bill Peebles (William Peebles)**: Also a research scientist at OpenAI and a Berkeley PhD <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>, <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>. He is known for "Scalable Diffusion Models with Transformers," which replaces the traditional U-Net backbone in latent diffusion models with a Transformer that operates on latent patches <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>, <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>, <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
*   **Aditya Ramesh ("Model Mechanic")**: A more senior researcher with significant citations, known for papers on image generation using language models and hierarchical text-conditioned image generation <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>, <a class="yt-timestamp" data-t="20:03:00">[20:03:00]</a>, <a class="yt-timestamp" data-t="20:14:00">[20:14:00]</a>. His work includes using a Transformer that auto-regressively models images and text as tokens in a single data stream, often employing a discrete variational autoencoder (DVAE) <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>, <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>.

### Inferred Technical Insights

While OpenAI did not release a detailed paper for Sora, several technical aspects can be inferred:
*   **Latent Diffusion Model**: Sora is believed to be a latent diffusion model, where denoising occurs in a compressed latent space rather than the raw image space <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>, <a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>.
*   **Space-Time Patches/Tokens**: Videos are compressed into a lower-dimensional latent space and then decomposed into "SpaceTime patches" <a class="yt-timestamp" data-t="25:51:00">[25:51:00]</a>. This approach allows the model to process the entire video at once, similar to the Lumiere model from Google <a class="yt-timestamp" data-t="28:37:00">[28:37:00]</a>, <a class="yt-timestamp" data-t="44:16:00">[44:16:00]</a>.
*   **Transformer Architecture**: Like Diffusion Transformers (Dit), Sora likely replaces the traditional U-Net with a Transformer architecture for the denoising process <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>, <a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>. The use of visual patches and Transformers allows Sora to train on and generate videos of variable resolutions and lengths <a class="yt-timestamp" data-t="31:50:00">[31:50:00]</a>.
*   **Data Augmentation (Recaptioning)**: OpenAI likely uses GPT-like models to expand short user prompts into longer, more detailed captions, enriching the training data <a class="yt-timestamp" data-t="35:34:00">[35:34:00]</a>.
*   **Synthetic Data Debate**: While some speculate Sora uses synthetic data generated by game engines like Unreal Engine, it's more probable that OpenAI simply included existing video game footage scraped from the internet in its massive training dataset <a class="yt-timestamp" data-t="36:57:00">[36:57:00]</a>, <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>.
*   **"World Simulators"**: Although Sora demonstrates some "world understanding," it's not yet a true physics simulation engine. It exhibits odd behaviors and perspective errors, suggesting an implicit, learned model of physics rather than explicit equations <a class="yt-timestamp" data-t="41:12:00">[41:12:00]</a>, <a class="yt-timestamp" data-t="42:25:00">[42:25:00]</a>.

## Gemini 1.5: Multimodal Understanding

Gemini 1.5, developed by Google DeepMind, is a highly compute-efficient [[multimodal_large_language_models | multimodal language model]] that excels at understanding video, text, and audio <a class="yt-timestamp" data-t="45:43:00">[45:43:40]</a>. It represents a significant step in [[overview_of_multimodal_models | multimodal models]] by being able to process and reason over a massive context window <a class="yt-timestamp" data-t="46:53:00">[46:53:00]</a>.

### Key Capabilities

*   **Long Context Window**: Gemini 1.5 can consume up to 10 million tokens of context, a "generational leap" over existing models like GPT-4 Turbo, which has a 128K token limit <a class="yt-timestamp" data-t="47:13:00">[47:13:00]</a>, <a class="yt-timestamp" data-t="47:40:00">[47:40:00]</a>.
*   **Near-Perfect Recall**: It achieves near-perfect recall on long-context retrieval tasks, making it highly effective for tasks like long document question answering <a class="yt-timestamp" data-t="46:59:00">[46:59:00]</a>.
*   **Multimodal Integration**: By converting various modalities (images, audio) into tokens, Gemini 1.5 can interleave and process them seamlessly with text tokens <a class="yt-timestamp" data-t="46:06:00">[46:06:00]</a>. This is a key aspect of [[multimodal_language_models | multimodal language models]].
*   **"Needle in the Haystack" Benchmark**: The model demonstrates impressive performance on the "needle in the haystack" task, where it can find specific information (e.g., correlating an image with a textual description within a long document) within a vast amount of data <a class="yt-timestamp" data-t="49:01:00">[49:01:00]</a>, <a class="yt-timestamp" data-t="50:45:00">[50:45:00]</a>. This capability showcases [[recent_advancements_in_multimodal_model_architectures | recent advancements in multimodal model architectures]].
*   **OCR and Speech Recognition**: It can implicitly perform optical character recognition (OCR) from visual tokens and achieve state-of-the-art speech recognition, even marginally surpassing Whisper V3 <a class="yt-timestamp" data-t="55:28:00">[55:28:00]</a>, <a class="yt-timestamp" data-t="56:31:00">[56:31:00]</a>.

### Inferred Technical Insights

Similar to Sora, Gemini 1.5's technical report lacks detailed implementation specifics, but inferences can be made:
*   **Compute**: It was trained on multiple 4,096-chip PODs of Google TPU V4 accelerators, highlighting the immense computational resources involved <a class="yt-timestamp" data-t="51:37:00">[51:37:00]</a>.
*   **Mixture of Experts (MoE)**: The paper explicitly mentions using a "mixture of experts" architecture <a class="yt-timestamp" data-t="57:52:00">[57:52:00]</a>. Given Google DeepMind's recent work, it's likely a "soft MoE" approach, where experts receive weighted averages of input tokens rather than hard assignments <a class="yt-timestamp" data-t="59:59:00">[59:59:00]</a>, <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. This relates to [[challenges_and_solutions_in_training_multimodal_models | challenges and solutions in training multimodal models]].
*   **Ring Attention for Long Context**: The long context capability is likely achieved through a technique similar to "Ring Attention," a recent Berkeley paper. This technique scales context size arbitrarily without approximation by distributing computations across a "ring" of hosts (e.g., GPUs) <a class="yt-timestamp" data-t="01:05:25">[01:05:25]</a>, <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>.
    *   Ring Attention, unlike RAG (Retrieval Augmented Generation) agent systems that summarize content, processes the actual, full context <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>, <a class="yt-timestamp" data-t="01:06:34">[01:06:34]</a>. This offers a [[comparison_of_different_multimodal_approaches | different multimodal approach]] to long context.
    *   It uses a "curriculum learning" approach, gradually increasing context size during training <a class="yt-timestamp" data-t="01:08:05">[01:08:05]</a>.
*   **Modality-Specific Tokens**: To seamlessly interleave different modalities, the model uses special tokens (e.g., "end of text," "start of image," "end of video") to explicitly signal transitions between data types <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Comparison and Future Outlook

While both Sora and Gemini 1.5 are impressive, they represent different types of breakthroughs.

*   **Sora** excels in visual output and marketing hype, primarily due to its striking video generation capabilities <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>, <a class="yt-timestamp" data-t="01:46:04">[01:46:04]</a>. Its potential to disrupt video and 3D content creation industries is immense <a class="yt-timestamp" data-t="01:48:51">[01:48:51]</a>.
*   **Gemini 1.5** is argued to be more technically transformative, particularly with its unprecedented long-context understanding and multimodal reasoning capabilities <a class="yt-timestamp" data-t="01:44:08">[01:44:08]</a>, <a class="yt-timestamp" data-t="01:45:56">[01:45:56]</a>. This advancement could render many current RAG (Retrieval Augmented Generation) startups obsolete, as the need for complex external retrieval systems diminishes when models can internally manage vast amounts of information <a class="yt-timestamp" data-t="01:47:21">[01:47:21]</a>.

The rapid development of these models, driven by massive compute resources and proprietary datasets, suggests an accelerating path towards AGI (Artificial General Intelligence) <a class="yt-timestamp" data-t="01:50:06">[01:50:06]</a>. This trend highlights a future where two dominant companies may control the leading edge of AI development, with significant [[future_directions_for_multimodal_and_agi_development | implications for industries]] and human interaction with digital worlds <a class="yt-timestamp" data-t="01:50:41">[01:50:41]</a>.