---
title: Multiheaded attention in transformers
videoId: eMlx5fFNoYc
---

From: [[3blue1brown]] <br/> 

The [[transformer_architecture_and_its_internal_workings | transformer]] architecture is a fundamental technology in modern AI, particularly within [[role_of_transformers_in_language_models | large language models]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The [[attention_mechanism_in_transformers | attention mechanism]], first introduced in the 2017 paper "Attention is All You Need," is a key component of transformers <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Its primary goal is to adjust word embeddings so they encode rich contextual meaning rather than just individual word meanings <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## The Role of Attention
The aim of a transformer is to progressively refine word embeddings so they incorporate contextual meaning <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. For example, the word "mole" has different meanings in phrases like "American shrew mole," "one mole of carbon dioxide," and "take a biopsy of the mole" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Initially, the embedding for "mole" is generic and context-free <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The [[use_of_attention_mechanisms_in_transformers | attention mechanism]] allows surrounding embeddings to pass information into the "mole" embedding, refining its meaning based on context <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Similarly, "tower" might be updated to "Eiffel Tower" if preceded by "Eiffel," or its "tall" association might be removed if preceded by "miniature" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

More broadly, the attention block enables information encoded in one embedding to be moved to another, potentially distant, embedding, incorporating rich contextual information <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. The final vector in a sequence must encode all relevant context to predict the next word accurately <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Single Head of Attention
A single head of attention processes embeddings to refine their contextual meaning. The process involves several steps:

1.  **Initial Embeddings**: Each input token (often a word or piece of a word) is associated with a high-dimensional vector, known as its embedding <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. These embeddings encode semantic meaning, with directions in the high-dimensional space corresponding to aspects of meaning, such as gender <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Additionally, embeddings include positional information <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
2.  **Queries, Keys, and Values**: Three distinct matrices are used to transform the initial embeddings:
    *   **Query Matrix (Wq)**: Multiplied by each embedding to produce a "query" vector <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. This matrix has tuneable parameters, learning to map nouns, for example, to directions that look for adjectives in preceding positions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   **Key Matrix (Wk)**: Multiplied by each embedding to produce a "key" vector <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Keys conceptually answer queries; for instance, the key matrix maps adjectives to vectors aligned with a noun's query <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   **Value Matrix (Wv)**: Used to produce "value" vectors, which represent the information to be added to another embedding <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

    These matrices perform [[matrix_representation_of_transformations | matrix transformations]] that adjust during training <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. The query and key vectors typically have a smaller dimension (e.g., 128) than the embedding vectors (e.g., 12,288) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The value vectors live in the same high-dimensional space as the embeddings <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

3.  **Calculating Attention Scores**: A dot product is computed between each possible key-query pair to measure how well they match <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This generates a grid of scores, where larger values indicate stronger alignment <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
4.  **Softmax Normalization**: The scores are normalized using a softmax function applied column by column <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This converts the scores into values between 0 and 1, where each column sums to 1, representing a probability distribution <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This normalized grid is called an **attention pattern** <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. The dimensions of this pattern are the square of the context size, which can be a bottleneck for large language models <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
5.  **Masking**: During training, to prevent later tokens from influencing earlier ones (which would "give away the answer"), entries in the attention pattern representing later tokens influencing earlier ones are set to negative infinity before softmax, resulting in zero after normalization <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This process is called masking <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
6.  **Updating Embeddings**: For each column in the attention pattern, value vectors are multiplied by their corresponding normalized weights from that column <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. These rescaled values are then summed to produce a change vector (delta-e), which is added to the original embedding <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This results in a more contextually refined embedding <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

### Parameter Count for a Single Head
For [[generative_pretrained_transformer_architecture | GPT-3]], a single attention head includes approximately 6.3 million parameters <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>:
*   **Query and Key Matrices**: Each has 12,288 columns (embedding dimension) and 128 rows (key/query space dimension), totaling about 1.5 million parameters each <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Value Matrix**: To optimize efficiency and reduce parameters, the value map is factored into two smaller matrices:
    *   A "value down" matrix: Maps large embedding vectors down to a smaller space (e.g., 128 dimensions).
    *   A "value up" matrix: Maps from this smaller space back up to the embedding space <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.
    This effectively constrains the overall value map to be a low-rank transformation, matching the parameter count of the key and query matrices <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.

### Self-Attention vs. Cross-Attention
The process described is known as **self-attention** <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. In **cross-attention**, which appears in other models (e.g., for translation), the key and query maps act on different datasets <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Multi-headed Attention
A full attention block within a transformer consists of **multi-headed attention**, where many single attention heads run in parallel <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
*   **Purpose**: This allows the model to learn many distinct ways that context can influence the meaning of a word <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. Different heads might capture different types of contextual updates (e.g., grammatical relations, semantic associations like "Harry" with "Potter" or "Prince") <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Mechanism**: Each head has its own distinct key, query, and value matrices, producing its own attention pattern and sequence of value vectors <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. For each token, every head proposes a change to be added to its embedding. All these proposed changes are summed together and added to the original embedding of that position <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

### Multi-headed Attention Parameter Count
[[generative_pretrained_transformer_architecture | GPT-3]] utilizes 96 attention heads within each block <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. With each head having approximately 6.3 million parameters, a multi-headed attention block contains around 600 million parameters <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. A technical detail in practice is that the "value up" matrices from each head are often combined into one large "output matrix" for the entire multi-headed attention block <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>.

## Overall Context within Transformers
Transformers typically consist of many copies of these attention blocks and other operations called multi-layer perceptrons <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>. As data flows through these successive layers, embeddings become increasingly nuanced, incorporating more abstract and higher-level information about the input, such as sentiment, tone, or underlying scientific truths <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.

For [[generative_pretrained_transformer_architecture | GPT-3]], with 96 distinct layers, the total number of parameters devoted to all attention heads is just under 58 billion <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. While significant, this accounts for about one-third of the network's total 175 billion parameters, with the majority residing in the blocks between attention steps <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.

A major reason for the success of the [[attention_mechanism_in_transformers | attention mechanism]] is its extreme parallelizability, allowing for a large number of computations to run quickly using GPUs <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. This parallelizability is crucial for scaling up models, which has led to significant qualitative improvements in performance <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.