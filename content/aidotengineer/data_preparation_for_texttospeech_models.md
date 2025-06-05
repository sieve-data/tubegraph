---
title: Data Preparation for TexttoSpeech Models
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

This article outlines the process of preparing data for [[texttospeech_model_finetuning | text-to-speech model fine-tuning]], specifically focusing on creating a voice dataset from a YouTube video to enable a model to sound like a specific voice <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. The process involves selecting source material, transcribing audio, manually correcting transcripts, and segmenting the data into a usable format.

## Workshop Context

The process detailed here is part of a workshop focused on [[texttospeech_model_finetuning | text-to-speech model fine-tuning]] of Sesame's CSM 1B model <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. All materials, including the Colab notebook and slides, are available on the Trellis Research GitHub under `AIWorldsfare-2025` <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Data Generation Process

The first section of the notebook covers data generation <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Selecting Source Material

The initial step is to select a YouTube video as the audio source <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
It is recommended to choose a video with a single speaker <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. While videos with multiple speakers can be used, they require additional data processing like diarization to split the audio, which is not covered in the basic notebook <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

### Transcription with Whisper

After selecting the video, the audio is transcribed using OpenAI's Whisper model within a Google Colab notebook <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, leveraging a GPU (CUDA) for processing <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Whisper Model Size**: The "turbo" transcription model is recommended for its balance of quality and speed, being almost as good as "large" but much faster than "small," "base," or "tiny" <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Tools**: `youtube-dlp` is used for downloading YouTube videos <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. It's advised to run this in Colab to avoid potential authentication issues when downloading from YouTube <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Output**: The transcription is saved to a local JSON file <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Manual Transcript Correction

Once the JSON transcription file is generated, it's crucial to review it for any misspellings or inaccuracies <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Users can perform a quick find-and-replace for common errors (e.g., correcting "Trellis" spelling) <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. After corrections, the updated JSON file should be re-uploaded to Google Colab to serve as the basis for the fine-tuning dataset <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### Creating the Dataset

The transcribed audio, originally in short segments from Whisper, is then combined into longer chunks for the dataset <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Segmentation**: The `simple` algorithm is used to stack segments until they reach a maximum length of about 30 seconds <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Each resulting chunk forms a row of data <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Dataset Structure**: The final dataset will consist of rows containing audio snippets (max 30 seconds) and their corresponding text transcriptions <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Hugging Face**: The prepared dataset can be pushed to Hugging Face <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Speaker ID**: The dataset requires an audio column and a text column, and optionally a source column referring to the speaker number (starting at zero) <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. If no speaker column is provided, a default speaker ID of zero is assigned <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

### Dataset Requirements and Best Practices

*   **Snippet Length**: Audio snippets up to 30 seconds are used <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Dataset Size**: A dataset of approximately 50 rows of 30-second snippets is generally sufficient to have a noticeable effect on the quality of the fine-tuned model <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. For better performance, especially without [[evaluation_of_voice_applications_including_audio_and_text | voice cloning]], aiming for 500 rows of 30-second snippets is recommended <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.
*   **Sentence Boundaries**: While the current implementation simply stacks segments, an opportunity for improvement is to end each row of data on a full stop. This can be achieved using libraries like NLTK to detect sentence boundaries or by using regular expressions <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Generally, having complete "paragraphs" within each data row is preferred <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   **Audio Quality**: Better filtering of the original data, such as removing segments with long pauses, can improve the pacing and overall quality of the generated voice <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>.

## Impact on Model Performance

The quality of the prepared dataset directly influences the [[texttospeech_model_finetuning | fine-tuning]] outcome. Even with a relatively small dataset (e.g., 30 minutes of video resulting in 41 clips) <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>, combining [[texttospeech_model_finetuning | fine-tuning]] with [[evaluation_of_voice_applications_including_audio_and_text | voice cloning]] can yield good performance <a class="yt-timestamp" data-t="00:33:15">[00:33:15]</a>. More data typically leads to better results, especially for zero-shot inference without voice cloning <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.