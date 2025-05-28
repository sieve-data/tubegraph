---
title: Layerwise scaling and architecture tricks
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 

Recent advancements in open-source [[large_language_models_llms_and_scaling | Large Language Models (LLMs)]], such as Apple's OpenELM and Microsoft's Phi-3, highlight various architectural and optimization "tricks" used to achieve high performance with smaller models and fewer training tokens. However, a recurring theme is the increasing emphasis on data quality over architectural novelty <a class="yt-timestamp" data-t="04:46:01">[04:46:01]</a>.

## Core Architectural Design: Decoder-Only Transformers

All three papers examined – OpenELM, Phi-3, and studies on Llama 3 – utilize a decoder-only Transformer architecture <a class="yt-timestamp" data-t="09:12:16">[09:12:16]</a>. This contrasts with the original Transformer model, which featured both an encoder and a decoder, primarily designed for translation tasks where an input sentence is encoded and then decoded into another language <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>. Modern LLMs typically use only the decoder part, processing sequences auto-regressively to predict the next token <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>. This simplifies the architecture by removing the need for an encoder pass before generating output <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.

## Optimization Techniques for Efficiency

Various architectural and implementation tricks are employed to enhance the efficiency of LLMs:

### Normalization Strategies
*   **Pre-normalization:** Unlike the original Transformer that performed normalization *after* attention and feed-forward layers, pre-normalization moves these `Add & Norm` operations to *before* these blocks <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.
*   **RMS Norm vs. Layer Norm:** OpenELM uses RMS Norm, a variant of normalization that can be very similar to Layer Norm <a class="yt-timestamp" data-t="35:54:00">[35:54:00]</a>.
*   **Fused Kernels:** A significant performance bottleneck in OpenELM's naive RMS Norm implementation was the lack of a single fused kernel <a class="yt-timestamp" data-t="33:50:00">[33:50:00]</a>. Fusing kernels involves combining multiple sequential operations (like matrix multiplication, dropout, activation) into a single, optimized GPU operation. This drastically reduces memory transfers and overhead, leading to faster execution, even if the mathematical result is identical <a class="yt-timestamp" data-t="37:31:00">[37:37:31]</a>. Implementing fused kernels is complex and often requires manual optimization <a class="yt-timestamp" data-t="39:47:00">[39:47:00]</a>.

### Attention Mechanisms
*   **Rotary Position Embeddings (RoPE):** Used for encoding positional information in the input sequence <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. Phi-3 also utilizes RoPE for extended context lengths <a class="yt-timestamp" data-t="47:28:00">[47:28:00]</a>.
*   **Grouped Query Attention (GQA):** An interpolation of multi-query and multi-head attention that aims to achieve multi-head quality at multi-query speeds <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. GQA reduces the number of keys and values in the KV cache, which improves inference efficiency <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>. Phi-3 also uses GQA <a class="yt-timestamp" data-t="22:39:00">[22:39:00]</a>.
*   **Flash Attention:** An optimization technique that exploits the GPU's memory hierarchy to more efficiently perform the attention mechanism, which is often the slowest part of a Transformer <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.

### Tokenization
OpenELM and Phi-3 both utilize the Llama 2 tokenizer, which has a vocabulary size of 32,000 tokens <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>. In contrast, Llama 3 introduced a new tokenizer with a much larger vocabulary size of 128,000 tokens, offering more nuance <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>. Models like OpenELM filter and tokenize data "on the fly" during training, allowing for experimentation with different tokenizers as hyperparameters <a class="yt-timestamp" data-t="24:50:00">[24:50:50]</a>.

## Layerwise Scaling

OpenELM highlights "layerwise scaling" as a key architectural trick <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. Traditional Transformer models maintain a uniform configuration across all layers (e.g., same number of attention heads, same feed-forward network dimensions) <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. In layerwise scaling, the dimensionality of the feed-forward network (FFN) and the number of heads in the multi-head attention are adapted per layer <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>. This adaptation makes sense because different layers within a Transformer deal with varying levels of abstraction; lower layers process low-level features, while higher layers handle more abstract features <a class="yt-timestamp" data-t="18:41:00">[18:41:00]</a>.

## [[large_language_models_llms_and_scaling | Quantization]] and Data Types

[[impact_of_architecture_on_training_and_inference | Quantization]] is a critical technique for running LLMs on resource-limited devices like mobile phones <a class="yt-timestamp" data-t="47:57:00">[47:57:00]</a>. It reduces the memory footprint and computation requirements by storing model parameters (weights) with fewer bits (e.g., 4-bit integers instead of 16-bit floating points) <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a>. Phi-3, for example, quantizes to 4 bits to occupy only about 1.8 GB of memory, enabling deployment on an iPhone 14 <a class="yt-timestamp" data-t="48:00:00">[48:00:00]</a>.

Studies on Llama 3's quantization performance show that while it still performs well at 4-bit and 8-bit quantization compared to previous Llama versions, it suffers "non-negligent degradation" at ultra-low bit widths (e.g., 2-bit or 1-bit) <a class="yt-timestamp" data-t="52:19:00">[52:19:00]</a>. Crucially, unlike Llama 1 and Llama 2, which could be heavily quantized and then fine-tuned with [[impact_of_architecture_on_training_and_inference | LoRA (Low Rank Adaptation)]] to surpass their original 16-bit performance, Llama 3 does not show this robustness <a class="yt-timestamp" data-t="01:17:38">[01:17:38]</a>. This suggests that Llama 3's high performance, attributed to its massive pre-training (15 trillion tokens) <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>, makes it more "fragile" to quantization <a class="yt-timestamp" data-t="01:39:41">[01:39:41]</a>. This shift raises questions about the future of inference precision and GPU hardware specialization <a class="yt-timestamp" data-t="01:22:19">[01:22:19]</a>.

## The [[role_of_model_architecture_and_data_scale | Role of Model Architecture and Data Scale]]

While architectural tricks are important, a strong takeaway from recent LLM developments is that data quality and curation are paramount <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>. As one OpenAI observer notes, "model behavior is not determined by the architecture, hyperparameters, or optimizer choices, it's determined by your data set" <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

*   **Data Curation:** OpenELM's improved accuracy with fewer tokens than previous models is attributed to heavily filtered and curated subsets of common datasets <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.
*   **Targeted Training Data:** Phi-3 emphasizes curating training data to improve the model's reasoning ability rather than its capacity for memorizing factual knowledge <a class="yt-timestamp" data-t="00:58:50">[00:58:50]</a>. The rationale is that models can access external tools like search engines for facts, freeing up internal capacity for logical reasoning <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.
*   **Synthetic Data and Multi-Phase Training:** Phi-3 uses a two-phase training curriculum, starting with general web data and then moving to heavily filtered web data mixed with LLM-generated synthetic data <a class="yt-timestamp" data-t="00:57:49">[00:57:49]</a>. This self-play loop, where the model generates data for its own training, is increasingly prevalent in modern LLMs <a class="yt-timestamp" data-t="00:56:02">[00:56:02]</a>.