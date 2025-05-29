---
title: Generative Pretrained Transformer architecture
videoId: wjZofJX0v4M
---

From: [[3blue1brown]] <br/> 

The initials GPT stand for Generative Pretrained Transformer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These are bots designed to generate new text <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The term "Pretrained" indicates that the model has undergone an initial learning process using a massive amount of data <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The "pre" prefix suggests that further fine-tuning for specific tasks with additional [[training_process_of_large_language_models | training]] is possible <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The "Transformer" component is the foundational invention behind the current surge in AI <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## What is a Transformer?

A [[role_of_transformers_in_language_models | transformer]] is a specific type of neural network, a machine learning model, that forms the core of modern AI advancements <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

Transformers can be used in various models:
*   Converting audio into a transcript <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Producing synthetic speech from text <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   Generating images from text descriptions (e.g., DALL-E, Midjourney) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   Translating text between languages (original invention by Google in 2017) <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

The variant underpinning tools like ChatGPT is trained to take a piece of text (potentially with accompanying images or sound) and predict what comes next in the passage <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This prediction is given as a probability distribution over many potential text chunks <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### From Prediction to Generation
While predicting the next word might seem different from generating new text, a prediction model can be leveraged for generation <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. To generate a longer piece of text:
1.  Provide an initial snippet of text <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
2.  The model samples randomly from its generated probability distribution <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
3.  The sampled text is appended to the original snippet <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
4.  The entire process is repeated with the new, longer text <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

This repeated prediction and sampling process is essentially how [[large_language_models_and_their_function | large language models]] like ChatGPT generate text one word at a time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Early demos of GPT-3 showcased this autocomplete function for stories and essays <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. To make a chatbot, a "system prompt" establishes the setting (e.g., a helpful AI assistant), and the user's input becomes the first dialogue <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## High-Level Data Flow through a Transformer

Here's a broad overview of how data moves through a [[transformer_architecture_and_its_internal_workings | transformer]] when generating a word <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>:

1.  **Tokenization**: The input is broken into "tokens" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. For text, these are usually words, sub-words, or common character combinations <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. For images or sound, they could be patches or chunks <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  **Vector Association (Embeddings)**: Each token is converted into a vector (a list of numbers) that encodes its meaning <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. In a high-dimensional space, words with similar meanings will have vectors close to each other <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
3.  **[[attention_mechanism_in_transformers | Attention Block]]**: The sequence of vectors passes through an [[use_of_attention_mechanisms_in_transformers | attention block]] <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This allows vectors to "talk" to each other, exchanging information to update their values based on context <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. For example, it differentiates the meaning of "model" in "machine learning model" versus "fashion model" <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. The updated "meaning" is entirely encoded in the vector entries <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  **Multi-Layer Perceptron (Feed-Forward Layer)**: After attention, vectors pass through another operation, often called a multi-layer perceptron or feed-forward layer <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. In this block, vectors do not interact with each other but undergo the same operation in parallel <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This step can be thought of as asking a series of questions about each vector and updating them based on the answers <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
5.  **[[matrix_representation_of_transformations | Matrix Multiplications]]**: All operations within these blocks primarily involve a large number of [[matrix_representation_of_transformations | matrix multiplications]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
6.  **Repetition**: The process of alternating between attention blocks and multi-layer perceptron blocks repeats multiple times <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. The goal is for the "essential meaning" of the passage to be distilled into the very last vector in the sequence <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
7.  **Final Prediction**: An operation on the last vector produces a probability distribution over all possible next tokens (text chunks) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## Deep Learning Foundations for Transformers

[[training_neural_networks_for_handwritten_digit_recognition | Deep learning]] models, including transformers, are a class of machine learning models that have demonstrated remarkable scalability in recent decades <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. They all utilize the backpropagation [[training_process_of_large_language_models | training]] algorithm <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. For backpropagation to work effectively at scale, these models adhere to a specific format <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>:

*   **Input Format**: All inputs must be formatted as an array of real numbers, often referred to as a "tensor" <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Layered Transformations**: The input data is progressively transformed through distinct layers, with each layer also structured as an array of real numbers, until a final output layer is reached <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. For text models, the final layer is a list of numbers representing the probability distribution for possible next tokens <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Weights (Parameters)**: Model parameters, known as "weights," interact with the data solely through weighted sums <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. These weighted sums are typically packaged as components in a [[matrix_representation_of_transformations | matrix vector product]] <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. Non-linear functions are also interspersed but do not depend on parameters <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **GPT-3 Scale**: GPT-3, for instance, has 175 billion parameters organized into nearly 28,000 distinct matrices, falling into eight categories <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. The weights are the "brains" of the model, learned during [[training_process_of_large_language_models | training]], while the data being processed is the specific input for a given run <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

## Initial Step: Tokenization and Embedding

The first step in text processing is to break the input into "tokens" and convert them into vectors <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Embedding Matrix (We)
The model uses a predefined vocabulary (e.g., 50,000 tokens) <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. The "embedding matrix" (`We`) has a column for each of these words/tokens, which determines the vector representation for each <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Like all matrices, its values begin randomly but are learned from data during [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

### Word Embeddings and Semantic Meaning
"Embedding a word" means representing it as a point in a high-dimensional space <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. GPT-3's word embeddings have 12,288 dimensions <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. During [[training_process_of_large_language_models | training]], the model tunes these embeddings such that directions in this space acquire semantic meaning <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

Examples of semantic directions:
*   The vector difference between "woman" and "man" is similar to the difference between "king" and "queen" <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. This suggests a "gender" direction <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   Subtracting "Germany" from "Italy" and adding it to "Hitler" yields a vector close to "Mussolini," associating directions with "Italian-ness" and "WWII Axis leaders" <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
*   The difference between "Germany" and "Japan" added to "sushi" results in a vector near "bratwurst" in some models <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

The [[matrix_representation_of_transformations | dot product]] of two vectors measures their alignment <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>:
*   Positive: vectors point in similar directions <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   Zero: perpendicular <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   Negative: opposite directions <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
This allows for quantitative measurement of semantic properties, like how "plural" a model finds a word <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

The embedding matrix is the first set of learned "weights" in the model <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. For GPT-3, with a vocabulary of 50,257 tokens and an embedding dimension of 12,288, this matrix contains approximately 617 million weights <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. Initially, each vector plucked from this matrix only encodes the meaning of a single word without context <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. The network's primary goal is to enable these vectors to absorb rich, context-specific meanings as they flow through the layers <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.

### Context Size
A transformer can only process a fixed number of vectors at a time, known as its "context size" <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. For GPT-3, the context size was 2048, meaning the data always looked like an array of 2048 columns, each with 12,000 dimensions <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This limits how much preceding text the transformer can consider when making a prediction <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

## Final Step: Unembedding and Probability Prediction

At the end of the transformer, the goal is to produce a probability distribution over all possible next tokens <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

### Unembedding Matrix (WU)
A separate matrix, the "Unembedding matrix" (`WU`), maps the very last vector in the context to a list of values (one for each token in the vocabulary, e.g., 50,000 values) <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This matrix's entries are also learned during [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. Similar to the embedding matrix but with swapped dimensions, it adds another 617 million parameters to the network <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

### Softmax Function
To convert the list of values into a valid probability distribution (where each value is between 0 and 1, and all sum to 1), a function called "softmax" is used <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. Softmax ensures that larger input values result in probabilities closer to 1, while smaller values become closer to 0 <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

The mathematical process for softmax:
1.  Raise *e* to the power of each number in the list, ensuring all values are positive <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
2.  Divide each term by the sum of all these positive values, normalizing the list to sum to 1 <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

A "temperature" parameter (T) can be introduced into the softmax function to influence the distribution's uniformity <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.
*   **Larger T**: Gives more weight to lower values, resulting in a more uniform distribution and potentially more varied, less predictable outputs <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
*   **Smaller T**: Causes larger values to dominate more aggressively, leading to more predictable outputs (e.g., T=0 makes it always pick the maximum value) <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

The raw, unnormalized outputs before softmax are referred to as "logits" <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.

## Conclusion

Understanding the core components like word embeddings, the softmax function, how [[matrix_representation_of_transformations | dot products]] measure similarity, and the prevalence of [[matrix_representation_of_transformations | matrix multiplication]] with tunable parameters lays the groundwork for comprehending the [[attention_mechanism_in_transformers | attention mechanism]] <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>, which is considered the heart of the [[transformer_architecture_and_its_internal_workings | transformer]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Subsequent explanations delve into multi-layer perceptron blocks and [[training_process_of_large_language_models | training]] processes <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.