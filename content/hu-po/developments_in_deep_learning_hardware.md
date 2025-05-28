---
title: Developments in deep learning hardware
videoId: t21REMsFJ_4
---

From: [[hu-po]] <br/> 

The landscape of [[Deep Learning and Neural Networks | machine learning]] software development has seen significant changes over the last decade, with many frameworks emerging and fading away <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. Historically, most of these frameworks have relied heavily on Nvidia's CUDA and perform best on Nvidia GPUs <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. However, with the advent of PyTorch 2.0 and OpenAI's Triton, Nvidia's dominant position, primarily due to its software, is being disrupted <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. This shift heralds a new era for [[Future trends in machine learning software and hardware | deep learning hardware]] <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## The Rise of PyTorch and In-House Hardware

In recent years, the [[Deep Learning and Neural Networks | machine learning]] framework ecosystem has consolidated, with PyTorch largely winning the "framework race" against Google's TensorFlow <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. While TensorFlow once held a significant market share (around 40%), PyTorch has grown to almost 50% market share by 2022, demonstrating its widespread adoption in research conferences <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.

PyTorch's success is attributed to its increased flexibility and usability compared to TensorFlow <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>. TensorFlow's compiled code language mindset, which involves creating and compiling a graph, contrasts with PyTorch's more Python-like, line-by-line execution workflow, making PyTorch easier to debug <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. The majority of recent generative [[Challenges and Advancements in AI Research | AI models]], including those that have made news, are based on PyTorch <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.

Concurrently, there's a growing trend of companies developing their own in-house [[Future trends in machine learning software and hardware | hardware]] for [[Deep Learning and Neural Networks | deep learning]]:
*   Apple with its M1 chips <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
*   Tesla with its Dojo chips <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   Google with its TPUs (Tensor Processing Units) <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.

This indicates a move away from relying solely on external hardware providers like Nvidia <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

## The Memory Wall: A Shifting Bottleneck

In [[Deep Learning and Neural Networks | machine learning]] model training, there are two primary time components: compute and memory <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. In the past, compute time (waiting for matrix multiplies) was the dominant factor <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>. However, as Nvidia's GPUs have developed, leveraging Moore's Law and architectural changes like tensor cores and lower-precision floating-point formats (e.g., FP16, FP8, FP4), compute speed has rapidly outpaced memory bandwidth <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.

Currently, the majority of time during GPU operations is spent waiting for information to move between memory caches within the GPU hierarchy (global memory, L2, L1, registers) <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. Matrix multiplication utilization is often only around 40% because the system is primarily waiting for memory shuffling <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>.

![GPU progression: flops vs. memory bandwidth](https://i.imgur.com/example.png)
The "flops" (floating-point operations per second) of GPUs have increased significantly more than memory bandwidth (gigabytes per second) from 2016 to 2022 <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>. This means modern GPU performance is now largely limited by memory bandwidth, not computational speed <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>.

Even in 2018, memory-heavy operations like normalization and element-wise operations consumed nearly 40% of a model's runtime despite accounting for significantly fewer flops than tensor contraction (matrix multiplies) <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>. As [[Future directions and potential breakthroughs in AI models | models]] continue to grow in size, requiring hundreds of gigabytes or even terabytes for model weights, the memory bottleneck becomes even more pronounced <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>. For example, large language models and production recommendation networks deployed by Baidu and Meta require dozens of terabytes of memory <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.

### Memory Hierarchy and Cost Constraints

The memory hierarchy in computing ranges from fast, expensive, and tiny capacity memory (like CPU registers and caches) to slow, cheap, and large capacity storage (like hard drives) <a class="yt-timestamp" data-t="19:00:00">[19:00:00]</a>. GPUs, designed for large inputs and outputs in parallel operations, are efficient but face the challenge of bringing enough data close to the compute units <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>.

SRAM (Static RAM), used for nearest shared memory pools on chips, is very fast but extremely expensive <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. Even advanced [[Deep Learning and Neural Networks | machine learning]] ASICs (Application-Specific Integrated Circuits) like Cerebras, with their multi-million dollar wafer-scale chips, struggle to hold massive model weights due to SRAM cost and capacity limitations <a class="yt-timestamp" data-t="22:17:00">[22:17:00]</a>. Nvidia's current A100 GPU has 40 megabytes of SRAM, while the next-gen H100 has 50 megabytes <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.

DRAM (Dynamic RAM), a tightly coupled off-chip memory, is much cheaper than SRAM but has significantly higher latency <a class="yt-timestamp" data-t="28:35:00">[28:35:00]</a>. While DRAM costs followed Moore's law for decades, they have plateaued since 2012 <a class="yt-timestamp" data-t="29:14:00">[29:14:00]</a>. The demands for memory have increased, with DRAM now comprising 50% of total server costs <a class="yt-timestamp" data-t="29:46:00">[29:46:00]</a>.

To achieve the massive bandwidth required for [[Deep Learning and Neural Networks | machine learning]], Nvidia uses HBM (High Bandwidth Memory), which involves 3D stacked layers of DRAM. This is more expensive (around $10-20 per gigabyte) but provides greater bandwidth <a class="yt-timestamp" data-t="30:42:00">[30:42:00]</a>. The Nvidia H100 GPU has a 5x increase in memory capacity over the P100 (2016) but a 46x increase in FP16 performance, further highlighting the growing imbalance <a class="yt-timestamp" data-t="29:57:00">[29:57:00]</a>. This imbalance leads to low flops utilization (e.g., 60% for A100s) as the compute units spend time waiting for data <a class="yt-timestamp" data-t="31:38:00">[31:38:00]</a>.

## Software Innovations to Overcome Hardware Limitations

### Operator Fusion

For eager execution models like PyTorch, where each operation is read from memory, computed, and then sent back to memory before the next operation, memory bandwidth becomes a critical bottleneck <a class="yt-timestamp" data-t="35:48:00">[35:48:00]</a>. A key optimization method is "operator fusion," where multiple functions are computed in one pass to minimize memory reads and writes <a class="yt-timestamp" data-t="37:08:00">[37:08:00]</a>. This is analogous to how compilers optimize code in languages like C++, by analyzing the computational graph and combining operations to reduce back-and-forth data movement <a class="yt-timestamp" data-t="37:22:00">[37:22:00]</a>.

PyTorch has increasingly implemented more fused operators natively, which improves eager mode performance but has ballooned its operator count to over 2,000 <a class="yt-timestamp" data-t="41:07:00">[41:07:00]</a>. This extensive list of operators makes it challenging for [[Future trends in machine learning software and hardware | AI hardware]] startups to fully implement PyTorch for their architectures <a class="yt-timestamp" data-t="43:58:00">[43:58:00]</a>.

### PyTorch 2.0 and its Compiler Stack

PyTorch 2.0, released in March 2023, introduces a compiled solution that supports graph execution, aiming to make it easier to utilize various hardware resources <a class="yt-timestamp" data-t="48:29:00">[48:29:00]</a>. It brings an 86% performance improvement for training on Nvidia's A100 and 26% for inference on CPUs <a class="yt-timestamp" data-t="48:50:00">[48:50:00]</a>. These benefits can extend to other GPUs and accelerators from various companies, fostering competition in the [[Future trends in machine learning software and hardware | hardware space]] <a class="yt-timestamp" data-t="49:04:00">[49:04:00]</a>.

PyTorch 2.0's advancements include:
*   **Better API support for parallelism**: Data parallelism, sharding, pipeline parallelism, and tensor parallelism, which are crucial for splitting large models across multiple GPUs <a class="yt-timestamp" data-t="50:50:00">[50:50:00]</a>.
*   **Native support for dynamic shapes**: Making it easier to handle varying sequence lengths in large language models <a class="yt-timestamp" data-t="00:52:02:00">[00:52:02:00]</a>.

The internal components of PyTorch 2.0's compiler stack are:
*   **PrimTorch**: Reduces the over 2,000 PyTorch operators down to a core set of 250 primitive operations, simplifying the implementation of non-Nvidia backends <a class="yt-timestamp" data-t="54:50:00">[54:50:00]</a>.
*   **Torch Dynamo**: Ingests PyTorch user scripts and generates an optimized graph. It supports partial graph capture, guarded graph capture, and just-in-time recapture, allowing for flexible compilation without users needing to drastically change their code <a class="yt-timestamp" data-t="55:27:00">[55:27:00]</a>. It has been tested on over 99% of 7,000 popular PyTorch models <a class="yt-timestamp" data-t="56:45:00">[56:45:00]</a>.
*   **Torch Inductor**: A Python-native [[Deep Learning and Neural Networks | machine learning]] compiler that takes the FX graph (with 50 primitive operators) from Dynamo, performs operator fusion and memory planning, and generates fast code for various accelerator backends <a class="yt-timestamp" data-t="01:02:14:00">[01:02:14:00]</a>.

### OpenAI Triton: Bypassing CUDA

OpenAI's Triton is a particularly disruptive element <a class="yt-timestamp" data-t="01:04:49:00">[01:04:49:00]</a>. It can take Python directly or feed through the PyTorch Inductor stack, converting the input into an LLVM intermediate representation and generating code <a class="yt-timestamp" data-t="01:04:56:00">[01:04:56:00]</a>. For Nvidia GPUs, Triton directly generates PTX code, *bypassing* Nvidia's closed-source CUDA libraries like cuBLAS in favor of open-source alternatives like Cutlass <a class="yt-timestamp" data-t="01:05:12:00">[01:05:12:00]</a>.

CUDA is typically used by specialists with deep understanding of hardware architecture <a class="yt-timestamp" data-t="01:06:09:00">[01:06:09:00]</a>. Triton bridges this gap, enabling higher-level languages to achieve performance comparable to lower-level languages while being more legible to the typical [[Deep Learning and Neural Networks | machine learning]] researcher <a class="yt-timestamp" data-t="01:07:52:00">[01:07:52:00]</a>. It automates crucial optimizations like memory coalescing and shared memory management <a class="yt-timestamp" data-t="01:08:04:00">[01:08:04:00]</a>.

Triton's open-source nature and growing adoption for various hardware vendors significantly reduce the time needed to build an [[Challenges and Advancements in AI Research | AI compiler]] stack for new hardware <a class="yt-timestamp" data-t="01:08:31:00">[01:08:31:00]</a>. This opens up the market for custom [[Future trends in machine learning software and hardware | AI hardware]] ASICs <a class="yt-timestamp" data-t="01:08:49:00">[01:08:49:00]</a>. Nvidia's lack of focus on usability in their software stack allowed outsiders like OpenAI and Meta to create a portable software solution <a class="yt-timestamp" data-t="01:08:54:00">[01:08:54:00]</a>.

## Conclusion and Future Outlook

The default [[Deep Learning and Neural Networks | machine learning]] software stack is shifting away from closed-source CUDA <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. While Nvidia still holds a significant advantage, the ecosystem is building its own tools due to Nvidia's proprietary limitations <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.

Although [[Future directions and potential breakthroughs in AI models | model architectures]] may continue to evolve rapidly <a class="yt-timestamp" data-t="00:47:06:00">[00:47:06:00]</a>, the development of frameworks like PyTorch 2.0 and tools like Triton will increasingly allow hardware to be swapped out more easily <a class="yt-timestamp" data-t="00:47:37:00">[00:47:37:00]</a>. This means a move towards a unified front-end with a smooth user experience that leverages graph generation and efficient parallelization <a class="yt-timestamp" data-t="01:01:09:00">[01:01:09:00]</a>.

The market for [[Future trends in machine learning software and hardware | deep learning hardware]] is becoming more open and uncertain, potentially leading to new winners emerging beyond Nvidia's traditional dominance <a class="yt-timestamp" data-t="01:10:05:00">[01:10:05:00]</a>. Companies like Google and Tesla are making their own hardware, and there might be a future where various companies develop their own integrated software stacks down to the "metal" <a class="yt-timestamp" data-t="01:11:42:00">[01:11:42:00]</a>.