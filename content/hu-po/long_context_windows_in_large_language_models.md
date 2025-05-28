---
title: Long context windows in large language models
videoId: PFxi6SmozZ4
---

From: [[hu-po]] <br/> 

Long context windows are a highly desirable feature in [[llm_large_language_models_development | Large Language Models (LLMs)]] due to their ability to process and understand significantly more information at once <a class="yt-timestamp" data-t="03:16:05">[03:16:05]</a>. This capability is crucial for tasks requiring extensive context, such as analyzing long documents, managing lengthy conversations, or processing entire codebases <a class="yt-timestamp" data-t="03:33:02">[03:33:02]</a>.

## The Quest for Extended Context: Gemini 1.5's "Secret Sauce"

Recent advancements, particularly with Google's Gemini 1.5, have demonstrated state-of-the-art context lengths, capable of processing up to 10 million tokens <a class="yt-timestamp" data-t="02:26:09">[02:26:09]</a>. DeepMind's head, Demis Hassabis, admitted that achieving such extreme context lengths required "some new innovations" or "Secret Sauce" <a class="yt-timestamp" data-t="03:01:03">[03:01:03]</a>. While the exact methods used by Google remain undisclosed, researchers are exploring techniques like "Long Rope" as potential solutions <a class="yt-timestamp" data-t="03:34:35">[03:34:35]</a>.

## Understanding Positional Embeddings (PE)

At the core of extending context length in Transformer models is the concept of Positional Embeddings (PE) <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>. Transformer models inherently treat input sequences as a "bag of words" or tokens, lacking an intrinsic understanding of their order <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. Therefore, explicit positional information must be injected <a class="yt-timestamp" data-t="06:33:02">[06:33:02]</a>.

### How Positional Embeddings Work
Positional embeddings are vectors that encode the position of each token in a sequence <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. They are combined with token embeddings (vectors representing the semantic meaning of words) before being fed into the Transformer <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>. The goal is for the Transformer to understand the relative position of tokens, ensuring that closer tokens have a stronger connection or higher attention score <a class="yt-timestamp" data-t="17:07:00">[17:07:00]</a>.

> "The more those vectors are kind of agreeing, the smaller that angle is between them, and that is the geometric definition of a dot product." <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>

### Rotary Position Embeddings (RoPE)
Rotary Position Embeddings (RoPE) represent an evolution in positional encoding <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. Introduced in the 2021 RoFormer paper, RoPE aims to encode absolute position while incorporating relative position dependency into the self-attention mechanism <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

RoPE achieves this by "rotating" the token vectors based on their position <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. The rotation angle for each dimension of the embedding is determined by sinusoidal functions with varying frequencies <a class="yt-timestamp" data-t="32:16:00">[32:16:00]</a>. This design ensures that the dot product between query and key vectors (central to attention) depends only on their relative position <a class="yt-timestamp" data-t="31:07:00">[31:07:00]</a>.

## Extending Context: Previous Approaches and Challenges

Extending the context window of pre-trained [[llm_large_language_models_development | LLMs]] is challenging. Naive extrapolation of positional embeddings often leads to degraded performance <a class="yt-timestamp" data-t="51:38:00">[51:38:00]</a>.

### Position Interpolation (PI)
Meta Platforms introduced Position Interpolation (PI), which involves downscaling the positional indices by a factor `s` (extension ratio) <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>. This method, used in [[llm_large_language_models_development | Llama]] models, effectively compresses the positional information. However, it can make the position information "very crowded," hindering the model's ability to distinguish closely positioned tokens <a class="yt-timestamp" data-t="50:52:00">[50:52:00]</a>.

### NTK-based and Yarn-based Interpolation
Subsequent methods like NTK-based interpolation and Yarn introduced "non-uniformities" by applying different interpolation strategies to different frequency-based groups of RoPE dimensions <a class="yt-timestamp" data-t="53:25:00">[53:25:00]</a>. For example, Yarn divides RoPE dimensions into three frequency-based groups, each with a distinct interpolation strategy <a class="yt-timestamp" data-t="54:10:00">[54:10:00]</a>. These methods rely on human-led empirical experiments to find optimal groupings, which can be suboptimal for new [[llm_large_language_models_development | LLMs]] <a class="yt-timestamp" data-t="55:13:00">[55:13:00]</a>.

## Long Rope: A Search-Based Approach to Context Extension

"Long Rope" is a recent innovation from Microsoft Research (Feb 2024) that extends the context window of pre-trained [[llm_large_language_models_development | LLMs]] to an impressive 2048k tokens <a class="yt-timestamp" data-t="37:29:00">[37:29:00]</a>. It's described as a "remix of a remix on a remix" of positional encoding concepts <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

### Key Innovations of Long Rope
Long Rope introduces three key innovations <a class="yt-timestamp" data-t="37:48:00">[37:48:00]</a>:
1.  **Non-uniform Positional Interpolation through Evolutionary Search:** Instead of hand-designing the "non-uniformities" (arbitrary boundaries for different interpolation strategies), Long Rope uses an evolutionary search algorithm to discover the optimal rescale factors (Lambda I) for each RoPE dimension and token position <a class="yt-timestamp" data-t="58:15:00">[58:15:00]</a>.
2.  **No Interpolation for Initial Tokens:** For the first `n_hat` positions in the input sequence (e.g., 256 tokens), Long Rope explicitly *does not* interpolate their positional embeddings <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. This is based on the observation that initial tokens often receive large attention scores and are crucial for performance <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. The optimal `n_hat` value is also found via evolutionary search <a class="yt-timestamp" data-t="01:02:40">[01:02:40]</a>.
3.  **Progressive Extension Strategy:** To achieve extremely long contexts (e.g., 2048k tokens), Long Rope employs a progressive [[finetuning_large_language_models | fine-tuning]] strategy <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. A model is first [[finetuning_large_language_models | fine-tuned]] on a smaller extended context length, then progressively on longer contexts in subsequent steps <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

### Methodology
The evolutionary search for optimal Lambda I and `n_hat` values involves:
*   Starting with a population of rescale factor configurations <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.
*   Randomly mutating these configurations <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.
*   Computing the [[large_language_models_in_machine_learning_research | LLM]] perplexity for each configuration <a class="yt-timestamp" data-t="01:06:07">[01:06:07]</a>.
*   Selecting the top-performing individuals ("parents") to create variants, while discarding poorly performing ones <a class="yt-timestamp" data-t="01:06:10">[01:06:10]</a>.
*   This iterative process, run on powerful GPUs (e.g., 8 or 16 A100s) <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>, eventually converges on highly optimized values <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

### Performance and Results
Long Rope models (fine-tuned Llama 2 and Mistral) demonstrate significant improvements:
*   **Perplexity:** They maintain low perplexity even at very high context window sizes (up to 2048k tokens), unlike other models whose perplexity "explodes" <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. Lower perplexity indicates better model goodness <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Pass Key Retrieval Accuracy:** Long Rope achieves nearly 100% accuracy in "needle in the haystack" tasks, where the model must retrieve a hidden five-digit number from an extremely long document <a class="yt-timestamp" data-t="01:12:01">[01:12:01]</a>.
*   **Benchmark Performance:** While extending context with Long Rope can lead to a slight loss of performance on traditional short-context benchmarks (like MMLU or H-SWAG) <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, it's not significant, and the model gains the ability to handle tasks that would be impossible for models with limited context <a class="yt-timestamp" data-t="01:14:51">[01:14:51]</a>.
*   **Efficiency:** Long Rope can extend context eight times without [[finetuning_large_language_models | fine-tuning]], and much further with the progressive [[finetuning_large_language_models | fine-tuning]] strategy <a class="yt-timestamp" data-t="01:21:23">[01:21:23]</a>.

## Future Outlook

### Impact on Retrieval Augmented Generation (RAG)
The increasing context windows of [[llm_large_language_models_development | LLMs]] may reduce the necessity of Retrieval Augmented Generation (RAG) for improving performance <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>. RAG traditionally augments [[llm_large_language_models_development | LLMs]] by dynamically retrieving relevant text chunks from external databases and concatenating them into the context window <a class="yt-timestamp" data-t="01:17:02">[01:17:02]</a>. As context lengths grow, [[llm_large_language_models_development | LLMs]] might simply be able to hold all necessary information within their context, reducing the overhead of external database queries and data transfer <a class="yt-timestamp" data-t="01:18:19">[01:18:19]</a>. However, vector databases will likely still be used for other purposes, just not necessarily for performance improvement via context augmentation <a class="yt-timestamp" data-t="01:18:46">[01:18:46]</a>.

### Hand-Designed vs. Learned Positional Embeddings
The development of Long Rope, relying on sophisticated human-engineered designs and evolutionary search, highlights an ongoing debate in [[large_language_models_in_machine_learning_research | machine learning research]] captured by Rich Sutton's "Bitter Lesson" <a class="yt-timestamp" data-t="01:23:05">[01:23:05]</a>. The Bitter Lesson suggests that general methods leveraging computation and learning ultimately outperform specific, human-designed knowledge or heuristics <a class="yt-timestamp" data-t="01:24:10">[01:24:10]</a>.

While hand-designed positional embeddings (like RoPE and its derivatives) currently offer superior performance, the long-term trend in [[large_language_models_in_machine_learning_research | AI research]] suggests a shift towards learned embeddings <a class="yt-timestamp" data-t="01:27:51">[01:27:51]</a>. Similar to how learned convolutional filters replaced hand-engineered Gabor filters in computer vision <a class="yt-timestamp" data-t="01:25:40">[01:25:40]</a>, future advancements might enable [[llm_large_language_models_development | LLMs]] to learn optimal positional embeddings directly from vast amounts of data and computational scale, potentially rendering complex human-designed approaches obsolete <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>.