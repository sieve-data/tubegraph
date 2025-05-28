---
title: Overview of Multimodal Models
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

[[multimodal_language_models | Multimodal models]] are a class of artificial intelligence models capable of processing and understanding information from multiple data "modalities" <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. A modality refers to a distinct type of data, such as images, text, or speech <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. These models use multiple modalities as input and often produce outputs in one or more modalities <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. The current landscape of [[recent_advancements_in_multimodal_model_architectures | Recent Advancements in Multimodal Model Architectures]] is rapidly evolving, with a clear trend towards more integrated and versatile architectures <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Architectural Approaches

The development of [[multimodal large language models | multimodal large language models]] has seen two primary architectural approaches:

### Late Fusion (Traditional Approach)
Historically, [[multimodal_learning_and_embeddings | multimodal models]] have often adopted a "late fusion" approach. This method involves combining separately pre-trained components for different modalities <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   **Components**: Typically, a pre-trained vision encoder (e.g., DINO or CLIP) and a pre-trained large language model (LLM) like Llama 17B or Mistral 7B are used <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a> <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Integration**: These components are "glued together" using an additional projection layer or adapter that transforms vision representations into tokens consumable by the LLM <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Training**: Training primarily focuses on tuning this projection layer, with some minor adjustments to the pre-trained backbones <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Output**: Models using this approach typically consume text and images but only output text <a class="yt-timestamp" data-t="01:34:09">[01:34:09]</a>.
*   **Performance Factor**: The performance of these models heavily relies on the strength of the pre-trained language model backbone <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>.

### Early Fusion (State-of-the-Art Approach)
The "early fusion" approach, as demonstrated by Meta's Chameleon, represents a significant leap forward.
*   **Integration**: All modalities are projected into a shared representation space from the very beginning, allowing for seamless reasoning and generation across modalities <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Training**: This approach necessitates training the model from scratch in an end-to-end fashion <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This means no reliance on separately pre-trained vision or language encoders <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Tokenization**: New image and text tokenizers are trained to encode raw data directly into tokens that are then fed into the language model <a class="yt="yt-timestamp" data-t="00:10:02">[00:10:02]</a> <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Output**: These models can generate interleaved text and images <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. This "mixed modal generation" capability is a novel feature, as previous models like GPT-4V could consume image tokens but only output text <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   **Cost**: This method requires a massive computing budget, with models like Chameleon 34B trained on 10 trillion tokens using over 3,000 NVIDIA A100 GPUs for millions of GPU hours <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a> <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a> <a class="yt-timestamp" data-t="01:35:31">[01:35:31]</a>.

## Key Models and Capabilities

### Chameleon (Meta AI Research)
*   **Type**: Early Fusion token-based mixed-modal foundation model <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Capabilities**: Performs visual question answering, image captioning, text generation, image generation, and long-form mixed-modal generation <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Performance**: Outperforms Llama 2 (text-only) and matches or exceeds the performance of much larger models, including Gemini Pro and GPT-4V, in human evaluations <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a> <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a> <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

### i-MiX 2 (Hugging Face)
*   **Type**: Late Fusion Vision Language Model <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
*   **Performance**: Achieves [[stateoftheart_video_generation_and_multimodal_models | state-of-the-art video generation and multimodal models]] within its size category (8 billion parameters) <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. This emphasizes the limitations faced by smaller budgets <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   **Pooling**: Explored different pooling techniques, finding that trainable pooling like "perceiver resampler" is effective for reducing visual tokens, improving efficiency and performance <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a> <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.

### Mirasol 3B (Google DeepMind/Research)
*   **Type**: Multimodal Autoregressive Model for time-aligned and contextual modalities <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.
*   **Modalities**: Focuses on video and audio, in addition to text, making it capable of consuming up to three modalities (video, audio, text) and outputting text <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a> <a class="yt-timestamp" data-t="01:36:31">[01:36:31]</a>.
*   **Innovation**: Transforms audio signals into spectrograms, allowing the reuse of a single Vision Transformer backbone for both video and audio encoding <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a> <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
*   **Token Turing Machine**: Introduced a "token turing machine" concept, effectively recreating a recurrent model with an external memory using Transformers <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>. This memory allows the model to retain information over time, similar to an LSTM's hidden state, enabling more complex and temporally aware behaviors (e.g., remembering past visual events) <a class="yt-timestamp" data-t="01:02:04">[01:02:04]</a> <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>.

## [[challenges_and_solutions_in_training_multimodal_models | Challenges and Solutions in Training Multimodal Models]]

*   **Computational Cost**: Training end-to-end multimodal models requires immense computational resources, limiting such endeavors to a few large companies with massive GPU clusters <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.
*   **Tokenization Quality**: Current image tokenizers may struggle with reconstructing images containing small text due to resolution loss during discretization <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.
*   **Logit Drift**: When training with multiple modalities of varying entropy (e.g., images versus text), modalities can "compete" during training, biasing the model's predictions towards certain modalities. Solutions involve techniques like query-key normalization and specific dropout layers <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a> <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a> <a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>.
*   **Conditional Generation**: Generating interleaved text and images requires inspecting tokens at each step to determine the next modality, introducing complexities in inference <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>. Additionally, fixed-size blocks of tokens for images mean that partial image generation is not permissible, requiring a complete image output once generation begins <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.
*   **Data Curations**: Multimodal models require diverse and high-quality datasets, including interleaved text-image data, and specialized safety datasets to address multimodal attack factors <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a> <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a> <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>.

## The Future of Multimodal AI

The trend in [[comparison_of_different_multimodal_approaches | multimodal model architectures]] is moving towards end-to-end training of increasingly complex models that integrate more modalities directly.
*   **Full Multimodality**: The ultimate goal is an end-to-end model that can consume and output any combination of video, audio, and text, seamlessly interleaved <a class="yt-timestamp" data-t="01:10:51">[01:10:51]</a> <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>. This represents the [[convergence_of_ai_models_across_modalities | convergence of AI models across modalities]] into a single, unified architecture.
*   **3D Outputs**: As virtual reality becomes more prevalent, the next step will likely be models that can process and generate 3D environments and objects (e.g., Gaussian Splats) directly from tokens <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a> <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>.
*   **Control Tokens**: Beyond perceptual modalities, future models may output "control tokens" to directly interface with robots, enabling end-to-end robotic control <a class="yt-timestamp" data-t="01:19:04">[01:19:04]</a> <a class="yt-timestamp" data-t="01:22:18">[01:22:18]</a>.
*   **The Bitter Lesson**: The progression of AI suggests that removing complexity in architecture and focusing on larger models, more data, and longer training leads to superior performance, rather than adding intricate modules <a class="yt-timestamp" data-t="01:29:50">[01:29:50]</a>.
*   **Impact**: These advancements could lead to truly human-like AI interactions, such as conducting Zoom calls with an AI generating realistic audio-visual representations <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. While the path to these models is expensive and compute-intensive, the vast amount of multimodal data available (e.g., from YouTube, Netflix) suggests that achieving these capabilities is primarily a matter of scaling <a class="yt-timestamp" data-t="01:39:41">[01:39:41]</a>.