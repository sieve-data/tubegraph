---
title: Data preparation for text to speech
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

This workshop focuses on [[text_to_speech_model_fine_tuning | text to speech model fine-tuning]] for models like Sesame's CSM 1B. The process involves creating a voice dataset, which can be done by recording audio or by pulling audio from a YouTube video <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Overview of Data Preparation

The data preparation stage for fine-tuning a text-to-speech model includes several key steps:
1.  **Data Generation**: Selecting a YouTube video, transcribing it using Whisper, and converting it into a dataset <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
2.  **Transcription and Correction**: Transcribing the video and manually correcting any misspellings in the transcript <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
3.  **Dataset Creation**: Combining short segments from Whisper into longer chunks <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
4.  **Formatting for Training**: Preparing the processed dataset for the training phase <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.

## Acquiring Source Data

To begin, you select a YouTube video to use as the source for your voice dataset <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
It is recommended to choose a video with only one speaker, as videos with multiple speakers would require additional data processing like diarization to split the audio, which is not supported in a basic notebook setup <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The process for acquiring audio involves:
*   Using `yt-dlp` (YouTube-DLP) to download the audio from the selected YouTube video <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   Running this process within Google Colab is recommended to avoid authentication issues that might block downloads from YouTube when running outside Colab <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Transcribing Audio

Once the audio is acquired, it needs to be transcribed:
*   **Tool**: OpenAI's Whisper model is used for transcription <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Model Size**: The "turbo" Whisper model size is recommended for transcription, as it's almost as good as "large" but significantly faster <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Output**: The transcript is saved as a JSON file locally <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Refining Transcriptions

After initial transcription, manual correction is advised:
*   Review the JSON transcript file for any misspelled words or inaccuracies <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   Perform a find-and-replace operation for common issues, such as correcting specific spellings like "Trellis" (one L) from its common English spelling (two L's) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   Re-upload the corrected JSON file to Google Colab to ensure the refined transcript is used for fine-tuning <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

## Segmenting and Structuring the Dataset

Whisper typically provides short segments of transcription <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. For fine-tuning, these need to be combined into longer chunks:
*   **Goal**: Create rows of data with audio snippets up to 30 seconds in length, each paired with its transcription <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Algorithm**: A simple stacking algorithm is used to combine segments until they reach more than 30 seconds, then a new row of data is created <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Dataset Size**: Approximately 50 snippets of 30 seconds each is generally enough data to have an effect on the quality of the fine-tuning <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. A 30-minute video can provide a sufficient amount of data <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>.
*   **Improvements**: Data compilation could be improved by ending each row of data on a full stop, possibly using a library like NLTK or regular expressions to detect sentence boundaries <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This ensures more complete "paragraphs" within each data row <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   **Storage**: The generated dataset can be pushed to Hugging Face or saved locally <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Dataset Structure for Training

The prepared dataset must have specific columns for the trainer:
*   **Required Columns**: `audio` and `text` columns <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Optional Column**: A `source` column to refer to the speaker number (e.g., `0` for the first speaker, `1` for a different speaker) <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
*   **Default Speaker**: If no speaker column is present, the code assigns a default `source` of `0` to all entries <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## Preparing Data for Training

Before training, the data needs final formatting:
*   **Length Determination**: The maximum audio length (in audio steps/tokens) and maximum text length (in tokens) are measured from the dataset <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. For example, a maximum audio length of about 700,000 audio steps and a maximum text length of 587 tokens were observed in the workshop <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>, <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.
*   **Input Preparation**: Unsloth is used to prepare the input IDs, attention mask, labels, input values, and cutoffs, which are necessary inputs for the trainer <a class="yt-timestamp" data-t="00:24:59">[00:24:59]</a>.
*   This processed dataset is then passed to the trainer for fine-tuning the [[token_based_text_to_speech_models | token-based text-to-speech model]] <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>, <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.