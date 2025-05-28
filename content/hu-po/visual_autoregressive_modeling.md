---
title: Visual autoregressive modeling
videoId: -jG7S5g071Q
---

From: [[hu-po]] <br/> 

Visual Autoregressive Modeling (VAR) is a novel generative paradigm for images that redefines autoregressive learning as next-scale prediction rather than next-token prediction <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This approach led to a paper that won a prestigious award at the Neural Information Processing Systems (NeurIPS) conference <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Controversy Surrounding the Paper
The first author, K. Tion, was reportedly involved in a legal battle with ByteDance, where he interned <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Allegations suggested Tion "maliciously disrupted or was poisoning internal model training by altering code" leading to "significant resource wastage" <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The extent of disruption and intent remains unclear, but such incidents in large training runs can lead to resource wastage from the last checkpoint and engineering time to fix issues <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Fundamentals of Autoregressive Learning and Image Generation

### Traditional Autoregressive Learning
[[selfimproving_machine_learning_models | Autoregressive learning]] is the core idea behind language models, where the model predicts the next token given all previous tokens in a sequence <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Language has an inherent one-dimensional order, allowing for sequential prediction <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Traditional Image Tokenization
For images, which are inherently 2D continuous signals, they are tokenized into a grid of 2D tokens, then flattened into a 1D sequence for autoregressive learning, mirroring sequential language modeling <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. This flattening typically uses a row-major raster scan (left-to-right, top-to-down) <a class="yt-timestamp" data-t="00:42:06">[00:42:06]</a>. Other scan orders like spiral or Z-curve have also been used <a class="yt-timestamp" data-t="00:42:13">[00:42:13]</a>.

### Problems with Traditional Flattening
This 1D raster scan order for images introduces several issues:
*   **Contradicts Bidirectional Correlation**: Image feature maps have bidirectional correlations, which conflicts with the unidirectional dependency assumption of autoregressive models <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.
*   **Restricts Generalizability**: It restricts generalizability in tasks requiring bidirectional reasoning (e.g., cannot predict the top part of an image given the bottom part) <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>.
*   **Disrupts Spatial Locality**: Flattening compromises the inherent spatial locality in image feature maps, where tokens and their immediate neighbors are closely correlated <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.
*   **Requires Position Embeddings**: To mitigate these issues, techniques like rotary position embeddings (RoPE) are used to remind the neural network of spatial positions <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. VAR aims to avoid the need for such embeddings <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

## VAR's Innovative Approach: Next Scale Prediction

VAR proposes a new generation paradigm where autoregressive learning on images is defined as [[potential_applications_of_multiscale_autoregressive_models | next-scale prediction]] or next-resolution prediction <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

### Hierarchical Perception
Humans typically perceive or create images in a hierarchical, multi-scale, coarse-to-fine manner <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. This intuition aligns with how convolutional neural networks (CNNs) process images, aggregating information hierarchically through receptive fields <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. This concept is also inspired by the human visual system, where neurons in the visual cortex are arranged in layers (V1, V2, V3) that process visual information at increasing levels of abstraction and receptive field size <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

### Two-Stage Training Process
VAR involves two main training stages:

#### Stage 1: Multiscale VQ-VAE Autoencoder
A multiscale VQ-VAE (Vector Quantized Variational Autoencoder) is trained to encode an image into K token maps, each at an increasingly higher resolution <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>.
*   **Encoder (E)**: A CNN takes a raw image and turns it into continuous feature maps <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.
*   **Quantizer**: These continuous feature vectors are then quantized by choosing the closest vector from a discrete codebook (vocabulary) <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>.
*   **Shared Codebook**: Uniquely, VAR uses a shared codebook across all scales, meaning the same vocabulary of tokens is used for both fine-grained (e.g., texture of a beak) and coarse-grained concepts (e.g., entire parrot) <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
*   **Decoder (D)**: The quantized discrete tokens are fed into a decoder to reconstruct the image <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>.
*   **Self-Supervised Training**: The VQ-VAE is trained in a self-supervised manner, where the original image serves as its own learning signal, making it easy to train on vast amounts of unlabeled image data <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>. VAR uses a vanilla VQ-VAE architecture <a class="yt-timestamp" data-t="01:10:19">[01:10:19]</a>.

#### Stage 2: VAR Transformer Training
The trained VQ-VAE then provides the token maps for the VAR Transformer.
*   **Next Scale Prediction**: The Transformer predicts the next higher resolution token map (RK) conditioned on all previous ones (R1, R2, ..., RK-1) <a class="yt-timestamp" data-t="00:50:41">[00:50:41]</a>.
*   **Start Token**: A class embedding serves as the start token for conditional information <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>.
*   **Blockwise Causal Attention Mask**: An attention mask ensures that each RK can only attend to previous or equal resolution maps (R <= K) <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>.
*   **Parallel Generation**: Unlike traditional autoregressive models where each token is predicted sequentially, VAR can generate an entire token map at a given resolution in parallel <a class="yt-timestamp" data-t="00:59:15">[00:59:15]</a>. This is because elements within the same resolution map do not depend on each other, only on previous, coarser resolution maps <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>.

## Key Advantages and Performance

VAR leverages a GPT-2 Transformer architecture <a class="yt-timestamp" data-t="01:10:22">[01:10:22]</a> and does not use advanced techniques like rotary position embeddings (RoPE), SwiGLU MLP, or RMSNorm <a class="yt-timestamp" data-t="01:10:55">[01:10:55]</a>. Despite its relative simplicity, it achieves impressive results:

*   **Superior Image Quality**: VAR improves Fréchet Inception Distance (FID) from 18 to 1 and Inception Score (IS) from 80 to 350 on ImageNet 256x256 <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. A FID of 1 is exceptionally low, indicating very high image quality compared to real images <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Faster Inference Speed**: VAR achieves a 20x faster inference speed compared to traditional methods <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This is due to its parallel token generation at each resolution step <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.
*   **Improved Computational Complexity**:
    *   Traditional autoregressive generation on an N x N latent space requires O(N^2) decoding iterations and O(N^6) total computations <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>.
    *   VAR significantly reduces this to O(N^4) total computations, with only log(N) iterations <a class="yt-timestamp" data-t="01:14:28">[01:14:28]</a>. This efficiency arises from the ability to generate all tokens within a given resolution map in parallel <a class="yt-timestamp" data-t="01:01:54">[01:01:54]</a>.
*   **Zero-Shot Generalization**: VAR demonstrates zero-shot generalization abilities in downstream tasks like image inpainting, outpainting, and editing, meaning it performs these tasks without fine-tuning <a class="yt-timestamp" data-t="01:13:09">[01:13:09]</a>.
*   **Scaling Laws**: VAR exhibits predictable scaling laws with respect to model size, training tokens, and optimal training compute, similar to large language models <a class="yt-timestamp" data-t="01:14:54">[01:14:54]</a>. Larger VAR Transformers are more compute-efficient, achieving the same performance with less computation <a class="yt-timestamp" data-t="01:16:56">[01:16:56]</a>.

## Limitations and Future Work
The paper identifies several areas for future research and improvement:
*   **VQ-VAE Tokenizer Enhancement**: Further advancements in the VQ-VAE tokenizer itself could significantly enhance autoregressive generative models <a class="yt-timestamp" data-t="01:17:33">[01:17:33]</a>.
*   **Text-to-Image Generation**: Applying VAR to [[Text Encoder Ensembles in Diffusion Models | text-to-image generation]] is a high priority <a class="yt-timestamp" data-t="01:17:48">[01:17:48]</a>.
*   **Extension to 3D and Video**: The concept can be extended to 3D and temporal dimensions, such as generating videos via [[Application of Vision Language Models in Robotics | next-scale prediction]] in 3D pyramids <a class="yt-timestamp" data-t="01:17:57">[01:17:57]</a>. This approach offers inherent advantages in temporal consistency compared to [[conditional_diffusion_model_for_neural_networks | diffusion-based generators]] like Sora <a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>.
*   **Other Data Modalities**: The core idea of rethinking 1D flattening for high-dimensional data could be applied to other modalities like [[rwkv_model_architecture | protein]] structures, graphs, or other complex data types where current flattening methods are unsatisfactory <a class="yt-timestamp" data-t="01:18:48">[01:18:48]</a>. This might involve adapting the multiscale hierarchical concept to suit the specific data structure <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

## Conclusion
VAR's success lies in its simple yet powerful reformulation of autoregressive image generation. By aligning with human perception and the principles of CNNs, it provides a more intuitive and computationally efficient method that outperforms traditional raster-scan approaches <a class="yt-timestamp" data-t="01:20:57">[01:20:57]</a>. This work suggests a significant shift in how [[mixture_of_experts_in_vision_language_modeling | vision language modeling]] and image generation models might be designed in the future, with implications for various applications and data types <a class="yt-timestamp" data-t="01:41:33">[01:41:33]</a>.