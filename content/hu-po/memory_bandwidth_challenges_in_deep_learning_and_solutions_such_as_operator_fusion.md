---
title: Memory bandwidth challenges in deep learning and solutions such as operator fusion
videoId: t21REMsFJ_4
---

From: [[hu-po]] <br/> 

The landscape of machine learning (ML) software development has seen significant changes, particularly with a shift in focus from raw compute power to memory bandwidth as the primary bottleneck in training and inference of large models <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Historically, deep learning models heavily relied on leveraging NVIDIA's CUDA, performing best on NVIDIA GPUs <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. However, advancements like PyTorch 2.0 and OpenAI's Triton are beginning to challenge NVIDIA's dominance, largely due to their software advancements that address these memory challenges <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## The Memory Wall

Over the last decade, as NVIDIA's GPUs have rapidly developed, the dominant factor limiting ML training time has shifted from compute time (matrix multiplies) to memory time <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. While NVIDIA's FLOPs (floating point operations per second) have increased by multiple orders of magnitude through architectural changes like tensor cores and lower precision floating-point formats (e.g., FP16, FP8, and the emerging FP4), memory bandwidth has not kept pace <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a> <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a> <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

This disparity means that GPUs spend a significant amount of time waiting for data to be transferred between different levels of the memory hierarchy, rather than performing computations <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. In 2018, operations such as normalization and element-wise operations consumed nearly 40% of a model's runtime, despite performing significantly fewer FLOPs than matrix multiplies, indicating they were memory-bound <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a> <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.

### Memory Hierarchy and Costs
Memory follows a hierarchy, from fast and expensive (closest to the processor) to slow and cheap (further away) <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **CPU Cache:** On-chip, super fast, super expensive, tiny capacity (SRAM) <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a> <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
*   **Physical Memory (RAM):** Off-chip, fast, reasonably priced, average capacity (DRAM) <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. DRAM costs plateaued around 2012 <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>.
*   **Solid State Drives (SSDs):** Average speed, reasonably priced, average capacity <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
*   **Mechanical Hard Drives:** Slow, cheap, large capacity <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

To achieve the massive bandwidth required for machine learning, NVIDIA uses **HBM memory** (High Bandwidth Memory), which involves 3D stacked layers of DRAM. This technology is more expensive (10-20 USD per gigabyte) <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.

The increasing gap between compute (FLOPs) and memory bandwidth is evident in NVIDIA's own hardware. From the P100 (2016) to the H100 (2022), memory capacity increased by 5x, but FP16 performance increased by a staggering 46x <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>. This imbalance leads to very low FLOPs utilization without heavy optimization <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. A 60% FLOPs utilization is considered very high, meaning the GPU's tensor cores are idle 40% of the time, waiting for data <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>.

## Impact of Memory Bottlenecks on Model Training

As models continue to grow, with large language models (LLMs) requiring hundreds of gigabytes or even terabytes for weights, [[computational_challenges_in_training_large_models | efficient memory management in AI systems]] becomes critical <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. The majority of time in training large models is spent waiting for data to reach compute units, not on performing matrix multiplies <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

:::info Analogy: CPU vs. GPU
A CPU is like a Ferrari, designed to quickly move individual pieces of cargo, performing varied workloads. A GPU is like a 16-wheeler truck, excellent at moving large amounts of cargo, specialized for simple, parallel operations like multiplications and additions <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
:::

Optimizing [[optimizing_gpu_usage_in_nerf_training | GPU usage in NeRF training]] and other deep learning tasks highlights this issue. Early NeRF implementations, written by ML researchers, were slow. CUDA experts at NVIDIA could re-implement NeRF to be 100 times faster by deeply understanding hardware architecture and optimizing memory movement <a class="yt-timestamp" data-t="01:07:01">[01:07:01]</a>. This deep understanding of hardware architecture is crucial for maximum performance <a class="yt-timestamp" data-t="01:06:46">[01:06:46]</a>.

## Solutions: Operator Fusion

One principal optimization method for models executing in eager mode (like PyTorch originally) is **operator fusion** <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. In eager mode, each operation is read from memory, computed, and then sent back to memory before the next operation <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>. This constant back-and-forth between memory and compute units is slow <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.

Operator fusion combines multiple functions into a single pass to minimize these memory reads and writes <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. Instead of sending intermediate results back to memory, they are kept on-chip and fed directly into the next operation <a class="yt-timestamp" data-t="00:40:11">[00:40:11]</a>. This is analogous to how compiled languages (like C++) optimize code execution compared to interpreted languages (like Python) <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. TensorFlow's graph mode inherently performs this compilation and fusion <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a>.

Over time, PyTorch integrated more native operators that are essentially fused versions of commonly used operations, which improved eager mode performance and reduced the need to write custom CUDA kernels <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>. However, this led to PyTorch ballooning to over 2,000 operators <a class="yt-timestamp" data-t="00:41:29">[00:41:29]</a>.

## Modern Software Stacks: PyTorch 2.0 and Triton

[[advancements_in_pytorch_20_and_its_potential_ability_to_operate_on_various_hardware | Advancements in PyTorch 2.0 and its potential ability to operate on various hardware]] and OpenAI's Triton are critical in addressing these memory challenges and [[challenges_and_future_possibilities_in_neural_network_diffusion | challenges and future possibilities in neural network diffusion]].

### PyTorch 2.0
Released for early testing in January 2023, PyTorch 2.0 adds a compiled solution that supports graph execution <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>. This shift significantly improves performance, showing an 86% improvement for training on NVIDIA's A100 GPUs and 26% for CPU inference <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>. PyTorch 2.0 aims to make it easier to achieve higher FLOPs utilization with less effort <a class="yt-timestamp" data-t="00:49:41">[00:49:41]</a>.

Key components of PyTorch 2.0 include:
*   **PrimTorch:** Reduces the 2,000+ PyTorch operators to a core set of around 250 primitive operators, making it simpler to implement different non-NVIDIA backends <a class="yt-timestamp" data-t="00:54:49">[00:54:49]</a> <a class="yt-timestamp" data-t="00:56:04">[00:56:04]</a>.
*   **TorchDynamo:** Ingests any PyTorch user script, including those calling third-party libraries, and generates an optimized graph. It supports dynamic shapes natively, which is beneficial for varying sequence lengths in LLMs <a class="yt-timestamp" data-t="00:54:49">[00:54:49]</a> <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. Dynamo enables partial graph capture (allowing unsupported constructs to run in eager mode between compiled graph segments) and guarded graph capture (recompiling only when necessary) <a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>.
*   **TorchInductor:** A Python-native deep learning compiler that takes the FX graph (with 50 operators) generated by Dynamo and performs a scheduling phase. This phase fuses operators and determines memory planning to minimize high-level memory cache transfers <a class="yt-timestamp" data-t="01:02:12">[01:02:12]</a> <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>. Inductor then generates wrapper code that runs on CPUs, GPUs, or other AI accelerators, significantly reducing the work for compiler teams building for new hardware <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a> <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>.

### OpenAI Triton
Triton is a key part of Inductor's backend code generation for GPUs <a class="yt-timestamp" data-t="01:04:51">[01:04:51]</a>. It's a highly disruptive technology because it directly generates PTX code for NVIDIA GPUs, *skipping NVIDIA's closed-source CUDA libraries* (like cuBLAS) in favor of open-source alternatives like Cutlass <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.

Triton addresses the complexity of writing efficient CUDA kernels, which traditionally requires a deep understanding of hardware architecture <a class="yt-timestamp" data-t="01:06:44">[01:06:44]</a>. Triton bridges this gap by enabling higher-level languages to achieve performance comparable to lower-level languages, making kernels more legible to ML researchers <a class="yt-timestamp" data-t="01:07:52">[01:07:52]</a>. It automates memory coalescing, shared memory management, and scheduling within streaming multiprocessors <a class="yt-timestamp" data-t="01:08:04">[01:08:04]</a>.

### Implications for the AI Hardware Landscape
The integration of PyTorch 2.0 with Triton and other open-source tools means that the software stack becomes more portable across different hardware platforms. This ability to swap out hardware while keeping the same framework will lead to greater competition in the AI hardware market <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>. Companies like Apple (M1 chips), Tesla (Dojo chips), and Google (TPUs) are already developing their own in-house AI hardware to avoid dependence on third-party vendors like NVIDIA <a class="yt-timestamp" data-t="00:41:19">[00:41:19]</a>.

This shift promises to democratize [[parallelizable_training_and_efficient_inference | efficient inference]] and training by making it easier for new AI hardware companies to build competitive compiler stacks and integrate with widely used ML frameworks <a class="yt-timestamp" data-t="01:08:40">[01:08:40]</a>. The focus is moving towards open software stacks that can run on a variety of hardware, rather than being tied to proprietary solutions <a class="yt-timestamp" data-t="00:53:16">[00:53:16]</a>. This is a significant step towards breaking NVIDIA's CUDA monopoly <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.