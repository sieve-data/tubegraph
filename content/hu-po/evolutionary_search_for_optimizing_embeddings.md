---
title: Evolutionary search for optimizing embeddings
videoId: PFxi6SmozZ4
---

From: [[hu-po]] <br/> 

Evolutionary search is an [[Optimization Methods in Machine Learning | optimization method]] used to discover optimal values for parameters in machine learning models. In the context of "Long Rope" – a variant of [[rotary_position_embeddings_and_long_contexts | Rotary Position Embeddings]] (RoPE) – this technique is applied to fine-tune the parameters governing how [[positional_embeddings_in_transformers | positional information]] is encoded and extended for extremely long contexts in Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.

## Background: The Need for Optimization in Positional Embeddings

[[Positional embeddings in Transformers | Positional embeddings]] are crucial for Transformer models, as they provide explicit positional information about tokens in a sequence, allowing the model to understand order and relative distances <a class="yt-timestamp" data-t="02:29:51">[02:29:51]</a>. RoPE, specifically, encodes absolute positions within a rotation matrix and incorporates relative position dependency in self-attention <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>. A key property of RoPE is that it decays inter-token dependency with increasing relative distances, meaning closer tokens have stronger connections <a class="yt-timestamp" data-t="01:16:30">[01:16:30]</a>.

Previous methods for extending context length using [[positional_embeddings_in_transformers | positional embeddings]] interpolation, such as "Yarn," relied on human-led empirical experiments to group RoPE dimensions based on frequencies <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a>. This human-designed approach was identified as potentially suboptimal for new LLMs <a class="yt-timestamp" data-t="00:55:13">[00:55:13]</a>. Long Rope aims to overcome this by using an evolutionary search <a class="yt-timestamp" data-t="00:58:14">[00:58:14]</a>.

## How Evolutionary Search is Applied

The goal of the evolutionary search in Long Rope is to discover better non-uniform [[positional_embeddings_in_transformers | positional interpolations]] <a class="yt-timestamp" data-t="00:58:15">[00:58:15]</a>. Instead of arbitrary human guesses for specific parameters, the search algorithm systematically finds optimal values for two key elements:

1.  **Rescale Factors (`Lambda I`)**: These factors modify [[rotary_position_embeddings_and_long_contexts | RoPE]]'s rotation angles for each dimension based on token positions <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>. The search explores values for `Lambda I` typically between 0.01 and 1 <a class="yt-timestamp" data-t="01:04:56">[01:04:56]</a>.
2.  **Initial Non-Interpolated Tokens (`n_hat`)**: For the first `n_hat` tokens in the input sequence, no interpolation is applied to their [[positional_embeddings_in_transformers | positional embeddings]] <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>. This is hypothesized to be beneficial because initial tokens often receive large attention scores <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>.

### The Search Process

The evolutionary search follows these steps <a class="yt-timestamp" data-t="01:05:49">[01:05:49]</a>:
*   **Initialization**: A population `p` of [[positional_embeddings_in_transformers | rescale factors]] (Lambda) and `n_hat` values is started, including values from previous papers like PI, NTK, and Yarn <a class="yt-timestamp" data-t="01:05:53">[01:05:53]</a>.
*   **Mutation**: Individuals (sets of parameters) within the population are randomly mutated <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.
*   **Evaluation**: The LLM perplexity is computed for each individual (parameter set) <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>. Perplexity measures how well an LLM predicts a sample of text; lower perplexity is better <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.
*   **Selection**: The top `k` individuals (those with the lowest perplexity) are selected to become "parents" <a class="yt-timestamp" data-t="01:06:09">[01:06:09]</a>. Poor-performing individuals are discarded <a class="yt-timestamp" data-t="01:06:22">[01:06:22]</a>.
*   **Reproduction**: New variants, "children," are created based on the parents <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>. This process iterates, with good performing ones getting amplified and bad ones removed <a class="yt-timestamp" data-t="00:59:24">[00:59:24]</a>.

### Training Setup

The evolutionary search was conducted using:
*   **Models**: Llama 2 7B and Mistral 7B <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>.
*   **Dataset**: RedPajama, a large dataset (3 trillion tokens) chunked into 128k segments for fine-tuning <a class="yt-timestamp" data-t="01:08:34">[01:08:34]</a><a class="yt-timestamp" data-t="01:22:25">[01:22:25]</a>.
*   **Hardware**: 8 A100 GPUs and 16 A100 GPUs, indicating a substantial computational investment <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>.
*   **Strategy**: A progressive extension strategy, where models are first fine-tuned on smaller context lengths and then gradually on longer ones <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a><a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.

## Results and Impact

Long Rope achieved significant improvements:
*   It extended the context window of pre-trained LLMs to an impressive 2048k tokens (equivalent to 2 million tokens), approaching the context length capabilities observed in Gemini 1.5 <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a><a class="yt-timestamp" data-t="00:39:57">[00:39:57]</a>.
*   Models using Long Rope maintain low perplexity even at very high context lengths, unlike other models whose perplexity explodes with increased context <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.
*   It demonstrated 100% PassKey retrieval accuracy, a "needle in the haystack" task, even with extended context windows up to 2048k tokens <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>.
*   While there is a slight loss in performance on traditional short-context benchmarks like MMLU and HSwag, the ability to handle much longer contexts outweighs this, suggesting a need for new long-context-specific benchmarks <a class="yt-timestamp" data-t="01:13:54">[01:13:54]</a>.
*   Long Rope allows for an 8x context window extension without fine-tuning, and even greater extensions with the progressive fine-tuning strategy <a class="yt-timestamp" data-t="01:21:23">[01:21:23]</a>.

## Commentary: The Bitter Lesson and Future of Optimization

The use of evolutionary search to find optimal [[positional_embeddings_in_transformers | positional embedding]] parameters, while effective, raises a fundamental question about the future of [[Optimization Methods in Machine Learning | optimization]] in machine learning, often framed by "The Bitter Lesson" by Rich Sutton <a class="yt-timestamp" data-t="01:23:02">[01:23:02]</a>.

The Bitter Lesson posits that general methods leveraging computation by search and learning are ultimately the most effective, outperforming human-engineered or hard-coded features in the long term <a class="yt-timestamp" data-t="01:23:30">[01:23:30]</a><a class="yt-timestamp" data-t="01:24:07">[01:24:07]</a>. This contrasts with historical approaches in fields like computer vision, where hand-designed Gabor filters for edge detection were eventually superseded by convolutional neural networks that learned their own optimal filters through computation <a class="yt-timestamp" data-t="01:24:37">[01:24:37]</a><a class="yt-timestamp" data-t="01:25:30">[01:25:30]</a>.

In the case of [[positional_embeddings_in_transformers | positional embeddings]], methods like RoPE, Yarn, and now Long Rope represent increasingly complex human-designed heuristics involving sinusoids with different frequencies and arbitrary interpolation rules <a class="yt-timestamp" data-t="01:26:22">[01:26:22]</a><a class="yt-timestamp" data-t="01:44:57">[01:44:57]</a>. Even with evolutionary search to find optimal values for these human-designed parameters, the underlying approach remains rooted in human intuition <a class="yt-timestamp" data-t="01:26:50">[01:26:50]</a><a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>.

While [[future_of_learnable_position_embeddings | learned positional embeddings]] have been attempted in earlier research (e.g., in papers from 2017-2020), they have not yet outperformed hand-designed ones <a class="yt-timestamp" data-t="01:30:29">[01:30:29]</a>. However, proponents of the Bitter Lesson suggest that with sufficient scale in data and training, fully [[future_of_learnable_position_embeddings | learned positional embeddings]] will eventually surpass all heuristically hand-designed methods <a class="yt-timestamp" data-t="01:30:46">[01:30:46]</a>. This implies a future where the complex manual engineering and evolutionary searches for optimal parameters may become obsolete, replaced by models that learn these fundamental representations directly from vast amounts of data <a class="yt-timestamp" data-t="01:27:56">[01:27:56]</a><a class="yt-timestamp" data-t="01:46:10">[01:46:10]</a>.

It is speculated that Google's "secret sauce" for Gemini 1.5's extreme context length could either be an even more convoluted, hand-designed system like Long Rope, or potentially a breakthrough in truly [[future_of_learnable_position_embeddings | learned positional embeddings]] <a class="yt-timestamp" data-t="01:48:15">[01:48:15]</a>.

### Related Topics
*   [[Optimization Methods in Machine Learning | Optimization Methods in Machine Learning]]
*   [[Second order optimization in machine learning | Second order optimization in machine learning]]
*   [[Large Language Models as optimizers | Large Language Models as optimizers]]
*   [[Optimization Techniques and Challenges for 3D Scene Representation | Optimization Techniques and Challenges for 3D Scene Representation]]
*   [[Positional embeddings in Transformers | Positional embeddings in Transformers]]
*   [[Rotary Position Embeddings and Long Contexts | Rotary Position Embeddings and Long Contexts]]
*   [[Future of learnable position embeddings | Future of learnable position embeddings]]
*   [[Multimodal learning and embeddings | Multimodal learning and embeddings]]
*   [[Joint embedding predictive architecture | Joint embedding predictive architecture]]