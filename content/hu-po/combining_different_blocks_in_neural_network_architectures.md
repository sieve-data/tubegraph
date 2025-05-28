---
title: Combining different blocks in neural network architectures
videoId: udIEwt0xM6A
---

From: [[hu-po]] <br/> 

Neural network architecture design is evolving, with a growing trend towards combining different types of computational blocks within a single model. This approach aims to leverage the strengths of various architectures, potentially leading to more versatile and efficient models.

## X-LSTM: A Modern Take on Recurrent Networks

X-LSTM, or Extended Long Short-Term Memory, is a recently introduced alternative architecture designed to reinvigorate the relevance of Long Short-Term Memory (LSTM) networks in the era of large language models (LLMs) <a class="yt-timestamp" data-t="02:35:10">[02:35:10]</a>. Developed by Sep Hochreiter, the original author of the LSTM, and a group in Austria, the paper was released on May 7, 2024 <a class="yt-timestamp" data-t="03:08:12">[03:08:12]</a>.

### The Original LSTM: Strengths and Limitations
LSTMs, introduced in the 1990s, have been pivotal in numerous deep learning successes <a class="yt-timestamp" data-t="03:50:50">[03:50:50]</a>. They constituted the first large language models, though these early LLMs were "kind of trash" compared to modern Transformers <a class="yt-timestamp" data-t="04:39:56">[04:39:56]</a>.

LSTMs are **recurrent architectures**, meaning they perform computations and pass information forward, operating on their own output recurrently <a class="yt-timestamp" data-t="09:01:21">[09:01:21]</a>. This recurrent nature makes them highly effective for time-based problems and sequential data, such as those found in:
*   AlphaStar model for StarCraft 2 <a class="yt-timestamp" data-t="08:29:43">[08:29:43]</a>
*   OpenAI Five model for DOTA 2 <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>
*   Magnetic controller for the Tokamak reactor <a class="yt-timestamp" data-t="08:35:05">[08:35:05]</a>

The core of an LSTM block involves a "constant error carousel" (cell state update `C of T`) and "gating" mechanisms (input, forget, and output gates) <a class="yt-timestamp" data-t="03:50:50">[03:50:50]</a>. The forget gate removes information, and the input gate adds information to the cell state as it's passed forward <a class="yt-timestamp" data-t="03:30:17">[03:30:17]</a>.

> [!INFO] Vanishing/Exploding Gradients
> The original LSTM structure helps mitigate vanishing gradients, a problem where gradients become extremely small during backpropagation through deep networks, hindering learning <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. Exploding gradients, where gradients become too large, are often handled by clipping their magnitude <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>, <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

However, LSTMs have notable limitations:
*   **Inability to revise storage decisions**: Once information is forgotten or overwritten, it cannot be easily retrieved <a class="yt-timestamp" data-t="03:13:30">[03:13:30]</a>.
*   **Limited storage capacity**: The dimensionality of the information passed between blocks is fixed, leading to information loss over long sequences <a class="yt-timestamp" data-t="03:13:50">[03:13:50]</a>.
*   **Lack of parallelizability**: Due to their recurrent nature, each block's computation depends on the output of the previous block, preventing parallel processing during training <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. This is a key advantage of Transformers, which can calculate attention scores in parallel <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

### X-LSTM Innovations: SL-LSTM and ML-LSTM
X-LSTM introduces two main variants to address the limitations of traditional LSTMs:
1.  **SL-LSTM (Scalar Memory, Scalar Update)**: This variant replaces the sigmoid activation functions in the input and forget gates with exponential functions <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>, <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. To prevent numerical issues like overflow or underflow from the exponential functions, an additional stabilization state (`M of T`) is introduced <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. SL-LSTMs still exhibit memory mixing, prohibiting fully parallelizable operations <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.
2.  **ML-LSTM (Matrix LSTM)**: This is the more significant variant as it enables parallel training. Instead of a scalar or vector `C` for the cell state, ML-LSTM uses a matrix `C` <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. This matrix memory allows for calculating parts of the matrix separately <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. Crucially, the output gate in ML-LSTM is externalized and no longer dependent on the hidden state from the previous time step <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>, unlike the traditional LSTM. This independence enables parallel computation <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

Both SL-LSTM and ML-LSTM incorporate concepts like layer normalization, causal convolutions (for processing time-series data), and gated MLPs (Multi-Layer Perceptrons) with GELU activation functions for up-projection and down-projection of dimensions, influenced by Cover's theorem <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.

### Architectural Composition: Combining Blocks
X-LSTM architectures are built by residually stacking X-LSTM blocks <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. Interestingly, the full X-LSTM model is often composed of an alternating mix of SL-LSTM and ML-LSTM blocks <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. For example, an "X-LSTM 7:1" model means seven out of eight blocks are ML-LSTM, and one is SL-LSTM <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

This approach of combining different types of blocks within a single architecture is not unique to X-LSTM. The [[hybrid_architectures_and_transformer_block_efficiency | Jamba architecture]], for instance, combines [[transformer_architecture_in_image_processing | Transformer blocks]] and [[combining_karpathy_training_code_with_mamba_blocks | Mamba blocks]] <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. This suggests a potential future trend in [[ai_model_architecture_and_parallelism_strategies | AI model architecture and parallelism strategies]], where the best models might be a combination of blocks that leverage different strengths, rather than a single winning architecture <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.

### Performance and Outlook
In comparative tests on the SlimPajama dataset (15 billion tokens), X-LSTM models (up to 1.3 billion parameters) perform favorably against older Transformer models (Llama 1) and older [[memory_optimization in neural networks | Mamba]] versions <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. While their perplexity scores are marginally better than the comparison models, the current CUDA kernels for X-LSTM are still unoptimized and about four times slower than Flash Attention or Mamba's scan mechanism <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

The authors claim that larger X-LSTM models could become serious competitors to current LLMs built with Transformer technology <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. Given their linear computational and constant [[memory_optimization in neural networks | memory optimization in neural networks]] complexity with respect to sequence length, X-LSTMs show significant potential in fields like reinforcement learning, time series prediction, and modeling physical systems <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. The ultimate success of X-LSTM and other alternative architectures will depend on further scaling and optimization of their implementations <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. This highlights the importance of the interplay between theoretical architecture design and efficient low-level software implementation, often requiring a rare blend of expertise <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.