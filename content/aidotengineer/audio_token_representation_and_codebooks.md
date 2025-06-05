---
title: Audio Token Representation and Codebooks
videoId: CXsbjcrf_5g
---

From: [[aidotengineer]] <br/> 

## Introduction
In the context of [[tokenbased_texttospeech_models | token-based text-to-speech models]], the goal is to convert text into audio by predicting audio tokens. This process is analogous to how models like GPT-4o predict the [[next_token_prediction_in_ai | next word or token]] in a text string <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For text-to-speech, the model takes a series of text tokens and aims to predict the [[next_token_prediction_in_ai | next audio token]] recursively <a class="yt:timestamp" data-t="00:02:10">[00:02:10]</a>.

## What are Audio Tokens?
The fundamental question for this process is: "How do you make tokens for audio?" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Unlike continuous soundwaves, audio tokens must be discrete representations. A small segment of audio can be represented as a choice from a "codebook" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Codebooks
A codebook functions like a dictionary, containing a series of vectors, where each vector represents a specific sound <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. These codebooks can be quite large to encompass a wide range of sounds, including both acoustics and semantics <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This approach allows sound to be represented discretely, similar to how text discretely represents meaning <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Training Codebooks
Codebooks are typically trained using an encoder-decoder architecture <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>:
1.  A soundwave is input and converted into tokens by an encoder <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  Another transformer then decodes these tokens back into a soundwave <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
3.  During training, the system evaluates how closely the decoded output wave matches the original input wave <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  Any discrepancies (loss) are used to adjust the model's weights through backpropagation <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

With sufficient data, this process enables the training of a codebook that can represent sound in a discrete form <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Hierarchical Representation
It has been found that using only one token per time step is insufficient to fully represent sound <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. A more effective approach, used in most [[tokenbased_texttospeech_models | token-based audio models]], involves a hierarchical representation or multiple tokens per time window <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This allows for a more detailed representation, including higher-level meaning or acoustics, and then more granular layers of representation <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Sesame Model Implementation
The Sesame model employs this approach by using 32 tokens at every audio window to represent sound <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   A "zeroth" token is predicted by the main transformer <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   A secondary transformer decodes the other 31 tokens, which capture additional meaning or detail <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

The Sesame model itself consists of two parts: a main 1 billion parameter model and a much smaller model that decodes these hierarchical tokens <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. The architecture includes a backbone model (the main transformer), a depth decoder for the additional tokens, and a codec model to convert between waveforms and tokens <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.