---
title: Google Deepmind Mirasol paper
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

The Mirasol 3B paper, "A Multimodal Autoregressive Model for Time-Aligned and Contextual Modalities," is a research paper from Google DeepMind and Google Research <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. It was first published on arXiv in 2023 and has received updates since <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. This paper explores a more advanced approach to multimodal models compared to earlier methods, focusing on video, audio, and text modalities <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>.

## Modalities and Processing

Mirasol 3B primarily works with video and audio inputs <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>.
Video and audio information are obtained at a much higher rate than text and are roughly aligned in time <a class="yt-timestamp" data-t="00:43:31">[00:43:31]</a>. This rough time alignment is crucial as audio corresponds to specific pieces of video <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

The model processes these modalities by partitioning video and audio sequences into consecutive "snippets" or chunks <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. The goal is to turn raw video and audio into sequences of tokens that can be fed into a Transformer model <a class="yt-timestamp" data-t="00:44:29">[00:44:29]</a>.

### Spectrograms for Audio
A key innovation in Mirasol 3B is representing audio as a spectrogram <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>. By turning audio into an image (spectrogram), the model can reuse the same Vision Transformer (ViT) backbone to encode both video and audio, making the process more efficient <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>. This means a single encoder can consume and encode both vision and audio <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.

### 3D Tubes for Video
The vision encoder in Mirasol 3B consumes "3D tubes" <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>. A video is treated as a sequence of image frames <a class="yt-timestamp" data-t="00:52:09">[00:52:09]</a>. These tubes correspond to specific local regions in space and specific regions in time <a class="yt-timestamp" data-t="00:52:15">[00:52:15]</a>. This allows the model to encode features that represent either the whole sequence (large time receptive field, small spatial field) or more spatial information (large spatial field, short sequential part) <a class="yt-timestamp" data-t="00:52:39">[00:52:39]</a>.

## Architecture

Mirasol 3B utilizes a "combiner" mechanism, which is similar to a projector <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>. This combiner takes the video and audio inputs and turns them into tokens <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>. This approach is reminiscent of "old school" Vision Language Models (VLMs) that encode vision and then project it into tokens for a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.

### Token Turing Machine
A significant, though somewhat buried, architectural component in Mirasol 3B is the "token Turing machine" <a class="yt-timestamp" data-t="00:59:14">[00:59:14]</a>.
A token Turing machine is described as a recurrent sequential model with Transformers and token-based operations <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>. It maintains an external memory <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>.

[!INFO] This mechanism allows the model to:
*   Read features from input and memory <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>.
*   Pass these features to a processor (also a Transformer) to generate intermediate outputs <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>.
*   Update the memory and produce the final output <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.

This external memory feature is akin to a built-in Retrieval Augmented Generation (RAG) system, allowing the model to recall information over time <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>. It significantly reduces the total time complexity for computation from O(T²) (traditional Transformers) to O(T) (constant with respect to time), as the computation is based on a fixed-size memory <a class="yt-timestamp" data-t="01:02:56">[01:02:56]</a>. This concept is similar to a Long Short-Term Memory (LSTM) network, but with Transformers replacing individual gates and components <a class="yt-timestamp" data-t="01:04:32">[01:04:32]</a>.

### Cross-Attention
The paper notes that cross-attention weights coordinate the learning between model components <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>. This [[selfimprovement_in_ai_models | decoupling]] allows for better parameter distribution within the model <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>. Unlike some other architectures, Mirasol 3B finds cross-attention beneficial because it allows information to flow from audio and images into the more text-focused parts of the model <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>.

## Training

Mirasol 3B is a relatively tiny model, at 3 billion parameters <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>. Half of its parameters are dedicated to the audio plus video autoregressive model (the combiner and encoders) <a class="yt-timestamp" data-t="01:06:29">[01:06:29]</a>.

The model is pre-trained on video-text pairs, using over 3 million samples <a class="yt-timestamp" data-t="01:07:32">[01:07:32]</a>.

Training losses include:
*   **Standard cross-entropy loss** for target and output text sequences <a class="yt-timestamp" data-t="01:05:22">[01:05:22]</a>.
*   **Modality reconstruction loss** where some audio-visual tokens are masked, and the model attempts to reconstruct them <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>. This helps train the new audio/video encoders <a class="yt-timestamp" data-t="01:05:53">[01:05:53]</a>.

## Comparison to Other Models

Mirasol 3B is noted to be "state-of-the-art" on multiple well-established multimodal benchmarks <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>. Processing video chunks autoregressively in time is found to be more advantageous than learning from the full video at once <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>.

While Mirasol 3B consumes video and audio, its output is text-only <a class="yt-timestamp" data-t="01:06:57">[01:06:57]</a>. This contrasts with Meta's Chameleon model, which outputs interleaved text and images <a class="yt-timestamp" data-t="01:00:58">[01:00:58]</a>, and is considered less advanced in that specific output capability <a class="yt-timestamp" data-t="01:10:49">[01:10:49]</a>. However, Mirasol 3B's ability to ingest audio and video places it closer to models like GPT-4o and Project Astra, which were demoed consuming audio and video <a class="yt-timestamp" data-t="01:07:59">[01:07:59]</a>. The paper is seen as a smaller, publicly available version of the sophisticated models being developed by Google <a class="yt-timestamp" data-t="01:08:20">[01:08:20]</a>.

The use of an external memory (token Turing machine) in Mirasol 3B mirrors behavior seen in demos of GPT-4o, where the model demonstrated memory of past visual events even after the visual input was no longer present <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

## Future Implications

The advancements seen in papers like Mirasol 3B suggest a future where models can consume and output multiple modalities, including audio, video, and text, in an interleaved fashion <a class="yt-timestamp" data-t="01:10:51">[01:10:51]</a>. The progression from text-only outputs to interleaved text and images (Chameleon) and then to audio/video inputs (Mirasol 3B, GPT-4o) points towards fully multimodal interaction <a class="yt-timestamp" data-t="01:10:58">[01:10:58]</a>. The next step is models capable of outputting video and audio, potentially leading to realistic visual representations of AI agents <a class="yt-timestamp" data-t="01:17:52">[01:17:52]</a>.

[!WARNING] [[challenges_and_implications_for_ai_safety | Challenges and implications for AI safety]] for such models include managing conditional flow during inference (as the model doesn't know if the next token will be image or text) and handling fixed-size blocks of tokens for images (meaning an image can't be paused or partially generated mid-sequence) <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>. These are new challenges that arise with interleaved multimodal generation <a class="yt-timestamp" data-t="00:55:02">[00:55:02]</a>.

The trend in [[open_source_artificial_intelligence | AI]] development, as illustrated by these papers, is moving towards end-to-end training of increasingly larger models on massive datasets, with a focus on removing architectural complexity <a class="yt-timestamp" data-t="01:30:20">[01:30:20]</a>. This approach requires significant computational resources, primarily accessible to large companies like Google and Meta <a class="yt-timestamp" data-t="01:36:08">[01:36:08]</a>.