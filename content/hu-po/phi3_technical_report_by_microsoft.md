---
title: Phi3 technical report by Microsoft
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 

The Phi-3 technical report details Microsoft's small open-source language model, Phi-3 [00:04:11, 00:41:23]. It was released on April 23, 2024 [00:04:23].

## Model Architecture and Characteristics
Phi-3 is built on a [[3d_representations_and_their_applications | Transformer decoder]] architecture [00:09:16, 00:47:24]. The model is designed to be highly capable while remaining compact enough to run locally on devices like a phone [00:04:11, 00:41:23, 00:47:57].

Key architectural features include:
*   **Size**: Phi-3 Mini has 3.8 billion parameters [00:41:25].
*   **Context Length**: It uses a 4K context length, with longer context introduced via LongRope [00:47:27, 00:47:28, 00:47:30].
*   **Tokenization**: Phi-3 employs the [[Quantization in LLaMA3 | Llama 2 tokenizer]], which has a vocabulary size of 32,000 [00:14:31, 00:14:43, 00:47:35]. This tokenizer is considered "old school" compared to the newer Llama 3 tokenizer with 128,000 tokens [00:16:01, 00:47:40].

## Training Methodology
Phi-3 Mini was trained on 3.3 trillion tokens [00:41:39]. A significant aspect of its training involves heavily filtered web data and [[Text to 3D content generation | synthetic data]] [00:43:57, 00:55:30]. This approach leverages LLM-based filtering of web data and LLM-created [[Text to 3D content generation | synthetic data]] to achieve performance levels typically observed in much larger models [00:44:11, 00:55:30, 00:55:47].

The training process is structured in two phases, forming a curriculum [00:57:32, 00:57:49]:
1.  **Phase 1**: Teaches the model general knowledge using web data [00:57:52, 00:58:24].
2.  **Phase 2**: Focuses on heavily filtered web data combined with [[Text to 3D content generation | synthetic data]] [00:57:55]. To prevent catastrophic forgetting of knowledge learned in Phase 1, a subset of the initial web data is included in Phase 2 [00:58:06, 00:58:30, 01:16:15]. This filtering ensures the web data contains the "correct level of knowledge" [00:58:50, 00:59:56]. The goal is to maximize the model's capacity for reasoning rather than memorizing factual knowledge, which can be retrieved via external tools like search engines [00:59:06, 00:59:27, 01:00:16, 01:00:46].

## Quantization for Deployment
To enable deployment on mobile devices like the iPhone 14, Phi-3 is designed to be quantized [00:48:00, 00:50:34, 01:11:00]. It is quantized to 4 bits, allowing it to occupy only about 1.8 gigabytes of memory [00:48:00, 00:48:03]. This results in an inference speed of approximately 12 tokens per second on an iPhone 14 with an A16 Bionic chip [00:50:34, 00:50:37].

## Performance and Evaluation
In terms of performance, Phi-3 Mini achieves a 68 MMLU score in a 5-shot evaluation [01:05:44]. The use of [[Text to 3D content generation | synthetic data]] and heavily filtered data is a key factor in its strong performance, allowing it to punch above its weight class compared to models trained on less curated data [00:44:11, 01:35:56].