---
title: Challenges and strategies for training largescale vision language models
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

[[multimodal_large_language_models | Vision language models]] (VLMs), also known as multimodal large language models (MLMs), large multimodal models (LMMs), or large scale vision language models (LVLMs), integrate visual and linguistic understanding to process and generate information. The field is rapidly evolving, with various research groups and companies publishing their own approaches and findings <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>, <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>, <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>, <a class="yt-timestamp" data-t="01:55:07">[01:55:07]</a>.

## Key Challenges in VLM Training

Training [[multimodal_large_language_models | Vision Language Models]] presents several [[challenges_in_training_large_computer_vision_models | challenges]], including:

*   **High Inference Costs** Training and running large models, especially for a product where every user request incurs a cost, can be prohibitively expensive <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>, <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. Companies like Google prioritize developing smaller, more cost-effective models for practical applications <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Data Quality and Availability**
    *   **Noisy Datasets:** [[challenges_in_training_large_computer_vision_models | Large language models]] often rely on massive datasets scraped from the internet or synthetically generated, which can introduce noise, incorrect labels, and imperfect assumptions <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>, <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. Manually cleaning such colossal datasets is impractical <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.
    *   **Lack of Interleaved Data:** There is a scarcity of high-quality datasets for multi-image, multi-round dialogue or interleaved image-text inputs, which are crucial for assistant-like interactions <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>, <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>. Synthetic data generation (e.g., using GPT-4 to create fake conversations from captioned images) is one approach to address this <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>, <a class="yt-timestamp" data-t="01:33:10">[01:33:10]</a>.
*   **Model Overfitting:** While less problematic with extremely large datasets and advanced data augmentation, ensuring a model generalizes well and doesn't overfit its training data remains a consideration <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>.
*   **Mismatched Model Sizes:** Using a disproportionately large [[large_language_models_and_their_applications | large language model]] (e.g., 70 billion parameters) with a relatively small vision encoder (e.g., 2 billion parameters) might not be optimal, suggesting that scaling the vision encoder size could yield significant performance gains <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>, <a class="yt-timestamp" data-t="01:30:59">[01:30:59]</a>.
*   **Lack of Standardized Terminology:** The proliferation of different acronyms (VLM, MLM, LMM, LVLM) and varied terminology for model components (e.g., "connector" vs. "adapter") creates confusion in the research community <a class="yt-timestamp" data-t="01:55:07">[01:55:07]</a>.

## Training Strategies and Approaches

Researchers employ various strategies to overcome these challenges and improve VLM performance:

### Efficient Model Design and Training

*   **Smaller, Practical Models:** Companies like Google aim for smaller models (e.g., PaLI-3 with 5 billion parameters) that offer competitive performance at lower inference costs, making them more suitable for production and mass adoption <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>, <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>, <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.
*   **Leveraging Pre-trained Components:** Instead of training from scratch, models often start with pre-trained [[scaling_of_language_models_and_vision_transformers | Vision Transformer]] (ViT) and [[large_language_models_and_their_applications | large language model]] backbones <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>, <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. This significantly reduces training time and computational resources.
*   **"Locked Image Tuning" (Freezing):** A common strategy is to freeze the pre-trained vision encoder, preventing gradients from flowing into it during training. This allows faster training with a lower compute budget by only pushing gradients into smaller components like an MLP connector or the language model <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>, <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **Multi-Stage Training Recipes:** Training VLMs can involve complex multi-stage processes, including initial pre-training, freezing specific parts, training on different objectives, instruction tuning, and potentially RLHF <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>, <a class="yt-timestamp" data-t="00:52:24">[00:52:24]</a>.

### Optimizing Vision Encoder Pre-training

*   **Contrastive vs. Classification Objectives:** Research indicates that vision encoders pre-trained with a contrastive objective (e.g., SigLIP/CLIP) perform significantly better for tasks like visually-situated text understanding and localization compared to those pre-trained with classification objectives (e.g., ImageNet classifiers) <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, <a class="yt-timestamp" data-t="01:42:05">[01:42:05]</a>. Contrastive learning pulls similar embeddings together and pushes different ones apart <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Higher Resolution Inputs:** Using vision encoders that support higher output resolutions (e.g., from QuenVL) can significantly improve model quality, especially for tasks requiring fine-grained detail, such as OCR <a class="yt-timestamp" data-t="00:58:50">[00:58:50]</a>.

### Enhancing Multimodal Integration

*   **Combining Multiple Vision Encoders:** An ensemble approach combining different pre-trained vision encoders (e.g., CLIP for global semantic information and DINOv2 for fine-grained pixel information) can enhance visual capabilities, although the performance gains might sometimes be small relative to the increased complexity and cost <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>, <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>, <a class="yt-timestamp" data-t="01:51:14">[01:51:14]</a>, <a class="yt-timestamp" data-t="01:51:57">[01:51:57]</a>.
*   **Multi-Level Feature Fusion:** Extracting and concatenating features from intermediate layers of vision encoders, in addition to the final output layer, can provide a richer representation that captures both low-level details (edges, textures) and high-level semantic concepts <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>, <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>, <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>, <a class="yt-timestamp" data-t="01:44:06">[01:44:06]</a>.
*   **Simple Connectors:** While some papers explore complex connectors like mini-ViT cross-attention layers, many find that a simple Multi-Layer Perceptron (MLP) or even a single linear layer is sufficient to bridge the vision encoder and the [[large_language_models_and_their_applications | large language model]] <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>, <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>, <a class="yt-timestamp" data-t="01:31:54">[01:31:54]</a>.
*   **Multimodal Causal Attention:** For multi-image and multi-round dialogues, a clever attention mechanism can be used to ensure image tokens primarily attend to other image tokens, and text tokens to other text tokens, with appropriate cross-modal attention between them <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>.
*   **Data Blending and Augmentation:** Employing techniques like shuffling image IDs within datasets can augment multimodal training data, though care must be taken to avoid creating incorrect references that degrade model performance <a class="yt-timestamp" data-t="01:32:42">[01:32:42]</a>, <a class="yt-timestamp" data-t="01:36:21">[01:36:21]</a>.
*   **Learning Rate Adjustments:** When fine-tuning pre-trained components, adjusting learning rates is critical. Applying a high learning rate to a model that was trained with a decreasing learning rate schedule can "undo" its pre-training <a class="yt-timestamp" data-t="01:05:32">[01:05:32]</a>.
*   **Using Chat-based vs. Raw LLMs:** If using a chat-based [[large_language_models_and_their_applications | large language model]] (one that has been instruction-tuned for dialogue), strict adherence to its instruction format is crucial for optimal performance <a class="yt-timestamp" data-t="01:08:30">[01:08:30]</a>. Non-chat-based LLMs are more general and adaptable to new tasks <a class="yt-timestamp" data-t="01:08:38">[01:08:38]</a>.
*   **Special Tokens:** Experiments suggest that it might be better not to incorporate special tokens for elements like "system instructions," "question," or "answer," but rather to literally type the words <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.

### Performance Evaluation

Standard benchmarks like ImageNet 1K might not accurately reflect a VLM's performance on tasks like visual question answering (VQA). A model performing well on image classification might be worse at VQA, highlighting the need for task-specific evaluation metrics <a class="yt-timestamp" data-t="01:39:17">[01:39:17]</a>. The lack of standardized benchmarks for agent-based models that interact with external APIs is also a noted challenge <a class="yt-timestamp" data-t="01:46:51">[01:46:51]</a>.

---

_This article is based on insights from recent papers on [[multimodal_large_language_models | vision language models]], including PaLI-3 (Google DeepMind), Comm (Huawei), LLaVA (Microsoft), DeepSpeed Visual Chat (Microsoft), and Qwen-VL (Alibaba)._