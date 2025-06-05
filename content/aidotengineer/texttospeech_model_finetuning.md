---
title: TexttoSpeech Model FineTuning
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

This article outlines a workshop on [[TexttoSpeech Model FineTuning | text-to-speech model fine-tuning]], specifically focusing on [[TokenBased TexttoSpeech Models | token-based text-to-speech models]] using Sesame's CSM 1B model <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The materials, including a Colab notebook and slides, are available on the Trellis Research GitHub repository under `AI Worldsfare-2025` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Workshop Objectives

By the end of this workshop, you should be able to:
*   Train a [[TexttoSpeech Model FineTuning | text-to-speech model]] to sound like a specific voice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   Understand how [[TokenBased TexttoSpeech Models | token-based text-to-speech models]] function <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The workshop focuses on Sesame CSM1B, but models like Orpheus from Canopy Labs are also token-based <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   Create a voice [[Data Preparation for TexttoSpeech Models | data set]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This can involve recording your own voice or extracting audio from a YouTube video <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   Perform [[Finetuning AI models for specific use cases | fine-tuning]] using Unsloth, a library based on transformers <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   Evaluate performance both before and after fine-tuning <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## How Token-Based Text-to-Speech Models Work

### Analogy to Language Models
[[Large language models and selfimprovement | Large language models]] like OpenAI's GPT-4o or Meta's Llama series take a string of text and predict the next word or token recursively <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. For [[TexttoSpeech Model FineTuning | text-to-speech]], the goal is to take a series of text tokens and predict the next audio token <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This involves passing a history of both text and audio to recursively decode the next audio token, producing a string of audio tokens that represent the desired speech <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Audio Tokens and Codebooks
The core challenge is representing continuous soundwaves as discrete audio tokens <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This is achieved by representing a piece of audio as a choice from a "codebook" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. A codebook functions like a dictionary, containing vectors where each vector represents a specific sound <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. These codebooks can be large to capture a wide variety of acoustics and semantics, allowing sound to be represented discretely, similar to how text represents meaning <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

Codebooks are trained using an encoder-decoder architecture <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. A soundwave is encoded into tokens, then decoded back into a wave <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. During training, the system compares the decoded output with the original input, using the difference (loss) to update the model's weights <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Hierarchical Representation
For effective sound representation, it's often insufficient to have just one token per time step <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. A hierarchical representation with multiple tokens allowed at the same timestamp or window provides a more detailed sound representation <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This approach uses multiple layers of tokens, capturing both higher-level meaning/acoustics and more granular details <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

### The Sesame Model Architecture
The Sesame model employs this hierarchical approach, using 32 tokens at each audio window to represent sound <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   A "zeroth token" is predicted by the main transformer <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   A secondary transformer decodes the remaining 31 "stack tokens" <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   Sesame therefore consists of two models: the main 1 billion parameter model and a much smaller model for decoding hierarchical tokens <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   The model also includes a codec to convert waveforms to tokens and vice-versa <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

## Fine-tuning Process Overview

The [[Finetuning AI models for specific use cases | fine-tuning]] process begins with a pre-trained model capable of taking text and audio inputs to output an audio stream <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The goal is to adapt this model to a specific voice by training it on a custom [[Data Preparation for TexttoSpeech Models | data set]] <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## Colab Notebook Setup and Data Generation

The entire process is covered in a single Colab notebook, available via the Trellis Research GitHub repo for AI Worlds Fair 2025 <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **GPU Connection:** Ensure your Colab runtime is connected to a GPU (e.g., T4), which should be available for free <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   The notebook has two main sections: [[Data Preparation for TexttoSpeech Models | Data Generation]] and Fine-tuning <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Data Generation Steps

1.  **Select YouTube Video:** Choose a YouTube video, preferably with a single speaker to avoid complex diarization (speaker separation), which is not supported in this basic notebook <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
2.  **Transcribe with Whisper:** Use OpenAI's Whisper model (e.g., "turbo" for speed and quality) within the Colab notebook to transcribe the audio <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. `YouTube DLP` and `Whisper` libraries need to be installed <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. The transcription is saved as a JSON file locally <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
3.  **Manual Correction:** Review the JSON transcript for misspelled words and perform find-and-replace operations (e.g., "trellis" with two 'l's to one 'l' for the company name) <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Re-upload the corrected file to Google Colab <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
4.  **Create Data Set Snippets:** Combine short Whisper segments into longer chunks, up to 30 seconds in length <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. A simple algorithm stacks segments until they exceed 30 seconds, forming a new data row <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   Roughly 50 clips of 30 seconds each are usually sufficient to have an effect on quality <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
    *   **Improvement Note:** Ideally, segments should end on a full stop (sentence boundary detection, e.g., using NLTK or regular expressions) to create more natural-sounding paragraphs within each data row <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
5.  **Push to Hugging Face:** The generated data set can be pushed to Hugging Face Hub <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
    *   When loading the data, it must have `audio` and `text` columns, and optionally a `source` column (for speaker ID, starting at zero) <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. If no speaker column is present, the code defaults to speaker zero <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## Model Loading and Initial Evaluation

### Installing Unsloth and Loading the Base Model
First, install Unsloth, which includes `transformers` and other necessary packages for loading and fine-tuning <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
Then, load the base CSM1B (Sesame) model using Unsloth <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   The model should fit easily within a 15GB T4 GPU as it's only a few gigabytes in size <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   Sesame models are now supported by `transformers` <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   The model architecture includes a backbone (main transformer), a depth decoder (for the 31 additional tokens), and a codec model <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

### Initial Inference (Before Fine-Tuning)
To evaluate the base model, perform zero-shot inference by passing text and observing the generated audio <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. With a non-zero temperature, the model will produce a random speaker's voice (male, female, deep, high-pitched) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Example Audio (Zero-Shot):** "We just finished fine-tuning a text to speech model." <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a> (Result: a woman's voice)
*   **Example Audio (Zero-Shot):** "Sesame is a super cool TTS model which can be fine-tuned with an SL." <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a> (Result: wide variance in speaker type)

### [[Voice Cloning and FineTuning Techniques | Voice Cloning]]
[[Voice Cloning and FineTuning Techniques | Voice cloning]] is distinct from [[Finetuning AI models for specific use cases | fine-tuning]] <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. In [[Voice Cloning and FineTuning Techniques | voice cloning]], a sample audio is passed into the model, influencing the generated output to sound more like the provided sample <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   The custom [[Data Preparation for TexttoSpeech Models | data set]] generated earlier is used for this purpose <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Example Audio (Cloned):** "Sesame is a super cool TTS model which can be fine-tuned with onslaught." <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a> (Result: closer to the speaker's voice, but still not as good as after fine-tuning)

## Fine-tuning with Unsloth

### Applying LoRA Adapters
[[Finetuning AI models for specific use cases | Fine-tuning]] is performed by applying LoRA (Low-Rank Adaptation) adapters <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. These adapters target specific layers (linear layers, QVO, MLP gate up and down) <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
*   **LoRA Alpha:** 16 (recommended for a 1 billion parameter model) <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   **Rescale LoRA:** Scales the learning rate of adapters based on their size <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.
*   **LoRA Rank:** 32 (determines the "width" or "height" of adapter matrices) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>.
*   Only a small subset of parameters (under 2%) are made trainable, which saves memory and speeds up training <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>, <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. Training embeddings is generally unnecessary if tokens aren't changing <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

### Data Preparation for Trainer
The loaded [[Data Preparation for TexttoSpeech Models | data set]] needs further formatting for the trainer <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.
*   Determine maximum audio length (e.g., 700,000 audio steps) <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.
*   Measure maximum text length (e.g., 587) <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>.
*   These lengths, along with a sampling rate, are passed into the trainer to prepare input IDs, attention masks, labels, and other tensors <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.

### Training Configuration
The processed data set is then passed to the trainer.
*   **Virtual Batch Size:** 8 (for 41 rows, this means 5 steps per epoch) <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.
*   **Epochs:** 1 epoch for this example <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.
*   **Warm-up Steps:** 3 (slowly increases the learning rate, though 1 might be more appropriate for very few steps) <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.
*   **Learning Rate:** 2e-4 (good for a 1 billion parameter model) <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
*   **Precision:** Automatically uses float16 or brain float16 based on the GPU (e.g., float16 on T4) <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.
*   **Optimizer:** AdamW 8-bit to reduce memory requirements <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
*   **Weight Decay:** Used to prevent overfitting <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>.
*   **Monitoring:** Ideally, use an evaluation [[Data Preparation for TexttoSpeech Models | data set]] to monitor evaluation loss and gradnorm (around 1 or less) using tools like TensorBoard <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

Training takes about 10 minutes <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>. The loss typically falls from around 6.34 to 3.7 <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.

## Post-Training Evaluation

### Saving the Model
After training, the model can be saved locally or pushed to Hugging Face Hub <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.
*   Pushing just the LoRA adapters is lightweight <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.
*   To push the full model, it needs to be merged first (e.g., to 16-bit format) <a class="yt-timestamp" data-t="00:29:59">[00:29:59]</a>.
*   A previously created fine-tuned model can be reloaded by specifying its name instead of the base model name <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.

### Fine-tuned Model Performance
After [[Finetuning AI models for specific use cases | fine-tuning]], new voice samples are generated using the adapted model.
*   **Example Audio (Fine-tuned, Zero-Shot):** "We just finished fine-tuning a text to speech model." <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a> (Result: male voice, sounds a little bit Irish, with some pacing issues)
*   **Example Audio (Fine-tuned, Zero-Shot):** "Sesame is a super cool TTS model which can be tuned on Slack." <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a> (Result: slight Irish accent, 'T' in 'tuned' still American, indicating room for improvement with more data)

### Fine-tuned Model with [[Voice Cloning and FineTuning Techniques | Voice Cloning]]
Combining [[Finetuning AI models for specific use cases | fine-tuning]] with [[Voice Cloning and FineTuning Techniques | voice cloning]] yields the best performance, even with a relatively small [[Data Preparation for TexttoSpeech Models | data set]] (e.g., a 30-minute video) <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.
*   **Example Audio (Fine-tuned + Cloned):** "Sesame is a super cool TTS model which can't be fine-tuned with onslaught." <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a> (Result: very good, strong Irish accent, even with natural-sounding errors, though intonation might not be perfect for every phrase)

## Conclusion

This workshop demonstrates that combining [[Finetuning AI models for specific use cases | fine-tuning]] with [[Voice Cloning and FineTuning Techniques | voice cloning]] can achieve good performance for [[TexttoSpeech Model FineTuning | text-to-speech models]] even with limited data <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>. For further improvements, aiming for around 500 rows of 30-second audio clips could significantly enhance performance, especially without [[Voice Cloning and FineTuning Techniques | voice cloning]] <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.

All resources are available on the Trellis Research GitHub: `trellis research/aiworldsfair 2025` <a class="yt-timestamp" data-t="00:33:28">[00:33:28]</a>. Future videos will cover more detailed [[Data Preparation for TexttoSpeech Models | data preparation]] and hyperparameter tuning <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.