---
title: quantization and optimization in machine learning
videoId: nTdJEQLday0
---

From: [[hu-po]] <br/> 

[[quantization in large language models | Quantization]] and optimization are crucial techniques for managing the computational demands of large machine learning models, particularly [[Quantization for large language models | Large Language Models (LLMs)]]. These methods aim to reduce memory footprint and improve training efficiency, making models more accessible and deployable <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

## [[quantization in large language models | Quantization]]
[[quantization in large language models | Quantization]] refers to the process of storing numerical parameters of a machine learning model at different precisions <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This means reducing the number of bits used to represent each parameter, leading to a smaller memory footprint for the model <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

### Precision Levels
*   **Full Precision (Float32):** Uses 32 bits to store a single number. A model with 1 billion parameters requires 4 gigabytes (GB) in float32 precision <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. A 20 billion parameter model would require 80 GB <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **Half Precision (Float16):** Uses 16 bits, halving the memory requirement compared to float32 <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. A 20 billion parameter model would fit in 40 GB <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **Integer Quantization (Int8):** Uses 8 bits per weight, further reducing memory. A 20 billion parameter model can fit in 20 GB using Int8 <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **4-bit Quantization:** This is the current limit, storing each parameter in just 4 bits of information <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. A 20 billion parameter model would require only 10 GB <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

### Performance Degradation and Mitigation
Reducing precision through [[quantization in large language models | quantization]] can lead to performance degradation, as the accuracy of the model's calculations is reduced <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. To address this:

*   **[[2bit quantization for machine learning models | 8-bit Matrix Multiplication (LLM.int8)]]:** This method, introduced in the paper "LLM.int8()", solves the performance degradation issue in [[Quantization for large language models | large language models]] by breaking down matrix multiplications into two stages <a class="yt-timestamp" data-t="03:57:00">[03:57:07]</a>:
    *   "Outlier hidden states" are performed in float16 <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
    *   "Non-outlier" parts are performed in int8 <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
    This intelligent use of different data types helps save memory while preserving performance <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

## [[Optimization Methods in Machine Learning | Optimization]] in Machine Learning
[[Optimization Methods in Machine Learning | Optimization]] in machine learning refers to the techniques and algorithms used to efficiently train models by adjusting their parameters to minimize a loss function or maximize a reward <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>, <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>.

### Key Concepts in Training
*   **Gradients:** During [[finetuning machine learning models | fine-tuning]], gradients are "pushed" into the [[quantization in large language models | large language model]], modifying its parameters <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>. This is distinct from in-context learning or prompt engineering, which do not alter model parameters <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.
*   **Optimizers:** Algorithms like AdamW are popular optimizers used to manage how gradients update model weights <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **GPU Memory:** Larger models require more GPU memory. For instance, a 20 billion parameter model in full precision requires 80 GB of GPU memory, which no consumer GPU provides <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. High-end consumer GPUs (e.g., Nvidia 4090) typically have 24 GB of memory <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>, while enterprise-grade GPUs like the A100 have 80 GB <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

### Parallelism Strategies for Scaling
When training models in a parallel way across multiple compute nodes (GPUs), various parallelism strategies are employed:

*   **Data Parallelism:** The same model is replicated on several machines, and each instance is fed a different batch of data <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This is the most straightforward strategy <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.
*   **Model Parallelism (Pipeline and Tensor Parallelism):** The model itself is distributed across multiple machines <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
    *   **Pipeline Parallelism:** Splits the model layer-wise across GPUs <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.
    *   **Tensor Parallelism:** Splits tensor operations within layers across GPUs <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **Sharding:** The process of breaking down a large blob of data (like model weights) into smaller blobs to be sent to different machines <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. This requires defining complex communication protocols <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

### Techniques for Reduced Memory and Efficient [[finetuning machine learning models | Fine-Tuning]]
*   **Freezing Pre-trained Weights:** A common technique in [[finetuning machine learning models | fine-tuning]] where a large portion of a model's pre-trained weights are frozen, preventing gradients from changing their values <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. This significantly reduces computation during [[finetuning machine learning models | fine-tuning]] and the size of the updated model that needs to be distributed <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
*   **Low-Rank Adaptation (LoRA) / PEFT:** A method that allows [[finetuning machine learning models | fine-tuning]] of [[Quantization for large language models | LLMs]] by freezing most pre-trained weights and creating low-rank versions of query and value layer attention matrices <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>. These low-rank matrices have far fewer parameters than the original model, enabling [[finetuning machine learning models | fine-tuning with quantized models | fine-tuning with less GPU memory]] <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. The PEFT (Parameter-Efficient Fine-Tuning) library by Hugging Face supports the creation and [[finetuning machine learning models | fine-tuning]] of these adapter layers <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **Adaptive Activation Checkpointing and Fused Kernels:** Advanced techniques to optimize memory usage and speed <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. Fused kernels combine multiple mathematical operations into a single, optimized GPU kernel, reducing overhead <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

## [[Quantization for large language models | Quantization]] and [[Optimization Methods in Machine Learning | Optimization]] in RLHF
Reinforcement Learning from Human Feedback (RLHF) utilizes these techniques for [[finetuning machine learning models | fine-tuning]] [[Quantization for large language models | LLMs]] like ChatGPT <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The process typically involves:
1.  **Supervised [[finetuning machine learning models | Fine-tuning]]:** An [[Quantization Techniques for Transformers | LLM]] is initially [[finetuning machine learning models | fine-tuned]] on human demonstrations and instructions <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.
2.  **Reward Model Training:** A separate reward model is trained using human-annotated comparison data, where human labelers rank different model outputs <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. This reward model (a value function) predicts how "good" a model's answer is for a given prompt <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.
3.  **RL-based [[finetuning machine learning models | Fine-tuning]]:** The [[Quantization for large language models | LLM]] is then further [[finetuning machine learning models | fine-tuned]] using the trained reward model and an RL algorithm, commonly [[second_order_optimization_in_machine_learning | Proximal Policy Optimization (PPO)]] <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. PPO is a widely used and relatively simple RL algorithm <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

In this context, [[finetuning with quantized models | fine-tuning with quantized models]] and low-rank adapters allows for training even 20 billion parameter models on a single 24 GB consumer GPU <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>, although a more robust training environment might use an A100 GPU with 80GB of memory <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.