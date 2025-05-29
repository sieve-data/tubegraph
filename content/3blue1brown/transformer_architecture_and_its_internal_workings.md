---
title: Transformer architecture and its internal workings
videoId: eMlx5fFNoYc
---

From: [[3blue1brown]] <br/> 

The transformer is a pivotal piece of technology found in [[generative_pretrained_transformer_architecture | large language models]] and many modern AI tools <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It first emerged in a seminal 2017 paper titled "Attention is All You Need" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This article explores the [[attention_mechanism_in_transformers | attention mechanism]] and its role in how transformers process data <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

The primary goal of a transformer model is to take an input text and predict the next word in the sequence <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Tokens and Embeddings

Input text is segmented into "tokens," which are often words or parts of words <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The first step in a transformer is to associate each token with a high-dimensional vector, known as its embedding <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The key idea is that specific directions in this high-dimensional embedding space correspond to semantic meaning <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. For example, adding a particular step in this space could transform a masculine noun's embedding into its corresponding feminine noun's embedding, illustrating how directions encode aspects of a word's meaning <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The aim of a transformer is to progressively adjust these embeddings so they encode richer contextual meaning, rather than just individual word meanings <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## The Need for Contextual Understanding

Initially, a token's embedding is a context-free lookup, meaning a word like "mole" would have the same initial vector regardless of whether it refers to an animal, a unit of chemical substance, or a skin growth <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The transformer's subsequent steps, particularly the attention mechanism, allow surrounding embeddings to pass information into and refine a word's meaning <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

The [[attention_mechanism_in_transformers | attention block]] calculates what needs to be added to a generic embedding to shift it towards a context-specific meaning <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For instance, "tower" might be updated to encode "Eiffel Tower" if preceded by "Eiffel," or its meaning further refined if preceded by "miniature" <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

More broadly, the attention block enables the model to transfer information between embeddings, even those far apart in the text, to enrich their meaning <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Ultimately, for tasks like predicting the next word in a novel, the final embedding must encapsulate all relevant contextual information from the entire passage <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Single Head of Attention: Computational Details

A "single head of attention" processes information to allow words to adjust the meanings of corresponding words, such as adjectives refining nouns <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

1.  **Initial Embeddings**: Each word's initial embedding (denoted `e`) is a high-dimensional vector that encodes both the word's meaning and its positional information <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

2.  **Queries (Q)**:
    *   Each embedding is multiplied by a "query matrix" (`Wq`) to produce a "query vector" (`q`) <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   Query vectors are smaller in dimension than embeddings (e.g., 128 dimensions for GPT-3) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
    *   Conceptually, a query vector for a noun like "creature" might encode the "question": "Are there any adjectives sitting in front of me?" <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   The entries of `Wq` are tuneable parameters learned from data <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

3.  **Keys (K)**:
    *   Each embedding is also multiplied by a "key matrix" (`Wk`) to produce a "key vector" (`k`) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   Key vectors live in the same smaller-dimensional space as query vectors <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
    *   Conceptually, key vectors "answer" queries. An adjective like "fluffy" would produce a key vector aligned with the query from "creature" <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

4.  **Dot Product Scores**:
    *   To measure how well each key matches each query, a dot product is computed between every possible key-query pair <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
    *   Larger dot products indicate closer alignment. For "fluffy" and "creature," these scores would be large positive numbers <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   If a key aligns closely with a query, machine learning practitioners say the embedding of the key-word "attends to" the embedding of the query-word <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

5.  **Softmax Normalization**:
    *   The raw dot product scores are normalized using the softmax function along each column <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This transforms scores into values between 0 and 1, with each column summing to 1, resembling a probability distribution <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
    *   The resulting grid of normalized values is called an "attention pattern" <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   Mathematically, this is expressed as `Softmax(Q * K^T / sqrt(d_k))` <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. The division by the square root of the key dimension (`d_k`) is for numerical stability <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

6.  **Masking**:
    *   During training, to prevent later words from "giving away" the answer for earlier words, later tokens are prevented from influencing earlier ones <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
    *   This is achieved by setting dot product scores for later-influencing-earlier pairs to negative infinity *before* applying softmax <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. After softmax, these become zero, maintaining column normalization <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. This process is called masking <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
    *   The size of the attention pattern is the square of the context size, which can be a significant bottleneck for [[understanding_complex_functions_and_their_transformations | large language models]] <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

7.  **Values (V)**:
    *   A "value matrix" (`Wv`) is multiplied by each initial embedding to produce a "value vector" <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
    *   Value vectors live in the same high-dimensional space as the embeddings <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   Conceptually, a value vector represents "what should be added" to another embedding if this word is relevant for adjustment <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

8.  **Updating Embeddings**:
    *   For each column in the attention pattern (representing a target word), each value vector is multiplied by its corresponding normalized attention weight from that column <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
    *   These rescaled value vectors are then summed together to produce a "change" vector (delta-e) <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
    *   This change vector is added to the original embedding of the target word, resulting in a new, contextually refined embedding <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Parameter Count for a Single Head (GPT-3 Example)

A single attention head is parameterized by three distinct matrices: `Wq`, `Wk`, and `Wv` <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

*   **Query and Key Matrices**: For GPT-3, `Wq` and `Wk` each have 12,288 columns (embedding dimension) and 128 rows (key/query space dimension) <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. This equates to approximately 1.5 million parameters each <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Value Matrix**: To be more efficient, the value map is often factored into two smaller matrices: `Wv_down` (mapping to the smaller dimension) and `Wv_up` (mapping back to the embedding dimension) <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. Each of these typically has the same size as `Wq` and `Wk` <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.
*   **Total for one head**: All four matrices (Q, K, V-down, V-up) lead to about 6.3 million parameters for one attention head <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

> [!NOTE|Self-Attention vs. Cross-Attention]
> The process described is "self-attention," where keys, queries, and values come from the same dataset <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. "Cross-attention" involves models processing two distinct types of data (e.g., text in different languages), where keys might come from one language and queries from another, and masking is typically not applied <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Multi-Headed Attention

A full attention block within a transformer uses "multi-headed attention," running many single attention heads in parallel <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>. This allows the model to learn various types of contextual updating <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

*   GPT-3, for example, uses 96 attention heads within each block <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   Each head has its own distinct key, query, and value matrices, leading to 96 distinct attention patterns and 96 sequences of value vectors <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   For each token, every head proposes a change to its embedding <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. These proposed changes are summed together and added to the original embedding, producing a single refined embedding from the multi-headed attention block <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

> [!NOTE|Technical Nuance: Output Matrix]
> In practical implementations, the `Wv_up` matrices for each head are often "stapled together" into one large "output matrix" associated with the entire multi-headed attention block <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. When papers refer to the "value matrix" for a given attention head, they often mean only the initial `Wv_down` projection <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.

### Total Parameters for Attention Heads (GPT-3)

With 96 heads per block, each block of multi-headed attention has approximately 600 million parameters <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. Since GPT-3 includes 96 distinct layers (each with an attention block), the total number of parameters devoted to all attention heads is just under 58 billion <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. This represents about a third of the network's total 175 billion parameters <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.

## Transformer Architecture beyond Attention

Data flowing through a transformer doesn't just go through a single attention block; it also passes through "multi-layer perceptrons" (MLPs) <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>. This sequence of attention blocks and MLPs is repeated many times in different layers <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>. With each layer, embeddings become more nuanced, imbibing more contextual meaning <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. This layered approach enables the model to encode higher-level and more abstract ideas, such as sentiment, tone, or underlying scientific truths <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.

## Advantages of Attention

A significant reason for the [[role_of_transformers_in_language_models | attention mechanism's success]] is its high parallelizability <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. This allows for a huge number of computations to be run efficiently on GPUs <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>. The ability to scale models significantly through parallelizable architectures has led to substantial qualitative improvements in performance <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

For more in-depth learning, resources from Andrej Karpathy and Chris Ola are highly recommended <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.