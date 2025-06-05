---
title: SearchBased Deep Learning Compilers
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

Luminal is an innovative ML library designed for radical simplification through search, aiming to be the future of machine learning libraries <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It achieves greater simplicity than most other ML libraries without compromising performance or capability, by leveraging compilers and, more specifically, search <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Problem with Current ML Libraries

Deep learning, at its core, is fundamentally simple, consisting primarily of linear algebra operations on scalars, vectors, matrices, and tensors, with a few core operations like additions, multiplies, and matrix multiplications <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, the machine learning software ecosystem is exceedingly complicated <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

For instance, PyTorch, a prominent library, features over 1,200 operations and 15 different data types, running on various devices such as CPUs, CUDA, AMD, and TPUs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This complexity scales multiplicatively (operations * data types * devices), leading to an exponential increase in complexity when supporting new operations, data types, or devices <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. As a result, PyTorch contains over 3 million lines of code, and TensorFlow is even larger <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Such complexity introduces numerous bugs and makes it extremely difficult for developers to extend, use, or build upon these libraries <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Luminal's Approach to [[Simplification of Machine Learning Libraries]]

Luminal adopts a top-down approach, identifying the minimum essential components required to run ML models <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Since deep learning is linear algebra, which boils down to simple operations, Luminal constructs complex models from a minimal set of basic "Lego block" operations <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

Luminal operates with only 12 core operations <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>:
*   **Unary Operations**: `x^2`, `log2`, `sin`, `reciprocal`, `square root` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>
*   **Binary Operations**: `addition`, `multiplication`, `modulo`, `less than` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   **Reductions**: `sum reduce`, `max reduce` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

With just these operations, Luminal can support all commercially relevant models, including language models, vision language models, CNNs, RNNs, and diffusion models <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Many seemingly complex operations are merely combinations of these simple ones. For example, subtraction is addition with multiplication by -1, division is multiplication with a reciprocal, and matrix multiplication and convolution can be derived by manipulating tensor shape metadata and combining basic operations <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

Luminal also recognized that while existing libraries prioritized dynamism for experimentation with RNNs and LSTMs, deep learning itself is not inherently dynamic <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. The dynamism in models like transformers is very small and bounded (e.g., KV cache length, sequence length) <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Therefore, Luminal represents models as static Directed Acyclic Graphs (DAGs) of operations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This approach makes Luminal incredibly simple, with under 5,000 lines of code, and allows for learning its core concepts in a single afternoon <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Achieving Performance Through Compilers

While Luminal's simplified graphs are slow by default (e.g., Llama 7B takes an entire day to generate a single sentence initially) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, the library's strength lies in transforming these primitive graphs into much faster ones using compilers <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Luminal compiles its way back to high performance <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

Unlike traditional ML stacks, which involve complex dependencies like Hugging Face Transformers, PyTorch, Xformers, cuDNN, cuBLAS, and CUDA <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>, Luminal directly emits CUDA code <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This eliminates dependency hell and simplifies bug tracing, making the stack as straightforward as possible: Luminal library, its graph, its compilers, and CUDA <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## The Challenge of ML Compilers: The VLIW Problem

One reason ML compilers haven't dominated is that as the complexity of the target code increases, the compiler's complexity scales exponentially (e.g., with the square or cube) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This eventually makes compilers too complex for humans to write <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

The trend in hardware development pushes towards simpler, faster, and more uniform hardware (CPUs -> GPUs -> TPUs) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. While this yields better performance per watt, it shifts more responsibility onto the software and, consequently, the compiler <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. This leads to the Very Long Instruction Word (VLIW) compiler problem: companies want simple hardware by having the compiler statically schedule everything, but compilers eventually become too complex for humans to write <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

## Search as the Solution for Deep Learning Compilers

Luminal overcomes the VLIW compiler problem by employing the same solution used by the AlphaGo team: search <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Instead of attempting to write a perfect algorithm to find the optimal code, Luminal searches through a vast space of logically equivalent GPU kernels <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

This process involves:
1.  Converting model graphs into expressions within a library called `egg log`, which uses e-graphs to efficiently represent the search space <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  Defining 20-25 simple rewrite rules <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. These rules make small, logically equivalent alterations to a GPU kernel, building an iteratively expanding search space <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
3.  Profiling the runtimes of various equivalent kernels within the search space and selecting the fastest one <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. For extremely large search spaces, techniques like Monte Carlo search are used to prune options <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

This search-based approach allows Luminal to find highly optimized kernels without needing to hand-write complex rules <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Optimizations Discovered Through Search

This search technique allows Luminal to automatically discover crucial optimizations:

*   **Kernel Fusion**: This optimization merges multiple operations into a single kernel, drastically reducing data movement, which typically accounts for 99% of energy and time spent in GPUs <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. By loading data once, performing multiple operations, and writing back once, an entire complex graph can be fused into a single kernel, leading to significant speedups <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This directly contributes to [[Efficiency and smart execution engines in AI applications]].
*   **Flash Attention**: Luminal's search process was able to independently discover Flash Attention, a very complex algorithm that took the industry five years to find (discovered by Tri Dao in 2022, five years after Transformers in 2017) <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This accomplishment demonstrates the power of search to find extremely complex optimizations that are not obvious to program into a compiler <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

### Deterministic Optimizations

After the search process identifies fast kernels, Luminal applies deterministic optimizations that are guaranteed to be beneficial:

*   **Buffer Reuse**: By analyzing the entire workload graph, the compiler identifies memory buffers that are never used simultaneously. These can then be allocated to the same physical memory, optimally reducing memory usage <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.
*   **Kernel Issuance**: Instead of the traditional CPU-GPU roundtrip for each kernel dispatch, Luminal issues all kernels at once to the GPU. This eliminates significant latency associated with waiting on the CPU, saving substantial time <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Training Capabilities

Initially designed for inference, Luminal's flexible graph representation allowed for the development of an external autograd engine <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. This external library derives a backward graph from a forward graph and attaches it, enabling Luminal's compilers (including the search process) to optimize both inference and training passes <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. This is unique among ML libraries, as training support is typically part of the core, whereas Luminal's approach allows for external contributors to develop their own autograds or advanced training setups <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

## Future Developments

Luminal is actively working on several fronts:
*   **Expanded Hardware Support**: Beyond current CPU, CUDA, and Metal support, plans include AMD, Tenstorrent, Groq, and TPUs to democratize ML across diverse hardware <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Distributed Inference and Training**: Implementing full 3D distribution (data parallel, pipeline parallel, tensor parallel) <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
*   **Reinforcement Learning (RL) Acceleration**: Codifying entire RL environments within the Luminal graph allows the environment's steps and the model's forward pass to be optimized and run entirely on the GPU, potentially dramatically accelerating RL workflows <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.
*   **Luminal Cloud**: A serverless inference endpoint platform where users can export their Luminal models as graph files and upload them. The cloud handles optimization, batching, queuing, and machine provisioning, with users paying only for execution time. This aims to deliver the simplest and fastest ML cloud experience <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. This streamlines the process of [[building_and_deploying_large_language_models]].

By embracing simplicity, Luminal aims to innovate far faster than more complex existing frameworks, pushing into territory previously covered by orders of magnitude more complex systems <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. For those interested in [[AI implementation and best practices]], Luminal offers a unique approach to development and deployment.