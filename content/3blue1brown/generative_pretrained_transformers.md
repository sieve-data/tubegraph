---
title: Generative Pretrained Transformers
videoId: wjZofJX0v4M
---

From: [[3blue1brown]] <br/> 

The acronym GPT stands for Generative Pretrained Transformer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These bots are designed to generate new text <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Components of GPT

### Generative

GPT models are "generative" because they create new text <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This generation is achieved by repeatedly predicting and sampling the next piece of text based on a given snippet, and then appending that sample to the text before making a new prediction <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This process of repeated prediction and sampling is what happens when users interact with ChatGPT or other [[large_language_models_and_prediction | large language models]], seeing text produced one word at a time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Pretrained

"Pretrained" signifies that the model has undergone a [[training_process_of_language_models | training process]] by learning from a massive amount of data <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The prefix also implies that there is scope for further fine-tuning on specific tasks through additional [[training_process_of_language_models | training]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### [[transformers_and_attention_in_language_models | Transformer]]

The "[[transformers_and_attention_in_language_models | Transformer]]" is the crucial component <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. A [[transformers_and_attention_in_language_models | Transformer]] is a specific type of [[neural_networks_and_transformers | neural network]], a machine learning model, and it represents the core invention behind the current boom in AI <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

Many different kinds of models can be built using [[transformers_and_attention_in_language_models | transformers]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>:
*   Some models process audio to produce transcripts <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Others create synthetic speech from text <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   Tools like DALL-E and Midjourney, which generate images from text descriptions, are also based on [[transformers_and_attention_in_language_models | transformers]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   The original [[transformers_and_attention_in_language_models | Transformer]], introduced by Google in 2017, was designed for translating text between languages <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

The variant of [[transformers_and_attention_in_language_models | transformer]] underlying tools like ChatGPT is trained to take in a piece of text (potentially with accompanying images or sound) and predict what comes next in the passage <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This prediction is expressed as a probability distribution over various text chunks that might follow <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

Early demonstrations of [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]] involved autocompleting stories and essays <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. To convert such a tool into a chatbot, a "system prompt" establishes the setting of a helpful AI assistant interacting with a user, followed by the user's initial question, and then the model predicts the AI assistant's response <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Data Flow in a [[transformers_and_attention_in_language_models | Transformer]]

A high-level overview of how data flows through a [[transformers_and_attention_in_language_models | transformer]] when it generates a word:

1.  **Input Tokenization**: The input text is broken down into smaller pieces called "tokens" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. For text, tokens are typically words, parts of words, or common character combinations <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. For images or sound, tokens could be small patches or chunks <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The model has a predefined vocabulary, e.g., 50,000 tokens for [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]] <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

2.  **Token to Vector (Embedding)**: Each token is associated with a vector, a list of numbers that encodes its meaning <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. In this high-dimensional space (e.g., 12,288 dimensions for [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]]) <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>, words with similar meanings tend to have vectors that are close to each other <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This initial transformation uses an "embedding matrix" (We) <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. The values of this matrix start randomly but are learned during [[training_process_of_language_models | training]] <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Directions in this embedding space can carry semantic meaning, such as gender information or relationships between concepts (e.g., Italy - Germany + Hitler ≈ Mussolini) <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

3.  **[[attention_mechanism_in_transformers | Attention Block]]**: The sequence of vectors passes through an operation called an [[attention_mechanism_in_transformers | attention block]] <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This block allows vectors to exchange information and update their values based on context <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. It identifies which words in a passage are relevant for updating the meaning of other words <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. The "meaning" of a word is entirely encoded in the entries of these vectors <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

4.  **Multi-Layer Perceptron (MLP) / Feed-Forward Layer**: After the [[attention_mechanism_in_transformers | attention block]], vectors pass through another operation, often called a multi-layer perceptron or feed-forward layer <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. In this block, vectors do not interact with each other; they all undergo the same operation in parallel <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This step can be thought of as asking a long list of questions about each vector and updating them based on the answers <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

5.  **Repeated Operations**: The process essentially repeats, cycling between [[multiheaded_attention_in_transformers | attention blocks]] and multi-layer perceptron blocks <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. The goal is for the essential meaning of the passage to be integrated into the last vector in the sequence <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

6.  **Output Prediction (Unembedding)**: An operation is performed on the final vector to produce a probability distribution over all possible next tokens <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This involves an "Unembedding matrix" (Wu) that maps the last vector to a list of values for each token in the vocabulary <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. The values in this matrix are also learned during [[training_process_of_language_models | training]] <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

7.  **Softmax Function**: A softmax function normalizes these values into a valid probability distribution, ensuring each value is between 0 and 1, and all values sum to 1 <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. Larger input values (called "logits") correspond to probabilities closer to 1 <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. A "temperature" parameter (T) can be added to the softmax function to influence the uniformity of the distribution; higher temperatures lead to more uniform distributions and potentially more creative but less coherent outputs, while lower temperatures lead to more predictable outputs <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.

### Underlying Computation

All operations within the [[attention_mechanism_in_transformers | attention blocks]] and multi-layer perceptron blocks primarily involve [[derivatives_in_neural_networks | matrix multiplications]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. The parameters of the model, known as "weights," are organized into matrices <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. These weights are the "brains" of the model, learned during [[training_process_of_language_models | training]], and determine its behavior <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The input data, which is processed by these weights, simply encodes the specific input for a given run <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Deep Learning Context

Deep learning is an approach to machine learning where data is used to determine how a model behaves <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Instead of explicitly coding a procedure, a flexible structure with tunable [[parameters_and_architecture_of_models_like_gpt3 | parameters]] is set up, and many examples of input/output pairs are used to tweak these [[parameters_and_architecture_of_models_like_gpt3 | parameters]] to mimic desired behavior <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

Deep learning models, like [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]] with its 175 billion [[parameters_and_architecture_of_models_like_gpt3 | parameters]] <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, have proven to scale remarkably well due to their use of the backpropagation [[training_process_of_language_models | training]] algorithm <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. For this algorithm to work at scale, models follow a specific format:
*   Inputs must be arrays of real numbers (tensors) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   Input data is progressively transformed through distinct layers, each structured as an array of real numbers <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   Model [[parameters_and_architecture_of_models_like_gpt3 | parameters]] (weights) interact with data only through weighted sums, often packaged as matrix-vector products <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]] Parameters

[[parameters_and_architecture_of_models_like_gpt3 | GPT-3]]'s 175 billion weights are organized into just under 28,000 distinct matrices, falling into eight different categories <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

Current parameter count tally from the transcript:
*   **Embedding Matrix (We)**: For [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]], with a vocabulary of 50,257 tokens and an embedding dimension of 12,288, this matrix accounts for approximately 617 million weights <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Unembedding Matrix (Wu)**: This matrix, which maps the final context vector to probability distribution over tokens, adds another 617 million [[parameters_and_architecture_of_models_like_gpt3 | parameters]] <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.
*   **Total so far**: Over 1 billion [[parameters_and_architecture_of_models_like_gpt3 | parameters]] <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. The remaining [[parameters_and_architecture_of_models_like_gpt3 | parameters]] are found within the [[attention_mechanism_in_transformers | attention blocks]] and multi-layer perceptron blocks, which form the "heart of the [[transformers_and_attention_in_language_models | transformer]]" <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.