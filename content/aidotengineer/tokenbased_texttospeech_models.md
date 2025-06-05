---
title: TokenBased TexttoSpeech Models
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

Token-based text-to-speech (TTS) models are designed to convert text into speech by predicting sequences of audio tokens <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. This approach is conceptually similar to how large language models predict the next word or token in a text sequence <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

## How Token-Based Models Work

A [[Audio Token Representation and Codebooks | token-based text-to-speech model]] takes in a series of text tokens and predicts the next audio token <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. Ideally, it can also incorporate a history of both text and audio from previous conversation to recursively decode and produce the next audio token, resulting in a string of audio tokens that represent the desired speech <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

The core of this process relies on a transformer model that can ideally input text and audio, and output a string of audio tokens <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

## [[Audio Token Representation and Codebooks | Audio Token Representation and Codebooks]]

A fundamental challenge for [[Audio Token Representation and Codebooks | token-based text-to-speech models]] is how to create discrete tokens for continuous audio soundwaves <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

### Codebooks
Audio, or small pieces of audio, can be represented as a selection from a codebook <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. A codebook acts like a dictionary containing a series of vectors, where each vector represents a specific sound <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. These codebooks can be quite large to capture a wide range of acoustics and semantics <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. This allows sound to be represented discretely, similar to how text discretely represents meaning <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

### Training Codebooks
Codebooks are typically trained using an encoder-decoder architecture <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.
1.  A soundwave is taken as input <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
2.  A transformer converts the soundwave into tokens <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
3.  Another transformer decodes these tokens back into a soundwave <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
4.  During training, the system assesses whether the decoded output matches the original input <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. Any difference (loss) is used to back-propagate and update the model's weights <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.

### Hierarchical Representation
For better sound representation, instead of just one token per time step, a hierarchical representation or multiple tokens are used at the same timestamp or window <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. This provides a more detailed representation by allowing higher-level meaning or acoustics to be represented alongside more granular details through multiple layers of representation <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

## Sesame CSM1B Model

The Sesame CSM1B model is a specific example of a [[Audio Token Representation and Codebooks | token-based text-to-speech model]] <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. It utilizes 32 tokens at every window to represent sound <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.

Its architecture includes:
*   **Main Transformer**: Predicts the "zeroth" token auto-regressively <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. This is a 1-billion-parameter model <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
*   **Secondary Transformer (Depth Decoder)**: Decodes the other 31 "stack" tokens, handling the hierarchical representation <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>. This is a much smaller model <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
*   **Codec Model**: Manages the conversion between waveform and tokens <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.

## [[TexttoSpeech Model FineTuning | Fine-tuning]] and [[Voice Cloning and FineTuning Techniques | Voice Cloning]]

Pre-trained [[Audio Token Representation and Codebooks | token-based text-to-speech models]] like Sesame CSM1B can take text and audio to output a stream of audio <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

### [[Data Preparation for TexttoSpeech Models | Data Preparation]]
For [[texttospeech_model_finetuning | fine-tuning]], a voice dataset is needed <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. This can be recorded by oneself, or audio can be pulled from a YouTube video and used as a basis for fine-tuning <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

The [[data_preparation_for_texttospeech_models | data generation]] process involves:
1.  Selecting a YouTube video, ideally with a single speaker to avoid complex diarization <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.
2.  Using Whisper (e.g., "turbo" model) to transcribe the video <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.
3.  Manually correcting the transcript (e.g., misspelled words) <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.
4.  Converting the transcript into a dataset of audio snippets (e.g., up to 30 seconds) and their corresponding text transcriptions <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. Approximately 50 such 30-second snippets are often enough to start seeing an effect <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>. These are stored with an audio column and a text column, and optionally a source column for speaker ID <a class="yt-timestamp" data-t="19:11:00">[19:11:00]</a>.

### [[TexttoSpeech Model FineTuning | Fine-tuning]] with Unsloth
[[TexttoSpeech Model FineTuning | Fine-tuning]] is performed using libraries like Unsloth, which is based on transformers <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This involves:
*   Loading the base model (e.g., CSM1B) <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>.
*   Applying LoRA adapters to train a subset of parameters, typically focusing on linear layers <a class="yt-timestamp" data-t="22:18:00">[22:18:00]</a>. This saves memory and speeds up training <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>.
*   Preparing the processed dataset for the trainer, including setting maximum text and audio lengths <a class="yt-timestamp" data-t="24:11:00">[24:11:00]</a>.
*   Configuring the trainer with parameters like virtual batch size, number of epochs (e.g., one epoch for initial tests), learning rate, and optimizer <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>.

### [[Voice Cloning and FineTuning Techniques | Voice Cloning]]
[[Voice Cloning and FineTuning Techniques | Voice cloning]] is distinct from [[texttospeech_model_finetuning | fine-tuning]] <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>. In [[voice_cloning_and_finetuning_techniques | voice cloning]], an audio sample is passed into the model, and the model then generates new audio that tends to sound more like the provided sample <a class="yt-timestamp" data-t="18:04:00">[18:04:00]</a>. This allows for a more consistent speaker voice without explicit fine-tuning <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.

While [[voice_cloning_and_finetuning_techniques | voice cloning]] improves the similarity to a target voice, combining [[texttospeech_model_finetuning | fine-tuning]] with [[voice_cloning_and_finetuning_techniques | cloning]] often yields the best performance, even with relatively small datasets (e.g., a 30-minute video) <a class="yt-timestamp" data-t="31:14:00">[31:14:00]</a>. For even better performance, more data (e.g., 500 rows of 30-second snippets) can be beneficial, especially for improved quality without [[voice_cloning_and_finetuning_techniques | voice cloning]] <a class="yt-timestamp" data-t="33:04:00">[33:04:00]</a>.