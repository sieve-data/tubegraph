---
title: Word Embeddings and Vectors
videoId: wjZofJX0v4M
---

From: [[3blue1brown]] <br/> 

[[token_embeddings_and_highdimensional_vectors | Word embeddings]] are a foundational concept in understanding how models like ChatGPT process language. They represent text, images, or sound as lists of numbers, allowing the model to perform computations and understand relationships between different pieces of data <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

## Tokens and Their Vector Representation
The input to a transformer model is first broken down into small pieces called tokens <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. For text, these tokens are typically words, parts of words, or common character combinations <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. If images or sound are involved, tokens can be small patches of an image or chunks of sound <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

Each of these tokens is then associated with a [[abstract_vector_spaces | vector]], which is a list of numbers <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. This [[abstract_vector_spaces | vector]] is designed to encode the meaning of that token <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

> [!NOTE] Meaning Encoded in Vectors
> The "meaning" of a token or word is entirely encoded in the entries of its corresponding [[abstract_vector_spaces | vector]] <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

### High-Dimensional Space
These [[abstract_vector_spaces | vectors]] can be thought of as giving coordinates in a very high-dimensional space <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. Words with similar meanings tend to have [[abstract_vector_spaces | vectors]] that are located close to each other in this space <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

For GPT-3, these [[abstract_vector_spaces | word embeddings]] have 12,288 dimensions <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. The high dimensionality allows for many distinct directions, which is important for encoding semantic meaning <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>. While visualizing such high-dimensional spaces is difficult, a three-dimensional slice can be used for animation purposes <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>.

### Semantic Meaning and Relationships
During training, models adjust their weights to create [[token_embeddings_and_highdimensional_vectors | embeddings]] where directions in the space carry semantic meaning <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.
For example:
*   Words close to "tower" in the [[abstract_vector_spaces | embedding]] space tend to have similar "tower-ish" vibes <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.
*   The [[understanding_vectors_in_linear_algebra | vector]] difference between "woman" and "man" is similar to the difference between "king" and "queen", suggesting a "gender information" direction <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>, <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>. This allows for analogies like `king + (woman - man) ≈ queen` <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>.
*   `Italy - Germany + Hitler` is close to `Mussolini`, associating directions with "Italian-ness" and "WWII axis leaders" <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.
*   `Germany - Japan + sushi` can be close to `bratwurst` <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.
*   "Cat" was found to be close to "beast" and "monster" in one model <a class="yt-timestamp" data-t="16:27:00">[16:27:00]</a>.

## Dot Product and Similarity
The [[understanding_vectors_in_linear_algebra | dot product]] of two [[abstract_vector_spaces | vectors]] can be used to measure how well they align or how similar they are <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>.
*   A positive [[understanding_vectors_in_linear_algebra | dot product]] indicates similar directions <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.
*   A zero [[understanding_vectors_in_linear_algebra | dot product]] indicates perpendicular [[abstract_vector_spaces | vectors]] <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.
*   A negative [[understanding_vectors_in_linear_algebra | dot product]] indicates opposite directions <a class="yt-timestamp" data-t="17:03:00">[17:03:00]</a>.

For instance, the [[understanding_vectors_in_linear_algebra | vector]] `cats - cat` might represent a "plurality direction". Computing its [[understanding_vectors_in_linear_algebra | dot product]] with singular versus plural nouns shows consistently higher values for plural nouns, indicating better alignment with this "plurality" direction <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>.

## Contextualization of Vectors
While initially, [[token_embeddings_and_highdimensional_vectors | vectors]] are simply plucked from an [[abstract_vector_spaces | embedding]] matrix, representing a single word's meaning <a class="yt-timestamp" data-t="19:24:00">[19:24:00]</a>, the primary goal of the neural network (like a transformer) is to enable these [[abstract_vector_spaces | vectors]] to "soak in context" <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>.

As [[abstract_vector_spaces | vectors]] pass through the network's attention blocks and feed-forward layers, they are progressively updated to incorporate information from their surroundings <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>. This allows a [[abstract_vector_spaces | vector]] that started as "king" to evolve into a more nuanced representation encoding details like "a king who lived in Scotland, murdered the previous king, and is described in Shakespearean language" <a class="yt-timestamp" data-t="18:51:00">[18:51:00]</a>.

## The Embedding Matrix
The [[abstract_vector_spaces | embedding]] matrix is the first set of "weights" in a transformer model <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>. It has a column for each word in the model's predefined vocabulary, and these columns determine the initial [[abstract_vector_spaces | vector]] for each word <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>. Its values are learned during the training process <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>.

For GPT-3:
*   Vocabulary size: 50,257 tokens (not strictly words) <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>.
*   Embedding dimension: 12,288 <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>.
*   Total weights: Approximately 617 million <a class="yt-timestamp" data-t="18:14:00">[18:14:00]</a>.

## The Unembedding Matrix
At the very end of the network, after the [[abstract_vector_spaces | vectors]] have processed context, another matrix called the Unembedding matrix (`WU`) is used <a class="yt-timestamp" data-t="21:45:00">[21:45:00]</a>. This matrix maps the very last [[abstract_vector_spaces | vector]] in the sequence to a list of values, one for each token in the vocabulary <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.

For GPT-3, the Unembedding matrix adds another 617 million parameters, bringing the total count to just over a billion so far <a class="yt-timestamp" data-t="21:56:00">[21:56:00]</a>.

## Softmax Function
The output of the Unembedding matrix is a list of "logits" <a class="yt-timestamp" data-t="25:37:00">[25:37:00]</a>. To convert these raw values into a probability distribution (where each value is between 0 and 1, and all values sum to 1), the softmax function is applied <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>, <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>.

Softmax works by:
1.  Raising `e` to the power of each number in the input list, making all values positive <a class="yt-timestamp" data-t="23:13:00">[23:13:00]</a>.
2.  Dividing each resulting term by the sum of all terms, normalizing them to sum to 1 <a class="yt-timestamp" data-t="23:21:00">[23:21:00]</a>.

If one input value (logit) is significantly larger than the rest, its corresponding output probability will dominate the distribution <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>. However, it remains "soft" in that other similarly large values also retain meaningful weight <a class="yt-timestamp" data-t="23:42:00">[23:42:00]</a>.

### Temperature Parameter
When a model like ChatGPT uses this distribution to generate the next word, a "temperature" parameter (T) can be introduced into the softmax function <a class="yt-timestamp" data-t="23:59:00">[23:59:00]</a>.
*   **Larger T:** Gives more weight to lower values, resulting in a more uniform and diverse distribution, leading to less predictable text <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>.
*   **Smaller T:** Causes larger values to dominate more aggressively, leading to more predictable text <a class="yt-timestamp" data-t="24:22:00">[24:22:00]</a>.
*   **T = 0:** All weight goes to the maximum value, leading to the most predictable word every time <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.

> [!EXAMPLE] Temperature in Story Generation
> With a seed text like "once upon a time there was A" <a class="yt-timestamp" data-t="24:33:00">[24:33:00]</a>:
> *   **Temperature zero:** Generates a predictable, trite story like a derivative of Goldilocks <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>.
> *   **Higher temperature:** Starts more originally (e.g., about a young web artist) but risks degenerating into nonsense <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>. API limits typically prevent setting T above 2 to avoid overly nonsensical outputs <a class="yt-timestamp" data-t="25:06:00">[25:06:00]</a>.