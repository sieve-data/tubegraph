---
title: GPU Kernel Optimization
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

Luminal is an ML library focused on radical simplification through [[SearchBased Deep Learning Compilers | search]] to achieve high performance and capability <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While deep learning is fundamentally simple linear algebra, consisting of scalars, vectors, matrices, tensors, and a few core operations like additions, multiplies, and matmuls <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, the existing machine learning software ecosystem is exceedingly complex <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## The Problem with Traditional ML Libraries

Libraries like PyTorch contain over 1,200 operations and 15 different data types, running on various [[gpu_infrastructure_and_performance | GPU]] devices like CPU, CUDA, AMD, TPUs, and NPUs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This complexity scales multiplicatively (operations × data types × devices), leading to massive codebases like PyTorch's 3 million lines of code or TensorFlow's even larger footprint <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This complexity introduces more bugs and makes it difficult to extend or build upon the libraries <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

Traditional stacks involve complex dependencies, from high-level libraries like Hugging Face Transformers to optimized kernels, `cuDNN`/`cuBLAS`, and CUDA <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Installing and debugging these complex stacks leads to "dependency hell" and significant pain in tracing down bugs <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Luminal's Simplified Approach

Luminal takes a top-down approach, identifying the minimum set of operations required to run ML models <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. It uses only 12 very simple core operations:
*   **Unary Operations**: x2, log2, sin, reciprocal, square root <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>
*   **Binary Operations**: addition, multiplication, modulo, less than <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   **Reductions**: sum reduce, max reduce <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

All other common operations (like subtraction, division, matmuls, and convolutions) can be formed by combining these 12 primitive operations, often by manipulating tensor shape metadata <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For example, a matrix multiply is effectively a broadcasted multiply followed by a sum reduction <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Static Graph Representation
Luminal acknowledges that deep learning is not fundamentally dynamic; earlier dynamism in libraries like PyTorch was for convenience during experimentation <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. The dynamism in models like transformers is typically small and bounded (e.g., KV cache length, sequence length) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

Luminal specifies models as directed acyclic graphs (DAGs) of operations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This graph representation allows for the entire workload to be known ahead of time <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
For example, a single dense neural network layer (a matrix multiply) can be represented as loading a tensor, loading a weight, element-wise multiplying them, and then sum reducing the result <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

This simplification results in Luminal being under 5,000 lines of code, making it easy to understand and learn within an afternoon <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Achieving Performance Through Compilers and Search

While Luminal's primitive graphs are slow by default (e.g., Llama 7B takes all day to generate a sentence) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, the goal is to transform these graphs into much faster ones using compilers <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Luminal directly generates CUDA code, creating a very simple stack between the library and the [[gpu_infrastructure_and_performance | GPU]] <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

### Overcoming the VLIW Compiler Problem with Search
The complexity of compilers scales rapidly (square or cube) with the complexity of the code they need to generate, making them too complex for humans to write beyond a certain point <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This "VLIW compiler problem" arises because simpler hardware (like [[gpu_infrastructure_and_performance | GPUs]] and TPUs) requires more complex static scheduling from the compiler <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

Luminal solves this by applying the same [[SearchBased Deep Learning Compilers | search]]-based approach used by AlphaGo <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Instead of hand-writing complex rules to produce fast code, Luminal [[SearchBased Deep Learning Compilers | searches]] through logically equivalent [[gpu_infrastructure_and_performance | GPU]] kernels <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

This process involves:
1.  **Graph to E-graph Conversion**: Converting the model's graphs into expressions within the `egglog` library, which uses e-graphs for memory-efficient representation of the search space <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
2.  **Rewrite Rules**: Applying simple rewrite rules (e.g., 20-25 rules) that make small, logically equivalent alterations to a [[gpu_infrastructure_and_performance | GPU]] kernel <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Iteratively applying these rules builds a massive search space <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
3.  **Runtime Profiling**: Testing the runtime of different equivalent kernels within the search space and choosing the fastest one <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. For larger spaces, techniques like Monte Carlo tree search are used to prune options <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### Examples of Search-Discovered Optimizations

*   **Kernel Fusion**: This optimization merges multiple operations into a single [[gpu_infrastructure_and_performance | GPU]] kernel to minimize data movement between global memory and compute units <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Data movement on [[gpu_infrastructure_and_performance | GPUs]] accounts for 99% of energy and time spent <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. By fusing kernels, data is loaded and written only once, dramatically speeding up complex graphs <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Flash Attention**: Luminal's [[SearchBased Deep Learning Compilers | search]] technique was able to independently discover flash attention, a complex algorithm that took the industry five years to find <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. This demonstrates the power of search to uncover highly non-obvious optimizations <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

### Deterministic Optimizations

After the search process identifies fast kernels, Luminal applies a set of deterministic optimizations that are known to always be beneficial:
*   **Buffer Reuse**: The compiler minimizes memory usage by optimally reusing memory buffers. By knowing the entire workload graph ahead of time, it can identify when buffers are no longer needed and assign their memory to other buffers <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.
*   **Batch Kernel Issuing**: Instead of the CPU dispatching one [[gpu_infrastructure_and_performance | GPU]] kernel at a time and waiting for its completion, Luminal dispatches all kernels at once to the [[gpu_infrastructure_and_performance | GPU]]. This eliminates the time-consuming round trip to the CPU for each kernel, saving significant time <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Training Support

Initially designed for inference, Luminal's flexible graph representation allowed for the creation of an external autograd engine. This engine derives a backward graph from a forward graph, enabling training capabilities. All the compilers and [[SearchBased Deep Learning Compilers | search]] processes used for inference also apply to the backward pass, effectively providing training for free <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. This external extension model is unique among ML libraries, allowing external contributors to build their own autograds or advanced training setups <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

## Future Developments

Luminal is actively working on:
*   **More Hardware Support**: Expanding support beyond CPU, CUDA, and Metal to include AMD, Tensor Torrent, Groq, and TPUs, aiming to democratize ML across diverse hardware <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   **Distributed Inference and Training**: Implementing full 3D distribution through data parallel, pipeline parallel, and tensor parallel approaches <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
*   **Reinforcement Learning Acceleration**: Codifying environments within the Luminal graph to optimize environment steps and model forward passes together on the [[gpu_infrastructure_and_performance | GPU]], dramatically accelerating RL workflows <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.

## Luminal Cloud

Luminal also offers a cloud service that leverages its graph representation. Users can export their Luminal models as files and upload them to the cloud to get a serverless inference endpoint <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. The Luminal cloud handles optimization, batching, queuing, and machine provisioning, with users only paying when their graph is executing <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. The goal is to provide the simplest, fastest, and most straightforward cloud experience <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.