---
title: Challenges and Advances in Image Tokenization
videoId: -jG7S5g071Q
---

From: [[hu-po]] <br/> 

Image tokenization is a crucial step in enabling machine learning models, particularly [[challenges_and_insights_in_transformer_architecture_and_training | Transformer]]s, to process and generate images. This process involves converting continuous image data into discrete tokens, similar to how words are processed in language models <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>.

## Traditional Approach: Raster Scan Ordering

Historically, image tokenization has involved discretizing continuous images into a grid of two-dimensional tokens <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>. These 2D grids are then flattened into a one-dimensional sequence for autoregressive learning, mirroring the process of sequential language modeling <a class="yt-timestamp" data-t="01:15:12">[01:15:12]</a>.

A common method for this flattening is the "patching" technique, where an image is divided into smaller patches <a class="yt-timestamp" data-t="01:15:32">[01:15:32]</a>. These patches are then ordered into a one-dimensional sequence, typically using a row-major raster scan (left to right, top to down) <a class="yt-timestamp" data-t="01:15:39">[01:15:39]</a>, <a class="yt-timestamp" data-t="01:15:40">[01:15:40]</a>. While other scan orders like spiral or Z-curve have been explored, the raster scan remains the most popular <a class="yt-timestamp" data-t="01:15:41">[01:15:41]</a>, <a class="yt-timestamp" data-t="01:42:07">[01:42:07]</a>.

## Challenges with Traditional Tokenization

The traditional raster scan approach presents several [[challenges_in_visual_segmentation_and_encoding | challenges in visual segmentation and encoding]]:
*   **Incorrect Inductive Prior** <a class="yt-timestamp" data-t="01:16:13">[01:16:13]</a>: Unlike language, which has an inherent one-dimensional flow, images possess complex two-dimensional spatial relationships. Forcing a one-dimensional order (like left to right, top to down) introduces an unnatural inductive prior that doesn't align with how image data is structured <a class="yt-timestamp" data-t="01:16:15">[01:16:15]</a>, <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>.
*   **Loss of Spatial Locality** <a class="yt-timestamp" data-t="01:16:20">[01:16:20]</a>: Flattening the 2D grid into a 1D sequence disrupts the inherent spatial locality of image features. Tokens that are close neighbors in the original image might become distant in the linear sequence, weakening their correlations under unidirectional constraints <a class="yt-timestamp" data-t="01:16:23">[01:16:23]</a>.
*   **Reliance on Position Embeddings** <a class="yt-timestamp" data-t="01:16:36">[01:16:36]</a>: To compensate for the lost spatial information, models processing flattened image sequences often rely on [[challenges_and_insights_in_transformer_architecture_and_training | position embeddings]] (e.g., Rotary Position Embeddings) to remind the network of the relative positions of tokens <a class="yt-timestamp" data-t="01:16:42">[01:16:42]</a>.
*   **Restricted Generalizability** <a class="yt-timestamp" data-t="01:17:27">[01:17:27]</a>: The unidirectional nature of raster scan limits the model's ability for bidirectional reasoning, making tasks like predicting the top part of an image given the bottom part difficult <a class="yt-timestamp" data-t="01:17:30">[01:17:30]</a>.

## VQ-VAE for Image Tokenization

A common tool for image tokenization is the Vector Quantized Variational AutoEncoder (VQ-VAE). This self-supervised learning strategy involves:
1.  **Encoder (E)** <a class="yt-timestamp" data-t="01:34:26">[01:34:26]</a>: A convolutional neural network (CNN) processes the raw image into a continuous, high-dimensional feature map (latent code) <a class="yt-timestamp" data-t="01:34:39">[01:34:39]</a>, <a class="yt-timestamp" data-t="01:35:12">[01:35:12]</a>.
2.  **Quantizer** <a class="yt-timestamp" data-t="01:35:35">[01:35:35]</a>: The continuous feature vectors are mapped to discrete tokens by finding the nearest vector in a predefined, discrete codebook (dictionary) <a class="yt-timestamp" data-t="01:35:42">[01:35:42]</a>, <a class="yt-timestamp" data-t="01:36:06">[01:36:06]</a>. This codebook is learned during training <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>. The vocabulary size for ImageNet is around 4,000 tokens, significantly smaller than language models' vocabulary sizes <a class="yt-timestamp" data-t="01:29:08">[01:29:08]</a>, <a class="yt-timestamp" data-t="01:30:17">[01:30:17]</a>.
3.  **Decoder (D)** <a class="yt-timestamp" data-t="01:37:15">[01:37:15]</a>: The selected discrete tokens are fed into a decoder (similar to the encoder) to reconstruct the image in pixel space <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>.
4.  **Training** <a class="yt-timestamp" data-t="01:38:31">[01:38:31]</a>: The VQ-VAE is trained by minimizing the distance between the original image and the reconstructed image, along with other losses. This process is self-supervised as the image itself serves as the learning signal <a class="yt-timestamp" data-t="01:46:51">[01:46:51]</a>.

## Advancements: Multiscale Tokenization in Visual Autoregressive Modeling (VARM)

The Visual Autoregressive Modeling (VARM) paper introduces a significant advance in image tokenization by employing a *multiscale* VQ-VAE <a class="yt-timestamp" data-t="01:45:54">[01:45:54]</a>. Instead of flattening a single 2D grid, VARM encodes an image into multiple token maps, each at an increasingly higher resolution <a class="yt-timestamp" data-t="01:45:03">[01:45:03]</a>.

Key features of this approach include:
*   **Multiscale Quantization** <a class="yt-timestamp" data-t="01:45:03">[01:45:03]</a>: The VQ-VAE produces K multiscale discrete token maps <a class="yt-timestamp" data-t="01:52:21">[01:52:21]</a>.
*   **Shared Codebook** <a class="yt-timestamp" data-t="01:41:09">[01:41:09]</a>: All token maps across different resolutions share a single codebook <a class="yt-timestamp" data-t="01:42:45">[01:42:45]</a>. This means the same vocabulary is used to represent concepts at various hierarchical scales, from fine textures (e.g., beak of a parrot) to broader objects (e.g., an entire parrot) <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>, <a class="yt-timestamp" data-t="01:04:31">[01:04:31]</a>.
*   **Interpolation for Resolutions** <a class="yt-timestamp" data-t="01:55:08">[01:55:08]</a>: Smaller resolutions are derived from larger ones through interpolation <a class="yt-timestamp" data-t="01:55:11">[01:55:11]</a>.
*   **Preservation of Spatial Locality** <a class="yt-timestamp" data-t="01:51:50">[01:51:50]</a>: Since there is no flattening operation, the inherent spatial locality of the image is preserved <a class="yt-timestamp" data-t="01:51:52">[01:51:52]</a>.
*   **Parallel Generation** <a class="yt-timestamp" data-t="01:59:17">[01:59:17]</a>: Each entire resolution map can be generated in parallel, as prediction for one part of a map does not depend on other parts of the same map, only on previous, coarser resolution maps <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>, <a class="yt-timestamp" data-t="01:08:55">[01:08:55]</a>. This contrasts sharply with the sequential nature of raster scan, which forces waiting for previous tokens <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.

This multiscale approach leverages the intuition from convolutional neural networks (CNNs) and the human visual system, where information is processed hierarchically from coarse to fine resolutions <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>, <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a>. It results in a more efficient and scalable model for image generation with a significantly reduced computational complexity of O(N^4) compared to O(N^6) for standard autoregressive models <a class="yt-timestamp" data-t="01:12:22">[01:12:22]</a>, <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>.