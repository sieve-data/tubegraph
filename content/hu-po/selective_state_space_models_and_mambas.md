---
title: Selective State Space Models and Mambas
videoId: 9s-9aSobky8
---

From: [[hu-po]] <br/> 

[[Mamba models and their applications | Mamba models]], formally known as Selective State Space Models (SSMs), are a class of efficient neural network architectures gaining prominence in various AI domains <a class="yt-timestamp" data-t="01:47:41">[01:47:41]</a>. Their primary advantage lies in their linear computational complexity with respect to sequence length, offering significant speed and memory efficiency benefits compared to traditional Transformer models, which exhibit quadratic complexity <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.

## Understanding State Space Models (SSMs)

A State Space Model (SSM) is a linear time-invariant system of equations designed to capture the dynamics of a system's state variables <a class="yt-timestamp" data-t="01:10:15">[01:10:15]</a>. They operate by processing sequences of data, maintaining a hidden state (memory) that is updated sequentially <a class="yt-timestamp" data-t="01:11:42">[01:11:42]</a>.

The fundamental equation for an SSM involves matrices A, B, and C <a class="yt-timestamp" data-t="01:12:25">[01:12:25]</a>. The "selective" aspect, a key contribution of the original Mamba paper, makes the B, C, and Delta (sampling period for continuous-to-discrete conversion) parameters dependent on the input <a class="yt-timestamp" data-t="01:13:21">[01:13:21]</a>. This input-dependent dynamic allows Mambas to selectively weigh or filter information from the input, akin to how attention mechanisms operate in Transformers by selecting relevant values <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>.

### SSMs vs. Transformers

The core [[state_space_models_vs_attentionbased_models | difference between SSMs and Transformers]] lies in their computational scaling with sequence length:
*   **Transformers** perform attention computations over the entire input sequence, leading to a quadratic increase in computational cost and memory footprint as the sequence length grows <a class="yt-timestamp" data-t="01:16:08">[01:16:08]</a>.
*   **SSMs** maintain a hidden state (memory) of a constant size, regardless of the input sequence length <a class="yt-timestamp" data-t="01:16:28">[01:16:28]</a>. This results in [[efficiency_and_performance_of_mamba_models_in_ai | linear growth]] in computation and memory with respect to the input sequence size <a class="yt-timestamp" data-t="01:16:50">[01:16:50]</a>.

While SSMs share conceptual similarities with older recurrent neural networks (RNNs) and LSTMs in carrying a fixed-size hidden state forward, their modern implementation allows for significantly more efficient training on GPUs, behaving almost like convolutional networks <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. This efficiency is why [[efficiency_and_performance_of_mamba_models_in_ai | Selective State Space Models]] are gaining popularity <a class="yt-timestamp" data-t="01:33:30">[01:33:30]</a>.

## Applications of Mamba Models

Mamba models are being explored across various modalities and problem spaces, often in [[hybrid_architectures_with_transformers_and_mambas | hybrid architectures]] that combine them with elements of Transformers.

### Gamba: Mambas for 3D Reconstruction

Gamba is a model that leverages Mambas for single-view 3D reconstruction, generating a three-dimensional representation (specifically, a Gaussian Splat) from a single input image <a class="yt-timestamp" data-t="02:51:53">[02:51:53]</a>.
*   **Process**: An image is fed into an image tokenizer (Dino V2, a Vision Transformer), producing image tokens <a class="yt-timestamp" data-t="02:25:03">[02:25:03]</a>. These tokens, along with camera parameters and learnable 3D Gaussian Splat tokens, are processed by a Mamba-based sequential network (the "Gamba model") to output 3D Gaussians <a class="yt-timestamp" data-t="02:49:10">[02:49:10]</a>.
*   **Architecture**: The Gamba model itself is a [[hybrid_architectures_with_transformers_and_mambas | combination of Transformers and Mambas]], as the initial image tokenizer is a Vision Transformer <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   **Performance**: While not state-of-the-art, Gamba demonstrates the feasibility of using Mambas for this task, achieving reconstruction in about 6 seconds on an Nvidia A100 GPU <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>. The paper acknowledges that results are "not that amazing" due to training on a smaller dataset <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>.
*   **Limitations**: The use of a Vision Transformer for image encoding is noted as a drawback, as it prevents the entire model from being Mamba-based <a class="yt-timestamp" data-t="02:22:50">[02:22:50]</a>. Additionally, the model's reliance on camera pose tokens might limit its real-world applicability outside of simulated environments <a class="yt-timestamp" data-t="02:43:08">[02:43:08]</a>. The paper also incorrectly states Mamba's unidirectional scan order, as multiple scan directions are possible <a class="yt-timestamp" data-t="02:13:13">[02:13:13]</a>.

### Cobra: Mambas in Vision-Language Models (VLMs)

Cobra extends Mambas to [[mamba_models_in_vision_language_and_multimodal_models | multimodal large language models]] (MLLMs or VLMs) for efficient inference <a class="yt-timestamp" data-t="02:23:05">[02:23:05]</a>. These models consume both image and text tokens to answer questions <a class="yt-timestamp" data-t="02:29:16">[02:29:16]</a>.
*   **Architecture**: Cobra primarily uses a Mamba-based language model (64 Mamba blocks) as its backbone <a class="yt-timestamp" data-t="02:36:35">[02:36:35]</a>. Similar to Gamba, it relies on pre-trained Vision Transformers (Dino and SigLip) for image encoding, which is a point of critique <a class="yt-timestamp" data-t="02:46:50">[02:46:50]</a>.
*   **Performance**: Cobra achieves competitive performance compared to other computationally efficient VLMs like LLaVA, while significantly reducing parameter count and increasing inference speed <a class="yt-timestamp" data-t="02:52:50">[02:52:50]</a>. It reaches 166 tokens per second, notably faster than Transformer-based models like MobileVLM Tiny (39 tokens/second) <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This speed makes it promising for [[mamba_models_and_their_applications | time-sensitive applications]] like visual-based robotic feedback control <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   **Training**: Cobra simplifies the training process by directly fine-tuning the entire VLM backbone and projector simultaneously, discarding the multi-stage pre-alignment phase seen in earlier VLM training paradigms <a class="yt-timestamp" data-t="02:39:13">[02:39:13]</a>.

### Jamba: A Hybrid Language Model

Jamba is an open-source language model developed by AI21 Labs that employs a [[hybrid_architectures_with_transformers_and_mambas | hybrid architecture]], combining Mamba blocks, Transformer blocks, and Mamba blocks with Mixture-of-Experts (MoE) <a class="yt-timestamp" data-t="03:50:01">[03:50:01]</a>.
*   **Architecture**: The model alternates between standard Mamba layers, Transformer layers, and Mamba + MoE layers <a class="yt-timestamp" data-t="03:54:15">[03:54:15]</a>. MoE layers use a router to select specific experts (MLPs) based on the input tokens, allowing the model to have a large total number of parameters (52 billion) while only activating a subset (e.g., 12 billion) during inference <a class="yt-timestamp" data-t="03:53:07">[03:53:07]</a>.
*   **Performance**: Jamba demonstrates competitive performance against other open-source models like Mixtral, Gemma, and Llama, sometimes slightly outperforming them on reasoning benchmarks <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.
*   **Advantages**: Its linear complexity allows for a large context window, supporting up to 140,000 tokens <a class="yt-timestamp" data-t="04:02:41">[04:02:41]</a>. Jamba is also specifically optimized for Nvidia A100 80GB GPUs <a class="yt-timestamp" data-t="04:06:37">[04:06:37]</a>.

## Challenges and Future Outlook

Despite the promising [[efficiency_and_performance_of_mamba_models_in_ai | efficiency and performance]] of Mamba models, particularly in [[mamba_models_and_their_applications | time-sensitive applications]], they face potential challenges:
*   **Hybrid Dependence**: Current applications like Gamba and Cobra still rely on Vision Transformers for initial image encoding, preventing an end-to-end Mamba architecture <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. Developing a purely Mamba-based image encoder is a recognized area for future work <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
*   **Quantization Limitations**: A significant potential "Achilles heel" for Mambas is their apparent difficulty in being quantized to very low precision <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. Both Cobra and Jamba indicate that Mamba blocks need to maintain relatively high precision (no lower than bf16 for Cobra, and Mamba blocks should be excluded from 8-bit quantization for Jamba) to avoid degrading model quality <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. This contrasts with Transformers, where significant progress has been made in achieving high performance with extremely quantized weights (e.g., 1.58 bits) <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. If Mambas cannot be effectively quantized, it could limit their memory and speed advantages, potentially favoring highly quantized Transformers in resource-constrained environments <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. This is an open area for research <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.

The widespread adoption of Nvidia A100 GPUs as a standard for AI development underscores the demand for efficient models <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>. Mambas' inherent efficiency makes them a strong contender for future AI models, especially if the quantization challenges can be overcome.