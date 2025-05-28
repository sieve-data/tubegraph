---
title: OpenELM paper on language model
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 

OpenELM is an open-source language model family developed by Apple, notable for its efficiency and transparent release strategy. It demonstrates significant performance improvements for its size, signaling Apple's entry into the [[opensource_advancements_in_visionlanguage_models | open-source]] large language model arena alongside Meta <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

## Key Characteristics and Performance

OpenELM focuses on creating efficient models, particularly suitable for deployment on mobile devices like iPhones <a class="yt-timestamp" data-t="27:17:00">[27:17:00]</a>.

*   **Model Size**: OpenELM models are relatively small, with parameters ranging from 270 million (tiny) to 3 billion <a class="yt-timestamp" data-t="27:06:00">[27:06:00]</a>. A 1 billion parameter model is considered "cell phone size" <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.
*   **Accuracy and Efficiency**: OpenELM exhibits a 2.36% improvement in accuracy compared to a previous [[llm_large_language_models_development | open language model]], Mamba, while requiring two times fewer pre-training tokens. This challenges traditional [[advancements_in_language_models | scaling laws]] that suggest larger models with more tokens always perform better <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>.
*   **Open-Source Commitment**: Unlike many "open-source" projects that only release weights and inference code, Apple provides a complete framework for training and evaluation. This includes training logs, multiple checkpoints, and pre-training configurations on publicly available datasets <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. They also release code to convert models to the MLX library for inference and fine-tuning on Apple devices <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.

## Architecture and Techniques

OpenELM utilizes a decoder-only Transformer architecture, which is standard for modern [[llm_large_language_models_development | language models]] <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

Key architectural features include:
*   **Pre-normalization**: Uses RMS Norm, applied before the attention and feed-forward layers <a class="yt-timestamp" data-t="12:22:00">[12:22:22]</a>.
*   **Rotary Position Embeddings**: A method for incorporating positional information into the model's understanding of text sequences <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.
*   **Grouped Query Attention (GQA)**: An interpolation between multi-query and multi-head attention, offering quality close to multi-head attention at speeds comparable to multi-query. This improves [[compute_efficiency_in_language_models | inference efficiency]] by reducing the size of the KV cache <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>.
*   **Flash Attention**: An optimized attention mechanism that improves speed by intelligently managing memory on the GPU <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.
*   **Tokenizer**: OpenELM uses the Llama 2 tokenizer with a vocabulary size of 32,000 <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>. This is considered "old school" compared to the Llama 3 tokenizer, which has a vocabulary size of 128,000 tokens <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.

### Layer-wise Scaling
A unique architectural trick highlighted by Apple is **layer-wise scaling** <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>.
Traditional Transformer models typically use a uniform configuration across all layers (e.g., the same number of attention heads and feed-forward network dimensions) <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. Layer-wise scaling adapts these parameters (number of attention heads, FFN width) for different layers. This is beneficial because different layers process information at varying levels of abstraction, from lower-level features to higher-level concepts <a class="yt-timestamp" data-t="18:41:00">[18:41:00]</a>.

## Training Details

OpenELM models were trained for 350,000 iterations using the AdamW optimizer <a class="yt-timestamp" data-t="26:50:00">[26:50:00]</a>.

*   **Pre-training Data**: The models are pre-trained on a mix of public datasets, including Refined Web, The Pile, RedPajama, and Dolma v1.6, totaling approximately 1.8 trillion tokens <a class="yt-timestamp" data-t="23:26:00">[23:26:00]</a>.
*   **Data Curation**: A critical aspect of OpenELM's training is the use of *subsets* of these large datasets. This involves curating and cleaning the data, which is considered a more impactful factor in performance than simply using the full, raw dataset <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>.
*   **On-the-Fly Tokenization**: Unlike approaches that use pre-tokenized data, OpenELM filters and tokenizes data "on the fly." This allows for experimentation with various tokenizers during hyperparameter sweeps, providing greater flexibility in the training process <a class="yt-timestamp" data-t="24:49:00">[24:49:00]</a>.
*   **Weight Averaging**: To improve accuracy and reduce noise, the final model used for inference is obtained by averaging the weights of the last five saved checkpoints during training <a class="yt-timestamp" data-t="27:57:00">[27:57:00]</a>.
*   **Instruction Tuning**: After pre-training, the models undergo instruction tuning to adapt them for chatbot functionalities <a class="yt-timestamp" data-t="30:06:00">[30:06:00]</a>.

## Hardware and Performance

### Training Hardware
The models were fine-tuned using eight Nvidia H100 GPUs, highlighting the significant computational resources required for [[llm_large_language_models_development | large language model development]] <a class="yt-timestamp" data-t="30:21:00">[30:21:00]</a>.

### Inference Hardware
Apple evaluated inference performance on both standard consumer-grade setups and Apple hardware:
*   **Consumer Setup**: An Intel CPU with 64GB of DDR5 RAM and an Nvidia RTX 4090 GPU with 24GB of VRAM <a class="yt-timestamp" data-t="31:10:00">[31:10:00]</a>. This configuration is considered a good standard for a deep learning computer at home <a class="yt-timestamp" data-t="32:19:00">[32:19:00]</a>.
*   **Apple Hardware**: An Apple MacBook Pro with an M2 Max system on chip and 64GB of RAM running Mac OS 14. The models and code were ported to Apple's MLX library for this <a class="yt-timestamp" data-t="32:45:00">[32:45:00]</a>.

### Performance Bottlenecks
Apple identified that a significant portion of OpenELM's processing time was due to a "naive implementation" of RMS Norm. This resulted in many individual kernel launches instead of a single, fused kernel, which would be more efficient <a class="yt-timestamp" data-t="33:45:00">[33:45:00]</a>. Fusing kernels involves combining multiple operations into a single, more efficient GPU operation, drastically improving speed without changing the mathematical outcome <a class="yt-timestamp" data-t="37:31:00">[37:31:00]</a>.

## Broader Implications

The development of OpenELM, alongside other models like Microsoft's F3 and Meta's [[llm_large_language_models_development | Llama 3]], reinforces several key trends in [[advancements_in_language_models | language model advancements]]:

*   **Data Quality Over Quantity**: The performance of OpenELM on fewer tokens, thanks to heavily curated data, underscores the growing realization that data quality and curation are paramount, possibly more so than raw data size or specific model architectures <a class="yt-timestamp" data-t="45:05:00">[45:05:00]</a>.
    *   Microsoft's F3 paper further elaborates on this, suggesting that smaller models should prioritize learning reasoning abilities over memorizing factual knowledge. Factual knowledge can be offloaded to external tools like search engines via techniques like RAG (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="59:54:00">[59:54:00]</a>.
*   **Synthetic Data**: The use of synthetic data generated by [[llm_large_language_models_development | language models]] themselves for training, particularly for domains like math and coding where validity can be verified, is becoming a common practice seen in F3 and [[llm_large_language_models_development | Llama 3]] <a class="yt-timestamp" data-t="55:36:00">[55:36:00]</a>. This represents a "self-play loop" where models create their own training data <a class="yt-timestamp" data-t="56:02:00">[56:02:00]</a>.
*   **[[quantization_of_language_models | Quantization]] Challenges**: While OpenELM targets small, deployable models that would benefit from [[quantization_of_language_models | quantization]], recent studies on [[comparison_of_different_vision_language_models | Llama 3]] suggest that newer, heavily pre-trained models might be more "fragile" to [[quantization_of_language_models | quantization]]. This means that reducing bit-width might lead to significant performance degradation that cannot be fully compensated by fine-tuning techniques like Laura, unlike previous generations of models <a class="yt-timestamp" data-t="0:11:00">[01:11:00]</a>. This has implications for the future of specialized [[compute_efficiency_in_language_models | GPU hardware]] for inference vs. training <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.