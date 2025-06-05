---
title: Deep learning compilers and optimization
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

Luminal aims for "radical simplification through search" in Machine Learning (ML) libraries <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The core philosophy is to achieve performance and capability without complexity by utilizing compilers and search <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Problem with Current ML Libraries
Deep learning is fundamentally simple, relying on linear algebra with basic operations like additions, multiplies, and matrix multiplications <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, existing ML libraries are highly complex <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

For example, PyTorch has over 1,200 operations and 15 different data types, supporting various devices like CPU, CUDA, AMD, TPUs, and NPUs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This complexity scales multiplicatively with the number of operations, data types, and supported devices (ops × data types × devices) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Adding a new operation, data type, or device causes complexity to explode <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This has resulted in PyTorch having over 3 million lines of code, and TensorFlow being even larger <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Such complexity leads to more bugs and makes the software difficult to extend or build upon <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Luminal's Simplification Strategy
Luminal takes a top-down approach, focusing on the minimum necessary components to run ML models <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. It uses a small set of very simple "Lego blocks" of operations to build complex models <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Core Operations
Luminal supports only 12 core operations <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>:
*   **Unary Operations**: `x2`, `log2`, `sin`, `reciprocal`, `square root` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>
*   **Binary Operations**: `addition`, `multiplication`, `modulo`, `less than` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   **Reductions**: `sum reduce`, `max reduce` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

These 12 operations can support all commercially relevant models, including language models, vision-language models, CNNs, RNNs, and diffusion models <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Other common operations are just combinations of these core ops <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>:
*   **Subtraction**: Addition and multiplication by -1 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
*   **Division**: Multiplication and reciprocal <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>
*   **Matrix Multiply (MatMul)**: Broadcasted multiply and then sum reduce, leveraging tensor shape metadata manipulation <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>
*   **Convolution**: Pooling through shape trackers and then a matmul with the convolution kernel <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>

### Static vs. Dynamic
Many existing libraries were built 5-10 years ago with dynamism at their core for experimentation, prioritizing hackability over performance <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. However, deep learning is not fundamentally dynamic; its inherent dynamism is very small and bounded <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. In transformer models, only the KV cache length and sequence length are truly dynamic; the rest of the model is static <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

Luminal represents models as directed acyclic graphs (DAGs) of operations <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. This approach makes Luminal extremely simple, with under 5,000 lines of code, making it learnable in an afternoon <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

## Compiling for High Performance
While Luminal's primitive graphs are slow by default, the goal is to transform them into faster graphs using compilers <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

Traditional deep learning stacks are very complex, with layers of dependencies like Hugging Face Transformers on top of PyTorch, xformers, cuDNN, cuBLAS, and CUDA <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. This leads to "dependency hell" during installation and makes bug tracing difficult <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Luminal simplifies this by directly generating CUDA code, creating a much simpler stack: Luminal -> Graph -> Compilers -> CUDA <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### The Compiler Problem: Complexity and Hardware Trends
ML compilers historically struggle to take over due to rapidly increasing complexity <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. As the complexity of generated code grows, the compiler's complexity scales with the square or cube of that growth, eventually becoming too complex for humans to write <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This bottlenecks hardware startups <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

Hardware is trending towards simpler designs (e.g., TPUs are simpler and faster than GPUs, which are simpler and faster than CPUs) to achieve better performance per watt <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This implies more complex software is needed to manage these simpler hardware architectures <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This leads to the "Very Large Instruction Width (VLIW) compiler problem," where hardware wants compilers to statically schedule everything, but compilers become too complex <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

### Solving Complexity with Search
Luminal addresses this by applying a search-based solution, similar to how AlphaGo conquered Go <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Instead of hand-writing perfect algorithms, Luminal searches through logically equivalent GPU kernels <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

The process involves:
1.  **Graph to Expressions**: Converting the model graphs into expressions within `egg log`, a library that uses e-graphs for memory-efficient representation of the search space <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  **Rewrite Rules**: Applying 20-25 simple rewrite rules, each making a small, logically equivalent alteration to a GPU kernel <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
3.  **Search Space Generation**: Iteratively applying these rules to build a vast search space of equivalent kernels <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
4.  **Performance Profiling**: Testing the runtime of different equivalent kernels and choosing the fastest one <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. For larger search spaces, techniques like Monte Carlo search prune the options <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### Found Optimizations
This search process can discover significant optimizations:

*   **Kernel Fusion**: Merging multiple operations into a single kernel to minimize data movement between global memory and compute units <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Data movement accounts for about 99% of energy and time spent in GPUs <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. By fusing, data is loaded once and written once, drastically improving performance <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
    *   For example, an unfused graph with many sequential operations, each requiring memory write-backs and read-ins, can be fused into a single, complex kernel that takes roughly the same time as any one of the individual operations <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

*   **Flash Attention Discovery**: Luminal's search technique was able to independently discover Flash Attention, a complex optimization for multi-head attention that took the industry five years to find <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. Luminal takes the naive multi-head attention graph, applies simple rewrite rules to build a huge search space, profiles kernels, and identifies Flash Attention as the fastest <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Luminal is believed to be the only compiler capable of this <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

### Deterministic Optimizations
After the search process generates fast kernels, Luminal applies deterministic optimizations that are always beneficial:
*   **Buffer Reuse**: Minimizing memory usage by optimally reusing memory buffers <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Since the entire workload is a graph, the compiler can identify when buffers are not concurrently used and assign them to the same memory location <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
*   **Kernel Issuance**: Dispatching all kernels to the GPU at once, rather than waiting for the CPU to dispatch each one sequentially and await its completion <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. This eliminates CPU-GPU roundtrip delays, saving significant time <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

## Training and Future Directions
Originally designed as an inference library <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>, Luminal's flexible graph representation allowed for an external autograd engine <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. This engine derives a backward graph from a forward graph, enabling [[developing_and_optimizing_ai_agents | training]] for free, as all inference compilers and search processes also apply to the backward pass <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. This extensibility allows external contributors to develop their own autograds or advanced [[finetuning_ai_models_for_better_performance | training]] setups <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

Future plans for Luminal include:
*   **Expanded Hardware Support**: Adding support for AMD, Tensor Torrent, Groq, and TPUs, beyond current CPU, CUDA, and Metal support, to democratize ML across hardware <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Distributed Inference and Training**: Implementing full 3D distributed capabilities through data parallel, pipeline parallel, and tensor parallel <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **Reinforcement Learning (RL) Acceleration**: Codifying RL environments directly into the Luminal graph to allow the environment and model to be optimized together and run entirely on the GPU <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. This could dramatically accelerate RL workflows <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

## Luminal Cloud
Luminal also offers a cloud service <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Users can export their Luminal model graphs, upload them to the cloud, and get a serverless inference endpoint <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>. The service handles optimization, batching, queuing, and machine provisioning, with users only paying when their graph is executing <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. This aims to be the simplest and fastest ML cloud experience <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.