---
title: Exponential gating and memory stabilization in xLSTM
videoId: udIEwt0xM6A
---

From: [[hu-po]] <br/> 

The [[introduction_to_xlstm_architecture | xLSTM]] architecture is a new [[transition_from_transformers_to_recurrent_neural_networks_rnns | recurrent neural network (RNN)]] design, proposed by Sep Hochreiter, the original author of the Long Short-Term Memory (LSTM) network. It aims to modernize LSTMs to compete with contemporary large language models, particularly [[comparison_of_xlstm_with_transformers_and_other_models | Transformers]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Traditional LSTMs, despite their historical success in areas like Starcraft II, DOTA, and Tokamak reactor control due to their recurrent nature for time-series data, faced limitations <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>, <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. These include:
*   Inability to revise storage decisions <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>, <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.
*   Limited storage capacity, as information can be forgotten or overwritten as it passes through recurrent blocks <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>, <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   Lack of [[parallel_training_in_xlstm | parallelizability]] due to memory mixing and the sequential dependency of calculations <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>, <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

xLSTM addresses these limitations through exponential gating and enhanced memory stabilization techniques <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

## Exponential Gating

In traditional LSTMs, input and forget gates utilize sigmoid activation functions <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. These sigmoids restrict output values between 0 and 1 <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>. xLSTM's **SL LSTM (Scalar Memory Scalar Update)** variant introduces exponential gating, replacing the sigmoid activation functions in the input and forget gates with exponential functions <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>, <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. This change allows the model to "revise storage decisions" within its memory cells <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>, conceptually similar to editing an ongoing "sheet of paper" of information <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

## Memory Stabilization

The introduction of exponential activation functions presents a challenge: they can lead to very large or very small values, causing **overflow** or **underflow** issues in computer memory <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>, <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>. To counteract this, xLSTM incorporates a stabilization technique similar to how [[quantization_for_large_language_models | softmax functions]] are stabilized <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>, <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.

This stabilization involves:
*   Introducing an additional state, M of T, which is essentially the maximum of the log values of the forget and input gates from the current and previous steps <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>, <a class="yt-timestamp" data-t="00:38:22">[00:38:22]</a>.
*   Subtracting this maximum value from the exponent before computation (e.g., `x_i - Max(all x_k)`), ensuring the exponential input remains within a manageable range and prevents numerical instability <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>, <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>.

This process is distinct from, but related to, the [[memory_optimization_in_neural_networks | vanishing and exploding gradients]] problem, which refers to the behavior of gradients during backpropagation that can slow down or destabilize training <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>. The stabilization in xLSTM primarily addresses the computational limits of numerical representation.

## Impact on xLSTM Variants

The two main variants of xLSTM are:
*   **SL LSTM**: Incorporates exponential gating and stabilization but still exhibits memory mixing, making it non-[[parallel_training_in_xlstm | parallelizable]] during training <a class="yt-timestamp" data-t="01:39:53">[01:39:53]</a>, <a class="yt-timestamp" data-t="01:42:49">[01:42:49]</a>.
*   **ML LSTM (Matrix Memory Matrix Update)**: To achieve [[parallel_training_in_xlstm | parallel training]], the ML LSTM enhances storage capacity by transforming the cell state (C) from a vector into a matrix <a class="yt-timestamp" data-t="00:44:15">[00:44:15]</a>. Crucially, the ML LSTM removes the memory mixing found in traditional LSTMs by making its output gate (`o_T`) independent of the previous hidden state (`h_T-1`) <a class="yt-timestamp" data-t="01:16:04">[01:16:04]</a>, <a class="yt-timestamp" data-t="01:43:34">[01:43:34]</a>. This structural change allows for the parallel computation of different parts of the matrix, enabling efficient scaling on GPUs <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>, <a class="yt-timestamp" data-t="01:43:50">[01:43:50]</a>.

xLSTM models typically combine both SL LSTM and ML LSTM blocks in their architectures, similar to how [[lcmlaura_accelerating_stable_diffusion_models | Jamba]] models mix [[Attention mechanism and its role in neural networks | Transformer]] and Mamba blocks <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>, <a class="yt-timestamp" data-t="01:20:05">[01:20:05]</a>. This hybrid approach leverages the strengths of both recurrent and parallelizable components.

Despite these advancements, practical implementation challenges remain. While the ML LSTM is theoretically faster due to parallelization, the current [[memory_optimization_in_neural_networks | Cuda kernels]] for xLSTM are not yet optimized, making them slower than highly optimized [[Attention mechanism and its role in neural networks | Transformer]] implementations like Flash Attention <a class="yt-timestamp" data-t="01:06:57">[01:06:57]</a>, <a class="yt-timestamp" data-t="01:34:50">[01:34:50]</a>. The ultimate success of xLSTM against [[comparison_of_xlstm_with_transformers_and_other_models | Transformers]] and other models will depend not only on its theoretical soundness but also on further engineering efforts to optimize its computational performance <a class="yt-timestamp" data-t="01:38:12">[01:38:12]</a>, <a class="yt-timestamp" data-t="01:46:15">[01:46:15]</a>.