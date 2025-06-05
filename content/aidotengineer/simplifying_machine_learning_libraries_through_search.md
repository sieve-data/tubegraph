---
title: Simplifying machine learning libraries through search
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

[[luminal_deep_learning_library | Luminal]] is a machine learning (ML) library designed to achieve radical simplification through the use of search-based compilation techniques <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Its core philosophy is to be significantly simpler than other ML libraries while maintaining high performance and capability by leveraging [[deep_learning_compilers_and_optimization | compilers]] and, more specifically, [[searchbased_optimization_for_gpu_kernels | search]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## The Problem: Complexity in ML Libraries

Deep learning, at its fundamental level, involves simple linear algebra, primarily operations on scalars, vectors, matrices, and tensors, with a few core operations like additions, multiplications, and element-wise operations <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Despite this inherent simplicity, the current ML software ecosystem is highly complicated <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

For example, PyTorch, a prominent ML library, features over 1,200 operations and 15 different data types, supporting various devices such as CPU, CUDA, AMD, TPUs, and NPUs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. The complexity of these libraries scales multiplicatively, not additively, with the number of operations, data types, and supported devices <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This means adding support for a new operation, data type, or device can cause complexity to explode <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. As a result, PyTorch comprises over 3 million lines of code, and TensorFlow is even larger <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This complexity leads to more bugs and makes it challenging for developers to extend or build upon these systems <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Luminal's Approach: Radical Simplification

[[luminal_deep_learning_library | Luminal]] addresses this complexity by taking a top-down approach, identifying the minimum set of operations required to run ML models <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
It operates on the principle that complex models can be constructed from very simple "Lego blocks" of operations <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Minimal Operation Set
[[luminal_deep_learning_library | Luminal]] utilizes only 12 fundamental operations <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>:
*   **Unary Operations**: `x2`, `log2`, `sin`, `reciprocal`, `square root` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>
*   **Binary Operations**: `addition`, `multiplication`, `modulo`, `less than` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   **Reductions**: `sum reduce`, `max reduce` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

These 12 operations are sufficient to support all commercially relevant models, including language models, vision-language models, CNNs, RNNs, and diffusion models <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Many seemingly complex operations are merely compositions of these simpler ones. For instance:
*   Subtraction is `addition` and `multiplication` by -1 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   Division is `multiplication` and `reciprocal` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   Matrix multiplication (matmuls) can be achieved via broadcasted `multiply` followed by `sum reduce` <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   Convolution can be performed by combining pooling (via shape trackers) and a matmul with a convolution kernel <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Static Graphs
Traditional ML libraries were built with dynamism at their core, important for experimental models like RNNs, where performance was less critical <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. However, deep learning is fundamentally not dynamic; its dynamism is very small and bounded <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. In a transformer model, only the KV cache length and sequence length are typically dynamic, while the rest of the model is static <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

[[luminal_deep_learning_library | Luminal]] specifies models as Directed Acyclic Graphs (DAGs) of operations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This graphical representation allows for a complete specification of models, from simple matrix multiplies to complex, large-scale models <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

As a result of this simplification, [[luminal_deep_learning_library | Luminal]] is remarkably simple: it is under 5,000 lines of code <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>, easy to understand, and designed to be learnable within an afternoon <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Achieving Performance Through Compilers and Search

While the simplified graphs are initially slow (e.g., Llama 7B running for a whole day to generate a single sentence) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, the intention is not to run these primitive graphs directly. Instead, these graphs are fed through [[deep_learning_compilers_and_optimization | compilers]] to transform them into faster, optimized graphs <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Simplified Stack
A traditional ML stack (e.g., Hugging Face Transformers -> PyTorch/XFormers -> cuDNN/cuBLAS -> CUDA) creates a complex dependency story, leading to "dependency hell" during installation and difficulties in bug tracing <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. [[luminal_deep_learning_library | Luminal]] directly emits CUDA code, creating a much simpler stack: the [[luminal_deep_learning_library | Luminal]] library, its graph, its compilers, and CUDA <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### The Compiler Challenge and Search
The core challenge in [[deep_learning_compilers_and_optimization | ML compilers]] is that their complexity scales non-linearly (e.g., quadratically or cubically) with the complexity of the code they need to generate <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This makes compilers incredibly difficult for humans to write beyond a certain point <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Furthermore, as hardware becomes simpler and more uniform (from CPUs to GPUs to TPUs, which are faster and more performance-per-watt efficient), the software and compilers need to become more complex to manage them <a class="yt-timestamp" data-t="00:09:50">[00:10:51]</a>. This leads to the VLIW compiler problem, where simple hardware requires overly complex compilers <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

[[luminal_deep_learning_library | Luminal]] overcomes this bottleneck by leveraging [[searchbased_optimization_for_gpu_kernels | search]] <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Inspired by AlphaGo, which used search to conquer the game of Go <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>, [[luminal_deep_learning_library | Luminal]] searches through logically equivalent GPU kernels <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

### How Search Works
1.  **Graph to Expressions**: Initial graphs are converted into expressions within a library called `egglog`, which uses e-graphs to efficiently represent a search space of equivalent expressions <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  **Rewrite Rules**: A small set of simple rewrite rules (20-25) are defined <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Each rule makes a small, logically equivalent alteration to a GPU kernel <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
3.  **Search Space Expansion**: By iteratively applying these simple rewrite rules, a vast search space of equivalent kernels is built <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
4.  **Profiling and Selection**: The system then profiles the runtime of various kernels within this search space and selects the fastest one <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. For larger spaces, techniques like Monte Carlo tree search are used to prune the search <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

This [[searchbased_optimization_for_gpu_kernels | search]] approach allows [[luminal_deep_learning_library | Luminal]] to find optimal kernels without needing to hand-write complex rules that guarantee fast code <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Types of Optimizations Found
*   **Kernel Fusion**: This common optimization merges multiple operations into a single kernel, significantly reducing data movement between global memory and compute units, which is often 99% of energy and time spent on GPUs <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. By loading data once, computing multiple operations, and writing back once, performance drastically improves <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Flash Attention Discovery**: [[luminal_deep_learning_library | Luminal]]'s [[searchbased_optimization_for_gpu_kernels | search]] technique was able to independently discover Flash Attention, a highly complex and crucial optimization for transformers that took the industry five years to find <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This demonstrates the power of search to uncover non-obvious, complex optimizations <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

### Deterministic Optimizations
After the [[searchbased_optimization_for_gpu_kernels | search]] process identifies fast kernels, [[luminal_deep_learning_library | Luminal]] applies deterministic optimizations that are known to always be beneficial:
*   **Buffer Reuse**: The compiler analyzes the entire workload graph to optimally reuse memory buffers, minimizing overall memory usage <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. If Buffer A and Buffer B are never used concurrently, they can share the same memory location <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.
*   **Batch Kernel Issuance**: Instead of the CPU dispatching one GPU kernel at a time and waiting for its completion, [[luminal_deep_learning_library | Luminal]] dispatches all kernels in advance, allowing the GPU to run through them sequentially <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. This eliminates significant round-trip time between the CPU and GPU <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

## Extending Luminal's Capabilities

### Training Support
While initially designed for inference, [[luminal_deep_learning_library | Luminal]]'s flexible graph representation allowed for the development of an external autograd engine <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. This engine derives a backward graph from a forward graph, enabling training capabilities. All the existing compilers and [[searchbased_optimization_for_gpu_kernels | search]] processes for inference also apply to training <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. This external extension model is unique among ML libraries, allowing external contributors to build custom autograds, gradient sharding, or other training setups <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### Future Developments
*   **Expanded Hardware Support**: Current support includes CPU, CUDA, and Metal. Future plans aim to support AMD, Tenstorrent, Groq, and TPUs to democratize ML across diverse hardware <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Distributed Inference and Training**: Implementing full 3D distributed capabilities, including data parallel, pipeline parallel, and tensor parallel <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **Reinforcement Learning (RL) Optimization**: Codifying environments within the [[luminal_deep_learning_library | Luminal]] graph, allowing the environment simulation and model forward pass to run entirely on the GPU <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>. This could dramatically accelerate RL workflows by eliminating the CPU-GPU bottleneck <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.

### Luminal Cloud
[[luminal_deep_learning_library | Luminal]] leverages its graph representation to offer a serverless inference endpoint through the [[luminal_deep_learning_library | Luminal]] cloud <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Users can export their [[luminal_deep_learning_library | Luminal]] model graphs, upload them, and receive a serverless inference endpoint <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>. The cloud handles optimization, batching, queuing, and machine provisioning, with users only paying for actual graph execution time <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. This aims to deliver the simplest and fastest cloud ML experience <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.

The simplicity of [[luminal_deep_learning_library | Luminal]]'s design allows for faster innovation compared to more complex frameworks <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.