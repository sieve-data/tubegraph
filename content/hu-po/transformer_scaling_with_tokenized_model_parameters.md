---
title: Transformer scaling with tokenized model parameters
videoId: yOT9WIL_2Kg
---

From: [[hu-po]] <br/> 

The "TokenFormer" is a novel model architecture that rethinks [[transformerbased_model_architectures | Transformer scaling]] by employing tokenized model parameters. Released on October 30th, the paper "TokenFormer: Rethinking Transformer Scaling with Tokenized Model Parameters" comes from the Max Planck Institute for Informatics, Google, and Peking University <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

## Core Innovation: P-Attention

TokenFormer replaces traditional linear projections within a Transformer block with a new attention mechanism called "P-attention" (Parameter attention) <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. This means that model weights themselves are represented as tokens <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

Traditionally, linear projections involve a fixed matrix of weights multiplied by an input vector <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. The dimensionality of these matrices is hardcoded when the neural network is initialized and remains constant during training and inference <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.

In P-attention:
*   **Input tokens** act as queries <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>.
*   **Model parameters** are represented as learnable "parameter tokens" that act as keys and values <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a> <a class="yt-timestamp" data-t="28:55:00">[28:55:00]</a>.
*   The input tokens attend to these parameter tokens, allowing for dynamic interactions between input and model weights <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

TokenFormer replaces *all* linear projections in a Transformer block with P-attention layers <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>. This includes:
*   The linear projections in the attention mechanism (for Query, Key, and Value matrices) <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   The output projection after the attention mechanism <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   The projections within the Multi-Layer Perceptron (MLP) or Feed-Forward Network (FFN) blocks <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a>.

This means that [[transformerbased_model_architectures | everything is attention]] <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.

## Scalability Advantages

TokenFormer proposes a natively [[scalability_of_transformerbased_diffusion_models | scalable architecture]] that leverages the attention mechanism for interactions between tokens and model parameters <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.

Unlike traditional [[transformerbased_model_architectures | Transformer architectures]] where changing architectural components (e.g., channel dimensions) typically requires retraining the entire model <a class="yt-timestamp" data-t="27:27:00">[27:27:00]</a>, TokenFormer allows for:
*   **Progressive and efficient [[scaling_of_language_models_and_vision_transformers | scaling]]**: New learnable tokens can be added to expand existing key-value parameter sets <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.
*   **Incremental growth**: Training can start with a small model (e.g., 24 million parameters) and progressively add more model tokens to expand to larger sizes (e.g., 1.4 billion parameters) <a class="yt-timestamp" data-t="12:27:00">[12:27:27]</a>.
*   **Faster training**: By starting with a smaller model and gradually expanding, TokenFormer can reach the same performance as a Transformer trained from scratch, but with significantly less compute cost (TPU hours) <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a> <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.

This "crystallization" approach to model growth, where intelligence starts from a small core and expands, offers significant savings in training time and money <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a> <a class="yt-timestamp" data-t="01:28:16">[01:28:16]</a>.

## Re-evaluating Transformer Components

The traditional understanding of [[transformerbased_model_architectures | Transformer architectures]] posits that:
*   The **attention mechanism** handles communication between input tokens <a class="yt-timestamp" data-t="34:51:00">[34:51:00]</a>.
*   The **Multi-Layer Perceptron (MLP)** or **Feed-Forward Network (FFN)** layers are responsible for storing factual knowledge <a class="yt-timestamp" data-t="35:30:00">[35:30:00]</a>. Research has shown that modifying specific neurons in MLPs can alter factual knowledge in models <a class="yt-timestamp" data-t="35:52:00">[35:52:00]</a>.

TokenFormer challenges this understanding because it replaces the MLP/FFN with attention mechanisms, yet still performs well <a class="yt-timestamp" data-t="36:50:00">[36:50:00]</a>. This suggests that the attention and MLP layers might be performing more similar functions than previously thought, both utilizing high-dimensional spaces to encode information <a class="yt-timestamp" data-t="55:14:00">[55:14:00]</a>.

Furthermore, MLPs constitute about two-thirds of the total parameters in a [[transformerbased_model_architectures | Transformer network]] (e.g., in Llama models) <a class="yt-timestamp" data-t="37:49:00">[37:49:00]</a>. By unifying the architecture under a single "P-attention" kernel, optimizing computation becomes easier, leading to more simplified and uniform model architectures <a class="yt-timestamp" data-t="38:26:00">[38:26:00]</a>.

## Deep Dive into the Attention Mechanism

In a Transformer's attention mechanism:
*   Input tokens `x` are transformed into Query (Q), Key (K), and Value (V) vectors via linear projections (multiplication by `WQ`, `WK`, `WV` weight matrices) <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.
*   **Query (Q)**: "What am I looking for?" <a class="yt-timestamp" data-t="19:15:00">[19:15:00]</a> (a question from a token).
*   **Key (K)**: "What do I contain?" <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a> (an answer or piece of information from a token).
*   **Value (V)**: The actual information or data that will be aggregated.

The attention matrix is calculated by the dot product of Queries and Keys, representing the "agreement" between questions and answers <a class="yt-timestamp" data-t="20:05:00">[20:05:00]</a>. A high dot product means high agreement, indicating that the corresponding Value should be given more weight when forming the output <a class="yt-timestamp" data-t="20:42:00">[20:42:00]</a>. This weighted sum of values allows tokens to integrate contextual information, refining their meaning <a class="yt-timestamp" data-t="23:36:00">[23:36:36]</a>.

Attention mechanisms naturally handle variable-length sequences because they operate on a weighted sum, which is extensible <a class="yt-timestamp" data-t="31:21:00">[31:21:00]</a>. Layer normalization further stabilizes this process by scaling vector magnitudes, ensuring that accumulated values remain within a reasonable range <a class="yt-timestamp" data-t="31:58:00">[31:58:00]</a>.

### Theoretical Implications: High-Dimensional Spaces and Information Storage

The ability of [[transformerbased_model_architectures | Transformer models]] to store and retrieve vast amounts of information can be intuited through the properties of high-dimensional spaces <a class="yt-timestamp" data-t="51:00:00">[51:00:00]</a>:
*   **Johnson-Lindenstrauss Lemma**: In an N-dimensional space, the number of vectors that are nearly orthogonal (e.g., between 89 and 91 degrees apart) grows exponentially with the number of dimensions <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a>. This means that as the dimensionality of the vector space increases, there is exponentially more "real estate" to store distinct pieces of information or concepts <a class="yt-timestamp" data-t="52:51:00">[52:51:00]</a>.
*   **Information Encoding**: Just as an anamorphic sculpture can encode multiple images depending on the viewing angle <a class="yt-timestamp" data-t="53:41:00">[53:41:00]</a>, high-dimensional spaces can store immense amounts of information. Large language models (LLMs) are essentially filling these very high-dimensional spaces with indexed information from their training data <a class="yt-timestamp" data-t="56:54:00">[56:54:00]</a>. Each [[transformerbased_model_architectures | Transformer layer]] guides tokens through this space to retrieve and integrate relevant information, refining their meaning over time <a class="yt-timestamp" data-t="57:05:00">[57:05:00]</a>.

This perspective suggests that both MLPs and attention mechanisms are fundamentally exploiting this property of high-dimensional spaces to store and retrieve information <a class="yt-timestamp" data-t="55:14:00">[55:14:00]</a>. Attention's power may lie in its ability to encode information as "questions" (queries) and "answers" (keys), allowing for more nuanced and dynamic retrieval <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>.

## Related Concepts

*   **Randomized Autoregressive Visual Generation**: This paper by ByteDance explores permuting the order of input sequences (e.g., image patches) during autoregressive training <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>. Since attention is order-invariant (positional embeddings are used to encode order), changing the scan order for images, which have redundant low-level information, can still lead to effective learning. This further reinforces the idea that what matters is the vector's direction in space, not necessarily the specific sequence of calculations to get there <a class="yt-timestamp" data-t="01:10:47">[01:10:47]</a>.
*   **Differential Transformer**: This architecture modifies the attention mechanism by taking the difference between two separate softmax attention maps <a class="yt-timestamp" data-t="01:19:04">[01:19:04]</a>. This subtraction aims to cancel noise and promote a sparser attention pattern, focusing on the most dominant relationships between tokens <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>.

## Limitations and Future Directions

While TokenFormer demonstrates promising results, its experiments are primarily conducted on "small toy models" <a class="yt-timestamp" data-t="01:36:37">[01:36:37]</a>. The assumption that these findings will hold at larger scales, though common in deep learning research, remains an empirical validation <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

The concept of [[layerwise_scaling_in_transformer_architectures | scaling]] model parameters as tokens could eventually face bottlenecks due to the computational complexity of attention mechanisms with very long sequences <a class="yt-timestamp" data-t="01:01:02">[01:01:02]</a>.

Regarding hallucinations, this architecture does not inherently solve the problem. Hallucinations arise when models interpolate in high-dimensional spaces, generating statements that don't correspond to real information in the training data <a class="yt-timestamp" data-t="01:12:51">[01:12:51]</a>. Future work might explore using variance or entropy in predictions to indicate the model's certainty, distinguishing between known facts and potentially hallucinated outputs <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>.

## Conclusion

TokenFormer represents a significant step in understanding [[implications_of_ai_model_scaling_and_convergence | AI model scaling and convergence]]. By demonstrating that attention mechanisms can replace all linear projections, including those in MLPs, it challenges long-held assumptions about the distinct roles of different components within [[transformerbased_model_architectures | Transformer architectures]] <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>. The ability to progressively scale models by adding parameter tokens offers a more efficient training paradigm, saving compute and time. Ultimately, TokenFormer highlights the profound capacity of high-dimensional spaces and dynamic attention mechanisms to store and retrieve vast amounts of information, driving the intelligence of modern LLMs <a class="yt-timestamp" data-t="01:31:52">[01:31:52]</a>.