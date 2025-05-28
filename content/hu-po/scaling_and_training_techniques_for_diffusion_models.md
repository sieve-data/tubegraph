---
title: Scaling and Training Techniques for Diffusion Models
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Stable Diffusion 3 (SD3) is the latest release in Stability AI's series of generative image models <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. Developed by Stability AI, a startup known for creating open-source models, SD3 is described as a "big paper" and potentially the "greatest diffusion model paper" ever read <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. Unlike academic papers often produced by one or two individuals, this paper is clearly the result of a much larger team <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. It offers a comprehensive collection and summary of various diffusion model techniques, covering training flows, [[Transformer architecture in diffusion models | architectures]], model parameter space, and data considerations across 28 jam-packed pages <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

Stability AI is praised for its commitment to open science by publishing such detailed papers, in contrast to other companies like Midjourney or OpenAI, which tend to keep their methods secret <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. SD3 is currently the state-of-the-art image model, a claim supported by robust human evaluations <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

## Fundamentals of Diffusion Models

Diffusion models generate data from noise by inverting the forward path of data towards noise <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>. They transform a pure noise distribution (P1) into a target data distribution (P0), which in the case of image generation, represents images <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>. This process involves moving from a noisy image state to a clean image state through a series of inference steps <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>. Each step requires running a neural network on a GPU <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.

A core concept is the "vector field," which guides the movement from noise to data <a class="yt-timestamp" data-t="22:05:00">[22:05:05]</a>. The diffusion model evaluates this vector field at each point to determine the direction to move in order to flow from the noise into the data distribution <a class="yt-timestamp" data-t="23:55:00">[23:55:00]</a>. The objective is to approximate this vector field using a neural network, whose weights are denoted by Theta <a class="yt-timestamp" data-t="21:48:00">[21:48:00]</a>.

## Training Objectives

The training process for diffusion models involves defining a loss function.
Initially, the "flow matching objective" (LFM) was proposed, which aims to minimize the squared difference between the true conditional vector field (UTz) and the neural network's predicted vector field (V Theta ZT) <a class="yt-timestamp" data-t="28:46:00">[28:46:00]</a>. However, this objective is intractable because the true conditional vector field is unknown <a class="yt-timestamp" data-t="29:43:00">[29:43:00]</a>.

This leads to the "conditional flow matching objective" (LCFM), which replaces the intractable term with a conditional vector field, making it computable <a class="yt-timestamp" data-t="29:59:00">[29:59:00]</a>.
Further manipulation of this loss function leads to the "noise prediction objective" <a class="yt-timestamp" data-t="33:41:00">[33:41:00]</a>. In this formulation, the neural network directly predicts the noise (Epsilon Theta ZT) instead of the velocity vector <a class="yt-timestamp" data-t="32:49:00">[32:49:00]</a>. This is significantly easier to calculate during training because the added noise is known <a class="yt-timestamp" data-t="33:21:00">[33:21:00]</a>.

## Flow Trajectories and Time Step Sampling

The paper systematically explores various methods for guiding the diffusion process and sampling time steps during training.

### Flow Trajectories

*   **Curved Paths vs. Straight Paths**: Traditional diffusion models often take "curved paths" in the high-dimensional image space, leading to many integration steps and less efficient sampling <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>. A "straight path" would allow for simulation with a single step, reducing error accumulation and improving sampling speed <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.
*   **[[Training and implementation details of Transformerbased diffusion models | Rectified Flow]]**: This method defines the forward process as a straight path between the data and noise distributions <a class="yt-timestamp" data-t="35:56:00">[35:56:00]</a>. It is the simplest and most intuitive formulation <a class="yt-timestamp" data-t="36:40:00">[36:40:00]</a>.
*   **Other Formulations**: The paper reviews and compares other flow trajectory methods, including EDM (from Karras 2022), Cosine (from Nichol and Dhariwal 2021), and LDM Linear (from [[latent_diffusion_model_for_neural_networks | Rombach et al. 2022]]) <a class="yt-timestamp" data-t="35:03:00">[35:03:00]</a>.

### Time Step Sampling

During training, a random time step (T) between 0 and 1 is chosen for each image to add noise and push a gradient <a class="yt-timestamp" data-t="38:44:00">[38:44:00]</a>.
*   **Uniform Distribution**: Most diffusion papers use a uniform distribution, meaning any time step between 0 and 1 has an equal probability of being chosen <a class="yt-timestamp" data-t="39:00:00">[39:00:00]</a>.
*   **Logit Normal Sampling**: This new technique biases time step sampling towards intermediate steps, typically between T=0.4 and T=0.6 <a class="yt-timestamp" data-t="41:46:00">[41:46:00]</a>. The intuition is that these intermediate steps are more critical for the model to learn effective noise removal or prediction <a class="yt-timestamp" data-t="42:22:00">[42:22:00]</a>.
*   **Other Sampling Methods**: The paper also considers mode sampling with heavy tails and CosMap <a class="yt-timestamp" data-t="40:19:00">[40:19:00]</a>.

### Ablation Studies and Results

The paper conducts extensive ablation studies, testing 24 combinations of flow trajectories and sampling settings <a class="yt-timestamp" data-t="44:02:00">[44:02:00]</a>. Using CLIP and FID scores for evaluation, the studies consistently show that:
*   The combination of [[Training and implementation details of Transformerbased diffusion models | rectified flow]] with logit normal sampling performs best <a class="yt-timestamp" data-t="48:52:00">[48:52:00]</a>. This confirms the hypothesis that intermediate time steps are more important <a class="yt-timestamp" data-t="49:05:00">[49:05:00]</a>.
*   [[Training and implementation details of Transformerbased diffusion models | Rectified flows]] are sample-efficient, outperforming other formulations when sampling fewer steps <a class="yt-timestamp" data-t="51:18:00">[51:18:00]</a>.

This comprehensive comparison saves future researchers significant computational resources by identifying optimal configurations <a class="yt-timestamp" data-t="01:59:01">[01:59:01]</a>.

## Model Architecture: [[Transformer architecture in diffusion models | Multimodal Diffusion Transformer (MMD)]]

The core of Stable Diffusion 3's architecture is a novel [[Transformer architecture in diffusion models | Transformer-based architecture]] called the [[Transformer architecture in diffusion models | Multimodal Diffusion Transformer (MMD)]] <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a> <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. This architecture builds upon the Diffusion Transformer (Dit) <a class="yt-timestamp" data-t="55:59:00">[55:59:00]</a>.

Key features of the [[Transformer architecture in diffusion models | MMD]] block:
*   **Separate MLPs for Modalities**: Unlike standard Transformers that might use cross-attention, the [[Transformer architecture in diffusion models | MMD]] uses two separate sets of weights for the image and text modalities, effectively having independent MLPs for each <a class="yt-timestamp" data-t="56:38:00">[56:38:00]</a>.
*   **Concatenated Self-Attention**: Instead of cross-attention, the image and text sequences are concatenated, and then a single self-attention mechanism is applied to the combined sequence <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>. This allows any part of the text sequence to pay attention to any part of the image sequence, and vice versa, enabling richer information flow between modalities <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>. After attention, the sequences are separated again for their respective MLPs <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>.
*   **Computational Cost**: This concatenated self-attention approach is more computationally expensive than cross-attention due to the increased sequence length, but it improves the integration of information <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>.

## Scaling Studies

The model's size is parameterized by a single variable, `D`, which controls the depth (number of attention blocks), hidden size (width of MLP layers), and number of attention heads <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a> <a class="yt-timestamp" data-t="01:09:47">[01:09:47]</a>. This unified parameterization simplifies scaling studies.

Results from the scaling studies show that:
*   Larger models (higher `D` values) consistently achieve lower validation loss and better performance <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>.
*   The scaling trend shows no sign of saturation, indicating that future models can continue to improve with increased compute and larger GPUs <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>.

## Data and Training Details

### Data Augmentation and Filtering

Stable Diffusion 3 is trained on large datasets like CC12M and ImageNet <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.
*   **Caption Augmentation**: Human-generated captions often lack detail. To address this, Stability AI uses an off-the-shelf vision-language model, CogVLM, to create synthetic annotations for images <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>. They use a 50/50 mix of original and synthetic captions during training <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.
*   **Deduplication**: The dataset is deduplicated by comparing image embeddings to avoid overfitting on duplicate images, ensuring a diverse representation of visual concepts <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>.

### Latent Space Operations

[[Latent diffusion model for neural networks | Diffusion models]] often operate in a "latent space" rather than raw pixel space <a class="yt-timestamp" data-t="01:17:55">[01:17:55]</a>. This latent space is the bottleneck of a pre-trained autoencoder <a class="yt-timestamp" data-t="01:18:01">[01:18:01]</a>.
*   **Latent Channel Dimensionality**: Increasing the number of latent channels (`D` in this context, separate from the model size `D`) significantly boosts reconstruction performance and achievable image quality <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a>. Experiments show that higher latent channel dimensions (e.g., 16 channels vs. 4 or 8) lead to better results across various metrics <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>.

### Text Encoders

SD3 uses an ensemble of three pre-trained, frozen text models for conditioning: Clip G14, Clip L14 (both from the CLIP family), and T5 XXL <a class="yt-timestamp" data-t="01:35:55">[01:35:55]</a> <a class="yt-timestamp" data-t="01:54:50">[01:54:50]</a>.
*   **Dropout**: The model is trained with an aggressive dropout rate (46%) on individual text encoders <a class="yt-timestamp" data-t="01:37:51">[01:37:51]</a>. This makes the model robust, allowing it to function effectively even if a subset of encoders is used during inference, which is beneficial for memory efficiency <a class="yt-timestamp" data-t="01:38:25">[01:38:25]</a>.
*   **Specific Contributions**: Removing the T5 encoder, while saving memory, significantly impacts the model's ability to spell correctly <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>. This suggests that the T5 encoder contributes a more nuanced textual understanding, possibly due to its different training objective compared to the contrastive learning of CLIP encoders <a class="yt-timestamp" data-t="01:41:08">[01:41:08]</a>.

### Training Pipeline Stages

The training pipeline for SD3 involves a three-stage process:
1.  **Pre-training**: Models are initially pre-trained at a low image resolution (e.g., 256x256) <a class="yt-timestamp" data-t="01:34:34">[01:34:34]</a>.
2.  **Fine-tuning**: This is followed by fine-tuning at higher resolutions <a class="yt-timestamp" data-t="01:35:37">[01:35:37]</a>.
3.  **Direct Preference Optimization (DPO)**: The model is aligned using DPO on a specific dataset (e.g., 128 captions from the Party Prompts set) <a class="yt-timestamp" data-t="01:45:19">[01:45:19]</a>. This step is crucial for making generated images more aesthetically pleasing, a quality often evaluated by human preference <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. DPO optimizes the model to generate images preferred by humans, even if it means slightly moving away from a strict matching of the original data distribution <a class="yt-timestamp" data-t="01:48:59">[01:48:59]</a>.

### Additional Training Tricks

*   **Mixed Precision Training**: To handle large models and resolutions, mixed precision training (e.g., bf16) is used to improve efficiency and reduce memory usage <a class="yt-timestamp" data-t="01:24:44">[01:24:44]</a>. QK normalization (normalizing Query and Key matrices before attention) helps stabilize training in these settings <a class="yt-timestamp" data-t="01:25:56">[01:25:56]</a>.
*   **Positional Encodings for Varying Aspect Ratios**: The model is trained on a mix of different resolutions and aspect ratios (e.g., phone, desktop resolutions) <a class="yt-timestamp" data-t="01:27:03">[01:27:03]</a>. 2D frequency embeddings are adapted using interpolation to ensure consistent positional information regardless of the image's aspect ratio <a class="yt-timestamp" data-t="01:27:50">[01:27:50]</a>.
*   **Resolution-Dependent Shifting of Time Step Schedules**: The optimal time step schedule for training depends on the image resolution <a class="yt-timestamp" data-t="01:28:20">[01:28:20]</a>. A "shift value" (e.g., 3, 6, 2, 4, 1.5, 1) is introduced, with a value of 3 being preferred by human evaluators <a class="yt-timestamp" data-t="01:29:01">[01:29:01]</a>. These subjective human preferences are directly used to tune hyperparameters <a class="yt-timestamp" data-t="01:30:32">[01:30:32]</a>.

## Performance and Scalability

[[Performance and scalability of diffusion models with Transformers | Stable Diffusion 3]] demonstrates competitive performance with state-of-the-art proprietary models like DALL-E 3 and Midjourney V6, often achieving higher human preference win rates <a class="yt-timestamp" data-t="01:31:47">[01:31:47]</a>. The model exhibits strong scaling laws, where increasing model size (depth, width, attention heads) consistently improves performance, suggesting continued future improvements with more computational resources <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>.

While the paper primarily focuses on image generation, a preliminary scaling study on videos was conducted, using methods like collapsing the temporal dimension into the batch axis <a class="yt-timestamp" data-t="01:12:23">[01:12:23]</a>. However, the results were likely not strong enough to be a focal point, especially after the release of Sora <a class="yt-timestamp" data-t="01:13:22">[01:13:22]</a>.

## Future Outlook

The consistent improvements with scaling laws suggest that the performance of diffusion models will continue to advance as more powerful GPUs become available <a class="yt-timestamp" data-t="01:21:27">[01:21:27]</a>. This continuous improvement implies an optimistic future for high-quality generative AI <a class="yt-timestamp" data-t="01:45:05">[01:45:05]</a>.