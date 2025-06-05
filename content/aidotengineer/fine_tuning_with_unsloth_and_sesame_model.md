---
title: Fine tuning with Unsloth and sesame model
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

This article provides an overview of [[text_to_speech_model_fine_tuning | fine-tuning text-to-speech (TTS) models]], specifically focusing on the Sesame CSM1B model using the Unsloth library <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The objective is to train a TTS model to sound like a specific voice <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, understand token-based TTS models <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, create voice datasets <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, perform [[finetuning_ai_models_for_better_performance | fine-tuning]] with Unsloth <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>, and [[evaluating_language_model_performance | evaluate performance]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. All workshop materials, including the Colab notebook and slides, are available on the Trellis Research GitHub under `AI Worldsfare-2025` <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Understanding Token-Based Text-to-Speech Models

Token-based TTS models function similarly to token-based text models like GPT-4o or Llama series <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. While text models predict the next word or token from an input string of text <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, TTS models take a series of text tokens and predict the next *audio token* <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. They can also incorporate a history of text and audio from previous conversation to recursively produce the next audio token <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

The core challenge is representing continuous audio waveforms as discrete tokens <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This is achieved by representing a small piece of audio as a choice from a "code book" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. A code book acts like a dictionary containing vectors, where each vector represents a specific sound <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

To train these code books, an encoder-decoder architecture is used <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. A soundwave is encoded into tokens, then decoded back into a wave <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. The difference between the input and output waves (loss) is used to update the model's weights <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

A single token per time step is often insufficient for detailed audio representation <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Therefore, token-based audio models typically use a hierarchical representation or multiple tokens per time window <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This allows for representing both higher-level meaning/acoustics and more granular details <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Sesame CSM1B Model Architecture

The Sesame model, specifically CSM1B, uses 32 tokens at every audio window to represent sound <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   A "zeroth" token is predicted by the main transformer <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   A secondary transformer decodes the other 31 "stack" tokens <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   The Sesame model consists of two parts: the main 1-billion parameter model and a much smaller model for decoding hierarchical tokens <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

The architecture includes:
*   A backbone model (the main transformer) <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
*   A depth decoder for the 31 additional tokens <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   A codec model to convert between waveform and tokens <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

## Data Preparation for Fine-tuning

The first step in [[finetuning_ai_models_for_better_performance | fine-tuning]] is data generation <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
1.  **Select a YouTube video:** Choose a video with a single speaker to avoid complex diarization <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
2.  **Transcribe with Whisper:** Use OpenAI's Whisper model (e.g., `turbo` size for speed and quality) within the Colab Notebook to transcribe the video <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. The transcription is saved as a JSON file <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
    > [!info] Colab Recommendation
    > Running YouTube downloads and Whisper transcription is recommended within Google Colab to avoid authentication issues <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
3.  **Correct Transcription:** Manually review the JSON transcript for misspellings (e.g., proper nouns like "Trellis" with one 'L' vs. two 'L's) and perform find-and-replace operations <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Re-upload the corrected file to Colab <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
4.  **Segment and Combine Audio:** Split the long transcript into shorter segments, combining them into chunks of up to 30 seconds <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. The `simple` algorithm stacks Whisper segments until they exceed 30 seconds, forming a new data row <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
    *   A typical dataset size of about 41 rows of 30-second clips can have an effect on quality <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Around 50 rows of 30-second snippets is a good starting point <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. For better performance, particularly without voice cloning, aim for around 500 rows of 30-second clips <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.
    > [!tip] Data Improvement
    > Consider ending each row of data on a full stop by using libraries like NLTK or regular expressions to detect sentence boundaries <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
5.  **Push to Hugging Face (Optional):** The processed dataset can be pushed to Hugging Face Hub <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
6.  **Load Raw Data Set:** The dataset needs to have an `audio` column and a `text` column <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. An optional `source` column refers to the speaker ID, starting at zero <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. If not provided, a default `source` of zero is assigned <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
7.  **Format Data for Trainer:** Determine the maximum audio and text lengths from the dataset <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>. Unsloth prepares the input IDs, attention masks, labels, input values, and cutoffs <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. This mapping is applied to create a processed dataset <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.

## Fine-tuning with Unsloth

Unsloth is a library built around Hugging Face Transformers <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a> that simplifies [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

1.  **Install Unsloth:** Install Unsloth, which includes transformers and other necessary packages <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
2.  **Load Base Model:** Load the Sesame CSM1B model using Unsloth <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. It's a 1-billion parameter model and fits within a T4 GPU's 15GB memory <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. The model supports auto-model for conditional generation <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
    > [!info] GPU Requirement
    > A GPU (e.g., T4 on Colab) is required <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
3.  **Apply LoRA Adapters:** Instead of training all model parameters, LoRA (Low-Rank Adaptation) adapters are applied to a subset of layers (e.g., linear layers, QVO, MLP linear layers) <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. This saves memory and speeds up training <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
    *   `lora_alpha` can be set to 16 for 1-billion parameter models <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
    *   `rescale_lora` scales the learning rate based on adapter size <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.
    *   `rank` of 32 can be used for adapter matrices <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>.
    *   Typically, less than 2% of parameters are trainable with this approach <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
    *   Training embeddings (e.g., `LM head`, `lm_embed`, `embed_tokens`) is generally not necessary unless token changes are involved <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

### Trainer Configuration

The processed dataset is passed to the trainer <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. Key configurations include:
*   **Virtual batch size:** For a T4, a virtual batch size of 8 or more can be used <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>. A batch size of 4 might be possible on a T4 <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.
*   **Epochs:** Even one epoch can yield results <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.
*   **Warm-up steps:** Controls how slowly the learning rate increases <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>. For small datasets (e.g., 5 total steps), reducing warm-up steps to one can be beneficial <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.
*   **Learning rate:** 2e-4 is typically suitable for a 1-billion parameter model <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
*   **Data type:** Automatically selected (e.g., `float16` on T4, `bfloat16` on Hopper/Blackwell/Ampere GPUs) <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.
*   **Optimizer:** AdamW 8-bit optimizer reduces memory requirements <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
*   **Weight decay:** Prevents overfitting <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>.
*   **Learning rate scheduler:** Constant learning rate can be used <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.
*   **Output directory:** Specifies where model outputs are saved <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.

Training can take about 10 minutes <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. The loss should decrease significantly (e.g., from ~6.34 to ~3.7) <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.
> [!caution] Evaluation Data
> Ideally, the training set should be split into `train` and `eval` sets to monitor `eval_loss` and `grad_norm` (should be around 1 or less) using tools like TensorBoard <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

## Performance Evaluation

### Zero-Shot Inference
Without [[finetuning_ai_models_for_better_performance | fine-tuning]] or voice cloning, the base model generates speech with a random speaker's voice due to non-zero temperature <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. This can result in a wide variance of voices (e.g., male, female, deep, high-pitched) <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

### Voice Cloning
Voice cloning involves passing an audio sample to the model, which then attempts to generate new text in a voice similar to the sample <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This yields a voice much closer to the sample than zero-shot inference, but still not as accurate as after [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

### Fine-tuned Model Performance
After [[finetuning_ai_models_for_better_performance | fine-tuning]], the model's output will have a consistent male voice (if trained on a male voice) <a class="yt-timestamp" data-t="00:31:25">[00:31:25]</a>. While improved, issues like pacing or subtle accent characteristics might still be present, indicating potential for further data filtering or more data <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.

### Fine-tuning combined with Voice Cloning
The best performance is typically achieved by combining [[finetuning_ai_models_for_better_performance | fine-tuning]] with voice cloning <a class="yt-timestamp" data-t="00:32:14">[00:32:14]</a>. This can produce very high-quality speech that closely matches the target voice, even with a relatively small amount of data (e.g., 30 minutes of video) <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.

## Saving and Pushing Models

After training, the model can be saved locally or pushed to Hugging Face Hub <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.
*   **Saving LoRA Adapters:** Saving the LoRA adapters is lightweight and creates a smaller repository <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.
*   **Merging and Saving Full Model:** To push the full, merged model, it needs to be merged into a 16-bit format first <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. This saves both the model and processor <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>.
*   **Reloading a Fine-tuned Model:** To reload a previously fine-tuned model, specify its name (e.g., `trellis/my-YouTube-tts`) instead of the base model name <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.