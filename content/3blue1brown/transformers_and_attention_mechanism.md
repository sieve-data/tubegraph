---
title: Transformers and attention mechanism
videoId: eMlx5fFNoYc
---

From: [[3blue1brown]] <br/> 

The [[Transformers and attention in language models | Transformer]] is a key piece of technology found in large language models and other modern AI tools <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It first appeared in the 2017 paper "Attention is All You Need" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Model Goal and Initial Embeddings

The model's primary goal is to take a piece of text and predict the next word <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Input text is broken into "tokens," often words or parts of words <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

The first step in a [[Transformers and attention in language models | Transformer]] is to associate each token with a high-dimensional vector, known as its "embedding" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Directions in this high-dimensional space correspond to semantic meaning <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For example, adding a certain step can transform a masculine noun's embedding to its feminine counterpart <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

Initially, these token embeddings are like a lookup table, encoding only the individual word's meaning without any context <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. For instance, the word "mole" would have the same embedding regardless of whether it refers to an "American shrew mole," "one mole of carbon dioxide," or "a biopsy of the mole" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Purpose of the [[Attention Mechanism in Transformers | Attention Mechanism]]

The aim of a [[Transformers and attention in language models | Transformer]] is to progressively adjust these embeddings so they encode richer contextual meaning, rather than just individual word meaning <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The [[Attention Mechanism in Transformers | attention mechanism]] is crucial for this adjustment <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It allows the model to move information from one embedding to another, even if they are far apart in the text <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

For example, the generic embedding of "tower" can be updated if preceded by "Eiffel" to specifically encode the Eiffel Tower, correlating with "Paris" or "France" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. If also preceded by "miniature," it should update further to not correlate with large objects <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

Ultimately, after flowing through many attention blocks, the final vector for a sequence (e.g., "was" in "therefore the murderer was") must encode all relevant contextual information from the passage to accurately predict the next word <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## A Single Head of [[Attention Mechanism in Transformers | Attention]]

A "single head of attention" performs a series of computations to refine embeddings <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. These computations involve matrix-vector products with tunable weights that the model learns from data <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Initial embeddings also encode the position of the word <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Queries, Keys, and Values

The process involves three distinct types of vectors:

1.  **Queries (Q)**: Each word's embedding is multiplied by a "query matrix" ($W_Q$) to produce a query vector <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Conceptually, a query "asks a question," e.g., a noun like "creature" asking "are there any adjectives in front of me?" <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Query vectors are typically smaller in dimension than embedding vectors, e.g., 128 dimensions <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
2.  **Keys (K)**: Simultaneously, each embedding is multiplied by a "key matrix" ($W_K$) to produce a key vector <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Keys conceptually "answer queries" <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. For example, adjectives like "fluffy" and "blue" would map to keys closely aligned with the query produced by "creature" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
3.  **Values (V)**: A "value matrix" ($W_V$) is multiplied by each embedding to produce a value vector <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. Value vectors live in the same high-dimensional space as the embeddings <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. They represent "what should be added" to another embedding if the current word is relevant <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

### Attention Pattern Calculation

1.  **Dot Products**: To measure how well each key matches each query, a dot product is computed between every possible key-query pair <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. A larger dot product indicates closer alignment <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. If a key aligns closely with a query, machine learning practitioners say that the key's embedding "attends" to the query's embedding <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
2.  **Masking**: During training, later words are prevented from influencing earlier words (to avoid "giving away the answer") through a process called masking <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This is achieved by setting dot product entries that represent later tokens influencing earlier ones to negative infinity before applying softmax <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. After softmax, these masked entries become zero, maintaining column normalization <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
3.  **Softmax Normalization**: The dot product scores (potentially masked) are then normalized using a softmax function along each column <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This transforms the scores into values between 0 and 1, with each column summing to 1, resembling a probability distribution <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. The resulting grid of normalized values is called an "attention pattern" <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   The formula for the attention pattern is: $Softmax(\frac{Q K^T}{\sqrt{d_k}})$ <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Here, $Q$ and $K$ are matrices of query and key vectors, respectively, and $d_k$ is the dimension of the key/query space <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### [[The process of updating embeddings using attention | Updating Embeddings]]

The attention pattern determines how much each value vector contributes to the update of a specific embedding <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

1.  Each value vector is multiplied by its corresponding weight from the attention pattern's column <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
2.  All these rescaled value vectors within a column are summed together to produce a "change" vector (delta-e) <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
3.  This delta-e is added to the original embedding of the word corresponding to that column <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. This process is applied across all columns, yielding a sequence of refined embeddings <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. The hope is that this new vector encodes a more contextually rich meaning <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

### Value Matrix Implementation

In practice, the value matrix ($W_V$) is often factored into two smaller matrices: a "value down" matrix that maps embeddings to a smaller space (e.g., 128 dimensions) and a "value up" matrix that maps back to the larger embedding space (e.g., 12,288 dimensions) <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. This constrains the overall value map to be a "low rank transformation," making it more efficient and reducing the number of parameters compared to a single large square matrix <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.

### Self-Attention vs. Cross-Attention

The process described is specifically "self-attention," where keys, queries, and values all come from the same dataset <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. In contrast, "cross-attention" involves models processing two distinct types of data, where keys might come from one language and queries from another in a translation task <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. Cross-attention typically does not apply masking <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

## [[Multiheaded attention in transformers | Multi-Headed Attention]]

A full [[Attention Mechanism in Transformers | attention block]] within a [[Transformers and attention in language models | Transformer]] consists of "[[Multiheaded attention in transformers | multi-headed attention]]" <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. This means many single attention heads are run in parallel, each with its own distinct key, query, and value matrices <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>. For example, [[Generative Pretrained Transformers | GPT]]-3 uses 96 attention heads per block <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

Each head produces a proposed change to be added to the embedding at each position <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. All these proposed changes from different heads are summed together and added to the original embedding <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

The purpose of [[Multiheaded attention in transformers | multi-headed attention]] is to give the model the capacity to learn many distinct ways that context changes meaning <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. Different heads might capture different types of contextual updates, e.g., grammatical relationships (adjectives modifying nouns) or more abstract associations (like "Harry" and "wizard" suggesting Harry Potter) <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

### Parameter Count for [[Attention Mechanism in Transformers | Attention]]

*   **Single Attention Head**: The key, query, and value matrices each contribute parameters. For [[Generative Pretrained Transformers | GPT]]-3, key and query matrices (12,288 columns by 128 rows) each add about 1.5 million parameters <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. The value map, factored into two matrices, has a similar number of parameters <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. In total, one attention head has approximately 6.3 million parameters <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
*   **Multi-Headed Attention Block**: With 96 heads, an attention block in [[Generative Pretrained Transformers | GPT]]-3 has around 600 million parameters <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Total for [[Generative Pretrained Transformers | GPT]]-3**: [[Generative Pretrained Transformers | GPT]]-3 includes 96 distinct layers <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. This means the total number of parameters devoted to all attention heads is just under 58 billion <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>.
    *   While significant, this is only about a third of [[Generative Pretrained Transformers | GPT]]-3's total 175 billion parameters, with the majority residing in other blocks like [[Neural Networks and Transformers | multi-layer perceptrons]] <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.

### Scalability and Further Processing

The size of the attention pattern is equal to the square of the context size, making context size a significant bottleneck for large language models <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. However, the [[Attention Mechanism in Transformers | attention mechanism]] is highly parallelizable, allowing for a huge number of computations to run efficiently on GPUs <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>. This parallelizability has been a key factor in the success and scaling of deep learning models <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

After data flows through an attention block, it also goes through other operations, such as [[Neural Networks and Transformers | multi-layer perceptrons]] <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>. These operations are repeated across many layers, allowing embeddings to continually refine their meaning, encoding higher-level and more abstract ideas like sentiment, tone, or scientific truths <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.