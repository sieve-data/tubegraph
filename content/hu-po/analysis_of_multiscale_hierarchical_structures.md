---
title: Analysis of multiscale hierarchical structures
videoId: -jG7S5g071Q
---

From: [[hu-po]] <br/> 

Visual Autoregressive Modeling (V.A.R.) introduces a novel approach to image generation by framing autoregressive learning as a process of "next scale prediction" or "next resolution prediction" <a class="yt-timestamp" data-t="0:07:42">[00:07:42]</a>, <a class="yt-timestamp" data-t="0:18:01">[00:18:01]</a>. This paradigm shift, which won a best paper award at the prestigious NeurIPS conference <a class="yt-timestamp" data-t="0:04:02">[00:04:02]</a>, deviates from traditional methods that flatten images into one-dimensional sequences.

## Traditional Autoregressive Image Modeling

Previously, autoregressive models for images typically involved tokenizing continuous images into 2D grids, which were then flattened into a one-dimensional sequence for autoregressive learning <a class="yt-timestamp" data-t="0:15:05">[00:15:05]</a>. This process mirrored sequential language modeling, where the model predicts the next token given all previous tokens <a class="yt-timestamp" data-t="0:08:01">[00:08:01]</a>, <a class="yt-timestamp" data-t="0:15:14">[00:15:14]</a>.

The most common flattening method is a row-major raster scan (left-to-right, top-to-down) <a class="yt-timestamp" data-t="0:15:41">[00:15:41]</a>, <a class="yt-timestamp" data-t="0:42:06">[00:42:06]</a>. Other variants include spiral or Z-curve orders <a class="yt-timestamp" data-t="0:42:13">[00:42:13]</a>. This ordering is based on the inductive prior of language and text <a class="yt-timestamp" data-t="0:15:51">[00:15:51]</a>.

### Limitations of Raster Scan Ordering

The raster scan approach for images presents several fundamental problems:
*   **Inappropriate Inductive Prior**: It is not the correct inductive prior for images, which inherently have complex, multi-directional relationships <a class="yt-timestamp" data-t="0:16:13">[00:16:13]</a>, <a class="yt-timestamp" data-t="0:43:01">[00:43:01]</a>.
*   **Bidirectional Correlation**: Image feature maps possess bidirectional correlations that contradict the unidirectional dependency assumption of autoregressive models <a class="yt-timestamp" data-t="0:43:21">[00:43:21]</a>. This limits generalizability in tasks requiring bidirectional reasoning, such as predicting the top part of an image given the bottom part <a class="yt-timestamp" data-t="0:43:28">[00:43:28]</a>.
*   **Spatial Locality Disruption**: Flattening disrupts the inherent spatial locality of image features. Closely correlated tokens may become distant in the linear sequence, weakening their relationships due to unidirectional constraints <a class="yt-timestamp" data-t="0:44:01">[00:44:01]</a>.
*   **Reliance on Position Embeddings**: To mitigate these issues, traditional models are forced to use position embeddings (e.g., [[layerwise_scaling_and_architecture_tricks | rotary position embeddings]]) to remind the neural network of the spatial relationships between tokens <a class="yt-timestamp" data-t="0:17:09">[00:17:09]</a>, <a class="yt-timestamp" data-t="0:44:21">[00:44:21]</a>, <a class="yt-timestamp" data-t="1:10:57">[01:10:57]</a>.
*   **Computational Inefficiency**: The sequential nature of raster scan generation means that token prediction cannot be parallelized. Predicting the *N*th token requires waiting for the (N-1)th token to be predicted <a class="yt-timestamp" data-t="1:00:50">[01:00:50]</a>. This leads to a total computational complexity of `O(N^6)` for generating an `N x N` image, where N is the image resolution <a class="yt-timestamp" data-t="1:14:02">[01:14:02]</a>, <a class="yt-timestamp" data-t="1:33:54">[01:33:54]</a>.

## Multiscale Hierarchical Approach in V.A.R.

V.A.R. reformulates the autoregressive task for images by leveraging a multiscale, coarse-to-fine nature <a class="yt-timestamp" data-t="0:17:56">[00:17:56]</a>. This means the model predicts the next higher resolution token map conditioned on all previously generated lower resolution maps <a class="yt-timestamp" data-t="0:18:05">[00:18:05]</a>, <a class="yt-timestamp" data-t="0:50:41">[00:50:41]</a>.

### Inspiration from Human Vision and CNNs

This hierarchical approach is deeply rooted in the understanding of how humans perceive images and how convolutional neural networks (CNNs) were designed <a class="yt-timestamp" data-t="0:19:19">[00:19:19]</a>, <a class="yt-timestamp" data-t="0:20:44">[00:20:44]</a>.
*   **Human Visual System**: The architecture of CNNs, with their hierarchical layers and increasing receptive fields, was inspired by the layers of pyramidal neurons in the human visual cortex (V1, V2, V3) <a class="yt-timestamp" data-t="0:21:06">[00:21:06]</a>, <a class="yt-timestamp" data-t="0:21:28">[00:21:28]</a>. Lower layers represent spatially restricted concepts, while higher layers aggregate information, representing concepts with a receptive field of the entire image <a class="yt-timestamp" data-t="1:28:51">[01:28:51]</a>.
*   **CNNs**: In a CNN, each neuron in a higher layer has a receptive field that aggregates information from a larger area of the lower layer, naturally building a hierarchical representation <a class="yt-timestamp" data-t="0:19:50">[0:19:50]</a>, <a class="yt-timestamp" data-t="0:20:06">[00:20:06]</a>. This "coarse-to-fine" inductive prior is inherently baked into CNNs <a class="yt-timestamp" data-t="0:20:06">[00:20:06]</a>.

### V.A.R. Implementation and Advantages

V.A.R. involves two main stages:
1.  **Multiscale VQ-VAE Training**: A multiscale VQ-VAE (Vector Quantized Variational Autoencoder) encodes an image into K token maps, each at an increasingly higher resolution, culminating in a map matching the original image resolution <a class="yt-timestamp" data-t="0:44:54">[00:44:54]</a>, <a class="yt-timestamp" data-t="0:52:29">[00:52:29]</a>.
    *   **Shared Codebook**: Notably, a single codebook (vocabulary) is utilized across all scales, meaning tokens at a coarse resolution (representing broader concepts like "parrot") share the same vocabulary with tokens at a fine resolution (representing micro-details like "beak texture") <a class="yt-timestamp" data-t="1:02:42">[01:02:42]</a>, <a class="yt-timestamp" data-t="1:03:05">[01:03:05]</a>.
    *   **Self-Supervised**: VQ-VAEs are easy to train as they are self-supervised; the image itself serves as the learning signal <a class="yt-timestamp" data-t="0:46:51">[00:46:51]</a>.
2.  **V.A.R. Transformer Training**: A Transformer model is then trained on these multiscale tokens. The autoregressive unit becomes an entire token map (a full resolution) rather than a single token <a class="yt-timestamp" data-t="0:51:54">[00:51:54]</a>.
    *   **No Position Embeddings**: This formulation means the V.A.R. Transformer does not require [[layerwise_scaling_and_architecture_tricks | position embeddings]] <a class="yt-timestamp" data-t="0:17:45">[00:17:45]</a>, as the hierarchical structure intrinsically conveys spatial information.
    *   **Parallel Generation**: All tokens within a specific resolution map can be generated in parallel, conditioned only on previously generated lower-resolution maps <a class="yt-timestamp" data-t="0:59:15">[00:59:15]</a>. This parallelization significantly improves inference speed <a class="yt-timestamp" data-t="0:59:05">[00:59:05]</a>, leading to a computational complexity of `O(N^4)` <a class="yt-timestamp" data-t="1:01:54">[01:01:54]</a>, <a class="yt-timestamp" data-t="1:14:31">[01:14:31]</a>. This is a substantial improvement over the `O(N^6)` of raster scan models.

### Performance and Scalability

V.A.R. has demonstrated remarkable performance:
*   **ImageNet 256x256 Benchmark**: V.A.R. improved the Fréchet Inception Distance (FID) from 18 to 1 and the Inception Score from 80 to 350 <a class="yt-timestamp" data-t="0:09:50">[00:09:50]</a>, <a class="yt-timestamp" data-t="0:10:00">[00:10:00]</a>, outperforming other models like Diffusion Transformers (DiT), Generative Adversarial Networks (GANs), and other autoregressive models <a class="yt-timestamp" data-t="1:13:21">[01:13:21]</a>.
*   **Inference Speed**: It achieves a 20x faster inference speed compared to previous approaches <a class="yt-timestamp" data-t="0:09:57">[00:09:57]</a>, <a class="yt-timestamp" data-t="1:14:43">[01:14:43]</a>. This is a direct consequence of the parallel generation enabled by the multiscale structure.
*   **Zero-Shot Generalization**: V.A.R. exhibits strong zero-shot generalization abilities for downstream tasks like image inpainting, outpainting, and editing, meaning it performs well without specific fine-tuning for these tasks <a class="yt-timestamp" data-t="0:42:06">[00:42:06]</a>.
*   **[[large_language_models_llms_and_scaling | Scaling Laws]]**: Like [[large_language_models_llms_and_scaling | Large Language Models (LLMs)]], V.A.R. adheres to predictable scaling laws. Increasing model size or training compute leads to a predictable decrease in test loss, indicating that larger V.A.R. Transformers are more compute-efficient <a class="yt-timestamp" data-t="1:14:54">[01:14:54]</a>, <a class="yt-timestamp" data-t="1:15:05">[01:15:05]</a>, <a class="yt-timestamp" data-t="1:16:56">[01:16:56]</a>.

## [[potential_applications_of_multiscale_autoregressive_models | Potential Applications and Future Work]]

The success of V.A.R. on images suggests broader applicability:
*   **Improvements to VQ-VAE**: Further advances in the VQ-VAE tokenizer could enhance autoregressive generative models <a class="yt-timestamp" data-t="1:17:33">[01:17:33]</a>.
*   **Text-to-Image/Video Generation**: The framework could be extended to [[multimodal_model_benchmarks | text-to-image generation]] and even [[potential_applications_of_multiscale_autoregressive_models | 3D models or videos]] <a class="yt-timestamp" data-t="1:17:48">[01:17:48]</a>, <a class="yt-timestamp" data-t="1:17:57">[01:17:57]</a>. For videos, this method offers inherent advantages in temporal consistency compared to diffusion-based generators like Sora <a class="yt-timestamp" data-t="1:18:04">[01:18:04]</a>.
*   **Beyond Images**: The core idea of rethinking how high-dimensional data is flattened into one-dimensional sequences for Transformers can be applied to other modalities where current flattening methods are "sketchy" <a class="yt-timestamp" data-t="0:56:53">[00:56:53]</a>, such as protein structures or graphs <a class="yt-timestamp" data-t="0:57:26">[00:57:26]</a>, <a class="yt-timestamp" data-t="1:19:09">[01:19:09]</a>. For [[multiresolution_hash_grids_for_3d_representation | 3D representation]], instead of rasterizing through a volume of space, a multiscale approach could offer a more natural ordering <a class="yt-timestamp" data-t="1:50:20">[01:50:20]</a>.

The simplicity, superior performance, and faster inference of V.A.R. make it a highly promising direction for scalable image and potentially other data modalities generation, indicating a shift away from traditional raster scan methods <a class="yt-timestamp" data-t="1:20:57">[01:20:57]</a>.