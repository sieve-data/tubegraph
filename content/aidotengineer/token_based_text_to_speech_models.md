---
title: Token based text to speech models
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

Token-based text-to-speech (TTS) models allow for the generation of speech from text, often with the ability to fine-tune the model to produce speech in a specific voice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This approach aims to train a model to output speech that sounds like a chosen voice <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## How Token-Based TTS Models Work

These models operate similarly to token-based text models like OpenAI's [[improving_chatgpts_voice_and_text_features | ChatGPT]] (e.g., GPT-4o) or Llama series models <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. While text models take a string of text and predict the next word or token recursively <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, TTS models aim to take a series of text tokens and predict the next "audio token" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Ideally, they can also incorporate a history of text and audio from previous conversation to recursively produce the next audio token <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

The core idea is to use a transformer model that inputs text and audio, and outputs a string of audio tokens <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Audio Tokens

A key challenge is representing continuous sound waves as discrete tokens <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This is achieved by representing a small piece of audio as a choice from a "code book" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. A codebook functions like a dictionary, containing a series of vectors where each vector represents a specific sound <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. These codebooks can be quite large to encompass a wide range of sounds, including acoustics and semantics <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

Codebooks are typically trained using an encoder-decoder structure <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>:
1.  A soundwave is taken as input.
2.  A transformer converts it into tokens.
3.  Another transformer decodes it back into a wave.
4.  During training, the model is optimized to minimize the difference between the input soundwave and the decoded output, adjusting weights through backpropagation <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

While a single token per time step is possible, a hierarchical representation or multiple tokens per time window works better for more detailed sound representation <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This allows for representing higher-level meaning or acoustics alongside more granular details through multiple layers of representation <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Sesame CSM1B Architecture

The Sesame model, specifically CSM1B, utilizes this hierarchical approach <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. It uses 32 tokens at every audio window to represent sound <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   A "zeroth token" is predicted by the main transformer <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   A secondary transformer decodes the other 31 "stack tokens" <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

Sesame consists of two models: the main 1-billion parameter model and a smaller model for decoding hierarchical tokens <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. The full [[architecture_and_deployment_of_speech_ai_models | model architecture]] includes:
*   A backbone model (the main transformer) <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
*   A depth decoder for the 31 additional tokens <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   A codec model to convert between waveforms and tokens <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

## [[text_to_speech_model_fine_tuning | Fine-tuning]] a Token-Based TTS Model

The process of [[text_to_speech_model_fine_tuning | fine-tuning]] a pre-trained model like CSM1B involves several steps to adapt it to a specific voice.

### [[data_preparation_for_text_to_speech | Data Preparation]]

To fine-tune, a voice dataset is needed <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This can be recorded or extracted from existing audio, such as a YouTube video <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It's recommended to use a video with a single speaker to avoid complex diarization <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The [[data_preparation_for_text_to_speech | data preparation]] process typically includes:
1.  **Audio Extraction:** Download audio from the chosen source (e.g., YouTube) <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
2.  **Transcription:** Use a tool like OpenAI's Whisper model (e.g., "turbo" size for efficiency) to transcribe the audio <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
3.  **Manual Correction:** Review the generated transcript (often a JSON file) for misspellings and make corrections <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
4.  **Snippet Generation:** Split the long transcript and audio into shorter chunks, ideally around 30 seconds in length, combining Whisper's shorter segments <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Aim for roughly 50 snippets of 30 seconds for noticeable effects <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. It is beneficial, though not strictly necessary for basic setup, to end each snippet on a full stop to improve pacing <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

The resulting dataset will have audio snippets paired with their transcriptions <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. If no speaker column is provided, a default speaker ID (e.g., '0') is assigned <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### Model Loading and Adapters

The CSM1B model is loaded using libraries like Unsloth, which leverages Hugging Face Transformers <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. The model is loaded with a specified maximum sequence length for text <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

For efficient fine-tuning, LoRA (Low-Rank Adaptation) adapters are applied <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. Instead of training all model parameters, only a small subset of adapter parameters are trained <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. These adapters are typically applied to the linear layers, such as QVO (query, value, output) and MLP (multi-layer perceptron) linear layers <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. This significantly saves memory and speeds up training <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. For a 1-billion parameter model, a LoRA alpha of 16 and rank of 32 are suggested <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. Only a small percentage (e.g., under 2%) of parameters become trainable with this method <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

### Training Configuration

The processed dataset is passed to a trainer <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. Key configurations include:
*   **Batch Size:** A virtual batch size of 8 or actual batch size of 2 can be used <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.
*   **Epochs:** Training for just one epoch can show significant effects <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.
*   **Warm-up Steps:** A small number of warm-up steps (e.g., 1-3) can be used to slowly increase the learning rate <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.
*   **Learning Rate:** A learning rate of 2e-4 is suitable for a 1-billion parameter model <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
*   **Optimizer:** AdamW 8-bit optimizer can reduce memory requirements <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
*   **Weight Decay:** Helps prevent overfitting <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>.
*   **Data Type:** Automatically set to float16 or brain float16 depending on the GPU <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.

During training, the loss typically decreases (e.g., from 6.34 to 3.7) <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>. Ideally, an evaluation dataset would be used to monitor evaluation loss and ensure it continues to fall <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

## Inference and Performance

Performance can be evaluated before and after fine-tuning.

### Zero-Shot Inference (Base Model)

Without any fine-tuning, the base model performs "zero-shot inference" <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. When given text, it generates audio in a random speaker's voice, as the temperature is non-zero <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>. This can result in a wide variance in speaker characteristics (e.g., male/female, deep/high-pitched voices) <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### [[voice_cloning_techniques | Voice Cloning]]

[[voice_cloning_techniques | Voice cloning]] is different from fine-tuning <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. With [[voice_cloning_techniques | voice cloning]], a sample audio of a desired voice is passed into the model, and the model then generates text-to-speech that sounds more like the provided sample <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>. While closer to the target voice than zero-shot inference, it's still not as accurate as fine-tuning <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

### Fine-Tuned Model Inference

After [[text_to_speech_model_fine_tuning | fine-tuning]], the model generates speech that sounds like the target voice from the training data <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. The randomness of voice characteristics is removed, and the model consistently produces a voice similar to the one it was fine-tuned on <a class="yt-timestamp" data-t="00:31:28">[00:31:28]</a>. Some remaining issues might include pacing or slight accent differences, which could be improved by better filtering of the original dataset <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.

The best performance is typically achieved when combining fine-tuning with [[voice_cloning_techniques | voice cloning]] <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>. This combination can yield "pretty good performance" even with a relatively small amount of data, such as a 30-minute video <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.

## Further Improvements and Considerations

*   **More Data:** For better performance, especially without [[voice_cloning_techniques | voice cloning]], creating a larger dataset (e.g., 500 rows of 30-second snippets) is recommended <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.
*   **Data Quality:** Improving [[data_preparation_for_text_to_speech | data preparation]] by ensuring snippets end on full stops or filtering out excessive pauses can enhance output quality <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   **Monitoring Training:** Using tools like TensorBoard to monitor evaluation loss and gradient norms can help optimize training and prevent overfitting <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
*   **Model Saving:** Fine-tuned models can be saved locally or pushed to model hubs like Hugging Face, either as lightweight LoRA adapters or as a merged, full model <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.