---
title: Quantization and memory optimization in deep learning
videoId: nTdJEQLday0
---

From: [[hu-po]] <br/> 

Deep learning models, especially large language models (LLMs), require significant computational resources and memory due to their vast number of parameters [00:00:58]. Managing these resources efficiently is crucial for training and deploying these models.

## Impact of Model Size on Memory
Machine learning models have different sizes, referring to the number of parameters they contain [00:01:04]. For instance, a "20B" model indicates it has 20 billion parameters [00:00:58]. The larger the model, the more memory it requires on a GPU (Graphics Processing Unit) to fit it [00:01:37]. A 24 gigabyte GPU, while not casual and costing over a thousand dollars, is still considered a consumer GPU; machine learning research often uses A100 GPUs, which are significantly more powerful [00:01:49].

A general rule of thumb for GPU memory usage is that to load a model, each billion parameters costs four gigabytes in float32 precision [00:29:22]. Therefore, a 20-billion parameter model in float32 precision would require 80 gigabytes of memory, which is too large for consumer GPUs [00:45:01].

## Precision and [[quantization_in_machine_learning_models | Quantization]]
Precision refers to how many bits are used to store a single number, which in turn affects the memory footprint of a model's parameters [00:16:41].
*   **Float64:** Uses 64 bits of information to store a single number [00:17:00].
*   **Float32:** Uses 32 bits, half the memory of float64 [00:17:12]. This is the most common data type [00:28:58].
*   **Float16 / BFloat16:** Uses 16 bits, halving the memory of float32 [00:17:20]. A 20-billion parameter model in float16 would require 40 gigabytes [00:45:21].
*   **Int8:** Uses 8 bits [00:29:16]. Storing a 20-billion parameter model as int8 reduces memory to 20 gigabytes [00:45:30].
*   **4-bit:** Research is ongoing to store numbers in just four bits, which would allow a 20-billion parameter model to fit in 10 gigabytes, making it accessible to a much broader array of consumer GPUs [00:17:26, 00:45:49].

[[quantization_in_machine_learning_models | Quantization]] is the process of taking these larger floating-point data types and making them smaller (e.g., from 32-bit to 8-bit) to enable faster and cheaper operations [00:36:45].

## [[impact_of_quantization_on_model_performance | Impact of Quantization on Model Performance]]
Reducing the precision of parameters through [[quantization_techniques_in_machine_learning | quantization]] can lead to [[impact_of_quantization_on_model_performance | performance degradation]] [00:36:57]. This is because less precise numbers (like using 3.14 for Pi instead of 100 decimal places) can lead to less accurate final results [00:37:12].

## [[quantization_techniques_in_machine_learning | Quantization Techniques in Machine Learning]]
One technique to mitigate performance degradation while still benefiting from reduced memory is **8-bit matrix multiplication** [00:36:16]. This method, introduced in the "LLM.int8()" paper, addresses the performance issue by breaking down matrix multiplications into two stages [00:38:27]:
*   **Outlier Hidden States:** Performed in float16 precision.
*   **Non-Outlier Part:** Performed in int8 precision [00:38:08].
This intelligent use of mixed precision helps save memory while maintaining performance [00:39:15].

## Other Memory Optimization Techniques
### Freezing Weights and Low-Rank Adaptation (LoRA)
Fine-tuning a large language model usually involves pushing gradients to change the values of all its weights [00:40:14]. However, a technique called **freezing weights** allows only a portion of the model's weights to be updated, leaving the majority unchanged [00:40:28]. This saves computation time by avoiding gradient calculations for frozen weights [00:40:28].

**Low-Rank Adaptation (LoRA)**, introduced in a 2021 paper, builds on this by freezing the pre-trained weights and creating low-rank versions of the query and value layer attention matrices within the Transformer architecture [00:39:39, 00:41:03]. These low-rank matrices have significantly fewer parameters than the original model, enabling fine-tuning with less GPU memory [00:41:31]. The original frozen weights are augmented by a low-rank adapter [00:42:05]. This approach drastically reduces the number of trainable weights [00:48:57].

### Parameter Efficient Fine-Tuning (PEFT)
The Hugging Face library PEFT (Parameter Efficient Fine-Tuning) supports the creation and fine-tuning of these adapter layers on LLMs [00:43:24]. It allows for loading models in 8-bit precision by simply adding `load_in_8bit=True` when calling the `from_pretrained` method [00:46:11]. PEFT also enables using the same model to get both "reference" and "active" logits (outputs) by deactivating adapters, thus avoiding the need for two separate model copies in memory during reinforcement learning training [00:50:45].

### Fused Kernels
When mathematical concepts in a model architecture are converted into GPU-executable code (kernels), there's an opportunity for optimization [00:34:50]. If multiple mathematical operations or layers are doing similar things in sequence, they can be combined into a single "fused kernel" [00:35:36]. This reduces overhead and can lead to significant speedups, although implementing it requires highly skilled engineers [00:35:45].

## Scaling Training: Distributed Training
Training large models at scale often requires distributed computing across multiple GPUs or machines [00:29:39]. This involves various parallelism strategies:

*   **Data Parallelism:** The most straightforward strategy. The same model is replicated on several machines, and each instance is fed a different batch of data [00:30:25, 00:32:25].
*   **Model Parallelism:** The model itself is split and distributed across many machines [00:30:45, 00:32:38].
    *   **Pipeline Parallelism:** Splits the model layer-wise [00:32:45].
    *   **Tensor Parallelism:** Splits tensors (operations) across GPUs within a layer [00:32:49].
*   **Sharding:** The process of taking one large blob of data and dividing it into smaller blobs to be sent to different machines [00:32:23].
*   **Communication Protocols:** Distributed training requires complex communication protocols between machines to share model weights and gradients [00:33:36]. This can be a significant challenge, as bottlenecks can arise from hardware differences, I/O, or matrix multiplication capabilities [00:33:50].

[!NOTE]
While some demonstrations suggest that training a 20-billion parameter model is possible on a single 24-gigabyte consumer GPU, full training rounds for such models are often undertaken on enterprise-grade GPUs like the Nvidia A100, which have 80 gigabytes of memory [00:53:03, 00:53:26].