---
title: Hybrid Architectures and Transformer Block Efficiency
videoId: Teru_qIdB8Y
---

From: [[hu-po]] <br/> 

Efficiently managing computational resources is a critical challenge in training and deploying large language models, especially those based on [[transformerbased_model_architectures | Transformer]] architectures. The "Mixture of Depths" (MoD) paper proposes a novel approach to dynamically allocate compute, significantly enhancing [[transformerbased_model_architectures | Transformer]] block efficiency during both training and inference <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Transformer Block Computation

A standard [[transformerbased_model_architectures | Transformer]] block consists of two main parts:
1.  **Multi-head self-attention mechanism:** This component treats every token in an input sequence equally, performing computation between all parts of the sequence <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The self-attention operation is computationally expensive, exhibiting a quadratic (O(N²)) relationship with respect to the input sequence length <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>, [00:35:50].
2.  **Feed-forward network (MLP):** This part also treats all tokens equally in terms of computation <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

Traditional [[transformerbased_model_architectures | Transformer]] models expend the same amount of computation (FLOPs – floating-point operations) per token in a forward pass <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, [00:14:01].

## Mixture of Depths (MoD) for Efficiency

MoD is an efficiency technique designed to intelligently route tokens, allowing them to skip unnecessary computations <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Instead of uniformly spreading FLOPs, MoD allows [[transformerbased_model_architectures | Transformers]] to learn to dynamically allocate compute to specific positions in a sequence <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

This dynamic allocation is achieved by:
*   **Conditional Skipping:** Tokens can either participate in a block's computation or pass through a residual connection, remaining unchanged and saving compute <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. The residual connection is computationally inexpensive compared to the attention and MLP blocks <a class="yt-timestamp" data-t="00:43:13">[00:43:13]</a>.
*   **Routing Mechanism:** A learnable "router" determines which tokens will participate. This router emits a scalar weight for each token, expressing its preference for that token to participate or to route around the block <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.
*   **Top-K Selection:** The router uses a top-K mechanism to select tokens for computation, ensuring a predefined number of tokens always go through the block <a class="yt-timestamp" data-t="00:37:59">[00:37:59]</a>. This means if 100 tokens are input and the capacity is 50%, exactly 50 tokens will go through, and 50 will skip <a class="yt-timestamp" data-t="00:54:54">[00:54:54]</a>.

### Benefits of MoD

MoD provides significant advantages:

*   **Compute Efficiency:** By capping the number of tokens that participate (e.g., to 50%), the self-attention computation, which is O(N²), becomes approximately 25% as intensive (because (N/2)² = N²/4) <a class="yt-timestamp" data-t="00:40:59">[00:40:59]</a>, [01:09:09]. Overall, MoD can lead to inference speed improvements of up to 50% <a class="yt-timestamp" data-t="00:38:39">[00:38:39]</a>, [01:41:50].
*   **Static Computation Graph:** A key innovation is that MoD maintains a static computation graph with known tensor sizes <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, [00:38:12]. This is crucial for efficient execution on hardware, as dynamic graph changes can lead to underutilization <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>.
*   **Improved Quality (Lower Loss):** MoD models not only train faster but also achieve lower loss (better performance) than baseline models using equivalent FLOPs <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>, [01:09:16]. This suggests that intelligently skipping layers can benefit the learning process, possibly by allowing information at different levels of abstraction to be selectively processed <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>, [00:42:27]
*   **KV Cache Size Reduction:** MoD models can have a larger KV cache size during autoregressive sampling, as less information needs to be stored for the attention mechanism <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>.

## MoD and Hybrid Architectures

MoD builds upon and relates to other architectural innovations:

*   **Relation to [[Soft Mixture of Experts in Transformer Architecture | Mixture of Experts (MoE)]]:** MoD is seen as a "pun on" or variant of [[Soft Mixture of Experts in Transformer Architecture | Mixture of Experts]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. While [[Soft Mixture of Experts in Transformer Architecture | MoE]] uses a router to select among multiple specialized "experts" (typically MLPs) to improve quality, MoD uses a router to decide whether to send a token through a block or skip it, primarily for efficiency <a class="yt-timestamp" data-t="00:34:14">[00:34:14]</a>, [00:35:09].
*   **Integration with MoE:** MoD can be combined with existing [[Soft Mixture of Experts in Transformer Architecture | MoE]] models.
    *   **Staged MoD:** A new router is added *before* the entire [[transformerbased_model_architectures | Transformer]] block to decide whether to skip the attention and MLP <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>. This offers the full computational benefits by skipping the expensive self-attention <a class="yt-timestamp" data-t="01:20:02">[01:20:02]</a>.
    *   **Integrated MoD:** An existing [[Soft Mixture of Experts in Transformer Architecture | MoE]] router can be modified to include a "noop" (no operation) expert, which effectively skips the MLP component <a class="yt-timestamp" data-t="01:18:38">[01:18:38]</a>. This simplifies the routing machinery but doesn't allow skipping the self-attention <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>.
*   **Application to [[comparison_of_rwkv_with_transformer_architectures | Mamba]] and Jamba:** While [[transformerbased_model_architectures | Transformers]] have O(N²) attention complexity, [[comparison_of_rwkv_with_transformer_architectures | Mamba]] models use state-space models and are linear in complexity <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>. The Jamba model is a [[combining_different_blocks_in_neural_network_architectures | hybrid architecture]] that combines [[transformerbased_model_architectures | Transformer]] blocks and [[comparison_of_rwkv_with_transformer_architectures | Mamba]] blocks <a class="yt-timestamp" data-t="01:10:43">[01:10:43]</a>. MoD's principles of conditional compute allocation could potentially be applied to [[comparison_of_rwkv_with_transformer_architectures | Mamba]] or [[combining_different_blocks_in_neural_network_architectures | hybrid architectures]], although the efficiency gains might be less pronounced for already efficient [[comparison_of_rwkv_with_transformer_architectures | Mamba]] blocks <a class="yt-timestamp" data-t="01:10:53">[01:10:53]</a>.

## Training and Inference Considerations

During training, MoD uses an "expert choice" routing where the router knows the entire sequence and selects the top-K tokens <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>. However, for autoregressive sampling (inference), the model cannot see future tokens. To address this, MoD employs a small auxiliary MLP predictor (a "second router") that predicts whether a token will be among the top-K or not <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>. This causal prediction approach leads to minimal performance degradation compared to the non-causal training scheme <a class="yt-timestamp" data-t="01:21:14">[01:21:14]</a>.

### Depth vs. Width

The research also indicates that when adding FLOPs to a model, it is empirically better to add depth (more layers) rather than width (more neurons per layer) <a class="yt-timestamp" data-t="01:12:25">[01:12:25]</a>. This finding aligns with the general intuition in deep learning that deeper networks can learn richer hierarchies of features <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>. MoD allows for this by freeing up computational budget that can then be reinvested into adding more layers.

MoD is anticipated to be widely adopted due to its simplicity and significant benefits in both speed and performance <a class="yt-timestamp" data-t="01:42:36">[01:42:36]</a>.