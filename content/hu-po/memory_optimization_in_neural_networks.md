---
title: memory optimization in neural networks
videoId: pov3pLFMOPY
---

From: [[hu-po]] <br/> 

Memory optimization is a critical aspect of working with large neural networks, particularly for fine-tuning massive models like Large Language Models (LLMs). This article explores QLoRA, an efficient fine-tuning approach that significantly reduces memory usage while preserving performance.

## Introduction to QLoRA

QLoRA (Quantized LoRA) is a method that drastically reduces the memory required to fine-tune large language models, enabling operations previously only possible on expensive, multi-GPU server racks to be performed on a single GPU [00:04:41]. For example, QLoRA can fine-tune a 65 billion parameter LLaMA model on a single 48 GB GPU [00:04:30], whereas traditional 16-bit fine-tuning would require over 780 GB of GPU memory, necessitating multiple server racks [01:17:15]. This approach preserves the full 16-bit fine-tuning task [[Performance and efficiency in machine learning models | performance]] [00:05:31], making it a dominant method for efficient fine-tuning [00:07:45].

## Key Innovations in QLoRA

QLoRA introduces several innovations to save memory without sacrificing [[Performance and efficiency in machine learning models | performance]] [01:02:24]:

1.  **4-bit Normal Float (NF4)**: A new data type that is "information theoretically optimal for normally distributed weights" [01:03:11].
2.  **Double [[quantization_and_optimization_in_machine_learning | quantization]]**: A method that further reduces memory by quantizing the [[quantization_and_optimization_in_machine_learning | quantization]] constants themselves [01:17:18].
3.  **Paged Optimizers**: Utilizes Nvidia unified memory to manage memory spikes during training, preventing out-of-memory errors [01:03:00].

## [[quantization_and_optimization_in_machine_learning | Quantization]] Fundamentals

[[quantization_and_optimization_in_machine_learning | Quantization]] is the process of discretizing an input from a representation that holds more information to one with less information [00:42:43]. It typically involves converting data types with more bits (e.g., 32-bit floats) to fewer bits (e.g., 8-bit integers) [00:43:00]. This process is inherently lossy, meaning information is lost [00:42:54].

A common technique is to rescale input data (often structured as a tensor) to fit the target data type's range, usually through normalization by the absolute maximum of the input elements [00:43:29]. This normalization ensures efficient use of the limited bits by minimizing the need to store large exponents, allowing more bits for the fraction (mantissa) [00:44:00].

However, outliers in the input tensor can reduce [[Energy and Compute Optimization in AI Models | efficiency]], as a large magnitude value can cause many [[quantization_and_optimization_in_machine_learning | quantization]] bins to be underutilized [00:49:09]. To mitigate this, input tensors are often chunked into smaller blocks that are then independently quantized [00:51:05]. This approach requires storing multiple [[quantization_and_optimization_in_machine_learning | quantization]] constants (one for each block), creating a trade-off between handling outliers and the overhead of storing these constants [00:51:47].

## 4-bit Normal Float (NF4)

The NF4 data type is built on quantile [[quantization_and_optimization_in_machine_learning | quantization]], an information-theoretically optimal approach for data types where each [[quantization_and_optimization_in_machine_learning | quantization]] bin has an equal number of assigned values [01:04:41]. This works effectively when input tensors come from a fixed distribution [01:11:19].

Since pre-trained neural network weights typically have a zero-centered normal distribution [01:12:21], NF4 leverages this assumption. It scales weights to fit a fixed distribution within an arbitrary range (e.g., -1 to 1) [01:12:47], allowing for computationally feasible exact quantile estimation [01:11:29]. The resulting NF4 data type is designed to have a discrete zero point, which is crucial for quantizing padding and other zero-valued elements without error [01:18:21]. Empirical results show NF4 yields better results than standard 4-bit integers and 4-bit floats [01:12:13].

## Double [[quantization_and_optimization_in_machine_learning | Quantization]]

Double [[quantization_and_optimization_in_machine_learning | quantization]] (DQ) further reduces memory by quantizing the [[quantization_and_optimization_in_machine_learning | quantization]] constants themselves [01:24:40]. These constants, which would typically be stored as 32-bit floats, are quantized to 8-bit floats [01:25:57]. This process involves subtracting the mean from the 32-bit constants before [[quantization_and_optimization_in_machine_learning | quantization]] to center their values around zero, similar to how weights are normalized [01:29:43]. DQ saves an average of about 0.37 bits per parameter, amounting to roughly 3 GB for a 65 billion parameter model [01:27:41].

## Paged Optimizers

Paged optimizers address memory spikes that occur during gradient checkpointing, which can cause out-of-memory errors when processing mini-batches with long sequence lengths [01:02:56]. This feature uses Nvidia unified memory, which allows for automatic page-to-page transfers between CPU RAM and GPU VRAM [01:31:34]. When the GPU runs out of memory, optimizer states are automatically "evicted" to CPU RAM and can be "paged" back to the GPU when needed [01:34:06]. While this process can introduce slowdowns if done frequently, for a 65B model with a batch size of 16, paged optimizers offer the same training speed as regular optimizers [01:50:09].

## Low-Rank Adapters (LoRA)

LoRA is a parameter-efficient fine-tuning method that significantly reduces memory requirements by introducing a small set of trainable parameters called "adapters" [00:53:47]. The original, large pre-trained model parameters remain fixed (or "frozen") [00:55:09]. Gradients during stochastic gradient descent are backpropagated through the frozen model weights to update only these small LoRA adapters [00:55:12].

The key insight is that while LoRA adapters are small (e.g., 0.2% of the original model weights [00:59:44]), a significant portion of memory footprint for LLM fine-tuning comes from activation gradients and not the LoRA parameters themselves [00:59:12]. By using [[quantization_and_optimization_in_machine_learning | quantization]] on the frozen base model and training only the small LoRA adapters, QLoRA achieves immense memory savings. A crucial finding is that applying LoRA to *all* linear Transformer block layers is necessary to match full 16-bit fine-tuning [[Performance and efficiency in machine learning models | performance]] [01:58:57], while the specific projection dimension (rank `R`) of the adapters has less impact on performance [02:00:20].

## Performance and Impact

QLoRA demonstrates that it is possible to fine-tune a [[quantization_and_optimization_in_machine_learning | quantized]] 4-bit model without any [[Performance and efficiency in machine learning models | performance]] degradation compared to a full 16-bit fine-tuned baseline [01:54:55]. This ability to "fully recover" performance loss due to imprecise [[quantization_and_optimization_in_machine_learning | quantization]] through adapter fine-tuning is significant [02:08:51].

QLoRA allows large models (e.g., LLaMA 65B) to be fine-tuned on a single consumer GPU [02:00:59], making state-of-the-art LLM fine-tuning accessible to individual researchers and smaller organizations outside of large industrial labs [02:04:47]. This increased accessibility is a major win for the open-source AI community [02:05:01].

Additionally, QLoRA enables extensive ablation studies, allowing researchers to train over a thousand models with varying parameters to deeply understand their behavior [01:10:57]. Studies with QLoRA have also shown that data quality is far more important than data set size for fine-tuning [01:14:45].

## Challenges and Future Directions

The evaluation of LLMs remains an art, with benchmarks often being biased or not fully trustworthy [00:08:46]. QLoRA authors found that GPT-4 evaluations, while cheap and reasonable, can have noticeable biases, such as assigning higher scores to systems appearing first in its prompt [02:41:50]. Despite this, GPT-4 evaluations largely agree with human judgments, providing a viable alternative for the open-source community [02:29:01].

Future work includes investigating:
*   How slower performance occurs with paging processes [01:50:12].
*   Whether multilingual training improves [[Performance and efficiency in machine learning models | performance]] [02:43:18].
*   Even more aggressive [[quantization_and_optimization_in_machine_learning | quantization]] to 3-bit base models combined with fine-tuning [02:57:15].

The findings suggest that the community can focus on increasing the number of parameters in the base model while decreasing their precision [02:13:44], pushing the boundaries of what is possible on limited hardware. The ongoing vertical integration in deep learning, where models and training processes are increasingly optimized for specific hardware architectures, also plays a role in this trend [01:57:00].