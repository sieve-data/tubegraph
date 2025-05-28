---
title: quantization in large language models
videoId: pov3pLFMOPY
---

From: [[hu-po]] <br/> 

[[quantization_in_large_language_models | Quantization]] is a crucial technique in machine learning, particularly for [[Large Language Models and their applications | large language models (LLMs)]], due to its ability to significantly improve model [[efficiency of large language models | efficiency]] in terms of memory and compute <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Understanding its trade-offs and techniques is becoming essential for anyone working in machine learning <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## QLoRA: An Efficient Fine-Tuning Approach
The paper "QLoRA: Efficient Fine-tuning of Quantized LLMs" by Tim Dettmers et al. introduces QLoRA, a method designed to reduce memory usage during the fine-tuning of LLMs <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Tim Dettmers is also known for the bitsandbytes library, which facilitates generic [[quantization and optimization in machine learning | quantization]] for PyTorch code <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The QLoRA repository (artidoro/qlora) provides specific code for [[quantization for large language models | LLM quantization]], particularly for models like LLaMA <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Memory Reduction and Accessibility
QLoRA allows for the fine-tuning of massive models, such as a 65-billion parameter LLaMA model, on a single 48-gigabyte GPU <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This is a dramatic reduction compared to the 780 gigabytes of GPU memory typically required for regular 16-bit fine-tuning of the LLaMA 65B model <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This capability significantly lowers the barrier to entry for LLM fine-tuning, making it accessible on consumer-grade GPUs <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a> <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>. This increased accessibility is considered a major win for the open-source AI community and independent researchers <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.

### Fine-Tuning Strategy
QLoRA's efficiency stems from a specific fine-tuning strategy:
*   **Frozen, Quantized Base Model:** The LLaMA model's weights are "frozen" (not changed during training) and quantized to a 4-bit precision <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a> <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
*   **Low-Rank Adapters (LoRA):** A small, additional "mini-model" called a low-rank adapter (LoRA) is attached to the original model <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Only the parameters within this LoRA adapter are updated via backpropagation <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This significantly reduces the number of trainable parameters <a class="yt-timestamp" data-t="00:53:47">[00:53:47]</a>.
*   **Full 16-bit Performance:** Despite the base model being quantized to 4-bit, QLoRA preserves the full 16-bit fine-tuning task performance <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This implies that the [[Performance and implications of quantized language models | performance degradation]] typically associated with [[2bit quantization for machine learning models | lower precision quantization]] can be recovered <a class="yt-timestamp" data-t="02:08:47">[02:08:47]</a>.

## Innovations of QLoRA
QLoRA introduces several key innovations to achieve its memory savings without sacrificing performance:

### 1. 4-bit NormalFloat (NF4)
This is a new data type designed for [[quantization and optimization in machine learning | quantization]]. It is "information theoretically optimal" for normally distributed weights, meaning it efficiently represents the values commonly found in neural networks <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a> <a class="yt-timestamp" data-t="01:13:57">[01:13:57]</a>.
*   **Quantile Quantization Basis:** NF4 builds on quantile quantization, where each quantization bin holds an equal expected number of values from the input tensor <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. For normally distributed data, this means more bins are concentrated around the mean (zero) and fewer towards the tails <a class="yt-timestamp" data-t="01:06:56">[01:06:56]</a>.
*   **Handling Outliers:** Traditional normalization-based quantization can be inefficient with outliers, as they disproportionately affect the scaling and waste quantization bins <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a> <a class="yt-timestamp" data-t="00:50:19">[00:50:19]</a>. NF4, by assuming a normal distribution, aims to optimize bin allocation.
*   **Exact Zero Representation:** To accurately represent common zero values (like padding), NF4 is an asymmetric data type with a discrete zero point <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.
*   **Empirical Superiority:** NF4 consistently yields better empirical results than standard 4-bit integers and 4-bit floats <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a> <a class="yt-timestamp" data-t="02:05:22">[02:05:22]</a>.
*   **Computation Data Type:** While weights are stored in 4-bit NF4, they are de-quantized to BFloat16 (BF16) for matrix multiplications during both forward and backward passes <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a> <a class="yt-timestamp" data-t="01:40:43">[01:40:43]</a>. BF16 is a 16-bit floating point format with more bits allocated to the exponent than standard FP16, allowing it to represent very small numbers more effectively, which is common in neural network training <a class="yt-timestamp" data-t="01:42:24">[01:42:24]</a>.

### 2. Double Quantization (DQ)
This technique further reduces memory by quantizing the quantization constants themselves <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a> <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>.
*   **Nested Quantization:** When input tensors are chunked for independent quantization (to mitigate outlier impact), multiple quantization constants are generated <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. These constants, initially stored as 32-bit floats, are then quantized to 8-bit floats (FP8) <a class="yt-timestamp" data-t="01:25:52">[01:25:52]</a>.
*   **Memory Savings:** Double quantization saves an average of about 0.37 bits per parameter, amounting to roughly 3 gigabytes for a 65-billion parameter model <a class="yt-timestamp" data-t="01:27:40">[01:27:40]</a>.

### 3. Paged Optimizers
To prevent "out of memory" (OOM) errors during training, especially when processing mini-batches with long sequence lengths, QLoRA uses paged optimizers <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a> <a class="yt-timestamp" data-t="01:02:56">[01:02:56]</a>.
*   **Unified Memory:** This relies on Nvidia Unified Memory, which enables automatic transfer of data pages between CPU RAM and GPU VRAM <a class="yt-timestamp" data-t="01:31:34">[01:31:34]</a>.
*   **Spike Management:** Optimizer states (intermediate values needed for gradient calculation, like in Adam or SGD) can cause memory spikes <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a> <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>. Paged optimizers allocate pageable memory for these states, automatically "evicting" them to CPU RAM when the GPU runs out of memory and bringing them back when needed <a class="yt-timestamp" data-t="01:33:57">[01:33:57]</a>.
*   **Runtime Impact:** For large models (33B and 65B parameters), paged optimizers maintain similar training speeds as regular optimizers, provided the batch size isn't too large <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>.

## Performance and Evaluation
The QLoRA paper conducts extensive ablation studies, training over a thousand models to evaluate its effectiveness <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.
*   **GuanaCo Models:** The best QLoRA model family, named "GuanaCo" (a species similar to a llama), outperforms other openly released models on the Vicuña benchmark, achieving 99.3% of the performance level of ChatGPT <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a> <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Data Quality over Quantity:** The studies reveal that data quality is significantly more important than dataset size for fine-tuning <a class="yt-timestamp" data-t="01:34:45">[01:34:45]</a>. Small, high-quality datasets can lead to state-of-the-art results <a class="yt-timestamp" data-t="01:33:31">[01:33:31]</a>.
*   **LLM Evaluation Challenges:**
    *   **Benchmarking Art:** Measuring model performance remains an "art" with various benchmarks available <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
    *   **GPT-4 as Judge:** GPT-4 is used for automated evaluation of chatbot performance through "tournament-style benchmarking" (ELO ratings) <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a> <a class="yt-timestamp" data-t="02:25:59">[02:25:59]</a>. While this is a cheap alternative to human evaluation, GPT-4 can exhibit biases, such as favoring models appearing first in its prompt <a class="yt-timestamp" data-t="02:41:50">[02:41:50]</a>.
    *   **Human-GPT-4 Agreement:** Human and GPT-4 evaluations largely agree on model rankings, though disagreements exist <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. The fact that GPT-4 is used to judge other LLMs and often ranks itself highest is noted as peculiar <a class="yt-timestamp" data-t="02:22:24">[02:22:24]</a>.
    *   **Benchmark Trustworthiness:** Current chatbot benchmarks are not entirely trustworthy for accurate performance evaluation <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. A single quantifiable score for general models is becoming less useful, suggesting a future with "bags of benchmarks" <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.
    *   **"Lemon Picking":** The paper includes a "lemon picking" analysis, deliberately seeking out instances where the models fail to show their limitations, contrasting with "cherry picking" (showcasing only the best results) <a class="yt-timestamp" data-t="01:53:56">[01:53:56]</a> <a class="yt-timestamp" data-t="02:35:53">[02:35:53]</a>.

## Broader Impacts and Future Directions
QLoRA's advancements have significant implications for the field:
*   **Democratization of LLM Fine-Tuning:** It dramatically increases the accessibility of LLM fine-tuning, allowing the largest publicly available models to be fine-tuned on a single GPU <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. This empowers independent researchers and fosters open-source AI development <a class="yt-timestamp" data-t="02:57:42">[02:57:42]</a>.
*   **Aggressive Quantization:** The ability to recover 16-bit performance after 4-bit fine-tuning suggests the potential for even more aggressive [[quantization for large language models | quantization]], possibly down to [[2bit quantization for machine learning models | 3-bit]] or even 1-bit base models, while still achieving high performance <a class="yt-timestamp" data-t="02:57:05">[02:57:05]</a>.
*   **Industry Trends:** The trend towards highly optimized hardware and software stacks (vertical integration) suggests that future LLM computation will increasingly occur in cloud data centers with specialized hardware, rather than on consumer devices, though the "Edge AI" community continues to push for on-device deployment <a class="yt-timestamp" data-t="02:58:32">[02:58:32]</a> <a class="yt-timestamp" data-t="02:23:45">[02:23:45]</a>.

The QLoRA paper is considered a "superstar paper" for its algorithmic novelty, comprehensive ablation studies, and significant contributions to making state-of-the-art NLP accessible <a class="yt-timestamp" data-t="03:05:57">[03:05:57]</a>.