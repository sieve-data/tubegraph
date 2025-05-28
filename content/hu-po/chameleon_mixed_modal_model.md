---
title: Chameleon mixed modal model
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

The Chameleon model, developed by Facebook AI Research (Meta), represents a significant advancement in the field of [[building_multimodal_models | building multimodal models]] <a class="yt-timestamp" data-t="02:40:40">[02:40:40]</a>. Released on May 16, 2024 <a class="yt-timestamp" data-t="03:17:20">[03:17:20]</a>, it is a family of early fusion, token-based mixed modal models <a class="yt-timestamp" data-t="05:17:17">[05:17:17]</a>.

## Capabilities
Chameleon handles various tasks, including:
*   Visual question answering <a class="yt-timestamp" data-t="05:28:28">[05:28:28]</a>
*   Image captioning <a class="yt-timestamp" data-t="05:30:46">[05:30:46]</a>
*   Text generation <a class="yt-timestamp" data-t="05:30:51">[05:30:51]</a>
*   Image generation <a class="yt-timestamp" data-t="05:31:53">[05:31:53]</a>
*   Long-form mixed-modal generation <a class="yt-timestamp" data-t="05:32:34">[05:32:34]</a>

A key new capability of Chameleon is its ability to [[interleaving_and_blending_techniques_in_multimodal_models | generate interleaved text and images]] <a class="yt-timestamp" data-t="05:59:02">[05:59:02]</a>. Unlike previous models like GPT-4V, which could consume image tokens but only output text, Chameleon can output sequences that mix text and image tokens seamlessly <a class="yt-timestamp" data-t="05:59:02">[05:59:02]</a>, <a class="yt-timestamp" data-t="06:02:02">[06:02:02]</a>, <a class="yt-timestamp" data-t="06:05:06">[06:05:06]</a>, <a class="yt-timestamp" data-t="06:09:09">[06:09:09]</a>.

## Architectural Approach
Chameleon's core difference from prior [[multimodal_capabilities_in_language_models | multimodal capabilities in language models]] (often referred to as Vision Language Models or VLMs) is its "early fusion" approach <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>, <a class="yt-timestamp" data-t="07:23:25">[07:23:25]</a>.
*   **Early Fusion**: All modalities (text and images) are projected into a shared representation space from the start, allowing for seamless reasoning and generation <a class="yt-timestamp" data-t="07:23:25">[07:23:25]</a>, <a class="yt-timestamp" data-t="07:29:31">[07:29:31]</a>. Images are immediately turned into tokens and fed directly into the mixed modal autoregressive language model, without an intermediate image encoder <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>, <a class="yt-timestamp" data-t="10:05:08">[10:05:08]</a>.
*   **From Scratch Training**: This early fusion approach necessitates training the model from scratch, rather than gluing together pre-trained components (like a vision encoder and a language model) <a class="yt-timestamp" data-t="07:09:08">[07:09:08]</a>, <a class="yt-timestamp" data-t="09:37:37">[09:37:37]</a>.

### Comparison with Prior Approaches (Late Fusion)
Traditional VLMs (like those from Hugging Face) typically use a "late fusion" approach <a class="yt-timestamp" data-t="08:05:05">[08:05:05]</a>, <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.
*   They consist of a separately trained vision encoder (e.g., DINO or CLIP) and a pre-trained language model (e.g., Llama 7B or Mistral 7B) <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>, <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>.
*   A small "projection layer" or "adapter" is used to convert vision representations into tokens compatible with the language model <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>, <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. This setup is less computationally demanding for developers without massive GPU resources <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>, <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

### Tokenization
Chameleon employs new image and text tokenizers <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.
*   **Image Tokenizer**: Encodes 512x512 images into 1024 discrete tokens, with a codebook size of 8,192 <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>, <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>. A weakness is its difficulty in reconstructing images with large amounts of tiny text <a class="yt-timestamp" data-t="19:24:00">[19:24:00]</a>, <a class="yt-timestamp" data-t="20:00:03">[20:00:03]</a>.
*   **Text Tokenizer**: Has a vocabulary size of 65,000 <a class="yt-timestamp" data-t="18:30:00">[18:30:00]</a>.

### Training Details
Chameleon models (7B and 34B parameters) are trained on a massive scale <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>, <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
*   **Compute Resources**: Trained on Meta's Research SuperCluster, comprising over 3,000 Nvidia A100 GPUs, accumulating over 4 million GPU hours <a class="yt-timestamp" data-t="35:33:00">[35:33:00]</a>, <a class="yt-timestamp" data-t="36:17:00">[36:17:00]</a>. This cluster uses Nvidia Quantum InfiniBand for high-speed GPU communication, essential for model and data parallelism <a class="yt-timestamp" data-t="41:31:00">[41:31:00]</a>, <a class="yt-timestamp" data-t="41:47:00">[41:47:00]</a>.
*   **Batch Size**: Uses monstrous global batch sizes, for example, 2^23 tokens (approximately 8 million tokens) <a class="yt-timestamp" data-t="35:20:00">[35:20:00]</a>, <a class="yt-timestamp" data-t="35:25:00">[35:25:00]</a>.
*   **Data Mix**: Pre-trained in two stages <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>:
    1.  **Stage One**: A data mixture including 2.9 trillion tokens of text (from Llama 2 pre-training data), over 1.5 trillion text-image tokens (publicly available and licensed data, possibly including scraped YouTube and Reddit data), and 100 billion tokens of interleaved text and images <a class="yt-timestamp" data-t="26:30:00">[26:30:00]</a>, <a class="yt-timestamp" data-t="27:52:00">[27:52:00]</a>, <a class="yt-timestamp" data-t="28:01:00">[28:01:00]</a>.
    2.  **Stage Two**: Introduces higher-quality datasets while gradually reducing the weight of the first stage data (e.g., by 50%) to prevent catastrophic forgetting <a class="yt-timestamp" data-t="28:32:00">[28:32:00]</a>, <a class="yt-timestamp" data-t="28:43:00">[28:43:00]</a>, <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>.

### Unique Challenges in Training
*   **Logit Drift Problem**: Because Chameleon shares weights across modalities and performs [[interleaving_and_blending_techniques_in_multimodal_models | interleaved text and images]] generation, modalities can compete with each other if not properly managed <a class="yt-timestamp" data-t="32:28:00">[32:28:00]</a>, <a class="yt-timestamp" data-t="33:00:00">[33:00:00]</a>. This happens when modalities have significantly varying entropy, leading the model to bias predictions towards easier modalities <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
    *   **Solution**: Introduce Dropout after attention and feed-forward layers, and implement QK (Query-Key) normalization within the attention mechanism <a class="yt-timestamp" data-t="33:29:00">[33:29:00]</a>, <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>. This is a deviation from standard Transformer architectures like Llama 2 <a class="yt-timestamp" data-t="33:39:00">[33:39:00]</a>.
*   **Inference Complexity**: The variable nature of token generation (image vs. text) at inference time means tokens must be inspected at each step. This requires conditional flow (e.g., an "if statement") to determine which tokenizer to use for decoding, which can be annoying to implement efficiently <a class="yt-timestamp" data-t="54:08:00">[54:08:00]</a>, <a class="yt-timestamp" data-t="54:31:00">[54:31:00]</a>.
    *   **Fixed-size blocks**: Unlike text generation, token-based image generation produces fixed-size blocks of tokens, meaning an image must be fully generated; it cannot be paused or cut short <a class="yt-timestamp" data-t="55:56:00">[55:56:00]</a>, <a class="yt-timestamp" data-t="56:02:00">[56:02:00]</a>.

## Performance
Chameleon 34B has demonstrated strong performance, matching or exceeding that of much larger [[comparison_with_other_multimodal_ai_models | comparison with other multimodal AI models]].
*   **State-of-the-Art**: It outperforms Llama 2 in text-only benchmarks <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>, showing that training on mixed modalities can lead to better performance on unimodal benchmarks <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
*   **Competitive with Industry Leaders**: Chameleon 34B matches or exceeds the performance of Gemini Pro and GPT-4V in pairwise human comparisons <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>, <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>. In human preference tests, Chameleon 34B was preferred over GPT-4V 46% of the time, with 30% being deemed "about the same," indicating its potential as the new state-of-the-art <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>, <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
    *   **Benchmark Challenge**: Comparing Chameleon to GPT-4V and Gemini Pro was challenging because the latter models can consume mixed-modal inputs but only output text. To facilitate comparison, GPT-4V was augmented with DALL-E 3 to generate images when required, and Gemini Pro with its corresponding image generation model <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>.

## Future Outlook
Chameleon's end-to-end, early-fusion, and [[interleaving_and_blending_techniques_in_multimodal_models | interleaved generation]] capabilities represent the future of [[multimodal_capabilities_and_experiments | multimodal capabilities and experiments]]. While Chameleon currently focuses on text and images, the broader trajectory of AI, hinted at by models like Google DeepMind's Mirasol 3B, points towards models consuming and generating a wider range of modalities (including audio and video) in an end-to-end fashion <a class="yt-timestamp" data-t="01:08:49">[01:08:49]</a>, <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>. This approach aims to eliminate the "glued-together" limitations of older VLMs and enable more sophisticated, human-like AI interactions <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>.