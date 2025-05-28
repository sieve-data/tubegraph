---
title: Comparison of xLSTM with Transformers and other models
videoId: udIEwt0xM6A
---

From: [[hu-po]] <br/> 

The xLSTM (extended Long Short-Term Memory) is a new alternative architecture in deep learning, with its paper released on May 7, 2024 <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The "LSTM" in xLSTM stands for Long Short-Term Memory, and the "X" denotes "extended" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. This work originates from a group in Austria, spearheaded by Sepp Hochreiter, who was the original author of the LSTM architecture <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Hochreiter's motivation was to re-establish LSTMs' relevance, given the dominant attention received by [[challenges_and_insights_in_transformer_architecture_and_training | Transformer architectures]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Historical Context: LSTM vs. Transformer

[[transition_from_transformers_to_recurrent_neural_networks_rnns | LSTMs]], introduced in the 1990s with their core ideas of a constant error carousel and gating, have historically been crucial to numerous deep learning successes <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. The original LSTM paper dates back to 1991, followed by a Schmidhuber paper in 1997, demonstrating Hochreiter's three decades of work in [[transition_from_transformers_to_recurrent_neural_networks_rnns | recurrent architectures]] <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. LSTMs were notably the foundation for the first large language models (LLMs) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. However, these early LSTM-based LLMs were considered "kind of trash" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

The landscape shifted significantly with the advent of [[challenges_and_insights_in_transformer_architecture_and_training | Transformer technology]], particularly with its parallelizable self-attention mechanism, which led to the rise of models like ChatGPT (where 'T' stands for Transformer) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. [[challenges_and_insights_in_transformer_architecture_and_training | Transformers]] quickly outpaced LSTMs at scale <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a> due to their ability to train components in parallel, leveraging "Big Data, Big Training, Big Model" [[layerwise_scaling_in_transformer_architectures | scaling laws]] <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### Limitations of Traditional LSTMs

While LSTMs excelled in time-based problems and sequential data processing, chosen for applications like AlphaStar (StarCraft 2) and OpenAI Five (Dota 2) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>, their recurrent nature presented key limitations:
*   **Inability to revise storage decisions** <a class="yt-timestamp" data-t="01:10:41">[01:10:41]</a>
*   **Limited storage capacity** <a class="yt-timestamp" data-t="01:10:41">[01:10:41]</a>
*   **Lack of parallelizability** due to memory mixing <a class="yt-timestamp" data-t="01:10:41">[01:10:41]</a>: Traditional LSTMs require sequential calculation, as each block depends on the output of the previous one <a class="yt-timestamp" data-t="01:13:40">[01:13:40]</a>. This dependency prevents concurrent processing, hindering scalability <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>.

## [[introduction_to_xlstm_architecture | xLSTM Architecture]]: Key Innovations

xLSTM introduces two main variants to address traditional LSTM limitations:
1.  **SLSTM (Scalar memory, Scalar update)**: Similar to the original LSTM but with key modifications <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
2.  **MLSTM (Matrix memory, Matrix update)**: Designed specifically for [[parallel_training_in_xlstm | parallel training]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### [[exponential_gating_and_memory_stabilization_in_xlstm | Exponential Gating and Memory Stabilization]]

A primary innovation in xLSTM, applicable to both SLSTM and MLSTM, is the replacement of sigmoid activation functions in the input and forget gates with exponential gates <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. This change allows for "revising storage decisions" <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

However, exponential activation functions can lead to large values causing overflow or underflow issues in computation <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>. To counter this, xLSTM incorporates an additional "stabilizer state" ($M_t$) <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>, which uses a normalization trick similar to softmax, subtracting the maximum value of the input to prevent numerical instability <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>.

### Matrix Memory and Parallelization

The MLSTM variant significantly enhances storage capacity by increasing the LSTM memory cell from a scalar (or vector) $C$ to a matrix $C$ <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a>. This concept draws from Transformer terminology, introducing "Keys" ($K_t$) and "Values" ($V_t$) to store information, which can later be retrieved by a "Query" ($Q_t$) vector <a class="yt-timestamp" data-t="00:44:57">[00:44:57]</a>.

The crucial aspect of MLSTM is its ability to perform [[parallel_training_in_xlstm | parallel training]] <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. Unlike traditional LSTMs or SLSTMs, MLSTM has no memory mixing in its recurrent path <a class="yt-timestamp" data-t="00:48:13">[00:48:13]</a>. Specifically, its output gate ($O_t$) is externalized and only dependent on the current input ($X_t$), not the previous hidden state ($H_{t-1}$) <a class="yt-timestamp" data-t="01:15:13">[01:15:13]</a>. This architectural choice removes the sequential dependency, allowing computations to be performed simultaneously <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>. This parallelization capability is what allows models to scale effectively, similar to the [[challenges_and_insights_in_transformer_architecture_and_training | Transformer's]] self-attention <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>.

### Architectural Design and Stacking

xLSTM models are constructed by [[layerwise_scaling_in_transformer_architectures | residually stacking]] xLSTM blocks <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This stacking is analogous to [[layerwise_scaling_in_transformer_architectures | Transformer blocks]], with residual connections allowing gradients to flow around blocks <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

Two main block designs exist:
1.  **Post-up Projection**: The up-projection (increasing dimensionality) and down-projection (reducing dimensionality) happen *after* the xLSTM block <a class="yt-timestamp" data-t="00:56:46">[00:56:46]</a>. This design is primarily used for SLSTM <a class="yt-timestamp" data-t="00:58:47">[00:58:47]</a>.
2.  **Pre-up Projection**: The up-projection occurs *before* the xLSTM block, and down-projection after <a class="yt-timestamp" data-t="00:56:57">[00:56:57]</a>. This design is leveraged for MLSTM <a class="yt-timestamp" data-t="00:58:52">[00:58:52]</a>. The concept of projecting into a higher-dimensional space can make patterns more linearly separable, as per Cover's Theorem <a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>.

Both block types incorporate:
*   **Pre-layer normalization**: Standard practice in [[challenges_and_insights_in_transformer_architecture_and_training | Transformers]] <a class="yt-timestamp" data-t="00:59:11">[00:59:11]</a>.
*   **Causal convolutions**: Applied to the input, these are temporal convolutions that only consider past information, suitable for time series data <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>.
*   **Block diagonal linear layers**: Used for gates, effectively limiting connectivity to specific "heads" within a block, similar to multiple heads in [[challenges_and_insights_in_transformer_architecture_and_training | Transformers]] <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>.
*   **Group Normalization**: Equivalent to head-wise layer normalization <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>.
*   **Gated MLP with GELU/Swish activation**: Used for up-projection and down-projection <a class="yt-timestamp" data-t="01:02:49">[01:02:49]</a>.

## [[comparison_with_other_selfsupervised_and_supervised_models | Performance Comparison and Scaling]]

Experiments on SlimPajama (15 billion tokens, a relatively small dataset) <a class="yt-timestamp" data-t="01:24:34">[01:24:34]</a> compare xLSTM (up to 1.3 billion parameters) against [[challenges_and_insights_in_transformer_architecture_and_training | Transformer-based]] Llama 1 and [[comparison_of_rwkv_with_transformer_architectures | RWKV]] (a recurrent model similar to Mamba) <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. xLSTM shows slightly better perplexity scores compared to Llama 1 and older [[comparison_of_rwkv_with_transformer_architectures | State Space Models (SSMs)]] <a class="yt-timestamp" data-t="01:27:51">[01:27:51]</a>. The paper claims xLSTMs perform "favorably" compared to state-of-the-art [[challenges_and_insights_in_transformer_architecture_and_training | Transformers]] and SSMs <a class="yt-timestamp" data-t="01:28:19">[01:28:19]</a>, but this is based on small models and older [[comparison_with_other_selfsupervised and supervised models | comparison models]] <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>.

### Associative Recall
In tasks like associative recall (similar to "needle in a haystack"), [[challenges_and_insights_in_transformer_architecture_and_training | Transformers]] (e.g., Llama) maintain perfect recall across their context length due to their quadratic memory complexity <a class="yt-timestamp" data-t="01:28:57">[01:28:57]</a>. Recurrent models like [[comparison_of_rwkv_with_transformer_architectures | Mamba]], [[comparison_of_rwkv_with_transformer_architectures | RWKV]], and xLSTM, while offering linear computational complexity, tend to be "forgetful" at smaller scales because they attempt to compress information into a fixed-size hidden state <a class="yt-timestamp" data-t="01:29:32">[01:29:32]</a>.

## Limitations and Future Directions

A significant limitation for xLSTM's immediate adoption is the lack of optimized CUDA kernels <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>. The current implementations are about four times slower than optimized solutions like FlashAttention for [[challenges_and_insights_in_transformer_architecture_and_training | Transformers]] or the scan used in [[comparison_of_rwkv_with_transformer_architectures | Mamba]] <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>. This highlights a common gap between theoretical model design and efficient hardware implementation. While xLSTM demonstrates potential at small scales, its performance at very large scales (e.g., 70 billion parameters) and its real-world applicability are yet to be fully proven <a class="yt-timestamp" data-t="01:34:23">[01:34:23]</a>.

Despite these current limitations, xLSTM's linear computation and constant memory complexity with respect to sequence length make it highly promising for fields like reinforcement learning, time series prediction, and modeling physical systems, where historical information needs to be accounted for efficiently <a class="yt-timestamp" data-t="01:36:45">[01:36:45]</a>.

## Hybrid Architectures

An interesting insight from this work is the idea of combining different block types within a single model <a class="yt-timestamp" data-t="01:19:52">[01:19:52]</a>. The xLSTM models evaluated were composed of alternating SLSTM and MLSTM blocks (e.g., xLSTM 7:1 has 7 MLSTM blocks and 1 SLSTM block) <a class="yt-timestamp" data-t="01:19:07">[01:19:07]</a>. This approach is reminiscent of the "Jamba" architecture, which combines [[challenges and insights in Transformer architecture and training | Transformer]] and [[comparison_of_rwkv_with_transformer_architectures | Mamba]] blocks <a class="yt-timestamp" data-t="01:20:05">[01:20:05]</a>. This trend suggests that future optimal model architectures might not rely solely on one type of block but rather on strategic combinations of blocks with different strengths <a class="yt-timestamp" data-t="01:21:04">[01:21:04]</a>.