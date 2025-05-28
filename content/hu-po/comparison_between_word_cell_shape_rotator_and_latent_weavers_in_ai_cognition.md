---
title: Comparison between word cell shape rotator and latent Weavers in AI cognition
videoId: Xk8FtcSlFxs
---

From: [[hu-po]] <br/> 

Understanding how Artificial Intelligence models "think" is crucial for their development and deployment. The field explores different modes of internal reasoning, moving beyond simple token-based processing to more complex, continuous, and potentially more powerful forms of cognition. This article explores three conceptual models for AI cognition: the word cell, the shape rotator, and the emergent latent weaver.

## The Word Cell: Reasoning in Token Space

The "word cell" concept describes an AI model that primarily reasons in terms of words and ideas, similar to how humans might experience an internal monologue <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>. In the context of AI, this translates to models whose internal reasoning trace is limited to discrete token space <a class="yt-timestamp" data-t="01:02:00">[01:12:00]</a>.

*   **Mechanism**: Current Large Language Models (LLMs) like DeepSeek's reasoning models operate by producing a sequence of tokens in their "thinking" process before generating a final answer <a class="yt-timestamp" data-t="03:59:51">[03:59:51]</a>. This means their internal thought process is explicitly verbalized and visible in token form <a class="yt-timestamp" data-t="01:12:34">[01:12:34]</a>.
*   **Interpretability**: A key "feature" of reasoning in token space is its interpretability. Humans can "read" the model's mind by examining its internal monologue, understanding the steps it takes to arrive at a conclusion <a class="yt-timestamp" data-t="01:11:39">[01:11:39]</a>.
*   **Limitations**: This approach can be computationally expensive as the reasoning trace grows, potentially leading to memory limitations on edge devices, especially with [[comparison_of_rwkv_with_transformer_architectures | Transformer]] architectures that exhibit quadratic scaling of memory with sequence length <a class="yt-timestamp" data-t="01:20:09">[01:20:09]</a>.

## The Shape Rotator: Multimodal Visualization of Thought

The "shape rotator" concept refers to an AI that thinks primarily in images and spatial terms, excelling at visualizing and mentally manipulating objects <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. This is analogous to how animals, like cats, might think by visualizing paths and movements rather than verbalizing them <a class="yt-timestamp" data-t="01:02:16">[01:02:16]</a>.

*   **Mechanism**: In AI, this is exemplified by multimodal models that integrate visual thought into their reasoning process. For instance, some models use verbal thought to condition an image generation model, then convert the generated image into "vision tokens" that are fed back into the reasoning chain <a class="yt-timestamp" data-t="00:59:27">[00:59:27]</a>.
*   **Advantages**: Early research suggests that integrating visual thought can improve performance on tasks like maze solving, demonstrating the benefit of moving beyond purely verbal reasoning <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.
*   **Challenges**: Understanding the thought process of a shape rotator AI is more complex than a word cell due to its non-verbal nature <a class="yt-timestamp" data-t="01:12:04">[01:12:04]</a>.

## The Latent Weaver: Reasoning in Latent Spaces

The "latent weaver" represents an advanced form of AI cognition where reasoning occurs entirely within a [[generative_latent_spaces_in_ai | continuous latent space]] <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This allows for thinking that is not constrained by discrete tokens or explicit visual representations.

*   **Mechanism**: Models employing a [[recurrent_depth_approach_in_ai_and_its_advantages_over_transformers | recurrent depth approach]] operate by embedding input data into a high-dimensional continuous latent space <a class="yt-timestamp" data-t="01:04:48">[01:04:48]</a>. A recurrent block then iteratively processes this embedding, performing computations in this latent space, akin to a variable-depth Transformer <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. This internal process is not verbalized but involves transformations of numerical vectors <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>.
*   **Advantages**:
    *   **Increased Capacity**: Reasoning in a continuous latent space offers significantly more capacity and flexibility for complex thought processes compared to discrete token space <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a>.
    *   **Efficiency for Test-Time Scaling**: Recurrent models like LSTMs or Mambas (which are related to RNNs) maintain a fixed-size memory, leading to linear scaling of compute with sequence length, unlike the quadratic scaling of Transformers <a class="yt-timestamp" data-t="01:17:45">[01:17:45]</a>. This allows for "100 times more thinking" (longer reasoning traces) at inference time without prohibitive memory costs <a class="yt-timestamp" data-t="01:19:37">[01:19:37]</a>.
    *   **Decentralized Training**: Recurrent depth networks reduce communication costs between accelerators, enabling more efficient training in distributed systems as they perform more computations locally before requiring data transfer <a class="yt-timestamp" data-t="01:24:02">[01:24:02]</a>.
*   **Interpretability Challenge**: Similar to shape rotators, understanding the internal reasoning of a latent weaver is difficult, as it's not directly human-readable <a class="yt-timestamp" data-t="01:12:26">[01:12:26]</a>. However, visualizations (like PCA of latent space trajectories) can offer some insight into how these models process information, such as converging to a fixed point or performing iterative "counting" via a "latent abacus" <a class="yt-timestamp" data-t="01:13:06">[01:13:06]</a>.

## Comparison and Future Directions

| Feature             | Word Cell (Token Space)                                | Shape Rotator (Visual Space)                                | Latent Weaver (Latent Space)                                      |
| :------------------ | :----------------------------------------------------- | :---------------------------------------------------------- | :---------------------------------------------------------------- |
| **Reasoning Medium** | Discrete tokens                                        | Images, spatial terms (converted to vision tokens)          | Continuous high-dimensional vectors                         |
| **Primary Model**   | Standard LLMs (e.g., DeepSeek)                         | [[vision_language_models_in_ai_agents | Vision language models]] with multimodal Chain-of-Thought | [[recurrent_depth_approach_in_ai_and_its_advantages_over_transformers | Recurrent Neural Networks]] (RNNs), LSTMs, Mambas |
| **Interpretability**| High (human-readable monologue)                        | Low (non-verbal, requires visualization)                    | Very Low (abstract, requires dimensionality reduction for insight)|
| **Capacity/Flex.**  | Limited by discrete vocabulary and token sequence      | Expanded by visual modalities                               | High (continuous, unconstrained by discrete tokens)               |
| **Computational Scalability** | Quadratic memory growth with sequence length for Transformers, inefficient for very long reasoning traces <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a> | Varies based on architecture, often similar to LLMs for textual part | Linear scaling, constant memory for long reasoning traces, efficient for edge devices <a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a> |

The trend in AI cognition suggests a move towards models that reason in more complex and abstract ways. While current models primarily exhibit word-cell-like "thinking," the emergence of multimodal models hints at shape-rotator-like internal processes. The ultimate frontier, however, appears to be the latent weaver, where reasoning occurs in a [[continuous_vs_discrete_latent_spaces_in_ai | continuous latent space]] <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>.

This shift has significant implications for [[future_directions_and_implications_of_ai_in_vision_language_models | AI development]]:
*   **Distillation**: Large, highly intelligent models (trained with techniques like RL) will likely be distilled into smaller, optimized models that run efficiently on edge devices like smartphones or robots <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. This "distillation" process can transfer knowledge even between models with different architectures, allowing for specialized inference models <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
*   **Self-Improvement**: AI models demonstrate a "Transcendence" effect where they can generalize beyond their training data through self-improvement loops <a class="yt-timestamp" data-t="00:45:54">[00:45:54]</a>. This process relies on filtering self-generated outputs (e.g., using majority voting among multiple models) to ensure data quality and avoid degradation, creating a self-improving "flywheel" <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>.
*   **Tool Use**: [[Vision language models in AI agents | Reasoning models]] will increasingly integrate external tool use (e.g., calculators, code interpreters) into their reasoning chains, with Reinforcement Learning (RL) enabling them to autonomously develop and execute their own test-time reasoning strategies <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.

Ultimately, the development of latent weavers could enable vastly more powerful and efficient AI agents capable of complex internal thought processes on a wide range of devices, even if those thoughts remain inscrutable to human observation <a class="yt-timestamp" data-t="01:21:56">[01:21:56]</a>.