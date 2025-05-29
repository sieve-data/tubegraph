---
title: Multiheaded attention in transformers
videoId: eMlx5fFNoYc
---

From: [[3blue1brown]] <br/> 
The [[Attention Mechanism in Transformers | attention mechanism]] is a core component of [[Transformers and attention mechanism | transformers]], which are key pieces of technology inside [[Generative Pretrained Transformers | large language models]] and many other modern AI tools <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It was introduced in the 2017 paper "Attention is All You Need" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This mechanism processes data by visualizing how it flows and transforms within the model <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Transformer Basics Recap
The primary goal of a transformer model is to take a piece of text as input and predict the next word <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

1.  **Tokens**: The input text is broken down into "tokens," which are often words or pieces of words <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. For simplicity, examples often treat tokens as single words <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
2.  **Embeddings**: The first step in a transformer is to associate each token with a high-dimensional vector, known as its "embedding" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
3.  **Semantic Meaning**: Directions within this high-dimensional space of embeddings correspond to semantic meaning <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For instance, a specific direction can represent gender, allowing a transformation from a masculine noun's embedding to its feminine counterpart <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
4.  **Contextual Refinement**: The aim of a transformer is to progressively adjust these embeddings <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Initially, an embedding only encodes an individual word <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The transformer bakes in much richer contextual meaning <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## The Need for Attention
The [[Attention Mechanism in Transformers | attention mechanism]] addresses the limitation of initial token embeddings, which are static look-up tables with no reference to context <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

Consider the word "mole" in phrases like "American shrew mole," "one mole of carbon dioxide," and "take a biopsy of the mole" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Humans understand "mole" has different meanings based on context <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. A well-trained attention block calculates what needs to be added to a generic embedding to move it to a context-specific meaning <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

Similarly, the word "tower" might have a generic embedding <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. If preceded by "Eiffel," the mechanism should update its vector to specifically encode "Eiffel Tower," correlating with concepts like Paris, France, or steel <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. If further preceded by "miniature," the vector should adjust to no longer correlate with large, tall things <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

Beyond refining a single word's meaning, the attention block allows the model to move information between embeddings, even distant ones, potentially with richer information than just a single word <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. After all vectors flow through the network, the prediction of the next token depends entirely on the last vector in the sequence <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. For example, in a mystery novel predicting the murderer, the final vector (initially "was") must encode all relevant contextual information from the full passage <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Single Head of Attention
A single head of attention involves a series of computations to produce refined embeddings <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Most computations involve [[Matrix representation of transformations | matrix-vector products]] with tunable weights learned from data <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Initial embeddings not only encode word meaning but also its position <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

Let's use the phrase "a fluffy blue creature roamed the verdant forest" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>, aiming for adjectives to adjust their corresponding nouns <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Queries (Q)
Each word's embedding is multiplied by a "query matrix" ($W_Q$) to produce a "query vector" (q) <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. This query vector has a smaller dimension than the embedding, e.g., 128 <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Conceptually, a noun's query asks, "Are there any adjectives sitting in front of me?" <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

### Keys (K)
Each word's embedding is also multiplied by a "key matrix" ($W_K$) to produce a "key vector" (k) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Key vectors reside in the same smaller dimensional space as queries <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Conceptually, key vectors answer queries; for example, adjectives like "fluffy" and "blue" would produce keys that align closely with the query from "creature" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

### Measuring Relevance: Dot Products
To measure how well each key matches each query, a dot product is computed for every possible key-query pair <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Larger dot products indicate closer alignment <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. In machine learning, if keys for "fluffy" and "blue" align with the query for "creature," it means "fluffy" and "blue" "attend" to "creature" <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

### Normalization: Softmax
The dot products generate a grid of scores ranging from negative to positive infinity <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. To use these as weights in a sum, they are normalized using the softmax function along each column <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This ensures values are between 0 and 1, and each column sums to 1, acting like a probability distribution <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. The resulting grid is called an "attention pattern" <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

The formula for the attention pattern is:
$Attention(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
Here, $Q$ and $K$ represent the full arrays of query and key vectors <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. $d_k$ is the dimension of the key/query space, and dividing by its square root helps with numerical stability <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. The softmax applies column by column <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

### Masking
For models like GPT, during training, it's crucial to prevent later words from influencing earlier words <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This is done by setting the dot product scores for future tokens to negative infinity before applying softmax, which turns them into zero after normalization <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. This process is called "masking" <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Masking is always applied in GPT-like models <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

The size of the attention pattern is the square of the context size, which is a major bottleneck for [[Generative Pretrained Transformers | large language models]] and scaling them up <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Values (V) and Embedding Updates
To update embeddings, a "value matrix" ($W_V$) is multiplied by each initial embedding to produce a "value vector" <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. This value vector lives in the same high-dimensional space as the embeddings <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. Conceptually, a value vector represents "what should be added to another embedding if this word is relevant" <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

For each column in the attention pattern, each value vector is multiplied by its corresponding normalized weight from that column <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. These rescaled values are then summed together to produce a change vector ($\Delta e$) <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. This $\Delta e$ is added to the original embedding for that position <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>, resulting in a more contextually refined embedding (e.g., "fluffy blue creature") <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This process is applied across all columns to refine all embeddings <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

### Parameters in a Single Attention Head
A single self-attention head is parameterized by three distinct matrices: Query ($W_Q$), Key ($W_K$), and Value ($W_V$) <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

For GPT-3, with an embedding dimension of 12,288 and a key/query space dimension of 128:
*   $W_Q$ and $W_K$ each have $12,288 \times 128$ parameters, roughly 1.5 million each <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   The value matrix $W_V$ is typically factored into two smaller matrices for efficiency: a "value down" matrix (e.g., $12,288 \times 128$) and a "value up" matrix (e.g., $128 \times 12,288$) <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. This makes the number of parameters for the value map similar to the key and query maps <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.
*   In total, these four matrices (WQ, WK, Value Down, Value Up) give about 6.3 million parameters for one attention head <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Multiheaded Attention
A full [[Structure of neural networks | attention block]] inside a [[Transformers and attention mechanism | transformer]] consists of "multi-headed attention," running many single attention heads in parallel <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. Each head has its own distinct Query, Key, and Value matrices <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.

For example, GPT-3 uses 96 attention heads per block <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. This means:
*   96 distinct Query and Key matrices, producing 96 distinct attention patterns <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   96 distinct Value matrices, producing 96 sequences of value vectors <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
*   Each head proposes a change to be added to each embedding <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.
*   All these proposed changes (one from each head for each token) are summed together and added to the original embedding for that position <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. This sum forms the refined embedding outputted by the multi-headed attention block <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.

By running many distinct heads in parallel, the model gains the capacity to learn many [[different_problemsolving_styles | distinct ways that context changes meaning]] <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. For example, one head might refine "car" based on "crashed," while another might refine "Harry" based on "Potter" or "Prince" <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

With 96 heads, each block of multi-headed attention in GPT-3 has about 600 million parameters <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

## Overall Context and Scale
Data flowing through a [[Transformers and attention in language models | transformer]] passes through many copies of attention blocks and other operations like multi-layer perceptrons (MLPs) <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>. This allows embeddings to imbibe more nuanced context from their surroundings with each layer <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. The goal is to encode higher-level and more abstract ideas, such as sentiment, tone, or underlying scientific truths <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

GPT-3 includes 96 distinct layers <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>, so the total number of attention parameters (key, query, and value) is multiplied by 96 layers, bringing the total to just under 58 billion parameters devoted to all attention heads <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>. While substantial, this is only about a third of the total 175 billion parameters in the network, with the majority coming from other blocks like MLPs <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.

A key factor in the success of the [[Attention Mechanism in Transformers | attention mechanism]] is its extreme parallelizability, allowing for a huge number of computations to run quickly on GPUs <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. This enables scaling up models, which has led to significant qualitative improvements in performance <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.