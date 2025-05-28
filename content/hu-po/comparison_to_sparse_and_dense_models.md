---
title: Comparison to Sparse and Dense Models
videoId: _epq9VsViJc
---

From: [[hu-po]] <br/> 

This article explores the evolution of Mixture of Experts (MoE) architectures, contrasting dense models with sparse and soft MoE variants, based on a paper titled "From Sparse to Soft Mixtures of Experts" by Google DeepMind <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This work builds upon earlier research, including "Sparse Mixture of Experts" (2022) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> and "Pathways" (2021) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, all from the same research thread <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Mixture of Experts (MoE) Architectures

Mixture of Experts (MoE) architectures are designed to [[performance_and_efficiency_in_machine_learning_models | scale model capacity]] without significantly increasing training or inference costs <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. The core idea is to replace dense feed-forward network (FFN) layers, often found in Transformer models, with multiple smaller, independent FFNs, called "experts" <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a> <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. This approach aims to avoid wasted computation seen in traditional neural networks where many neurons' activations are very close to zero <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. MoEs leverage the intuition that most neural networks are "mostly zero," meaning only a few pathways through the network truly matter for a given input <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. By selectively activating these pathways, MoEs can achieve better performance at a fraction of the computational cost <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

However, traditional MoEs suffer from several issues:
*   Training instability <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>
*   Token dropping (inputs not processed by any expert) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>
*   Inability to scale the number of experts effectively <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
*   Ineffective fine-tuning <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>

## Sparse Mixture of Experts

Earlier MoE work, known as "sparse mixture of experts," employs a discrete router to decide which expert modules should process each input token <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a> <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. This routing can be based on techniques like Token Choice (selecting top-K experts per token) or Expert Choice (selecting top-C tokens per expert) <a class="yt-timestamp" data-t="01:39:56">[01:39:56]</a>.

A significant challenge with sparse MoEs is their discrete and often non-differentiable nature <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>. This makes training complex, often requiring heuristic auxiliary losses to balance expert utilization and minimize unassigned tokens <a class="yt-timestamp" data-t="01:19:12">[01:19:12]</a> <a class="yt-timestamp" data-t="01:59:50">[01:59:50]</a>. This discrete routing can lead to "token dropping," where some input tokens are not used in computation <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>, or "expert imbalance," where some experts receive disproportionately more tokens <a class="yt-timestamp" data-t="00:56:27">[00:56:27]</a>.

One notable consequence of sparse MoEs is their non-deterministic output at the sequence level, which arises from batch effects during inference <a class="yt-timestamp" data-t="01:00:43">[01:00:43]</a> <a class="yt-timestamp" data-t="01:04:05">[01:04:05]</a>. If tokens from different inputs within a batch compete for limited expert slots, the output for one input can be affected by others in the same batch <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a> <a class="yt-timestamp" data-t="01:01:14">[01:01:14]</a>.

## Soft Mixture of Experts (Soft-MoE)

Soft-MoE is proposed as a fully differentiable sparse Transformer that overcomes many of the challenges faced by previous MoE approaches <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a> <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>. Instead of discrete routing, Soft-MoE performs a "soft assignment" by passing different weighted combinations of *all* input tokens to each expert <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a> <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. This weighted combination (mixing of tokens) allows for continuous operations, making the entire model fully differentiable <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.

In Soft-MoE, each expert processes a certain number of "slots," and each slot receives a weighted average of *all* input tokens <a class="yt-timestamp" data-t="01:01:51">[01:01:51]</a>. The weights for these combinations are determined by learnable "per-slot parameters" (Phi) multiplied by the input tokens, and then normalized via a softmax function <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a> <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>. After experts process these combined inputs, their outputs are again combined using "combined weights" (C) to recover the original sequence length <a class="yt-timestamp" data-t="02:12:47">[02:12:47]</a>.

Soft-MoE offers several advantages:
*   **Differentiability**: All operations are continuous and fully differentiable, simplifying training <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>.
*   **Stability**: Soft routing provides stability during training by preventing abrupt changes in discrete routes <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.
*   **Scalability**: It scales well to thousands of experts <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.
*   **Balance**: It is "balanced by construction," meaning every slot is filled with a weighted average of all tokens, thus immune to token dropping and expert imbalance <a class="yt-timestamp" data-t="00:56:38">[00:56:38]</a>.
*   **Determinism**: It is per-example deterministic at inference, unlike sparse MoEs that suffer from batch effects <a class="yt-timestamp" data-t="02:00:03">[02:00:03]</a>.
*   **Speed**: It significantly outperforms most sparse MoEs because it avoids slow, non-differentiable sort or top-K operations <a class="yt-timestamp" data-t="00:58:27">[00:58:27]</a>.

Although "not technically sparse" since every input token fractionally activates all model parameters <a class="yt-timestamp" data-t="00:58:50">[00:58:50]</a>, Soft-MoE still achieves efficiency by ensuring each expert only processes a subset of the total slots <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>.

### Comparison to Dense Models and Other MoE Variants

The paper conducts extensive experiments on the JFT-4B dataset (a proprietary Google dataset with over 4 billion images across 29,000 classes) <a class="yt-timestamp" data-t="01:37:16">[01:37:16]</a>, using Vision Transformer (ViT) models, and evaluating on metrics like JFT-4B Precision@1 and ImageNet 10-shot accuracy <a class="yt-timestamp" data-t="01:38:46">[01:38:46]</a>.

Soft-MoE consistently "dominates" (outperforms in every metric) dense ViT models and other sparse MoE variants (Token Choice, Expert Choice) <a class="yt-timestamp" data-t="01:38:32">[01:38:32]</a> <a class="yt-timestamp" data-t="01:45:50">[01:45:50]</a>.
*   **[[performance_and_efficiency_in_machine_learning_models | Performance and Efficiency]]**: Soft-MoE significantly lowers inference costs (e.g., 10.5% lower inference cost, 5.7% lower wall-clock time) while matching or substantially outperforming other models <a class="yt-timestamp" data-t="01:50:01">[01:50:01]</a> <a class="yt-timestamp" data-t="01:52:16">[01:52:16]</a>. Even smaller Soft-MoE models can match the quality of larger dense ViT models when trained for longer periods <a class="yt-timestamp" data-t="01:57:21">[01:57:21]</a>.
*   **Training**: Soft-MoE models can be trained for longer without overfitting, continually improving performance, unlike some scaling laws for dense models where additional training yields diminishing returns <a class="yt-timestamp" data-t="01:48:28">[01:48:28]</a>. The time required for Soft-MoE training also scales more favorably with an increasing number of experts compared to other sparse MoE approaches <a class="yt-timestamp" data-t="02:01:15">[02:01:15]</a>.
*   **Ablation Studies**: Experiments show that even naive routing strategies (e.g., identity or uniform mixing of tokens) within a Soft-MoE structure can outperform dense Transformers <a class="yt-timestamp" data-t="02:05:41">[02:05:41]</a>, suggesting that the mixture-of-experts architecture itself contributes significant benefits.
*   **Learned Representations**: Representations learned by Soft-MoE models are also significantly better for other tasks, such as image-language contrastive learning, outperforming dense models in zero-shot classification benchmarks like CIFAR-100 <a class="yt-timestamp" data-t="02:07:08">[02:07:08]</a> <a class="yt-timestamp" data-t="02:08:31">[02:08:31]</a>.

## Similarities to Attention Mechanisms

The mechanism of Soft-MoE, involving learned weights for combining input tokens before feeding them to experts, bears strong similarities to attention mechanisms in Transformers <a class="yt-timestamp" data-t="02:22:37">[02:22:37]</a> <a class="yt-timestamp" data-t="02:23:51">[02:23:51]</a>. Just as attention heads "pay attention" to different parts of the input sequence <a class="yt-timestamp" data-t="02:17:40">[02:17:40]</a>, Soft-MoE's "slots" (and by extension, the experts) learn to focus on specific semantic concepts within an image, such as the duck's bill or head <a class="yt-timestamp" data-t="02:16:55">[02:16:55]</a>. This suggests a convergence towards an attention-like routing strategy, even when designing for expert mixtures <a class="yt-timestamp" data-t="02:23:18">[02:23:18]</a>.

However, a key distinction from multi-headed attention is that Soft-MoE experts are non-linear and combine full-sized (D-dimensional) vectors, rather than processing smaller (D/H-dimensional) subsets of the input like individual attention heads <a class="yt-timestamp" data-t="02:26:50">[02:26:50]</a>.

## Current Limitations

A notable limitation of Soft-MoE is its difficulty in being applied to auto-regressive decoders, which are crucial for large language models <a class="yt-timestamp" data-t="02:27:53">[02:27:53]</a>. Decoders require a causal mask to prevent information leakage from future tokens into current predictions <a class="yt-timestamp" data-t="02:29:12">[02:29:12]</a>. Since Soft-MoE relies on weighted combinations of *all* tokens, naively applying it to a decoder would introduce correlations between past and future tokens, breaking causality <a class="yt-timestamp" data-t="02:29:51">[02:29:51]</a>. The paper identifies adapting Soft-MoE for auto-regressive decoders as a promising direction for future research <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

## Implications and Future Work

Soft-MoE offers a significant step forward in [[comparison_of_xlstm_with_transformers_and_other_models | scaling machine learning models]] efficiently. Its ability to provide faster inference at lower computational costs makes it particularly relevant for applications requiring rapid responses, such as real-time control loops in robotics <a class="yt-timestamp" data-t="02:21:20">[02:21:20]</a>. The continuous improvement in model quality with extended training, coupled with its overall superior performance, suggests Soft-MoE could become a standard for future Transformer architectures <a class="yt-timestamp" data-t="02:22:42">[02:22:42]</a>.

Future work will likely focus on resolving the challenges of applying Soft-MoE to language model decoders, potentially through masked Soft-MoE variants <a class="yt-timestamp" data-t="02:31:01">[02:31:01]</a>. Optimizing hyperparameters (number of experts, slots per expert) for specific hardware configurations also remains a complex, yet crucial, area of research <a class="yt-timestamp" data-t="02:30:32">[02:30:32]</a>.