---
title: Comparison of Different Multimodal Approaches
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

Multimodal models, capable of processing and generating information across different data types like text, images, audio, and video, are at the forefront of AI research. Recent advancements highlight distinct architectural and training philosophies adopted by major players in the field.

## The "Glued" Approach: Open-Source Multimodal Models

The approach commonly seen in the open-source community, exemplified by Hugging Face's [[recent_advancements_in_multimodal_model_architectures | iFix2]] model, involves combining pre-trained, separate components.

*   **Architecture**
    *   These models typically "glue together" a pre-trained [[multimodal_learning_and_embeddings | vision encoder]] (e.g., Dino, CLIP) and a pre-trained [[multimodal_language_models | language model]] (e.g., Llama 17B, Mistral 7B) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   An additional "projection layer" or "adapter" is introduced to connect the visual representations to the language model's input token space <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   The input sequence to the language model is a concatenation of visual and text tokens <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.
    *   [[multimodal_learning_and_embeddings | Pooling techniques]] like the perceiver resampler are used to reduce the number of visual tokens for computational efficiency, though naive average pooling can degrade performance <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.
*   **Training & Performance**
    *   The primary training effort focuses on tuning the projection layer and, to a lesser extent, parts of the pre-trained models <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This reduces the need for massive GPU clusters <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
    *   The quality of the pre-trained [[multimodal_language_models | language model]] has the greatest impact on downstream performance <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
    *   These models achieve state-of-the-art *within their specific size categories*, rather than overall <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   **Limitations**
    *   They are typically limited to consuming images and text, and outputting text <a class="yt-timestamp" data-t="01:34:15">[01:34:15]</a>.
    *   They often struggle with accurately extracting tiny text from images due to the lossy nature of image tokenization <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.
    *   Hugging Face's research suggests [[recent_advancements_in_multimodal_model_architectures | cross-attention]] blocks can be computationally expensive and may make training harder when added to language model layers <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.

## End-to-End Early Fusion: Meta's Chameleon

Meta's Chameleon model represents a more ambitious approach, training a single, large model from scratch.

*   **Architecture**
    *   Chameleon is a family of "early fusion token-based mixed-modal models" <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>.
    *   All modalities (initially text and images) are immediately converted into tokens and projected into a shared representation space from the beginning <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
    *   This requires training the entire model, including new image and text tokenizers, from scratch <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   It can generate "interleaved text and images" as output, a key differentiating capability <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>.
    *   The model uses standard Transformer architecture components like RMS Norm, Swig glue, and rotary position embeddings <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>.
*   **Training & Performance**
    *   Training is conducted in an end-to-end fashion on massive datasets, including 2.9 trillion text tokens and 1.5 trillion text-image tokens, plus 400 billion tokens of interleaved text and images <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.
    *   It uses a multi-stage pre-training process, gradually introducing higher-quality data and reducing the weight of initial datasets to prevent catastrophic forgetting <a class="yt-timestamp" data-t="00:28:32">[00:28:32]</a>.
    *   This approach requires immense computational resources, such as Meta's Research Super Cluster with over 3,000 Nvidia A100 GPUs and millions of GPU hours <a class="yt-timestamp" data-t="00:35:33">[00:35:33]</a>.
    *   Chameleon 34B has demonstrated [[overview_of_multimodal_models | stateoftheart_video_generation_and_multimodal_models | state-of-the-art performance]], outperforming models like Gemini Pro and [[multimodal_capabilities_in_large_language_models_using_clip | GPT-4V]] in human evaluations <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. It even outperforms text-only LLMs on unimodal benchmarks, suggesting benefits from multimodal training <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Challenges**
    *   "Logit drift" occurs when modalities with varying entropy compete, leading to a bias towards easier-to-predict modalities <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. This is mitigated with architectural tweaks like Dropout and QK Norm <a class="yt-timestamp" data-t="00:33:29">[00:33:29]</a>.
    *   Generating interleaved content introduces new challenges in inference, such as managing conditional decoding flow and ensuring complete image generation when context length limits are reached <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>.

## Multimodal with External Memory: Google's Mirasol 3B

Google DeepMind's Mirasol 3B focuses on integrating more diverse modalities like video and audio, and introduces a concept of external memory.

*   **Architecture**
    *   It handles video and audio information, which are naturally time-aligned <a class="yt-timestamp" data-t="00:43:31">[00:43:31]</a>.
    *   A key innovation is representing audio as a spectrogram, which allows the same Vision Transformer (ViT) backbone to encode both video (as image frames) and audio (as image-like spectrograms), enabling component reuse <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>.
    *   The model also employs a "combiner" mechanism (similar to a projector) to encode joint audio-visual information <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>.
    *   Crucially, this paper introduces a "Token Turing Machine" – a recurrent sequential model with Transformers and token-based operations that maintains an **external memory** <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>. This memory allows the model to retain and retrieve information, enabling behavior like remembering past events from video input <a class="yt-timestamp" data-t="01:02:04">[01:02:04]</a>.
    *   This external memory reduces the time complexity of the model from O(T²) to O(T) with respect to input sequence length <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>.
    *   Unlike Hugging Face's findings, Google's model utilizes [[recent_advancements_in_multimodal_model_architectures | cross-attention]] to coordinate learning between different components <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>.
*   **Training & Performance**
    *   The audio and video encoders are trained from scratch using reconstruction losses, often by masking portions of the input <a class="yt-timestamp" data-t="01:05:16">[01:05:16]</a>.
    *   While smaller (3B parameters) and outputs text-only, it hints at the capabilities of larger models like Google's Astra, which can consume audio and video <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>.

## The Future of Multimodal AI

The progression across these approaches highlights a clear trend towards [[convergence_of_ai_models_across_modalities | more integrated and generalized multimodal models]]:

*   **From Glued to End-to-End**: The industry is moving away from piecemeal integration of pre-trained components towards training monolithic, end-to-end models from scratch. This eliminates integration complexities and unlocks higher performance <a class="yt-timestamp" data-t="01:34:35">[01:34:35]</a>.
*   **Expanding Modalities**: Models are evolving from handling just text and images to incorporating video and audio, moving towards full perception of the real world <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>.
*   **Flexible Outputs**: The ability to generate interleaved content across modalities (e.g., text and images, eventually audio and video) is becoming a standard for advanced [[multimodal_large_language_models | multimodal large language models]] <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>.
*   **Memory and Stateful Inference**: The integration of external memory mechanisms in [[multimodal_large_language_models | multimodal large language models]] (like the Token Turing Machine) represents a shift towards stateful inference, allowing models to remember past interactions and observations, crucial for long-term coherence and reasoning <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>.
*   **The Bitter Lesson**: The trend reinforces the "bitter lesson" in AI: simple architectures scaled with massive data and compute often outperform complex, hand-engineered systems. This means removing complexity in design rather than adding it, by relying on uniform tokenization and large-scale training <a class="yt-timestamp" data-t="01:30:18">[01:30:18]</a>.

Ultimately, the goal is a single, large [[multimodal_large_language_models | multimodal large language model]] that can consume and output any modality (text, image, audio, video, even control tokens for robotics) in an interleaved, end-to-end fashion, leveraging external memory for extended context. This represents a significant step towards more human-like AI capabilities.