---
title: Highdimensional vector embeddings
videoId: eMlx5fFNoYc
---

From: [[3blue1brown]] <br/> 

High-dimensional vector embeddings are a fundamental component of modern large language models (LLMs) and other AI tools, particularly within the internal workings of a transformer <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. They were a key piece of the "Attention is All You Need" paper published in 2017 <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Purpose and Representation
In the context of language models, the goal is to predict the next word in a sequence of text <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The input text is first broken down into "tokens," which are often words or pieces of words <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The initial step in a transformer is to associate each of these tokens with a high-dimensional vector, known as its embedding <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The core idea is that different directions within this high-dimensional space of all possible embeddings correspond to semantic meaning <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. For instance, adding a specific step in this space could transform the embedding of a masculine noun into that of its corresponding feminine noun <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This allows for the encoding of various aspects of a word's meaning <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Contextual Refinement
Initially, a token's embedding is context-free, acting like a lookup table <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. For example, the word "mole" would have the same initial embedding regardless of whether it refers to an animal, a unit of measurement, or a skin growth <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. The aim of a transformer is to progressively adjust these embeddings to bake in much richer contextual meaning <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

This adjustment allows the model to:
*   **Discern different meanings**: A well-trained attention block can calculate what needs to be added to a generic embedding to move it towards one of its specific contextual meanings <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For instance, the embedding of "mole" would be updated differently based on the surrounding words like "American shrew" or "carbon dioxide" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Incorporate modifiers**: If the word "tower" is preceded by "Eiffel," its generic embedding might be updated to specifically encode the Eiffel Tower, correlating with vectors associated with Paris or steel <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Further context, like "miniature," would refine the embedding even more, causing it to no longer correlate with large things <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Transfer information**: The attention block facilitates the movement of information encoded in one embedding to another, even if they are far apart in the text <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

Ultimately, the final vector in a sequence, which might have started simply embedding a single word, must be updated by multiple attention blocks to encode all relevant information from the full context window necessary for predicting the next word <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Embeddings in the Attention Mechanism
Within a single head of attention, embeddings are transformed for interaction:
*   **Queries (Q)**: Each embedding is multiplied by a "query matrix" (Wq) to produce a query vector <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Conceptually, a query vector asks: "Are there any relevant words near me?" <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These vectors typically have a smaller dimension than the full embedding <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Keys (K)**: Each embedding is also multiplied by a "key matrix" (Wk) to produce a key vector <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Key vectors are conceptualized as answers to queries, matching closely aligned queries <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. They reside in the same smaller-dimensional space as query vectors <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Values (V)**: A "value matrix" (Wv) is multiplied by each embedding to produce a value vector <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. These value vectors live in the same high-dimensional space as the original embeddings <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. They represent the specific "information" or "change" that should be added to another embedding if relevance is determined <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

The process involves computing dot products between query and key pairs to measure relevance, which then informs how value vectors are weighted and summed to update the original embeddings <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. The result is a sequence of more refined embeddings that "imbibe" contextual meaning <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Dimensionality and Parameters
For GPT-3, the embedding dimension is 12,288 <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. The smaller key/query space dimension is 128 <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   The query and key matrices (Wq, Wk) each have 12,288 columns and 128 rows, contributing roughly 1.5 million parameters each <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>, <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   The value matrix (Wv) is typically factored into two smaller matrices (e.g., "value down" and "value up" matrices, which is not conventional naming) to ensure parameter efficiency, keeping the number of parameters similar to the key and query matrices <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>, <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. This constraint on the overall value map is a [[Transformations between different dimensions | low rank transformation]] <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   A single attention head, including these four matrices, totals about 6.3 million parameters <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>, <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.

### Multi-Headed Attention
A full attention block within a transformer consists of "multi-headed attention," running many such operations in parallel, each with its own distinct key, query, and value maps <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>, <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. For example, GPT-3 utilizes 96 attention heads per block <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>, leading to approximately 600 million parameters per block <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>, <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.

Each head produces a proposed change for an embedding, and these changes are summed together and added to the original embedding, resulting in a more refined, contextually rich output <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>, <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>, <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. This parallel processing allows the model to learn various ways context influences meaning <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>, <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

## Overall Significance
As data flows through multiple layers of attention blocks and other operations (like multi-layer perceptrons), embeddings become increasingly nuanced. This allows the model to encode higher-level and more abstract ideas, such as sentiment, tone, or underlying scientific truths relevant to the text <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.

The total number of parameters dedicated to attention heads in GPT-3 across 96 layers is nearly 58 billion <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>, <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>, <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>. While substantial, this accounts for about a third of the network's total 175 billion parameters <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>, <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>. A key reason for the success of the attention mechanism is its high parallelizability, enabling a huge number of computations on GPUs, which aligns with the trend that scale alone leads to significant qualitative improvements in model performance <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>, <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.