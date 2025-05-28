---
title: Memory Management and Parallelism in Serving Laura Adapters
videoId: G7FnlVYRUuY
---

From: [[hu-po]] <br/> 

Serving a multitude of fine-tuned models efficiently presents significant challenges in artificial intelligence (AI) inference. Traditional methods often lead to high costs and inefficient resource utilization. Recent advancements, particularly with techniques like Low-Rank Adaptation (LoRA), offer new opportunities for optimization in serving diverse AI models <a class="yt-timestamp" data-t="03:17:50">[03:17:50]</a>.

## The Challenge of Serving Multiple Fine-Tuned Models

When serving models, particularly for different customers or use cases, a common approach is to have a distinct fine-tuned model for each specific need <a class="yt-timestamp" data-t="02:59:01">[02:59:01]</a>. This can lead to a scenario where numerous computers, each with a loaded model, are required, which is costly and inefficient <a class="yt-timestamp" data-t="02:59:05">[02:59:05]</a>. The goal is to serve all variations from a single machine dynamically and compute-efficiently <a class="yt-timestamp" data-t="02:59:01">[02:59:01]</a>.

[[introduction_to_laura_techniques_for_neural_networks | LoRA]] (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that adapts a base model by adding small, low-rank matrices (A and B) to the existing weights <a class="yt-timestamp" data-t="04:02:02">[04:02:02]</a>. This makes fine-tuning cheaper and faster, and allows for "hot-swapping" different LoRAs onto a pre-trained model <a class="yt-timestamp" data-t="05:30:33">[05:30:33]</a>. While LoRA is highly efficient for single-adapter inference, directly merging multiple LoRAs into the base model creates multiple weight copies, leading to missed batching opportunities and increased latency when serving many adapters concurrently <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>.

The concept of [[dynamic_adapter_loading_with_laurax | dynamic adapter loading]], as explored by systems like LoRA X, aims to load only the pre-trained Large Language Model (LLM) weights and then dynamically fetch specific fine-tuned LoRA adapters at runtime <a class="yt-timestamp" data-t="02:53:31">[02:53:31]</a>. This approach minimizes blocking during ongoing requests and significantly reduces the overhead of loading new adapters, making interactive evaluation possible immediately after training <a class="yt-timestamp" data-t="02:59:56">[02:59:56]</a>.

## SLaura: Scalable Serving of Many LoRA Adapters

[[efficient_serving_of_finetuned_models_with_slaura | SLaura]] is a system designed for scalable serving of thousands of concurrent LoRA adapters on a single GPU <a class="yt-timestamp" data-t="03:09:10">[03:09:10]</a>. It addresses the challenges of memory management and parallelism for diverse LoRA adapters.

[!NOTE]
SLaura's core innovation lies in its approach to [[memory_optimization_in_neural_networks | memory management]] and [[ai_model_architecture_and_parallelism_strategies | parallelism strategies]] to enable efficient serving of numerous LoRAs. It improves throughput by up to 4 times and increases the number of served adapters by several orders of magnitude compared to state-of-the-art libraries <a class="yt-timestamp" data-t="03:04:03">[03:04:03]</a>.

### Memory Management with Unified Paging

A significant challenge in serving large models is [[memory_and_computational_efficiency_in_pointbased_methods | memory and computational efficiency]]. Graphics Processing Unit (GPU) memory is fast but limited, while main memory (RAM) is slower but much larger <a class="yt-timestamp" data-t="03:31:06">[03:31:06]</a>. SLaura addresses this by storing all LoRA adapters in main memory and dynamically fetching only the active adapters needed for the current batch to GPU memory <a class="yt-timestamp" data-t="03:14:51">[03:14:51]</a>.

A crucial insight of SLaura is the analogy between dynamic adapter weights and dynamic Key-Value (KV) cache tensors <a class="yt-timestamp" data-t="02:21:51">[02:21:51]</a>.
*   **KV Cache**: In Transformer models (like LLMs), the KV cache stores hidden states of preceding tokens to speed up autoregressive decoding <a class="yt-timestamp" data-t="03:57:34">[03:57:34]</a>. The size of the KV cache fluctuates with the input sequence length <a class="yt-timestamp" data-t="02:22:03">[02:22:03]</a>.
*   **LoRA Weights**: LoRA weights have a dimension of `R` (rank) by `H` (hidden dimension), while KV cache tensors have a dimension of `S` (sequence length) by `H` <a class="yt-timestamp" data-t="02:23:17">[02:23:17]</a>.

The shared `H` dimension between LoRA weights and KV cache tensors is leveraged by SLaura to reduce memory fragmentation <a class="yt-timestamp" data-t="02:23:56">[02:23:56]</a>. SLaura proposes a **unified paging mechanism** that manages both dynamic adapter weights and KV cache tensors within a single memory pool <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a>. This pool uses a fixed page size of `H` elements <a class="yt-timestamp" data-t="02:26:44">[02:26:44]</a>. By storing both in an interleaved and non-contiguous manner within this unified pool, SLaura maximizes GPU memory utilization <a class="yt-timestamp" data-t="02:27:21">[02:27:21]</a>.

### Batching and Parallelism Strategies

SLaura's batching strategy focuses on online and high-throughput serving of many LoRA adapters simultaneously <a class="yt-timestamp" data-t="01:36:36">[01:36:36]</a>. Unlike approaches that merge LoRA weights into the base model for single-adapter inference, SLaura keeps the base model computation separate from individual LoRA computations <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. This allows for greater batching opportunities for the more costly base model operations (`XW`) <a class="yt-timestamp" data-t="01:08:40">[01:08:40]</a>, while the less costly LoRA operations (`XAB`) are performed separately using custom kernels <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.

To achieve this, SLaura employs:
1.  **Heterogeneous Batching**: It optimizes for varying sequence lengths and adapter ranks using highly optimized custom CUDA kernels <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>. These kernels operate directly on non-contiguous memory, aligned with the unified memory pool design <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>. One such kernel is the Multi-size Batched Gather Matrix Matrix Multiplication (MBGMM), implemented in Triton <a class="yt-timestamp" data-t="01:13:11">[01:13:11]</a>.
2.  **Tensor Parallelism**: For multi-GPU inference, SLaura designs a novel tensor parallelism strategy <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>. This strategy minimizes communication costs for the added LoRA computation by scheduling communications on smaller intermediate tensors and fusing larger ones with base model communications <a class="yt-timestamp" data-t="01:15:52">[01:15:52]</a>.
    *   **Communication Overhead**: In [[ai_model_architecture_and_parallelism_strategies | parallel processing]], operations like `all-gather` and `all-reduce` are crucial for exchanging data between GPUs <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>. These can introduce latency if one GPU is a "slowpoke" <a class="yt-timestamp" data-t="01:41:09">[01:41:09]</a>. SLaura's optimization fuses `all-gather` operations with a final `all-reduce`, leveraging the smaller dimension of LoRA matrices (`R` is much smaller than `H`) to reduce total communication time <a class="yt-timestamp" data-t="01:42:56">[01:42:56]</a>.

[!TIP]
The ability to serve multiple LoRA adapters on a single GPU is a game-changer for businesses building AI applications. It drastically reduces inference costs by allowing a single node to serve diverse fine-tuned models, instead of maintaining dedicated infrastructure for each variation <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>. This is critical for startups offering customized fine-tuning services where customers might not have the technical expertise for fine-tuning or serving models themselves <a class="yt-timestamp" data-t="01:03:57">[01:03:57]</a>.

### Request Scheduling and Fairness

SLaura incorporates an iteration-level (token-level) scheduling and batching strategy <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>. This means requests are managed at the level of individual tokens during decoding <a class="yt-timestamp" data-t="01:12:17">[01:12:17]</a>.
To optimize batching, SLaura uses "adapter clustering," prioritizing requests that use the same adapter <a class="yt-timestamp" data-t="01:14:40">[01:14:40]</a>. However, it also balances this with fairness considerations to prevent requests for less popular adapters from experiencing excessive latency <a class="yt-timestamp" data-t="01:16:25">[01:16:25]</a>. An "early abort" admission control strategy is implemented to sustain performance when traffic exceeds system capacity, dropping requests if service level objectives (SLOs) cannot be met <a class="yt-timestamp" data-t="01:17:49">[01:17:49]</a>.

## Performance and Real-World Impact

SLaura demonstrates significant performance improvements. It can serve up to 2,000 adapters simultaneously <a class="yt-timestamp" data-t="01:53:03">[01:53:03]</a> and shows impressive throughput enhancements: up to 4 times higher than VM and 30 times higher than Hugging Face's PFT library <a class="yt-timestamp" data-t="01:53:34">[01:53:34]</a>. These gains are observed in both synthetic and real-world workloads, such as chatbot arena traces <a class="yt-timestamp" data-t="01:54:01">[01:54:01]</a>.

While [[lcmlaura_accelerating_stable_diffusion_models | LCM-LoRA]], a technique to accelerate Stable Diffusion models by distilling consistency model benefits into a LoRA <a class="yt-timestamp" data-t="01:57:30">[01:57:30]</a>, is somewhat distinct, SLaura's underlying principles of efficient [[memory_optimization_in_neural_networks | memory management]] and [[ai_model_architecture_and_parallelism_strategies | parallelism strategies]] could potentially be adapted for such models as well, though it's not currently implemented <a class="yt-timestamp" data-t="02:02:44">[02:02:44]</a>. The core ideas surrounding the efficient handling of multiple, dynamically loaded adapters are broadly applicable across different AI modalities.

The breakthroughs achieved by SLaura, by leveraging insights into memory structure and optimizing low-level operations, demonstrate the significant potential for further advancements in AI model serving, even on existing hardware <a class="yt-timestamp" data-t="01:46:26">[01:46:26]</a>. Future extensions may include support for additional adapter methods, enhanced fused kernels, and the use of multiple CUDA streams to further parallelize base model and LoRA computations <a class="yt-timestamp" data-t="01:55:42">[01:55:42]</a>.