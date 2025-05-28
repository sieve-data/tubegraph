---
title: Expert Choice and Token Choice Routing
videoId: Teru_qIdB8Y
---

From: [[hu-po]] <br/> 
In the context of Transformer-based language models, **routing mechanisms** are employed to dynamically allocate computational resources. These mechanisms determine which parts of the model (or which "experts") process specific tokens in a sequence, aiming for [[compute_efficiency_and_intelligent_routing | compute efficiency and intelligent routing]]. A key challenge is maintaining a static computation graph, which is crucial for efficient hardware utilization [00:06:13](<a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>, [00:14:45](<a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>).

Random routing of tokens significantly underperforms compared to learned routing [00:46:09](<a class="yt-timestamp" data-t="00:46:09">[00:46:09]</a>, [00:46:46](<a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>). Two main learned routing schemes are **Token Choice** and **Expert Choice**.

### Token Choice Routing

In **Token Choice** routing, the router generates a probability distribution for each token, allowing the token to choose its preferred computational path [00:46:57](<a class="yt-timestamp" data-t="00:46:57">[00:46:57]</a>, [00:48:06](<a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>).

A significant drawback of this method is the potential for **imbalanced load**:
*   If a path's capacity is exceeded, surplus tokens must be dropped [00:48:22](<a class="yt-timestamp" data-t="00:48:22">[00:48:22]</a>, [00:49:09](<a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>).
*   Conversely, if a path doesn't attract enough tokens to fill its capacity, it leads to wasted computational resources (empty slots in GPU operations) [00:49:21](<a class="yt-timestamp" data-t="00:49:21">[00:49:21]</a>, [00:50:10](<a class="yt-timestamp" data-t="00:50:10">[00:50:10]</a>).
*   The choice of which tokens to drop when capacity is exceeded is often arbitrary, with priority sometimes given to tokens that appear earlier in the sequence [00:50:16](<a class="yt-timestamp" data-t="00:50:16">[00:50:16]</a>).

### Expert Choice Routing

**Expert Choice** routing flips the dynamic: instead of tokens choosing paths, each computational path (or "expert") selects the top *K* tokens based on the tokens' preferences [00:47:15](<a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>, [00:50:41](<a class="yt-timestamp" data-t="00:50:41">[00:50:41]</a>).

This method offers a key advantage:
*   It ensures perfect load balance, as exactly *K* tokens are guaranteed to be processed by each path, maximizing hardware utilization [00:47:21](<a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>, [00:50:53](<a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>).
*   Tokens are dropped only if they are not among the top *K* chosen by any path [00:51:35](<a class="yt-timestamp" data-t="00:51:35">[00:51:35]</a>).
*   A single token might be routed to multiple paths if its preference is high enough for more than one expert [00:51:28](<a class="yt-timestamp" data-t="00:51:28">[00:51:28]</a>, [00:51:30](<a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>).

The "Mixture of Depth" (MoD) paper specifically deploys **Expert Choice routing** [00:48:42](<a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>, [00:51:42](<a class="yt-timestamp" data-t="00:51:42">[00:51:42]</a>).

### Router Implementation and Challenges

The router for both schemes emits a scalar weight for each token, reflecting its preference for participating in a block's computation [00:36:59](<a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>). This weight is determined by a linear projection of the token's embedding using a trained weight matrix (W), meaning the router itself has parameters that are updated via gradient descent during training [00:53:22](<a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>, [00:53:34](<a class="yt-timestamp" data-t="00:53:34">[00:53:34]</a>, [01:44:13](<a class="yt-timestamp" data-t="01:44:13">[01:44:13]</a>).

A key challenge for these routing schemes, especially Expert Choice, arises during **autoregressive sampling** (inference), where the model predicts tokens one by one [00:55:59](<a class="yt-timestamp" data-t="00:55:59">[00:55:59]</a>, [01:21:12](<a class="yt-timestamp" data-t="01:21:12">[01:21:12]</a>):
*   The top-K operation in Expert Choice is *non-causal*, as it requires knowing the router weights for all tokens in the sequence, including future ones [00:55:40](<a class="yt-timestamp" data-t="00:55:40">[00:55:40]</a>, [01:23:01](<a class="yt-timestamp" data-t="01:23:01">[01:23:01]</a>).
*   During inference, future tokens are unknown.
*   To address this, an auxiliary MLP predictor (a second, smaller router) is used during inference. This predictor, trained with a stop gradient, predicts whether a token will be among the top *K* selected or not [00:57:27](<a class="yt-timestamp" data-t="00:57:27">[00:57:27]</a>, [00:59:07](<a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>, [01:21:26](<a class="yt-timestamp" data-t="01:21:26">[01:21:26]</a>). This causal, predictor-based approach leads to minimal performance degradation [01:21:14](<a class="yt-timestamp" data-t="01:21:14">[01:21:14]</a>, [01:22:10](<a class="yt-timestamp" data-t="01:22:10">[01:22:10]</a>).

### Application in Mixture of Depth (MoD)

In MoD, the router decides whether a token goes through the full Transformer block (self-attention and MLP) or skips it via a residual connection [00:23:30](<a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>, [01:39:04](<a class="yt-timestamp" data-t="01:39:04">[01:39:04]</a>). Skipping is computationally cheap, while processing through the block is expensive [01:39:06](<a class="yt-timestamp" data-t="01:39:06">[01:39:06]</a>, [01:43:13](<a class="yt-timestamp" data-t="01:43:13">[01:43:13]</a>). By setting a block's capacity (e.g., 50% of tokens), the self-attention computation, which is quadratic with sequence length, becomes significantly less intensive (e.g., 25% of the original flops for a 50% reduction in tokens) [00:44:17](<a class="yt-timestamp" data-t="00:44:17">[00:44:17]</a>, [01:40:50](<a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>). This leads to faster inference (upwards of 50% faster) and often better model performance for equivalent training flops [00:38:39](<a class="yt-timestamp" data-t="00:38:39">[00:38:39]</a>, [01:08:56](<a class="yt-timestamp" data-t="01:08:56">[01:08:56]</a>, [01:41:46](<a class="yt-timestamp" data-t="01:41:46">[01:41:46]</a>).