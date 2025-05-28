---
title: Scaling of language models and vision transformers
videoId: BJ98vicRYHg
---

From: [[hu-po]] <br/> 

The LLaVA (Large Language and Visual Assistant) project explores the [[implications_of_ai_model_scaling_and_convergence | scaling]] of [[large language models and their applications | language models]] and [[applications_in_vision_transformers | Vision Transformers]] (ViTs) to create powerful multimodal AI [03:04]. LLaVA represents an end-to-end trained large multimodal model that integrates a vision encoder and an [[large language models and their applications | Large Language Model]] (LLM) for general-purpose visual and language understanding [06:48].

## LLaVA's Architecture and Components
LLaVA connects a pre-trained vision encoder with an LLM using a relatively simple projection matrix or a multi-layer perceptron (MLP) [29:20].

### Vision Encoder
The vision encoder, sometimes referred to as a "backbone" or "vision tower," consumes raw images and outputs a rich feature representation [06:56]. LLaVA specifically uses OpenAI's CLIP (Contrastive Language-Image Pre-training) ViT-L/14 model [07:26].

*   **Patch-based Processing**: [[applications_in_vision_transformers | Vision Transformers]] process images by cutting them into small patches (e.g., 14x14 pixels) and treating these patches as a sequence or "sentence" of image tokens [07:45].
*   **Contrastive Pre-training**: The CLIP model is pre-trained using a contrastive loss, where image-text pairs are pulled together in an embedding space if they are related and pushed apart if unrelated [08:45]. This creates an embedding space where text and images with similar semantic meanings are closer [09:09].
*   **Resolution Scaling**: A key improvement in LLaVA 1.5 was the use of a CLIP model with a slightly larger image resolution (336x336 pixels compared to the original 224x224) [08:23], which contributed to improved performance [00:59:51].

### Language Model
LLaVA integrates with a [[large language models and their applications | large language model]], specifically Vicuna [16:37], which is a variant of LLaMA [16:39]. Vicuna itself is fine-tuned on GPT-4 answers [16:56].

## Scaling Observations and Insights

The LLaVA project provides significant insights into [[implications_of_ai_model_scaling_and_convergence | AI model scaling]], particularly highlighting the importance of data and training recipes over complex architectures.

### Training Efficiency vs. Pre-training Costs
LLaVA 1.5 achieved state-of-the-art results on 11 different benchmarks with approximately one day of training on a single A100 node (8 A100 GPUs) [06:05]. However, this efficiency is largely due to the use of highly pre-trained components (CLIP by OpenAI and Vicuna/LLaMA by Meta/Facebook) [09:49]. The actual LLaVA training primarily involves fine-tuning a small "projection matrix" (an MLP) that connects the vision encoder to the LLM [47:06]. This minimal trainable component allows for a much smaller memory and compute footprint, enabling training on consumer-grade GPUs [47:17].

### Data Scaling and Mixture
The transparency of LLaVA's data mixture is lauded as a key aspect of true open-source AI [22:39].

*   **Instruction-Following Data**: The initial LLaVA 1.0 paper demonstrated the effectiveness of "visual instruction tuning" using machine-generated instruction-following data [12:03]. This data was created by feeding text descriptions (including bounding box coordinates) of images into a text-only GPT-4 model to generate conversational question-answer pairs, without actually showing the image to GPT-4 [13:10].
*   **Two-Stage Tuning**: LLaVA employs a two-stage instruction tuning procedure:
    1.  **Feature Alignment (Pre-training)**: Initially, the model is pre-trained on image-text pairs (e.g., a subset of CC3M) where the task is to generate captions from images. In this stage, both the visual encoder and the LLM are frozen, with only the projection matrix being trained to align image features with the LLM's word embedding space [46:57].
    2.  **Instruction Tuning**: In the second stage, the weights of both the projection layer and the LLM (specifically, via LoRA fine-tuning) are updated using more diverse instruction-following data, including multimodal chat data and academic VQA (Visual Question Answering) datasets [49:18].
*   **Data Dominance**: Scaling results show that most of the performance boost comes from adding more and diverse fine-tuning data, such as VQA V2, OK-VQA, and OCR-VQA [01:05:05]. This suggests a shift in machine learning research focus from novel model architectures to the "training recipe" and data mixture [01:06:05].

### Model and Resolution Scaling
While LLaVA demonstrates strong performance with relatively smaller [[large language models and their applications | LLMs]] (7B and 13B parameters), the results suggest further scaling of the LLM could yield even better performance [01:31:56]. The improvement from using a higher-resolution CLIP vision encoder (336x336) also contributed to LLaVA 1.5's gains [01:00:07].

### Research Directions and Implications
The success of LLaVA suggests several key implications for the field:

*   **Simple Architectures**: The effectiveness of a simple MLP as a visual-language connector challenges the notion that complex cross-modal connection architectures are necessary [01:02:59].
*   **Data Efficiency**: LLaVA achieves state-of-the-art results with "significantly less compute and training data" than other methods, implying that focused instruction tuning on diverse, high-quality data can be more impactful than massive, generalized pre-training for specific multimodal tasks [01:32:51].
*   **Synthetic Data Generation**: The practice of using powerful LLMs (like GPT-4) to synthetically generate instruction-following data is a growing paradigm, creating a "virtuous cycle" where models generate data to train better models [02:27:54].
*   **Accessibility**: The open-source nature, reproducibility, and affordability of LLaVA's training process make state-of-the-art multimodal LLM research more accessible to a wider community [01:10:07].

## Limitations and Challenges

Despite its strengths, LLaVA has limitations:

*   **Commercial Use Licenses**: Due to the reliance on GPT-generated data for instruction tuning, LLaVA's license (following LLaMA 2's license) restricts commercial use [01:12:09].
*   **Hallucination**: While LLaVA 1.5 has reduced propensity for hallucination, it can still occasionally disseminate misinformation [01:40:55].
*   **Single Image Processing**: The current model is not yet capable of processing multiple images due to the lack of sufficient instruction-following data and context length limitations [01:40:39].

The debate continues regarding whether modular approaches (like LLaVA's, combining pre-trained vision and language components) will eventually be surpassed by truly end-to-end trained generalist models, reflecting the "bitter lesson" philosophy in AI [01:43:57]. However, the practical and computational advantages of LLaVA's approach make it a strong contender for current and near-future research and application [01:50:51].