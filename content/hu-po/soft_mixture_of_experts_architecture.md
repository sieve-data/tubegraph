---
title: Soft Mixture of Experts architecture
videoId: _epq9VsViJc
---

From: [[hu-po]] <br/> 

The [[Soft Mixture of Experts architecture | Soft Mixture of Experts]] (Soft MoE) architecture is an extension of the earlier sparse [[Mixture of Experts in vision language modeling | Mixture of Experts]] (MoE) models, developed by Google DeepMind. The initial work on this thread of research includes "Pathways" (October 2021) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, followed by "Sparse Mixture of Experts" (2022) <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, and finally "From Sparse to Soft Mixtures of Experts" (August 2, 2023) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Overview of Mixture of Experts (MoEs)

[[Mixture of experts in vision language modeling | MoE]] architectures allow for scaling model capacity without significantly increasing training or inference costs <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Larger models typically incur higher computational costs due to more neurons and parameters, leading to longer training and inference times, and increased memory complexity <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. The core idea behind MoEs stems from the observation that in many neural networks, a significant portion of computations involve values close to zero, representing wasted compute <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. By selectively activating only parts of the network, MoEs aim to achieve better results at a lower computational cost <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

Traditional sparse MoEs replace dense feed-forward network (FFN) layers with multiple independent FFNs, called "experts" <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. A "router" mechanism then determines which expert(s) should process specific input "tokens" (e.g., image patches in vision models) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### Issues with Sparse MoEs
Despite their benefits, sparse MoEs suffer from several challenges <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>:
*   **Training Instability**: Often due to discrete optimization problems in deciding token-to-expert assignments <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Token Dropping**: Some input tokens may not be assigned to any expert, leading to lost information <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>.
*   **Expert Imbalance**: Some experts receive disproportionately more tokens than others <a class="yt-timestamp" data-t="00:56:27">[00:56:27]</a>.
*   **Scaling Limitations**: Inability to easily scale the number of experts <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   **Ineffective Fine-tuning** <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Non-determinism**: Due to hard, discrete routing decisions, the output for a given input can change based on other inputs in the batch, leading to non-deterministic behavior (e.g., in [[Gemini 15 multimodal mixture of experts | GPT-4]]) <a class="yt-timestamp" data-t="03:03:01">[03:03:01]</a>.

## Soft Mixture of Experts (Soft MoE)

Soft MoE proposes a fully differentiable sparse Transformer architecture that addresses the limitations of traditional sparse MoEs <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### Core Mechanism
Instead of a sparse and discrete router that makes hard assignments <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>, Soft MoE performs an implicit *soft assignment* by passing different weighted combinations of *all* input tokens to each expert <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

Each expert processes a fixed number of "slots," and each slot receives a weighted average of all input tokens <a class="yt-timestamp" data-t="01:01:51">[01:01:51]</a>. These weights are determined by learnable per-slot parameters ($\Phi$) and the input values themselves, through a softmax operation <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>. After experts process their respective weighted input combinations, their outputs are again combined using another set of "combined weights" ($C$) to produce the final output tokens, maintaining the original sequence length <a class="yt-timestamp" data-t="01:21:26">[01:21:26]</a>.

### Advantages of Soft MoE
*   **Full Differentiability**: All operations within Soft MoE layers are continuous and fully differentiable <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>. This allows for direct gradient propagation through the routing mechanism, simplifying training and optimization compared to non-differentiable hard routing <a class="yt-timestamp" data-t="00:54:04">[00:54:04]</a>.
*   **Immunity to Token Dropping and Imbalance**: Because every slot is filled with a weighted average of *all* tokens (with strictly positive weights thanks to softmax), Soft MoE inherently avoids token dropping and expert imbalance issues seen in sparse MoEs <a class="yt-timestamp" data-t="00:56:38">[00:56:38]</a>.
*   **Per-Example Determinism**: Soft MoE gracefully sidesteps inter-batch dynamics (where inputs within a batch compete for expert capacity), making predictions deterministic at the sequence level, regardless of other inputs in the batch <a class="yt-timestamp" data-t="01:04:05">[01:04:05]</a>.
*   **Faster and More Scalable**: It avoids computationally expensive sorting or top-K operations <a class="yt-timestamp" data-t="00:58:29">[00:58:29]</a>. This makes it significantly faster than most sparse MoEs <a class="yt-timestamp" data-t="00:58:35">[00:58:35]</a>. The time complexity primarily depends on the total number of slots, not the number of experts <a class="yt-timestamp" data-t="00:57:47">[00:57:47]</a>. It can scale to thousands of experts <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
*   **Enhanced Performance**: Experiments demonstrate that Soft MoE consistently outperforms dense Transformers and other sparse MoE variants across various metrics, for a given computational budget (flops or time) <a class="yt-timestamp" data-t="01:43:28">[01:43:28]</a>. It allows for significantly better model performance and/or reduced inference costs <a class="yt-timestamp" data-t="01:43:43">[01:43:43]</a>.
*   **Improved Trainability**: Soft MoE models can be trained for longer without overfitting, continually improving performance <a class="yt-timestamp" data-t="01:55:58">[01:55:58]</a>. This allows smaller Soft MoE models to match or exceed the quality of much larger dense models trained for standard durations <a class="yt-timestamp" data-t="01:57:21">[01:57:21]</a>.

## Soft MoE Architecture Details

Soft MoE layers replace the feed-forward network (FFN) blocks in Transformer models <a class="yt-timestamp" data-t="00:59:01">[00:59:01]</a>. Specifically, in the experiments on Vision Transformers (ViTs), they replace the second half of MLP blocks <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>, typically the last six out of twelve blocks <a class="yt-timestamp" data-t="01:58:23">[01:58:23]</a>.

### Key Components:
*   **Experts ($F$)**: Multiple independent FFNs <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Slots ($P$)**: Each expert processes a fixed number of slots <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>. The total number of slots is a critical hyperparameter determining the computational cost <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. Optimal performance is often achieved with one slot per expert <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>.
*   **Learnable Parameters ($\Phi$)**: Each slot has a corresponding D-dimensional vector of learnable parameters <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.
*   **Dispatch Weights ($D$)**: Computed via a softmax operation on the product of input tokens and learnable slot parameters ($\Phi$) <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>. These weights determine the weighted combination of all input tokens that feed into each expert's slot <a class="yt-timestamp" data-t="01:01:51">[01:01:51]</a>.
*   **Combined Weights ($C$)**: Similarly computed using softmax, these weights combine the outputs from all experts to form the final output tokens <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.

### Connection to Attention Mechanisms
The process of weighing and combining tokens in Soft MoE bears strong similarities to attention mechanisms in Transformers <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a>. Just as attention allows every part of an input to communicate with every other part <a class="yt-timestamp" data-t="01:03:27">[01:03:27]</a>, Soft MoE ensures every expert has a path to information from every single token <a class="yt-timestamp" data-t="01:03:53">[01:03:53]</a>. Different slots, and thus experts, learn to focus on specific semantic concepts within the input, similar to how attention heads specialize <a class="yt-timestamp" data-t="02:16:55">[02:16:55]</a>.

## Applications and Limitations

### Vision Transformers
Soft MoE has been demonstrated using Vision Transformers (ViTs) for image classification and [[Mixture of experts in vision language modeling | vision-language modeling]] tasks <a class="yt-timestamp" data-t="01:42:42">[01:42:42]</a>. Training on a proprietary Google dataset (JFT-4B with over 4 billion images) <a class="yt-timestamp" data-t="01:37:16">[01:37:16]</a>, Soft MoE ViT models significantly outperform standard dense ViTs and other MoE variants <a class="yt-timestamp" data-t="01:43:28">[01:43:28]</a>. They achieve better accuracy at lower inference costs and can be trained for longer to achieve even higher quality <a class="yt-timestamp" data-t="01:57:21">[01:57:21]</a>.

### Language Decoders (Future Work)
A current limitation of Soft MoE is its direct application to auto-regressive decoders in language models <a class="yt-timestamp" data-t="02:27:55">[02:27:55]</a>. Decoders require causality preservation, meaning future tokens should not influence the prediction of the current token <a class="yt-timestamp" data-t="02:28:06">[02:28:06]</a>. The weighted combination approach of Soft MoE, which considers all tokens, would allow information from future tokens to "leak in" <a class="yt-timestamp" data-t="02:29:51">[02:29:51]</a>. This requires further research into masked Soft MoE variants <a class="yt-timestamp" data-t="02:28:42">[02:28:42]</a>. It is speculated that companies like OpenAI may have already developed such solutions for their proprietary language models <a class="yt-timestamp" data-t="02:30:02">[02:30:02]</a>.

## Impact
The principles behind Soft MoE, offering faster inference and reduced computational costs, are particularly relevant for applications requiring low latency, such as using large language models for fast control loops in robotics <a class="yt-timestamp" data-t="02:21:40">[02:21:40]</a>.