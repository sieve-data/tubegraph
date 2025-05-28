---
title: Compute Efficiency and Intelligent Routing
videoId: Teru_qIdB8Y
---

From: [[hu-po]] <br/> 

In the realm of Transformer-based language models, efficient compute allocation has become a critical challenge. Traditional Transformer models uniformly distribute floating-point operations (flops), which measure computational effort, across all input sequences [00:04:06]. This uniform allocation is largely due to the attention mechanism, which treats every token in a sequence equally, resulting in a quadratic computational complexity with respect to the input sequence length [00:14:23]. This approach, while powerful, can be inefficient as not all tokens require the same level of processing in every layer [00:41:17].

A key aspect of [[energy_and_compute_optimization_in_ai_models | Energy and Compute Optimization in AI Models]] is the reliance on static computation graphs [00:14:45]. These graphs define the exact operations and tensor sizes beforehand, allowing hardware (like GPUs) to maximize utilization [00:06:47]. Previous conditional computation techniques often suffered from dynamic computation graphs, which made efficient hardware execution problematic [00:06:36].

## Mixture of Depths (MoD)

The Mixture of Depths (MoD) architecture, developed by Google DeepMind in April 2024, addresses this challenge by enabling Transformers to dynamically allocate flops to specific positions within a sequence [00:04:51]. This technique optimizes compute allocation across model depth by making per-token decisions in each layer about whether to perform full computation or skip it [00:23:34].

### Core Mechanism: Skipping Blocks

MoD operates on the principle that not every token needs to pass through every Transformer block. A Transformer block consists of two main parts: the self-attention mechanism and the feed-forward network (MLP) [00:05:32]. Tokens can either engage with these computationally expensive components or bypass them entirely via a residual (or skip) connection [00:23:32].

This concept builds upon the idea of residual connections, first popularized by the Deep Residual Learning for Image Recognition paper in 2015, which introduced "ResNets" [00:24:20]. These connections allow information to skip layers, which can improve training and model performance [00:25:08]. In MoD, this skipping mechanism is made dynamic and context-sensitive at the token level [00:37:36].

### The Router

At the heart of MoD is a router that determines the computational path for each token [00:33:39]. This router produces a scalar weight for every token, indicating its preference to participate in a block's computation or to route around it [00:36:59].

MoD primarily utilizes a [[expert_choice_and_token_choice_routing | Top-K Routing Mechanism]] [00:38:07]:
*   **Capacity**: A predetermined "capacity" defines the total number of tokens allowed to participate in a given computation [00:40:40]. For example, a common capacity used in MoD is 50%, meaning only 50% of tokens will undergo full computation per block [00:36:54].
*   **Expert Choice Routing**: Unlike [[expert_choice_and_token_choice_routing | Token Choice Routing]], where tokens choose their preferred path and surplus tokens may be dropped [00:48:06], MoD employs [[expert_choice_and_token_choice_routing | Expert Choice Routing]] [00:51:45]. In this scheme, the computational paths (or "experts") themselves select the top-K tokens with the highest routing weights [00:50:53]. This guarantees perfect load balance within the computational graph, ensuring that all allocated compute resources are utilized without empty slots [00:50:01].

The router learns its routing decisions through training, as its internal weights are updated via gradient descent, similar to other model parameters [01:44:39].

### Efficiency Benefits

The primary advantage of MoD stems from its ability to reduce the computational burden of the self-attention mechanism. Since self-attention is an O(N²) operation (where N is sequence length) [00:35:50], reducing the effective sequence length processed by half (e.g., by skipping 50% of tokens) results in a 75% reduction in flops for that attention step (because (N/2)² = N²/4) [00:44:20].

This optimization leads to significant performance improvements:
*   **Faster Inference**: MoD models can be upwards of 50% faster during inference [00:08:39]. This translates to quicker responses for users interacting with models like ChatGPT [01:06:37].
*   **Improved Training Efficiency**: MoD models can achieve lower loss with the same amount of training time or flops as traditional Transformers [01:05:50].
*   **Higher Quality**: Beyond just speed, MoD models can also achieve lower losses (meaning better prediction accuracy) for an equivalent flop budget compared to baseline models [01:09:09]. This suggests a qualitative improvement, possibly due to the model learning to direct computation where it's most impactful [01:42:05].

## MoD vs. Mixture of Experts (MoE)

While MoD draws inspiration from [[expert_choice_and_token_choice_routing | Mixture of Experts]] (MoE) [00:03:07], there's a crucial distinction in their application of intelligent routing:
*   **MoE**: In an MoE model, a router typically selects one or more specialized MLP "experts" for each token to pass through within a layer [00:34:40]. The goal is often to improve quality or scale model capacity [00:03:09].
*   **MoD**: In contrast, the MoD router's primary role is to decide whether a token engages with the *entire* Transformer block (including the self-attention and MLP) or skips it completely [00:35:12]. This directly targets [[energy_and_compute_optimization_in_ai_models | Energy and Compute Optimization in AI Models]] by reducing the total compute per token.

### Combining MoD and MoE

The paper explores combining MoD with MoE, creating "Mixture of Depths and Experts" (MoDE) [01:17:06]. Two main variants are proposed:
*   **Staged MoDE**: This involves adding an MoD router *before* an existing MoE block, allowing tokens to skip the entire attention and MLP computation [01:18:18]. This maximizes compute efficiency by bypassing the expensive self-attention [01:20:02].
*   **Integrated MoDE**: This simplifies the routing machinery by integrating a "noop" (no-operation) expert directly into the existing MoE's MLP experts [01:18:41]. While simpler to implement for existing MoE models, it only allows skipping the MLP, not the self-attention [01:20:33].

## Training and Inference Adaptations

A challenge arises during autoregressive sampling (inference) because the top-K routing used in training is "non-causal" – it requires knowing all token weights in the sequence [00:55:39]. For inference, where tokens are predicted one by one, future tokens are unknown [01:21:48]. MoD addresses this by training an auxiliary MLP predictor that learns to predict whether a token will be among the top-K or not, allowing for causal routing during inference with minimal performance degradation [00:57:52].

## Architectural Implications

MoD also highlights broader architectural insights:
*   **Depth over Width**: When adding flops to a model, it's empirically better to add depth (more layers/blocks) than to add width (more neurons per layer) [01:12:21]. This reinforces the long-held intuition in deep learning that deeper networks can learn richer hierarchies of features [01:12:10].
*   **KV Cache Optimization**: The reduced processing means the KV cache (storing key and value vectors for attention) can be more efficiently managed, potentially allowing for larger effective context windows during autoregressive sampling [01:32:00].

The generic nature of MoD's routing mechanism opens doors for future [[optimization_by_prompting_opro | Optimization Techniques in Surfels]] and integrations, such as routing tokens to specialized "experts" for tasks like memory lookup or tool use, rather than just computational blocks [01:34:40]. This suggests a future where models dynamically tailor their internal computations based on context and task needs.