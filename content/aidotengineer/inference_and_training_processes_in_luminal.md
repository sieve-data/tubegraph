---
title: Inference and Training Processes in Luminal
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 
## Luminal's Radical Simplification for Machine Learning

Luminal is presented as an ML library that achieves "radical simplification through search" <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. It aims to be far simpler than most other ML libraries without compromising performance or capability, leveraging compilers and search techniques <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### The Problem of ML Library Complexity

Deep learning, at its core, is described as fundamentally simple: linear algebra involving scalars, vectors, matrices, and tensors, with a few core operations like additions, multiplies, and element-wise operations <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, the machine learning software ecosystem is exceedingly complicated <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

For instance, PyTorch, a prominent library, has over 1,200 operations and 15 different data types, running on various devices such as CPU, CUDA, AMD, and TPUs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This complexity scales multiplicatively (operations × data types × devices), leading to massive codebases like PyTorch's over 3 million lines or TensorFlow's even larger size <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This complexity leads to bugs and makes it difficult to extend or use <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Luminal's Simplified Approach

Luminal takes a top-down approach, identifying the minimum required components for ML models <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. It reduces deep learning to just 12 fundamental operations, treating models as "Lego blocks" of simple operations <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>:
*   **Unary Operations**: `x2`, `log`, `sin`, `reciprocal`, `square root` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
*   **Binary Operations**: `addition`, `multiplication`, `modulo`, `less than` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   **Reductions**: `sum reduce`, `max reduce` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

With these operations, Luminal can support all commercially relevant models, including language models, vision language models, CNNs, RNNs, and diffusion models <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. More complex operations like subtraction, division, matrix multiplication (matmuls), and convolution are derived by combining these 12 basic operations and manipulating tensor shape metadata <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Luminal also notes that while older libraries were built with dynamism at their core for experimentation with RNNs and LSTMs, deep learning models are fundamentally not dynamic <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. In a transformer model, only the KV cache length and sequence length are dynamic; the rest is static <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Luminal specifies models as directed acyclic graphs (DAGs) of operations, allowing for a static representation that can be optimized <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

This simplification results in Luminal being under 5,000 lines of code, designed to be learnable in an afternoon <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### The [[AI Model Training and Inference | Inference]] Process: Compilation Through Search

While Luminal's primitive graphs are initially slow (e.g., Llama 7B taking all day to generate a sentence <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>), the core idea is to transform these graphs into much faster ones using compilers <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

Luminal's stack is notably simpler than traditional ML stacks. A traditional stack might involve [[AI implementation and best practices | Hugging Face Transformers]] on top of PyTorch and xformers, which use handwritten kernels, sometimes calling operations in cuDNN or cuBLAS, all sitting on CUDA <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This creates complex dependencies and "dependency hell" <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. In contrast, Luminal directly emits CUDA code, with nothing between its library, graph, compilers, and CUDA <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

#### Overcoming Compiler Complexity with Search

Traditional ML compilers face a problem: as the complexity of the generated code grows, the compiler's complexity scales even faster (e.g., squared or cubed) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. This "VIW compiler problem" (Very Large Instruction Width) means human-written compilers become too complex beyond a certain point <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

Luminal's solution is to use search, akin to how AlphaGo tackled the game of Go <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Instead of writing a perfect algorithm, Luminal searches through logically equivalent GPU kernels <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

The process involves:
1.  **Graph to Expressions**: Converting the operation graphs into expressions within a library called `egg log`, which uses egraphs to efficiently represent the search space <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  **Rewrite Rules**: Applying 20-25 simple rewrite rules, each making a small, logically equivalent alteration to a GPU kernel <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Iterative application of these rules builds a large search space <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
3.  **Profiling and Selection**: The system profiles the runtime of different equivalent kernels and chooses the fastest one <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. For larger search spaces, Monte Carlo search is used to prune possibilities <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

#### Optimizations Found by Search

This search-based compilation finds crucial optimizations:
*   **Kernel Fusion**: Merging multiple operations (e.g., `sin` followed by `x2`) into a single kernel to minimize data movement to and from global memory <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Data movement accounts for about 99% of GPU energy and time <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. A single fused kernel can be vastly faster than a sequence of unfused operations <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Flash Attention**: Luminal's search technique was able to independently discover Flash Attention, a complex algorithm that took the industry about five years to find <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

#### Deterministic Optimizations

After the search process, Luminal applies deterministic optimizations that are always beneficial:
*   **Buffer Reuse**: Minimizing memory usage by optimally reusing memory buffers. Because the entire workload is specified as a graph, the compiler can identify when buffers are no longer needed and reuse their memory <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.
*   **Batch Kernel Issuance**: Issuing all GPU kernels at once, rather than the traditional method of CPU dispatching one kernel, waiting for it to finish, and then dispatching the next <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. This eliminates significant round-trip time to the CPU <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

### The [[AI Model Training and Inference | Training]] Process

Luminal was initially designed for inference <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. However, due to its flexible graph representation, an external library (crate) was built to serve as an autograd engine <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. This engine derives a backward graph from a given forward graph and attaches it <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.

This means Luminal gets training "for free," as all the same compilers and search processes used for inference also work on the backward pass <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>. This extensibility allows external contributors to write their own autograds, gradient sharding, or advanced training setups, a unique capability among ML libraries <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

### Future Developments

Luminal aims to expand its capabilities:
*   **Hardware Support**: Adding support for AMD, Tenstorrent, Groq, and TPUs, to "break the CUDA coupe" and democratize ML across different hardware <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Distributed Inference and Training**: Implementing full 3D distribution, including data parallel, pipeline parallel, and tensor parallel <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **[[Custom model training and reinforcement learning | Reinforcement Learning]] Optimization**: Addressing the bottleneck in RL where models run on GPU and environments on CPU. By codifying environments within the Luminal graph, both the model's forward pass and environment steps can be optimized and run entirely on the GPU <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.
*   **[[Luminal Cloud and Serverless Implementation | Luminal Cloud]]**: A serverless inference endpoint solution where users export a Luminal model graph, upload it, and get an endpoint. Luminal handles optimization, batching, queuing, and machine provisioning, with users paying only for graph execution time <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.

Luminal's simplicity allows for faster innovation compared to more complex frameworks <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.