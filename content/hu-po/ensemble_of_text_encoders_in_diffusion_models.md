---
title: Ensemble of text encoders in diffusion models
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Diffusion models leverage pre-trained models to derive suitable representations from text conditioning, which is the prompt typed by a user to generate an image <a class="yt-timestamp" data-t="00:54:48">[00:54:48]</a>. The quality of the text encoder is crucial for the final generated image quality <a class="yt-timestamp" data-t="01:35:33">[01:35:33]</a>.

## Utilizing Multiple Text Encoders

In [[diffusion_models_and_transformers | diffusion models]], ensembles of models generally outperform single models, especially when trained with slightly different objectives on varied datasets <a class="yt-timestamp" data-t="01:35:55">[01:35:55]</a>. However, using an ensemble is more computationally expensive and demands more memory <a class="yt-timestamp" data-t="01:36:28">[01:36:28]</a>.

To achieve the best possible results, the model in question utilizes an ensemble of three text encoders during training <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>:
*   Clip G14 <a class="yt-timestamp" data-t="00:55:11">[00:55:11]</a>, specifically Open Clip G14 <a class="yt-timestamp" data-t="00:55:32">[00:55:32]</a>.
*   Clip L14 <a class="yt-timestamp" data-t="00:55:11">[00:55:11]</a>, specifically Clip L14 <a class="yt-timestamp" data-t="00:55:32">[00:55:32]</a>.
*   T5 XXL <a class="yt-timestamp" data-t="00:55:11">[00:55:11]</a>, which is the T5 1.1 XXL text encoder from Google <a class="yt-timestamp" data-t="00:55:40">[00:55:40]</a>, <a class="yt-timestamp" data-t="00:55:43">[00:55:43]</a>.

These three encoders are trained with an individual dropout rate of 46% <a class="yt-timestamp" data-t="01:37:51">[01:37:51]</a>. This high dropout rate during training makes the model robust <a class="yt-timestamp" data-t="01:38:23">[01:38:23]</a>, allowing an arbitrary subset of the encoders to be used during inference <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>. This is particularly relevant for memory efficiency, especially considering the T5 XL encoder alone has 4.7 billion parameters <a class="yt-timestamp" data-t="01:39:27">[01:39:27]</a>.

## Impact of Text Encoders

Removing the T5 encoder has minimal impact on aesthetic quality ratings but significantly affects the model's ability to generate correctly spelled text <a class="yt-timestamp" data-t="01:40:01">[01:40:01]</a>, <a class="yt-timestamp" data-t="01:40:59">[01:40:59]</a>. For instance, without T5, the model may misspell words like "Transformer" <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>.

The Clip text encoders are trained through a contrastive learning process, aiming to make images and text share the same embedding space <a class="yt-timestamp" data-t="01:41:08">[01:41:08]</a>. This makes them good at capturing semantic knowledge between images and text <a class="yt-timestamp" data-t="01:41:32">[01:41:32]</a>. In contrast, T5, trained with a different objective, provides a distinct type of text encoding <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>. This is similar to using ensembles of [[the_role_of_variational_autoencoders_in_latent_diffusion | DINO features]] and Clip features, where the visual features from different training methods offer different strengths <a class="yt-timestamp" data-t="01:41:57">[01:41:57]</a>.

This diversity means that different text encoders have slightly different strengths and weaknesses, and their combination yields a greater benefit <a class="yt-timestamp" data-t="01:42:10">[01:42:10]</a>. For example, the T5 text encoder can provide a more nuanced understanding of spatial relationships described by words like "into," ensuring objects are precisely positioned as described in the prompt <a class="yt-timestamp" data-t="01:42:58">[01:42:58]</a>, <a class="yt-timestamp" data-t="01:43:03">[01:43:03]</a>.

### Pre-computing Embeddings

To optimize training speed, all captions in the dataset are pre-encoded using these text encoders before training begins <a class="yt-timestamp" data-t="02:03:56">[02:03:56]</a>. This allows the model to sample already encoded text for mini-batches, avoiding the need for on-the-fly text encoding during training <a class="yt-timestamp" data-t="02:04:28">[02:04:28]</a>.