---
title: Text to speech model fine tuning
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

This article summarizes a workshop on [[Text to speech model fine tuning | text-to-speech (TTS) model fine-tuning]], focusing on the Sesame CSM 1B model. The aim is to train a TTS model to replicate a specific voice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. All workshop materials, including the Colab notebook and slides, are available on the Trellis Research GitHub under `AI Worldsfare-2025` <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## How [[token_based_text_to_speech_models | Token-Based Text to Speech Models]] Work

[[token_based_text_to_speech_models | Token-based text-to-speech models]] function similarly to large language models like GPT-4o or Llama, which predict the next word or token in a text string <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. For TTS, the goal is to take a series of text tokens and predict the next "audio token" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The model can also take a history of text and audio from a conversation to recursively decode the next audio token <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

The core challenge is how to represent continuous audio waveforms as discrete tokens <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This is achieved by representing a piece of audio as a choice from a "codebook," which is a dictionary of vectors representing specific sounds <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. These codebooks can be large to capture a wide variety of acoustics and semantics <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

Codebooks are trained using an encoder-decoder structure: a soundwave is encoded into tokens, then decoded back into a wave, and the difference between the input and output (loss) is used to update weights <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. For better representation, a hierarchical approach or multiple tokens per time step (window) is used, allowing for more detailed and layered sound representation <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

The Sesame model, specifically CSM1B, uses 32 tokens at every window to represent sound <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. A primary transformer predicts the zeroth token, while a secondary transformer decodes the remaining 31 tokens <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Thus, Sesame comprises two models: a main 1 billion parameter model and a smaller model for hierarchical token decoding <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Workshop Process

The workshop demonstrates [[finetuning_ai_models_for_better_performance | fine-tuning]] a pre-trained Sesame model using a custom dataset <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. The process involves:
1.  **[[data_preparation_for_text_to_speech | Data Generation]]**: Creating a voice dataset from a YouTube video <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  **[[fine_tuning_with_unsloth_and_sesame_model | Fine-tuning]]**: Utilizing [[fine_tuning_with_unsloth_and_sesame_model | Unsloth]], a library based on transformers, to [[finetuning_ai_models_for_better_performance | fine-tune]] the model <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
3.  **[[evaluating_language_model_performance | Performance Evaluation]]**: Assessing the model's performance both before and after [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### [[data_preparation_for_text_to_speech | Data Generation]]

The [[data_preparation_for_text_to_speech | data generation]] section of the Colab notebook guides users to:
*   **Select a YouTube video**: It is recommended to choose a video with a single speaker to avoid complex diarization <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Transcribe audio**: Whisper (OpenAI) is used within the Colab environment to transcribe the audio, with "turbo" transcription recommended for its balance of quality and speed <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Correct transcripts**: Users can manually review and correct misspelled words in the generated JSON transcript file <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Create the dataset**: The long transcript is split into shorter segments, combined into chunks of up to 30 seconds, forming rows of data with audio snippets and their corresponding text <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. A dataset of approximately 50 rows of 30-second snippets is suggested for a noticeable effect <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Push to Hugging Face (optional)**: The created dataset can be pushed to Hugging Face Hub <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   **Dataset structure**: The dataset requires an `audio` column and a `text` column, with an optional `source` column for speaker ID (defaulting to zero for single speakers) <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Future improvements**: Compiling segments to end on full stops using libraries like NLTK or regular expressions could improve data quality <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

### [[fine_tuning_with_unsloth_and_sesame_model | Fine-Tuning]]

The [[fine_tuning_with_unsloth_and_sesame_model | fine-tuning]] process involves:
*   **Installing Unsloth**: A library that includes transformers and packages for loading and [[finetuning_ai_models_for_better_performance | fine-tuning]] models <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **Loading the base model**: The CSM1B Sesame model is loaded. It's a few gigabytes in size and fits easily on a T4 GPU (15GB memory) <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. The model architecture includes a backbone transformer, a depth decoder, and a codec model <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
*   **Applying LoRA adapters**: Instead of training all parameters, small adapters are applied to target specific layers like linear layers (QVO, MLP linear layers) <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. This saves memory and accelerates training <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
    *   A LoRA alpha of 16 is recommended for 1 billion parameter models, and a rank of 32 for adapter matrices <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
    *   Only about 2% of the model parameters are trainable with this approach <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.
*   **Data preparation for trainer**: The maximum audio and text lengths from the dataset are determined and passed to the trainer <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. Unsloth handles the preparation of input IDs, attention masks, labels, etc. <a class="yt-timestamp" data-t="00:24:59">[00:24:59]</a>.
*   **Training parameters**:
    *   Virtual batch size of 8 (with 41 rows, leading to 5 steps per epoch) <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.
    *   One epoch of training <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.
    *   Warm-up steps for slow learning rate increase <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.
    *   Learning rate of 2E-4 is suitable for a 1 billion parameter model <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
    *   AdamW 8-bit optimizer for memory reduction <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
    *   Weight decay helps prevent overfitting <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>.
    *   Training loss is expected to decrease from around 6.34 to 3.7 <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.
*   **Monitoring training**: Ideally, an evaluation dataset would be used to monitor eval loss and stop training if it ceases to fall <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>. TensorBoard can be used to monitor losses and `grad_norm` <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.

### [[evaluating_language_model_performance | Performance Evaluation]]

Model performance is evaluated through inference, comparing results before and after [[finetuning_ai_models_for_better_performance | fine-tuning]]:

*   **Zero-shot inference (before [[finetuning_ai_models_for_better_performance | fine-tuning]])**:
    *   The model generates audio with a random speaker voice (male or female, deep or high-pitched) due to a non-zero temperature <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.
    *   Example: A woman's voice for the text "We just finished fine-tuning a text to speech model" <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
    *   Example: A different voice for "Sesame is a super cool TTS model which can be fine-tuned with Unsloth" <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   **Voice cloning (before [[finetuning_ai_models_for_better_performance | fine-tuning]])**:
    *   A sample of the target voice is passed to the model, which then generates text that sounds more like the input sample <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This provides a closer match to the target voice than zero-shot inference <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.
    *   Example: A voice closer to the speaker's original voice, but still not as good as after [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.
*   **[[customization_and_personalization_in_speech_ai | Fine-tuned]] model inference**:
    *   **Zero-shot inference**: After [[finetuning_ai_models_for_better_performance | fine-tuning]], the model generates a male voice, closer to the speaker, but with some pacing issues or a slight Irish accent <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>.
    *   **Voice cloning with [[finetuning_ai_models_for_better_performance | fine-tuning]]**: Combining [[finetuning_ai_models_for_better_performance | fine-tuning]] with voice cloning yields the best performance, producing audio that closely matches the speaker's voice, including their accent <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>.
    *   Example: "Sesame is a super cool TTS model which can be fine-tuned with Unsloth," generated with a natural-sounding Irish accent <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.

## Conclusion

The workshop demonstrates that even a relatively small amount of data (e.g., 30 minutes of video for 41 rows) can yield good performance when combining [[finetuning_ai_models_for_better_performance | fine-tuning]] with voice cloning <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>. For even better performance, especially without voice cloning, aiming for around 500 rows of 30-second data is suggested <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.

The fine-tuned model (LoRA adapters) can be saved locally or pushed to Hugging Face Hub, either as lightweight adapters or merged into a full 16-bit model <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. To reload a previously fine-tuned model, its name would be specified instead of the base model name <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.