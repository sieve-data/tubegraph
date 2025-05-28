---
title: Open Source Voice Mode Alternatives
videoId: x3fX7v7xjUA
---

From: [[hu-po]] <br/> 

As [[Speech to Speech Models | speech-to-speech models]] become more prevalent, exemplified by OpenAI's Advanced Voice Mode, the open-source community is actively developing comparable alternatives. Two prominent open-source projects, Moshi and Llama Omni, demonstrate innovative approaches to achieve low-latency, natural conversational AI experiences.
<a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>

## Moshi: A Speech-Text Foundation Model for Real-Time Dialogue
Moshi, developed by Qai, a small lab based in Paris, France, released its extensive 67-page paper on September 18, 2024.
<a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>
The project exemplifies [[Open Source vs Proprietary AI Models | open-source contributions]], sharing detailed experiments, comparisons, and architectural reasoning.
<a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>

### Addressing Limitations of Traditional Systems
Traditional spoken dialogue systems relied on a pipeline of independent components:
*   **Voice Activity Recognition (VAR)**
*   **Speech Recognition (ASR)**
*   **Textual Dialogue (LLM)**
*   **Speech-to-Speech (TTS)**
<a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>

This cascaded approach suffered from compounding latency, typically resulting in several seconds of delay, which is too slow for natural human conversation.
<a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a> Additionally, [[Speech to Speech Models | paralinguistic information]] like emotion and accent was lost during the conversion to text and back, leading to a robotic output.
<a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>

### Moshi's Key Innovations
Moshi addresses these issues by integrating these components into a single system, primarily relying on [[transformer_models_in_audio_generation | Transformer-based models]].
<a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>

#### Multistream Audio Language Model
Moshi is designed as a multi-stream audio language model that explicitly processes input and output audio streams jointly into auto-regressive token streams.
<a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a> This design removes the concept of discrete "speaker turns," allowing the model to be trained on natural conversations with overlaps and interruptions.
<a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>
When the user speaks, Moshi can still produce tokens, but they decode into near-silent waveforms, reflecting natural conversational dynamics.
<a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>

#### Architecture
The core components include:
*   **Mimi (Neural Audio Codec)**: Converts high-dimensional audio waveforms into compressed, discretized sequences of tokens for the Transformer.
<a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a> Mimi combines semantic (content of the audio) and acoustic (how it sounds) information into a single tokenizer using [[open_source_language_models_and_data_curation_strategies | residual vector quantization]] and [[open_source_language_models_and_data_curation_strategies | knowledge distillation]] from external models like WavLM.
<a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>
*   **RQ Transformer (Depth Transformer)**: This [[transformer_models_in_audio_generation | Transformer model]] is capable of handling multiple simultaneous sequences (streams).
<a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a> These streams include:
    *   Text tokens (for inner monologue).
    *   Semantic tokens (Moshi's output).
    *   Acoustic tokens (Moshi's output).
    *   Semantic tokens (user's input).
    *   Acoustic tokens (user's input).
<a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>
*   **Inner Monologue**: Moshi displays an "inner monologue" (text tokens) that represents its thought process, acting like a scratchpad.
<a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>
*   **Helium Language Model**: Serves as the text language model backbone, though it requires specific training techniques (alternating with text-only data) to prevent catastrophic forgetting due to the complex audio modalities.
<a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>

#### Latency
Moshi operates at an 80-millisecond frame rate, outputting an entire column of tokens for each time step.
<a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a> By introducing a slight two-step delay (160 milliseconds) between semantic and acoustic tokens for better quality, Moshi achieves a theoretical latency of 160ms, with 200ms in practice.
<a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a> This is close to human perceptual limits.
<a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>

#### Training Data Strategy
Moshi's training heavily relies on synthetically generated data:
*   **Text Data**: Collected from Wikipedia, Wiki books, Wiki Source, Wiki news, and Stack Exchange.
<a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a>
*   **Audio Data Creation**: 7 million hours of text data were transcribed using [[open_source_language_models_and_data_curation_strategies | Whisper]].
<a class="yt-timestamp" data-t="01:18:54">[01:18:54]</a> Text was converted into speech using the Cozy Voice 300M SFT TTS model, with modifications like adding filler words and converting non-text symbols to spoken forms to resemble natural spoken English.
<a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a> 20,000 hours of synthetic speech data were generated using a TTS model conditioned on a single actor's voice to give Moshi a consistent voice.
<a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>
*   **Fisher Dataset**: 2,000 hours of phone conversations (collected in 2004) with two separate channels (allowing ground truth separated streams for training multi-stream generation). This dataset was upsampled using Audio SR.
<a class="yt-timestamp" data-t="01:20:23">[01:20:23]</a>
*   **Instruction Tuning**: Instruction tuning datasets like Alpaca were adapted for speech responses.
<a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a> Data augmentation techniques were used to create audio with lower quality to make the model robust to noisy environments.
<a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a> Safety conversations were also generated to train the model to refuse unethical requests.
<a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>

## Llama Omni: Seamless Speech Interaction with Large Language Model
Llama Omni, originating from Chinese academic institutions, also aims for low-latency, seamless speech interaction.
<a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>

### Architecture and Training
Llama Omni's design is reminiscent of [[Open Source vs Proprietary AI Models | vision-language models]]:
*   **Pre-trained Speech Encoder**: Utilizes [[open_source_language_models_and_data_curation_strategies | Whisper]] (specifically Whisper Large V3) to convert waveforms into compressed representations.
<a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>
*   **Speech Adapter**: A two-layer perceptron acts as a "glue" layer to connect the pre-trained speech encoder to the Large Language Model.
<a class="yt-timestamp" data-t="01:29:30">[01:29:30]</a>
*   **Large Language Model (LLM)**: Uses Llama 3.1 8B Instruct, a relatively smaller but capable Llama model.
<a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>
*   **Streaming Speech Decoder**: Consists of several [[transformer_models_in_audio_generation | Transformer layers]]. Unlike Moshi, this decoder runs in a non-auto-regressive manner, taking the hidden states from the LLM as input to generate discrete unit sequences.
<a class="yt-timestamp" data-t="01:39:21">[01:39:21]</a> This non-auto-regressive nature might limit its ability to incorporate broader conversational context (e.g., emotional tone).
<a class="yt-timestamp" data-t="01:41:24">[01:41:24]</a>

### Latency and Data
Llama Omni achieves a low latency of 226 milliseconds.
<a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a> Its training benefits from the robust pre-trained components, particularly Whisper Large V3 (trained on millions of hours of audio).
<a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a> This reduces the need for a massive, custom-curated dataset, allowing them to use a smaller 200k synthetic speech instruction dataset.
<a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>

### [[Open Source vs Proprietary AI Models | Open Source vs Proprietary AI Models]]

Both Moshi and Llama Omni highlight the significant progress in open-source AI, offering capabilities comparable to proprietary models like OpenAI's Voice Mode. The detailed papers provide transparency into their architectures, training methodologies, and challenges.
<a class="yt-timestamp" data-t="01:39:54">[01:39:54]</a>

A key takeaway from both projects is the increasing reliance on **synthetically generated data** for training. Rather than solely relying on user-generated data, these models leverage vast amounts of existing text data and advanced TTS models to create high-quality audio datasets.
<a class="yt-timestamp" data-t="01:42:47">[01:42:47]</a> This "AI-improving-AI" loop, where previous generation AIs ([[open_source_language_models_and_data_curation_strategies | Whisper]], WavLM, Audio SR) are used to generate data for next-generation models, suggests that the perceived "data moat" of proprietary companies may be less significant than previously thought.
<a class="yt-timestamp" data-t="01:31:38">[01:31:38]</a> The relatively small "sim-to-real gap" in audio (synthetically generated audio being very close to real audio) makes this approach particularly effective.
<a class="yt-timestamp" data-t="01:37:06">[01:37:06]</a>

These open-source alternatives offer promising directions for [[future_directions_for_multimodal_and_agi_development | multimodal and AGI development]], particularly in real-time interaction and potential applications beyond speech, such as robotics with multi-stream inputs and outputs.
<a class="yt-timestamp" data-t="01:04:03">[01:04:03]</a>
For users interested in experiencing these technologies, Moshi provides a public demo at moshi.chat.
<a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>
[[Speech2Speech AI application features | Exporting and sharing audio from AI conversations]] or other features are not explicitly detailed in the provided transcript.
[[Requirements and setup for using Speech2Speech AI | Requirements and setup for using Speech2Speech AI]] are not explicitly detailed beyond using GPUs like Nvidia L40s.
<a class="yt-timestamp" data-t="01:14:11">[01:14:11]</a>