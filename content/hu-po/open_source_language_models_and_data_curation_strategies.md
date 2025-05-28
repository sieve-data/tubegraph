---
title: Open source language models and data curation strategies
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 

Recent advancements in [[large_language_models_and_their_applications | Large Language Models]] (LLMs) highlight a growing trend among tech giants to release [[open_source_ai_models_and_accessibility | open source models]], often focusing on smaller, more efficient architectures. This contrasts with companies like OpenAI and Anthropic, who maintain a closed-source approach to their models <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. The development of these models often emphasizes sophisticated data curation strategies over sheer data volume or complex architectural tricks <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>.

## OpenELM (Apple)

Released on April 22nd, Apple's OpenELM is an [[open_source_ai_models_and_accessibility | open source language model]] family, featuring models as small as 270 million parameters, primarily designed for cell phones <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>, <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>, <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>. OpenELM demonstrates a 2.36% accuracy improvement over a previous open language model (MML), requiring two times fewer pre-training tokens <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This suggests that the training process and data quality are more critical than the quantity of training data <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

Apple's release is notably comprehensive, providing not just model weights and inference code, but also the complete framework for training and evaluation on publicly available datasets, including training logs, multiple checkpoints, and pre-training configurations <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>, <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

### Architectural Details and Tricks
OpenELM uses a decoder-only Transformer architecture <a class="yt-timestamp" data-t="00:10:00">[01:10:00]</a>, which is now standard for modern language models <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. Key techniques include:
*   **Pre-normalization with RMS Norm**: Normalization is applied before attention and feed-forward layers <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Rotary Position Embeddings**: A common method for incorporating positional information <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
*   **Grouped Query Attention**: Improves inference speed by sharing keys and values across multiple query heads, optimizing KV caching <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Flash Attention**: An optimization for attention mechanisms that leverages GPU memory hierarchy for faster computation <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Layer-wise Scaling**: A notable trick where the dimensionality of the Feed-Forward Network (FFN) and the number of attention heads are adapted per layer, rather than remaining uniform across all layers <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>, <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. This acknowledges that different layers process information at varying levels of abstraction <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Data Curation and Training
OpenELM's pre-training data includes RefinedWeb, The Pile, RedPajama, and Dolma v1.6, totaling approximately 1.8 trillion tokens <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>, <a class="yt-timestamp" data-t="00:41:49">[00:41:49]</a>. A crucial aspect is the use of *subsets* of these datasets, indicating a curated, cleaner mix of data <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
*   **On-the-fly Tokenization**: Unlike prior approaches that use pre-tokenized data, OpenELM filters and tokenizes data as it's consumed. This allows for experimentation with various [[tokenization_and_synthetic_data_generation_in_language_models | tokenizers]] during hyperparameter sweeps <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.
*   **Weight Averaging**: Instead of using the very last checkpoint, the final model is an average of the last five checkpoints. This technique helps reduce noise from individual batches and improves generalization <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

## Phi-3 (Microsoft)

Microsoft's Phi-3, another small [[large_language_models_and_their_applications | language model]], introduces Phi-3 Mini with 3.8 billion parameters, trained on 3.3 trillion tokens <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>, <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a>. The core innovation of Phi-3, similar to Llama 3, lies in its use of heavily filtered data and [[tokenization_and_synthetic_data_generation_in_language_models | synthetic data]] <a class="yt-timestamp" data-t="00:42:13">[00:42:13]</a>, <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.

### The Importance of Data Quality
Microsoft highlights that while scaling laws suggest predictable improvements with more data, these laws assume fixed data sources <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. By filtering web data using LLMs and generating synthetic data, Phi-3 achieves performance typically seen in much larger models <a class="yt-timestamp" data-t="00:44:11">[00:44:11]</a>.

[!QUOTE]
"It's become awfully clear to me that these models are truly approximating their data sets to an incredible degree... trained on the same data set for long enough, pretty much every model with enough weights and training time converges to the same point. It implies that model behavior is not determined by the architecture, hyperparameters, or optimizer choices; it's determined by your data set, nothing else." <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>

This perspective, supported by observations from OpenAI, underscores that data set quality and curation are paramount, rather than architectural intricacies <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>.

### Training Curriculum
Phi-3 employs a two-phase training curriculum to mitigate catastrophic forgetting <a class="yt-timestamp" data-t="00:57:32">[00:57:32]</a>:
1.  **Phase 1**: Trains the model on general knowledge from web data <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>.
2.  **Phase 2**: Uses heavily filtered web data mixed with [[tokenization_and_synthetic_data_generation_in_language_models | synthetic data]]. A portion of the phase 1 data is included to prevent the model from forgetting its initial learning <a class="yt-timestamp" data-t="00:57:55">[00:57:55]</a>, <a class="yt-timestamp" data-t="00:58:30">[00:58:30]</a>.

A key aspect of this filtering is to remove factual knowledge (e.g., specific sports scores) and instead prioritize data that improves the model's reasoning ability <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>. This is because smaller models have limited capacity for factual knowledge, and future LLMs are expected to augment their knowledge with external tools like search engines <a class="yt-timestamp" data-t="00:59:27">[00:59:27]</a>, <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>. By focusing training on reasoning, models become "smarter" in problem-solving rather than just memorization <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>.

## Llama 3 (Meta) and Quantization

Meta's Llama 3 models are trained on an immense 15 trillion tokens of data <a class="yt-timestamp" data-t="01:09:35">[01:09:35]</a>. Following its release, numerous papers quickly emerged, evaluating Llama 3 across various domains, including [[challenges_and_approaches_in_adapting_large_language_models_for_specific_tasks | low-bit quantization]]. This rapid response from academic groups suggests they have evaluation infrastructures prepared, waiting for new [[open_source_ai_models_and_accessibility | open source models]] to be released to conduct and publish experiments swiftly <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>.

### Quantization Challenges
[[large_language_models_and_their_applications | Quantization]] reduces the memory and computation requirements of LLMs by representing parameters with fewer bits (e.g., 4-bit integers instead of 16-bit floats) <a class="yt-timestamp" data-t="01:10:57">[01:10:57]</a>. This allows models to run on resource-limited devices like iPhones <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, <a class="yt-timestamp" data-t="00:50:33">[00:50:33]</a>.

However, studies on Llama 3 show a "non-negligent degradation" in performance when quantized, especially at ultra-low bit widths (e.g., 2-bit or 1-bit) <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>. This differs from Llama 1 and Llama 2, where quantization combined with techniques like LoRA (Low-Rank Adaptation) fine-tuning could sometimes surpass the performance of the original 16-bit models <a class="yt-timestamp" data-t="01:17:38">[01:17:38]</a>.

With Llama 3, LoRA fine-tuning on a small dataset can no longer fully compensate for the performance loss due to quantization <a class="yt-timestamp" data-t="01:18:27">[01:18:27]</a>. This suggests that the strong performance of Llama 3, largely due to its massive pre-training data, makes it more "fragile" to quantization <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>, <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>. This challenges the previous assumption that quantization would always be a highly effective optimization for inference <a class="yt-timestamp" data-t="01:21:48">[01:21:48]</a>.

## Conclusion

The release of models like OpenELM, Phi-3, and Llama 3 underscores the growing importance of [[open_source_ai_models_and_accessibility | open source LLMs]]. A key takeaway from these developments is the critical role of data curation and quality over mere quantity. Filtering data to focus on reasoning abilities and integrating [[tokenization_and_synthetic_data_generation_in_language_models | synthetic data generation]] are becoming standard practices <a class="yt-timestamp" data-t="01:42:06">[01:42:06]</a>. However, the unexpected sensitivity of models like Llama 3 to quantization poses new [[challenges_and_approaches_in_adapting_large_language_models_for_specific_tasks | challenges]] and raises questions about future hardware design and the most efficient methods for deploying LLMs <a class="yt-timestamp" data-t="01:40:45">[01:40:45]</a>, <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>.