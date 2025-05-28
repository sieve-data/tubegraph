---
title: State space models vs attentionbased models
videoId: rzXjKcqkjxM
---

From: [[hu-po]] <br/> 

Machine learning architectures for processing sequential data, such as text, video, or motion, typically fall into two main categories: State Space Models (SSMs) and attention-based models (like Transformers). While both aim to understand and generate sequences, they differ fundamentally in their approach to handling information and computational efficiency <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## State Space Models (SSMs)

State Space Models, including modern variants like [[introduction_to_selective_state_space_models_and_mambas | Mamba]], are conceptualized based on a continuous system that maps a one-dimensional function or sequence through a hidden state `H` <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>. This hidden state acts as a compressed representation of all previously processed information in the sequence <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.

### Working Principle
Traditionally, SSMs (like Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTMs)) process data sequentially: to compute the next hidden state, the previous state must first be computed <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. This makes them inherently sequential processes <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

### Discretization
Since real-world data like video frames or motion keyframes are discrete, the continuous ordinary differential equations (ODEs) that define SSMs are approximated through a process called discretization <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>. This typically involves methods like the zero-order hold, which turns a continuous function into a piecewise constant signal by sampling values at discrete points in time <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>. The parameters of an [[introduction_to_selective_state_space_models_and_mambas | Mamba]] model are found within its core matrices (A, B, C) <a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>.

### Advantages of Modern SSMs (Mamba)
*   **Efficiency:** [[introduction_to_selective_state_space_models_and_mambas | Mamba]] models offer linear complexity with respect to input sequence length <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This means their memory and compute requirements scale linearly, making them highly efficient for very long sequences compared to Transformers <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
*   **Parallel Training:** Unlike older RNNs, modern [[introduction_to_selective_state_space_models_and_mambas | Mamba]] models can be trained in parallel, significantly improving training speed and making them competitive with Transformers <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Specific Task Performance:** [[introduction_to_selective_state_space_models_and_mambas | Mamba]] models are particularly advantageous in tasks involving very long sequences, such as [[state_space_models_in_vision | video understanding]] or motion generation <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

### Disadvantage of SSMs
*   **Inductive Bias:** SSMs compress all past information into a single hidden state, which can lead to forgetting less important details from earlier in the sequence <a class="yt-timestamp" data-t="02:00:10">[02:00:10]</a>.

### Scanning Strategies
When applying SSMs to complex data modalities like video or motion, the "scanning" strategy defines how the model processes the sequence <a class="yt-timestamp" data-t="00:51:32">[00:51:32]</a>.
*   **Bidirectional Scanning:** Involves scanning the sequence in both forward and reverse directions (e.g., from first to last frame, and last to first frame) <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>. This helps to reduce the likelihood of forgetting information <a class="yt-timestamp" data-t="01:56:27">[01:56:27]</a>.
*   **Spatial-First vs. Temporal-First:** For video, this determines whether the model scans an entire frame before moving to the next (spatial-first) or processes a specific patch across all frames first (temporal-first) <a class="yt-timestamp" data-t="00:51:54">[00:51:54]</a>. Spatial-first bidirectional scanning has shown to be effective in [[state_space_models_in_vision | video understanding]] <a class="yt-timestamp" data-t="00:59:12">[00:59:12]</a>.
*   **Hierarchical Scanning:** In models like Motion [[introduction_to_selective_state_space_models_and_mambas | Mamba]], the number of scans can change depending on the level of abstraction in the model's hierarchy <a class="yt-timestamp" data-t="00:53:53">[00:53:53]</a>. Lower levels dealing with fine-grained details might undergo more scans than higher levels dealing with abstract concepts <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.

## Attention-Based Models (Transformers)

Transformers revolutionized sequential data processing by introducing the attention mechanism. Instead of relying on a compressed hidden state, Transformers save all past representations of the sequence and then "attend" to them <a class="yt-timestamp" data-t="00:27:25">[00:27:25]</a>.

### Working Principle
Transformers process information in parallel <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. They compute all possible interactions between different parts of the sequence simultaneously, creating an attention map that determines the relationships between tokens <a class="yt-timestamp" data-t="00:28:15">[00:28:15]</a>.

### Advantages of Transformers
*   **Power and Versatility:** Transformers are very powerful and can easily adapt to a wide range of problems due to their flexible attention mechanism <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Global Dependencies:** They excel at capturing long-range dependencies across sequences, as every part of the sequence can directly interact with every other part <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This means information from far apart points in the sequence can be equally important <a class="yt-timestamp" data-t="01:54:41">[01:54:41]</a>.

### Disadvantages of Transformers
*   **Computational Cost:** The attention mechanism leads to quadratic scaling of computational requirements with respect to the input sequence length <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This means that for very long sequences or high-resolution data, Transformers become extremely memory and compute intensive <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Memory Intensity:** The creation of a square attention map leads to substantial increases in memory usage <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## The Competition: When to Choose Which?

The choice between SSMs and attention-based models often boils down to the nature of the data and available computational resources:

*   **Long Sequences:** For tasks involving very long sequences (e.g., high-resolution videos, detailed motion sequences), [[introduction_to_selective_state_space_models_and_mambas | Mamba]] models offer a significant advantage due to their linear complexity and lower GPU consumption <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This is critical as data dimensionality continues to increase (e.g., 4K video, more detailed skeletons for motion) <a class="yt-timestamp" data-t="01:32:38">[01:32:38]</a>.
*   **GPU Advancement:** The future success of [[introduction_to_selective_state_space_models_and_mambas | Mamba]] models relative to Transformers depends on how quickly GPU performance advances <a class="yt-timestamp" data-t="01:31:08">[01:31:08]</a>. If GPUs continue to achieve massive performance gains, the quadratic scaling of Transformers might become less of a bottleneck, allowing them to remain dominant due to their inductive bias <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>. However, if GPU improvements slow down, [[introduction_to_selective_state_space_models_and_mambas | Mamba]] models will become increasingly essential to handle growing data sizes <a class="yt-timestamp" data-t="01:31:50">[01:31:50]</a>.

## Conclusion

Both State Space Models and attention-based models represent powerful approaches to sequential data processing. While Transformers excel at global understanding through parallel attention, they face challenges with computational and memory scaling for very long sequences. [[introduction_to_selective_state_space_models_and_mambas | Mamba]], as a modern SSM, addresses these scaling issues with linear complexity and parallel training capabilities, making it a strong candidate for future applications dealing with ever-increasing data dimensionality. The ongoing "arms race" between model architectures and hardware advancements will continue to shape the optimal choice for different AI tasks.