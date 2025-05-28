---
title: Transformer models and MoEs
videoId: _epq9VsViJc
---

From: [[hu-po]] <br/> 

## Introduction to Mixtures of Experts
[[Transformer models in 3D reconstruction | Transformer]] architectures can scale model capacity without substantial increases in training or inference costs through the use of Mixtures of Experts (MoEs) <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Model capacity refers to the size of a model <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. While larger models typically demand more computational resources and time for training and inference, MoEs offer a way to manage these costs <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Genealogy of MoE Research
The research into Mixtures of Experts has evolved over several years, primarily driven by Google DeepMind <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Pathways (October 2021)**: The earliest version in this research thread <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Sparse Mixture of Experts (2022)**: Introduced techniques for sparsely activating token paths <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This approach is speculated to be used in models like GPT-4 and GPT-3.5 <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>, contributing to their non-deterministic outputs <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>.
*   **Soft Mixture of Experts (August 2023)**: The latest extension, proposing a fully [[differentiability_in_moes | differentiable]] approach to MoEs <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Motivation for MoEs
The core idea behind MoEs stems from the observation that a significant portion of neurons in traditional neural networks, particularly in fully connected layers, are often inactive or contribute very little to the final prediction <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>, <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. By only activating a subset of the model's parameters for a given input, MoEs aim to achieve:
*   **Increased Model Capacity**: Allowing for larger models <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Reduced Computational Cost**: Lower training and inference expenses compared to dense models of similar capacity <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. This efficiency comes from leveraging the inherent sparsity of neural networks, where only a few pathways truly matter <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

## Sparse Mixture of Experts (Sparse MoE)
Sparse MoE architectures replace dense feed-forward network (FFN) layers within a [[transformer_models_in_3d_reconstruction | Transformer]] block with a "mixture of independent FFNs," referred to as experts <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Each expert is a small, independent feed-forward neural network (typically a multi-layer perceptron or MLP) <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>, <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>.

A "router" determines which experts process which input tokens <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This routing is typically a discrete optimization problem <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

### Issues with Sparse MoE
Despite their benefits, Sparse MoEs suffer from several challenges:
*   **Training Instability** <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Token Dropping**: Some input tokens may not be routed to any expert <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>, <a class="yt-timestamp" data-t="00:19:58">[00:19:58]</a>, <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>.
*   **Expert Imbalance**: Some experts receive disproportionately more tokens than others <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>, <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>.
*   **Inability to Scale Number of Experts**: Hard routing can be challenging with many experts <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, <a class="yt-timestamp" data-t="02:01:46">[02:01:46]</a>.
*   **Ineffective Fine-tuning** <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Non-differentiability**: Most sparse MoE approaches use discrete routing mechanisms, making them non-[[differentiability_in_moes | differentiable]] <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>. This complicates training as gradients cannot be smoothly backpropagated through the routing decisions <a class="yt-timestamp" data-t="00:53:54">[00:53:54]</a>.
*   **Batch Effects at Inference**: In sparse MoEs, inputs within a batch can compete for limited expert capacity, leading to non-deterministic outputs because the prediction for one input depends on others in the batch <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>, <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>.

## Soft Mixture of Experts (Soft MoE)
Soft MoE addresses the limitations of Sparse MoE by introducing a "soft assignment" mechanism, replacing the discrete router with weighted combinations of input tokens <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>, <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.

### How Soft MoE Works
Instead of routing tokens to specific experts, Soft MoE passes different weighted combinations of *all* input tokens to *each* expert <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>, <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.
1.  **Input Slots**: Each expert processes a fixed number of "slots" (P) <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.
2.  **Learnable Parameters (Phi)**: Each slot has corresponding learnable parameters (Phi) <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>, <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.
3.  **Dispatch Weights (D)**: Input tokens (X) and the learnable parameters (Phi) are used to compute "dispatch weights" (D) via a [[differentiability_in_moes | softmax]] function <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>, <a class="yt-timestamp" data-t="00:37:39">[00:37:39]</a>. These weights determine the convex combination of all input tokens for each slot <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.
4.  **Expert Processing**: The weighted token combinations are fed into the experts (FFNs) <a class="yt-timestamp" data-t="00:47:44">[00:47:44]</a>.
5.  **Combined Weights (C)**: The outputs from all expert slots are then combined using "combined weights" (C), also computed similarly with a [[differentiability_in_moes | softmax]] function <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>, <a class="yt-timestamp" data-t="00:37:39">[00:37:39]</a>. The final output (Y) maintains the original input dimensionality <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.

### Benefits of Soft MoE
*   **Fully [[differentiability_in_moes | Differentiable]]**: All operations in Soft MoE layers are continuous and [[differentiability_in_moes | fully differentiable]], allowing for seamless gradient backpropagation and efficient learning of the weighting parameters <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>, <a class="yt-timestamp" data-t="00:54:19">[00:54:19]</a>.
*   **Immunity to Token Dropping and Expert Imbalance**: Since every slot receives a weighted average of *all* tokens (even if some weights are very small), there is no token dropping or imbalance <a class="yt-timestamp" data-t="00:56:38">[00:56:38]</a>, <a class="yt-timestamp" data-t="02:00:06">[02:00:06]</a>.
*   **Scalability**: Soft MoE can scale to thousands of experts <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>, and its cost is primarily determined by the total number of slots, not experts, enabling greater flexibility <a class="yt-timestamp" data-t="00:57:47">[00:57:47]</a>.
*   **Per-Example Determinism**: By combining all tokens within each input sequence, Soft MoE ensures per-example determinism, eliminating batch effects seen in Sparse MoE <a class="yt-timestamp" data-t="01:06:13">[01:06:13]</a>, <a class="yt-timestamp" data-t="01:04:05">[01:04:05]</a>.
*   **Faster Inference**: Significantly faster than most sparse MoEs due to avoiding slow sorting or top-K operations <a class="yt-timestamp" data-t="00:58:35">[00:58:35]</a>.

### Similarities to [[transformer_architecture_in_diffusion_models | Attention Mechanisms]]
Soft MoE shares conceptual similarities with [[transformer_architecture_in_diffusion_models | attention mechanisms]], especially in its use of weighted averages and the [[differentiability_in_moes | softmax]] function <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a>, <a class="yt-timestamp" data-t="01:22:37">[01:22:37]</a>. Both approaches leverage the idea that every part of the input should have a way to contribute to the output, or that experts should have access to information from all tokens <a class="yt-timestamp" data-t="01:03:16">[01:03:16]</a>, <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a>.

However, key distinctions exist:
*   In multi-headed attention, each head processes a smaller, divided portion of the input's dimensionality (e.g., `D/H`) <a class="yt-timestamp" data-t="01:23:01">[01:23:01]</a>.
*   In Soft MoE, experts are non-linear and combine vectors of the full dimensionality (D) at their input and output <a class="yt-timestamp" data-t="01:24:27">[01:24:27]</a>. Every expert has a path to every single part of the input sequence due to the weighted aggregation <a class="yt-timestamp" data-t="01:23:56">[01:23:56]</a>.

## Implementation Details
Soft MoE layers typically replace the second half of MLP blocks in a [[transformer_models_in_3d_reconstruction | Transformer]] architecture <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>, specifically in the encoder part for vision [[Transformer models in 3D reconstruction | Transformers]] <a class="yt-timestamp" data-t="01:17:46">[01:17:46]</a>.

*   **Jax and Einsum**: The paper provides a Jax implementation, utilizing `jnp.einsum` for efficient tensor operations <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>, <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>. Einsum (Einstein summation) is a concise notation for complex tensor multiplications <a class="yt-timestamp" data-t="00:41:52">[00:41:52]</a>.
*   **L2 Normalization**: L2 normalization is applied to input (X) and learnable parameters (Phi) to maintain stability, especially when scaling model dimensions or increasing learning rates <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>, <a class="yt-timestamp" data-t="01:15:18">[01:15:18]</a>.

### [[hyperparameters_and_hardware_considerations_in_moes | Hyperparameters and Hardware Considerations]]
Key [[hyperparameters_and_hardware_considerations_in_moes | hyperparameters]] in Soft MoE include the number of experts (N) and the number of slots per expert (P) <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>.
*   **Total Slots and Cost**: The total number of slots (`N * P`) is the primary factor determining the computational cost (FLOPs) of a Soft MoE layer <a class="yt-timestamp" data-t="00:57:47">[00:57:47]</a>.
*   **Optimal Configuration**: Experiments suggest that using one slot per expert (P=1) is often the optimal choice for performance <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>, <a class="yt-timestamp" data-t="01:54:55">[01:54:55]</a>. This configuration allows per-slot learnable parameters to effectively act as per-expert parameters, learning specific intricacies of each expert <a class="yt-timestamp" data-t="01:32:50">[01:32:50]</a>.
*   **Hardware Impact**: The choice of `N` and `P` depends heavily on the available hardware (e.g., GPUs, TPUs) and its interconnects, influencing memory and time complexity <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>, <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.

## Performance and Evaluation
Soft MoE models were extensively evaluated against dense [[transformer_models_in_3d_reconstruction | Transformer models in 3D reconstruction | Transformers]] and other sparse MoE variants (Token Choice, Expert Choice) <a class="yt-timestamp" data-t="01:35:29">[01:35:29]</a>, <a class="yt-timestamp" data-t="01:35:54">[01:35:54]</a>.

### [[model_training_and_evaluation_methods | Training and Evaluation Methods]]
*   **Dataset**: Models were trained on JFT-4B, an internal Google dataset containing over 4 billion images across 29,000+ classes <a class="yt-timestamp" data-t="01:37:16">[01:37:16]</a>, <a class="yt-timestamp" data-t="01:38:07">[01:38:07]</a>.
*   **Metrics**: Evaluation focused on:
    *   Upstream validation precision on JFT-4B <a class="yt-timestamp" data-t="01:38:46">[01:38:46]</a>.
    *   ImageNet 10-shot accuracy (freezing model weights, replacing head, and training on 10 images per class) <a class="yt-timestamp" data-t="01:38:51">[01:38:51]</a>.
    *   ImageNet fine-tuning accuracy (fully fine-tuning the entire model) <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a>.
*   **Training Scale**: Over 106 models were trained, ranging from 1 billion to 54 billion parameters, for up to 300K steps with a batch size of 4096 <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>, <a class="yt-timestamp" data-t="01:49:42">[01:49:42]</a>.

### [[performance_and_scalability_of_diffusion_models_with_transformers | Performance and Scalability]]
Soft MoE consistently "dominates" (outperforms in every metric <a class="yt-timestamp" data-t="01:38:23">[01:38:23]</a>, <a class="yt-timestamp" data-t="01:38:35">[01:38:35]</a>) other approaches across various model sizes, training budgets, and evaluation metrics <a class="yt-timestamp" data-t="01:43:28">[01:43:28]</a>:
*   **Superior Performance**: Achieves better accuracy and precision for the same amount of training and model size <a class="yt-timestamp" data-t="01:44:43">[01:44:43]</a>, <a class="yt-timestamp" data-t="01:53:15">[01:53:15]</a>.
*   **Extended Training**: Soft MoE models can be trained for significantly longer periods without overfitting, continuing to improve performance <a class="yt-timestamp" data-t="01:55:58">[01:55:58]</a>. A smaller Soft MoE model (e.g., ViT-S) can even match the quality of a much larger dense model (ViT-L) by training for longer <a class="yt-timestamp" data-t="01:57:21">[01:57:21]</a>.
*   **Cost Efficiency**: Soft MoE models are computationally cheaper during inference, offering significant wall-clock time reductions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   **Robustness**: Even with simplified routing mechanisms (like identity or uniform averaging), Soft MoE still outperforms dense [[transformer_models_in_3d_reconstruction | Transformers]] <a class="yt-timestamp" data-t="02:05:50">[02:05:50]</a>.
*   **Contrastive Learning**: Soft MoE's learned representations are also significantly better for other tasks, such as image-language contrastive learning, outperforming standard vision [[Transformer models in 3D reconstruction | Transformers]] when used as an image encoder in a CLIP-like model <a class="yt-timestamp" data-t="02:06:42">[02:06:42]</a>, <a class="yt-timestamp" data-t="02:07:38">[02:07:38]</a>.

## Limitations and Future Work
*   **[[multimodal_diffusion_transformer_architecture | Auto-Regressive Decoders]]**: Soft MoE currently faces difficulties with [[multimodal_diffusion_transformer_architecture | auto-regressive decoders]], commonly found in language models, due to the need to preserve causality between past and future tokens (i.e., masking future tokens during prediction) <a class="yt-timestamp" data-t="01:28:01">[01:28:01]</a>, <a class="yt-timestamp" data-t="01:28:42">[01:28:42]</a>. Naively applying Soft MoE would allow information from future tokens to "leak" into the current prediction <a class="yt-timestamp" data-t="01:29:51">[01:29:51]</a>. This remains a promising research avenue <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
*   **[[hyperparameters_and_hardware_considerations_in_moes | Hardware Optimization]]**: While Soft MoE offers theoretical cost benefits, optimizing its [[hyperparameters_and_hardware_considerations_in_moes | hyperparameters and hardware considerations in MoEs | hyperparameters]] (like number of experts and slots) for specific distributed computing setups remains complex <a class="yt-timestamp" data-t="01:19:32">[01:19:32]</a>, <a class="yt-timestamp" data-t="01:27:38">[01:27:38]</a>.
*   **Learning Rate Schedules**: Optimal learning rate schedules for Soft MoE may differ from standard [[transformer_architecture_in_diffusion_models | Transformers]], suggesting another area for research <a class="yt-timestamp" data-t="01:51:11">[01:51:11]</a>.
*   **Impact on Hallucinations**: The paper does not directly address the impact of Soft MoE on hallucinations in generative models, but it's an interesting question for future work, especially if Soft MoE can be adapted for decoders <a class="yt-timestamp" data-t="01:40:47">[01:40:47]</a>.

In summary, Soft MoE presents a robust and efficient alternative to traditional [[transformer_models_in_3d_reconstruction | Transformer]] architectures and previous sparse MoE variants, offering superior performance and computational advantages by using a fully [[differentiability_in_moes | differentiable]] soft assignment mechanism <a class="yt-timestamp" data-t="02:22:12">[02:22:12]</a>, <a class="yt-timestamp" data-t="02:22:50">[02:22:50]</a>. This innovation has the potential to significantly improve [[scalable_diffusion_models_with_transformers | inference speed]] for large models, which is crucial for applications like robotics and fast control loops <a class="yt-timestamp" data-t="02:21:12">[02:21:12]</a>.