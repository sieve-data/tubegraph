---
title: Vision language models and key differences
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

[[Multimodal large language models vs vision language models | Vision language models]] (VLMs) are a type of artificial intelligence model that combines visual information with language understanding to perform various tasks <a class="yt-timestamp" data-t="02:28:09">[02:28:09]</a>. They fundamentally combine a visual model with a large language model (LLM), held together by some form of connector <a class="yt-timestamp" data-t="02:28:25">[02:28:25]</a>.

## Terminology
The community has not yet settled on a single acronym for these models <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. Common terms include:
*   **Vision Language Models (VLMs)** <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>, <a class="yt-timestamp" data-t="55:59:00">[55:59:00]</a>
*   **Multimodal Large Language Models (MLLMs)** <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>, <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>, <a class="yt-timestamp" data-t="55:46:00">[55:46:00]</a>
*   **Large Multimodal Models (LMMs)** <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>, <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>
*   **Large Scale Vision Language Models (LSVLMs)** <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>, <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>

Regardless of the acronym, they all represent a combination of a visual model and a large language model <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

## Core Architecture
At their core, [[Vision language models and encoders | VLMs]] typically involve:
1.  An **image encoder** (also known as a vision encoder or vision tower) that processes visual input <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
2.  A **text encoder** (or language model) that handles textual input <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
3.  A **connector** or **adapter** that bridges the outputs of the image encoder to the language model <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

The image is typically fed through a vision encoder, turning it into a representation or embedding, often consisting of "visual tokens" <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>, <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. Textual input is tokenized and embedded into text tokens <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. These visual and text tokens are then fed into a large language model <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

## [[Comparison of different vision language models | Key Differences and Design Choices]]

### Vision Encoder Pre-training Strategies
A significant difference among [[Vision language models and encoders | VLMs]] lies in how their vision encoders are pre-trained:
*   **Classification Objective:** Models are pre-trained on tasks like ImageNet classification <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>, where they learn to classify images into categories <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>. Examples include VGG or ResNet models trained on ImageNet <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   **Contrastive Objective:** Models are pre-trained using a contrastive loss, which encourages embeddings of matching image-text pairs to align while pushing unmatched pairs apart <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>, <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>. This often involves data sets with image-caption pairs <a class="yt-timestamp" data-t="12:25:00">[12:25:27]</a>. Examples include CLIP (from OpenAI) and SigLIP (a sigmoid-based improvement over softmax-based contrastive loss) <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. DINOv2 (from Meta) is another vision transformer trained with a self-supervised objective <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>, <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

**Finding:** Studies, like the Google Pali paper, have found that contrastively pre-trained vision encoders generally lead to better and more efficient [[Vision language models and their advancements | VLMs]], particularly for localization and text understanding tasks, even if they slightly underperform on standard image classification benchmarks like ImageNet <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>, <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>, <a class="yt-timestamp" data-t="07:09:00">[07:09:11]</a>.

### [[Vision language connectors and architectures | Connector Architectures]]
The "glue" that connects the vision encoder to the language model can vary:
*   **Multi-Layer Perceptron (MLP):** A common and conceptually simpler approach, where a small fully connected neural network processes the vision encoder's output before feeding it to the LLM <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This is used in models like LLaVA <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   **Cross-Attention Module:** Some models, like Alibaba's Qwen-VL, use a single-layer cross-attention module as the adapter <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. While fancier, experiments suggest it might not offer significant benefits over simpler MLPs <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>, <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
*   **Multi-level Feature Fusion:** Some architectures, such as Huawei's CoMM, combine features from different layers (shallow to deep) of the vision encoder, arguing that different layers capture different levels of detail (e.g., edges vs. semantic concepts) <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>, <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### Ensemble of Vision Encoders
Some models combine multiple pre-trained vision encoders. For example, Huawei's CoMM paper explored using both CLIP and DINOv2 vision encoders, taking their outputs and fusing them before feeding them to the LLM <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. This acts as an ensemble of encoders, leveraging their different strengths (e.g., CLIP for global semantic information, DINOv2 for fine-grained pixel information) <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. While it offers some performance improvement, the added complexity and inference cost might not always justify the marginal gains <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

### Training Philosophies and Techniques
*   **Freezing vs. Fine-tuning:** Most [[Vision language models and their advancements | VLM]]s freeze the pre-trained vision encoder during training, only training the connector (e.g., MLP) and the language model <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This significantly reduces compute requirements and speeds up training <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
    *   **Locked Image Tuning (LIT):** This technique involves strategically freezing and unfreezing parts of the model during training, allowing for better utilization of pre-training benefits without overwriting them <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   **Multi-stage Training Recipes:** Some models, like Qwen-VL, employ complex multi-stage training processes, including pre-training with frozen LLM, followed by multitask pre-training (training all components), and finally supervised fine-tuning with a frozen vision encoder <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.
*   **Learning Rates:** When fine-tuning pre-trained components (like language embeddings or vision encoders), it's often advised to use a smaller learning rate to avoid undoing previous pre-training <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
*   **LLM Choice:** The base LLM's nature matters. Using a "chat-based" (instruction-tuned) LLM requires strict adherence to its instruction format during fine-tuning, otherwise, it can lead to worse model quality <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>, <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   **Special Tokens:** Experiments have shown that using literal words like "system instruction" or "answer" instead of inserting new "special tokens" can yield better model quality <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>, <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

## [[Challenges and improvements in vision language models | Challenges and Future Directions]]

### Data Quality and Availability
*   **Data Scarcity:** There's a shortage of high-quality, complex multimodal datasets, especially for multi-round, multi-image dialogues <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.
*   **Synthetic Data:** To address data scarcity, models like LLaVA create synthetic datasets by giving GPT-4 images and generating fake conversations <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Data Augmentation:** More intricate data blending methods, like shuffling image IDs in datasets, are being explored, but they risk creating incorrect references and deteriorating performance <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>, <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
*   **Noise and Imperfection:** With giant, internet-scraped or synthetically generated datasets, manual cleaning is impossible, leading to increased noise and imperfect assumptions about data pairs <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

### Model Scale and Efficiency
*   **Parameter Count:** While larger models often yield better performance, smaller models (e.g., Google's Pali with 5 billion parameters) are more practical for inference and profitability in commercial applications <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   **Vision Encoder Size:** There's a debate on the optimal balance between vision encoder and language model size. A mismatch, like a 2B vision encoder with a 70B LLM, might be an "overkill" <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. Larger vision encoders (e.g., 22B) are being developed, but their impact on end-to-end VLM performance for tasks like VQA is still being explored <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>, <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.

### Benchmarking and Evaluation
Current benchmarks often fall short for complex, multi-round, multi-image dialogue scenarios <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. There's a need for better evaluation methods for agent-based models that interact with external APIs <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. Many papers claim "state-of-the-art" by comparing against less-known benchmarks or by finding niches <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

### Multimodality Beyond Text Output
Current [[Vision language models and their advancements | VLMs]] primarily take images and text as input and output only text <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. The next step is to enable models to output images and other modalities directly, rather than relying on external tools or APIs (like DALL-E for image generation) <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. This would require the language model to learn to output "vision tokens" that can then be used to generate an image <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

## Specific Implementations and Their Contributions

### Google Pali (PALI-3)
*   **Focus:** Developing smaller, faster, and stronger [[Vision language models and their advancements | VLMs]] for practical deployment <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   **Parameters:** 5 billion parameters <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.
*   **Key Finding:** Contrastively pre-trained vision encoders (like SigLIP) are more effective than classification-pre-trained ones for [[Vision language models and their advancements | VLM]] tasks like localization and text understanding <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>, <a class="yt-timestamp" data-t="07:09:00">[07:09:11]</a>.
*   **Multilingual Capabilities:** Leverages Google's strength in multilingual language models, often claiming state-of-the-art on multilingual benchmarks <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>, <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.

### Huawei CoMM (CLIP to DINO)
*   **Focus:** Investigating the effectiveness of different visual encoders and combining them <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>, <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.
*   **Approach:** Fuses visual embeddings from both CLIP and DINOv2 vision encoders, and incorporates multi-level features from intermediate layers <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>, <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.
*   **Finding:** Combination yields slight improvements, with different layers being useful for different tasks (e.g., shallow layers for low-level details, deeper layers for semantics) <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>, <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. However, the performance gains are considered underwhelming given the increased complexity and cost <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.
*   *Note: This paper was retracted.* <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>

### Microsoft DeepSpeed Visual Chat
*   **Focus:** Enabling multi-round, multi-image dialogues and enhancing scalability <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>, <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
*   **Framework:** Leverages the DeepSpeed framework for parallel training across multiple GPUs <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
*   **Key Contribution:** Introduces an "Innovative Multimodal Causal Attention Mechanism" for more clever handling of attention between image and text tokens in interleaved inputs <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Learnings:** Found that the final checkpoint, even if seemingly overfitted, sometimes delivers better testing results <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. Also noted challenges in creating good data sets for multi-round visual assistance <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.

### Alibaba Qwen-VL
*   **Focus:** Developing a versatile, large-scale, multilingual [[Vision language models and their advancements | VLM]] for understanding, localization, and text reasoning <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
*   **Multilingual Support:** Trained on multilingual image-text data, primarily English and Chinese <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.
*   **Architecture:** Uses OpenCLIP's Vision Transformer (ViT-BigG) as its vision encoder <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a> and a cross-attention module as its connector <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
*   **Training:** Employs a complex multi-stage training recipe that involves freezing/unfreezing components (similar to locked image tuning) <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.