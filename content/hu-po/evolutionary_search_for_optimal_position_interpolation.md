---
title: Evolutionary search for optimal position interpolation
videoId: PFxi6SmozZ4
---

From: [[hu-po]] <br/> 

[[long_rope | LongRope]] is a recent innovation in extending the context length of [[transformer]]-based Large Language Models (LLMs), drawing significant attention due to its potential connection to techniques used in Google's Gemini 1.5, which boasts state-of-the-art context lengths <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This approach, developed by Microsoft Research, is described as a "remix on a remix on a remix" of existing [[positional_embeddings | positional embedding]] concepts <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a> <a class="yt-timestamp" data-t="01:22:15">[01:22:15]</a>.

## The Role of Positional Embeddings

[[transformer]] models, being sequence-to-sequence architectures, require explicit [[positional_embeddings | positional information]] to understand the order of input tokens <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a> <a class="yt-timestamp" data-t="02:29:51">[02:29:51]</a>. This is typically provided through [[positional_embeddings | positional embeddings]] – small vectors added to the token embeddings that encode their position within the sequence <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a> <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

### Rotary Positional Embeddings (RoPE)

A significant advancement in [[positional_embeddings | positional embeddings]] came with [[rotary_positional_embeddings | RoPE]] (Rotary Position Embeddings), introduced in 2021 <a class="yt-timestamp" data-t="01:22:22">[01:22:22]</a> <a class="yt-timestamp" data-t="01:22:54">[01:22:54]</a>. [[rotary_positional_embeddings | RoPE]] is a hand-designed method that aims to model the dependency between elements at different positions in the sequence <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>. It encodes absolute position within a rotation matrix and incorporates relative position dependency into the self-attention formulation <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>. Key properties of [[rotary_positional_embeddings | RoPE]] include:
*   **Flexibility with sequence length**: It can be expanded to longer sequences <a class="yt-timestamp" data-t="01:16:28">[01:16:28]</a>.
*   **Decaying inter-token dependency**: The similarity (dot product) between tokens decreases as their relative distance increases <a class="yt-timestamp" data-t="01:16:30">[01:16:30]</a>. This aligns with the intuition that closer tokens should have a stronger connection <a class="yt-timestamp" data-t="01:17:20">[01:17:20]</a>.

The underlying mechanism of [[rotary_positional_embeddings | RoPE]] involves rotating the semantic meaning vectors of tokens using rotation angles derived from sine and cosine functions. Different dimensions of the [[positional_embeddings | position embedding]] vector are associated with different frequencies (e.g., lower dimensions have low frequencies, higher dimensions have high frequencies) <a class="yt-timestamp" data-t="00:44:07">[00:44:07]</a> <a class="yt-timestamp" data-t="01:37:54">[01:37:54]</a>.

## Limitations of Prior Context Extension Methods

Extending the context length of pre-trained LLMs beyond their original training limit (e.g., 4096 tokens for Llama 2) is challenging <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. Naive extrapolation of [[rotary_positional_embeddings | RoPE]] often leads to poor performance.

Prior methods, such as "Position Interpolation" (Pi) <a class="yt-timestamp" data-t="02:23:24">[02:23:24]</a> and its successors like "NTK-based interpolation" and "Yarn," attempted to address this by interpolating the existing [[rotary_positional_embeddings | RoPE]] values <a class="yt-timestamp" data-t="02:26:26">[02:26:26]</a>. However, these methods had limitations:
*   **Crowded position information**: Simple interpolation can make [[positional_embeddings | positional information]] too dense, hindering the model's ability to distinguish closely positioned tokens <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>.
*   **Human-designed heuristics**: Methods like Yarn divide [[rotary_positional_embeddings | RoPE]] dimensions into frequency-based groups, each with a different interpolation strategy <a class="yt-timestamp" data-t="02:54:10">[02:54:10]</a>. These groupings and strategies are based on human-led empirical experiments and arbitrary "nonlinear" boundaries, which may be suboptimal for new LLMs <a class="yt-timestamp" data-t="02:57:59">[02:57:59]</a>.

## LongRope's Innovation: Evolutionary Search for Optimal Interpolation

[[long_rope | LongRope]] improves upon these methods by replacing human-designed rules with an [[evolutionary_search_for_optimal_position_interpolation | efficient evolutionary search]] to discover optimal "non-uniform [[positional_embeddings | positional interpolations]]" <a class="yt-timestamp" data-t="02:58:11">[02:58:11]</a>.

The search targets two key forms of non-uniformity in [[positional_embeddings | positional interpolation]] <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>:
1.  **Fixed initial tokens (`n_hat`)**: The first `n_hat` positions in the sequence are explicitly *not* interpolated, retaining their original [[positional_embeddings | positional embeddings]] <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a> <a class="yt-timestamp" data-t="01:02:17">[01:02:17]</a>. This is hypothesized to be beneficial because initial tokens often receive large attention scores <a class="yt-timestamp" data-t="01:02:25">[01:02:25]</a>.
2.  **Dimension-dependent rescale factors (`Lambda_i`)**: The scaling of [[rotary_positional_embeddings | RoPE]]'s rotation angles (Theta) for subsequent tokens (beyond `n_hat`) varies across different dimensions of the embedding <a class="yt-timestamp" data-t="00:44:23">[00:44:23]</a> <a class="yt-timestamp" data-t="01:07:56">[01:07:56]</a>. This allows for differential interpolation based on the frequency characteristics of each dimension (e.g., low-frequency dimensions interpolated differently from high-frequency ones) <a class="yt-timestamp" data-t="02:54:52">[02:54:52]</a>.

### The Evolutionary Search Process

Instead of guessing these parameters, [[long_rope | LongRope]] uses an [[evolutionary_search_for_optimal_position_interpolation | evolutionary search algorithm]] <a class="yt-timestamp" data-t="00:58:50">[00:58:50]</a>:
1.  **Initial Population**: Start with a population of potential rescale factors and `n_hat` values, including those derived from prior methods like Pi, NTK, and Yarn <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.
2.  **Mutation**: Randomly mutate these parameters <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.
3.  **Evaluation**: Compute the LLM's perplexity (a measure of goodness, lower is better) for each set of parameters <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>.
4.  **Selection & Reproduction**: The top-performing individuals (those with low perplexity) become "parents" and are used to create variants (children) for the next generation <a class="yt-timestamp" data-t="01:06:09">[01:06:09]</a>. Poor-performing individuals are discarded <a class="yt-timestamp" data-t="01:06:22">[01:06:22]</a>.
5.  **Iteration**: This process is repeated iteratively, allowing the search to converge towards optimal values for the rescale factors and `n_hat` <a class="yt-timestamp" data-t="01:09:14">[01:09:14]</a>.

This computationally intensive search requires significant resources, with experiments conducted using 8 to 16 A100 GPUs <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>. Models like Llama 2 7B and Mistral 7B are fine-tuned on datasets like RedPajama, chunked into long segments for evaluation <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>.

## Performance and Implications

[[long_rope | LongRope]] demonstrates impressive results:
*   **Extended Context**: It extends LLM context windows to an "unprecedented 2048k tokens" <a class="yt-timestamp" data-t="01:19:47">[01:19:47]</a>.
*   **Perplexity**: Achieves low perplexity even at very high context lengths (2048k tokens) on Llama 2 and Mistral, unlike other methods which show exploding perplexity <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.
*   **PassKey Retrieval Accuracy**: Maintains near 100% accuracy in "needle in the haystack" tasks, where a specific five-digit number is hidden within a very long document <a class="yt-timestamp" data-t="01:11:40">[01:11:40]</a>.
*   **Progressive Extension**: It allows for a progressive fine-tuning strategy, starting with smaller context lengths and gradually increasing <a class="yt-timestamp" data-t="03:04:01">[03:04:01]</a>.
*   **Zero-Shot Extension**: Crucially, [[long_rope | LongRope]] can extend the context window by up to 8 times *without any fine-tuning* <a class="yt-timestamp" data-t="01:21:23">[01:21:23]</a>.
*   **Benchmark Retention**: While there is a slight drop in performance on traditional short-context benchmarks (like MMLU or H-SWAG), it's not catastrophic, and the models retain most of their original capabilities <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>.

This advancement suggests that models with extremely long context windows may eventually reduce the need for techniques like Retrieval Augmented Generation (RAG) for certain applications, as all necessary information could potentially fit within the LLM's context <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>.

## The "Bitter Lesson" and Future of Positional Embeddings

This approach, while highly effective, highlights an ongoing debate in AI research encapsulated by Rich Sutton's "Bitter Lesson" <a class="yt-timestamp" data-t="01:22:55">[01:22:55]</a>. Sutton posits that general methods leveraging computation (like search and learning) ultimately outperform human-engineered heuristics in the long term <a class="yt-timestamp" data-t="01:23:30">[01:23:30]</a>.

The history of computer vision provides an analogy: early methods relied on hand-designed filters (e.g., Gabor filters) to detect features like edges <a class="yt-timestamp" data-t="01:24:37">[01:24:37]</a>. However, convolutional neural networks (CNNs) eventually surpassed these by *learning* optimal filters directly from data <a class="yt-timestamp" data-t="01:25:30">[01:25:30]</a>.

Similarly, [[rotary_positional_embeddings | RoPE]] and its "remixes" like [[long_rope | LongRope]] represent increasingly complex human-designed heuristics for [[positional_embeddings | positional embeddings]] <a class="yt-timestamp" data-t="01:27:11">[01:27:11]</a>. While effective now, the long-term trend suggests that [[positional_embeddings | positional embeddings]] will eventually be entirely *learned* by the models themselves, similar to how token embeddings are learned <a class="yt-timestamp" data-t="01:27:35">[01:27:35]</a>. Although past attempts to learn [[positional_embeddings | positional embeddings]] directly have not outperformed hand-designed ones <a class="yt-timestamp" data-t="01:30:38">[01:30:38]</a>, the "Bitter Lesson" implies that with sufficient scale and computation, learned methods will ultimately prevail <a class="yt-timestamp" data-t="01:30:46">[01:30:46]</a>.