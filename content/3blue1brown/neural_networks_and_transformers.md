---
title: Neural Networks and Transformers
videoId: wjZofJX0v4M
---

From: [[3blue1brown]] <br/> 

The term "[[generative_pretrained_transformers | Generative Pretrained Transformer]]" (GPT) refers to bots that generate new text and have been trained from a massive amount of data, with room for fine-tuning on specific tasks [00:00:05]. The "Transformer" component is a specific kind of [[structure_of_neural_networks | neural network]], a machine learning model, and serves as the core invention underpinning the current boom in artificial intelligence [00:00:23].

## Applications of Transformers
[[transformers_and_attention_in_language_models | Transformers]] form the basis for various AI models:
*   **Audio processing** Some models take audio input and produce a transcript [00:00:47].
*   **Synthetic speech generation** Other models produce synthetic speech from text [00:00:51].
*   **Image generation** Tools like DALL-E and Midjourney, which generate images from text descriptions, are based on [[transformers_and_attention_in_language_models | Transformers]] [00:00:56].
*   **Language translation** The original Transformer, introduced in 2017 by Google, was invented for translating text from one language to another [00:01:13].
*   **Predicting next elements** Models like ChatGPT are trained to take text (and potentially accompanying images or sound) and predict what comes next in a passage, typically as a probability distribution over possible text chunks [00:01:22]. This process of repeated prediction and sampling is how [[transformers_and_attention_in_language_models | large language models]] like ChatGPT produce text one word at a time [00:02:41].

## High-Level Data Flow in a Transformer
When a chatbot generates a word, the process involves several steps [00:03:14]:

### Tokenization and Vector Embeddings
The input is first broken into "tokens," which can be words, parts of words, or common character combinations for text, or patches/chunks for images/sound [00:03:19]. Each token is then associated with a "vector" (a list of numbers) that encodes its meaning [00:03:37]. These vectors can be thought of as coordinates in a high-dimensional space, where words with similar meanings tend to have vectors that are close to each other [00:03:45].

The conversion of words into vectors happens via an "embedding matrix" (labeled `We`), where each word in the model's predefined vocabulary (e.g., 50,000 tokens for GPT-3) corresponds to a column [00:12:55]. This matrix's values are learned during training [00:13:15]. For GPT-3, the embedding dimension is 12,288, leading to about 617 million weights in this matrix [00:13:52], [00:18:10].

Semantic meaning is encoded in the directions of this high-dimensional space [00:14:28]. For example, the difference vector between "woman" and "man" might be similar to that between "king" and "queen" [00:14:58].

### [[attention_mechanism_in_transformers | Attention Blocks]]
The sequence of vectors passes through an "attention block," which allows vectors to communicate and update their values by passing information back and forth [00:03:55]. This mechanism helps resolve the meaning of words based on their context, e.g., distinguishing "model" in "machine learning model" from "fashion model" [00:04:04]. The [[attention_mechanism_in_transformers | Attention Mechanism]] is considered the heart of the [[transformers_and_attention_in_language_models | Transformer]] [00:06:58], [00:26:23].

### Multi-Layer Perceptrons (Feed-Forward Layers)
After the [[attention_mechanism_in_transformers | attention block]], vectors pass through another operation, referred to as a "multi-layer perceptron" or "feed-forward layer" [00:04:29]. In this block, vectors are processed independently and in parallel, without interacting with each other [00:04:38]. This step can be conceptualized as asking a series of questions about each vector and updating it based on the answers [00:04:45].

### Core Computation: Matrix Multiplications
All operations within both [[attention_mechanism_in_transformers | attention blocks]] and multi-layer perceptron blocks are essentially "giant piles of matrix multiplications" [00:04:54]. The "weights" of the model, which are the learnable parameters, are organized into matrices that transform the data vectors [00:10:54].

### Context Size
A [[transformers_and_attention_in_language_models | Transformer]] can only process a fixed number of vectors at a time, known as its "context size" [00:19:49]. For GPT-3, the context size was 2048, meaning the network processes an array of 2048 columns, each with 12,000 dimensions [00:19:54]. This limits how much text the model can consider when making a prediction [00:20:05].

## Prediction Mechanism
At the very end of the [[structure_of_neural_networks | network]], the goal is to produce a probability distribution over all possible next tokens [00:20:29].

### Unembedding Matrix
The last vector in the sequence is mapped to a list of values (one for each token in the vocabulary) using an "Unembedding matrix" (labeled `WU`) [00:20:58]. Like the embedding matrix, its entries are learned during training [00:21:50]. This matrix has a row for each word in the vocabulary and a number of elements equal to the embedding dimension, adding another 617 million parameters to the network for GPT-3 [00:21:56].

### Softmax Function
The list of values produced by the Unembedding matrix (often called "logits" [00:25:37]) is then normalized into a probability distribution using the "softmax function" [00:23:00]. This function ensures each value is between 0 and 1, and all values sum to 1 [00:23:31]. It works by raising *e* to the power of each number (making them positive) and then dividing each by the sum of all values [00:23:13].

Softmax can incorporate a "temperature" constant (T) in the denominator of its exponents [00:24:04]. A larger T makes the distribution more uniform, allowing for less predictable word choices, while a smaller T makes larger values dominate more aggressively [00:24:17].

## Deep Learning Foundations of Transformers

[[transformers_and_attention_in_language_models | Transformers]] are a class of deep learning models that have demonstrated remarkable scalability [00:09:10].

### Machine Learning vs. Deep Learning
Machine learning involves using data to determine how a model behaves, creating a function that takes an input (e.g., an image) and produces a label or predicts a next word [00:07:33]. Instead of explicitly coding the task, a flexible [[structure_of_neural_networks | structure]] with "tunable parameters" (like "knobs and dials") is set up, and many examples are used to adjust these parameters to mimic desired behavior [00:08:05].

Deep learning models are characterized by their use of the "backpropagation" training algorithm and adhere to a specific format for efficient scaling [00:09:16].

### Tunable Parameters (Weights)
In deep learning, model parameters are referred to as "weights" [00:10:17]. These weights constitute the "actual brains" of the model, being learned during training and determining its behavior [00:12:12]. GPT-3, for instance, has 175 billion parameters organized into nearly 28,000 distinct matrices [00:08:52], [00:11:10].

### Data Format
The input to any deep learning model must be formatted as an array of real numbers, often called a "tensor" [00:09:41]. This input data is progressively transformed through multiple layers, with each layer also structured as an array of real numbers, until a final output layer is produced [00:09:56].

### Weighted Sums and Matrix-Vector Products
A key feature of deep learning models is that parameters interact with data primarily through "weighted sums" [00:10:22]. These weighted sums are typically packaged as components in "matrix vector products" [00:10:37]. Understanding how to interpret these underlying matrices is crucial [00:04:58], [00:10:54].

## Semantic Meaning in Embeddings
Word embeddings represent words as points in a high-dimensional space, and during training, the model learns embeddings where specific directions in this space acquire semantic meaning [00:14:21].

### Dot Product and Alignment
The "dot product" of two vectors is a way to measure how well they align [00:16:37]. Computationally, it involves multiplying corresponding components and adding the results, aligning with the "weighted sums" computation [00:16:44]. Geometrically, a positive dot product indicates similar directions, zero means perpendicular, and negative means opposite directions [00:16:55]. This concept is crucial for understanding the [[attention_mechanism_in_transformers | Attention Mechanism]] [00:16:34], [00:26:10].

### Soaking in Context
The vectors in the embedding space are not static representations of individual words but have the capacity to "soak in context" [00:18:25]. A vector initially representing a word like "king" might be modified through the [[structure_of_neural_networks | network]] to encode nuanced information from its surroundings, such as being a king in Scotland who murdered the previous king [00:18:43]. The primary goal of the [[structure_of_neural_networks | network]] is to enable each vector to incorporate a richer, more specific meaning from its context [00:19:37].

The next step in understanding [[transformers_and_attention_in_language_models | Transformers]] involves delving into the details of the [[attention_mechanism_in_transformers | attention mechanism]], which is central to how context is integrated [00:06:06], [00:26:23].