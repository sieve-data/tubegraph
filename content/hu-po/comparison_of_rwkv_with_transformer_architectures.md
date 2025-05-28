---
title: Comparison of RWKV with Transformer architectures
videoId: ZDHE119dFR8
---

From: [[hu-po]] <br/> 

The RWKV (Receptance Weighted Key Value) model is a novel neural network architecture designed to combine the strengths of [[transition_from_transformers_to_recurrent_neural_networks_rnns | Recurrent Neural Networks (RNNs)]] with the high performance typically associated with [[transformerbased_model_architectures | Transformer-based Large Language Models (LLMs)]] <a class="yt-timestamp" data-t="01:28:20">[01:28:20]</a>. Its core aim is to achieve [[transformerbased_model_architectures | Transformer-level LLM performance]] while maintaining the efficient inference characteristics of RNNs <a class="yt-timestamp" data-t="01:29:33">[01:29:33]</a>.

## Background on Transformers
[[transformerbased_model_architectures | Transformers]] have revolutionized Natural Language Processing (NLP) due to their ability to handle both local and long-range dependencies and their capability for parallelized training <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a> <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. Recent models like GPT-3, ChatGPT, GPT-4, LLaMA, and Chinchilla exemplify the power of [[transformerbased_model_architectures | Transformer architectures]] <a class="yt-timestamp" data-t="01:14:11">[01:14:11]</a>. However, their self-attention mechanism poses significant [[challenges_and_insights_in_transformer_architecture_and_training | challenges]] due to its quadratic computational and memory complexity concerning sequence length <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a> <a class="yt-timestamp" data-t="01:16:15">[01:16:15]</a>. This means that as the sequence length increases, the computational resources required grow exponentially <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>.

## RWKV Architecture and Core Concepts
RWKV introduces a unique architecture that blends elements of both [[transition_from_transformers_to_recurrent_neural_networks_rnns | RNNs]] and [[transformerbased_model_architectures | Transformers]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>. Its name derives from its four primary model elements <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>:
*   **R (Receptance)**: A vector acting as the acceptance of past information, similar to a forget gate in [[transition_from_transformers_to_recurrent_neural_networks_rnns | LSTMs]] <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a> <a class="yt-timestamp" data-t="01:54:50">[01:54:50]</a>.
*   **W (Weight)**: A positional weight decay vector, which is trainable and determines the importance of information further back in time <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.
*   **K (Key)**: A vector analogous to the Key in traditional attention, representing "the things that I have" <a class="yt-timestamp" data-t="00:54:37">[00:54:37]</a>.
*   **V (Value)**: A vector analogous to the Value in traditional attention, representing "the things that I want to communicate" <a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>.

The architecture comprises stacked residual blocks, each formed by a time mixing and a channel mixing sub-block with recurrent architectures <a class="yt-timestamp" data-t="00:56:40">[00:56:40]</a>.

## Key Comparisons

### Computational Complexity
A fundamental difference lies in computational complexity:
*   **Transformers**: Exhibit quadratic (T²) scaling for both time and memory complexity during training due to the dot-product self-attention mechanism <a class="yt-timestamp" data-t="01:16:15">[01:16:15]</a>. This quadratic scaling refers to the sequence length (T) <a class="yt-timestamp" data-t="01:14:11">[01:14:11]</a>.
*   **RWKV**: Achieves linear (T) scaling for time and memory complexity <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This is a significant [[advantages_and_limitations_of_rwkv_in_neural_network_models | advantage]], allowing for much longer sequence processing <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>. The WKV computation, a core part of RWKV, is specifically designed to avoid quadratic cost <a class="yt-timestamp" data-t="01:10:19">[01:10:19]</a>.

### Attention Mechanism
RWKV reformulates the attention mechanism to avoid the quadratic cost:
*   **Transformers**: Use dot-product token interaction (Q * Kᵀ) to calculate attention scores, which is a vector multiplication <a class="yt-timestamp" data-t="01:09:55">[01:09:55]</a>.
*   **RWKV**: Replaces the fixed Query (Q) in attention with a scalar-based time decay factor (W) <a class="yt-timestamp" data-t="01:46:02">[01:46:02]</a> <a class="yt-timestamp" data-t="02:06:42">[02:06:42]</a>. This allows interactions to occur between scalars rather than vectors, enabling parallel computation <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. The WKV operation is central to this, acting as the attention mechanism without the quadratic cost <a class="yt-timestamp" data-t="01:10:11">[01:10:11]</a>.

### Parallelization and Inference
RWKV is designed for efficient training and inference:
*   **Transformers**: Allow for efficient parallel training because they process the entire sequence simultaneously <a class="yt-timestamp" data-t="01:06:09">[01:06:09]</a>. However, during inference (e.g., in a chatbot), they typically require a KV cache that grows linearly with sequence length, leading to degraded efficiency and increased memory footprint for longer sequences <a class="yt-timestamp" data-t="02:05:58">[02:05:58]</a>.
*   **RWKV**: Combines the efficient parallelizable training of [[transformerbased_model_architectures | Transformers]] with the efficient inference of [[transition_from_transformers_to_recurrent_neural_networks_rnns | RNNs]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. It can be trained in "time parallel mode" like [[transformerbased_model_architectures | Transformers]] <a class="yt-timestamp" data-t="01:31:30">[01:31:30]</a>. For inference, it leverages an [[transition_from_transformers_to_recurrent_neural_networks_rnns | RNN-like structure]] ("time sequential mode"), where each output token depends only on the latest state, which is of constant size regardless of sequence length <a class="yt-timestamp" data-t="02:11:31">[02:11:31]</a>. This constant memory footprint for inference is a major [[advantages_and_limitations_of_rwkv_in_neural_network_models | advantage]] over [[transformerbased_model_architectures | Transformers]] <a class="yt-timestamp" data-t="02:11:31">[02:11:31]</a>.

### Gradient Stability and Layer Stacking
RWKV addresses gradient stability more inherently than traditional [[transition_from_transformers_to_recurrent_neural_networks_rnns | RNNs]]:
*   **Traditional RNNs**: Suffer from vanishing gradients due to long dependency paths <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>.
*   **RWKV**: Utilizes softmax in conjunction with [[transition_from_transformers_to_recurrent_neural_networks_rnns | RNN-style updates]] to avoid vanishing/exploding gradients <a class="yt-timestamp" data-t="01:32:46">[01:32:46]</a>. Its gate values are not data-dependent, meaning they don't require recomputing previous hidden states, which contributes to parallelizability and stability <a class="yt-timestamp" data-t="01:33:02">[01:33:02]</a>. Layer normalization further enhances training dynamics <a class="yt-timestamp" data-t="01:35:35">[01:35:35]</a>. These design elements enable the stacking of multiple layers in a manner that surpasses the capabilities of existing [[transition_from_transformers_to_recurrent_neural_networks_rnns | RNNs]] <a class="yt-timestamp" data-t="01:36:41">[01:36:41]</a>.

### Context Handling
*   **Transformers**: Process the entire input sequence simultaneously, allowing them to explicitly consider all previous tokens for the next prediction <a class="yt-timestamp" data-t="02:09:50">[02:09:50]</a>.
*   **RWKV**: Compresses all previous sequence information into a single fixed-size hidden state vector <a class="yt-timestamp" data-t="02:17:17">[02:17:17]</a>. While efficient, this [[advantages_and_limitations_of_rwkv_in_neural_network_models | inherently limits its ability]] to recall "minutiae information over very long contexts" as it represents a "lossy form of compression" <a class="yt-timestamp" data-t="02:09:14">[02:09:14]</a>.

### Prompt Sensitivity
*   **Transformers**: Due to their full attention mechanism, [[transformerbased_model_architectures | Transformer models]] are generally less sensitive to minor variations in prompt wording or structure <a class="yt-timestamp" data-t="01:58:30">[01:58:30]</a>.
*   **RWKV**: Shows increased importance of prompt engineering <a class="yt-timestamp" data-t="02:09:26">[02:09:26]</a>. Its performance can significantly improve (e.g., 30% F1 measure boost) when prompts are adjusted to better suit its [[transition_from_transformers_to_recurrent_neural_networks_rnns | RNN-like processing]], acknowledging it is "not capable for retrospective processing" <a class="yt-timestamp" data-t="01:58:20">[01:58:20]</a> <a class="yt-timestamp" data-t="02:48:48">[02:48:48]</a>. This could be a significant [[advantages_and_limitations_of_rwkv_in_neural_network_models | limitation]] <a class="yt-timestamp" data-t="01:59:42">[01:59:42]</a>.

### Parameter Initialization
RWKV uses unique initialization strategies:
*   **Transformers**: Typically initialize embeddings with small Gaussian-distributed values <a class="yt-timestamp" data-t="02:30:51">[02:30:51]</a>.
*   **RWKV**: Initializes embedding matrices with very small uniform values (e.g., +/- 1e-4) and applies an additional layer normalization, which helps accelerate and stabilize training <a class="yt-timestamp" data-t="02:47:58">[02:47:58]</a>. Most weights are initialized to zero, and no biases are used for linear layers <a class="yt-timestamp" data-t="02:49:20">[02:49:20]</a>.

## Performance and Scaling
Experiments indicate that RWKV performs on par with similarly sized [[transformerbased_model_architectures | Transformers]] <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. It exhibits the same scaling properties as [[transformerbased_model_architectures | Transformers]]; as the model size (number of parameters) increases, its accuracy also improves <a class="yt-timestamp" data-t="02:05:58">[02:05:58]</a>. RWKV has been successfully scaled to tens of billions of parameters, demonstrating its potential for large-scale models <a class="yt-timestamp" data-t="02:11:31">[02:11:31]</a>.

## Advantages and Limitations
RWKV's main [[advantages_and_limitations_of_rwkv_in_neural_network_models | advantages]] include its linear scaling for memory and computation, making it highly efficient, especially during inference <a class="yt-timestamp" data-t="02:05:58">[02:05:58]</a> <a class="yt-timestamp" data-t="02:06:50">[02:06:50]</a>. This allows for processing significantly longer sequences more efficiently than [[transformerbased_model_architectures | Transformers]] <a class="yt-timestamp" data-t="02:05:58">[02:05:58]</a>.

However, its [[advantages_and_limitations_of_rwkv_in_neural_network_models | limitations]] include the potential for information loss over very long contexts due to the continuous compression of information into a single vector representation <a class="yt-timestamp" data-t="02:09:14">[02:09:14]</a>. Additionally, its increased sensitivity to prompt engineering means that carefully designed prompts are crucial for optimal performance <a class="yt-timestamp" data-t="02:09:26">[02:09:26]</a>.

## Future Potential
The development of RWKV represents a significant step towards reconciling the trade-offs between computational efficiency and model performance in sequence modeling <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. Future work includes enhancing its time decay formulations, further improving computational efficiency with advanced Cuda kernel implementations <a class="yt-timestamp" data-t="02:00:58">[02:00:58]</a>, and exploring [[hybrid_architectures_and_transformer_block_efficiency | encoder-decoder architectures]] and cross-attention replacement <a class="yt-timestamp" data-t="02:01:41">[02:01:41]</a>. There's also interest in leveraging RWKV's state or context for [[applications_and_future_potential_of_rwkv_in_ai | interpretability and predictability]], as well as adapting [[application_of_lora_in_transformer_architectures | parameter-efficient fine-tuning]] methods and different quantizations for deployment on [[applications_and_future_potential_of_rwkv_in_ai | edge devices]] <a class="yt-timestamp" data-t="02:05:33">[02:05:33]</a> <a class="yt-timestamp" data-t="02:05:49">[02:05:49]</a>.