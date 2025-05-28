---
title: Text to image generation with diffusion Transformers
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Stable Diffusion 3 (SD3) is the third and most recent release of Stable Diffusion, a [[diffusion_models_and_image_generation | generative image model]] developed by Stability AI <a class="yt-timestamp" data-t="02:35:01">[02:35:01]</a>. Stability AI is a startup known for creating open-source models, particularly in image generation <a class="yt-timestamp" data-t="02:52:50">[02:52:50]</a>. This release is considered highly significant, potentially being one of the most comprehensive [[diffusion_models_and_image_generation | diffusion model]] papers due to its detailed exploration of various training flows, architectures, data considerations, and extensive parameter sweeps <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

SD3 is claimed to be the current state-of-the-art [[diffusion_models_and_image_generation | image model]] based on robust human evaluations <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. While the field of image generation is reaching the top of its S-curve, where performance improvements between successive versions are becoming smaller, SD3 demonstrates near-indistinguishable quality from reality across various styles, including fantasy, anime, and cinematic <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.

Stability AI is lauded for its commitment to open science, publishing detailed papers like this that reveal intricate technical details, unlike other companies such as Midjourney or OpenAI <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.

## Core Concepts of Diffusion Models

[[diffusion_models_and_image_generation | Diffusion models]] operate by creating data from noise, inverting a forward path where data gradually becomes noise <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>. They transform a pure noise distribution (e.g., pixel noise) into a target data distribution (e.g., images) <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>. This process involves multiple inference steps, where each step requires running a neural network on a GPU <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>. The generated data points are novel, not just copies from the training set, but follow the distribution of the training data <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

Most [[diffusion_models_and_image_generation | diffusion models]] follow a "curved path" in the high-dimensional image space, moving through intermediate states (e.g., a cat changing color before settling on the desired gray) <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.

## Key Innovations in Stable Diffusion 3

### Rectified Flow

A significant advancement in SD3 is the adoption of Rectified Flow, a generative model formulation that connects data and noise in a straight line <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. This straight path is more efficient, requiring fewer integration steps to simulate the process and reducing error accumulation, which directly impacts sampling speed <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>.

The paper formalizes the problem of [[diffusion_models_and_image_generation | diffusion models]] by defining a loss function that unifies various existing approaches (EDM, Cosine, LDM Linear) as different variants <a class="yt-timestamp" data-t="34:32:00">[34:32:00]</a>. Through extensive experimentation, Stability AI determined that Rectified Flow, the simplest formulation (a simple linear interpolation between noise and data), consistently outperforms other methods <a class="yt-timestamp" data-t="36:40:00">[36:40:00]</a>.

### Tailored SNR Samplers

Another innovation involves improving noise sampling techniques for training rectified flow models by biasing them towards perceptually relevant scales <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. Instead of uniformly sampling time steps (T) between 0 (image) and 1 (pure noise), SD3 employs **logit normal sampling** <a class="yt-timestamp" data-t="40:41:00">[40:41:00]</a>. This method prioritizes sampling T values in the middle of the range (e.g., between 0.4 and 0.6) <a class="yt-timestamp" data-t="44:55:00">[44:55:00]</a>. The intuition behind this is that intermediate steps are crucial for the model to learn to effectively remove or predict noise, as these are the most challenging transformations between noise and data <a class="yt-timestamp" data-t="42:22:00">[42:22:00]</a>.

Experimental results show that the combination of Rectified Flow with logit normal sampling ("RF log Norm") consistently achieves the best performance across various metrics, outperforming other combinations <a class="yt-timestamp" data-t="48:52:00">[48:52:00]</a>. This empirical finding saves future researchers and developers significant computational resources, as they no longer need to perform this ablation study themselves <a class="yt-timestamp" data-t="01:59:04">[01:59:04]</a>.

### Multimodal Diffusion Transformer (MMD) Architecture

SD3 introduces a novel [[Diffusion models and Transformers | Transformer-based architecture]] for [[text_to_image_diffusion_models | text to image generation]] called the Multimodal Diffusion Transformer (MMD) <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>. This architecture is a variant of the Diffusion Transformer (DiT) architecture, which is believed to be behind models like Sora and Lumiere <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.

The MMD architecture uses separate sets of weights for the image and text modalities, effectively having two independent Transformers for each modality <a class="yt-timestamp" data-t="56:38:00">[56:38:00]</a>. Crucially, instead of using cross-attention, the MMD concatenates the image and text sequences (after patch encoding and adding positional embeddings) and then performs a self-attention operation across the combined sequence <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>. This allows any part of the text sequence to pay attention to any part of the image sequence, and vice versa, facilitating richer information flow <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>. After the shared attention, the sequences are separated again, and a distinct Multi-Layer Perceptron (MLP) is applied to each modality <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>. While computationally more expensive due to the larger sequence length for attention, this design enables better interaction between modalities <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>.

### Scalability and Autoencoder Latent Space

SD3 parameterizes the model size using a single variable, `D`, which simultaneously controls the model's depth (number of attention blocks), hidden size (width), and number of attention heads <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>. This simplified parameterization allows for cleaner [[scalability_of_transformerbased_diffusion_models | scaling studies]] <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. The results show a clear scaling law: the larger the model (higher `D`), the better its performance, with validation loss decreasing consistently <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>. This suggests that performance improvements can continue by simply increasing model size as computational resources (GPUs) become more powerful <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>.

The model operates in the latent space of a pre-trained autoencoder for efficiency <a class="yt-timestamp" data-t="01:17:55">[01:17:55]</a>. The reconstruction quality of this autoencoder sets an upper bound on the achievable image quality <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>. Increasing the number of latent channels (also denoted as `D` in the context of the autoencoder) significantly boosts reconstruction performance and, consequently, overall image quality <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a>. This further reinforces the "bigger is better" scaling trend <a class="yt-timestamp" data-t="01:21:55">[01:21:55]</a>.

## Training and Data Enhancements

### Ensemble of Text Encoders

SD3 utilizes an [[ensemble_of_text_encoders_in_diffusion_models | ensemble of text encoders]] for conditioning, specifically Clip G14, Clip L14, and T5 XXL <a class="yt-timestamp" data-t="01:54:40">[01:54:40]</a>. The quality of the text encoder is critical for the final image quality <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

To make the model robust and flexible for inference, they train with a high individual dropout rate (46%) for each text encoder <a class="yt-timestamp" data-t="01:37:54">[01:37:54]</a>. This allows arbitrary subsets of the encoders to be used at inference time, meaning users can opt for a smaller memory footprint by using only one or two encoders without significant performance drops <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>.

A notable finding is that removing the T5 XXL text encoder (which is very large) primarily impacts the model's ability to spell text correctly in images, while having limited effect on aesthetic quality or prompt adherence <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>. This suggests that different text encoders contribute unique capabilities to the overall model <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a>.

### Data Augmentation and Filtering

SD3 uses large datasets like CC12M and ImageNet for training <a class="yt-timestamp" data-t="01:15:14">[01:15:14]</a>. Recognizing the limitations of human-generated captions (often overly focused on subjects, omitting background details) <a class="yt-timestamp" data-t="01:16:04">[01:16:04]</a>, they augment captions using a pre-trained Vision Language Model (Cog VLM) to create synthetic annotations <a class="yt-timestamp" data-t="01:16:18">[01:16:18]</a>. They use a 50/50 mix of original and synthetic captions <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.

The training data is also meticulously deduplicated to prevent overfitting to specific, frequently occurring images <a class="yt-timestamp" data-t="01:50:11">[01:50:11]</a>. This involves embedding images and using similarity search (e.g., Faiss) to identify and remove near-duplicates, ensuring a diverse representation of visual concepts <a class="yt-timestamp" data-t="01:50:27">[01:50:27]</a>.

### Optimization and Alignment

The training pipeline for SD3 involves three stages:
1.  **Pre-training** at a small image resolution (e.g., 256x256) <a class="yt-timestamp" data-t="01:24:31">[01:24:31]</a>.
2.  **Fine-tuning** at a higher resolution <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
3.  **Direct Preference Optimization (DPO)**: A final alignment stage using human preference data (e.g., "party prompts" dataset) <a class="yt-timestamp" data-t="01:45:26">[01:45:26]</a>. This DPO step enhances the aesthetic appeal of generated images, even with simple captions, by fine-tuning specific low-rank adaptation (LoRA) matrices <a class="yt-timestamp" data-t="01:46:16">[01:46:16]</a>. This means the model learns to generate images that humans find more visually pleasing, even if it slightly deviates from perfectly matching the raw data distribution <a class="yt-timestamp" data-t="01:48:59">[01:48:59]</a>.

Other technical tricks include:
*   **QK normalization**: Normalizing the Query (Q) and Key (K) vectors in the attention mechanism to prevent instability during mixed-precision training (e.g., bf16) at high resolutions <a class="yt-timestamp" data-t="01:25:56">[01:25:56]</a>.
*   **Positional encodings for varying aspect ratios**: Adapting 2D frequency embeddings via interpolation to handle mixed resolutions and aspect ratios (e.g., phone vs. desktop resolutions), allowing generation of non-square images <a class="yt-timestamp" data-t="01:27:03">[01:27:03]</a>.
*   **Resolution-dependent shifting of time step schedules**: Adjusting the time step sampling based on image resolution, with optimal shift values determined by human preference evaluations <a class="yt-timestamp" data-t="01:28:21">[01:28:21]</a>.

## Performance and Evaluation

SD3's performance is rigorously evaluated using quantitative metrics like CLIP score and FID (Fréchet Inception Distance, specifically calculated on CLIP features) <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>, where lower scores indicate better quality <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

Crucially, SD3 undergoes extensive human evaluation, considered the "gold standard" for assessing image generation quality <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. In blind A/B comparisons against competitors like DALL-E 3, Midjourney V6, and SDXL, SD3 consistently achieves higher win rates, demonstrating its state-of-the-art status <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

## Future Outlook

The [[scalability_of_transformerbased_diffusion_models | scaling trend]] observed in SD3 shows "no sign of saturation" <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>. This optimistic outlook suggests that with continued increases in computational power, future [[text_to_image_diffusion_models | text to image diffusion models]] can achieve even greater performance <a class="yt-timestamp" data-t="02:05:46">[02:05:46]</a>. While the current paper primarily focuses on image generation, Stability AI has also conducted preliminary [[techniques_for_text_to_3d_conversion_involving_diffusion_models | scaling studies of MMD on videos]] <a class="yt-timestamp" data-t="01:12:27">[01:12:27]</a>, indicating potential future releases in video generation.