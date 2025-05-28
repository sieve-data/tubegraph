---
title: Latency in Speech Models
videoId: x3fX7v7xjUA
---

From: [[hu-po]] <br/> 

Recent advancements in [[speech_to_speech_models | speech-to-speech models]] have focused on achieving low latency to enable more natural, real-time spoken dialogue <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This contrasts with traditional cascaded systems that suffer from significant delays <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Challenges with Traditional Pipeline Systems

Older systems for spoken dialogue rely on a pipeline of independent components:
1.  **Voice Activity Recognition (VAR)** <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
2.  **Speech Recognition (ASR)**: Converts audio to text <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  **Textual Dialogue (LLM)**: Processes text and generates a text response <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
4.  **Speech to Speech (TTS)**: Converts text back into audio <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

The primary issue with this cascaded approach is that latency compounds across the many components, leading to a typical global latency of several seconds <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This delay is too slow for humans to experience natural conversation <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Additionally, paralinguistic information like emotion and accent is often lost when audio is converted to text and then back to speech <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Modern Low-Latency Approaches

Two open-source papers, Moshi and Llama Omni, propose solutions to address these latency challenges by integrating these components into a more unified system <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

### Moshi

Moshi aims for real-time dialogue by processing input and output audio streams jointly into two auto-regressive token streams <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This removes the traditional concept of speaker turns, allowing the model to be trained on natural conversations with overlaps and interruptions <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

*   **Latency**: Moshi boasts a theoretical lower limit of 160 milliseconds and achieves 200 milliseconds in practice <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
*   **Time Steps**: Each time step or "frame" in Moshi is 80 milliseconds <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   **Delay for Quality**: A slight delay of one to two steps (80-160 milliseconds) between semantic and acoustic tokens significantly improves generation quality <a class="yt-timestamp" data-t="00:51:16">[00:51:16]</a>. This minimal delay is imperceptible to humans, allowing the model more context to produce higher quality audio <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>.
*   **Multistream Design**: The model handles multiple parallel streams, including its own speech tokens, user speech tokens, and an "inner monologue" of text tokens <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>, enabled by a [[Transformer models in audio generation | depth Transformer]] <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>.

### Llama Omni

Llama Omni also focuses on low-latency [[speech_to_speech_models | speech-to-speech interaction]] <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
*   **Latency**: It achieves a latency as low as 226 milliseconds <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>, comparable to Moshi <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
*   **Architecture**: It utilizes a pre-trained speech encoder (like Whisper) <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>, a speech adapter, a [[Multimodal Language Models | Large Language Model (LLM)]] (Llama 3.1 8B Instruct) <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>, and a streaming speech decoder <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>.
*   **Simultaneous Generation**: Like Moshi, it simultaneously generates text and speech responses from speech instructions <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

## Human Perception of Latency

The goal of achieving low latency is to mimic natural human conversation <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   Human reaction time is around 100 milliseconds <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   A 60 frames per second display has about 16 milliseconds per frame <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   While noticeable differences exist between 10 milliseconds and 100 milliseconds, going below 1 millisecond typically doesn't matter for human perception <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
*   The current latencies of around 200 milliseconds are considered "more than good enough" for natural interaction <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>.

## Implications for Future AI

The pursuit of low-latency [[speech_to_speech_models | speech-to-speech models]] has broader implications for AI development:
*   **Multimodal AI**: The multi-stream design seen in Moshi could be applied to other modalities like robotics, allowing simultaneous consumption of visual, force, and proprioceptive inputs while outputting visual and action tokens <a class="yt-timestamp" data-t="01:04:50">[01:04:50]</a>.
*   **[[Quantization for large language models | Model Quantization]]**: For models to run locally on devices like cell phones or VR headsets, efficient [[Quantization for large language models | quantization]] techniques are crucial <a class="yt-timestamp" data-t="01:33:13">[01:33:13]</a>. This impacts the [[performance_and_implications_of_quantized_language_models | performance and implications of quantized language models]], influencing whether AI interactions are cloud-based (centralized control) or local (decentralized) <a class="yt-timestamp" data-t="01:34:21">[01:34:21]</a>.
*   **Data Generation**: The reliance on synthetically generated datasets (e.g., converting text data into speech data using TTS models like Cozy Voice 300M sft <a class="yt-timestamp" data-t="01:23:37">[01:23:37]</a>) suggests that user-generated data may not be a necessary "moat" for developing high-performing AI, especially given the small "sim-to-real gap" in audio <a class="yt-timestamp" data-t="01:31:02">[01:31:02]</a>. This contributes to the overall [[efficiency of large language models | efficiency of large language models]] by reducing reliance on costly human annotation.
*   **[[evaluation_metrics_for_language_models | Evaluation Metrics]]**: The use of AI (like GPT-4) to score content and style in [[evaluation_metrics_for_language_models | evaluating model output]] has become a standard, though it raises questions about bias and independent assessment <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>.