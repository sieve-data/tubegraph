---
title: AI model architecture and parallelism strategies
videoId: _TghtP0ZyoM
---

From: [[hu-po]] <br/> 

The Llama 3.1 model, a significant advancement in AI, utilizes a foundational architecture with sophisticated parallelism strategies to achieve its performance.

## Model Architecture

Llama 3.1 employs a standard dense [[transformerbased_model_architectures | Transformer model architecture]] that is "almost identical" to its predecessor, Llama 2 <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>, <a class="yt-timestamp" data-t="01:55:51">[01:55:51]</a>. The core of its design involves converting input text into discrete tokens <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>, which are then processed through token embeddings. These embeddings pass through multiple Transformer blocks, each containing a self-attention mechanism and a multi-layer perceptron (also known as a Feed-Forward Network or FFN) <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>-<a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. Finally, a classification head selects the next token from a vocabulary of 128,000 possibilities <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. The model operates via auto-regressive decoding, predicting one token at a time and adding it to the context for subsequent predictions <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>-<a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

Key architectural details include:
*   **Layers**: The 8B model has 32 layers, while the larger 405B model has 126 layers <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>-<a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
*   **Position Embeddings**: Llama 3 utilizes "Rope" embeddings, indicating no new advancements in this specific area for the model <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Tokenizer**: The tokenizer reduces text by a factor of 3.94, meaning each token is roughly four characters <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>-<a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. The vocabulary size is 128,000 tokens <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.

The performance gains of Llama 3 are primarily attributed to improvements in data quality and diversity, rather than significant algorithmic changes <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>-<a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

## Parallelism Strategies

Training large AI models like Llama 3 requires extensive computational resources and sophisticated parallelism techniques. The Llama 3 405B model is so large that it "does not fit in the GPU memory of a single machine with eight Nvidia H100s" <a class="yt-timestamp" data-t="01:59:25">[01:59:25]</a>. Consequently, it requires distributed training across multiple server nodes, for example, 16 GPUs for BF16 precision <a class="yt-timestamp" data-t="01:59:47">[01:59:47]</a>.

Four main types of [[parallelism_and_scalability_in_machine_learning | parallelism]] are employed:
1.  **Tensor Parallelism**: Splits individual weight tensors (e.g., half of a self-attention operation) into multiple chunks distributed across different devices <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>-<a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
2.  **Pipeline Parallelism**: Partitions the model vertically, stage by stage (layer by layer), allowing different devices to process different stages of the model in parallel. This often involves staggering the computation to reduce idle time <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>-<a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>, <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>-<a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.
3.  **Data Parallelism**: Splits the batch of training data, with different portions of the batch processed by different GPUs <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>-<a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.
4.  **Context Parallelism**: Divides the input context, with different parts calculated by different GPUs <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>-<a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

All four types of parallelism operate simultaneously, creating a "compute mesh" where each GPU sees a "four-dimensional slice" across these dimensions <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>-<a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. The order of parallelism dimensions (tensor, context, pipeline, data) is optimized for network communication, with the innermost parallelism requiring the highest bandwidth and lowest latency, typically constrained to within the same server <a class="yt-timestamp" data-t="01:55:51">[01:55:51]</a>-<a class="yt-timestamp" data-t="01:56:06">[01:56:06]</a>, <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>-<a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

> "Within the same server node... that node has the fastest communication between it... it's going to be a lot faster to communicate between two GPUs that are sitting on the same node rather than one GPU that's on one pod and another GPU that's on a complete different pod" <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>-<a class="yt-timestamp" data-t="01:06:26">[01:06:26]</a>

## Hardware and Infrastructure

The Llama 3 training utilized a "research super cluster" comprising 16,000 H100 GPUs, each consuming 700 Watts and possessing 80 gigabytes of high-bandwidth memory (HBM) <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>-<a class="yt-timestamp" data-t="00:51:05">[00:51:05]</a>. The system includes a distributed file system with over 240 petabytes of storage, capable of a peak throughput of 7 terabytes per second <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>-<a class="yt-timestamp" data-t="00:51:52">[00:51:52]</a>.

A major challenge for these large-scale training efforts is supporting "highly bursty checkpoint" operations <a class="yt-timestamp" data-t="00:51:54">[00:51:54]</a>. All GPUs often attempt to save their state simultaneously, leading to sudden demands on the storage system. Additionally, environmental factors like midday temperatures can impact GPU performance, causing dialectical throughput variations of 1-2% <a class="yt-timestamp" data-t="00:57:50">[00:57:50]</a>-<a class="yt-timestamp" data-t="00:57:53">[00:57:53]</a>. This highlights [[energy_and_compute_optimization_in_ai_models | energy consumption]] as a growing bottleneck <a class="yt-timestamp" data-t="00:58:41">[00:58:41]</a>.

Even with these advanced setups, GPU utilization during training is only about 40% <a class="yt-timestamp" data-t="01:03:15">[01:03:15]</a>. This low utilization is primarily due to communication overhead, as GPUs spend a significant amount of time waiting for data or for other GPUs to complete their tasks <a class="yt-timestamp" data-t="01:03:40">[01:03:40]</a>-<a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>.

For [[technical_aspects_of_ai_model_training_and_finetuning | inference]], Llama 3 leverages [[technical_aspects_of_ai_model_training_and_finetuning | pipeline parallelism]] and FP8 quantization <a class="yt-timestamp" data-t="01:58:57">[01:58:57]</a>-<a class="yt-timestamp" data-t="01:59:02">[01:59:02]</a>. While BF16 precision requires two server nodes for the 405B model, using FP8 quantization allows the model to fit on a single node, significantly boosting throughput by roughly two times due to faster intra-node communication <a class="yt-timestamp" data-t="02:06:58">[02:06:58]</a>-<a class="yt-timestamp" data-t="02:07:25">[02:07:25]</a>. However, not all parameters are quantized; parameters in the self-attention layer and the first/last Transformer layers are not quantized <a class="yt-timestamp" data-t="02:03:03">[02:03:03]</a>-<a class="yt-timestamp" data-t="02:03:19">[02:03:19]</a>.