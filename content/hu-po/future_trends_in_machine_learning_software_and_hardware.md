---
title: Future trends in machine learning software and hardware
videoId: t21REMsFJ_4
---

From: [[hu-po]] <br/> 

The landscape of machine learning (ML) software development has seen significant changes over the last decade, with many frameworks relying heavily on NVIDIA's CUDA and performing best on NVIDIA GPUs <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. However, the arrival of PyTorch 2.0 and OpenAI's Triton is challenging NVIDIA's dominant position, mainly due to its software model <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. This shift may herald a new age for [[developments_in_deep_learning_hardware | deep learning hardware]] <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Evolution of ML Frameworks: PyTorch vs. TensorFlow

A few years ago, the ML framework ecosystem was fragmented, with TensorFlow initially being a frontrunner and holding around 40% market share <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. Google appeared poised to control the ML industry, leveraging TensorFlow and its successful AI application-specific accelerator, the TPU <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.

However, PyTorch has largely won the framework race <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. By 2020, PyTorch's mention rate at ML conferences reached nearly 70-80%, up from about 10% in 2017 <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>. This was primarily due to PyTorch's increased flexibility and usability compared to TensorFlow <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>. TensorFlow's graph-based approach, similar to a compiled language, made debugging challenging, whereas PyTorch's Python-like eager execution allowed for line-by-line execution and easier debugging <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>, <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>, <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>. Most recent generative AI models are based on PyTorch <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.

Google is now somewhat isolated due to its preference for its own software stack and hardware (TPUs) over PyTorch and NVIDIA GPUs <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. Google also has another framework, Jax, which competes directly with TensorFlow <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.

## The Memory Wall in ML Training

Machine learning model training time is dominated by two components: compute and memory <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. In the past, compute time (waiting for matrix multiplies) was the dominant factor <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>. However, as NVIDIA GPUs developed with architectural changes like tensor cores and lower precision floating-point formats (e.g., FP16, FP8, and even FP4), compute speed has rapidly outpaced memory bandwidth <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>, <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>.

[!NOTE|Memory Bottleneck]
GPUs are now largely memory-bound, meaning they spend the majority of time waiting for data to move between different memory caches (e.g., from RAM to GPU RAM, then to L2, L1 caches, and registers) rather than performing calculations <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>, <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>. For example, matrix multiplication utilization is often only around 40% because of this waiting <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>.

The memory hierarchy, from fast, expensive, and small-capacity CPU caches to slow, cheap, and large mechanical hard drives, highlights the cost of placing more memory closer to compute <a class="yt-timestamp" data-t="18:55:00">[18:55:00]</a>, <a class="yt-timestamp" data-t="19:00:00">[19:00:00]</a>. SRAM, often used for on-chip memory, is very expensive, and even large quantities (like 40GB on Cerebras chips) are insufficient for modern 100-billion-parameter models <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>, <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>. DRAM, while cheaper, introduces higher latency <a class="yt-timestamp" data-t="28:40:00">[28:40:00]</a>. Moore's Law, which historically decreased DRAM costs, has plateaued since 2012 <a class="yt-timestamp" data-t="28:58:00">[28:58:00]</a>, <a class="yt-timestamp" data-t="29:14:00">[29:14:00]</a>.

For instance, from NVIDIA's 2016 P100 to 2022 H100 GPUs, memory capacity increased 5x, but FP16 performance increased 46x, exacerbating the memory bottleneck <a class="yt-timestamp" data-t="29:57:00">[29:57:00]</a>. This "memory wall" means that despite higher theoretical flops, GPUs achieve low utilization without heavy optimization <a class="yt-timestamp" data-t="31:13:00">[31:13:00]</a>.

## Addressing the Memory Wall and NVIDIA's Dominance

### Operator Fusion
One principal optimization method for models executing in eager mode is **operator fusion** <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>. Instead of writing each intermediate result to memory, multiple functions are computed in one pass to minimize memory reads and writes <a class="yt-timestamp" data-t="37:09:00">[37:09:00]</a>. This is analogous to how compilers optimize code, reducing the back-and-forth between memory and compute cores <a class="yt-timestamp" data-t="37:22:00">[37:22:00]</a>. PyTorch natively incorporated many fused operators, growing to over 2,000 operators to improve performance and usability <a class="yt-timestamp" data-t="41:09:00">[41:09:00]</a>.

### PyTorch 2.0 and Its Components
PyTorch 2.0, released in March 2023, is a significant development <a class="yt-timestamp" data-t="48:21:00">[48:21:00]</a>. Its primary difference is the addition of a **compiled solution that supports graph execution** <a class="yt-timestamp" data-t="48:29:00">[48:29:00]</a>, a shift that makes proper utilization of various hardware resources much easier <a class="yt-timestamp" data-t="48:37:00">[48:37:00]</a>. PyTorch 2.0 boasts an 86% performance improvement for training on NVIDIA A100 GPUs and 26% for CPU inference <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>. These benefits could extend to GPUs and accelerators from AMD, Intel, and other hardware companies <a class="yt-timestamp" data-t="49:04:00">[49:04:00]</a>.

Key components of PyTorch 2.0:
*   **Prim Torch**: Reduces the over 2,000 PyTorch operators down to 250 primitive operators, making it simpler and more accessible to implement different non-NVIDIA backends <a class="yt-timestamp" data-t="54:49:00">[54:49:00]</a>.
*   **Torch Dynamo**: Ingests any PyTorch user script, including those calling third-party libraries, and generates a computational graph <a class="yt-timestamp" data-t="55:41:00">[55:41:00]</a>. Dynamo can lower complex operations to the 250 primitive operations <a class="yt-timestamp" data-t="56:02:00">[56:02:00]</a>. It enables partial graph capture, guarded graph capture, and just-in-time recapture, making compilation more flexible and user-friendly compared to traditional graph-mode execution <a class="yt-timestamp" data-t="59:19:00">[59:19:00]</a>.
*   **Torch Inductor**: A Python-native deep learning compiler that takes the FX graph from Dynamo and generates fast code for multiple accelerator backends <a class="yt-timestamp" data-t="01:02:14:00">[01:02:14:00]</a>. Inductor performs operator fusion and memory planning, further optimizing the computation <a class="yt-timestamp" data-t="01:02:48:00">[01:02:48:00]</a>.

### OpenAI Triton
OpenAI's Triton is highly disruptive to NVIDIA's closed-source CUDA software stack <a class="yt-timestamp" data-t="01:04:49:00">[01:04:49:00]</a>. Triton takes Python input (often fed through the PyTorch Inductor stack) and directly generates PTX code for NVIDIA GPUs, *skipping NVIDIA's closed-source CUDA libraries* like cuBLAS in favor of open-source alternatives like Cutlass <a class="yt-timestamp" data-t="01:05:06:00">[01:05:06:00]</a>, <a class="yt-timestamp" data-t="01:05:14:00">[01:05:14:00]</a>.

Triton bridges the gap by enabling higher-level languages to achieve performance comparable to lower-level languages, making kernels legible to typical ML researchers <a class="yt-timestamp" data-t="01:07:52:00">[01:07:52:00]</a>. This dramatically reduces the time needed to build an AI compiler stack for new hardware, thereby opening up the market for custom AI hardware and ASICs <a class="yt-timestamp" data-t="01:08:40:00">[01:08:40:00]</a>.

## Impact on Hardware Landscape

Companies like Apple (M1 chips), Tesla (Dojo chips), and Google (TPUs) are increasingly developing their own in-house hardware for deep learning <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. This trend is driven by the need to optimize models directly for specific hardware to achieve greater efficiency in training and inference <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

The developments in PyTorch 2.0 and Triton are making the software stack more portable to different hardware <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>, enabling competition among hardware vendors beyond NVIDIA <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. Many companies like AMD, Intel, Tenstorrent, Luminous Computing, Amazon, Microsoft, Marvel, Meta, Graphcore, Cerebras, and SambaNova are entering the [[developments_in_deep_learning_hardware | machine learning hardware]] space <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>, <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

The challenge for AI hardware startups designing ASICs is that the ML model architectures themselves change rapidly (e.g., from ConvNets to Transformers), making it difficult for hardware designs, which take years, to keep up with the moving target <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## Future Outlook

The default software stack for machine learning models will no longer solely rely on closed-source CUDA <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. The ecosystem, driven by OpenAI and Meta, has built its own tools due to NVIDIA's prior failures with proprietary solutions <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.

There is a convergence towards a hybrid approach in ML framework design. Both Jax (from Google) and PyTorch 2.0 are moving towards a model where initial execution is eager, but the system automatically compiles and optimizes a computational graph for subsequent runs <a class="yt-timestamp" data-t="01:00:53:00">[01:00:53:00]</a>. This approach balances the flexibility of eager mode with the performance benefits of compilation.

As model architectures stabilize (though this is debated, with some predicting continued sharp turns in architectures) and abstractions from PyTorch 2.0, OpenAI Triton, and MLOps firms become standard, the architecture and economics of chip solutions will become the biggest drivers for purchase, rather than the ease of use provided by NVIDIA's software <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>, <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. This signals a more open market for [[developments_in_deep_learning_hardware | AI hardware]] moving forward <a class="yt-timestamp" data-t="01:12:07:00">[01:12:07:00]</a>.