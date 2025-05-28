---
title: Stable Diffusion 3 Overview
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Stable Diffusion 3 (SD3) is the third and most recent release of Stable Diffusion, a generative image model developed by Stability AI, a startup known for its open-source models [00:02:35]. The paper introducing SD3, "Scaling Rectified Flow [[transformer_architecture_in_diffusion_models | Transformers]] for High-Resolution Image Synthesis," is considered a comprehensive collection and summary of [[neural_network_diffusion_concept | diffusion models]] techniques [00:03:53]. It is 28 pages long and packed with information on training flows, architectures, model parameter space, and data [00:04:01]. Stability AI's decision to publish such detailed papers is highly valued for its transparency [00:07:02].

## Understanding [[neural_network_diffusion_concept | Diffusion Models]] in SD3

[[neural_network_diffusion_concept | Diffusion models]] create data from noise by inverting the forward path of data towards noise [00:07:41]. They take a pure noise distribution and transform it into a data distribution, such as an image [00:07:56]. Each step in this process involves an inference step on a neural network [00:14:36].

### Rectified Flow and Path Optimization

Traditionally, the path from noise to data in high-dimensional image space is often "curved," requiring multiple integration steps [00:13:52]. This "curved path" means the model takes detours in the latent space before reaching the desired final image [01:16:16].

SD3 utilizes "rectified flow," a generative model formulation that aims to connect data and noise in a straight line [00:08:22]. This straight path reduces the number of inference steps needed, directly impacting sampling speed and efficiency by reducing error accumulation [00:14:10]. Rectified flow is the simplest possible form for this transition, and experiments showed it to be the best variant for [[neural_network_diffusion_concept | diffusion models]] [01:56:01].

### Noise Sampling Techniques

During training, [[neural_network_diffusion_concept | diffusion models]] add noise to images and then train the model to predict and remove it [00:33:33]. The specific time step (T) at which noise is added significantly impacts training [00:38:44].

While most [[neural_network_diffusion_concept | diffusion model]] papers use a uniform distribution for sampling T [00:39:00], SD3 employs a "logit normal sampling" strategy [00:40:41]. This method biases the sampling towards intermediate time steps (e.g., between T=0.4 and T=0.6) [00:41:59]. The intuition behind this is that these intermediate steps are where the model needs to work hardest to understand the distribution and learn to predict noise effectively [00:42:15].

The paper conducted extensive ablation studies, testing 24 combinations of flow trajectories (rectified flow, EDM, cosine, LDM linear) and sampling settings (logit normal, logid normal, mode sampling with heavy tails, Coast map) [00:43:51]. Rectified flow with logit normal sampling consistently achieved the best performance across various metrics like CLIP and FID scores [00:48:52]. This experiment offers significant computational savings for future research by identifying the most efficient combination [01:59:04].

## Model Architecture: The Multimodal Diffusion Transformer (MMD)

SD3 introduces a novel [[transformer_architecture_in_diffusion_models | Transformer-based architecture]] called the Multimodal Diffusion Transformer (MMD) [00:09:56]. This architecture builds upon the Diffusion Transformer (DiT) model [00:55:59].

A key innovation in the MMD is its approach to handling different modalities (text and image). Instead of using cross-attention, which is common in other Transformer architectures, MMD concatenates the image tokens (as a sequence of patches) and text tokens into a single sequence [00:59:11]. Self-attention is then performed on this combined sequence, allowing any part of the text to pay attention to any part of the image, and vice-versa [00:59:20]. After the attention operation, the model splits the combined sequence, and separate Multi-Layer Perceptrons (MLPs) are applied to the image and text representations [01:00:09]. This "symmetric design" allows both representations to work in their own space while still accounting for the other modality [00:57:57]. While more computationally expensive due to the longer sequence length, it enables better information flow between modalities [01:02:17].

### Text Encoders and Robustness

SD3 uses an ensemble of three pre-trained, frozen text models to derive text conditioning: CLIP G14, CLIP L14, and T5 XXL [00:55:16]. Ensembles generally offer better performance than single models but require more memory and compute [01:35:59].

To mitigate this, SD3 trains its model with a high dropout rate (46%) for individual text encoders [01:37:54]. This means that during training, the output from a text encoder might be replaced with zeros, making the model robust to the absence of certain encoders during inference [01:38:20]. This allows users with less powerful GPUs to run SD3 with a subset of the text encoders without significant performance drops [01:39:24].

An interesting finding is that removing the T5 XXL text encoder (which has 4.7 billion parameters) has minimal impact on aesthetic quality but significantly affects the model's ability to generate correctly spelled text [01:39:50]. This suggests that T5 XXL contributes a nuanced understanding of token relationships crucial for spelling and precise positional understanding (e.g., "ferret in the jar" vs. "ferret near the jar") [01:42:58].

## Scaling and Training Techniques

SD3 parameterizes model size using a single variable, 'D', which determines the model's depth (number of attention blocks), hidden size, and number of attention heads [01:08:10]. This simplified parameterization allows for cleaner [[scaling_and_training_techniques_for_diffusion_models | scaling studies]], showing that larger models (higher 'D' values) consistently achieve lower validation loss and better performance [01:10:50].

Other [[scaling_and_training_techniques_for_diffusion_models | training and implementation details of Transformer-based diffusion models]] include:
*   **Latent Space Autoencoder** [[training_and_implementation_details_of_transformerbased_diffusion_models | Training and implementation details of Transformer-based diffusion models]]: The model operates in the latent space of a pre-trained autoencoder [01:17:56]. Increasing the channel dimension of this latent space (e.g., from 4 to 8 to 16) improves the reconstruction quality of the autoencoder, thus enhancing the overall image quality of the [[neural_network_diffusion_concept | diffusion model]] [01:19:46].
*   **Mixed Precision Training** [[training_and_implementation_details_of_transformerbased_diffusion_models | Training and implementation details of Transformer-based diffusion models]]: To improve efficiency and allow for larger models, SD3 uses mixed precision training (bf16) [01:25:01]. Normalizing the Query (Q) and Key (K) vectors before the attention operation (QK normalization) prevents instability and divergence during high-resolution training [01:25:56].
*   **Varying Aspect Ratios** [[training_and_implementation_details_of_transformerbased_diffusion_models | Training and implementation details of Transformer-based diffusion models]]: SD3 trains on a mix of different image resolutions and aspect ratios (e.g., cellphone, desktop) [01:27:03]. It uses 2D frequency embeddings and adapts them through interpolation to maintain consistency across resolutions [01:27:50].
*   **Resolution-Dependent Time Step Shifting** [[training_and_implementation_details_of_transformerbased_diffusion_models | Training and implementation details of Transformer-based diffusion models]]: The time step schedule (how 'T' values are sampled) is adjusted based on image resolution using a "shift value" (Alpha) [01:28:20]. Human evaluations were used to determine the optimal shift value, indicating a reliance on subjective human preference for certain hyperparameters [01:29:09].
*   **Data Curation**: The model trains on large datasets like CC12M and ImageNet [01:15:14]. Stability AI augments human-generated captions with synthetic annotations created by a Vision Language Model (Cog VLM) to enrich the descriptive detail [01:16:11]. They also deduplicate their datasets to prevent overfitting to specific images and ensure a diverse representation of visual concepts [01:50:12].
*   **Direct Preference Optimization (DPO)**: SD3 employs a three-stage training pipeline: pre-training, fine-tuning at higher resolutions, and finally, Direct Preference Optimization (DPO) [01:45:26]. DPO aligns the model's output with human aesthetic preferences, even if it means subtly shifting away from the true data distribution [01:48:59]. This stage helps generate images that are visually pleasing and cinematic, contributing to high human preference scores [01:49:08].

## Performance and Comparisons

SD3 claims state-of-the-art performance in image generation [00:03:36]. This claim is substantiated through human evaluations, where people blindly compare images generated by different models based on representativeness, quality, and aesthetic appeal [00:52:23].

SD3 outperforms competitors like Midjourney V6, DALL-E 3, and its predecessor SDXL in human preference evaluations, achieving a win rate above 50% [01:31:50]. The scaling trend shows no sign of saturation, suggesting that future improvements are possible with larger models and more computational resources [01:45:01].

### Potential for Video Generation

Stability AI is also exploring the application of MMD to video generation, similar to OpenAI's Sora and Google's Lumiere [01:12:27]. While not a central focus of this paper, preliminary [[challenges_in_3d_model_generation_using_diffusion_models | scaling studies]] on videos were conducted by collapsing the temporal dimension into the batch access [01:12:41].# Stable Diffusion 3 Overview

Stable Diffusion 3 (SD3) is the third and most recent release of Stable Diffusion, a generative image model developed by Stability AI, a startup known for its open-source models [00:02:35]. The paper introducing SD3, "Scaling Rectified Flow [[transformer_architecture_in_diffusion_models | Transformers]] for High-Resolution Image Synthesis," is considered a comprehensive collection and summary of [[neural_network_diffusion_concept | diffusion models]] techniques [00:03:53]. It is 28 pages long and packed with information on training flows, architectures, model parameter space, and data [00:04:01]. Stability AI's decision to publish such detailed papers is highly valued for its transparency [00:07:02].

## Understanding [[neural_network_diffusion_concept | Diffusion Models]] in SD3

[[neural_network_diffusion_concept | Diffusion models]] create data from noise by inverting the forward path of data towards noise [00:07:41]. They take a pure noise distribution and transform it into a data distribution, such as an image [00:07:56]. Each step in this process involves an inference step on a neural network [00:14:36].

### Rectified Flow and Path Optimization

Traditionally, the path from noise to data in high-dimensional image space is often "curved," requiring multiple integration steps [00:13:52]. This "curved path" means the model takes detours in the latent space before reaching the desired final image [01:16:16].

SD3 utilizes "rectified flow," a generative model formulation that aims to connect data and noise in a straight line [00:08:22]. This straight path reduces the number of inference steps needed, directly impacting sampling speed and efficiency by reducing error accumulation [00:14:10]. Rectified flow is the simplest possible form for this transition, and experiments showed it to be the best variant for [[neural_network_diffusion_concept | diffusion models]] [01:56:01].

### Noise Sampling Techniques

During training, [[neural_network_diffusion_concept | diffusion models]] add noise to images and then train the model to predict and remove it [00:33:33]. The specific time step (T) at which noise is added significantly impacts training [00:38:44].

While most [[neural_network_diffusion_concept | diffusion model]] papers use a uniform distribution for sampling T [00:39:00], SD3 employs a "logit normal sampling" strategy [00:40:41]. This method biases the sampling towards intermediate time steps (e.g., between T=0.4 and T=0.6) [00:41:59]. The intuition behind this is that these intermediate steps are where the model needs to work hardest to understand the distribution and learn to predict noise effectively [00:42:15].

The paper conducted extensive ablation studies, testing 24 combinations of flow trajectories (rectified flow, EDM, cosine, LDM linear) and sampling settings (logit normal, logid normal, mode sampling with heavy tails, Coast map) [00:43:51]. Rectified flow with logit normal sampling consistently achieved the best performance across various metrics like CLIP and FID scores [00:48:52]. This experiment offers significant computational savings for future research by identifying the most efficient combination [01:59:04].

## Model Architecture: The Multimodal Diffusion Transformer (MMD)

SD3 introduces a novel [[transformer_architecture_in_diffusion_models | Transformer-based architecture]] called the Multimodal Diffusion Transformer (MMD) [00:09:56]. This architecture builds upon the Diffusion Transformer (DiT) model [00:55:59].

A key innovation in the MMD is its approach to handling different modalities (text and image). Instead of using cross-attention, which is common in other Transformer architectures, MMD concatenates the image tokens (as a sequence of patches) and text tokens into a single sequence [00:59:11]. Self-attention is then performed on this combined sequence, allowing any part of the text to pay attention to any part of the image, and vice-versa [00:59:20]. After the attention operation, the model splits the combined sequence, and separate Multi-Layer Perceptrons (MLPs) are applied to the image and text representations [01:00:09]. This "symmetric design" allows both representations to work in their own space while still accounting for the other modality [00:57:57]. While more computationally expensive due to the longer sequence length, it enables better information flow between modalities [01:02:17].

### Text Encoders and Robustness

SD3 uses an ensemble of three pre-trained, frozen text models to derive text conditioning: CLIP G14, CLIP L14, and T5 XXL [00:55:16]. Ensembles generally offer better performance than single models but require more memory and compute [01:35:59].

To mitigate this, SD3 trains its model with a high dropout rate (46%) for individual text encoders [01:37:54]. This means that during training, the output from a text encoder might be replaced with zeros, making the model robust to the absence of certain encoders during inference [01:38:20]. This allows users with less powerful GPUs to run SD3 with a subset of the text encoders without significant performance drops [01:39:24].

An interesting finding is that removing the T5 XXL text encoder (which has 4.7 billion parameters) has minimal impact on aesthetic quality but significantly affects the model's ability to generate correctly spelled text [01:39:50]. This suggests that T5 XXL contributes a nuanced understanding of token relationships crucial for spelling and precise positional understanding (e.g., "ferret in the jar" vs. "ferret near the jar") [01:42:58].

## [[scaling_and_training_techniques_for_diffusion_models | Scaling and Training Techniques for Diffusion Models]]

SD3 parameterizes model size using a single variable, 'D', which determines the model's depth (number of attention blocks), hidden size, and number of attention heads [01:08:10]. This simplified parameterization allows for cleaner [[scaling_and_training_techniques_for_diffusion_models | scaling studies]], showing that larger models (higher 'D' values) consistently achieve lower validation loss and better performance [01:10:50].

Other [[training_and_implementation_details_of_transformerbased_diffusion_models | training and implementation details of Transformer-based diffusion models]] include:
*   **Latent Space Autoencoder**: The model operates in the latent space of a pre-trained autoencoder [01:17:56]. Increasing the channel dimension of this latent space (e.g., from 4 to 8 to 16) improves the reconstruction quality of the autoencoder, thus enhancing the overall image quality of the [[neural_network_diffusion_concept | diffusion model]] [01:19:46].
*   **Mixed Precision Training**: To improve efficiency and allow for larger models, SD3 uses mixed precision training (bf16) [01:25:01]. Normalizing the Query (Q) and Key (K) vectors before the attention operation (QK normalization) prevents instability and divergence during high-resolution training [01:25:56].
*   **Varying Aspect Ratios**: SD3 trains on a mix of different image resolutions and aspect ratios (e.g., cellphone, desktop) [01:27:03]. It uses 2D frequency embeddings and adapts them through interpolation to maintain consistency across resolutions [01:27:50].
*   **Resolution-Dependent Time Step Shifting**: The time step schedule (how 'T' values are sampled) is adjusted based on image resolution using a "shift value" (Alpha) [01:28:20]. Human evaluations were used to determine the optimal shift value, indicating a reliance on subjective human preference for certain hyperparameters [01:29:09].
*   **Data Curation**: The model trains on large datasets like CC12M and ImageNet [01:15:14]. Stability AI augments human-generated captions with synthetic annotations created by a Vision Language Model (Cog VLM) to enrich the descriptive detail [01:16:11]. They also deduplicate their datasets to prevent overfitting to specific images and ensure a diverse representation of visual concepts [01:50:12].
*   **Direct Preference Optimization (DPO)**: SD3 employs a three-stage training pipeline: pre-training, fine-tuning at higher resolutions, and finally, Direct Preference Optimization (DPO) [01:45:26]. DPO aligns the model's output with human aesthetic preferences, even if it means subtly shifting away from the true data distribution [01:48:59]. This stage helps generate images that are visually pleasing and cinematic, contributing to high human preference scores [01:49:08].

## Performance and [[comparisons_with_diffusion_models | Comparisons with Diffusion Models]]

SD3 claims state-of-the-art performance in image generation [00:03:36]. This claim is substantiated through human evaluations, where people blindly compare images generated by different models based on representativeness, quality, and aesthetic appeal [00:52:23].

SD3 outperforms competitors like Midjourney V6, DALL-E 3, and its predecessor SDXL in human preference evaluations, achieving a win rate above 50% [01:31:50]. The scaling trend shows no sign of saturation, suggesting that future improvements are possible with larger models and more computational resources [01:45:01].

### Potential for Video Generation

Stability AI is also exploring the application of MMD to video generation, similar to OpenAI's Sora and Google's Lumiere [01:12:27]. While not a central focus of this paper, preliminary [[challenges_in_3d_model_generation_using_diffusion_models | scaling studies]] on videos were conducted by collapsing the temporal dimension into the batch access [01:12:41].