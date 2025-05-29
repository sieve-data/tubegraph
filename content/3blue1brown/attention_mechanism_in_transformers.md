---
title: Attention mechanism in transformers
videoId: eMlx5fFNoYc
---

From: [[3blue1brown]] <br/> 

The attention mechanism is a core piece of technology within [[role_of_transformers_in_language_models | large language models]] and other modern AI tools <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It was first introduced in the 2017 paper "Attention is All You Need" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This mechanism is crucial for [[transformer_architecture_and_its_internal_workings | transformers]] to process data by visualizing how it flows <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Role in Language Models
The primary goal of a model using a [[transformer_architecture_and_its_internal_workings | transformer]] is to predict the next word in a given text <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The input text is first divided into "tokens," often words or parts of words <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Each token is initially associated with a high-dimensional vector called its "embedding" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Directions within this high-dimensional embedding space correspond to semantic meaning; for example, a specific direction might transform a masculine noun's embedding into its feminine counterpart <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

The aim of a [[transformer_architecture_and_its_internal_workings | transformer]] is to iteratively adjust these embeddings, allowing them to encode rich contextual meaning rather than just an individual word's meaning <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Initially, token embeddings are lookup tables with no context <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The attention mechanism enables surrounding embeddings to pass information into a given word's embedding <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Examples of Contextual Refinement
Consider the word "mole" in phrases like "American shrew mole," "one mole of carbon dioxide," and "take a biopsy of the mole" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The initial embedding for "mole" would be identical in all these cases, but the attention mechanism allows the model to calculate what needs to be added to the generic embedding to shift it towards one of its specific context-dependent meanings <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

Similarly, the generic embedding for "tower" could be refined if preceded by "Eiffel," correlating it with Paris or steel structures <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. If also preceded by "miniature," the embedding would further update to no longer correlate with large structures <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. More broadly, the attention block facilitates the transfer of information between embeddings, even those far apart in the text, incorporating richer context than just a single word <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Single Head of Attention
A single head of attention is a fundamental component of the attention mechanism <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Initial Embeddings
Each word's initial high-dimensional vector encoding includes both its meaning and its position in the text <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. These are denoted as `e` <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. The goal is to produce refined embeddings where, for instance, nouns have ingested meaning from their adjectives <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Queries, Keys, and Values
The process largely relies on [[matrix_representation_of_transformations | matrix-vector products]] involving tunable weights <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>:
*   **Queries (Q)**: Each embedding is multiplied by a "query matrix" (`wq`) to produce a query vector <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Conceptually, a query encodes what a word (e.g., a noun) is "asking for" (e.g., adjectives preceding it) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. Query vectors are typically smaller in dimension than embedding vectors (e.g., 128 dimensions) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Keys (K)**: Simultaneously, each embedding is multiplied by a "key matrix" (`wk`) to produce a key vector <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Keys are thought of as "answering" queries <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. The key matrix maps embeddings to the same smaller dimensional space as queries <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Values (V)**: A "value matrix" (`wv`) is also multiplied by each embedding to produce a value vector <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. Value vectors exist in the same high-dimensional space as the embeddings and represent the information a word should "provide" if relevant to another <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

### Computing the Attention Pattern
1.  **Dot Products**: To measure how well each key matches each query, a dot product is computed for every possible key-query pair <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Large dot products indicate close alignment <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
2.  **Normalization with Softmax**: These raw scores, which can range from negative infinity to infinity, are then normalized using a softmax function applied column by column <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This transforms the scores into values between 0 and 1, where each column sums to 1, resembling a probability distribution <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
3.  **Scaling**: For numerical stability, these dot products are divided by the square root of the dimension of the key-query space <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
4.  **Masking**: To prevent later words from influencing earlier words (especially during training for next-token prediction), certain entries in the dot product grid (those representing later tokens influencing earlier ones) are set to negative infinity before softmax <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. After softmax, these become zero, maintaining column normalization <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. This process is called masking <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

The resulting normalized grid is called an "attention pattern" <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. The size of this pattern is the square of the context size, which can be a significant bottleneck for [[role_of_transformers_in_language_models | large language models]] <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

The compact notation for this calculation is `softmax(Q * K^T / sqrt(d_k))` <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### Updating Embeddings
Once the attention pattern is computed, the model updates the embeddings <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>:
1.  **Value Vector Generation**: A sequence of value vectors is produced by multiplying the value matrix (`wv`) by every embedding <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
2.  **Weighted Sum**: For each column in the attention pattern, each value vector is multiplied by its corresponding weight in that column <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
3.  **Addition**: All these rescaled values in a column are summed together to produce a change vector (`delta-e`), which is then added to the original embedding for that position <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This process results in a more refined, contextually rich embedding <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

### Parameter Count (Single Head)
In [[generative_pretrained_transformer_architecture | GPT-3]], the key and query matrices each have 12,288 columns (embedding dimension) and 128 rows (key/query space dimension), resulting in approximately 1.5 million parameters each <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. The value matrix, which maps embeddings to the embedding space, is typically factored into two smaller matrices for efficiency: a "value down" matrix and a "value up" matrix <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. All four of these matrices (Q, K, Value Down, Value Up) typically have the same size, leading to approximately 6.3 million parameters for one attention head <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

### Self-Attention vs. Cross-Attention
The mechanism described is specifically "self-attention" <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>, where queries, keys, and values all come from the same dataset (e.g., a single text passage). "Cross-attention" involves models processing two distinct types of data, like text in different languages for translation, where keys might come from one language and queries from another <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Multi-Headed Attention
A full attention block within a [[transformer_architecture_and_its_internal_workings | transformer]] consists of [[multiheaded_attention_in_transformers | multi-headed attention]], where many single attention heads run in parallel <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. Each head has its own distinct key, query, and value maps <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.

### How it Works
*   Each of the multiple heads (e.g., 96 in [[generative_pretrained_transformer_architecture | GPT-3]]) produces a distinct attention pattern and sequence of value vectors <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   For each token position, every head generates a proposed change to be added to that position's embedding <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.
*   These proposed changes from all heads are summed together and then added to the original embedding, resulting in a single refined embedding for that position <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

### Purpose
[[Multiheaded_attention_in_transformers | Multi-headed attention]] allows the model to learn many distinct ways that context can influence meaning <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. For example, one head might identify adjectives for nouns, while another might associate names with their typical contexts (e.g., "Harry" with "wizard" or "Queen") <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

### Parameter Count (Multi-Headed)
With 96 heads, each containing its own Q, K, and factored V matrices, each block of [[multiheaded_attention_in_transformers | multi-headed attention]] has approximately 600 million parameters <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

### Technical Nuance
In practice, the "value up" matrices from all heads are often "stapled together" into one large "output matrix" for the entire [[multiheaded_attention_in_transformers | multi-headed attention]] block <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. When papers refer to the "value matrix" for a single head, they often mean only the "value down" projection <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.

## Overall Role in Transformers
Data flowing through a [[transformer_architecture_and_its_internal_workings | transformer]] passes through multiple attention blocks and other operations like multi-layer perceptrons <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>. Repeated application of these operations allows embeddings to imbibe more and more nuanced meaning from their surroundings <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>. This capacity enables the model to encode higher-level and more abstract ideas, such as sentiment, tone, or underlying scientific truths <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.

In [[generative_pretrained_transformer_architecture | GPT-3]], which has 96 distinct layers, the total number of parameters devoted to all attention heads is just under 58 billion <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. This represents about one-third of the total 175 billion parameters in the network, with the majority coming from other blocks between attention steps <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.

A key factor in the success of the [[use_of_attention_mechanisms_in_transformers | attention mechanism]] is its extreme parallelizability, allowing for a huge number of computations to be run efficiently on GPUs <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. This parallel processing capability is vital for scaling models, which has led to significant qualitative improvements in deep learning performance <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.