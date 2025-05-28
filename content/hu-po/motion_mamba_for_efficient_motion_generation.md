---
title: Motion Mamba for efficient motion generation
videoId: rzXjKcqkjxM
---

From: [[hu-po]] <br/> 

Motion Mamba is a model designed for efficient and long sequence [[motion_modeling_in_ai | motion generation]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This paper, released on March 12, 2024, came out around the same time as the [[video_mamba_for_video_understanding | Video Mamba]] paper, prompting a comparison between the two models in different modalities <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Core Problem and Approach

Human [[motion_modeling_in_ai | motion generation]] is a significant area in generative computer vision, but achieving long sequence and efficient motion generation remains a [[challenges_in_video_motion_estimation | challenge]] <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. This is due to the inherent "long sequence" problem, similar to video understanding, where large amounts of data exist across the time domain <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

[[limitations_and_potential_of_mamba_models_in_ai | Mamba models]], which are a type of state-space model (SSM), offer a solution due to their linear complexity and efficient hardware-aware design, unlike Transformers which have quadratic scaling computational requirements for long sequences <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>, <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>, <a class="yt-timestamp" data-t="01:51:50">[01:51:50]</a>. Motion Mamba represents the first integration of the [[limitations_and_potential_of_mamba_models_in_ai | Mamba model]] into the domain of [[motion_modeling_in_ai | motion generation]] <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>.

### State-Space Models (SSMs)

SSMs are based on a continuous system that maps a 1D function or sequence through a hidden state `H` <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>, <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>. This hidden state compresses all information from previous points in time <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>. The continuous ordinary differential equation (ODE) for SSMs is approximated using discretization, specifically the zero-order hold method, to handle discrete sequences like video frames or motion keyframes <a class="yt-timestamp" data-t="00:31:15">[00:31:15]</a>, <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>. This transforms the continuous ODE into a discrete equation where the hidden state `H_T` at time `T` depends on the previous hidden state `H_T-1` and the input `X` <a class="yt-timestamp" data-t="00:32:28">[00:32:28]</a>.

Unlike traditional linear time-invariant SSMs, [[limitations_and_potential_of_mamba_models_in_ai | Mamba models]] implement a selective scan mechanism as their core SSM operator <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>, <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. The parameters of a [[limitations_and_potential_of_mamba_models_in_ai | Mamba model]] reside within specific matrices (A, B, C) that are learned during training <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>.

## Architecture

Motion Mamba is built as a latent diffusion model <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>, <a class="yt-timestamp" data-t="00:38:37">[00:38:37]</a>.

*   **Latent Diffusion Model**: Diffusion models gradually reduce noise from a Gaussian distribution to a target data distribution <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>. In Motion Mamba, the diffusion process occurs in a latent space, which is a compressed representation of the full motion animation <a class="yt-timestamp" data-t="00:46:03">[00:46:03]</a>. This compression is achieved using a variational autoencoder (VAE), consisting of an encoder to map motions to the latent space and a decoder to reconstruct motions from it <a class="yt-timestamp" data-t="00:46:29">[00:46:29]</a>, <a class="yt-timestamp" data-t="00:47:39">[00:47:39]</a>. The diffusion model's denoiser is conditioned on text input, processed by a frozen text encoder (e.g., from CLIP) <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>.
*   **Denoiser Architecture**: The denoiser unit utilizes a U-Net architecture, comprising encoder blocks that reduce dimensionality and decoder blocks that reconstruct it, arranged in reverse order <a class="yt-timestamp" data-t="00:49:19">[00:49:19]</a>, <a class="yt-timestamp" data-t="00:49:30">[00:49:30]</a>. A Transformer-based attention mixer block is placed at the "choke point" (bottleneck) where dimensionality is smallest, making attention mechanisms more computationally feasible <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.
*   **Specialized Mamba Blocks**: Motion Mamba introduces two specialized blocks:
    *   **Hierarchical Temporal Mamba Block**: This block processes the temporal dimension (the time dimension of the animation) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>, <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. It employs a hierarchical scan strategy where the number of scans changes depending on the layer's depth in the encoder-decoder hierarchy <a class="yt-timestamp" data-t="00:53:53">[00:53:53]</a>, <a class="yt-timestamp" data-t="00:55:59">[00:55:59]</a>. Lower levels, dealing with high-frequency details like exact joint motions, have more scans, while higher, more abstract levels (e.g., representing concepts like "walking") have fewer scans <a class="yt-timestamp" data-t="00:56:02">[00:56:02]</a>, <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>.
    *   **Bidirectional Spatial Mamba Block**: This block handles the spatial dimension, which in [[motion_modeling_in_ai | motion generation]] refers to the arrangement of joints in the skeleton (e.g., head-to-toe, toe-to-head) <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>, <a class="yt-timestamp" data-t="01:58:54">[01:58:54]</a>. Bidirectional scanning means processing the sequence from both forward and reverse directions <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>, <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## Experimental Results and Evaluation

Motion Mamba was evaluated on two key benchmarks for [[motion_modeling_in_ai | motion generation]]:
*   **HumanML3D**: Contains approximately 14,000 motions <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>.
*   **KIT ML**: Contains about 3,000 motions <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>.

These datasets are considered relatively small for generative tasks <a class="yt-timestamp" data-t="01:20:28">[01:20:28]</a>.

### Performance Metrics

Motion Mamba claims to achieve state-of-the-art (SOTA) performance, showing a 50% FID (Fréchet Inception Distance) improvement and quadruple improvement in inference speed compared to previous diffusion-based methods like MLD and MotionDiffuse <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>, <a class="yt-timestamp" data-t="01:46:08">[01:46:08]</a>, <a class="yt-timestamp" data-t="01:46:17">[01:46:17]</a>.

On HumanML3D, Motion Mamba's FID score is 0.28, which, at the time of its release, was considered state-of-the-art compared to MLD (0.473) and MotionDiffuse (0.54) <a class="yt-timestamp" data-t="01:25:52">[01:25:52]</a>, <a class="yt-timestamp" data-t="01:34:54">[01:34:54]</a>. For KIT ML, Motion Mamba scored 0.307 FID, outperforming MLD (0.4) <a class="yt-timestamp" data-t="01:26:52">[01:26:52]</a>, <a class="yt-timestamp" data-t="01:27:02">[01:27:02]</a>. While strong, newer papers may have since surpassed these scores <a class="yt-timestamp" data-t="01:26:07">[01:26:07]</a>.

### Inference Speed

A significant advantage of [[limitations_and_potential_of_mamba_models_in_ai | Mamba models]] is their speed and computational efficiency, especially with long sequences, due to their linear scaling complexity <a class="yt-timestamp" data-t="01:29:09">[01:29:09]</a>. Motion Mamba demonstrates significantly faster average inference times compared to MotionDiffuse and MLD <a class="yt-timestamp" data-t="01:34:39">[01:34:39]</a>, <a class="yt-timestamp" data-t="01:34:52">[01:34:52]</a>.

### Future Potential

As the dimensionality of motion data increases (e.g., more detailed skeletons with hands and more joint rotations, higher sampling frequencies), [[limitations_and_potential_of_mamba_models_in_ai | Mamba models]] are poised to become increasingly advantageous over Transformers unless GPU performance scales dramatically to offset the quadratic complexity of attention mechanisms <a class="yt-timestamp" data-t="01:32:02">[01:32:02]</a>, <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>. Motion Mamba's efficiency and effectiveness mark a significant leap forward in [[motion_modeling_in_ai | human motion generation]] <a class="yt-timestamp" data-t="01:46:32">[01:46:32]</a>, <a class="yt-timestamp" data-t="01:46:35">[01:46:35]</a>. There is also potential for Motion Mamba to act as a data generator, creating larger datasets for training even more advanced [[motion_modeling_in_ai | generative motion models]] <a class="yt-timestamp" data-t="01:21:35">[01:21:35]</a>.