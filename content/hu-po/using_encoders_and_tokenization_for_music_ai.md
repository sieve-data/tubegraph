---
title: Using encoders and tokenization for music AI
videoId: SodPUNBFeMY
---

From: [[hu-po]] <br/> 

[[music_generation_with_musicgen | MusicGen]] is a system developed by Meta AI Research that focuses on conditional music generation. It employs advanced AI techniques, particularly encoders and [[Tokenization and Latent Spaces in AI | tokenization]], to convert raw audio into discrete representations suitable for large language models. This approach allows for controllable generation based on textual descriptions and/or melodic features <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a> <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a> <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## Core Technology: Encoders and Tokenization

The fundamental challenge in generating music with AI lies in handling high-resolution audio signals, which can have sampling rates as high as 44 or 48 kilohertz, compared to 16 kilohertz for speech <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a> <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Music also contains complex harmonies and melodies from various instruments, making generation difficult due to human sensitivity to disharmony <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

To make audio modeling tractable, [[music_generation_with_musicgen | MusicGen]] represents audio signals as multiple streams of discrete tokens <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This process involves:

*   **EnCodec Audio Tokenizer**: [[music_generation_with_musicgen | MusicGen]] utilizes EnCodec, a convolutional autoencoder that quantizes the latent space using [[Quantization Techniques for AI Models | residual vector quantization]] <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a> <a class="yt-timestamp" data-t="00:30:1">[00:30:01]</a>. EnCodec converts raw audio (e.g., 32 kHz monophonic audio) into a continuous tensor with a significantly lower frame rate (e.g., 50 Hz) <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a> <a class="yt-timestamp" data-t="01:28:02">[01:28:02]</a>.
*   **[[Quantization Techniques for AI Models | Residual Vector Quantization (RVQ)]]**: This technique takes an infinite-resolution audio waveform and turns it into discrete, increasingly higher-resolution tokens <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. RVQ involves quantizing the audio signal, then quantizing the "residual" (the difference or error) between the quantized signal and the original, and so on <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a> <a class="yt-timestamp" data-t="00:31:47">[00:31:47]</a>. The first quantization level typically holds the most significant signal information <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>. [[music_generation_with_musicgen | MusicGen]] uses four quantizers, creating four parallel discrete token sequences (codebooks) <a class="yt-timestamp" data-t="01:28:57">[01:28:57]</a> <a class="yt-timestamp" data-t="01:49:52">[01:49:52]</a>. Each codebook has a size of 2048 words <a class="yt-timestamp" data-t="01:29:03">[01:29:03]</a>.

## MusicGen Model Architecture

[[music_generation_with_musicgen | MusicGen]] is built upon a single-stage Transformer-based autoregressive decoder <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>. Unlike prior work that used cascading or hierarchical models to generate coarse then finer audio versions <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a> <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>, [[music_generation_with_musicgen | MusicGen]] aims to produce the final product in one inference step <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

*   **Autoregressive Transformer**: The model predicts the next audio token based on all previously generated tokens, similar to how language models predict the next word <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a> <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>.
*   **Codebook Interleaving Patterns ([[Multistream design in AI | Multistream design]])**: A key innovation in [[music_generation_with_musicgen | MusicGen]] is its efficient token interleaving patterns, which handle the multiple parallel streams of acoustic tokens. The issue is that quantization levels are dependent (e.g., the second level quantizes the residual of the first) <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a> <a class="yt-timestamp" data-t="00:55:09">[00:55:09]</a>. Directly predicting them in parallel might lose dependencies, while sequential prediction is slow <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a> <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>. [[music_generation_with_musicgen | MusicGen]] explores different patterns to balance computational cost and quality <a class="yt-timestamp" data-t="00:55:43">[00:55:43]</a> <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>:
    *   **Flattening**: Predicts all codebooks at each time step, increasing complexity but maintaining detail <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>.
    *   **Delay Pattern**: Introduces a delay between codebooks to allow for more parallel prediction, especially for less important quantizers (k2, k3, k4), significantly speeding up inference <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a> <a class="yt-timestamp" data-t="01:32:0">[01:32:00]</a> <a class="yt-timestamp" data-t="02:00:28">[02:00:28]</a>.
    *   **Parallel Pattern**: Predicts all codebooks at the same time in parallel, assuming independence <a class="yt-timestamp" data-t="02:03:30">[02:03:30]</a>.
    *   **Valley Pattern**: Predicts the first codebook for all time steps sequentially, then predicts the remaining codebooks (2, 3, 4) in parallel <a class="yt-timestamp" data-t="02:03:44">[02:03:44]</a>.
*   **Positional Embeddings**: Sinusoidal embeddings are used to encode the current time step within the sequence <a class="yt-timestamp" data-t="01:15:33">[01:15:33]</a>.
*   **Attention Mechanisms**: The Transformer decoder uses causal self-attention and cross-attention blocks. Cross-attention is fed the conditioning signal (text and/or melody) <a class="yt-timestamp" data-t="01:16:13">[01:16:13]</a> <a class="yt-timestamp" data-t="01:17:04">[01:17:04]</a>. To improve speed and memory efficiency, [[music_generation_with_musicgen | MusicGen]] uses flash attention <a class="yt-timestamp" data-t="01:33:42">[01:33:42]</a>.

## Conditioning Mechanisms

[[music_generation_with_musicgen | MusicGen]] allows for granular control over generation through two main conditioning modalities:

### Text Conditioning

Users can describe the desired music (e.g., "cheerful song with acoustic guitars") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This text is encoded into a vector representation using pre-trained text encoders <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>.
*   **Encoders Used**: T5, Flan-T5, and [[Impact of Text Encoders on Image Generation | CLAP]] (a joint text-audio representation model akin to CLIP for image-text) <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a> <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.
*   **Text Pre-processing & Augmentation**: Techniques include text normalization (omitting stop words, lemmatizing) and word dropout during training to enhance robustness <a class="yt-timestamp" data-t="01:40:02">[01:40:02]</a> <a class="yt-timestamp" data-t="01:42:0">[01:42:00]</a>. Additional metadata like genre, BPM, and instrument tags are also concatenated to the text description <a class="yt-timestamp" data-t="01:41:07">[01:41:07]</a>.

### Melody Conditioning

Beyond text, [[music_generation_with_musicgen | MusicGen]] can be conditioned on existing melodic structures from other audio tracks, enabling the model to match a given harmonic and melodic structure <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a> <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a> <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>.
*   **Chromograms**: Melodies are converted into chromograms, which are 2D image-like representations showing time on the x-axis and frequency bins on the y-axis, indicating spectral information <a class="yt-timestamp" data-t="01:09:19">[01:09:19]</a>.
*   **Information Bottleneck**: To simplify conditioning, [[music_generation_with_musicgen | MusicGen]] chooses the "dominant time frequency bin" in each step, effectively turning the 2D chromogram into a 1D sequence for conditioning <a class="yt-timestamp" data-t="01:10:27">[01:10:27]</a> <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   **Unsupervised Approach**: This melody conditioning method is unsupervised, removing the need for costly supervised data <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>.

## Training and Evaluation

[[music_generation_with_musicgen | MusicGen]] was trained on 20,000 hours of licensed music, including an internal dataset and data from Shutterstock and Pond5 <a class="yt-timestamp" data-t="01:43:17">[01:43:17]</a> <a class="yt-timestamp" data-t="02:11:20">[02:11:20]</a>. Training involved 30-second audio crops for 1 million steps using the AdamW optimizer with mixed precision (FP16/BFloat16) <a class="yt-timestamp" data-t="01:34:06">[01:34:06]</a> <a class="yt-timestamp" data-t="01:37:50">[01:37:50]</a>.

### Evaluation Metrics

The system was evaluated using both objective and subjective metrics:

*   **Objective Metrics**:
    *   **Fréchet Audio Distance (FAD)**: Measures the plausibility of generated audio by comparing embeddings from a pre-trained audio classifier <a class="yt-timestamp" data-t="01:48:54">[01:48:54]</a> <a class="yt-timestamp" data-t="01:50:01">[01:50:01]</a>.
    *   **KL Divergence**: Quantifies the similarity of class probabilities between original and generated music using an audio classifier <a class="yt-timestamp" data-t="01:48:54">[01:48:54]</a> <a class="yt-timestamp" data-t="01:50:08">[01:50:08]</a>.
    *   **CLAP Score**: Computes the alignment between text descriptions and generated audio <a class="yt-timestamp" data-t="01:48:54">[01:48:54]</a> <a class="yt-timestamp" data-t="01:52:16">[01:52:16]</a>.
    *   **Chroma Cosine Similarity**: A new metric introduced to measure the average cosine similarity between frames of quantized chromas of reference and generated samples <a class="yt-timestamp" data-t="01:58:43">[01:58:43]</a>.
*   **Subjective (Human) Metrics**: Human evaluators, typically from Amazon Mechanical Turk, rated samples based on overall quality (OVL) and relevance to the text input (Rel) on a scale of 1 to 100 <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a> <a class="yt-timestamp" data-t="01:53:33">[01:53:33]</a>. Melody matching was also rated against reference pieces <a class="yt-timestamp" data-t="01:59:26">[01:59:26]</a>.

### Ablation Studies and Findings

*   **Model Size**: Studies comparing 300 million, 1.5 billion, and 3.3 billion parameter models showed only marginal improvements in objective metrics, and human evaluators perceived roughly the same quality across all sizes <a class="yt-timestamp" data-t="02:01:11">[02:01:11]</a> <a class="yt-timestamp" data-t="02:01:21">[02:01:21]</a>. This suggests that the 300M parameter model might be sufficient <a class="yt-timestamp" data-t="02:01:55">[02:01:55]</a>.
*   **Codebook Patterns**: While "flattening" achieved the best objective scores, it came at a high computational cost. The "delay" and "partial flattening" patterns achieved similar quality for a fraction of the computational effort (e.g., 1500 steps for delay vs. 6000 for flattening) <a class="yt-timestamp" data-t="01:59:52">[01:59:52]</a> <a class="yt-timestamp" data-t="02:00:28">[02:00:28]</a>. Human ratings for these patterns were largely consistent <a class="yt-timestamp" data-t="02:00:51">[02:00:51]</a>.
*   **Text Encoders**: The choice of text encoder (T5, Flan-T5, CLAP) significantly impacted performance, sometimes more so than model size or codebook patterns <a class="yt-timestamp" data-t="02:15:28">[02:15:28]</a>.

## Challenges and Ethical Considerations

The field of AI music generation still faces several challenges:
*   **Data Scarcity and Access**: Many state-of-the-art models are trained on internal or proprietary datasets (e.g., Meta's internal licensed music, Shutterstock, Pond5), limiting public access and hindering reproducible research <a class="yt-timestamp" data-t="01:56:46">[01:56:46]</a> <a class="yt-timestamp" data-t="01:57:50">[01:57:50]</a>.
*   **Lack of Standardization**: There isn't yet a single, agreed-upon method for audio generation, with various techniques and combinations being explored <a class="yt-timestamp" data-t="02:09:51">[02:09:51]</a>.
*   **Ethical Implications**: Concerns include the potential for unfair competition for artists and a lack of diversity in training datasets, often containing a larger proportion of Western-style music <a class="yt-timestamp" data-t="02:12:22">[02:12:22]</a> <a class="yt-timestamp" data-t="02:12:31">[02:12:31]</a>. Open research is seen as a way to ensure equitable access to these powerful models <a class="yt-timestamp" data-t="02:12:42">[02:12:42]</a>.