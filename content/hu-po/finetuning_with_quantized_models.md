---
title: finetuning with quantized models
videoId: pov3pLFMOPY
---

From: [[hu-po]] <br/> 

[[finetuning_machine_learning_models | Finetuning machine learning models]] is an effective way to enhance their performance and modify their behaviors, but it can be prohibitively expensive for very large models <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. A conventional 16-bit finetuning of the Llama 65B model, for instance, demands over 780 GB of GPU memory <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>. The QLoRA method addresses this challenge by enabling efficient [[finetuning_language_models_for_specific_tasks | finetuning of large language models]] (LLMs) with significantly reduced memory usage <a class="yt-timestamp" data-t="01:27:07">[01:27:07]</a>. This breakthrough allows a 65-billion-parameter model to be finetuned on a single 48GB GPU, while preserving 16-bit finetuning task performance <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>.

## What is QLoRA?

QLoRA (Quantized Low Rank Adaptation) is an efficient finetuning approach that drastically reduces memory requirements without sacrificing performance <a class="yt-timestamp" data-t="01:02:28">[01:02:28]</a>. It is considered one of the most efficient and quickest types of [[finetuning_machine_learning_models | finetuning]], even enabling finetuning on a consumer GPU <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. The paper "QLoRA: Efficient Finetuning of Quantized LLMs" by Tim Dettmers and others details this method <a class="yt-timestamp" data-t="01:53:07">[01:53:07]</a>. Tim Dettmers is also the author of the `bitsandbytes` library, which is a popular GitHub repository for various [[quantization_and_optimization_in_machine_learning | quantization techniques]] <a class="yt-timestamp" data-t="02:46:46">[02:46:46]</a>.

The core principle of QLoRA involves backpropagating gradients through a frozen, 4-bit quantized pretrained LLM <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. Instead of updating the full model weights, which remain fixed, a small set of learnable, low-rank adapter weights (LoRA) are added and tuned <a class="yt-timestamp" data-t="00:53:47">[00:53:47]</a>. This allows for significant memory savings because gradients are only pushed into these small LoRA modules <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.

## Key Innovations of QLoRA

QLoRA introduces several innovations to save memory without sacrificing performance <a class="yt-timestamp" data-t="01:02:28">[01:02:28]</a>:

### 1. 4-bit NormalFloat (NF4)

NF4 is an information-theoretically optimal [[2bit_quantization_for_machine_learning_models | quantization data type]] for normally distributed weights <a class="yt-timestamp" data-t="01:03:07">[01:03:07]</a>. It yields better empirical results than standard 4-bit integers and 4-bit floats <a class="yt-timestamp" data-t="01:04:03">[01:04:03]</a>. Neural network weights typically follow a zero-centered normal distribution <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.

The process of quantization involves discretizing an input from a representation with more information (e.g., 32-bit floats) to one with less information (e.g., 4-bit) <a class="yt-timestamp" data-t="00:42:43">[00:42:43]</a>. This is inherently a lossy process <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>. To maximize the utility of the limited bits, input data is commonly rescaled or normalized to fit the target data type's range <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.

A common issue in [[Quantization for large language models | quantization]] is that outliers can cause the quantization bits to be poorly utilized, leading to wasted bins <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>. To mitigate this, the input tensor (e.g., model weights) is chunked into smaller blocks, and each block is independently quantized <a class="yt-timestamp" data-t="00:51:05">[00:51:05]</a>. This results in numerous "quantization constants" that need to be stored <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

### 2. Double Quantization (DQ)

Double Quantization reduces memory overhead by quantizing the quantization constants themselves <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>. For example, if the initial quantization constants are stored as 32-bit floats, DQ can quantize them down to 8-bit floats <a class="yt-timestamp" data-t="01:25:53">[01:25:53]</a>. This saves approximately 0.37 bits per parameter, translating to about 3 GB for a 65-billion-parameter model <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. Like the primary weights, these quantization constants are also centered around zero before quantization for efficiency <a class="yt-timestamp" data-t="01:29:18">[01:29:18]</a>.

### 3. Paged Optimizers

During [[finetuning_machine_learning_models | finetuning]], memory spikes can occur, especially when processing mini-batches with long sequence lengths <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. These spikes can lead to "out of memory" (OOM) errors, crashing the program <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. Paged optimizers manage these memory spikes by leveraging Nvidia's unified memory feature <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. This allows the GPU to automatically transfer optimizer states (which are intermediate values and gradients) to CPU RAM when GPU memory runs low <a class="yt-timestamp" data-t="01:33:51">[01:33:51]</a>. This mechanism helps prevent OOM errors, making it feasible to finetune large models on a single GPU <a class="yt-timestamp" data-t="01:48:52">[01:48:52]</a>. When needed, the data is "paged" back to the GPU <a class="yt-timestamp" data-t="01:34:11">[01:34:11]</a>.

## LoRA (Low-Rank Adaptation)

LoRA is a method for [[finetuning_pretrained_models_with_minimal_additional_parameters | finetuning pretrained models with minimal additional parameters]] <a class="yt-timestamp" data-t="00:53:47">[00:53:47]</a>. It works by introducing small, trainable "adapters" alongside the fixed, pre-trained model weights <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>. The gradients are backpropagated through the frozen model to update only these adapter weights <a class="yt-timestamp" data-t="00:55:24">[00:55:24]</a>.

In QLoRA, the base model weights are stored in 4-bit NF4 precision, while the LoRA adapters are typically stored and computed in 16-bit BrainFloat (BF16) precision <a class="yt-timestamp" data-t="01:36:03">[01:36:03]</a>. When a quantized weight tensor is used, it is de-quantized to BF16 for matrix multiplication, then calculations are performed in 16-bit <a class="yt-timestamp" data-t="01:03:55">[01:03:55]</a>.

Crucially, QLoRA found that applying LoRA adapters to *all* linear Transformer block layers is required to match full 16-bit finetuning performance <a class="yt-timestamp" data-t="01:58:55">[01:58:55]</a>. The projection dimension (rank `R`) of the LoRA adapters does not significantly affect performance <a class="yt-timestamp" data-t="01:59:43">[01:59:43]</a>.

## Performance and Implications

QLoRA has demonstrated that it is possible to finetune a [[Quantization for large language models | quantized 4-bit model]] without any performance degradation compared to full 16-bit finetuning <a class="yt-timestamp" data-t="01:52:25">[01:52:25]</a>. The method reduces the memory requirement for finetuning a 65-billion-parameter model from over 780 GB to less than 48 GB <a class="yt-timestamp" data-t="02:00:16">[02:00:16]</a>.

The Guanaco family of models, trained using QLoRA, achieved 99.3% of ChatGPT's performance level on the Vicuna Benchmark, requiring only 24 hours of finetuning on a single professional GPU <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>. Smaller Guanaco models (e.g., 7B parameters) can be finetuned in less than 12 hours on a consumer GPU <a class="yt-timestamp" data-t="02:21:17">[02:21:17]</a>.

QLoRA's efficiency significantly enhances the accessibility of LLM finetuning, making it possible for the largest publicly available models to be finetuned on a single GPU <a class="yt-timestamp" data-t="02:03:38">[02:03:38]</a>. This is a major win for the open-source AI community and independent researchers, as it removes the prohibitive compute costs traditionally associated with LLM training <a class="yt-timestamp" data-t="02:57:51">[02:57:51]</a>.

Key findings from QLoRA's extensive studies (over 1000 models finetuned) include:
*   Data quality is far more important than dataset size for finetuning <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   [[Performance and implications of quantized language models | Quantized 4-bit adapter finetuning]] can fully recover performance loss due to imprecise [[quantization in large language models | quantization]] <a class="yt-timestamp" data-t="02:08:47">[02:08:47]</a>.
*   Hyperparameter settings found on smaller models (e.g., 7B) often generalize well to larger models (e.g., 65B), reducing the need for costly hyperparameter sweeps on large models <a class="yt-timestamp" data-t="02:17:42">[02:17:42]</a>.
*   GPT-4 based evaluations, while showing some biases (e.g., preferring the first response presented), are a cheap and reasonably reliable alternative to human evaluation for chatbot performance <a class="yt-timestamp" data-t="01:49:59">[01:49:59]</a>.

## Conclusion

QLoRA represents a significant advancement in [[advancements_in_model_efficiency_through_quantization | model efficiency through quantization]] and [[finetuning_machine_learning_models | finetuning]]. By combining innovations like 4-bit NormalFloat, Double Quantization, and Paged Optimizers with the LoRA adaptation method, it makes the finetuning of massive LLMs accessible on consumer-grade hardware. This democratizes LLM research and development, allowing smaller teams and individual researchers to compete with large industry labs in pushing the state of the art in AI <a class="yt-timestamp" data-t="02:57:51">[02:57:51]</a>.