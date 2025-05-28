---
title: Efficient Serving of FineTuned Models with SLaura
videoId: G7FnlVYRUuY
---

From: [[hu-po]] <br/> 

Serving a multitude of diverse, [[finetuning_machine_learning_models | fine-tuned machine learning models]] presents significant challenges for cloud providers and companies offering AI services. When customers require specific adaptations of a base model, the traditional approach of loading each [[finetuning_pretrained_models_with_minimal_additional_parameters | fine-tuned model]] onto a dedicated server becomes highly inefficient and costly [0:28:40]. SLaura is a system designed to address these challenges by enabling the scalable serving of thousands of concurrent Low-Rank Adaptation (Laura) adapters on a single GPU [0:31:01].

## What is Laura?

Laura, short for Low-Rank Adaptation, is a parameter-efficient [[introduction_to_laura_techniques_for_neural_networks | fine-tuning method]] for neural networks [0:04:02]. It introduces a small, additional pair of matrices (A and B) alongside the original pre-trained model's weights [0:04:15]. Instead of [[finetuning_machine_learning_models | fine-tuning]] the entire original model, only these much smaller Laura matrices are trained [0:05:27]. This approach is significantly cheaper and faster, and it allows for "hot-swapping" or compositing different Laura adapters onto a single pre-trained model [0:05:33]. Laura is not limited to specific neural network types; it can be used for diffusion models (e.g., images) or [[finetuning_language_models_for_specific_tasks | language models]] (e.g., text) [0:04:31].

## [[lcmlaura_accelerating_stable_diffusion_models | LCM Laura]]: A Specialized Application

[[lcmlaura_accelerating_stable_diffusion_models | LCM Laura]] is an example of a specialized Laura application focused on accelerating Stable Diffusion models [0:06:06]. Latent Consistency Models (LCMs) are designed to accelerate text-to-image generation by producing high-quality images with minimal inference steps [0:07:12]. Traditional diffusion models require multiple inference steps, where each step involves a feed-forward pass through the GPU, making generation slow [0:07:51].

[[lcmlaura_accelerating_stable_diffusion_models | LCM Laura]] distills the acceleration benefits of LCMs into a Laura adapter [0:14:08]. This means the "LCM magic" can be applied as a small, pluggable Laura to any existing Stable Diffusion model, enabling faster image generation (e.g., from 10 steps to 2 steps) without requiring a completely new model [0:15:02], [0:19:37]. Furthermore, [[lcmlaura_accelerating_stable_diffusion_models | LCM Laura]] can be combined with other style-specific Lauras, allowing for both accelerated and stylized image generation [0:21:52]. However, indefinitely combining many Lauras can lead to performance degradation as the model moves too far from its original base parameters [0:23:23].

## The Problem: Efficiently Serving Many Fine-Tuned Models

For companies serving fine-tuned models, a core challenge is how to handle numerous customer requests, each potentially requiring a different fine-tuned model [0:27:49]. Loading each unique fine-tuned model onto a separate machine is resource-intensive [0:28:43]. The goal is to efficiently serve every type of Laura dynamically from a single computer [0:28:58].

Traditional serving methods often involve preloading all model weights or dynamically loading and unloading adapters [0:29:48]. While merging a single Laura into the base model can offer low latency, this approach leads to multiple weight copies and missed batching opportunities when serving many adapters concurrently [1:02:08]. The constant adding and subtracting of Laura weights on the fly is also inefficient due to communication overhead [1:03:04], [1:42:08].

Another significant memory challenge for [[large_language_models_as_optimizers | large language models]] is the Key-Value (KV) cache [0:39:56]. The KV cache stores the hidden states of previous tokens during auto-regressive decoding, which is essential for efficient generation but consumes substantial GPU memory [0:57:32], [0:43:16]. Since KV cache sizes vary with input sequence lengths, and new ones are allocated per request, this leads to memory fragmentation and IO overhead [0:39:45], [1:22:48].

## SLaura's Innovative Solutions

SLaura proposes several innovations for scalable Laura serving, aiming for high [[performance_and_efficiency_in_machine_learning_models | performance and efficiency]] [0:31:09], [0:55:00].

### Separated Batched Computation
SLaura's core insight is to separate the computation of the base model from the individual Laura computations [1:03:30]. Unlike previous methods that merge Laura weights into the base model, SLaura performs the base model's forward pass (XW) and the Laura adapter's computation (XBA) separately [1:03:42], [2:01:11]. This allows for efficient batching of the more costly base model computation across all requests, regardless of their specific Laura [1:08:47]. The smaller Laura computations are then added back at the end [1:04:09], [2:01:32].

### Unified Paging for Memory Management
SLaura introduces "unified paging" to manage dynamic adapter weights and KV cache tensors within a single, unified memory pool [0:37:37], [1:21:42]. This innovation stems from the crucial observation that both KV cache tensors and Laura weights share a common dimension: the hidden dimension (H) [1:23:51].
*   A KV cache tensor has a shape of `S` (sequence length) by `H` (hidden dimension) [1:23:17].
*   A Laura weight has a shape of `R` (rank) by `H` (hidden dimension) [1:23:41].
Because of this shared `H` dimension, SLaura can treat both as "pages" within a unified memory pool, allowing them to be stored in an interleaved and non-contiguous manner [1:24:24], [1:27:26]. This design reduces memory fragmentation and allows for better utilization of GPU memory, especially when dealing with variable sizes of KV caches and adapter ranks [1:24:58]. SLaura stores all adapters in the main memory (RAM) and fetches only the active adapters needed for the current batch to the faster, but smaller, GPU memory [0:31:14], [1:11:22]. This leverages the cheaper main memory for larger storage while keeping frequently accessed data close to the processor.

### Heterogeneous Batching and Custom CUDA Kernels
To efficiently handle varying sequence lengths in KV caches and different Laura ranks, SLaura employs highly optimized custom CUDA kernels [0:34:59]. These kernels, such as "multi-size batched gather Matrix Matrix multiplication (MB-GMM)," operate directly on non-contiguous memory [1:32:54]. This low-level optimization is crucial because standard matrix multiplication (GEMM) kernels often require significant padding for heterogeneous data, leading to poor hardware utilization [1:09:37], [1:10:53]. By custom-tailoring these kernels, SLaura avoids such inefficiencies.

### Novel Tensor Parallelism Strategy
For multi-GPU inference, SLaura introduces a novel tensor parallelism strategy [0:53:50], [1:34:14]. Tensor parallelism splits parts of the model across multiple GPUs to reduce memory usage and latency [1:34:36]. SLaura's approach minimizes communication costs for the added Laura computation by aligning partition strategies and scheduling communications on small intermediate tensors, fusing them with larger communications of the base model [0:53:55], [1:42:04]. This prevents a single GPU from becoming a "slowpoke" that holds up the entire system due to communication overhead [2:02:54].

### Request Scheduling and Admission Control
SLaura adopts an iteration-level, token-based scheduling strategy [1:12:11]. This means requests are managed at the level of individual tokens during decoding, allowing for fine-grained control over resource allocation [1:12:44]. The system also includes an "early abort" admission control strategy [1:17:49]. This allows SLaura to estimate which requests can be served within a desired latency (Service Level Objective, SLO) and prioritize them, maintaining fairness across different user requests [1:17:16].

## Performance and Efficiency Gains

SLaura demonstrates significant [[performance_and_efficiency_in_machine_learning_models | performance and efficiency]] improvements, particularly for [[efficiency_of_large_language_models | large language models]]. Compared to state-of-the-art libraries like Hugging Face's PFT and vLLM, SLaura can improve throughput by up to 4 times and increase the number of served adapters by several orders of magnitude [0:36:03], [1:53:34]. SLaura can serve up to 2,000 adapters simultaneously on a single GPU [1:53:03]. This is a substantial leap from systems that might only serve a handful of adapters [1:53:20]. These gains are observed across both synthetic and real-world workloads, even when using multiple GPUs [1:54:24].

## Conclusion

SLaura represents a major advancement in the efficient serving of [[finetuning_and_training_curriculums_in_ai_models | fine-tuned]] AI models, especially for large language models with numerous Laura adapters. By intelligently managing memory through unified paging, optimizing computations with custom CUDA kernels, employing novel tensor parallelism, and implementing sophisticated scheduling, SLaura makes large-scale customized [[finetuning_machine_learning_models | fine-tuning]] services feasible and cost-effective [1:55:23]. This approach paves the way for more accessible and tailored AI applications by reducing the infrastructure burden.