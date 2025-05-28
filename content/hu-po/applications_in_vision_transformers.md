---
title: Applications in Vision Transformers
videoId: _epq9VsViJc
---

From: [[hu-po]] <br/> 

[[Vision Transformers and their efficiency | Vision Transformers]] (ViTs) are a type of model architecture that utilizes the attention mechanism, now widely used in artificial intelligence models <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>, <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. This article discusses the application of a novel Mixture of Experts (MoE) approach, called Soft MoE, within [[Vision Transformers and their efficiency | Vision Transformer]] architectures, primarily for [[Computer vision deep dive | visual recognition]] tasks <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>.

## Vision Transformers Overview
A [[Vision Transformers and their efficiency | Vision Transformer]] processes images by breaking them down into smaller "patches," which are then treated as "tokens" – analogous to how [[Scaling of language models and vision transformers | language models]] break sentences into tokens <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. These tokens are then fed into the transformer architecture.

In a standard [[Vision Transformers and their efficiency | Vision Transformer]] (ViT) block, there's an attention computation followed by a feed-forward block (also known as a Multi-Layer Perceptron or MLP) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. The feed-forward block is often a "dense" fully connected neural network <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

### Limitations of Dense Models
Larger [[Vision Transformers and their efficiency | Vision Transformer]] models generally offer improved performance but come with significantly increased computational costs for both training and inference <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This is due to the greater number of neurons and parameters, leading to more calculations on GPUs or CPUs <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Soft Mixture of Experts (Soft MoE)
Soft MoE is a technique proposed by Google DeepMind to scale model capacity without substantial increases in training or inference costs <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. It addresses issues found in earlier sparse MoE approaches, such as training instability, token dropping, and difficulties in scaling the number of experts <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Integration in Vision Transformers
Instead of a single dense feed-forward block, Soft MoE replaces it with a "mixture of experts" <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Each "expert" is an independent feed-forward network or MLP <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>, <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This approach is applied only to the MLP blocks within the [[Vision Transformers and their efficiency | Vision Transformer]] architecture, not the attention blocks <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>. In their experiments, they applied MoE layers in the last six of twelve blocks of the ViT-S backbone <a class="yt-timestamp" data-t="01:58:23">[01:58:23]</a>, <a class="yt-timestamp" data-t="01:58:26">[01:58:26]</a>.

Unlike previous sparse MoE methods that used a discrete router to assign tokens to specific experts, Soft MoE employs a "soft assignment" by passing different weighted combinations of all input tokens to each expert <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>, <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This means every slot (input to an expert) is filled with a weighted average of *all* tokens, allowing for a fully differentiable process <a class="yt-timestamp" data-t="00:56:40">[00:56:40]</a>, <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.

### Key Advantages of Soft MoE in ViTs
1.  **Differentiability**: All operations in Soft MoE layers are continuous and fully differentiable, making them easier to train via backpropagation <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.
2.  **Avoids Token Dropping and Imbalance**: Soft MoE is inherently immune to issues like token dropping (where some tokens are not processed) and expert imbalance (where some experts receive more tokens than others), as every slot receives a weighted average of all tokens <a class="yt-timestamp" data-t="00:56:38">[00:56:38]</a>, <a class="yt-timestamp" data-t="00:56:40">[00:56:40]</a>.
3.  **Faster Inference**: By avoiding discrete assignments and sorting/top-K operations, Soft MoE is significantly faster than most sparse MoEs <a class="yt-timestamp" data-t="00:58:29">[00:58:29]</a>, <a class="yt-timestamp" data-t="00:58:35">[00:58:35]</a>.
4.  **Scalability**: It scales well to a large number of experts (thousands) without significant increases in training or inference costs, and can achieve higher model capacity <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a>, <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>.
5.  **Deterministic Inference (per-example)**: Unlike sparse MoEs which can be non-deterministic due to competition for expert slots in a batch, Soft MoE is per-example deterministic <a class="yt-timestamp" data-t="02:00:03">[02:00:03]</a>, <a class="yt-timestamp" data-t="02:00:06">[02:00:06]</a>, <a class="yt-timestamp" data-t="02:00:09">[02:00:09]</a>.

## Experimental Results
The paper evaluates Soft MoE on [[Computer vision deep dive | image classification]] and [[Vision language models and their applications | image-language contrastive learning]] tasks, using various sizes of [[Vision Transformers and their efficiency | Vision Transformer]] models (ViT-S, ViT-B, ViT-L, ViT-H) and comparing them against dense ViTs and other sparse MoE variants like Token Choice and Expert Choice <a class="yt-timestamp" data-t="01:34:35">[01:34:35]</a>, <a class="yt-timestamp" data-t="01:35:45">[01:35:45]</a>, <a class="yt-timestamp" data-t="01:36:02">[01:36:02]</a>.

Experiments were conducted on the proprietary JFT-4B dataset (containing over 4 billion images across 29,000+ classes) for pre-training <a class="yt-timestamp" data-t="01:37:16">[01:37:16]</a>, <a class="yt-timestamp" data-t="01:37:50">[01:37:50]</a>. Evaluation metrics included JFT-4B Precision@1, ImageNet 10-shot accuracy, and ImageNet fine-tuning accuracy <a class="yt-timestamp" data-t="01:38:48">[01:38:48]</a>.

### Performance Summary
*   **Dominance**: Soft MoE consistently outperforms dense [[Vision Transformers and their efficiency | Vision Transformers]] and other sparse MoE approaches across all evaluated metrics and computational budgets <a class="yt-timestamp" data-t="01:44:45">[01:44:45]</a>, <a class="yt-timestamp" data-t="01:50:16">[01:50:16]</a>.
*   **Cost-Efficiency**: Soft MoE achieves better performance for the same or lower computational cost <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>. For example, Soft MoE-B/16 can match the performance of ViT-H/14 while having 10.5% lower inference cost and being 5.7% faster <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>, <a class="yt-timestamp" data-t="00:49:10">[00:49:10]</a>.
*   **Longer Training**: Soft MoE models can be trained for longer periods without overfitting, leading to further performance gains <a class="yt-timestamp" data-t="01:54:50">[01:54:50]</a>, <a class="yt-timestamp" data-t="01:56:02">[01:56:02]</a>.
*   **Smaller Models, Bigger Impact**: A smaller Soft MoE model (e.g., ViT-S) trained for longer can achieve similar performance to a much larger dense ViT model (e.g., ViT-L) <a class="yt-timestamp" data-t="01:57:21">[01:57:21]</a>.

## Conclusion
Soft MoE presents a significant advancement in developing more efficient and performant [[Vision Transformers and their efficiency | Vision Transformer]] architectures. Its ability to offer better performance at lower computational costs makes it highly relevant for industry needs, especially for applications requiring faster inference like [[RT2 Robotic Transformer for Vision Language Action Models | robotics]] control loops <a class="yt-timestamp" data-t="02:21:12">[02:21:12]</a>.

The paper notes that a promising future research direction is adapting Soft MoE for auto-regressive decoders in [[Scaling of language models and vision transformers | language models]], which would require careful handling of causal masking <a class="yt-timestamp" data-t="02:22:57">[02:22:57]</a>.