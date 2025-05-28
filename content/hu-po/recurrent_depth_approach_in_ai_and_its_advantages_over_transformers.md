---
title: Recurrent depth approach in AI and its advantages over Transformers
videoId: Xk8FtcSlFxs
---

From: [[hu-po]] <br/> 

The recurrent depth approach in AI is a method for [[Deep Learning and Neural Networks | models]] to perform [[Chain of Thought Decoding in AI | reasoning]] in a continuous latent space rather than relying solely on token-based [[Chain of Thought Decoding in AI | thought processes]] <a class="yt-timestamp" data-t="01:03:14">[01:03:14]</a>. This approach allows for significantly increased "thinking" or computation during inference, leading to improved performance <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>.

## Core Concept

Traditional [[Deep Learning and Neural Networks | language models]] (LLMs) like [[Foundation models in AI | Transformers]] primarily reason by generating sequences of tokens, which can be thought of as an "inner monologue" or "verbal Chain of Thought" <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>. This process occurs in discrete token space, meaning each step of reasoning is a word or sub-word unit <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>.

The recurrent depth approach, as described in the paper "Scaling Up Test Time Compute with Latent Reasoning: A Recurrent Depth Approach," proposes that models can improve by reasoning *entirely* in a continuous latent space <a class="yt-timestamp" data-t="01:03:18">[01:03:18]</a>. This contrasts with the "wasteful" projection of internal reasoning into discrete verbalized tokens <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>. The term "latent Weavers" is used to describe models that natively think in their continuous latent space <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>.

### Model Architecture

A model utilizing recurrent depth is typically structured around decoder-only [[Foundation models in AI | Transformer]] blocks <a class="yt-timestamp" data-t="01:04:39">[01:04:39]</a>. It consists of three main components:
1.  **Prelude (Encoder)**: Embeds the input data (sequence of tokens) into a high-dimensional continuous latent space <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a>.
2.  **Recurrent Block**: Takes the latent embedding and a noise input, performing iterative computations to produce a new state in the latent space <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. This block performs the "reasoning" in the embedding space <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>. The number of recurrences (`R`) can vary during the forward pass, allowing for dynamic computation based on problem complexity <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a>.
3.  **Coda (Decoder)**: Unembeds the final latent state back into token space, producing a probability distribution over possible output tokens <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.

Functionally, a model with only eight "real" layers, when its recurrent block is iterated, can achieve an effective depth of 132 layers <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>. This allows for computational chains deeper than even the largest fixed-depth [[Foundation models in AI | Transformers]] <a class="yt-timestamp" data-t="01:10:17">[01:10:17]</a>.

## Advantages over Transformers

The recurrent depth approach offers several advantages, particularly in the context of "test time scaling" – increasing compute at inference time to improve accuracy <a class="yt-timestamp" data-t="01:26:48">[01:26:48]</a>.

### Variable Depth and Efficiency
*   **Variable Computation**: Unlike [[Foundation models in AI | Transformers]] which have a fixed number of layers and thus a fixed amount of computation per token <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>, recurrent models can have a variable amount of layers or computation per token by iterating the recurrent block <a class="yt-timestamp" data-t="01:08:36">[01:08:36]</a>.
*   **Linear Scaling**: This approach shares similarities with [[Transition from Transformers to recurrent neural networks RNNs | recurrent neural networks (RNNs)]] and LSTMs, which exhibit linear scaling with sequence length in terms of memory and computation <a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a>. This is a significant advantage over [[Foundation models in AI | Transformer]] models, where the attention mechanism leads to quadratic scaling of memory and compute with sequence length <a class="yt-timestamp" data-t="01:18:14">[01:18:14]</a>. This means [[Transition from Transformers to recurrent neural networks RNNs | LSTMs]] can be "100 times faster" <a class="yt-timestamp" data-t="01:19:33">[01:19:33]</a>, allowing for 100 times more "thinking" <a class="yt-timestamp" data-t="01:19:37">[01:19:37]</a>.
*   **Edge Device Suitability**: The fixed memory footprint of recurrent models makes them highly suitable for edge devices like cell phones or robots, where memory is limited <a class="yt-timestamp" data-t="01:20:26">[01:20:26]</a>. This contrasts with [[Foundation models in AI | Transformers]] which require a growing KV cache as the reasoning trace lengthens <a class="yt-timestamp" data-t="01:20:30">[01:20:30]</a>.

### Training and Distributed Systems
*   **Reduced Communication Cost**: Recurrent depth networks perform more floating-point operations (flops) per parameter than standard [[Foundation models in AI | Transformers]] <a class="yt-timestamp" data-t="01:22:36">[01:22:36]</a>. This significantly reduces the communication cost between accelerators during training at scale, as more computation can be done locally on each device <a class="yt-timestamp" data-t="01:22:40">[01:22:40]</a>.
*   **Distributed Training**: This characteristic enables higher device utilization and makes it more feasible to train [[Deep Learning and Neural Networks | models]] with slower interconnects, potentially leading to more distributed training paradigms rather than relying solely on giant data centers with very fast networking <a class="yt-timestamp" data-t="01:24:26">[01:24:26]</a>.

## Challenges and Observations

### Interpreting Latent Reasoning
One challenge with reasoning in latent space is the difficulty in interpreting the thought process <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>. Unlike token-based reasoning (where the inner monologue is explicit and readable) <a class="yt-timestamp" data-t="01:11:32">[01:11:32]</a>, latent reasoning occurs in a continuous, high-dimensional vector space, making it opaque to human understanding <a class="yt-timestamp" data-t="01:12:16">[01:12:16]</a>.

However, attempts to visualize the latent reasoning space using dimensionality reduction techniques like PCA reveal interesting behaviors:
*   **Fixed Points**: Many tokens converge to a fixed point in the latent space, indicating the model has settled on its conclusion <a class="yt-timestamp" data-t="01:13:38">[01:13:38]</a>.
*   **Loops**: The latent trajectory can enter loops, suggesting the model is repeating a pattern of computation <a class="yt-timestamp" data-t="01:13:46">[01:13:46]</a>.
*   **Sliders**: Trajectories can noticeably drift in a specific direction, potentially serving as a mechanism for the model to "count" or keep track of iterations <a class="yt-timestamp" data-t="01:14:09">[01:14:09]</a>. This is akin to a "latent Abacus" <a class="yt-timestamp" data-t="01:16:01">[01:16:01]</a>.

### Training Recurrent Depth Models
Training [[Transition from Transformers to recurrent neural networks RNNs | recurrent neural networks]] traditionally faced challenges due to the need to backpropagate gradients through potentially infinite-length chains, leading to high memory consumption <a class="yt-timestamp" data-t="01:10:25">[01:10:25]</a>. The recurrent depth approach often employs truncated backpropagation, where gradients are only pushed through the last `K` iterations, mitigating these issues <a class="yt-timestamp" data-t="01:10:48">[01:10:48]</a>.

## Implications

The re-emergence of [[Transition from Transformers to recurrent neural networks RNNs | RNN-like architectures]] for test-time scaling suggests a potential [[Transition from Transformers to recurrent neural networks RNNs | shift away from the pure Transformer paradigm]] <a class="yt-timestamp" data-t="01:20:41">[01:20:41]</a>. While [[Foundation models in AI | Transformers]] excel in many areas, their memory scaling limits the depth of reasoning they can perform on edge devices <a class="yt-timestamp" data-t="01:20:09">[01:20:09]</a>. A hybrid approach, combining the strengths of both architectures, may become prevalent <a class="yt-timestamp" data-t="01:25:35">[01:25:35]</a>.

The ability to reason efficiently in latent space could profoundly impact the development of [[Challenges and improvements in animated AI models | AI models]] for robotics and other applications where hardware footprint is a concern <a class="yt-timestamp" data-t="01:21:44">[01:21:44]</a>. This means future robots might "think" not by generating verbose internal monologues, but by performing extensive computations in their internal latent representations <a class="yt-timestamp" data-t="01:22:09">[01:22:09]</a>.