---
title: Stable Diffusion 3 release and features
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Stable Diffusion 3 (SD3) is the third and most recent release of the Stable Diffusion generative image model <a class="yt-timestamp" data-t="02:35:01">[02:35:01]</a>. It is a generative image model created by Stability AI, a startup primarily known for its open-source models <a class="yt-timestamp" data-t="02:46:01">[02:46:01]</a>. The paper introducing SD3, titled "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis," is considered a comprehensive collection and summary of diffusion models <a class="yt-timestamp" data-t="03:53:01">[03:53:01]</a>. It covers various aspects including training flows, architectures, model parameter space, and data considerations <a class="yt-timestamp" data-t="04:01:01">[04:01:01]</a>. Stability AI's commitment to publishing such detailed papers, in contrast to other companies like Midjourney or OpenAI, is highly valued for its transparency and contribution to the community <a class="yt-timestamp" data-t="07:02:01">[07:02:01]</a>.

## Core Diffusion Model Concepts

### Functionality
[[differences_between_Diffusion_Models_and_Consistency_Models | Diffusion models]] create data from noise by inverting the forward path of data towards noise <a class="yt-timestamp" data-t="07:41:01">[07:41:01]</a>. They effectively transform a pure noise distribution into a target data distribution, such as images <a class="yt-timestamp" data-t="07:56:01">[07:56:01]</a>.

### Rectified Flow
Rectified Flow is a generative model formulation that connects data and noise in a straight line <a class="yt-timestamp" data-t="08:22:01">[08:22:01]</a>. Unlike traditional diffusion processes that might take "curved paths" involving many intermediate integration steps, a straight path can be simulated with a single step, reducing computation and error accumulation <a class="yt-timestamp" data-t="14:05:01">[14:05:01]</a>. This efficiency directly impacts sampling speed <a class="yt-timestamp" data-t="14:20:01">[14:20:01]</a>. In SD3, rectified flow defines the forward process as a straight path between the data distribution and the standard normal distribution <a class="yt-timestamp" data-t="35:56:01">[35:56:01]</a>. Experiments showed that rectified flow outperforms other formulations like EDM and Cosine, especially when sampling fewer steps <a class="yt-timestamp" data-t="51:19:01">[51:19:01]</a>.

### Noise Sampling Techniques
When training diffusion models, a specific time step `T` is chosen for each image to add noise <a class="yt-timestamp" data-t="38:44:01">[38:44:01]</a>. Most previous diffusion papers commonly used a uniform distribution for selecting `T` <a class="yt-timestamp" data-t="39:00:01">[39:00:01]</a>. However, SD3 improves this by biasing `T` towards perceptually relevant scales using a logit normal distribution <a class="yt-timestamp" data-t="38:38:01">[38:38:01]</a>. This means intermediate time steps (around `T=0.4` to `T=0.6`) are sampled more frequently, as these are considered more crucial for learning the noise removal process <a class="yt-timestamp" data-t="41:59:01">[41:59:01]</a>.

### Loss Function
The model's training aims to predict noise rather than directly matching the flow vector field, making the objective more tractable <a class="yt-timestamp" data-t="33:04:01">[33:04:01]</a>. The choice of flow trajectory and time step sampler are key hyperparameters. Through comprehensive ablation studies, SD3 demonstrates that the combination of rectified flow with logit normal sampling consistently achieves the best performance across various metrics <a class="yt-timestamp" data-t="48:52:01">[48:52:01]</a>.

## Architecture: Multimodal Diffusion Transformer (MMD)

SD3 introduces a novel [[diffusion_models_and_Transformers | Transformer]]-based architecture for text-to-image generation called the Multimodal Diffusion Transformer (MMD) <a class="yt-timestamp" data-t="08:56:01">[08:56:01]</a>.

### Key Features
*   **Separate Weights for Modalities**: The MMD architecture uses separate sets of weights for the image and text modalities, effectively creating two independent Transformers <a class="yt-timestamp" data-t="56:38:01">[56:38:01]</a>.
*   **Concatenated Attention**: Unlike other [[latent_diffusion_models_and_architectures | diffusion models]] that use cross-attention, MMD concatenates the image tokens and text tokens into a single sequence <a class="yt-timestamp" data-t="59:09:01">[59:09:01]</a>. It then performs self-attention over this combined sequence, allowing any part of the text to pay attention to any part of the image, and vice-versa <a class="yt-timestamp" data-t="59:30:01">[59:30:01]</a>. After the attention operation, the modalities are separated for their respective Multi-Layer Perceptrons (MLPs) <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>. This design, while more computationally expensive due to the longer sequence length, allows for richer interaction between modalities <a class="yt-timestamp" data-t="01:02:17">[01:02:17]</a>.
*   **Basis on Dit**: The MMD builds upon the [[diffusion_models_and_Transformers | Diffusion Transformer]] (Dit) architecture <a class="yt-timestamp" data-t="55:59:01">[55:59:01]</a>.

### [[scaling_and_optimization_in_diffusion_models | Scaling and Optimization]]
The model's size is parameterized by a single variable, `D`, representing its depth (number of attention blocks) <a class="yt-timestamp" data-t="01:12:01">[01:12:01]</a>. This `D` also proportionally determines the hidden size (width) and number of attention heads, simplifying [[scaling_and_optimization_in_diffusion_models | scaling and optimization]] studies <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>. [[scaling_and_optimization_in_diffusion_models | Scaling]] studies show that larger `D` values (larger models) consistently lead to lower validation loss and improved performance <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>. This suggests that performance improvements can continue by simply increasing model size as computational resources allow <a class="yt-timestamp" data-t="01:14:59">[01:14:59]</a>.

> [!NOTE] D parameter
> The parameter `D` is used for both the model's depth and the number of latent channels, which can be confusing <a class="yt-timestamp" data-t="01:19:50">[01:19:50]</a>. Increasing the number of [[latent_diffusion_models_and_architectures | latent diffusion models and architectures | latent channels]] (e.g., from 4 to 16) also significantly boosts the reconstruction performance of the autoencoder, leading to higher image quality <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a>. This suggests that future improvements can also come from larger GPUs enabling larger latent dimensions <a class="yt-timestamp" data-t="01:21:18">[01:21:18]</a>.

## Training Data and Practices

SD3 is primarily trained on datasets like CC12M and ImageNet <a class="yt-timestamp" data-t="01:15:18">[01:15:18]</a>.
*   **Caption Augmentation**: To overcome the limitations of human-generated captions (which often omit background or composition details), SD3 augments its data using an off-the-shelf vision-language model, CogVLM, to create synthetic annotations <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>. The training mixes original captions with synthetic ones, though the paper doesn't explore various mix ratios beyond a 50/50 blend <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>.
*   **Data Deduplication**: The dataset is deduplicated to ensure a diverse representation of visual concepts and prevent overfitting to common images <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>. This involves embedding images and using similarity search to identify and remove duplicates <a class="yt-timestamp" data-t="01:50:16">[01:50:16]</a>.
*   **Mixed Precision Training**: SD3 employs mixed-precision training (specifically `bf16`) for efficiency <a class="yt-timestamp" data-t="01:26:05">[01:26:05]</a>. Normalizing the Query (Q) and Key (K) tensors before the attention operation helps stabilize training at higher resolutions <a class="yt-timestamp" data-t="01:25:56">[01:25:56]</a>.
*   **Resolution-Dependent Shifting**: The time step schedule for noise addition is adjusted based on image resolution, as different resolutions may benefit from different biases in `T` sampling <a class="yt-timestamp" data-t="01:28:21">[01:28:21]</a>.
*   **Pre-computing Embeddings**: Text embeddings from the various text encoders are pre-computed before training. This accelerates the training process by avoiding real-time encoding of captions for each mini-batch <a class="yt-timestamp" data-t="02:03:54">[02:03:54]</a>.

## Text Encoders

SD3 utilizes an ensemble of three pre-trained, frozen text models for conditioning: CLIP G14, CLIP L14, and T5 XXL <a class="yt-timestamp" data-t="01:35:55">[01:35:55]</a>. The quality of the text encoder is crucial for the final image quality <a class="yt-timestamp" data-t="01:35:33">[01:35:33]</a>.

*   **Dropout Strategy**: During training, an individual dropout rate of 46% is applied to the text encoders <a class="yt-timestamp" data-t="01:37:51">[01:37:51]</a>. This means that at any given time, the input from one or more text encoders might be replaced with zeros <a class="yt-timestamp" data-t="01:38:02">[01:38:02]</a>.
*   **Inference Flexibility**: This aggressive dropout makes the model robust to incomplete text encoder inputs during inference <a class="yt-timestamp" data-t="01:39:13">[01:39:13]</a>. Users can choose to use a subset of the encoders (e.g., only the two CLIP models) to reduce memory usage without significant performance drops <a class="yt-timestamp" data-t="01:39:37">[01:39:37]</a>.
*   **T5's Role in Spelling**: Notably, removing the T5 XXL encoder has minimal impact on aesthetic quality but significantly affects the model's ability to generate correctly spelled text <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>. This highlights T5's unique contribution to textual nuance, likely due to its different training objective compared to CLIP <a class="yt-timestamp" data-t="01:42:04">[01:42:04]</a>.

## Performance and Evaluation

SD3 is currently a state-of-the-art image model <a class="yt-timestamp" data-t="03:36:01">[03:36:01]</a>.
*   **Quantitative Metrics**: Performance is evaluated using CLIP (measures text-image alignment) and FID (Fréchet Inception Distance, measures image quality and diversity) scores <a class="yt-timestamp" data-t="01:54:53">[01:54:53]</a>. Smaller FID and higher CLIP (depending on the specific metric) indicate better performance <a class="yt-timestamp" data-t="01:54:57">[01:54:57]</a>.
*   **Human Evaluation**: Stability AI claims state-of-the-art performance based on robust human evaluations <a class="yt-timestamp" data-t="05:25:01">[05:25:01]</a>. In blind A/B comparisons against models like [[differences_between_Diffusion_Models_and_Consistency_Models | DALL-E 3]] and Midjourney V6, SD3 consistently shows a higher win rate <a class="yt-timestamp" data-t="01:31:53">[01:31:53]</a>. This suggests that the model generates images that are more representative of the text prompt, of higher quality, and aesthetically more pleasing <a class="yt-timestamp" data-t="01:45:36">[01:45:36]</a>.
*   **Direct Preference Optimization (DPO)**: SD3 incorporates a three-stage training pipeline: pre-training on low resolution, fine-tuning on higher resolution, and then applying DPO <a class="yt-timestamp" data-t="01:45:30">[01:45:30]</a>. DPO is used as a final alignment step to make generated images more aesthetically pleasing, even with simpler captions <a class="yt-timestamp" data-t="01:46:16">[01:46:16]</a>. This process prioritizes human subjective preferences over strict adherence to the true data distribution <a class="yt-timestamp" data-t="01:48:59">[01:48:59]</a>.

## Future Outlook

The [[scaling_and_optimization_in_diffusion_models | scaling trend]] of SD3 shows no sign of saturation <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>, indicating continued performance improvements are possible with larger models and more powerful GPUs <a class="yt-timestamp" data-t="02:05:44">[02:05:44]</a>. While the paper primarily focuses on image generation, preliminary [[future_potential_of_3D_diffusion_models | scaling studies of 3D diffusion models]] (MMD on videos) were conducted <a class="yt-timestamp" data-t="01:12:27">[01:12:27]</a>, suggesting future potential for video generation from Stability AI <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>.