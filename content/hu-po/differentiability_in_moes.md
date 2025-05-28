---
title: Differentiability in MoEs
videoId: _epq9VsViJc
---

From: [[hu-po]] <br/> 

[[transformer_models_and_moes | Mixture of Experts (MoEs)]] are neural network architectures designed to scale model capacity without significant increases in training or inference costs <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. A core challenge in traditional sparse [[transformer_models_and_moes | MoEs]] lies in the inherent **discrete optimization problem** of deciding which "expert" module should process a given input token <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

## Discrete vs. Differentiable Routing

Traditional sparse [[transformer_models_and_moes | MoEs]] use a router to make hard, discrete assignments of tokens to experts <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. This involves a learning process for the router parameters, often using techniques like linear programs, reinforcement learning, or greedy top-K selection <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. However, these discrete assignment mechanisms are typically non-differentiable <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>.

### Challenges of Discrete Routing

*   **Non-differentiability:** The discrete nature of assigning tokens to experts means that gradients cannot be directly propagated through this decision-making step during training <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>.
*   **Training Instability:** Large fractions of input tokens can simultaneously change their discrete routes, leading to training challenges <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>.
*   **Auxiliary Losses:** Many discrete methods require hand-designed heuristic auxiliary losses to balance expert utilization and minimize unassigned tokens <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.
*   **Batch Effects:** In scenarios like inference with small batch sizes or novel inputs, competition for limited expert capacity can lead to inter-batch dependencies, where one input affects the routing and prediction for other inputs <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. This is believed to contribute to the non-deterministic nature of models like GPT-4 and 3.5 when given the same input <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>.

## SoftMoE: A Fully Differentiable Approach

SoftMoE proposes a solution by making all operations within its layers continuous and **fully differentiable** <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a> <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. This means that gradients can be taken and back-propagated through the entire system, enabling end-to-end training <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>.

Instead of hard assignments, SoftMoE performs a **soft assignment** by passing a weighted combination of all input tokens to each expert <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a> <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
This is achieved through:
*   **Learnable Parameters (Phi):** Each slot (which effectively maps to an expert in optimal configurations) has corresponding learnable parameters (Phi) <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.
*   **Softmax for Weights:** The weights (dispatch and combined weights) are computed using a softmax function <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a> <a class="yt-timestamp" data-t="00:56:46">[00:56:46]</a>. This ensures all weights are strictly positive and allows for continuous gradient flow <a class="yt-timestamp" data-t="00:56:46">[00:56:46]</a> <a class="yt-timestamp" data-t="00:58:55">[00:58:55]</a>.
*   **Weighted Averages:** Input tokens are merged into linear, weighted combinations before being dispatched to experts <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. Similarly, expert outputs are combined using weighted averages <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.

### Benefits of Differentiable Routing (SoftMoE)

*   **End-to-End Learning:** The fully differentiable nature allows the model to learn the optimal routing weights (Phi) through standard backpropagation <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>.
*   **Stability:** Soft routing provides greater training stability, as token route changes are continuous rather than abrupt <a class="yt-timestamp" data-t="02:00:42">[02:00:42]</a>.
*   **Avoids Discrete Operations:** SoftMoE eliminates the need for sorting or top-K selection, which are often slow and not well-suited for efficient hardware execution <a class="yt-timestamp" data-t="00:58:29">[00:58:29]</a>.
*   **Immunity to Token Dropping and Imbalance:** Since every slot is filled with a weighted average of *all* input tokens, SoftMoE inherently avoids issues like token dropping and expert imbalance seen in sparse [[transformer_models_and_moes | MoEs]] <a class="yt-timestamp" data-t="00:56:38">[00:56:38]</a>.
*   **Per-Example Determinism:** By combining all tokens within each input sequence, SoftMoE ensures that the model's output for a given input is deterministic at the per-example level, removing dependencies on other inputs in a batch <a class="yt-timestamp" data-t="01:06:11">[01:06:11]</a> <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>.

SoftMoE layers replace the feed-forward blocks within [[transformer_models_and_moes | Transformer models]], especially in the encoder part <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a> <a class="yt-timestamp" data-t="01:13:07">[01:13:07]</a>. This approach enables larger model capacity at lower inference costs and significantly outperforms standard [[transformer_models_and_moes | Transformers]] and other [[transformer_models_and_moes | MoE]] variants across various metrics like image classification and image-language contrastive learning <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

### Similarities to Attention Mechanisms

The use of weighted averages in SoftMoE bears a strong resemblance to attention mechanisms in [[transformer_models_and_moes | Transformers]] <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a> <a class="yt-timestamp" data-t="02:17:52">[02:17:52]</a>. Both approaches leverage the idea that every part of the input should have a way to communicate or contribute to every other part, rather than relying on hard, discrete routing <a class="yt-timestamp" data-t="01:03:18">[01:03:18]</a> <a class="yt-timestamp" data-t="02:17:52">[02:17:52]</a>. The key distinction lies in how the "heads" (in attention) or "experts" (in SoftMoE) process and combine information <a class="yt-timestamp" data-t="01:23:34">[01:23:34]</a>.

### Limitations

A current limitation of SoftMoE is its application to auto-regressive decoders, common in language models <a class="yt-timestamp" data-t="01:28:01">[01:28:01]</a>. The all-to-all weighted combination in SoftMoE could "leak" information from future tokens, violating the causality requirement of decoders (where predictions should only depend on past tokens) <a class="yt-timestamp" data-t="01:29:49">[01:29:49]</a>. This is an area left for future research, though it is hypothesized that masked SoftMoEs might offer a solution <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a> <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

## Hyperparameter Considerations

The [[hyperparameters_and_hardware_considerations_in_moes | total number of slots]] is a key hyperparameter that dictates the computational cost of a SoftMoE layer <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a> <a class="yt-timestamp" data-t="00:57:47">[00:57:47]</a>. The choice of `P` (slots per expert) and `N` (number of experts) depends heavily on [[hyperparameters_and_hardware_considerations_in_moes | hardware considerations]] and distributed computing setups <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. While increasing the number of experts can increase total parameters without direct impact on time complexity (as long as `P` is chosen optimally), there are still overheads due to data transfer in distributed systems <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>. Studies suggest that one slot per expert tends to be the optimal choice for performance <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a> <a class="yt-timestamp" data-t="01:55:05">[01:55:05]</a>.

Overall, the shift from [[continuous_vs_discrete_optimization | discrete to continuous optimization]] in SoftMoE represents a significant advancement, enabling more stable, efficient, and performant [[transformer_models_and_moes | MoE]] architectures for large-scale models <a class="yt-timestamp" data-t="02:22:15">[02:22:15]</a>.