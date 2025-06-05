---
title: Searchbased optimization for GPU kernels
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

Luminal is an ML library built on the principle of "radical simplification through search" <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. While fundamental deep learning operations are simple linear algebra, consisting of scalars, vectors, matrices, tensors, and core operations like additions, multiplies, and element-wise ops <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>, machine learning software ecosystems are highly complex <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. PyTorch, for example, has over 1,200 operations, 15 data types, and runs on many devices, leading to multiplicative complexity that causes its codebase to exceed 3 million lines <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. This complexity leads to bugs and makes libraries difficult to extend <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

Luminal addresses this by reducing the core operations to a minimal set of 12 very simple operations: unary operations (x2, log2, sin, reciprocal, square root), binary operations (addition, multiplication, modulo, less than), and reductions (sum reduce, max reduce) <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. These fundamental operations can represent all commercially relevant deep learning models, including language models, vision models, CNNs, RNNs, and diffusion models <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. More complex operations like subtraction, division, matrix multiplication (matmuls), and convolutions can be formed by combining these simple ops and manipulating tensor shape metadata <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

## Complexity and Compilers

Traditional deep learning libraries were often built with dynamism at their core for experimentation, but this added significant complexity <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. Luminal represents models as static directed acyclic graphs (DAGs) of operations, with minimal bounded dynamism (e.g., KV cache and sequence length in transformers) <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. This simplification results in Luminal's core library being under 5,000 lines of code, making it easy to understand and extend <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>.

However, a model defined with these primitive operations is inherently slow <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>. The speed is achieved by taking these initial graphs and transforming them into much faster graphs using [[deep_learning_compilers_and_optimization | compilers]] <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. Unlike traditional stacks that rely on complex dependencies (e.g., Hugging Face on PyTorch, xformers, cuDNN, cuBLAS, CUDA), Luminal directly emits CUDA code, simplifying the dependency stack and making debugging easier <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.

## The Problem with Traditional Compilers

Traditional ML [[deep_learning_compilers_and_optimization | compilers]] face a bottleneck: as the complexity of the generated code grows, the compiler's complexity scales super-linearly (square or cube), making it too difficult for humans to write <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>. This is known as the VLIW (Very Long Instruction Word) compiler problem <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. Furthermore, hardware is becoming simpler (e.g., TPUs are simpler and faster than GPUs, which are simpler and faster than CPUs), requiring more complex software to manage low-level details that hardware no longer handles <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

## Search-Based Optimization

Luminal's solution to this compiler complexity is to use search <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>, similar to how AlphaGo conquered the game of Go <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. Instead of hand-writing complex rules for optimal code generation, Luminal searches through logically equivalent GPU kernels to find the fastest one <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.

### How Search Works
1.  **Graph Conversion**: The initial operation graphs are converted into expressions within `egglog`, a library that uses e-graphs to represent the search space efficiently <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
2.  **Rewrite Rules**: Luminal uses 20-25 simple rewrite rules that make small, logically equivalent alterations to a GPU kernel <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>.
3.  **Search Space Generation**: By iteratively applying these simple rules, a vast search space of equivalent kernels is built <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>.
4.  **Profiling and Selection**: The runtime of different equivalent kernels within the search space is profiled, and the fastest one is chosen <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>. For very large search spaces, techniques like Monte Carlo Tree Search are used to prune options <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.

### Examples of Search-Found Optimizations

*   **Kernel Fusion**: This optimization combines multiple operations into a single kernel. For instance, if operation B operates on the output of operation A (e.g., `sign` followed by `x2`), the naive approach involves loading data, performing A, writing to memory, reading from memory, performing B, and writing to memory again <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. Since data movement accounts for approximately 99% of energy and time spent on GPUs <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>, kernel fusion merges these into one kernel, loading data once and writing the final result once, dramatically reducing runtime <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. Luminal's compiler can merge a complex series of operations into a single, much faster kernel <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>.
*   **Flash Attention**: Luminal's search technique was able to discover Flash Attention, a complex algorithm that took the industry about five years to find (discovered by Tri Dao in 2022, Transformers in 2017) <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>. By taking a naive multi-head attention graph, applying simple rewrite rules to build a search space, and profiling kernels, Luminal's compiler autonomously found Flash Attention. This demonstrates the power of search in finding non-obvious, highly complex optimizations <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>.

## Deterministic Optimizations

After the search process identifies the fastest kernel, Luminal applies a set of deterministic optimizations that are known to always be beneficial, regardless of their specific impact <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

*   **Buffer Reuse**: Luminal minimizes memory usage by optimally reusing memory buffers. Since the entire workload is specified as a graph, the compiler can identify when buffers are not used simultaneously and allocate them to the same memory location, significantly reducing memory footprint <a class="yt-timestamp" data-t="18:37:00">[18:37:00]</a>.
*   **Kernel Issuance**: Instead of the traditional method where the CPU dispatches a GPU kernel, waits for it to finish, and then dispatches the next, Luminal dispatches all kernels to the GPU at once. This avoids costly CPU-GPU roundtrips and saves significant time <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>.

## Training and Future Directions

Although initially designed as an inference library, Luminal's flexible graph representation allowed for an external autograd engine to be built <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>. This engine derives a backward graph from a forward graph, enabling [[Finetuning AI models for better performance | training]] and leveraging the same [[deep_learning_compilers_and_optimization | compilers]] and search processes for the backward pass <a class="yt-timestamp" data-t="20:40:00">[20:40:00]</a>. This external autograd is a unique feature, as other ML libraries typically integrate training into their core <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.

Future plans for Luminal include:
*   **Expanded Hardware Support**: Supporting AMD, Tensor Torrent, Groq, and TPUs, beyond current CPU, CUDA, and Metal support, to democratize ML across diverse hardware <a class="yt-timestamp" data-t="21:41:00">[21:41:00]</a>.
*   **Distributed Inference and Training**: Implementing full 3D distribution through data, pipeline, and tensor parallelism <a class="yt-timestamp" data-t="22:04:00">[22:04:00]</a>.
*   **Reinforcement Learning (RL) Acceleration**: Codifying environments within the Luminal graph so that both the model's forward pass and the environment step can be optimized and run entirely on the GPU, significantly accelerating RL workflows <a class="yt-timestamp" data-t="22:17:00">[22:17:00]</a>.

Luminal also offers a cloud service where users can export their Luminal graphs, upload them, and get a serverless inference endpoint. This service handles optimization, batching, queuing, and machine provisioning, with users only paying when their graph is executing <a class="yt-timestamp" data-t="23:06:00">[23:06:00]</a>. The simplicity of Luminal's core design allows for rapid innovation in these areas, tackling problems typically addressed by far more complex frameworks <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.