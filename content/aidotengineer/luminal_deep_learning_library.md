---
title: Luminal deep learning library
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

[[Simplifying machine learning libraries through search | Luminal]] is a deep learning library created with the core philosophy of radical simplification through search [00:00:16]. It aims to be significantly simpler than most other machine learning (ML) libraries without compromising performance or capability, achieving this through the use of [[Deep learning compilers and optimization | compilers]] and search [00:00:20]. The library focuses on simplifying the complex ML software ecosystem [00:01:04].

## The Problem of Complexity in ML Libraries
Deep learning, at its core, involves simple linear algebra, primarily operations on scalars, vectors, matrices, and tensors with a few core operations like additions, multiplications, and element-wise operations [00:00:36]. Despite this fundamental simplicity, ML libraries are notoriously complex [00:01:01].

For example:
*   **PyTorch** has over 1,200 operations and more than 15 different data types [00:01:10].
*   It supports numerous devices including CPU, CUDA, AMD, TPUs, and NPUs [00:01:21].
*   The complexity scales multiplicatively, not additively, with the number of operations, data types, and supported devices [00:01:42]. This means adding support for a new operation, data type, or device causes an explosion in complexity [00:01:51].
*   PyTorch is over 3 million lines of code, and TensorFlow is even larger [00:02:02].
*   This complexity leads to more bugs and makes it difficult for developers to extend, use, or build upon these libraries [00:02:15].

Traditional ML libraries were often built with dynamism at their core, especially 5 to 10 years ago when experimentation with RNNs and LSTMs required hackability and dynamism over raw performance [00:04:35]. However, the inherent dynamism in modern deep learning models is often very small and bounded, such as the KV cache length and sequence length in transformer models, with the rest being static [00:05:06].

## Luminal's Approach to Simplicity
[[Simplifying machine learning libraries through search | Luminal]] takes a top-down approach, identifying the minimum set of fundamental elements required to run ML models [00:02:27].
*   **Minimal Operations**: Deep learning boils down to simple linear algebra operations [00:02:38]. Luminal uses only 12 very simple core operations:
    *   **Unary Operations**: `x2`, `log2`, `sin`, `reciprocal`, `square root` [00:02:53].
    *   **Binary Operations**: `addition`, `multiplication`, `modulo`, `less than` [00:03:05].
    *   **Reductions**: `sum reduce`, `max reduce` [00:03:10].
*   **Compositionality**: All commercially relevant models and complex operations can be derived from these 12 basic operations [00:03:14].
    *   Subtraction is `addition` and `multiplication` by -1 [00:03:51].
    *   Division is `multiplication` and `reciprocal` [00:03:57].
    *   Matrix multiplications (`matmuls`) can be achieved by manipulating tensor shape metadata, performing a broadcasted `multiply`, and then `sum reduce` [00:04:03].
    *   Convolutions can be formed using pooling via shape trackers and a `matmul`-like operation with a convolution kernel [00:04:21].
*   **Static Graph Representation**: Models in [[Simplifying machine learning libraries through search | Luminal]] are specified as Directed Acyclic Graphs (DAGs) of operations [00:05:30]. This static representation allows for comprehensive optimization [00:18:52].
    *   A simple example is a matrix multiply for a dense neural network layer [00:05:37].
    *   More complex models are represented by larger graphs [00:06:04].

The consequence of this simplified approach is that [[Simplifying machine learning libraries through search | Luminal]] is extremely simple [00:06:19]. It is under 5,000 lines of code and is designed to be learnable in an afternoon [00:06:26].

## Performance Through [[Deep learning compilers and optimization | Compilers]] and Search
While the primitive graphs are slow (e.g., Llama 7B takes all day for a sentence) [00:06:49], the core idea is to transform these graphs into much faster ones using [[Deep learning compilers and optimization | compilers]] [00:07:01].

### Luminal's Simplified Stack
A traditional ML stack is highly complex, involving multiple layers like Hugging Face Transformers, PyTorch, xFormers, custom handwritten kernels, cuDNN, cuBLAS, and CUDA [00:07:23]. This complexity leads to "dependency hell" during installation and makes bug tracing extremely difficult [00:07:53].

[[Simplifying machine learning libraries through search | Luminal]] simplifies this by directly generating CUDA code [00:08:24]. The stack is simply: [[Simplifying machine learning libraries through search | Luminal]] library, graph, compilers, and CUDA [00:08:29].

### The Challenge of ML Compilers
The complexity of compilers scales exponentially with the complexity of the code they need to generate (e.g., square or cube) [00:09:07]. This bottleneck has hindered the development of ML compilers and hardware startups [00:09:31].
Hardware trends also contribute to this challenge:
*   **CPUs**: Complex, attempting to predict programmer intent, leading to slower performance for ML operations [00:10:04].
*   **GPUs**: Simpler than CPUs, requiring more explicit programmer control, but offering better performance per watt [00:10:21].
*   **TPUs**: Even simpler, demanding full programmer control over scheduling and memory management, resulting in extremely fast and efficient hardware [00:10:51].
This trend pushes for simpler, faster hardware, which in turn demands more complex software and compilers [00:11:08]. This leads to the Very Large Instruction Width (VLIW) compiler problem: hardware aims for simplicity by having the compiler statically schedule operations, but compilers become too complex for humans to write [00:11:22].

### Solving Compiler Complexity with Search
[[Simplifying machine learning libraries through search | Luminal]] tackles the compiler complexity problem by turning to search, similar to how AlphaGo conquered the game of Go [00:11:57]. Instead of writing a perfect algorithm, Luminal searches through a vast space of logically equivalent GPU kernels to find the fastest one [00:12:42].
*   **E-graphs and Rewrite Rules**: Graphs are converted into expressions using the `egg log` library, which represents the search space efficiently using e-graphs [00:13:15].
*   [[Deep learning compilers and optimization | Luminal]] defines 20-25 simple rewrite rules, each making a small, logically equivalent alteration to a GPU kernel [00:13:34].
*   Iteratively applying these rules builds an extremely large search space of equivalent kernels [00:13:56].
*   The system then profiles the runtime of different kernels within this space and chooses the fastest one [00:14:07]. For very large search spaces, techniques like Monte Carlo tree search are used to prune options [00:14:19].

### Key Optimizations Found by Search
1.  **Kernel Fusion**: This optimization merges multiple operations into a single kernel, significantly reducing data movement between memory and compute units [00:14:45]. Data movement typically accounts for 99% of energy and time spent in GPUs [00:15:23]. By fusing operations, data is loaded once, processed, and written back once, dramatically improving performance [00:15:38].
    *   An unfused graph (left) performs many operations with intermediate memory writes, while a fused graph (right) combines them into one complex kernel [00:15:54]. The fused kernel, despite its complexity, takes little more time than a single unfused kernel [00:16:23].
2.  **Flash Attention**: [[Simplifying machine learning libraries through search | Luminal]]'s search technique successfully discovered Flash Attention, a highly complex algorithm that took the industry five years to find (discovered by Tri Dao in 2022, five years after Transformers in 2017) [00:16:42].
    *   By taking a naive multi-head attention graph, applying simple rewrite rules, and searching, [[Simplifying machine learning libraries through search | Luminal]] can autonomously find Flash Attention [00:17:15].
    *   This is a significant achievement, as [[Simplifying machine learning libraries through search | Luminal]] is currently the only compiler known to achieve this through search [00:17:30].

### Deterministic Optimizations
After the search process generates fast kernels, [[Simplifying machine learning libraries through search | Luminal]] applies deterministic optimizations that are guaranteed to be beneficial:
1.  **Buffer Reuse**: The compiler minimizes memory usage by optimally reusing memory buffers [00:18:37]. Because the entire workload is specified as a graph, the compiler can identify when buffers are not simultaneously needed and assign them to the same memory location [00:18:52].
2.  **Batching and Kernel Issuance**: Instead of the traditional CPU-GPU round trip for each kernel dispatch, [[Simplifying machine learning libraries through search | Luminal]] issues all kernels at once to the GPU [00:19:31]. The GPU then runs through them sequentially, saving significant launch time [00:19:56].

## Training Capabilities
While initially designed for inference, [[Simplifying machine learning libraries through search | Luminal]]'s flexible graph representation allowed for the creation of an external autograd engine [00:20:25]. This external library can derive a backward graph from a forward graph, attach it, and then run it through the same downstream compilers and search process, effectively providing training capabilities for free [00:20:40]. This unique external extension capability allows for external contributors to write their own autograds, gradient charting, or advanced training setups [00:21:06].

## Future Developments and [[luminal_cloud_and_serverless_inference | Luminal Cloud]]
[[Simplifying machine learning libraries through search | Luminal]] has several exciting future plans:
*   **Hardware Support**: Expand support beyond CPU, CUDA, and Metal to include AMD, Tenstorrent, Groq, and TPUs, aiming to democratize ML across diverse hardware [00:21:41].
*   **Distributed Inference and Training**: Implement full 3D distributed capabilities, including data parallel, pipeline parallel, and tensor parallel approaches [00:22:04].
*   **Reinforcement Learning (RL) Acceleration**: Codify RL environments within the [[Simplifying machine learning libraries through search | Luminal]] graph, allowing the environment simulation to be optimized and run on the GPU alongside the model's forward pass, which could dramatically accelerate RL workflows [00:22:17].
*   **[[luminal_cloud_and_serverless_inference | Luminal Cloud]]**: Develop a serverless inference platform [00:23:06]. Users can export their [[Simplifying machine learning libraries through search | Luminal]] model graphs, upload them, and get a serverless inference endpoint [00:23:11]. The cloud handles optimization, batching, queuing, and machine provisioning, with users only paying when their graph is executing [00:23:22]. This aims to deliver the simplest and fastest cloud ML experience [00:23:36].

[[Simplifying machine learning libraries through search | Luminal]] is pushing into territory previously covered by significantly more complex frameworks, with its simplicity enabling faster innovation and reducing overhead [00:23:53].