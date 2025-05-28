---
title: Building multimodal models
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

Multimodal models are a rapidly evolving area in AI, focusing on processing and generating information across multiple data types, known as "modalities" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Examples of modalities include images, text, and speech <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Recent advancements highlight different approaches to building these complex systems, from "gluing" pre-trained components to training from scratch with massive computational resources <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Defining Multimodality

A "modality" refers to a specific type of data, such as images, text, or speech <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Therefore, a multimodal model utilizes multiple modalities <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. The most common combination in current research involves text and images <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Current Landscape of Multimodal Models

The development of multimodal models is being driven by major players like Google, Facebook AI Research (Meta), and the open-source community represented by Hugging Face <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Open-Source Approach: "Gluing" Pre-Trained Models

The open-source community, often limited by budget, typically builds [[multimodal_large_language_models_vs_vision_language_models | Vision Language Models (VLMs)]] by combining pre-trained components <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a><a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>:
*   **Vision Encoder**: A pre-trained model (e.g., Dino, Clip) converts images into representations <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a><a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Language Model (LLM)**: A pre-trained LLM (e.g., Llama 7B, Mistral 7B) handles text <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Projection Layer**: A small, additional layer (also called a projector or adapter) connects the vision encoder's output to the LLM's input, converting visual representations into tokens the LLM can understand <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a><a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
*   **Training**: Primarily involves fine-tuning this projection layer, with some gradient propagation to the pre-trained components <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

This approach is cost-effective, leveraging models already trained by larger entities <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. An example is Hugging Face's iFIX 2, an 8-billion-parameter VLM that achieves state-of-the-art performance within its size category <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

### From-Scratch Training: [[chameleon_mixed_modal_model | Chameleon]]

Meta's [[chameleon_mixed_modal_model | Chameleon]] model represents a more ambitious approach: training a multimodal model from scratch in an end-to-end fashion <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Early Fusion**: Instead of separate encoders, all modalities are projected into a shared representation space from the beginning <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Images go directly through a tokenizer to produce tokens fed into the language model, rather than through a dedicated image encoder <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Capabilities**: [[chameleon_mixed_modal_model | Chameleon]] supports visual question answering, image captioning, text generation, image generation, and a new "mixed modal generation" feature, which involves generating [[interleaving_and_blending_techniques_in_multimodal_models | interleaved text and images]] <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a><a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   **Performance**: [[chameleon_mixed_modal_model | Chameleon]] 34B matches or exceeds larger models like Gemini Pro and GPT-4V, and even outperforms Llama 2 in text-only tasks <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a><a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This suggests that training on mixed modalities can improve performance even on unimodal benchmarks <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Resources**: Training from scratch requires immense computational resources, such as Meta's Research SuperCluster with over 3,000 Nvidia A100 GPUs <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>, and global batch sizes of 8 million tokens <a class="yt-timestamp" data-t="00:35:20">[00:35:20]</a>.

### Multimodal Turing Machine: Mirasol 3B

Google DeepMind's Mirasol 3B introduces a different approach, focusing on processing time-aligned and contextual modalities like video, audio, and text <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>.
*   **Architecture**: It decouples multimodal modeling into separate auto-regressive models, partitioning video and audio into consecutive snippets <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.
*   **Audio Processing**: A notable trick is representing audio as a spectrogram, effectively turning it into an image that can be processed by the same Vision Transformer backbone used for video <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a><a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.
*   **Token Turing Machine**: The most significant innovation is the "token Turing machine," a recurrent sequential model with Transformers and token-based operations that maintains an external memory <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>. This allows the model to store and retrieve information, giving it a form of long-term memory for inference <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a><a class="yt-timestamp" data-t="01:02:04">[01:02:04]</a>.

## Key Technical Aspects

### [[multimodal_models_and_tokenization | Tokenization]]
For text, a vocabulary size of around 65,000 is common <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. For images, new tokenizers encode 512x512 images into 1024 discrete tokens with a codebook size of 8,192 <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a><a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. Image tokenization involves cutting images into patches and encoding them into feature vectors <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. A weakness of current image tokenizers is difficulty in reconstructing images with large amounts of tiny text <a class="yt-timestamp" data-t="00:29:25">[00:29:25]</a>.

### Data and [[model_training_and_evaluation_methods | Training Methods]]
[[model_training_and_evaluation_methods | Model training and evaluation methods]] for advanced multimodal models involve multi-stage pipelines:
1.  **First Stage**: Pre-training on vast datasets, such as 2.9 trillion text-only tokens (from Llama 2) and 1.5 trillion text-image tokens <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a><a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.
2.  **Secondary Stage**: Incorporating higher-quality, often [[interleaving_and_blending_techniques_in_multimodal_models | interleaved]] data, while gradually reducing the weight of the first-stage data to prevent catastrophic forgetting <a class="yt-timestamp" data-t="00:28:32">[00:28:32]</a>.
3.  **Supervised Fine-Tuning (SFT)**: The final stage uses the cleanest, highest-quality data, including highly aesthetic images for generation and carefully curated safety data to prevent unsafe content <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a><a class="yt-timestamp" data-t="00:38:43">[00:38:43]</a>.

### Architectural Considerations
*   **Early Fusion vs. Late Fusion**: Early fusion, as seen in [[chameleon_mixed_modal_model | Chameleon]], projects all modalities into a shared space from the start <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Late fusion (or the "glued" approach) processes modalities separately before combining their representations <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
*   **Cross-Attention**: Cross-attention allows information flow between different modalities, but can be more computationally expensive <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. Removing cross-attention can improve efficiency for smaller models <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.
*   **Pooling**: Techniques like perceiver resampler are used to reduce the number of visual tokens, improving compute efficiency at training and inference without significant performance loss <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.
*   **Logit Drift**: When training end-to-end with multiple modalities, there can be "logit drift" where modalities compete due to varying entropy, biasing the model towards easier predictions <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a><a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>. This is addressed through architectural modifications like query-key normalization <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.

### [[multimodal_model_benchmarks | Multimodal Model Benchmarks]]
Traditional automatic [[multimodal_model_benchmarks | benchmarks]] can be gamed <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. Human evaluation (pairwise comparisons where evaluators don't know the model source) is considered the "gold standard" <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

## [[multimodal_capabilities_and_experiments | Multimodal Capabilities and Experiments]]

Current state-of-the-art models like [[chameleon_mixed_modal_model | Chameleon]] can output [[interleaving_and_blending_techniques_in_multimodal_models | interleaved text and images]] <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. This presents new challenges:
*   **Conditional Decoding**: The decoding process changes based on whether the model is generating image or text tokens, requiring inspection at each step <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>.
*   **Fixed vs. Variable Length Outputs**: Text generation has variable length, but image generation produces fixed-size blocks of tokens corresponding to an image, which must be completed <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.

The "token Turing machine" concept in Mirasol 3B suggests a future where models maintain an internal memory, enabling them to recall past events or information, as demonstrated by GPT-4o remembering a prior action <a class="yt-timestamp" data-t="01:01:02">[01:01:02]</a>. This memory function allows for a more "stateful" inference, though it adds complexity to deployment compared to stateless LLMs <a class="yt-timestamp" data-t="01:12:07">[01:12:07]</a>.

## Future Outlook

The trajectory of multimodal models points towards:
*   **End-to-End Training**: Moving away from gluing separate components, towards single, large models trained from scratch on all modalities <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>.
*   **Unified Modality Processing**: Treating all modalities (text, audio, video) as sequences of tokens, allowing for uniform processing by Transformer architectures <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a><a class="yt-timestamp" data-t="01:21:58">[01:21:58]</a>.
*   **Interleaved Multi-Modal Output**: Models capable of seamlessly generating text, audio, and video in an interleaved fashion <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a><a class="yt-timestamp" data-t="01:17:37">[01:17:37]</a>.
*   **3D and Control Tokens**: The eventual capability to output 3D models (e.g., Gaussian Splats) or control tokens for robotics, enabling AI interaction with the physical world <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a><a class="yt-timestamp" data-t="01:21:14">[01:21:14]</a><a class="yt-timestamp" data-t="01:19:02">[01:19:02]</a>. This suggests a future where AI interfaces become fully immersive, moving beyond two-dimensional screens into VR environments with rendered avatars <a class="yt-timestamp" data-t="01:18:48">[01:18:48]</a>.

The "bitter lesson" of AI research suggests that removing complexity and scaling up data and model size, rather than over-engineering, will lead to further breakthroughs in [[multimodal_capabilities_in_language_models | multimodal capabilities in language models]] <a class="yt-timestamp" data-t="01:30:20">[01:30:20]</a>. While massive compute is currently required for foundational training, techniques like distillation and quantization can later make large models small enough to run on consumer devices <a class="yt-timestamp" data-t="01:43:04">[01:43:04]</a>.