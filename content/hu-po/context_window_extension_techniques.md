---
title: Context window extension techniques
videoId: PFxi6SmozZ4
---

From: [[hu-po]] <br/> 

Large Language Models (LLMs) rely on a "context window" or "context length," which dictates the amount of information a Transformer can attend to simultaneously [00:02:29](<a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Extending this context window is a desirable feature [00:02:29](<a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For instance, [[long_context_windows_in_large_language_models | Gemini 1.5]] from Google boasts state-of-the-art context length, though its specific innovations remain undisclosed by DeepMind's head, Demis Hassabis [00:02:24](<a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, [00:02:51](<a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Achieving extremely long context windows, such as 10 million tokens, requires new innovations [00:02:56](<a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Transformers are fundamental to many AI applications, including video understanding, diffusion models, and language models [00:03:16](<a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. A significant increase in input length or context provides a substantial advantage [00:03:33](<a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Understanding Positional Embeddings

Transformers are sequence-to-sequence models that process inputs as a list of tokens [00:06:13](<a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. They do not inherently understand the order of these tokens, necessitating the explicit injection of positional information [00:22:50](<a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. This is achieved through **positional embeddings (PE)** [00:06:38](<a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### Basic Concept of Positional Embeddings

Positional embeddings are vectors that inform the Transformer about a token's position within a sequence [00:06:47](<a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Example (Vision Transformer):** When an image is converted into a sequence of visual patches (tokens), small purple squares with numbers (0, 1, 2, 3, etc.) represent the position embeddings [00:06:09](<a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, [00:06:34](<a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Example (Language Model):** In a simplified model with a vocabulary of three words (A, B, C) and a fixed context length, each position (e.g., 0, 1, 2) has a corresponding position embedding vector [00:10:17](<a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. These position vectors are typically added to the token embeddings before being fed into the Transformer [00:10:50](<a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

Unlike token embeddings, which are learned high-dimensional vectors representing semantic meaning [00:08:48](<a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, traditional positional embeddings are often "hand-engineered" [00:11:43](<a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>, [00:32:29](<a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>. They appear as "weird hardcoded kind of looking repeating patterns" derived from sinusoidal functions with varying frequencies [00:12:01](<a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>, [00:31:37](<a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>.

### Rotary Position Embeddings (RoPE)

**RoPE** (Rotary Position Embeddings) emerged from the 2021 RoFormer paper [00:12:43](<a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>, [00:12:57](<a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Goal:** To model the dependency between elements at different positions in a sequence and extract meaning from the *relative* position of tokens [00:13:37](<a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>, [00:13:51](<a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   **Properties:**
    *   Flexibility with respect to sequence length [00:16:28](<a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.
    *   Decays inter-token dependency with increasing relative distances (i.e., closer tokens have more similarity) [00:16:30](<a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   **Intuition (Rotation Matrix):** The core idea is to rotate the token embedding vectors by an angle that depends on their position [00:19:18](<a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>, [00:20:38](<a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>. This rotation affects the dot product (a measure of similarity) between query and key vectors in the self-attention mechanism, ensuring that tokens closer together have higher attention scores [00:19:50](<a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>, [00:20:45](<a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.
*   **Mathematical Formulation:** RoPE encodes absolute position within a rotation matrix and incorporates relative position dependency into the self-attention [00:16:14](<a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. Using Euler's identity, the complex exponential terms can be expressed as cosines and sines [00:30:32](<a class="yt-timestamp" data-t="00:30:32">[00:30:32]</a>, [00:30:40](<a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>. The self-attention score then becomes dependent on the relative position `m - n` between tokens [00:30:57](<a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>. The frequencies of these sinusoidal functions vary across the embedding dimensions, resulting in the complex patterns observed in positional embedding visualizations [00:32:05](<a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>, [00:32:38](<a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>. RoPE is a continuous function that can be discretized to obtain position embeddings for a given context length [00:33:22](<a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>.

## LongRoPE: A Novel Approach to Context Extension

LongRoPE, a Microsoft Research paper from February 2024, is a "remix" of previously developed RoPE extensions [00:36:38](<a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>, [01:03:59](<a class="yt-timestamp" data-t="01:03:59">[01:03:59]</a>. It extends LLM context windows to an "unprecedented" 2048K tokens [01:19:47](<a class="yt-timestamp" data-t="01:19:47">[01:19:47]</a>.

### Building on Previous Work

Previous methods to extend RoPE include:
*   **Position Interpolation (PI):** Linearly scales the RoPE frequency values across all dimensions [00:42:16](<a class="yt-timestamp" data-t="00:42:16">[00:42:16]</a>, [00:50:38](<a class="yt-timestamp" data-t="00:50:38">[00:50:38]</a>. However, this "crowds" the positional information, making it hard for the model to distinguish closely positioned tokens [00:50:50](<a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.
*   **NTK-based Interpolation:** Splits low- and high-frequency dimensions and rescales them differently [00:53:22](<a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>.
*   **YARN:** Divides RoPE dimensions into three frequency-based groups, each with a different interpolation strategy [00:54:08](<a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>. YARN's grouping relies on "human-led empirical experiments," which can lead to suboptimal performance for new LLMs [00:55:11](<a class="yt-timestamp" data-t="00:55:11">[00:55:11]</a>.

LongRoPE aims to improve upon these by addressing their reliance on "human-designed rules" and exploring "unexplored nonlinearities" [00:57:59](<a class="yt-timestamp" data-t="00:57:59">[00:57:59]</a>.

### Key Innovations of LongRoPE

1.  **Non-Uniformities in Positional Interpolation:** LongRoPE identifies and exploits non-uniformities by finding effective rescale factors for RoPE's rotation angles across each dimension, based on token positions [00:37:48](<a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>, [00:43:29](<a class="yt-timestamp" data-t="00:43:29">[00:43:29]</a>. This means different parts of the positional embedding vector (corresponding to different frequencies) are scaled differently [00:44:03](<a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>.
    *   Crucially, for an initial `n_hat` number of tokens (e.g., 256), no interpolation is applied [01:00:17](<a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>, [01:02:22](<a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a>. This is based on the hypothesis that initial tokens receive large attention scores and are critical [01:01:35](<a class="yt-timestamp" data-t="01:01:35">[01:01:35]</a>.
2.  **Evolutionary Search for Optimal Parameters:** Instead of human guesswork, LongRoPE uses an evolutionary search algorithm to discover the optimal values for these non-uniform rescale factors (Lambda I) and the `n_hat` parameter [00:45:24](<a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>, [00:58:11](<a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>.
    *   The search process involves:
        *   Starting with a population of rescale factors.
        *   Randomly mutating them.
        *   Computing the LLM's perplexity for each.
        *   Selecting top-performing individuals as "parents" to create variants, while discarding poorly performing ones [01:05:51](<a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.
        *   This iterative process aims to find the best `Lambda` and `n_hat` values [01:06:57](<a class="yt-timestamp" data-t="01:06:57">[01:06:57]</a>.
    *   This search was conducted on Llama 2 7B and Mistral 7B models, fine-tuned on subsets of the RedPajama dataset (3 trillion tokens) [01:08:24](<a class="yt-timestamp" data-t="01:08:24">[01:08:24]</a>, [01:10:14](<a class="yt-timestamp" data-t="01:10:14">[01:10:14]</a>. The search required significant computational resources (8 A100 GPUs, then 16 A100 GPUs) [01:09:44](<a class="yt-timestamp" data-t="01:09:44">[01:09:44]</a>.
3.  **Progressive Extension Strategy:** For extremely long contexts, a fine-tuning strategy is employed where the model is first fine-tuned on a smaller context length, and then gradually increases the context length in subsequent fine-tuning stages [00:38:04](<a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>, [01:03:01](<a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. This allows for smooth adaptation to longer sequences [01:03:04](<a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>.

### Performance Metrics

LongRoPE was evaluated using several metrics:

*   **Perplexity (Lower is Better):** LongRoPE (Mistral and Llama 2 versions) maintained low perplexity even as the context window size increased to 2048K tokens, unlike other models (CodeLlama, Yarn Llama) which saw an explosion in perplexity [00:39:30](<a class="yt-timestamp" data-t="00:39:30">[00:39:30]</a>, [00:40:43](<a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.
*   **Pass Key Retrieval Accuracy (Higher is Better):** In a "needle in the haystack" task (finding a hidden five-digit number in a long document), LongRoPE models consistently achieved nearly 100% accuracy, even at very long context lengths (up to 256K) [01:10:06](<a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>, [01:11:40](<a class="yt-timestamp" data-t="01:11:40">[01:11:40]</a>. Other models largely failed to retrieve the pass key beyond their trained context length [01:12:08](<a class="yt-timestamp" data-t="01:12:08">[01:12:08]</a>.
*   **General Benchmarks:** When evaluated on standard benchmarks like MMLU, HellaSwag, and TruthfulQA, LongRoPE models showed only a slight decrease in performance compared to their original versions [01:13:31](<a class="yt-timestamp" data-t="01:13:31">[01:13:31]</a>. This indicates that extending the context with LongRoPE does not significantly degrade overall model capabilities [01:14:13](<a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>.

### Implications and Advantages

*   **Retaining Original Architecture:** LongRoPE allows models to retain their original architecture with minor modifications to positional embeddings [00:04:57](<a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Significant Context Extension:** It can extend the context window 8 times without any fine-tuning [01:21:52](<a class="yt-timestamp" data-t="01:21:52">[01:21:52]</a>. With progressive fine-tuning, context windows can reach up to 2048K tokens [01:21:55](<a class="yt-timestamp" data-t="01:21:55">[01:21:55]</a>.

## Broader Discussion

### The "Bitter Lesson": Learned vs. Hand-Engineered Features

> [!NOTE] Rich Sutton's "The Bitter Lesson" [01:23:02](<a class="yt-timestamp" data-t="01:23:02">[01:23:02]</a>
> "General methods that leverage computation are ultimately the most effective" [01:23:30](<a class="yt-timestamp" data-t="01:23:30">[01:23:30]</a>.
> Building explicit knowledge into agents often helps in the short term but eventually plateaus, with breakthroughs coming from scaling computation through search and learning [01:23:57](<a class="yt-timestamp" data-t="01:23:57">[01:23:57]</a>.

The evolution of positional embeddings, from basic hand-designed sinusoids to sophisticated techniques like LongRoPE with evolutionary search, mirrors a historical pattern in AI research [01:26:26](<a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>. In computer vision, early methods relied on hand-engineered features like Gabor filters for edge detection [01:24:37](<a class="yt-timestamp" data-t="01:24:37">[01:24:37]</a>. Eventually, these were superseded by convolutional neural networks that learned optimal filters directly from data, often resembling the hand-designed ones but performing better through scale and computation [01:25:27](<a class="yt-timestamp" data-t="01:25:27">[01:25:27]</a>, [01:26:06](<a class="yt-timestamp" data-t="01:26:06">[01:26:06]</a>.

Similarly, despite the complexity and improvements offered by methods like LongRoPE, they remain "hand-engineered" to a degree [01:27:07](<a class="yt-timestamp" data-t="01:27:07">[01:27:07]</a>. The prevailing opinion, following the Bitter Lesson, suggests that future advancements will likely involve learning positional embeddings directly, much like token embeddings are learned [01:27:18](<a class="yt-timestamp" data-t="01:27:18">[01:27:18]</a>. While attempts to learn positional encodings have historically failed to outperform hand-designed ones, it is anticipated that increased scale and computation will eventually enable learned embeddings to become superior [01:30:31](<a class="yt-timestamp" data-t="01:30:31">[01:30:31]</a>, [01:30:46](<a class="yt-timestamp" data-t="01:30:46">[01:30:46]</a>.

> [!WARNING] The speaker speculates that all this "weird stuff" of hand-engineering complex positional embeddings might become irrelevant in the future, replaced by models that simply learn them [01:28:18](<a class="yt-timestamp" data-t="01:28:18">[01:28:18]</a>.

### Speculation: [[long_context_windows_in_large_language_models | Gemini's]] Secret Sauce

The development of LongRoPE highlights the ongoing quest to understand and replicate the breakthroughs in long context models like [[long_context_windows_in_large_language_models | Gemini 1.5]] [01:33:17](<a class="yt-timestamp" data-t="01:33:17">[01:33:17]</a>. While LongRoPE offers a powerful technique, it's unknown if Google's "secret sauce" for Gemini's exceptional context length is a more convoluted hand-engineered solution or if they have already achieved truly learned positional embeddings [01:33:28](<a class="yt-timestamp" data-t="01:33:28">[01:33:28]</a>, [01:48:13](<a class="yt-timestamp" data-t="01:48:13">[01:48:13]</a>.

### Impact on Retrieval-Augmented Generation (RAG)

The significant increase in context window size poses a question about the future of Retrieval-Augmented Generation (RAG) [01:16:01](<a class="yt-timestamp" data-t="01:16:01">[01:16:01]</a>. RAG was developed to overcome the limitations of smaller context windows by allowing LLMs to access external memory (databases of text) [01:16:22](<a class="yt-timestamp" data-t="01:16:22">[01:16:22]</a>.
With LLMs capable of processing millions of tokens directly in their context, the need to selectively retrieve and concatenate text chunks might diminish [01:17:09](<a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>. While embedding vectors and databases will likely still be used for other purposes, the role of RAG as a performance improvement technique by explicitly managing context might become less critical [01:18:46](<a class="yt-timestamp" data-t="01:18:46">[01:18:46]</a>, [01:19:51](<a class="yt-timestamp" data-t="01:19:51">[01:19:51]</a>.