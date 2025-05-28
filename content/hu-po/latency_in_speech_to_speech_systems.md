---
title: Latency in speech to speech systems
videoId: x3fX7v7xjUA
---

From: [[hu-po]] <br/> 

Modern [[speech_to_speech_models | speech to speech systems]], often referred to as [[speech_to_speech_ai_app_features | voice mode]] experiences, aim to create natural and responsive conversations between a user and an AI. A critical challenge in achieving this is minimizing [[memory_bandwidth_and_machine_learning_bottlenecks | latency]] <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Traditional Pipeline Latency

Older [[speech_to_speech_models | speech to speech systems]] typically rely on a cascaded pipeline of independent components <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>:
1.  **Voice Activity Recognition (VAR)** <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
2.  **Speech Recognition (ASR)**: Converts user audio into text <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  **Textual Dialogue (LLM/NLU)**: A text-to-text [[evolution_of_language_models_and_memory_systems | language model]] processes the text <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
4.  **Speech-to-Speech (TTS)**: Converts the AI's textual response back into audio <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

The primary issue with this traditional design is that [[memory_bandwidth_and_machine_learning_bottlenecks | latency]] compounds across these many components <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, resulting in a typical global [[memory_bandwidth_and_machine_learning_bottlenecks | latency]] of several seconds <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This delay is too slow for natural human conversation <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Additionally, [[language_model_performance_and_sensitivity | paralinguistic information]] like emotion and accent can be lost when speech is converted to text and back <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Text-based [[evolution_of_language_models_and_memory_systems | language models]] also tend to generate written English rather than conversational spoken English, which includes filler words and non-text symbols <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>.

## Low-Latency Speech-to-Speech Models

Recent advancements, exemplified by open-source models like Moshi and Llama Omni, aim to solve the [[memory_bandwidth_and_machine_learning_bottlenecks | latency]] problem by integrating these separate parts into a single system <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### Moshi: A Multi-Stream Approach
Moshi, developed by a small French organization called Qti, uses a [[tokenization_and_latent_spaces_in_ai | speech-text Foundation model]] that explicitly processes input and output audio streams jointly into two auto-regressive [[tokenization_and_latent_spaces_in_ai | token]] streams <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Design**: Moshi employs a novel "multi-stream" [[evolution_of_language_models_and_memory_systems | Transformer]]-based architecture, removing the concept of speaker turns <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This allows training on natural conversations with arbitrary dynamics, including overlap and interruptions <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Parallel Streams**: Instead of a single sequence of [[tokenization_and_latent_spaces_in_ai | tokens]], Moshi handles multiple simultaneous streams:
    *   **Text Tokens**: For an inner monologue or "scratchpad" <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
    *   **Semantic Tokens**: Representing the content of the audio <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
    *   **Acoustic Tokens**: Representing the actual sound/waveform, including intonation and emotion <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
    *   **User Stream**: Models the user's speech, even predicting what the user might say <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.
*   **Latency**: Moshi achieves a theoretical lower limit of 160 milliseconds and 200 milliseconds in practice <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This is achieved by operating at an 80-millisecond frame rate and introducing a two-frame delay between input and output for better context <a class="yt-timestamp" data-t="00:51:16">[00:51:16]</a>.
*   **Silence Tokens**: When the user speaks and Moshi remains silent, the model still outputs [[tokenization_and_latent_spaces_in_ai | tokens]], but these decode into a near-silent waveform <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>.

### Llama Omni: Seamless Speech Interaction
Llama Omni, from Chinese academic institutions, also focuses on low-latency seamless speech interaction <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>.
*   **Design**: It uses a pre-trained [[efficient_inference_techniques_for_vision_language_models | speech encoder]], a speech adapter, an [[evolution_of_language_models_and_memory_systems | LLM]], and a streaming speech decoder <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.
*   **Component Integration**: Llama Omni is designed similarly to [[efficient_inference_techniques_for_vision_language_models | Vision Language Models]] (VLMs) <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>. It uses a pre-trained speech encoder (like Whisper) and a pre-trained [[evolution_of_language_models_and_memory_systems | language model]] (like Llama 3.1 8B Instruct) <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>. An adapter layer glues these components together <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>.
*   **Latency**: Llama Omni boasts a [[memory_bandwidth_and_machine_learning_bottlenecks | latency]] as low as 226 milliseconds <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.
*   **Decoder Behavior**: Its speech decoder runs in a non-auto-regressive manner <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a>, processing chunks rather than attending to the entire conversation context in real-time, which might limit its ability to incorporate dynamic elements like emotion <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>.

## Human Perception of Latency
Human reaction time is around 100 milliseconds <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. While differences between 10ms and 100ms are noticeable, sub-millisecond differences are not <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. The ~200ms latency of these models is considered "more than good enough" for natural conversation <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.

## Technical Considerations for Latency
*   **Audio Sampling and Processing**: Audio waveforms have many samples per second (e.g., 24 kHz) <a class="yt-timestamp" data-t="01:19:42">[01:19:42]</a>. To be processed by [[evolution_of_language_models_and_memory_systems | Transformers]], this high-dimensional data must be compressed into a discretized sequence of [[tokenization_and_latent_spaces_in_ai | tokens]] <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>. This involves significant upsampling and downsampling to reduce the sequence length <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.
*   **Causal Processing**: Moshi's Mimi encoder and decoder are causal, allowing for streaming inference without looking ahead in time, which is essential for real-time applications <a class="yt-timestamp" data-t="00:50:11">[00:50:11]</a>.
*   **Synchronization**: For real-time [[speech_to_speech_models | speech to speech systems]] with strict timing, coordinating operations between the CPU and GPU is crucial <a class="yt-timestamp" data-t="01:37:01">[01:37:01]</a>. Tools like CUDA events are used to synchronize tasks and allow for efficient overlap of computation and communication <a class="yt-timestamp" data-t="01:36:26">[01:36:26]</a>.
*   **[[efficiency_in_compute_for_language_models | Quantization]]**: This technique reduces the precision of model parameters to decrease [[memory_bandwidth_and_machine_learning_bottlenecks | compute]] footprint <a class="yt-timestamp" data-t="01:33:14">[01:33:14]</a>, which is vital for running models on devices like cell phones <a class="yt-timestamp" data-t="01:33:19">[01:33:19]</a>. However, [[efficiency_in_compute_for_language_models | quantization]] is lossy and can degrade audio quality if applied too heavily <a class="yt-timestamp" data-t="01:33:48">[01:33:48]</a>.

## Interconnected AI Research
The development of low-latency [[speech_to_speech_models | speech to speech systems]] heavily relies on previously trained models and synthetically generated datasets <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>. For example:
*   Both Moshi and Llama Omni leverage OpenAI's Whisper (especially Whisper Large V3) for components like speech encoders or for transcribing audio data <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.
*   WavLM, another pre-trained audio model, is used by Moshi for knowledge distillation <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
*   Text-to-Speech (TTS) models like Cozy Voice 300M SFT are used to convert vast text datasets (e.g., Alpaca, UltraChat) into synthetic speech datasets for training <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>.
*   Older datasets like the Fisher dataset (collected in 2004) provide ground truth separated audio streams crucial for multi-stream training <a class="yt-timestamp" data-t="01:20:23">[01:20:23]</a>.

This interconnectedness means that current AIs are improving themselves by feeding off the outputs of other AIs <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>, leading to a paradigm shift where creating vast amounts of synthetic data is possible without relying on user-generated data <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>.