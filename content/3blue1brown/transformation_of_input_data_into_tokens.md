---
title: Transformation of input data into tokens
videoId: wjZofJX0v4M
---

From: [[3blue1brown]] <br/> 

The "T" in GPT (Generative Pretrained Transformer) stands for [[role_of_transformers_in_language_models | Transformer]], a specific kind of neural network and machine learning model that is the core invention underlying the current boom in AI <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. When a chatbot like ChatGPT generates a word, the process begins with the transformation of input data <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Input Processing: Breaking Down Data into Tokens

The first step in a [[role_of_transformers_in_language_models | transformer]] model is to break up the input into small pieces called tokens <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Text Inputs**: For text, tokens typically consist of words, small pieces of words, or common character combinations <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Other Media**: If images or sound are involved, tokens could be small patches of an image or little chunks of sound <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

Each of these tokens is then associated with a vector, which is a list of numbers meant to encode the meaning of that piece of data <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. Conceptually, these vectors provide coordinates in a very high-dimensional space where words with similar meanings tend to be represented by vectors that are close to each other <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### The Embedding Matrix

The transformation of words into vectors is achieved through an "embedding matrix" <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Structure**: This matrix has a single column for each word in the model's predefined vocabulary, which for GPT-3 is 50,257 tokens <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>, <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Learning Process**: The values within this embedding matrix, like all weight matrices in the model, start randomly but are learned based on data during the [[training_process_of_large_language_models | training]] process <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>, <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Dimensions**: In GPT-3, these word embeddings have 12,288 dimensions <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Parameter Count**: The embedding matrix alone contributes approximately 617 million weights to the model (50,257 vocabulary size * 12,288 embedding dimensions) <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>, <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

### Semantic Meaning in Embeddings

"Embedding a word" means thinking of these vectors geometrically as points in a high-dimensional space <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>, <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. As a model [[training_process_of_large_language_models | trains]] and tunes its weights, it settles on embeddings where directions in the space acquire a semantic meaning <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>, <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

*   **Similarity Measurement**: The dot product of two vectors is a useful mathematical intuition to measure how well they align <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>, <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
    *   Positive dot product: Vectors point in similar directions <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>, <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
    *   Zero dot product: Vectors are perpendicular <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
    *   Negative dot product: Vectors point in opposite directions <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

*   **Semantic Directions**: The model learns to encode meaning such that:
    *   Words with similar "vibes" (e.g., "tower" and related words) have close embeddings <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
    *   Vector differences can represent abstract relationships (e.g., "woman" - "man" is similar to "queen" - "king") <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>, <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This implies a direction in space encodes gender information <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
    *   Quantitative measurement of concepts: The difference between "cats" and "cat" can represent a "plurality direction," where plural nouns align more with this direction <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>, <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

### Incorporating Context

In [[role_of_transformers_in_language_models | transformers]], the vectors in the embedding space are designed to represent individual words and also to soak in context <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>, <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>. Initially, vectors are simply "plucked" from the embedding matrix, encoding only the meaning of a single word without surrounding input <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>, <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

The primary goal of the network that these vectors flow through is to enable each vector to absorb a richer, more specific meaning based on its context <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>, <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. For example, the meaning of "model" in "a machine learning model" differs from "a fashion model" <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This contextual understanding is managed by mechanisms like the [[use_of_attention_mechanisms_in_transformers | attention block]], which allows vectors to communicate and update their values based on other words in the sequence <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

The network can only process a fixed number of vectors at a time, known as its "context size" <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. For GPT-3, the context size was 2048, meaning the data flowing through the network always consists of an array of 2048 columns, each with 12,000 dimensions <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>, <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. This limits how much text a [[role_of_transformers_in_language_models | transformer]] can incorporate when making a prediction <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

### The Unembedding Matrix

At the very end of the [[role_of_transformers_in_language_models | transformer]] network, another matrix, called the "Unembedding matrix" (WU), is used <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>. This matrix maps the final context-rich vector in the sequence to a list of 50,000 values (one for each token in the vocabulary), which are then normalized into a probability distribution for the next token <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>, <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. The Unembedding matrix, conceptually similar to the embedding matrix but with swapped order, adds another 617 million parameters <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>, <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.

This process of input transformation, contextual processing, and output prediction forms the foundation for understanding complex mechanisms like [[use_of_attention_mechanisms_in_transformers | attention]] within [[role_of_transformers_in_language_models | transformer]] models <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.