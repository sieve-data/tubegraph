---
title: Challenges and Solutions in Training Multimodal Models
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

Developing and training [[multimodal models | multimodal models]] presents unique challenges, particularly when aiming for state-of-the-art performance and advanced capabilities like interleaved generation. These challenges span from architectural design and data handling to computational requirements and the very nature of multimodal inference <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Architectural and Fusion Approaches

Historically, many [[multimodal models | multimodal models]], particularly early [[Multimodal Language Models | Vision Language Models]] (VLMs) like those developed by Hugging Face (e.g., iFix), adopted a "late fusion" or "gluing" approach <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>, <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.

*   **Approach:** This method involves combining a pre-trained vision encoder (like Dino or CLIP) with a pre-trained language model (like Llama 17B or Mistral 7B) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. A small projection layer (adapter) is then trained to translate the vision representations into tokens compatible with the language model <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.
*   **Challenge:** The performance of such models heavily relies on the quality of the pre-trained language model; a better language model leads to significant improvements <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. This approach is limited by the inherent separation of modalities in initial training <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Solution/Evolution (Early Fusion):** Newer models like Meta's Chameleon adopt an "early fusion" approach, where all modalities are projected into a shared representation space from the beginning and the entire model is trained from scratch in an end-to-end fashion <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This allows for seamless reasoning and generation across modalities <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Specific Architectural Considerations

*   **Pooling:** Simple average pooling in vision encoders can degrade performance, as it leads to information loss <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. Trainable pooling techniques, such as the perceiver resampler, are more effective at reducing visual token size while improving compute efficiency and downstream performance <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>, <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
*   **Cross-Attention vs. Autoregressive:** In some contexts (like the Hugging Face paper), cross-attention architecture can be computationally expensive and harder to train, leading to preference for fully autoregressive models for efficiency <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>. However, for models trained from scratch with vast resources (like Google's Mirasol), cross-attention is beneficial as it facilitates information flow between modalities <a class="yt-timestamp" data-t="00:48:31">[00:48:31]</a>.

## Data and Tokenization Challenges

*   **Image Tokenization and Text Readability:** Current image tokenizers, even with 512x512 images turned into 1024 discrete tokens with an 8,192 codebook size, struggle with reconstructing images containing tiny text <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>, <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. This is because the resolution might not be high enough, leading to "garbled" text <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. The visual token codebook size is currently much smaller than text vocabulary (e.g., 8,000 vs. 65,000), suggesting this area is still in its early stages <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.
*   **Data Scale and Variety:** Training powerful [[multimodal models | multimodal models]] requires massive and diverse datasets. For example, Chameleon was trained on 2.9 trillion text tokens (like Llama 2 data), over 1.5 trillion text-image tokens (publicly available and licensed data, potentially scraped from YouTube/Reddit), and 400 billion tokens of interleaved text and images (like blog posts or Wikipedia pages) <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
*   **Multi-Stage Training and Catastrophic Forgetting:** When using multi-stage training pipelines (e.g., initial pre-training on large, "noisier" data, followed by secondary pre-training on higher-quality data), direct switching between datasets can lead to catastrophic forgetting <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>. The solution is to "weave" datasets, gradually reducing the weight of the first-stage data while introducing the second-stage data <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.
*   **Safety Data:** With multimodal outputs, safety data must also be multimodal (e.g., interleaved text and images) to address potential multimodal attack factors that are outside the distribution of text-only or text-to-image safety benchmarks <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>.

## Training and Inference Difficulties

*   **Logit Drift Problem:** When sharing all model weights across modalities (as in early fusion), modalities with significantly varying entropy (e.g., images vs. text) can compete with each other during training, leading to a "logit drift" problem <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>, <a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>.
    *   **Solution:** Introduce Dropout after attention and feed-forward layers, and apply layer normalization (qk norm) to query and key vectors within the attention mechanism <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>, <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.
*   **Interleaved Output Complexity:** When a model generates interleaved text and images, the decoding process becomes more complex because the next token's modality is not fixed <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>.
    *   **Challenge:** Tokens must be inspected at each step, and tokens not belonging to the current modality space must be masked or ignored <a class="yt-timestamp" data-t="00:55:03">[00:55:03]</a>. Also, image generation produces fixed-size blocks of tokens; the model cannot pause or generate half an image if the context length is exhausted <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
*   **Computational Scale:** Training models like Chameleon requires immense computational resources, including over 3,000 Nvidia A100 GPUs and over 4 million GPU hours, connected by high-speed networking like Nvidia Quantum Infiniband <a class="yt-timestamp" data-t="00:35:33">[00:35:33]</a>, <a class="yt-timestamp" data-t="00:41:11">[00:41:11]</a>. This restricts such end-to-end training to only a few companies globally <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>.

## The Role of Memory and Statefulness

Traditional Transformer models are largely stateless during inference, meaning each interaction is independent <a class="yt-timestamp" data-t="01:11:48">[01:11:48]</a>. However, advanced [[Multimodal large language models | multimodal large language models]] like Google's Mirasol (and implied for GPT-4o) introduce a "token Turing machine" concept, which includes an external memory <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>, <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>.

*   **Challenge:** Implementing stateful inference (where a model remembers past interactions) adds significant complexity to data centers and memory management. It's unclear if this memory resides in GPU RAM or an external database, affecting latency and scalability <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>.
*   **Solution:** The token Turing machine (resembling an LSTM) uses a fixed-size memory that the model can write to and read from, enabling constant time complexity (O(T)) with respect to input length, rather than O(T^2) of traditional Transformers <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>, <a class="yt-timestamp" data-t="01:13:31">[01:13:31]</a>. This allows for contextual awareness over longer durations <a class="yt-timestamp" data-t="01:01:47">[01:01:47]</a>.

## Future Directions

The trend suggests a move towards increasingly complex, end-to-end trained [[multimodal models | multimodal models]] that consume and generate multiple modalities (text, image, audio, video) in an interleaved fashion <a class="yt-timestamp" data-t="01:10:59">[01:10:59]</a>, <a class="yt-timestamp" data-t="01:39:17">[01:39:17]</a>. This also implies future capabilities such as:

*   **3D Outputs:** Beyond 2D images, models may eventually output 3D models or even interact with virtual reality environments with 3D tokens <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   **Control Tokens:** Integrating control tokens could allow these models to directly control robots <a class="yt-timestamp" data-t="01:09:02">[01:09:02]</a>, <a class="yt-timestamp" data-t="01:19:04">[01:19:04]</a>.

The "bitter lesson" of deep learning suggests that removing architectural complexity and focusing on larger models, more data, and longer training leads to better performance <a class="yt-timestamp" data-t="01:30:18">[01:30:18]</a>. This implies a future where a single, massive, end-to-end model handles all modalities, rather than complex piecemeal systems <a class="yt-timestamp" data-t="01:30:27">[01:30:27]</a>, <a class="yt-timestamp" data-t="01:31:21">[01:31:21]</a>.