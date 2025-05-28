---
title: Music generation with MusicGen
videoId: SodPUNBFeMY
---

From: [[hu-po]] <br/> 

MusicGen is a recent development from Meta AI Research that focuses on [[conditional_music_generation | simple and controllable music generation]] <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. The model, detailed in a paper released in June 2023 <a class="yt-timestamp" data-t="01:14:15">[01:14:15]</a>, is designed to generate high-quality music based on textual descriptions and/or melodic features <a class="yt-timestamp" data-t="00:44:59">[00:44:59]</a>.

## Core Architecture and Principles

MusicGen is built upon a single-stage Transformer language model (LM) <a class="yt-timestamp" data-t="05:27:54">[05:27:54]</a>, a departure from prior work that often utilizes cascading or hierarchical models for music generation <a class="yt-timestamp" data-t="05:57:57">[05:57:57]</a>. This single-stage approach aims to produce the final audio in one inference step, potentially speeding up the process <a class="yt-timestamp" data-t="06:26:24">[06:26:24]</a>.

### [[Using encoders and tokenization for music AI | Audio Tokenization with EnCodec]]

The model does not generate raw audio waveforms directly. Instead, it operates over "compressed discrete music representations," also known as tokens <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. This is achieved using the EnCodec audio tokenizer, a convolutional autoencoder that quantizes the latent space using Residual Vector Quantization (RVQ) <a class="yt-timestamp" data-t="02:30:53">[02:30:53]</a>, <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

Key aspects of this tokenization include:
*   **Sampling Rate**: EnCodec converts 32 kHz monophonic audio (32,000 samples per second) into a lower frame rate of 50 Hz (50 tokens per second) <a class="yt-timestamp" data-t="02:07:05">[02:07:05]</a>. This drastically reduces the amount of data the Transformer needs to process <a class="yt-timestamp" data-t="02:44:46">[02:44:46]</a>.
*   **Residual Vector Quantization (RVQ)**: RVQ uses multiple "codebooks" (quantization levels) <a class="yt-timestamp" data-t="02:57:43">[02:57:43]</a>. Each subsequent codebook quantizes the "residual" (the error or difference) left by the previous quantization level <a class="yt-timestamp" data-t="03:00:23">[03:00:23]</a>. In MusicGen, four quantizers (codebooks) are used <a class="yt-timestamp" data-t="02:18:53">[02:18:53]</a>, each with a size of 2048 distinct tokens <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. The first codebook typically contains the most significant portion of the audio signal <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

### Codebook Interleaving Patterns

A significant contribution of MusicGen is its "codebook interleaving patterns" <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>. These patterns define how the multiple parallel streams of acoustic tokens (from the different RVQ codebooks) are processed by the single Transformer LM <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>. The goal is to optimize the trade-off between generation quality and computational speed <a class="yt-timestamp" data-t="02:24:15">[02:24:15]</a>.

Different patterns explored include:
*   **Flattening Pattern**: Concatenates all codebook tokens into one giant vector, leading to a high computational cost but potentially better generation <a class="yt-timestamp" data-t="02:04:03">[02:04:03]</a>.
*   **Delay Pattern**: Introduces an offset (delay) between the prediction of different codebooks, allowing some degree of parallel processing while acknowledging dependencies <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>. This results in fewer autoregressive steps and is more computationally efficient <a class="yt-timestamp" data-t="02:00:28">[02:00:28]</a>.
*   **Parallel Pattern**: Predicts all codebooks from the same timestep in parallel, potentially missing dependencies <a class="yt-timestamp" data-t="02:03:30">[02:03:30]</a>.
*   **Valley Pattern**: Predicts the first (most important) codebook for all timesteps, then predicts the remaining codebooks (two, three, and four) in parallel <a class="yt-timestamp" data-t="02:03:44">[02:03:44]</a>.

## Conditional Music Generation

MusicGen allows for conditioning on both text and melodic features <a class="yt-timestamp" data-t="06:43:26">[06:43:26]</a>.

*   **Text Conditioning**: Textual descriptions (e.g., "cheerful song with acoustic guitars" <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>) are encoded using pre-trained text encoders like T5, Flan-T5, or CLAP (a joint text-audio representation model) <a class="yt-timestamp" data-t="01:46:42">[01:46:42]</a>.
*   **Melody Conditioning**: Users can provide an MP3 file as a melodic reference <a class="yt-timestamp" data-t="05:05:39">[05:05:39]</a>. This melody is converted into a chromogram (a 2D image-like representation of audio <a class="yt-timestamp" data-t="01:09:19">[01:09:19]</a>), which is then quantized by taking the "dominant time-frequency bin" (ARG Max) at each step <a class="yt-timestamp" data-t="01:10:27">[01:10:27]</a>, <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. This selected information is then fed into the Transformer as a prefix to the input sequence <a class="yt-timestamp" data-t="01:17:36">[01:17:36]</a>.

## Training and Evaluation

The MusicGen models were trained on 20,000 hours of licensed music from internal datasets, Shutterstock, and Pond5 <a class="yt-timestamp" data-t="01:43:17">[01:43:17]</a>, <a class="yt-timestamp" data-t="01:43:42">[01:43:42]</a>. Training involved 30-second audio crops for 1 million steps using the AdamW optimizer <a class="yt-timestamp" data-t="01:34:06">[01:34:06]</a>. [[Training and finetuning of MusicGen models | Mixed-precision training]] (using FP16 and BFloat16) and Flash Attention were employed for efficiency <a class="yt-timestamp" data-t="01:38:10">[01:38:10]</a>.

Evaluation involved both objective metrics (FID, KL Divergence, CLAP score, and a new "chroma cosine similarity" metric <a class="yt-timestamp" data-t="01:48:43">[01:48:43]</a>, <a class="yt-timestamp" data-t="01:53:53">[01:53:53]</a>) and human subjective studies <a class="yt-timestamp" data-t="01:48:49">[01:48:49]</a>. Human evaluators rated overall quality and relevance to text input on a scale of 1 to 100 <a class="yt-timestamp" data-t="01:53:34">[01:53:34]</a>.

## [[Comparison with other music generation models | Performance and Findings]]

*   **Model Size**: While MusicGen was trained in various sizes (300M, 1.5B, 3.3B parameters) <a class="yt-timestamp" data-t="01:32:37">[01:32:37]</a>, human evaluations suggested that larger models did not significantly outperform the smallest 300M parameter model in terms of perceived quality <a class="yt-timestamp" data-t="02:01:27">[02:01:27]</a>.
*   **Melody Conditioning**: Objective metrics showed that adding melody conditioning could sometimes degrade performance <a class="yt-timestamp" data-t="01:55:08">[01:55:08]</a>, <a class="yt-timestamp" data-t="01:53:30">[01:53:30]</a>. However, human ratings were not significantly affected, and specific "chroma cosine similarity" evaluations confirmed its ability to follow a given melody <a class="yt-timestamp" data-t="01:58:36">[01:58:36]</a>.
*   **Codebook Patterns**: The delay pattern resulted in the fewest autoregressive steps (1500 for 30 seconds of audio), significantly faster than the flattening pattern (6000 steps) <a class="yt-timestamp" data-t="02:00:28">[02:00:28]</a>. The choice of codebook pattern had minimal impact on human perceived quality <a class="yt-timestamp" data-t="02:00:52">[02:00:52]</a>.
*   **Text Encoders**: The choice of text encoder (e.g., T5 vs. Flan-T5 vs. CLAP) had a noticeable impact on generation quality <a class="yt-timestamp" data-t="02:15:31">[02:15:31]</a>.

## Availability and [[GitHub repository analysis for audio generation | AudioCraft Exploration]]

MusicGen's code and models are publicly available on a GitHub repository called AudioCraft <a class="yt-timestamp" data-t="01:25:26">[01:25:26]</a>, along with a Colab notebook and a Hugging Face demo <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. The models include pre-trained weights for download via Git LFS <a class="yt-timestamp" data-t="03:22:54">[03:22:54]</a>.

## Ethical Considerations

The paper acknowledges several ethical challenges associated with large-scale generative models, including:
*   Potential lack of diversity in the training dataset, which predominantly consists of Western-style music <a class="yt-timestamp" data-t="02:24:55">[02:24:55]</a>.
*   The potential for unfair competition for human artists <a class="yt-timestamp" data-t="02:33:04">[02:33:04]</a>.

The authors advocate for open research to ensure equal access to these models for all actors <a class="yt-timestamp" data-t="02:43:08">[02:43:08]</a>.