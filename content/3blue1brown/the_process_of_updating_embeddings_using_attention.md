---
title: The process of updating embeddings using attention
videoId: eMlx5fFNoYc
---

From: [[3blue1brown]] <br/> 

The [[Transformers and attention in language models | transformer]] is a core piece of technology in large language models and other modern AI tools, first introduced in the 2017 paper "Attention is All You Need" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The attention mechanism is crucial for how these models process data <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Core Idea: Contextualizing Word Meanings

The primary goal of the model being studied is to take a piece of text and predict the next word <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Input text is broken into small units called [[token_embeddings_and_highdimensional_vectors | tokens]], often words or pieces of words <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

The first step in a [[Transformers and attention mechanism | transformer]] is to associate each token with a [[token_embeddings_and_highdimensional_vectors | high-dimensional vector]], known as its [[Word Embeddings and Vectors | embedding]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Directions within this high-dimensional space correspond to semantic meaning; for example, adding a certain step can transform a masculine noun embedding into its feminine counterpart <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

The aim of a transformer is to progressively adjust these embeddings so they encode a much richer contextual meaning, rather than just representing an individual word <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Why Context Matters

Initially, a token's embedding is a lookup table with no reference to context <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. For instance, the word "mole" has different meanings in "American shrew mole," "one mole of carbon dioxide," and "take a biopsy of the mole," but its initial embedding would be the same across all <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The attention mechanism allows surrounding embeddings to pass information into a given word's embedding <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

A well-trained attention block calculates what needs to be added to a generic embedding to shift it towards one of its specific context-dependent meanings <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For example, if "tower" is preceded by "Eiffel," its embedding should update to specifically encode the Eiffel Tower, correlating with concepts like Paris and France <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. If also preceded by "miniature," it should update further, losing correlation with large things <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

Beyond refining a single word's meaning, the attention block enables the model to move information encoded in one embedding to another, even if they are far apart in the text <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Ultimately, for tasks like predicting the next word in a mystery novel after "Therefore the murderer was," the final embedding for "was" must incorporate all relevant information from the entire context window <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Single Head of Attention: The Process

To understand the computations, consider the phrase "a fluffy blue creature roamed the verdant forest," focusing on adjectives adjusting noun meanings <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This is what's called a single head of attention <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

The initial embedding for each word (`e`) encodes its meaning and position <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The goal is to produce a new set of refined embeddings where, for example, nouns have "ingested" meaning from their adjectives <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Most computations involve matrix-vector products, where matrices contain [[Adjusting weights and biases in neural networks | tuneable weights]] learned from data <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### 1. Queries (Q)

Each word's embedding is multiplied by a "query matrix" (`W_Q`) to produce a query vector <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Purpose**: Conceptually, a query is like a word "asking" for relevant information. For instance, the noun "creature" might ask, "Are there any adjectives sitting in front of me?" <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Dimensions**: Query vectors have a smaller dimension (e.g., 128) than the embedding vector <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Learning**: The entries of `W_Q` are model parameters, learned from data <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. A learned `W_Q` might map noun embeddings to directions encoding a search for preceding adjectives <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### 2. Keys (K)

At the same time, each embedding is multiplied by a "key matrix" (`W_K`) to produce a key vector <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Purpose**: Keys conceptually "answer" queries <a class="yt-timestamp" data-t="00:07:59">[00:08:03]</a>. Adjectives like "fluffy" and "blue" might produce keys that align closely with the query from "creature" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Dimensions**: Key vectors share the same smaller dimension as query vectors <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Learning**: `W_K` entries are also tunable parameters <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### 3. Calculating Attention Scores

To measure how well each key matches each query, a dot product is computed between every possible key-query pair <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   Higher dot products indicate closer alignment and relevance <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   When a key and query align, machine learning practitioners say the embedding of the key's word "attends to" the embedding of the query's word <a class="yt-timestamp" data-t="00:08:59">[00:09:02]</a>.
*   These raw scores can range from negative to positive infinity <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### 4. Normalizing Scores with Softmax (Attention Pattern)

To ensure scores represent weights (between 0 and 1, summing to 1 per column), a [[Activation functions in neural networks | softmax]] function is applied along each column of the dot product grid <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This normalized grid is called the attention pattern <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

The mathematical representation for this is `softmax(Q * K^T / sqrt(d_k))`, where `Q` and `K` are matrices of query and key vectors, and `d_k` is the dimension of the key/query space <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### 5. Masking for Future Tokens

During [[Neural network learning process | training]], it's crucial that later words do not influence earlier words to avoid "giving away the answer" <a class="yt-timestamp" data-t="00:11:46">[00:11:49]</a>. This is achieved through masking:
*   Before applying softmax, all entries representing a later token influencing an earlier one are set to negative infinity <a class="yt-timestamp" data-t="00:12:13">[00:12:16]</a>.
*   After softmax, these values become zero, while columns remain normalized <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   This masking is applied in [[Generative Pretrained Transformers | GPT]] models <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### 6. Values (V) and Updating Embeddings

Once the attention pattern (weights) is computed, words pass information to each other using "value vectors."
*   **Values**: Each word's embedding is multiplied by a "value matrix" (`W_V`) to produce a value vector <a class="yt-timestamp" data-t="00:13:44">[00:13:47]</a>.
    *   This value vector lives in the same high-dimensional space as the embeddings <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   Conceptually, if a word is relevant, its value vector represents "what exactly should be added to the embedding of that something else" <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **Weighted Sum**: For each column (representing a target word, e.g., "creature"), each value vector is multiplied by its corresponding weight from the attention pattern <a class="yt-timestamp" data-t="00:14:42">[00:14:45]</a>.
    *   For "creature," large proportions of the value vectors for "fluffy" and "blue" would be added, while others are nearly zeroed out <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   **Update**: All these rescaled values in the column are summed to produce a change vector (`delta-e`), which is then added to the original embedding of the target word <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   This process is applied across all columns, yielding a sequence of more contextually refined embeddings <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

### Parameter Counts for a Single Head

A single attention head is parameterized by three matrices: `W_Q`, `W_K`, and `W_V` <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. Using GPT-3 numbers:
*   `W_Q` and `W_K` each have 12,288 columns (embedding dimension) and 128 rows (key/query dimension), resulting in about 1.5 million parameters each <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   For efficiency, the `W_V` matrix is typically factored into two smaller matrices:
    *   A "value down" matrix mapping from the large embedding space to a smaller space (e.g., 128 dimensions) <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.
    *   A "value up" matrix mapping from this smaller space back to the embedding space <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
    *   This makes the overall value map a "low rank transformation" <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   All four matrices (W_Q, W_K, W_V_down, W_V_up) have similar sizes, leading to approximately 6.3 million parameters for one attention head <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Multi-Headed Attention

A full attention block within a [[Transformers and attention mechanism | transformer]] consists of [[Multiheaded attention in transformers | multi-headed attention]], where many single attention operations run in parallel <a class="yt-timestamp" data-t="00:20:31">[00:20:35]</a>.
*   GPT-3, for example, uses 96 attention heads per block <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   Each head has its own distinct `W_Q`, `W_K`, and `W_V` matrices, producing its own attention pattern and value vectors <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   For each token, every head produces a "proposed change" to be added to that token's embedding <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.
*   All these proposed changes are summed together and added to the original embedding, resulting in the refined embedding outputted by the block <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

### Why Multi-Headed Attention?

Running many distinct heads in parallel gives the model the capacity to learn numerous ways context changes meaning <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. Different heads might capture:
*   Grammatical relationships (e.g., adjective-noun) <a class="yt-timestamp" data-t="00:19:32">[00:19:35]</a>.
*   Syntactic relationships (e.g., verb-object) <a class="yt-timestamp" data-t="00:19:40">[00:19:43]</a>.
*   Semantic associations (e.g., "wizard" and "Harry" suggesting Harry Potter, versus "Queen," "Sussex," and "William" suggesting Prince Harry) <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### Total Parameters for Multi-Headed Attention

With 96 heads, each block of multi-headed attention in GPT-3 contains around 600 million parameters <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

## Overall Transformer Structure

Data flows through multiple layers of [[Transformers and attention in language models | transformers]]. Each layer includes attention blocks and other operations called multi-layer perceptrons (feed-forward neural networks) <a class="yt-timestamp" data-t="00:23:23">[00:23:28]</a>. This repeated processing allows embeddings to incorporate increasingly nuanced and abstract contextual information, leading to the encoding of higher-level concepts like sentiment, tone, or underlying truths <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.

GPT-3 has 96 distinct layers <a class="yt-timestamp" data-t="00:24:16">[00:24:21]</a>. The total number of key, query, and value parameters devoted to all attention heads is just under 58 billion <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>. While significant, this accounts for about one-third of GPT-3's total 175 billion parameters, with the majority coming from the multi-layer perceptron blocks <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.

## Scalability and Parallelization

A major reason for the attention mechanism's success is its extreme parallelizability, allowing a huge number of computations to run quickly using GPUs <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. This aligns with the observation that scaling models up often leads to significant qualitative improvements in performance <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

The attention pattern's size is equal to the square of the context size, which can be a significant bottleneck for large language models, making scaling context non-trivial <a class="yt-timestamp" data-t="00:12:42">[00:12:49]</a>.