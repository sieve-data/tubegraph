---
title: Dynamic adapter loading for model serving
videoId: G7FnlVYRUuY
---

From: [[hu-po]] <br/> 

Serving a multitude of fine-tuned models to diverse users presents significant challenges for cloud providers and startups aiming to offer customized artificial intelligence services <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>. The traditional approach of loading a separate full model for each specific fine-tuning or use case is inefficient and costly <a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a>. [[comparison_of_full_model_finetuning_and_adapterbased_methods | Adapter-based methods]], particularly Low-Rank Adaptation (LoRA), offer a parameter-efficient way to adapt base models for various tasks <a class="yt-timestamp" data-t="03:19:50">[03:19:50]</a>. Dynamic adapter loading focuses on efficiently managing and deploying these adapters.

## The Problem of Model Serving

When serving models, a key challenge arises from the need to support many fine-tuned versions of a base model, each tailored to different user requests or use cases <a class="yt-timestamp" data-t="00:27:49">[00:27:49]</a>. For example, a single base language model like LLaMA 2 might be fine-tuned with different LoRAs for tasks such as French poetry or German poetry <a class="yt-timestamp" data-t="01:15:44">[01:15:44]</a>.

Traditional serving infrastructure typically preloads all model weights <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>. If each fine-tuned model requires its own dedicated computational instance (e.g., a separate GPU), this quickly leads to high operational costs and underutilization of resources, especially if a specific LoRA is only requested occasionally <a class="yt-timestamp" data-t="02:52:13">[02:52:13]</a>.

## LoRA X: Dynamic Adapter Loading

LoRA X (LoRA Exchange) introduces the concept of [[dynamic_routing_in_language_models | dynamic adapter loading]] to address this problem <a class="yt-timestamp" data-t="02:47:48">[02:47:48]</a>. Instead of preloading all model weights, LoRA X loads only the pre-trained Large Language Model (LLM) weights and then dynamically loads each set of fine-tuned LoRA adapters at runtime <a class="yt-timestamp" data-t="02:52:54">[02:52:54]</a>. This approach aims to prevent blocking under ongoing requests <a class="yt-timestamp" data-t="03:00:01">[03:00:01]</a>.

In the LoRA X system, an individual request queue is maintained per fine-tuned adapter <a class="yt-timestamp" data-t="03:04:04">[03:04:04]</a>. While new fine-tuned model adapter weights are dynamically loaded, associated requests wait in a queue, allowing other requests to proceed <a class="yt-timestamp" data-t="03:10:01">[03:10:01]</a>. The overhead of dynamically loading a new adapter is observed to be around 200 milliseconds, which is typically less than the text generation response time <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. This allows for interactive evaluation of fine-tuned models immediately after [[machine_learning_model_training | training]] <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

## S-LoRA: Scalable Serving of Thousands of Concurrent Adapters

S-LoRA builds on the idea of dynamic adapter loading to serve thousands of concurrent LoRA adapters on a single GPU <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. The system achieves high throughput and efficiency by separating the base model computation from individual LoRA computations <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>, managing memory efficiently, and orchestrating parallelism across multiple GPUs <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

### Key Innovations of S-LoRA

1.  **Unified Paging for Memory Management**:
    S-LoRA stores all LoRA adapters in the main memory (RAM) and fetches only the active adapters needed for the current batch to the GPU memory <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a> <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. This approach leverages the fact that main memory is significantly cheaper and larger than GPU memory (VRAM) <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>.
    A crucial insight of S-LoRA is that dynamic adapter weights are analogous to Dynamic KV caches <a class="yt-timestamp" data-t="01:21:49">[01:21:49]</a>. Both have variable sizes and operations <a class="yt-timestamp" data-t="01:21:57">[01:21:57]</a>. A KV cache tensor has a shape of (Sequence Length, Hidden Dimension) (S, H), and a LoRA weight tensor has a shape of (Rank, Hidden Dimension) (R, H) <a class="yt-timestamp" data-t="01:23:17">[01:23:17]</a>. Since both share the 'H' (Hidden Dimension) <a class="yt-timestamp" data-t="01:23:51">[01:23:51]</a>, they can be stored in a unified memory pool to reduce fragmentation <a class="yt-timestamp" data-t="01:25:56">[01:25:56]</a>. This pool statically allocates a large buffer that manages both dynamic adapter weights and KV cache tensors in a paged manner, where each page corresponds to a vector of H elements <a class="yt-timestamp" data-t="01:26:42">[01:26:42]</a> <a class="yt-timestamp" data-t="01:24:44">[01:24:44]</a>.

2.  **Heterogeneous Batching and Optimized Cuda Kernels**:
    Unlike traditional methods that merge LoRA weights into the base model (efficient for a single adapter but problematic for multiple) <a class="yt-timestamp" data-t="01:06:54">[01:06:54]</a>, S-LoRA keeps the LoRA computations separate <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>. This enables efficient batching of the more costly base model computations (XW operation) across different requests, as the additional LoRA computation (XAB) is substantially lower <a class="yt-timestamp" data-t="01:08:45">[01:08:45]</a>.
    To handle the varying sequence lengths and adapter ranks in batches (heterogeneity), S-LoRA employs custom CUDA kernels <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>. These kernels operate directly on non-contiguous memory, aligning with the unified memory pool design <a class="yt-timestamp" data-t="01:32:50">[01:32:50]</a>. An example is the "Multi-Size Batched Gather Matrix Matrix Multiplication" (MB-GMM) kernel, implemented in Triton, which efficiently batches LoRA computations <a class="yt-timestamp" data-t="01:33:06">[01:33:06]</a>.

3.  **Tensor Parallelism (S-LoRA TP)**:
    For multi-GPU inference, S-LoRA introduces a novel [[challenges_and_solutions_in_model_configuration | tensor parallelism strategy]] for batched LoRA computation <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a> <a class="yt-timestamp" data-t="01:16:21">[01:16:21]</a>. This strategy aims to minimize communication costs for the added LoRA computation by scheduling communications on smaller intermediate tensors and fusing larger ones with communications of the base model <a class="yt-timestamp" data-t="01:35:55">[01:35:55]</a>. The base model uses Megatron-LM tensor parallelism strategy, and S-LoRA aligns the partition strategies of inputs and outputs to the added LoRA computation <a class="yt-timestamp" data-t="01:35:27">[01:35:27]</a>. The efficiency gain comes from the LoRA's low rank (R is very small, e.g., 8 or 64, compared to Hidden Dimension H of 4096 or 8192) <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a> <a class="yt-timestamp" data-t="01:44:55">[01:44:55]</a>, which means communication overhead for LoRA operations is minimal <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

### Scheduling and Performance

S-LoRA adopts an iteration-level (token-level) scheduling and batching strategy <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>. This means requests are scheduled at the token level, with continuous communication between the CPU (main memory) and GPU (VRAM) to load and offload adapter weights and KV caches <a class="yt-timestamp" data-t="01:27:54">[01:27:54]</a>. The system also employs a forward-looking strategy to predict required adapters for the next batch based on the current waiting queue, allowing for prefetching into available memory to reduce I/O time <a class="yt-timestamp" data-t="01:31:55">[01:31:55]</a>.

For handling many adapters, S-LoRA prioritizes batching requests that use the same adapter (adapter clustering) to enhance efficiency <a class="yt-timestamp" data-t="01:14:37">[01:14:37]</a>. An admission control strategy with an "early abort" mechanism ensures that service level objectives (e.g., desired latency) are met by dropping requests if the system capacity is exceeded <a class="yt-timestamp" data-t="01:17:06">[01:17:06]</a>.

S-LoRA demonstrates significant performance improvements:
*   Up to 4 times higher throughput compared to vLLM (a system for efficient memory management for large language models) <a class="yt-timestamp" data-t="01:53:34">[01:53:34]</a>.
*   Up to 30 times higher throughput compared to Hugging Face PEFT (a popular library for parameter-efficient fine-tuning) <a class="yt-timestamp" data-t="01:53:37">[01:53:37]</a>.
*   Can serve up to 2,000 adapters simultaneously on a single GPU <a class="yt-timestamp" data-t="01:53:03">[01:53:03]</a>.

These improvements are achieved through efficient memory management, custom CUDA kernels (like the MB-GMM), and optimized [[integrating_multiple_laura_adapters_with_large_models | tensor parallelism]] <a class="yt-timestamp" data-t="01:55:30">[01:55:30]</a>. The concepts are extensible to other adapter methods and modalities <a class="yt-timestamp" data-t="00:44:57">[00:44:57]</a>.