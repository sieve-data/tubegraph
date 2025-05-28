---
title: JPEG encoding and generation with language models
videoId: SkvyrgSzigo
---

From: [[hu-po]] <br/> 

The `jpeg LM` [[jpeg_lm_llms_as_image_generators_on_canonical_codec_representations | jpeg LM]] paper, released on August 15, 2024, by the University of Washington and Meta's research lab (Fair), explores a novel approach to image and video generation using [[large_language_models_and_their_applications | large language models]] (LLMs) <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Core Concept
The central idea of [[jpeg_lm_llms_as_image_generators_on_canonical_codec_representations | jpeg LM]] is to directly model images and videos as compressed files saved on a computer via canonical codecs <a class="yt-timestamp" data-t="01:00:44">[01:00:44]</a>. For images, JPEG is used, and for videos, AVC h264 <a class="yt-timestamp" data-t="01:13:54">[01:13:54]</a>. Instead of generating images in pixel space or a latent space of shapes, the LLM literally generates the sequence of tokens that represent the image when it is encoded in a format like JPEG <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>.

This approach is considered counter-intuitive and was largely unexplored prior to this work, described as an "approach almost void of prior work" due to many assumed challenges, or even a "stupid idea that works" <a class="yt-timestamp" data-t="01:14:08">[01:14:08]</a>.

## Architecture and Training
The [[jpeg_lm_llms_as_image_generators_on_canonical_codec_representations | jpeg LM]] model utilizes conventional LLM architectures (autor regressive Transformers) without any vision-specific modifications, such as convolutions or 2D positional embeddings <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>. This design choice aims to maximize the model's generality <a class="yt-timestamp" data-t="01:08:07">[01:08:07]</a>.

The model was pre-trained from scratch using a 7B Llama 2 model <a class="yt-timestamp" data-t="01:09:06">[01:09:06]</a>. The training dataset consisted of 23 million 256x256 images <a class="yt-timestamp" data-t="01:09:12">[01:09:12]</a>. Each image was JPEG encoded with a quality factor of 25 <a class="yt-timestamp" data-t="01:09:16">[01:09:16]</a> and translated into approximately 5,000 tokens <a class="yt-timestamp" data-t="01:09:30">[01:09:30]</a>. For video generation, the model handled sequences of 15 frames <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>. The vocabulary used for the JPEG tokens was 256 discrete values, along with special beginning and end of sequence tokens <a class="yt-timestamp" data-t="01:07:16">[01:07:16]</a>.

## Comparison with VQ-VAE
The paper directly compares its approach to [[vqvae | Vector Quantized Variational Autoencoders]] (VQ-VAE), a common method for image tokenization in generative models <a class="yt-timestamp" data-t="01:06:26">[01:06:26]</a>.

### VQ-VAE Mechanics
A [[vqvae | VQ-VAE]] operates as a two-stage process: tokenizer training and language model training <a class="yt-timestamp" data-t="00:45:02">[00:45:02]</a>. It discretizes continuous images into a learned vocabulary of tokens <a class="yt-timestamp" data-t="00:45:02">[00:45:02]</a>. An encoder maps an image to a spatial feature, which is then quantized by finding the nearest neighbor in a learned codebook (vocabulary) <a class="yt-timestamp" data-t="00:47:57">[00:47:57]</a>. A decoder then reconstructs the image from these quantized tokens <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>. This process is lossy, meaning information is lost during compression <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>.

### Encoding Differences
Both JPEG and [[vqvae | VQ-VAE]] are lossy compression methods <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>. However, the type of information loss differs:
*   **JPEG Encoding:** This is a hand-designed compression method <a class="yt-timestamp" data-t="01:11:29">[01:11:29]</a>. It prioritizes details like small human faces and text characters, making it significantly better at preserving these elements compared to VQ <a class="yt-timestamp" data-t="01:12:15">[01:12:15]</a>.
*   **VQ-VAE Encoding:** While it may preserve color and sharpness better in some areas, it often loses more detail in highly perceptible elements like faces <a class="yt-timestamp" data-t="01:12:18">[01:12:18]</a>.

Despite its simplicity, [[jpeg_lm_llms_as_image_generators_on_canonical_codec_representations | jpeg LM]] consistently outperforms the [[vqvae | VQ]] Transformer in evaluations, demonstrating the viability of this novel approach <a class="yt-timestamp" data-t="01:13:40">[01:13:40]</a>.

## Implications
The [[jpeg_lm_llms_as_image_generators_on_canonical_codec_representations | jpeg LM]] paper suggests a unification of the paradigms in language generation and visual generation <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>. By directly generating the byte-level representation of compressed files, the model avoids the need for complex, vision-specific architectures or learned tokenization schemes (like VQ-VAE) <a class="yt-timestamp" data-t="01:15:40">[01:15:40]</a>. This opens doors for [[large_language_models_and_their_applications | LLMs]] to generate diverse data types (images, videos, and potentially even 3D models like STL files) by simply learning to output their canonical encoded forms <a class="yt-timestamp" data-t="01:12:52">[01:12:52]</a>. The fact that a relatively small 7B Llama 2 model trained from scratch on a limited dataset can achieve this is considered impressive <a class="yt-timestamp" data-t="01:21:49">[01:21:49]</a>.