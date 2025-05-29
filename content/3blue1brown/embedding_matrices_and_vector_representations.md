---
title: Embedding matrices and vector representations
videoId: wjZofJX0v4M
---

From: [[3blue1brown]] <br/> 

The core invention underlying the current boom in artificial intelligence (AI) is a specific type of neural network called a Transformer <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, which forms the basis for models like ChatGPT <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Understanding how data flows through a transformer involves grasping the concept of tokens and their [[Vector representation and coordinate systems | vector representations]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Tokens and Vectors

The initial step in a transformer's process involves breaking down the input into smaller pieces known as "tokens" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. For text, these tokens are typically words, parts of words, or common character combinations <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. If the input includes images or sound, tokens could be small patches of an image or chunks of sound <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

Each of these tokens is then associated with a vector, which is a list of numbers designed to encode the meaning of that piece <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. These vectors can be conceptualized as coordinates within a [[Highdimensional vector embeddings | high-dimensional space]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, where words or tokens with similar meanings are represented by vectors that are spatially close to one another <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## The Embedding Matrix

The process of converting words into vectors, often referred to as "embedding" a word, was a common practice in machine learning prior to the advent of transformers <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>, <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

The first [[Matrix representations and transformations | matrix]] encountered in a transformer model is the **embedding matrix** (labeled `We`) <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>, <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   This matrix has a column for each word in the model's predefined vocabulary, which for GPT-3 is 50,257 tokens <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>, <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>, <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   The columns of this matrix determine the vector representation for each word <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   Initially, the values in the embedding matrix are random, but they are learned and refined based on training data <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
*   In GPT-3, the embedding dimension is 12,288 <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>, resulting in approximately 617 million weights within this matrix alone <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>, <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

### Semantic Meaning in Embeddings

As a model adjusts its weights during training, it establishes embeddings where specific directions within the [[Highdimensional vector embeddings | high-dimensional space]] carry semantic meaning <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>, <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   For example, words with "tower-ish vibes" might cluster together <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>, <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   A classic illustration is how the vector difference between "woman" and "man" is similar to the difference between "king" and "queen" <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>, <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>, indicating a "gender information" direction <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
*   Similarly, vector arithmetic can reveal associations like the difference between "Italy" and "Germany" combined with "Hitler" yielding "Mussolini" <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>, <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>, or "sushi" plus ("Germany" minus "Japan") leading to "bratwurst" <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>, <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

### Dot Products and Similarity

The [[Matrix representations and transformations | dot product]] of two vectors is a crucial mathematical concept, especially for understanding attention mechanisms. It measures how well vectors align <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>, <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>:
*   A positive dot product indicates similar directions <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   Zero indicates perpendicularity <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   A negative dot product indicates opposite directions <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   Dot products are computationally derived by multiplying corresponding components and summing the results, which aligns with the weighted sums prevalent in deep learning models <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>, <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

For instance, the vector difference between "cats" and "cat" can represent a "plurality direction." Taking the dot product of this vector with singular nouns often yields lower values than with their plural counterparts, demonstrating how alignment with this direction indicates "plural-ness" <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>, <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

## Context and Vector Transformation

In transformers, embedding vectors are not static; they have the capacity to "soak in context" <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>, <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>. A vector initially representing a word like "king" can be progressively modified by various blocks within the network (e.g., attention blocks and multi-layer perceptrons) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This allows it to encode a more specific and nuanced meaning that incorporates the surrounding text <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>, <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

The network processes a fixed number of vectors simultaneously, known as its "context size" <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. For GPT-3, this was 2048 <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>, meaning the data always consists of an array of 2048 columns, each with 12,288 dimensions <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. This context size determines how much previous text the transformer can consider when predicting the next word <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

## The Unembedding Matrix and Softmax

At the very end of the network, the goal is to predict the next token by generating a probability distribution over all possible tokens <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>, <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. This involves two main steps:

1.  **Unembedding Matrix**: A [[Matrix representations and transformations | matrix]] called the **Unembedding matrix** (labeled `WU`) maps the final vector in the context to a list of 50,000 values (one for each token in the vocabulary) <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>, <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. These values are often referred to as "logits" <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>, <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>. Like the embedding matrix, its entries are learned during training <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>, <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>. It adds another 617 million parameters to the network <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>, <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
2.  **Softmax Function**: This function normalizes the raw output (logits) into a valid probability distribution, ensuring each value is between 0 and 1 and all values sum to 1 <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>, <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>, <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. The largest input values correspond to probabilities closest to 1, while smaller values approach 0 <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>, <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. It achieves this by taking the exponent of each input value (to make them positive) and then dividing each by the sum of all exponentiated values <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>, <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.

### Temperature Parameter

The softmax function can include a "temperature" (`T`) parameter in the denominator of its exponents <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>, <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
*   A larger `T` value gives more weight to lower input values, resulting in a more uniform and less predictable probability distribution <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>, <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.
*   A smaller `T` value makes larger input values dominate more aggressively, leading to a sharper, more predictable distribution <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
*   Setting `T` to zero means all weight goes to the maximum value, making the model always choose the most predictable word <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>, <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>, <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.

In summary, the transformation of input into [[Vector representation and coordinate systems | vectors]], their manipulation through [[matrix_representation_of_transformations | matrix representation of transformations]] (particularly [[matrixvector_multiplication | matrix-vector multiplication]]), and the final probability output via softmax, are fundamental to how modern AI models process and generate language <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>, <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.