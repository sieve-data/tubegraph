---
title: Introduction to xLSTM architecture
videoId: udIEwt0xM6A
---

From: [[hu-po]] <br/> 

The xLSTM (Extended Long Short-Term Memory) is a new architecture introduced in a paper published on May 7, 2024 <a class="yt-timestamp" data-t="03:12">[03:12]</a>. It is an evolution of the traditional Long Short-Term Memory (LSTM) network. The primary author, Sep Hochreiter, is also the original author of the LSTM <a class="yt-timestamp" data-t="03:28">[03:28]</a>. The development of xLSTM aims to re-establish LSTMs as a relevant and scalable alternative in the landscape of modern deep learning architectures, particularly challenging the dominance of [[Large Language Models and their applications | Transformers]] <a class="yt-timestamp" data-t="03:38">[03:38]</a>.

## Historical Context: The Original LSTM

The LSTM architecture emerged in the 1990s <a class="yt-timestamp" data-t="03:50">[03:50]</a>, with foundational papers appearing in 1991 and 1997 <a class="yt-timestamp" data-t="04:09">[04:09]</a>. LSTMs introduced core ideas like the "constant error carousel" and "gating" mechanisms <a class="yt-timestamp" data-t="03:54">[03:54]</a>.

### Key Characteristics and Successes
LSTMs are a type of [[Transition from Transformers to recurrent neural networks RNNs | recurrent neural network]] (RNN) <a class="yt-timestamp" data-t="09:01">[09:01]</a>. They process information sequentially, where the computation at a given time step relies on information passed forward from the previous time step <a class="yt-timestamp" data-t="09:12">[09:12]</a>. This recurrent nature makes them particularly well-suited for modeling time-series data <a class="yt-timestamp" data-t="10:39">[10:39]</a>.

LSTMs have been central to numerous deep learning successes:
*   **AlphaStar (StarCraft 2)** <a class="yt-timestamp" data-t="08:29">[08:29]</a>
*   **OpenAI Five (DOTA)** <a class="yt-timestamp" data-t="08:32">[08:32]</a>
*   **Magnetic controller for the Tokamak reactor (DeepMind)** <a class="yt-timestamp" data-t="08:35">[08:35]</a>

They also constituted the first [[Large Language Models and their applications | Large Language Models]] (LLMs), though these early LSTM-based LLMs were not as performant as modern [[Large Language Models and their applications | Transformer]]-based models like ChatGPT <a class="yt-timestamp" data-t="04:36">[04:36]</a>.

### Core Components of LSTM
The original LSTM's architecture involves several gates and a cell state (C_t):
*   **Cell State (Constant Error Carousel):** C_t carries information across time steps <a class="yt-timestamp" data-t="15:18">[15:18]</a>.
*   **Forget Gate (F_t):** Controls what information from the previous cell state (C_{t-1}) should be "forgotten" or erased <a class="yt-timestamp" data-t="15:56">[15:56]</a>.
*   **Input Gate (I_t):** Determines what new information from the current input (X_t) should be "added" to the cell state <a class="yt-timestamp" data-t="16:47">[16:47]</a>.
*   **Output Gate (O_t):** Controls what part of the cell state is exposed as the hidden state (H_t) <a class="yt-timestamp" data-t="21:30">[21:30]</a>.
*   **Activation Functions:** Typically sigmoid (for gates, outputs 0-1) and tanh (for cell input, outputs -1 to 1) <a class="yt-timestamp" data-t="18:00">[18:00]</a>.

All components of the memory cell in an LSTM are crucial for its operation <a class="yt-timestamp" data-t="20:33">[20:33]</a>.

### Limitations of Original LSTMs
Despite their strengths, traditional LSTMs faced limitations:
*   **Inability to revise storage decisions:** Once information is "forgotten" or "overwritten" in the cell state, it's lost <a class="yt-timestamp" data-t="12:18">[12:18]</a>.
*   **Limited storage capacity:** The cell state is a fixed-length vector, which limits the amount of historical information that can be retained over very long sequences <a class="yt-timestamp" data-t="12:49">[12:49]</a>.
*   **Lack of [[parallel_training_in_xlstm | parallelizability]]**: Due to their recurrent nature, computation at each time step depends on the output of the previous step. This sequential dependency prevents parallel computation, which is critical for scaling [[Large Language Models and their applications | Large Language Models]] on modern hardware like GPUs <a class="yt-timestamp" data-t="13:42">[13:42]</a>. This is in contrast to [[Large Language Models and their applications | Transformers]], which benefit from parallel self-attention <a class="yt-timestamp" data-t="05:09">[05:09]</a>.

## Innovations in xLSTM

xLSTM addresses the limitations of traditional LSTMs through two main innovations: [[exponential_gating_and_memory_stabilization_in_xlstm | Exponential Gating]] and a modified memory structure.

### 1. [[exponential_gating_and_memory_stabilization_in_xlstm | Exponential Gating]]
To enable the ability to revise storage decisions, xLSTM replaces the sigmoid activation functions in the input and forget gates with exponential activation functions <a class="yt-timestamp" data-t="26:00">[26:00]</a>.
*   **Challenge:** Exponential functions can lead to very large or very small values, causing numerical overflow or underflow when represented on computer hardware (e.g., float16, bfloat16 data types) <a class="yt-timestamp" data-t="29:49">[29:49]</a>.
*   **Stabilization:** To mitigate this, xLSTM introduces an additional state (M_t) for stabilization. This is analogous to how softmax normalization is used to prevent numerical instability with exponentials <a class="yt-timestamp" data-t="30:00">[30:00]</a>. This M_t subtracts the maximum value of the input, ensuring numbers remain within a representable range <a class="yt-timestamp" data-t="35:11">[35:11]</a>.

### 2. Modified Memory Structure (M-LSTM)
To enhance storage capacity and enable [[parallel_training_in_xlstm | parallel training]], xLSTM introduces two variants: SL-LSTM and M-LSTM.

*   **SL-LSTM (Scalar-memory Scalar-update LSTM):**
    *   This variant primarily incorporates [[exponential_gating_and_memory_stabilization_in_xlstm | exponential gating]] and normalization/stabilization techniques <a class="yt-timestamp" data-t="38:53">[38:53]</a>.
    *   It retains the memory mixing via recurrent connections from the hidden state (H_{t-1}) to the memory cell input <a class="yt-timestamp" data-t="39:27">[39:27]</a>.
    *   Due to this memory mixing, SL-LSTM is **not parallelizable** during training, as each computation depends on the previous output <a class="yt-timestamp" data-t="06:29">[06:29]</a>. However, the authors did develop a fast Cuda kernel for it <a class="yt-timestamp" data-t="06:29">[06:29]</a>.

*   **M-LSTM (Matrix-memory LSTM):**
    *   This is the more significant innovation regarding [[parallel_training_in_xlstm | parallelizability]].
    *   It transforms the LSTM memory cell from a scalar/vector (C_t) into a **matrix** (C_t) <a class="yt-timestamp" data-t="44:13">[44:13]</a>. This is somewhat analogous to the KV cache in [[Large Language Models and their applications | Transformers]] <a class="yt-timestamp" data-t="44:57">[44:57]</a>.
    *   The M-LSTM reuses [[Large Language Models and their applications | Transformer]] terminology, calling components Keys (K_t), Values (V_t), and Queries (Q_t) <a class="yt-timestamp" data-t="45:09">[45:09]</a>.
    *   Crucially, M-LSTM eliminates memory mixing in its recurrence <a class="yt-timestamp" data-t="48:18">[48:18]</a>. Specifically, its output gate (O_t) is made **externalized** and depends only on the current input (X_t), rather than the hidden state (H_{t-1}) of the previous block <a class="yt-timestamp" data-t="16:11">[16:11]</a>, <a class="yt-timestamp" data-t="16:22">[16:22]</a>.
    *   This design enables the recurrence to be formulated in a **parallel version** <a class="yt-timestamp" data-t="48:21">[48:21]</a>, allowing for efficient [[parallel_training_in_xlstm | parallel training]] on GPUs.

## xLSTM Architecture Design

xLSTM models are constructed by residually stacking building blocks <a class="yt-timestamp" data-t="06:56">[06:56]</a>. This means that xLSTM blocks (like [[Large Language Models and their applications | Transformer blocks]]) are stacked one on top of the other, with residual connections (or skip connections) allowing gradients to flow around the blocks <a class="yt-timestamp" data-t="07:32">[07:32]</a>.

Two main designs for these blocks are proposed:

1.  **Residual Block with Post-Up Projection (primarily for SL-LSTM):**
    *   Employs a pre-layer normalization and residual structure <a class="yt-timestamp" data-t="59:09">[59:09]</a>.
    *   Input can optionally pass through a causal convolution with a Swish activation function <a class="yt-timestamp" data-t="00:59:09">[59:09]</a>. Causal convolutions are useful for time-series data as they ensure that the output at a given time step only depends on current and past inputs, not future ones <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>.
    *   The cell input, input gate, forget gate, and output gate are fed through a block-diagonal linear layer with four diagonal blocks (or "heads") <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>. This limits connectivity to within each head, promoting local processing <a class="yt-timestamp" data-t="01:10:57">[01:10:57]</a>.
    *   The hidden state then passes through a group normalization layer <a class="yt-timestamp" data-t="01:02:23">[01:02:23]</a>.
    *   The output is *up-projected* to a higher dimension and then *down-projected* back, using a gated MLP with a GELU activation function. This up-projection is motivated by Cover's Theorem, which suggests that patterns may be more linearly separable in higher-dimensional spaces <a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>.

2.  **Residual Block with Pre-Up Projection (primarily for M-LSTM):**
    *   Also uses a pre-layer norm residual structure <a class="yt-timestamp" data-t="01:12:56">[01:12:56]</a>.
    *   The input is *up-projected first* (e.g., by a factor of two) before being fed into the M-LSTM cell <a class="yt-timestamp" data-t="01:13:06">[01:13:06]</a>.
    *   It features an "externalized output gate" which is separate from the main cell calculation and only depends on the input, enabling [[parallel_training_in_xlstm | parallelization]] <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.
    *   The M-LSTM cell input is dimension-wise causally convolved with a Swish activation <a class="yt-timestamp" data-t="01:13:36">[01:13:36]</a>.
    *   Queries (Q) and Keys (K) are obtained via block-diagonal projection matrices <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. Values (V) skip the convolution part and are fed directly <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>.
    *   After sequence mixing, outputs are normalized via group normalization <a class="yt-timestamp" data-t="01:17:35">[01:17:35]</a>.
    *   A learnable skip input is added, and the result is combined with the external output gate, followed by a down-projection <a class="yt-timestamp" data-t="01:17:56">[01:17:56]</a>.

### Hybrid Models
Notably, a full xLSTM model is often composed of a mix of SL-LSTM blocks and M-LSTM blocks <a class="yt-timestamp" data-t="01:19:08">[01:19:08]</a>. For example, an "xLSTM 7:1" means that out of eight blocks, seven are M-LSTM and one is SL-LSTM <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>. This approach of combining different architectural blocks (like in the Jamba model which combines [[Large Language Models and their applications | Transformer]] and Mamba blocks) suggests a potential future where optimal models are hybrids, leveraging the strengths of different recurrent and parallel architectures <a class="yt-timestamp" data-t="01:20:02">[01:20:02]</a>.

## [[Comparison of xLSTM with Transformers and other models | Performance and Comparison]]

The paper presents [[Comparison of xLSTM with Transformers and other models | experiments]] comparing xLSTM to [[Large Language Models and their applications | Transformers]] (specifically Llama 1) and State Space Models (like Mamba and RWKV) on a dataset of 15 billion tokens (SlimPajama) <a class="yt-timestamp" data-t="01:24:34">[01:24:34]</a>. The largest model trained was 1.3 billion parameters <a class="yt-timestamp" data-t="01:25:02">[01:25:02]</a>.

### Key Findings:
*   **Perplexity:** xLSTM models showed favorably, often slightly better perplexity scores than Llama 1 and older Mamba/RWKV models of comparable size <a class="yt-timestamp" data-t="01:27:01">[01:27:01]</a>.
*   **Memory Capacity (Associative Recall):**
    *   [[Large Language Models and their applications | Transformers]] (e.g., Llama) generally maintain perfect recall due to their quadratic complexity with respect to sequence length, effectively "storing" all information <a class="yt-timestamp" data-t="01:28:57">[01:28:57]</a>.
    *   Recurrent models like Mamba, RWKV, and xLSTM, while having linear complexity (and thus being more memory efficient), can be "forgetful" due to their fixed-size hidden state limiting information retention over very long contexts <a class="yt-timestamp" data-t="01:29:32">[01:29:32]</a>. Larger xLSTM models, however, perform better at associative recall than smaller ones <a class="yt-timestamp" data-t="01:30:13">[01:30:13]</a>.
*   **Ablation Studies:** Confirmed that both [[exponential_gating_and_memory_stabilization_in_xlstm | exponential gating]] and the matrix memory contribute significantly to xLSTM's improved performance over traditional LSTMs <a class="yt-timestamp" data-t="01:30:49">[01:30:49]</a>.
*   **Computational Efficiency:** While M-LSTM is [[parallel_training_in_xlstm | parallelizable]] in theory, the current Cuda kernels for xLSTM are not optimized and are about four times slower than highly optimized implementations like FlashAttention used in [[Large Language Models and their applications | Transformers]] <a class="yt-timestamp" data-t="01:07:03">[01:07:03]</a>. This highlights the gap between theoretical architectural advancements and practical engineering implementations <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>.

### Future Potential:
The authors suggest that [[Large Language Models and their applications | scaling laws]] indicate larger xLSTM models could become serious competitors to current LLMs built with [[Large Language Models and their applications | Transformer]] technology <a class="yt-timestamp" data-t="01:36:32">[01:36:32]</a>. xLSTM holds significant potential beyond general [[Large Language Models and their applications | Large Language Models]], particularly in fields that benefit from efficient handling of sequential data and long histories, such as:
*   Reinforcement learning <a class="yt-timestamp" data-t="01:36:44">[01:36:44]</a>
*   Time series prediction <a class="yt-timestamp" data-t="01:36:45">[01:36:45]</a>
*   Modeling of physical systems <a class="yt-timestamp" data-t="01:36:46">[01:36:46]</a>
*   Control problems (e.g., robotics, nuclear fusion controllers) <a class="yt-timestamp" data-t="01:37:01">[01:37:01]</a>

The success of xLSTM at scale will depend on further engineering efforts to optimize its computational kernels, similar to how FlashAttention boosted [[Large Language Models and their applications | Transformer]] performance <a class="yt-timestamp" data-t="01:38:08">[01:38:08]</a>.