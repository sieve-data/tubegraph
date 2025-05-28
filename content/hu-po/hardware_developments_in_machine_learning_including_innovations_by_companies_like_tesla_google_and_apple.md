---
title: Hardware developments in machine learning including innovations by companies like Tesla Google and Apple
videoId: t21REMsFJ_4
---

From: [[hu-po]] <br/> 

The landscape of [[hardware_for_ai_training_and_deployment | hardware for AI training and deployment]] is undergoing significant transformation, challenging the long-standing dominance of NVIDIA in the field of machine learning (ML) [01:43:00]. Historically, most machine learning software development has heavily relied on NVIDIA's CUDA and performed best on NVIDIA GPUs [02:11:00]. However, with the arrival of [[advancements_in_pytorch_20_and_its_potential_ability_to_operate_on_various_hardware | PyTorch 2.0]] and OpenAI's Triton, NVIDIA's dominant position, largely due to its software model, is being disrupted [02:32:00]. This shift heralds a new age for deep learning hardware, where companies are increasingly bringing hardware development in-house [01:43:00], [04:13:00].

## The Shifting Bottleneck: From Compute to Memory

Over the last decade, the primary bottleneck in machine learning training has shifted from compute time (waiting for matrix multiplications) to memory bandwidth [03:03:00], [12:03:00], [14:46:00]. NVIDIA's GPUs have seen their computational power (FLOPS) increase by multiple orders of magnitude due to architectural changes like the tensor core and lower precision floating-point formats (e.g., FP16, FP8, and even the beginnings of FP4) [12:13:00], [12:20:00], [12:43:00], [12:59:00].

Despite these advancements, memory bandwidth has not kept pace with the increase in FLOPS [14:35:00], [32:19:00]. This means that GPUs spend a significant portion of their time (up to 40-60%) idle, waiting for data to be transferred between memory caches [11:23:00], [11:53:00], [31:41:00]. Large language models, for example, can require hundreds of gigabytes, if not terabytes, for their model weights alone, further exacerbating memory demands [01:03:00], [17:03:00], [17:09:00].

### The Memory Hierarchy and its Costs
Memory follows a hierarchy, from fast and expensive (on-chip SRAM) to slow and cheap (mechanical hard drives) [21:48:00], [21:55:00].
*   **SRAM (Static RAM):** Found directly on the chip, it's super fast, super expensive, and has tiny capacity [19:17:00], [21:55:00]. Attempting to use huge pools of SRAM for model weights faces issues due to cost and capacity limitations [22:01:00], [22:19:00], [25:39:00]. For instance, a 1 GB SRAM on TSMC's 5nm process would cost hundreds of dollars [25:36:00].
*   **DRAM (Dynamic RAM):** Off-chip memory that is an order of magnitude higher in latency than SRAM but much cheaper [28:35:00], [28:49:00]. However, the cost of DRAM has plateaued since around 2012, no longer following Moore's Law's cost reduction trend [29:14:00], [29:31:00].
*   **HBM (High Bandwidth Memory):** NVIDIA uses HBM, a 3D-stacked DRAM, to achieve massive bandwidth, but it's more expensive (USD 10-20 per GB) due to packaging [30:50:00], [31:00:00].

The increasing cost and stagnant progression of memory relative to compute power highlight the "memory wall," where memory bandwidth and capacity are the limiting factors for high-performance machine learning [29:52:00], [30:29:00].

## In-House Hardware Innovations

The increasing importance of [[ai_algorithms_and_computational_constraints | AI algorithms and computational constraints]] and memory limitations is driving major tech companies to develop their own specialized [[hardware_for_ai_training_and_deployment | hardware for AI training and deployment]]:
*   **Apple:** With their M1 chips, Apple has developed in-house expertise, likely intending to conduct their deep learning on their own silicon [04:19:00], [04:24:00].
*   **Tesla:** Tesla is developing its own Dojo chips specifically for deep learning, primarily for its vision stack [04:27:00], [04:35:00], [45:24:00].
*   **Google:** Google has been a pioneer in custom AI hardware with its Tensor Processing Units (TPUs) [04:39:00]. While their TensorFlow framework lost market share to PyTorch [02:42:00], [03:33:00], Google remains at the forefront of advanced ML models (e.g., Transformers, PaLM, LaMDA) and continues to leverage TPUs for their development [08:18:00], [06:18:00]. Google has also developed a new framework, Jax, which directly competes with TensorFlow and is preferred by some, especially for its handling of parallelism and dynamic shapes [07:42:00], [52:15:00].

This trend of companies developing their own hardware means that model development is increasingly tailored to specific hardware architectures for optimal efficiency [44:44:00], [45:37:00].

## Software Solutions for Hardware Flexibility

The challenge of hardware diversity and the memory wall are being addressed through significant [[open_source_contributions_to_ai_development | open source contributions to AI development]] in the software layer, particularly with [[advancements_in_pytorch_20_and_its_potential_ability_to_operate_on_various_hardware | PyTorch 2.0]] and OpenAI's Triton.

### PyTorch 2.0's Compiler Approach
[[advancements_in_pytorch_20_and_its_potential_ability_to_operate_on_various_hardware | PyTorch 2.0]], now an [[opensource_ai_and_its_implications | open-source AI]] project established and moved out from Meta [48:09:00], introduces a compiled solution that supports graph execution [48:29:00]. This contrasts with PyTorch's original "eager mode," which executed operations line-by-line, causing frequent memory transfers [35:48:00], [36:37:00].

PyTorch 2.0 leverages several key components:
*   **Operator Fusion:** Instead of writing each intermediate result to memory, multiple functions are computed in one pass to minimize memory reads and writes [37:08:00]. This is analogous to compilers in traditional programming languages optimizing code [37:22:00].
*   **PrimTorch:** This reduces the number of PyTorch operators from over 2,000 to a core set of about 250, simplifying the implementation of different non-NVIDIA backends [54:49:00].
*   **TorchDynamo:** This robust compiler ingests any PyTorch script, including those calling third-party libraries, and generates an optimized computational graph [55:27:00], [55:41:00]. It supports partial graph capture, guarded graph capture, and just-in-time recapture, making it more flexible than traditional graph-mode compilers like TensorFlow's [59:19:00].
*   **TorchInductor:** A Python-native deep learning compiler that takes the optimized FX graph (reduced to around 50 core operators) [01:02:41], [01:03:03] and moves to a scheduling phase where operators are fused and memory planning is determined [01:02:48]. It then generates code for various accelerator back-ends like CPUs, GPUs, or other AI accelerators [01:03:34].

### OpenAI's Triton: Bypassing CUDA
OpenAI's Triton is a particularly disruptive innovation that bypasses NVIDIA's closed-source CUDA libraries [01:04:49], [01:05:14]. Triton can take Python code directly or be fed through the PyTorch Inductor stack [01:04:56]. It converts the input to an LLVM intermediate representation and directly generates PTX code for NVIDIA GPUs, avoiding NVIDIA's proprietary CUDA libraries like CUBLAS in favor of [[open_source_artificial_intelligence | open-source artificial intelligence]] equivalents like Cutlass [01:05:04], [01:05:17], [01:05:27].

Triton is crucial because it bridges the gap between high-level languages (like Python) and low-level hardware performance [01:07:52]. Unlike complex CUDA kernels that require deep understanding of hardware architecture, Triton kernels are more legible to typical machine learning researchers [01:06:44], [01:07:58]. It automates memory coalescing, shared memory management, and scheduling, significantly reducing the work required for a compiler team to support a new AI accelerator [01:08:04], [01:08:43].

## Future Implications
The developments in [[applications_in_machine_learning_and_ai | applications in machine learning and AI]], particularly the rise of [[advancements_in_pytorch_20_and_its_potential_ability_to_operate_on_various_hardware | PyTorch 2.0]] and OpenAI Triton, aim to break NVIDIA's competitive advantage in [[the_role_of_cuda_and_tensorflow_in_machine_learning_software_development | CUDA and TensorFlow]] [03:55:00], [05:33:00]. This allows the software that runs models on NVIDIA GPUs to transfer seamlessly to other hardware with minimal effort [04:27:00].

As [[challenges_and_innovations_in_ai_model_architecture_and_scaling | challenges and innovations in AI model architecture and scaling]] continue, the economics of the chip solution will become a bigger driver of hardware purchases than the ease of use previously afforded by NVIDIA's software [04:46:00]. The market for [[hardware_for_ai_training_and_deployment | hardware for AI training and deployment]] is becoming more open, with numerous companies attempting to become leaders in machine learning hardware [04:20:00], [04:22:00], [04:54:00], [04:58:00]. This increased competition and the standardization around [[open_source_contributions_to_ai_development | open source contributions to AI development]] like Triton could lead to a more diversified ecosystem of AI hardware solutions [01:11:05], [01:11:22].