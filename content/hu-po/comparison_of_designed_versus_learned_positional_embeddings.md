---
title: Comparison of designed versus learned positional embeddings
videoId: PFxi6SmozZ4
---

From: [[hu-po]] <br/> 

[[Role of positional embeddings in Transformers | Positional embeddings]] are crucial components in Transformer models, providing explicit information about the order of input tokens <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. Without them, Transformer models, which compute attention by multiplying every element with every other element, would lack awareness of sequence order <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>, <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This article explores two main philosophies for generating these embeddings: hand-designed (or engineered) methods and learned methods.

## Hand-Designed Positional Embeddings

Historically, and currently, many effective positional embeddings are carefully designed by researchers.

### Basic Positional Embeddings

In a basic sense, [[Role of positional embeddings in Transformers | positional embeddings]] involve adding a small vector to each token's embedding that signifies its position in a sequence <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. For example, in a Vision Transformer (ViT), visual patches are given numerical positions (0, 1, 2, 3, etc.) which are then encoded as position embeddings <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>. These embeddings are then combined with the token embeddings (e.g., by addition) before being fed into the Transformer <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.

Visually, these hand-designed positional embeddings can appear as "weird hardcoded kind of repeating patterns" <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>, often derived from sinusoidal functions <a class="yt-timestamp" data-t="32:28:00">[32:28:00]</a>.

### Rotary Position Embeddings (RoPE)

A significant advancement in designed positional embeddings is Rotary Position Embeddings (RoPE), introduced in the 2021 RoFormer paper <a class="yt-timestamp" data-t="12:46:00">[12:46:46]</a>. RoPE aims to encode absolute position while incorporating relative position dependency into the self-attention mechanism <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>.

Key properties of RoPE include:
*   **Flexibility with sequence length**: It can be extended to longer sequences <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.
*   **Decaying inter-token dependency**: The relevance between tokens decreases as their relative distance increases <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>, meaning tokens closer together have more "similarity" in their positional vectors <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.

The intuition behind RoPE involves rotating token vectors by an angle dependent on their position <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a>. This rotation affects the dot product used in attention, ensuring that closer tokens have a higher similarity score <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>. Mathematically, this relies on Euler's identity, effectively expressing the rotation as a combination of cosine and sine terms <a class="yt-timestamp" data-t="27:04:00">[27:04:00]</a>. The frequency of these sinusoidal patterns varies across the embedding dimensions, with lower dimensions having lower frequencies and higher dimensions having higher frequencies <a class="yt-timestamp" data-t="44:06:00">[44:06:00]</a>.

### Extensions of RoPE: Position Interpolation, NTK, and Yarn

Subsequent research built upon RoPE to extend context lengths further:

*   **Position Interpolation (PI)**: A Meta paper from 2023 extended RoPE by linearly interpolating positions <a class="yt-timestamp" data-t="21:58:00">[21:58:00]</a>. However, this approach can make position information "crowded" <a class="yt-timestamp" data-t="50:50:00">[50:50:50]</a>, as rotations become too small, leading to underperformance at high extension ratios <a class="yt-timestamp" data-t="52:54:00">[52:54:00]</a>.
*   **NTK-based Interpolation**: This method rescales based on position within the sequence <a class="yt-timestamp" data-t="53:30:00">[53:30:00]</a>.
*   **Yarn**: This approach further divided RoPE dimensions into three frequency-based groups, each with a different interpolation strategy <a class="yt-timestamp" data-t="54:10:00">[54:10:00]</a>. These groupings and strategies were determined by "human-led empirical experiments" <a class="yt-timestamp" data-t="55:11:00">[55:11:00]</a>, indicating a heuristic, non-linear approach.

### Long Rope: The "Remix of a Remix of a Remix"

Long Rope, a 2024 paper by Microsoft Research, is described as a "remix of position interpolated rope, which is a remix of rope, which is a remix of [[Role of positional embeddings in Transformers | positional embeddings]]" <a class="yt-timestamp" data-t="36:40:00">[36:40:00]</a>. It significantly extends the context window of pre-trained Large Language Models (LLMs) to an "unprecedented 2048K tokens" <a class="yt-timestamp" data-t="37:28:00">[37:28:00]</a>, potentially mimicking the secret sauce behind Google's Gemini 1.5 <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

Long Rope's key innovations include:
1.  **Exploiting Non-uniformities**: It identifies and leverages two forms of non-uniformities in positional interpolation:
    *   **Initial Token Handling**: The first `n_hat` positions in the sequence are *not* interpolated <a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>, retaining their original positional embeddings. This is because initial tokens often receive large attention scores <a class="yt-timestamp" data-t="01:01:38">[01:01:38]</a>.
    *   **Dimension-Dependent Rescaling**: It identifies effective rescale factors (Lambda I) for RoPE's rotation angles for each dimension, based on token positions <a class="yt-timestamp" data-t="42:55:00">[42:55:00]</a>. These factors account for the varying frequencies across the embedding dimensions <a class="yt-timestamp" data-t="44:17:00">[44:17:00]</a>.
2.  **[[Evolutionary search for optimal position interpolation | Evolutionary Search]]**: Rather than human-designed heuristics like Yarn, Long Rope uses an [[Evolutionary search for optimal position interpolation | evolutionary search]] algorithm to discover optimal values for `n_hat` and the Lambda I rescale factors <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>. This process involves:
    *   Starting with a population of rescale factors.
    *   Randomly mutating them.
    *   Computing LLM perplexity for each variant.
    *   Selecting top-performing individuals as "parents" to generate new variants, while discarding poorly performing ones <a class="yt-timestamp" data-t="00:58:50">[00:58:50]</a>.
    *   This iterative process aims to find the best values that humans might not intuitively guess <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.
3.  **Progressive Extension Strategy**: Models are fine-tuned gradually with increasing context lengths (e.g., from 4K to 8K, then to 16K, etc.) <a class="yt-timestamp" data-t="00:38:04">[00:38:04]</a>.

Long Rope has shown significant performance improvements in perplexity (lower is better) and "Pass Key Retrieval Accuracy" (higher is better, akin to a needle-in-a-haystack task) compared to previous methods like PI and Yarn <a class="yt-timestamp" data-t="01:03:37">[01:03:37]</a>. While extending context length, Long Rope models retain most of their original benchmark performance (e.g., on MMLU, HellaSwag, TruthfulQA) <a class="yt-timestamp" data-t="01:13:31">[01:13:31]</a>.

## Learned Positional Embeddings and the "Bitter Lesson"

Despite the successes of sophisticated hand-designed approaches, some argue that the future lies in learned positional embeddings, as espoused by Rich Sutton's "Bitter Lesson" <a class="yt-timestamp" data-t="01:23:02">[01:23:02]</a>.

### The Bitter Lesson

The "Bitter Lesson" posits that "general methods that leverage computation are ultimately the most effective" <a class="yt-timestamp" data-t="01:23:30">[01:23:30]</a>. It suggests that while building human-designed knowledge into AI agents might provide short-term gains, it eventually plateaus and inhibits further progress <a class="yt-timestamp" data-t="01:23:58">[01:23:58]</a>. Breakthroughs, instead, come from "scaling computation by search and learning" <a class="yt-timestamp" data-t="01:24:07">[01:24:07]</a>.

### Analogy to Computer Vision

This principle can be seen in the evolution of computer vision:
*   **Hand-Designed**: Early computer vision relied on hand-designed filters like Gabor filters, which were manually crafted to detect specific features (e.g., vertical or horizontal edges) <a class="yt-timestamp" data-t="01:24:37">[01:24:37]</a>.
*   **Learned**: With the advent of Convolutional Neural Networks (CNNs), these filters became learned parameters <a class="yt-timestamp" data-t="01:25:27">[01:25:27]</a>. Researchers discovered that simply pushing gradients into the network allowed it to learn optimal filters, often resembling the human-designed ones but performing better <a class="yt-timestamp" data-t="01:25:40">[01:25:40]</a>.

### Current State and Future Outlook

Currently, [[Role of positional embeddings in Transformers | positional embeddings]] remain a complex, hand-engineered system of sinusoids and arbitrary non-linear boundaries <a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>. While researchers have attempted to learn positional embeddings (e.g., in papers cited in the original RoFormer paper), these attempts have not yet outperformed hand-designed methods <a class="yt-timestamp" data-t="01:30:29">[01:30:29]</a>.

However, the "Bitter Lesson" suggests this is likely a matter of scale <a class="yt-timestamp" data-t="01:30:46">[01:30:46]</a>. Just as learned filters eventually surpassed Gabor filters, it's predicted that with sufficient computational power, data, and model size, models will learn optimal positional embeddings that outperform all heuristically hand-designed ones <a class="yt-timestamp" data-t="01:30:52">[01:30:52]</a>. This would eliminate the need for the increasingly convoluted and complicated design processes seen in the progression from RoPE to Long Rope <a class="yt-timestamp" data-t="01:47:11">[01:47:11]</a>.

The eventual learned positional embeddings might still exhibit sinusoidal patterns, validating the human intuition, but they would be found through optimization rather than explicit design <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>.