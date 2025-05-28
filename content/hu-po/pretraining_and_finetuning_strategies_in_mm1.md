---
title: Pretraining and finetuning strategies in MM1
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 
Apple's MM1 models represent a significant contribution to the field of multimodal AI, focusing on Vision Language Models (VLMs) <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. Despite Apple's historically secretive nature, the MM1 paper is noted for its extensive detail and transparency regarding [[finetuning machine learning models | finetuning]] and pre-training strategies <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.

The overarching goal of the MM1 project was to build performant multimodal large language models (MLLMs), which the community often refers to as Vision Language Models (VLMs) <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>, capable of consuming both image and text data to produce text <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. The MM1 family includes models up to 30 billion parameters, encompassing both dense and Mixture-of-Expert (MoE) variants <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>. These models exhibit appealing properties such as enhanced in-context learning, multi-image reasoning, and few-shot Chain-of-Thought prompting <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>.

### Core Design Decisions

The development of MM1 involved three major axes of design decisions <a class="yt-timestamp" data-t="21:27:00">[21:27:00]</a>:
1.  **Architecture:** Investigating different pre-trained image encoders and various methods of connecting them to Large Language Models (LLMs) <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>.
2.  **Data Choices:** Considering different types of data and their relative mixture weights <a class="yt-timestamp" data-t="21:44:00">[21:44:00]</a>.
3.  **Training Procedure:** Determining which parts of the model to train at what stage <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.

### [[Finetuning large language models | Pre-training Strategies]]

The pre-training of MM1 models is crucial for achieving state-of-the-art few-shot results <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

#### Image Encoder
The image encoder plays a substantial role, with image resolution and image token count having the highest impact <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
*   **Model Choice:** MM1 uses a Vision Transformer (ViT) large 14 (ViT-L/14) as its image encoder <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>. Unlike many VLM papers that use publicly available pre-trained encoders and freeze them, Apple trains their ViT from scratch, allowing gradients to flow into it during pre-training <a class="yt-timestamp" data-t="46:52:00">[46:52:00]</a>, <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a>.
*   **Loss Function:** The image encoder is trained with a Contrastive Language-Image Pre-training (CLIP) loss <a class="yt-timestamp" data-t="24:44:00">[24:44:00]</a>. CLIP losses endow the visual encoder with semantic knowledge by contrasting positive (similar) and negative (dissimilar) image pairs, ensuring similar concepts are close in the embedding space <a class="yt-timestamp" data-t="33:35:00">[33:35:00]</a>. This differs from reconstructive losses (like DINOv2), which explicitly capture all parts of an image with fine-grained details <a class="yt-timestamp" data-t="33:46:00">[33:46:00]</a>, <a class="yt-timestamp" data-t="37:34:00">[37:34:00]</a>.
*   **Resolution and Token Count:** Increasing image resolution (e.g., from 224 to 336 pixels) and the number of image tokens (e.g., from 64 to 144) significantly improves performance <a class="yt-timestamp" data-t="41:12:00">[41:12:00]</a>, <a class="yt-timestamp" data-t="45:37:00">[45:37:00]</a>. The final model uses a 378x378 pixel resolution with 144 tokens <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>.
*   **Ensembles:** While MM1 focuses on a single image encoder, other models in the open-source community, like MuSiC-Polyp, use ensembles of different image encoders (e.g., CLIP, SAM, OCR) to capture various types of visual information, offering a richer representation despite higher computational overhead <a class="yt-timestamp" data-t="38:40:00">[38:40:00]</a>.

#### Vision-Language Connector
The vision-language connector (also called a projector) adapts the visual features from the image encoder to be compatible with the LLM's token space <a class="yt-timestamp" data-t="25:35:00">[25:35:00]</a>, <a class="yt-timestamp" data-t="01:00:44">[01:00:44]</a>.
*   **Impact:** A surprising finding in the MM1 paper is that the architectural design of this connector has a "comparatively negligible performance" impact <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>, <a class="yt-timestamp" data-t="01:37:47">[01:37:47]</a>. This contradicts findings in other literature and aligns with the "bitter lesson" of focusing on scale and data over intricate architectural choices <a class="yt-timestamp" data-t="49:40:00">[49:40:00]</a>. MM1 uses a C-abstractor for its connector, despite the negligible impact on performance <a class="yt-timestamp" data-t="01:00:47">[01:00:47]</a>.

#### Data Mix and Composition
A careful mix of image caption, interleaved image-text, and text-only data is crucial for achieving strong results <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>, <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.
*   **Proportions:** The pre-training data consists of 45% captioned images (e.g., CC3M, CC12M), 45% interleaved image-text documents, and 10% text-only data <a class="yt-timestamp" data-t="26:18:00">[26:18:00]</a>.
*   **Captioning Data:** Contains relatively short text highly relevant to the image. It primarily lifts zero-shot performance <a class="yt-timestamp" data-t="53:41:00">[53:41:00]</a>.
*   **Interleaved Data:** Features substantially longer and more diverse text, often loosely related to surrounding images (like news articles). This type of data is instrumental for few-shot and text-on performance <a class="yt-timestamp" data-t="53:50:00">[53:50:00]</a>.
*   **Text-only Data:** Included to ensure the LLM's ability to process and understand text tokens is maintained, preventing it from over-focusing on vision during pre-training <a class="yt-timestamp" data-t="56:56:00">[56:56:00]</a>.
*   **[[Finetuning with synthetic data | Synthetic Data]]**: The use of [[finetuning_with_synthetic_data | synthetic captions]] (e.g., VCap 300M) yielded noticeable performance improvements, particularly for few-shot learning <a class="yt-timestamp" data-t="42:26:00">[42:26:00]</a>, <a class="yt-timestamp" data-t="58:16:00">[58:16:00]</a>.

#### Training Procedure
*   **Unfrozen Training:** Both the LLM and the visual encoders are pre-trained entirely unfrozen, allowing gradients to propagate throughout the entire model <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a>. This contrasts with common VLM practices of freezing pre-trained components.
*   **Scaling Laws:** MM1 experiments confirm that model performance consistently improves with increased image resolution and more pre-training data (pre-training steps) <a class="yt-timestamp" data-t="01:33:19">[01:33:19]</a>.
*   **Hyperparameter Sweeps:** Apple conducts extensive hyperparameter sweeps (e.g., for learning rate and weight decay) using smaller model configurations (e.g., 3 billion parameters) to identify optimal settings, assuming these findings generalize to larger models (e.g., 30 billion parameters) <a class="yt-timestamp" data-t="22:50:00">[22:50:00]</a>. They also note that validation loss was not strongly correlated with downstream task performance <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.

### [[Efficiency and performance of finetuning methods | Finetuning Strategies]]

MM1 utilizes a two-stage training pipeline, where pre-training is followed by a fine-tuning stage <a class="yt-timestamp" data-t="01:18:51">[01:18:51]</a>.
*   **Supervised Fine-tuning (SFT):** The models undergo supervised [[finetuning machine learning models | fine-tuning]] on smaller, more specific Visual Question Answering (VQA) data sets, such as Coco Captions, NoCaps, TextCaps, and various VQA benchmarks <a class="yt-timestamp" data-t="01:19:01">[01:19:01]</a>, <a class="yt-timestamp" data-t="01:35:39">[01:35:39]</a>.
*   **[[Finetuning with synthetic data | Synthetic Data for Finetuning]]**: A significant aspect of the fine-tuning process is the use of data sets generated by GPT-4 Vision, effectively enabling [[instruction_tuning_with_synthetic_data | distillation]] from this powerful proprietary model <a class="yt-timestamp" data-t="01:20:06">[01:20:06]</a>. This implies that MM1 learns to mimic the responses and capabilities of GPT-4 Vision.
*   **Internal Data:** Apple also incorporates an internal, text-only fine-tuning data set, described as similar to ShareGPT <a class="yt-timestamp" data-t="01:22:50">[01:22:50]</a>.
*   **Unfrozen Components:** Similar to pre-training, both the image encoder and the LLM remain unfrozen during SFT, leading to better empirical performance <a class="yt-timestamp" data-t="01:35:56">[01:35:56]</a>.
*   **Inference:** Outputs during fine-tuning are generated using greedy decoding <a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>.

### Model Architecture and Performance

MM1's core architecture relies on a decoder-only language model <a class="yt-timestamp" data-t="26:27:00">[26:27:00]</a>.
*   **Mixture-of-Experts (MoE):** MM1 includes MoE variants, with up to 64 experts and employing a top-2 gating mechanism <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>, <a class="yt-timestamp" data-t="01:13:20">[01:13:20]</a>. This allows for a larger total model capacity while keeping the activated parameters per inference constant <a class="yt-timestamp" data-t="01:0:42:00">[01:10:42:00]</a>. MoE models consistently show better performance than dense counterparts on most benchmarks <a class="yt-timestamp" data-t="01:32:04">[01:32:04]</a>. Load balancing techniques are used during training to prevent experts from becoming dominant and ensure even distribution of tokens <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
*   **Performance:** MM1 achieves state-of-the-art results compared to other published open-source pre-training models like Flamingo and Emu2 <a class="yt-timestamp" data-t="01:17:31">[01:17:31]</a>. However, when compared to closed models like GPT-4 Vision and Gemini Ultra, MM1's performance is competitive but not always state-of-the-art <a class="yt-timestamp" data-t="01:30:52">[01:30:52]</a>.

### Development Ecosystem

Apple leverages various tools and frameworks for MM1's development:
*   **Framework:** The models are trained using `axlearn`, a library built on top of JAX and XLA <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>.
*   **Evaluation:** For multimodal pre-training evaluations, Apple uses an internal fork of the Luther AI LM evaluation harness <a class="yt-timestamp" data-t="01:36:57">[01:36:57]</a>.
*   **Experiment Tracking:** Weights & Biases is used for experiment tracking <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.
*   **Hardware:** Notably, the paper does not disclose the specific hardware (GPUs or TPUs) used for training, which has led to speculation <a class="yt-timestamp" data-t="01:03:05">[01:03:05]</a>.

Overall, the MM1 paper provides valuable insights into [[techniques_for_efficient_model_finetuning | efficient model fine-tuning]] and pre-training strategies, particularly emphasizing the importance of data quality, mix, and the decision to train components unfrozen.