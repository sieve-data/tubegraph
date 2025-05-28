---
title: Challenges and insights in Transformer architecture and training
videoId: yOT9WIL_2Kg
---

From: [[hu-po]] <br/> 

This article explores fundamental aspects of [[Scaling of language models and vision transformers | Transformer]] architecture and training, focusing on recent research that challenges conventional understandings of how these models store and process information.

## TokenFormer: Rethinking Transformer Scaling
The paper "TokenFormer: Rethinking Transformer Scaling with Tokenized Model Parameters," released on October 30, 2023, introduces a novel approach to [[Scaling of language models and vision transformers | Transformer scaling]] [00:02:56]. Originating from the Max Planck Institute for Informatics, Google, and Peking University, TokenFormer proposes replacing every component of a [[Hybrid Architectures and Transformer Block Efficiency | Transformer block]] with a new type of attention mechanism [00:03:08]. In this architecture, the model weights themselves function as tokens [00:03:36].

This design demonstrates that "attention is all you need" to an extreme degree, as it literally replaces all operations with attention mechanisms [00:04:06]. The model is described as a natively scalable architecture, leveraging the attention mechanism for both computations among input tokens and interactions between tokens and model parameters [00:09:23].

### P-Attention Mechanism
TokenFormer utilizes a mechanism called "P-attention" (parameter attention), where learnable tokens represent model parameters, and input tokens attend to these parameter tokens [00:09:48]. This contrasts with traditional linear projections, which involve fixed-size parameter matrices [00:08:00], where the dimensionality is hardcoded when the neural network is initialized and remains constant during training and inference [00:08:05].

In P-attention, instead of hardcoded weights, the weights are considered as tokens [00:10:13]. This allows for the addition or removal of more tokens as the model scales, enabling "progressive and efficient scaling" [00:10:22]. The paper demonstrates this by scaling models from 24 million to 1.4 billion parameters by adding new key-value parameter pairs [00:12:28].

This incremental scaling process allows for faster training, as a smaller model can be initially trained with less compute, and then expanded [00:10:50]. This leads to significant cost and time savings compared to training a large [[Scaling of language models and vision transformers | Transformer]] from scratch to reach the same performance level [00:11:53].

### Replacing Linear Projections
TokenFormer replaces all linear projections within a [[Hybrid Architectures and Transformer Block Efficiency | Transformer]] with P-attention layers [00:16:16]. This includes:
*   The linear projections in the Query (Q), Key (K), and Value (V) components of the attention mechanism [00:14:29].
*   The output projection layer after the attention block [00:15:38].
*   The multi-layer perceptron (MLP) or feed-forward network (FFN) layers [00:14:15].

Traditionally, the MLP/FFN accounts for approximately two-thirds of a [[Scaling of language models and vision transformers | Transformer]]'s total parameters [00:37:44]. By replacing it with an attention mechanism, TokenFormer simplifies the model architecture, making it more uniform and potentially easier to optimize at scale by using a single kernel type for all computations [00:38:28].

## Understanding the Transformer Block
A standard [[Hybrid Architectures and Transformer Block Efficiency | Transformer block]] typically consists of two main components:
1.  **Attention Mechanism:** Handles communication among input tokens [00:14:02].
2.  **Multi-Layer Perceptron (MLP) / Feed-Forward Network (FFN):** Processes information independently for each token [00:14:06].

### The Role of Attention (Q, K, V)
The attention mechanism involves Query (Q), Key (K), and Value (V) vectors, which are produced by multiplying input tokens by respective weight matrices [00:18:03].
*   **Query (Q) Vector:** Represents "what am I looking for?" [00:19:12].
*   **Key (K) Vector:** Represents "what do I contain?" or "what do I have?" [00:19:18].
*   **Value (V) Vector:** Contains the information to be added or combined [00:20:50].

The attention matrix is formed by the dot product of Queries and Keys, indicating the "agreement" or relevance between questions and answers [00:20:02]. A high agreement leads to a higher attention score, meaning more of the corresponding Value is incorporated into the output [00:20:49]. This process allows a token's representation to be enriched by information from other relevant tokens in the sequence, adjusting its "meaning" based on context [00:23:25].

The ability of attention mechanisms to handle variable-length sequences is attributed to the weighted sum operation and the use of layer normalizations [00:31:05]. Layer normalization ensures that even large sums are normalized to a consistent range (e.g., between zero and one), preventing exploding gradients and maintaining stable representations regardless of sequence length [00:31:58].

### Re-evaluating the MLP's Role
Conventional understanding, supported by research like "Knowledge Neurons in Pretrained Transformers" (2022), suggests that the MLP/FFN layers are primarily responsible for storing factual knowledge [00:35:36]. Studies have shown that by modifying specific neurons within these MLPs, factual knowledge (e.g., "The Eiffel Tower is in Paris") can be altered [00:36:02].

However, TokenFormer challenges this by entirely replacing the MLP with an attention mechanism, yet still achieving competitive performance [00:36:50]. This raises a crucial question: if the MLP, thought to be the repository of knowledge, is removed, where does the model's knowledge reside [00:37:07]? This suggests that the attention mechanism and the MLP might be more functionally similar than previously assumed, both leveraging high-dimensional spaces to encode information [00:55:14].

## Theoretical Insights: High-Dimensional Spaces and Memory
The efficiency of neural networks, particularly [[Scaling of language models and vision transformers | Transformers]], in storing vast amounts of information can be explained by mathematical properties of high-dimensional spaces.

### Johnson-Lindenstrauss Lemma and Orthogonality
The Johnson-Lindenstrauss Lemma highlights that in an N-dimensional space, the number of vectors that are "almost orthogonal" (e.g., between 89 and 91 degrees apart) grows exponentially with the number of dimensions [00:49:37].
*   **Implication:** Higher dimensionality provides exponentially more "real estate" to store distinct pieces of information or concepts [00:51:57]. Each orthogonal direction can represent a separate concept or meaning [00:51:00].

This property suggests that as [[Scaling of language models and vision transformers | Transformer]] models increase in size and dimensionality, their capacity to store and process information grows exponentially [01:00:41]. This is presented as the "real [[Scaling of language models and vision transformers | scaling]] law" governing their increasing intelligence [01:25:13].

### Analogy to Human Memory and Language
The process of storing and retrieving information in neural networks can be analogized to human memory and the concept of "memory palaces" (method of loci) [00:45:23]. This ancient mnemonic technique involves associating pieces of information with specific locations in a familiar imagined space [00:46:16].

François Chollet proposes that language acts as an indexing and retrieval system for our own ideas and memories [00:41:14]. Similarly, in [[Scaling of language models and vision transformers | Transformer]] models, language tokens, as vectors in a high-dimensional space, effectively serve as addresses to stored information [00:41:41]. Each layer of a [[Hybrid Architectures and Transformer Block Efficiency | Transformer block]] refines the "meaning" of a token by integrating contextual information, akin to traversing a path in a memory palace [00:43:12].

## Challenges and Future Directions

### Hallucinations
The problem of "hallucinations" in LLMs is not equivalent to overfitting [01:15:03]. Hallucination occurs when the model extrapolates or interpolates information in its high-dimensional semantic space, generating statements that are not grounded in its training data [01:12:04]. The model may not know whether a retrieved "fact" is true or merely an interpolation from learned areas [01:12:40].

Monitoring metrics like entropy or variance at each token prediction could indicate the model's certainty, potentially signaling a hallucination when variance is high, suggesting the model is in an "unseen" part of its high-dimensional space [01:13:59].

### Order Invariance and Randomized Training
The inherent order invariance of the attention mechanism (due to its reliance on weighted sums and layer normalization) means that the order of input tokens doesn't inherently matter; positional embeddings are added to provide this information [01:06:33].

A paper on randomized autoregressive visual generation explores this by randomly permuting the input sequence order during training for image generation [01:06:02]. While text is highly compact and ordered, visual data is often more low-level and redundant. Training on random permutations (gradually decreasing randomness over time) has shown effectiveness for images, suggesting that for certain data types, the specific scan order might be less critical than the overall set of information present [01:09:01]. This implies that models can still converge to the correct "location" in high-dimensional space regardless of the precise sequence of inputs, as long as the content is the same [01:11:11].

### Differential Transformers
The [[Comparison of xLSTM with Transformers and other models | Differential Transformer]] is another architecture that modifies the attention mechanism [01:19:07]. It computes attention scores as the difference between two separate softmax attention maps [01:19:21]. This subtraction technique aims to cancel out noise and promote a "sparse attention pattern," meaning only the most dominant and meaningful attention weights are retained, reducing reliance on tiny, less significant adjustments to token meanings [01:21:26]. The parameters governing this subtraction (like the magic number Lambda) are often empirically found rather than derived from pure theory [01:22:50].

These advancements collectively push the boundaries of understanding [[Scaling of language models and vision transformers | Transformer]] capabilities, suggesting that the architecture is more flexible and robust than previously thought, and that much of its power lies in its ability to efficiently navigate and store information within vast, high-dimensional spaces.