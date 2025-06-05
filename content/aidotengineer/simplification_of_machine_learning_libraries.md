---
title: Simplification of Machine Learning Libraries
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

Luminal aims for radical simplification in [[AI models and training methods | machine learning]] (ML) libraries through the use of search-based compilation <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This approach makes Luminal simpler than most other ML libraries without compromising performance or capability <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## The Problem: Complexity in Current ML Libraries
Deep learning, at its core, is simple linear algebra involving scalars, vectors, matrices, and tensors, with a few fundamental operations like additions, multiplies, and matrix multiplications <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, the existing [[AI models and training methods | machine learning]] software ecosystem is highly complex <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

For instance:
*   **PyTorch** features over 1,200 operations, 15 different data types, and supports numerous devices (CPU, CUDA, AMD, TPUs, NPUs) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   The complexity scales multiplicatively, not additively, with the number of operations, data types, and supported devices <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Adding a new operation, data type, or device can lead to an explosion in complexity <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   PyTorch exceeds 3 million lines of code, and TensorFlow is even larger <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   This complexity results in more bugs and makes it difficult for developers to extend, use, or build within these frameworks <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

Older libraries were designed with dynamism at their core (e.g., for RNNs and LSTMs) to allow for hackability and experimentation, often at the expense of performance <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Luminal's Approach to Simplification

Luminal adopts a top-down approach, identifying the minimum required components to run [[AI models and training methods | ML models]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Minimal Operations
Deep learning, as linear algebra, can be broken down into simple operations. Luminal uses a set of just 12 core operations as "Lego blocks" to build complex models <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:
*   **Unary Operations**: `x2`, `log2`, `sin`, `reciprocal`, `square root` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
*   **Binary Operations**: `addition`, `multiplication`, `modulo`, `less than` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   **Reductions**: `sum reduce`, `max reduce` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

With these 12 operations, Luminal can support all commercially relevant models, including language models, vision language models, CNNs, RNNs, and diffusion models <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Many seemingly complex operations are combinations of these primitives:
*   **Subtraction**: `addition` + `multiplication` by -1 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
*   **Division**: `multiplication` + `reciprocal` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>
*   **Matrix Multiplications (Matmuls)**: Broadcasted `multiply` + `sum reduce` (with tensor shape manipulation) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>
*   **Convolution**: Pooling via shape trackers + `matmul` with a convolution kernel <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

### Static Graph Representation
Deep learning itself is not fundamentally dynamic; typical model dynamism is small and bounded, such as the KV cache length and sequence length in a transformer model <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Luminal specifies models as directed acyclic graphs (DAGs) of operations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This allows the entire workload to be specified ahead of time <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

### Resulting Simplicity
As a consequence of these design choices, Luminal is very simple:
*   It is under 5,000 lines of code <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   The goal is for the entire library to be learnable in an afternoon, with core concepts understandable in a couple of hours <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Achieving Performance Through Compilers and Search

While simple, Luminal's primitive graphs of operations are initially slow <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. The core innovation lies in transforming these graphs into much faster ones using compilers, specifically through a search-based approach <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Traditional ML Stack vs. Luminal
A traditional [[AI implementation and best practices | ML stack]] often involves many layers (e.g., Hugging Face Transformers on PyTorch, Xformers, optimized kernels, then calling cuDNN/cuBLAS on CUDA) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This creates complex dependencies, leading to "dependency hell" during installation and making bug tracing difficult <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

Luminal simplifies this by directly emitting CUDA code <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. There is nothing between Luminal's library, graph, and compilers, and CUDA <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### The [[SearchBased Deep Learning Compilers | Search-Based Compiler]] Solution
The complexity of compilers scales exponentially with the complexity of the code they need to generate <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. This has bottlenecked the ecosystem, especially for hardware startups with specialized hardware <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. As hardware becomes simpler and faster (e.g., from CPUs to GPUs to TPUs, which require more explicit programmer control for better performance per watt), the software/compiler needs to become more complex <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

This leads to the VLIW (Very Large Instruction Width) compiler problem: hardware designers want simple hardware, requiring the compiler to statically schedule everything, but compilers for this become too complex for humans to write <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

Luminal solves this by applying the same solution used by AlphaGo for cracking the game of Go: **search** <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Instead of hand-writing perfect algorithms, Luminal searches through logically equivalent GPU kernels <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

#### How Search Works
1.  **Graph to Expressions**: Luminal converts its operation graphs into expressions using the `egg log` library, which represents the search space efficiently using e-graphs <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  **Rewrite Rules**: Luminal defines 20-25 simple rewrite rules <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Each rule makes a small, logically equivalent alteration to a given GPU kernel <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
3.  **Search Space Generation**: By iteratively applying these simple rewrite rules, a very large search space of equivalent kernels is built <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
4.  **Performance Profiling**: Luminal then profiles the runtime of these different equivalent kernels and selects the fastest one <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. For larger search spaces, techniques like Monte Carlo search are used to prune the search <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

#### Optimizations Found Through Search
*   **Kernel Fusion**: This optimization merges multiple operations into a single kernel to minimize data movement to and from global memory, which is typically 99% of the energy and time spent on GPUs <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
    *   An unfused graph involves writing results to memory and reading them back for each sequential operation <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
    *   A fused kernel merges these, drastically reducing data movement and making the entire aggregate graph far faster <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Flash Attention**: Luminal's search technique was able to independently discover Flash Attention, a complex algorithm that took the industry five years to find <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. By running simple rewrite rules on a naive multi-head attention graph and profiling the search space, Luminal identified Flash Attention as the fastest kernel <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This is believed to be unique among compilers <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

## Deterministic Optimizations

After the search process finds the fastest kernels, Luminal applies deterministic optimizations that are guaranteed to be beneficial:
*   **Buffer Reuse**: By having the entire workload as a graph, the compiler can optimally reuse memory buffers. It identifies buffers that are not simultaneously in use and assigns them to the same memory location, minimizing memory usage <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.
*   **Kernel Dispatching**: Instead of the traditional CPU-GPU round trip for each kernel launch, Luminal dispatches all kernels at once into a queue, allowing the GPU to run through them sequentially and saving significant time <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Training Support as an Extension

Luminal was initially designed as an inference library <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. However, due to its flexible graph representation, an external library for an autograd engine was built that works directly within Luminal <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. This engine derives a backward graph from a forward graph and attaches it, allowing Luminal's compilers (including the search process) to optimize for training as well <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. This modularity means external contributors can write their own autograds or other advanced training setups <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

## Future Developments

Luminal has ambitious future plans:
*   **More Hardware Support**: Expanding support beyond CPU, CUDA, and Metal to include AMD, Tensor Torrent, Groq, and TPUs, aiming to democratize [[AI implementation and best practices | ML]] across various hardware <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Distributed Inference and Training**: Implementing full 3D distributed capabilities, including data parallel, pipeline parallel, and tensor parallel <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **Reinforcement Learning (RL) Optimization**: Codifying environments within the Luminal graph so that both the model's forward pass and environment steps can be optimized and run entirely on the GPU, significantly accelerating RL workflows <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
*   **Luminal Cloud**: Offering a serverless inference endpoint by allowing users to export Luminal models as graphs, upload them to the cloud, and get an optimized endpoint <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Luminal handles optimization, batching, queuing, and machine provisioning, with users paying only when their graph executes, aiming for the simplest and fastest cloud experience <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.

The simplicity of Luminal's design allows for faster innovation compared to more complex frameworks <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.