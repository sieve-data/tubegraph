---
title: Speech to Speech Models
videoId: x3fX7v7xjUA
---

From: [[hu-po]] <br/> 

Speech-to-Speech (S2S) models, often referred to as "voice mode" experiences, aim to create natural, real-time audio conversations with large language models (LLMs) <a class="yt-timestamp" data-t="01:55:59">[01:55:59]</a>. Unlike traditional pipelines, these advanced systems directly process and respond in audio form, allowing for interruptions and natural conversational dynamics <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

## Limitations of Traditional Speech Pipelines
Historically, spoken dialogue systems relied on a cascaded pipeline of independent components:
1.  **Voice Activity Recognition (VAR)** <a class="yt-timestamp" data-t="05:00:01">[05:00:01]</a>
2.  **Speech Recognition (ASR)**: Converts audio into text <a class="yt-timestamp" data-t="05:01:03">[05:01:03]</a>.
3.  **Textual Dialogue (LLM)**: Processes text and generates a text response <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.
4.  **Speech-to-Speech (TTS)**: Converts the text response back into audio <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

This cascaded approach suffered from significant drawbacks:
*   **Latency**: Latency compounded across components, typically resulting in several seconds of delay <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. This is too slow for natural human conversation <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.
*   **Loss of Paralinguistic Information**: Emotion, accent, and other non-speech audio cues were lost when audio was converted to text <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.
*   **Discrete Turns**: The traditional system required explicit speaker turns, preventing overlapping speech or interruptions, unlike real conversations <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.
*   **Written vs. Spoken English**: [[large language models and their applications | LLMs]] trained on text tend to generate written English, which differs significantly from natural spoken English (e.g., using complex sentences, ordered lists, or lacking filler words) <a class="yt-timestamp" data-t="35:25:00">[35:25:00]</a>.

## Open-Source Speech-to-Speech Models

Two recent open-source papers, Moshi and Llama Omni, address these limitations by integrating components into unified systems.

### Moshi
Moshi, developed by a small organization named Qti in Paris, France <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>, is an extensive project with a 67-page paper detailing its architecture and experiments <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

#### Key Features:
*   **Multistream Audio Language Model**: Moshi explicitly processes input and output audio streams jointly into multiple auto-regressive token streams <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>. This removes the concept of speaker turns, allowing the model to be trained on natural conversations with overlap and interruptions <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.
*   **Inner Monologue**: Moshi includes an "inner monologue" stream, which is a text output serving as a scratchpad for the [[large language models and their applications | LLM]] <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. This is an additional stream alongside the user's speech, the model's semantic tokens, and the model's acoustic tokens <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.
*   **Overlap Handling**: When the user speaks, Moshi continues to produce tokens, but these decode into natural silence, allowing for seamless overlap <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>.

#### Architecture:
Moshi's architecture integrates several components:
*   **Mimi (Neural Audio Codec)**: Converts raw audio waveforms into a compressed, discretized sequence of tokens and vice-versa <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>. Mimi is causal and can be used in a streaming fashion <a class="yt-timestamp" data-t="50:07:00">[50:07:00]</a>. It combines semantic and acoustic information into a single tokenizer using residual vector quantization and [[Ensemble Learning for Language Models | knowledge distillation]] from WavLM <a class="yt-timestamp" data-t="43:35:00">[43:35:00]</a>.
*   **RQ Transformer (Depth Transformer)**: This transformer, based on work by LucidRains, efficiently trains multi-dimensional sequences auto-regressively <a class="yt-timestamp" data-t="43:57:00">[43:57:57]</a>. It handles multiple simultaneous streams of tokens (text, semantic, acoustic for both Moshi and the user) <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. It consists of a temporal Transformer (for time-based context) and a depth Transformer (for cross-stream attention) <a class="yt-timestamp" data-t="01:06:10">[01:06:10]</a>.
*   **Helium Language Model**: This is the [[large language models and their applications | LLM]] backbone for Moshi <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>. It's a Transformer model that integrates Flash Attention and a SentencePiece tokenizer <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

#### Latency:
Moshi operates at an 80-millisecond frame rate <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>. By introducing a two-frame delay between semantic and acoustic tokens for context, it achieves a theoretical minimum latency of 160 milliseconds, with practical latency around 200 milliseconds <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

#### Training and Data:
Moshi's training involves four phases:
1.  Pre-training on unsupervised data <a class="yt-timestamp" data-t="01:28:27">[01:28:27]</a>.
2.  Post-training with simulated multistreams <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.
3.  Fine-tuning on the Fisher dataset <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.
4.  Instruction fine-tuning on a custom dataset <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

To prevent catastrophic forgetting of its original knowledge, the model is trained half the time on full text batches <a class="yt-timestamp" data-t="01:45:47">[01:45:47]</a>.

Its data generation process heavily relies on synthetic data:
*   **Text to Audio**: Text data (from Wikipedia, WikiBooks, Stack Exchange, etc.) is converted into speech using a TTS model like Cozy Voice 300M SFT <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Voice Consistency**: 20,000 hours of synthetic speech data are generated, conditioned on a single actor's voice (who recorded 70 speaking styles) to give Moshi a consistent voice <a class="yt-timestamp" data-t="01:37:41">[01:37:41]</a>.
*   **Whisper for Transcription**: 7 million hours of audio are transcribed using OpenAI's Whisper <a class="yt-timestamp" data-t="01:18:54">[01:18:54]</a>.
*   **Fisher Dataset**: This dataset contains 2,000 hours of phone conversations recorded on separate channels, providing ground truth for separated audio streams essential for multistream training <a class="yt-timestamp" data-t="01:20:23">[01:20:23]</a>. It's upsampled using Audio SR <a class="yt-timestamp" data-t="01:21:47">[01:21:47]</a>.
*   **Data Augmentation**: Misspellings and low-quality audio scenarios are simulated to make the model robust <a class="yt-timestamp" data-t="01:28:34">[01:28:34]</a>. Safety conversations are also generated to train the model to refuse unethical requests <a class="yt-timestamp" data-t="01:29:37">[01:29:37]</a>.

### Llama Omni
Llama Omni, from Chinese academic institutions <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>, also aims for low-latency, seamless speech interaction.

#### Key Features:
*   **Simultaneous Generation**: It simultaneously generates text and speech responses directly from speech instructions <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Lower Latency**: Achieves latency as low as 226 milliseconds <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

#### Architecture:
Llama Omni utilizes a more modular, yet integrated, approach:
*   **Pre-trained Speech Encoder**: Uses OpenAI's Whisper Large V3 to convert speech into compressed representations <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
*   **Speech Adapter**: A two-layer perceptron acts as a "glue" layer, connecting the pre-trained speech encoder to the [[large language models and their applications | large language model]] <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This is reminiscent of [[Multimodal Language Models | Vision-Language Models]] <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **[[large language models and their applications | LLM]]**: Based on Llama 3.1 8B Instruct, which auto-regressively generates text responses <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Streaming Speech Decoder**: This component converts the [[large language models and their applications | LLM]]'s output into discrete units and then a waveform using a vocoder <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. However, it runs in a non-auto-regressive manner, which may limit its ability to incorporate full conversational context into the audio output (e.g., emotion) <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

#### Training and Data:
Llama Omni uses a two-stage training process:
1.  **Stage 1**: The pre-trained speech encoder is frozen, and the speech adapter and [[large language models and their applications | LLM]] are trained to understand each other <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
2.  **Stage 2**: The [[large language models and their applications | LLM]] and speech adapter are frozen, and the speech decoder is fine-tuned to produce high-quality speech from the [[large language models and their applications | LLM]]'s tokens <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

Like Moshi, Llama Omni heavily relies on synthetic data:
*   It uses instruction tuning datasets (like Alpaca and UltraChat) <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   These text datasets are adapted to spoken English (by adding filler words, converting symbols) and then converted into speech using a TTS model like Cozy Voice 300M SFT <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   The training leverages Whisper Large V3, which itself was trained on millions of hours of audio, including pseudo-labeled audio generated by earlier Whisper versions <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Overarching Trends and Implications

### Low Latency and Human Perception
Both models prioritize low [[Latency in Speech Models | latency]], aiming to achieve response times (around 200ms) that feel natural to humans <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. Human reaction time is around 100 milliseconds, suggesting that further reductions in latency beyond this threshold may not significantly improve the user experience <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.

### The Role of [[Ensemble Learning for Language Models | Distillation]] and Pre-trained Models
These S2S models heavily rely on existing pre-trained models. For instance, Llama Omni uses Whisper as its encoder and decoder <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>, while Moshi uses [[Ensemble Learning for Language Models | distillation]] from WavLM to train its Mimi encoder <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This highlights a trend where AI models build upon and learn from the outputs of other AIs, creating an interconnected ecosystem where "all AIs are really just the same AI" <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

### Synthetic Data Generation and the "Data Flywheel"
A significant insight from both papers is the extensive use of synthetically generated data <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. They convert massive text datasets into audio using advanced TTS models. This suggests that for audio modalities, the "sim-to-real gap" (the difference between simulated/synthetic data and real-world data) is very small, allowing for effective training on artificial datasets <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. This challenges the traditional "data flywheel" concept, where user-generated data is seen as crucial for AI improvement, as synthetic data generation can achieve comparable results <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

### Potential Future Applications
The multi-stream design of Moshi, where a model simultaneously consumes and produces multiple types of tokens (e.g., visual, speech, action), could be applied to other domains, particularly robotics. A robot could continuously process camera input, force sensor data, and user speech, while simultaneously outputting action tokens and even updating its internal representation of the world (e.g., via streaming Gaussian Splats) <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

### Quantization and Local vs. Cloud AI
The goal of running [[Speech2Speech AI application features | S2S models]] on mobile devices necessitates quantization techniques to reduce model size and computational footprint <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. The success of quantization will determine whether AI interactions primarily occur locally on devices or in centralized cloud data centers, impacting privacy and control <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

These open-source developments provide significant insight into the capabilities and engineering required for advanced, low-[[Latency in Speech Models | latency]] speech-to-speech AI systems.