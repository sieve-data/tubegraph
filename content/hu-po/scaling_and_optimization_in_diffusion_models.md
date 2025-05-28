---
title: Scaling and optimization in diffusion models
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Stable Diffusion 3 (SD3) represents the third and most recent release of Stable Diffusion, a generative [[diffusion_models_and_image_generation | image model]] developed by Stability AI, an organization known for creating open-source models <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This paper is considered a comprehensive summary of [[diffusion_models_and_image_generation | diffusion models]] in general, detailing various training flows, architectures, model parameter space sweeps, and data handling techniques <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. It is currently regarded as a state-of-the-art [[diffusion_models_and_image_generation | image model]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

The advancements in SD3 reflect a maturity in [[diffusion_models_and_image_generation | image generation]] technology, reaching a point where generated images are almost indistinguishable from reality <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The paper highlights the significant contributions of Stability AI in openly publishing their methods, a contrast to other companies that often keep their advancements proprietary <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## Fundamentals of Diffusion Models

[[diffusion_models_and_image_generation | Diffusion models]] operate by creating data from noise through the inversion of a forward path that transforms data into noise <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. This process takes a pure noise distribution and gradually converts it into a target data distribution, such as an image <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The goal is to learn a mapping that allows sampling from a noise distribution to generate new data points that align with the training data's distribution but are not directly present in it <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

The process involves multiple inference steps, where each step requires running a neural network on a GPU to move from a noisy state closer to the desired image <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. Conceptually, this movement occurs within a high-dimensional image space.

## Optimization of Flow Trajectories

Traditional [[diffusion_models_and_image_generation | diffusion models]] often follow "curved paths" in the high-dimensional latent space, meaning the iterative denoising process might deviate before converging to the final image <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. This curved path necessitates many integration steps, increasing computational cost <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

### [[rectified_flow_in_diffusion_models | Rectified Flow]]

[[rectified_flow_in_diffusion_models | Rectified flow]] is a generative model formulation that aims to connect data and noise distributions in a straight line, reducing the number of steps required for image generation <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. A straight path can be simulated with a single step, minimizing error accumulation and directly impacting sampling speed <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. In SD3, [[rectified_flow_in_diffusion_models | rectified flow]] defines the forward process as a straight path between the data and standard normal distributions <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>.

The underlying mathematical formulation involves defining a velocity vector field that guides the movement from noise to data <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. A neural network approximates this velocity function <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. The training objective for this vector field, known as the flow matching objective, is often intractable <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>. To overcome this, SD3 uses a *conditional flow matching objective*, which is tractable and allows for the calculation of the vector field <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>. This eventually leads to a "noise prediction objective," where the neural network outputs the noise component, which is easier to calculate during training as the noise is self-added <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.

SD3's paper systematically compares [[rectified_flow_in_diffusion_models | rectified flow]] with other established flow trajectories like EDM, Cosine, and LDM Linear <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>. The experimental results indicate that [[rectified_flow_in_diffusion_models | rectified flow]] consistently performs best <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.

## Optimization of Time Step Sampling

During training, [[diffusion_models_and_image_generation | diffusion models]] rely on sampling different time steps (T) to apply noise and push gradients <a class="yt-timestamp" data-t="00:38:31">[00:38:31]</a>. Historically, a uniform distribution was used to pick these time steps <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

SD3 proposes a new sampling strategy called **logit normal sampling** <a class="yt-timestamp" data-t="00:40:41">[00:40:41]</a>. This method biases the sampling towards intermediate time steps, typically between T=0.4 and T=0.6 <a class="yt-timestamp" data-t="00:41:46">[00:41:46]</a>. The intuition behind this is that these intermediate steps are where the model faces the most difficulty and gains the most understanding of the data distribution, as it transitions between highly noisy and nearly clear images <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>.

Through extensive ablation studies comparing logit normal sampling with other methods like mode sampling with heavy tails and Cosine mapping, SD3 found that the combination of [[rectified_flow_in_diffusion_models | rectified flow]] and logit normal sampling yields the best performance <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.

## Model Architecture: Multimodal Diffusion Transformer (MMD)

SD3 introduces a novel **Multimodal Diffusion Transformer (MMD)** architecture for text-to-image generation <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>. This architecture builds upon the Diffusion Transformer (DiT) <a class="yt-timestamp" data-t="00:55:59">[00:55:59]</a>.

The key innovation of the MMD architecture is its handling of multimodal inputs (text and image). Instead of using cross-attention mechanisms, it concatenates the sequence representations of both text and image tokens <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>. A self-attention operation is then performed on this combined sequence, allowing any part of the text sequence to pay attention to any part of the image sequence, and vice versa <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>. After the attention operation, the architecture separates the modalities, using distinct Multi-Layer Perceptrons (MLPs) for image and text processing <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>. This "symmetric design" allows both representations to work in their own space while still accounting for the other modality <a class="yt-timestamp" data-t="00:57:53">[00:57:53]</a>.

While this concatenation approach is more computationally expensive than cross-attention due to the increased sequence length, it enables richer information flow between modalities <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>.

## Scaling Studies

SD3 conducts extensive [[scalability_of_transformerbased_diffusion_models | scaling studies]] by parameterizing model size using a single variable, `D` <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>. This `D` controls the model's depth (number of attention blocks), hidden size (width), and number of attention heads <a class="yt-timestamp" data-t="01:08:13">[01:08:13]</a>. This unified parameterization simplifies [[scalability_of_transformerbased_diffusion_models | scaling comparisons]] <a class="yt-timestamp" data-t="01:09:51">[01:09:51]</a>.

The studies demonstrate a clear scaling law: larger models (higher `D`) consistently achieve lower validation loss and better performance <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>. This trend shows no sign of saturation, suggesting that future improvements can be achieved by simply increasing model size as GPU capabilities advance <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>.

The choice of latent space dimensionality in the pre-trained autoencoder also impacts image quality. Increasing the number of latent channels (e.g., from 4 to 8 to 16) leads to significantly boosted reconstruction performance and higher image quality <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a>. This suggests that as GPUs become larger, increasing this latent dimension will continue to yield better [[diffusion_models_and_image_generation | diffusion models]] <a class="yt-timestamp" data-t="01:21:27">[01:21:27]</a>.

## Data and Training Optimizations

### Data Augmentation and Deduplication
SD3 utilizes large-scale image datasets like CC12M and ImageNet <a class="yt-timestamp" data-t="01:15:13">[01:15:13]</a>. To address the limitations of human-generated captions (which often lack detail regarding background or composition), SD3 augments its captions <a class="yt-timestamp" data-t="01:16:01">[01:16:01]</a>. They use an off-the-shelf vision-language model, CogVLM, to create synthetic annotations, mixing them 50/50 with original captions <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>. This process improves the precision of text information, leading to better image generation accuracy <a class="yt-timestamp" data-t="01:22:37">[01:22:37]</a>.

Additionally, SD3 performs deduplication on its dataset to prevent overfitting on specific images and ensure a diverse training experience, allowing the model to capture a wider variety of visual concepts <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>.

### Training Stability and Efficiency
SD3 employs several techniques for stable and efficient training:
*   **Mixed Precision Training:** To manage memory and speed, models are trained using mixed precision (e.g., bf16). Normalizing the Query (Q) and Key (K) before the attention operation helps prevent instability in the attention logits, ensuring efficient training <a class="yt-timestamp" data-t="01:25:41">[01:25:41]</a>.
*   **Progressive Resolution Training:** Models are pre-trained at lower resolutions (e.g., 256x256) and then fine-tuned on higher resolutions <a class="yt-timestamp" data-t="01:31:31">[01:31:31]</a>.
*   **Positional Encodings for Varying Aspect Ratios:** SD3 trains on a mix of different resolutions and aspect ratios (e.g., cell phone vs. desktop formats) <a class="yt-timestamp" data-t="01:27:03">[01:27:03]</a>. They adapt 2D frequency embeddings using interpolation to ensure consistent positional information regardless of aspect ratio <a class="yt-timestamp" data-t="01:27:48">[01:27:48]</a>.
*   **Resolution-Dependent Time Step Schedules:** The time step sampling schedule is adjusted based on the image resolution, with different "shifting factors" preferred by human evaluators for various sizes <a class="yt-timestamp" data-t="01:28:21">[01:28:21]</a>.
*   **Pre-computed Embeddings:** To accelerate training, text embeddings from text encoders are pre-computed and stored, rather than being encoded on the fly during each training step <a class="yt-timestamp" data-t="02:03:51">[02:03:51]</a>.

### Direct Preference Optimization (DPO)
SD3 uses a three-stage training pipeline: pre-training, fine-tuning, and then **Direct Preference Optimization (DPO)** <a class="yt-timestamp" data-t="01:45:33">[01:45:33]</a>. DPO is used to align the model with human aesthetic preferences <a class="yt-timestamp" data-t="01:46:10">[01:46:10]</a>. By pushing gradients into LoRAs (Low-Rank Adaptation) based on a dataset of aesthetically pleasing prompts, the model generates more visually appealing images, even from simpler captions <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. This technique helps achieve higher scores in human evaluation studies <a class="yt-timestamp" data-t="01:49:35">[01:49:35]</a>.

### Text Encoders
SD3 leverages an ensemble of three pre-trained, frozen text models for text conditioning: Clip G14, Clip L14, and T5 XXL <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>. This ensemble approach generally boosts overall model performance <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>.

To enhance robustness and memory efficiency, SD3 trains with a high dropout rate (46%) on individual text encoders <a class="yt-timestamp" data-t="01:37:53">[01:37:53]</a>. This allows arbitrary subsets of the encoders to be used during inference without significant performance drops <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>. Notably, removing the T5 XXL encoder primarily impacts the model's ability to generate correctly spelled text, while having limited effect on aesthetic quality ratings <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>. This suggests that different text encoders contribute unique strengths to the generated image's fidelity to the prompt <a class="yt-timestamp" data-t="01:42:10">[01:42:10]</a>.

## Evaluation and State-of-the-Art

SD3's performance is evaluated using quantitative metrics like CLIP scores (measuring text-image similarity) and FID (Fréchet Inception Distance, specifically FCD or F-Clip Distance in this case, assessing image quality and diversity) <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>.

Crucially, SD3 substantiates its state-of-the-art claim with human preference evaluations <a class="yt-timestamp" data-t="01:31:47">[01:31:47]</a>. In A/B comparisons against leading proprietary models like DALL-E 3 and Midjourney V6, SD3 consistently achieves higher win rates, demonstrating its superior aesthetic and quality generation <a class="yt-timestamp" data-t="01:32:18">[01:32:18]</a>. These human-driven assessments, while sometimes based on hard-to-articulate intuitions, are considered the gold standard for evaluating [[diffusion_models_and_image_generation | image generation models]] <a class="yt-timestamp" data-t="01:29:11">[01:29:11]</a>.

## Future Outlook

The scaling trends observed in SD3 show no signs of saturation, indicating that further performance improvements can be achieved by continuing to increase model sizes and leveraging more powerful hardware in the future <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>.

While the paper primarily focuses on image generation, there is a preliminary mention of applying the MMD architecture to video generation, suggesting ongoing efforts in this area <a class="yt-timestamp" data-t="01:12:23">[01:12:23]</a>. It's speculated that while SD3 is state-of-the-art for images, a video counterpart might not yet be competitive with models like Sora <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>.