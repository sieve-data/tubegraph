---
title: comparison of recurrent networks and Transformers
videoId: Xk8FtcSlFxs
---

From: [[hu-po]] <br/> 

The discussion around [[test time scaling]] in machine learning models highlights significant architectural differences between Transformers and recurrent neural networks (RNNs), such as LSTMs and Mambas, particularly concerning their performance at inference time and their respective approaches to reasoning.

## Transformers

Transformers are characterized by a fixed number of layers, implying a fixed depth of computation for each token during processing <a class="yt-timestamp" data-t="01:08:04">[01:08:04]</a>.

### Scalability and Memory
The core of a Transformer's operation relies on its attention mechanism, which leads to a [[performance_and_scalability_of_diffusion_models_with_transformers | quadratic scaling of compute and memory]] with respect to sequence length <a class="yt-timestamp" data-t="01:18:14">[01:18:14]</a>. This is due to the KV (Key-Value) cache, which accumulates information from all previous tokens in the sequence, causing it to grow with the sequence length <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>. This quadratic scaling makes it computationally intensive to handle very long reasoning traces, as the memory required on an edge device might become insufficient <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>.

### Reasoning in Token Space
Transformers, especially large language models (LLMs) like those from OpenAI (e.g., O3), predominantly reason in "token space" <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a>. This means their reasoning traces are sequences of tokens, which are readily understandable and interpretable by humans <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>. For instance, a model might explicitly verbalize its thought process ("let's break down the process of counting") <a class="yt-timestamp" data-t="01:11:40">[01:11:40]</a>.

### Training and Distributed Systems
Training large Transformer models often requires massive compute clusters with very fast interconnects, such as the conceptual "Stargate" data centers, to push large gradients into the models <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. The slowest link in this training chain is often the communication between GPUs <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a>.

## Recurrent Neural Networks (RNNs) and State-Space Models (Mambas)

Recurrent networks, including LSTMs and newer architectures like [[comparisons_between_mambas_and_transformers | Mambas]], approach sequence processing differently.

### Scalability and Memory
Unlike Transformers, RNNs and Mambas maintain a fixed-size hidden state or memory, which they constantly interact with <a class="yt-timestamp" data-t="01:16:59">[01:16:59]</a> <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>. This results in [[performance_and_scalability_of_diffusion_models_with_transformers | linear scaling]] with sequence length, making them significantly more efficient for very long sequences compared to Transformers' quadratic scaling <a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a>.

### Reasoning in Latent Space
A key advantage of recurrent architectures in the context of [[scalable_diffusion_models_with_Transformers | test time scaling]] is their ability to reason in a continuous latent space rather than being limited to token space <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>. This "latent weaving" allows for a more continuous and less constrained reasoning process, potentially leading to more interesting and powerful reasoning traces <a class="yt-timestamp" data-t="01:19:08">[01:19:08]</a>. However, this comes at the cost of interpretability, as it is much harder to understand what the model is doing internally <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>.

An example of latent reasoning is a model keeping track of a number by subtly shifting its latent state in a specific direction, akin to a "latent abacus" <a class="yt-timestamp" data-t="01:15:23">[01:15:23]</a>.

### Training and Inference
While RNNs can be slower to train due to the need for [[invertible neural networks | truncated backpropagation]] (which limits the length of the gradient chain) <a class="yt-timestamp" data-t="01:10:49">[01:10:49]</a>, they can be much faster for inference—potentially "100 times faster" than Transformer-based models for equivalent "thinking" <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. This makes them highly suitable for edge devices like cell phones or robots, where memory and compute are constrained but long reasoning might be required <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>.

Furthermore, recurrent depth networks perform more floating-point operations (FLOPs) per parameter, reducing communication costs between accelerators. This enables higher device utilization, especially when training with slower interconnects, making them potentially better suited for [[dynamic_token_routing_in_transformers | distributed training]] systems compared to Transformers <a class="yt-timestamp" data-t="01:24:27">[01:24:27]</a>.

## Key Differences and Emerging Trends

| Feature             | Transformers                                                                                                        | Recurrent Networks (LSTMs/Mambas)                                                                                                    |
| :------------------ | :------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------- |
| **Scaling (Memory/Compute)** | Quadratic with sequence length <a class="yt-timestamp" data-t="01:18:14">[01:18:14]</a>                                                                                        | Linear with sequence length <a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a>                                                                                                  |
| **Memory**          | Growing KV cache <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>                                                                                                 | Fixed hidden state/memory <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>                                                                                                    |
| **Reasoning Space** | Token space ("word cells"), interpretable <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a> <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>                                           | Latent space ("latent weavers"), less interpretable but potentially more powerful <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a> <a class="yt-timestamp" data-t="01:12:26">[01:12:26]</a> |
| **Inference Speed** | Slower with increasing reasoning trace length due to memory overhead <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>                                                     | Potentially 100x faster for long reasoning traces <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>                                                                           |
| **Training**        | Requires fast interconnects for distributed training; model parallelism is communication-heavy <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a> | More FLOPs per parameter, less communication cost; better for slower interconnects in distributed training <a class="yt-timestamp" data-t="01:24:44">[01:24:44]</a>    |
| **Application Focus** | Training large, complex models <a class="yt-timestamp" data-t="01:32:31">[01:32:31]</a>                                                                                              | Edge devices (phones, robots) where efficiency is critical <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>                                                                   |

### Hybrid Approaches and Distillation
While the "Attention Is All You Need" paper suggested doing away with RNNs entirely, current trends indicate a potential return to hybrid architectures that combine aspects of both Transformers and RNNs (LSTMs, GRUs, Mambas) <a class="yt-timestamp" data-t="01:26:02">[01:26:02]</a>. This is because the ability of RNNs to perform variable, long-duration computation per token, which is essential for extensive reasoning at inference, complements the Transformer's strengths in capturing long-range dependencies during training <a class="yt-timestamp" data-t="01:26:10">[01:26:10]</a>.

[[Distillation]] is seen as a key tool to bridge the gap between powerful, large models (often Transformers) and efficient, smaller models (potentially RNNs/Mambas) designed for edge deployment <a class="yt-timestamp" data-t="01:31:30">[01:31:30]</a>. A large, sophisticated model can be trained (perhaps with reinforcement learning (RL) to internalize complex reasoning strategies) and then its knowledge distilled into a smaller model, even if the architectures are completely different <a class="yt-timestamp" data-t="01:32:16">[01:32:16]</a>. This allows for the deployment of highly intelligent models on resource-constrained devices <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>.

### The Role of [[performance_and_scalability_of_diffusion_models_with_transformers | Reinforcement Learning]] (RL)
RL plays an increasingly important role in improving reasoning models. Larger models trained with RL can autonomously develop and execute their own test-time reasoning strategies, reducing the need for explicit human-engineered search methods like beam search <a class="yt-timestamp" data-t="02:29:08">[02:29:08]</a>. This suggests that RL will primarily be applied to the large models, and then their improved reasoning capabilities will be transferred to smaller, inference-optimized models through distillation <a class="yt-timestamp" data-t="01:30:27">[01:30:27]</a>.

This implies a future where core intelligence is cultivated in large, centralized models via RL and then efficiently deployed to a wide range of edge devices through architecture-agnostic distillation <a class="yt-timestamp" data-t="01:30:38">[01:30:38]</a>.