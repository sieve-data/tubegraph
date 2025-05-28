---
title: Vision language models and their applications
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

## Introduction
[[vision_language_models | Vision language models]] (VLMs) are a rapidly evolving area in AI, with numerous papers and products emerging, including GPT-4 Vision and offerings from Google and other major tech companies <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Key research in this field includes papers such as PALI-3 from Google DeepMind/Research <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, "From CLIP to DINO" (Huawei, later retracted) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>, LLaVA from Microsoft and academic institutions <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>, DeepSpeed Visual Chat from Microsoft <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>, and Qwen-VL from Alibaba <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. These models fundamentally combine a visual model with a large language model <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Terminology
The community has not yet settled on a single acronym for these models <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Common terms include:
*   [[vision_language_models | Vision Language Models]] (VLM) <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>
*   Multimodal Large Language Models (MLLM) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>
*   Large Multimodal Models (LMM) <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>
*   Large Scale Vision Language Models (LSVLM) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="01:45:05">[01:45:05]</a>

Regardless of the acronym, they all describe models that integrate visual and linguistic understanding <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

## Key Components
A VLM typically consists of:
1.  **Vision Encoder:** Processes image input into a numerical representation (embedding) <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>.
2.  **Language Model:** Processes text inputs and generates text outputs <a class="yt-timestamp" data-t="00:30:12">[00:30:12]</a>.
3.  **Connector/Adapter (MLP or Cross-Attention):** A small neural network that bridges the vision encoder and the language model, converting visual embeddings into a format understandable by the language model <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>, <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>, <a class="yt-timestamp" data-t="01:54:05">[01:54:05]</a>. This component is often frozen or only partially trained to reduce compute costs <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.

## Training Objectives and Architectures

### Vision Transformers (ViTs)
[[Vision language models with pretrained components | Vision Transformers]] (ViTs) are a popular model architecture for images and video, adapting the Transformer architecture (largely used for language models) to visual tasks <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. ViTs process images by cutting them into small patches, which are then treated as "visual tokens" <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>. Each patch also includes a positional embedding to indicate its location within the image <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>.

### Pre-training Objectives
Two primary pre-training objectives for vision encoders are commonly compared:
1.  **Classification Objective:** Typically involves training on datasets like ImageNet for image classification. Examples include VGG or ResNet models <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.
2.  **Contrastive Objective:** Encourages embeddings of matching image-text pairs to be close in the representation space, while pushing embeddings of unmatched pairs apart <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>, <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. CLIP is a prominent example of a contrastively pre-trained vision encoder <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.

Studies, like the PALI-3 paper, indicate that contrastively pre-trained vision encoders (e.g., SigLIP-based ViTs) generally yield superior performance for visually situated text understanding and localization tasks in VLMs, even if they slightly underperform on standard image classification benchmarks <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>, <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

### Locked Image Tuning (LIT)
[[Vision language models with pretrained components | Locked Image Tuning]] (LIT) is a technique that involves freezing certain parts of the model during training, specifically allowing gradients to flow only into the text encoder or certain adapter layers, rather than the entire image encoder <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>, <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>. This allows for faster training and reduced computational budget <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. LIT also enables taking advantage of pre-trained vision and text encoders without overwriting their initial learning <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

### [[comparison_of_vision_architectures | Comparison of Vision Architectures]]
Some research explores combining multiple pre-trained vision encoders, such as CLIP and DINOv2, which are trained on different datasets and with different losses <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>. CLIP tends to capture global semantic information, while DINOv2 excels at fine-grained pixel information <a class="yt-timestamp" data-t="00:39:46">[00:39:46]</a>. By fusing features from multiple layers of these different encoders, a slightly better performance can be achieved <a class="yt-timestamp" data-t="01:11:50">[01:11:50]</a>, <a class="yt-timestamp" data-t="01:26:01">[01:26:01]</a>. However, the gains may not always justify the increased inference cost and complexity <a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>.

## Applications and Capabilities

### Visually Situated Text Understanding & Localization
[[Vision language models | VLMs]] demonstrate superior performance in tasks that require understanding text within a visual context and precisely locating objects or information in images <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

### Multilingual Support
Google's models, for example, leverage their strong multilingual language models to achieve state-of-the-art results on multilingual cross-modal retrieval benchmarks <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Alibaba's Qwen-VL also focuses on multilingual image-text data, particularly English and Chinese <a class="yt-timestamp" data-t="00:47:35">[00:47:35]</a>.

### Multi-Round, Multi-Image Dialogues
Advanced [[vision_language_models | VLMs]] can handle interleaved image and text inputs in multi-round dialogues, enabling more complex interactions <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>. This involves sophisticated attention mechanisms within the language model to manage information flow between multiple images and text turns <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>.

### Efficiency and Scalability
Companies like Google prioritize developing smaller, faster, and stronger [[vision_language_models | VLMs]], such as PALI-3 (5 billion parameters), to ensure profitability at inference time compared to larger models that might incur significant costs per user request <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>, <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>. DeepSpeed Visual Chat also focuses on optimizing LLMs by incorporating multimodal capabilities with a focus on enhancing efficiency and scalability <a class="yt-timestamp" data-t="00:36:08">[00:36:08]</a>.

### Data Augmentation and Instruction Tuning
Creating high-quality datasets for instruction tuning is a significant challenge for [[vision_language_models | VLMs]] <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>. Techniques involve synthetically generating conversations about images using large language models like GPT-4 <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>. However, complex data augmentation methods, such as shuffling images or generating text, can introduce noise and lead to deteriorated performance or incorrect references <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

### Future Directions
Future developments for [[vision_language_models_in_ai_agents | VLMs in AI agents]] may involve the ability for models to output not just text, but also images directly, moving beyond current methods that rely on external tools like diffusion models through APIs <a class="yt-timestamp" data-t="01:21:39">[01:21:39]</a>. This would require training language models to output "vision tokens" directly, leading to more integrated and versatile multimodal AI systems <a class="yt-timestamp" data-t="01:21:16">[01:21:16]</a>. The field could also see models becoming self-improving, guiding their own development and benchmark creation <a class="yt-timestamp" data-t="01:48:37">[01:48:37]</a>.