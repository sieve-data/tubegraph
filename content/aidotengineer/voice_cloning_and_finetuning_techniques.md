---
title: Voice Cloning and FineTuning Techniques
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

This article explores the concepts of [[TexttoSpeech Model FineTuning | text-to-speech (TTS) model fine-tuning]] and voice cloning, focusing on techniques and practical applications. The goal of [[TexttoSpeech Model FineTuning | fine-tuning]] a TTS model is to make it sound like a specific voice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Understanding [[TokenBased TexttoSpeech Models | Token-Based Text-to-Speech Models]]

[[TokenBased TexttoSpeech Models | Token-based text-to-speech models]], such as Sesame CSM1B and Orpheus from Canopy Labs, function similarly to text models like GPT-4o or LLaMA <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a> <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. While text models predict the next word or token from a text string, TTS models aim to take a series of text tokens and predict the next audio token <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

Audio is represented discreetly by choosing from a "codebook," which acts like a dictionary where vectors represent specific sounds <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. These codebooks can be extensive to encompass a wide range of sounds, including acoustics and semantics <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Training these codebooks involves an encoder-decoder framework where a soundwave is converted into tokens and then decoded back into a wave. The system learns by minimizing the difference between the original input soundwave and the reconstructed output <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

A hierarchical representation, allowing multiple tokens per time step, generally works better for representing sound in [[TokenBased TexttoSpeech Models | token-based audio models]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The Sesame model, for instance, uses 32 tokens at every audio window to represent sound, with a main transformer predicting the zeroth token and a secondary transformer decoding the remaining 31 tokens <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a> <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The Sesame model consists of a 1 billion parameter main model and a smaller model for decoding hierarchical tokens <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Data Preparation for Fine-Tuning

To fine-tune a TTS model, a voice dataset is required <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This can be created by recording a voice or, as demonstrated, by extracting audio from a YouTube video <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

The process involves:
1.  **Selecting Audio Source:** Choosing a YouTube video, ideally with a single speaker to simplify data processing <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
2.  **Transcription:** Using [[Speech recognition technology and applications | Whisper]] (e.g., "turbo" model for efficiency) to transcribe the audio into text <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a> <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This typically saves as a JSON file <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
3.  **Manual Correction:** Reviewing and correcting any misspelled words or inaccuracies in the transcribed text <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
4.  **Segmenting Data:** Combining short segments from the [[Speech recognition technology and applications | Whisper]] transcription into longer chunks, typically up to 30 seconds in length, to form rows of data <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a> <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. Approximately 50 such 30-second snippets are generally sufficient to have an effect on quality <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
5.  **Dataset Structure:** The final dataset should have an audio column and a text column, and optionally a source column for speaker ID (e.g., 0 for a single speaker) <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

## Fine-Tuning Process

[[TexttoSpeech Model FineTuning | Fine-tuning]] is performed using Unsloth, a library built on Hugging Face Transformers <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a> <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

The steps include:
1.  **Model Loading:** Loading the base model (e.g., CSM1B) with a specified maximum sequence length <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. The model typically loads into the GPU <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
2.  **Adapter Application:** Applying LoRA (Low-Rank Adaptation) adapters to specific layers of the model, such as linear layers (QVO, gate up and down layers) <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a> <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>. This approach trains only a subset of parameters, saving memory and speeding up training <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a> <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. For a 1 billion parameter model, a LoRA alpha of 16 and a rank of 32 are recommended <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a> <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>.
3.  **Data Processing:** Preparing the loaded dataset for the trainer by setting parameters like sampling rate, maximum text length, and maximum audio length <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a> <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
4.  **Training Configuration:** Setting up the training parameters, including virtual batch size (e.g., 8), number of epochs (e.g., 1), warm-up steps, and learning rate (e.g., 2e-4 for a 1 billion parameter model) <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a> <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a> <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a> <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>. AdamW 8-bit optimizer can be used to reduce memory <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
5.  **Execution:** Running the training process, which typically takes around 10 minutes and shows a decrease in loss <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a> <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. Ideally, an evaluation dataset is used to monitor loss and prevent overfitting <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

## Voice Cloning

Voice cloning involves passing an audio sample to the model, prompting it to generate new audio that sounds similar to the provided sample <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a> <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This differs from zero-shot inference, where the model generates a random speaker's voice based on temperature settings <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a> <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. While voice cloning provides a voice closer to the target, it is not as accurate as fine-tuning <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

## Performance Evaluation

Performance is evaluated by generating audio samples before and after [[TexttoSpeech Model FineTuning | fine-tuning]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Zero-shot inference:** Produces unpredictable voices (male, female, deep, high-pitched) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a> <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   **Voice cloning (base model):** Produces a voice closer to the input sample but still shows variance and may not fully capture the speaker's nuances <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.
*   **Fine-tuned model (zero-shot):** Removes the randomness of the voice, typically sounding like the target speaker's gender, but may still have issues with pacing or accent <a class="yt-timestamp" data-t="00:31:23">[00:31:23]</a> <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>.
*   **Fine-tuned model with cloning:** Expected to yield the best results, combining the benefits of specific voice training with cloning for nuanced output <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a> <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.

Even with a relatively small amount of data (e.g., a 30-minute video yielding 41 clips of up to 30 seconds each), combining fine-tuning with cloning can achieve good performance <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a> <a class="yt-timestamp" data-t="00:33:15">[00:33:15]</a> <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>. For even better performance, especially without voice cloning, aiming for around 500 rows of 30-second audio clips is recommended <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>. Further improvements could involve better filtering of the original dataset to avoid long pauses or by using libraries like NLTK to detect sentence boundaries for cleaner data segmentation <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a> <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.