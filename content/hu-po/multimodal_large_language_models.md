---
title: Multimodal large language models
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 

[[Multimodal Language Models | Multimodal large language models]] (MMLLMs) are defined as large-scale [[large_language_models_and_their_applications | Foundation models]] that consume image and text data and produce text as an output <a class="yt-timestamp" data-t="06:10:59">[06:10:59]</a>. While the term "multimodal" implies multiple modalities (such as images, text, and audio), MMLLMs discussed here specifically refer to models that handle vision and language, often referred to as Vision Language Models (VLMs) by the community <a class="yt-timestamp" data-t="07:10:59">[07:10:59]</a>. Apple, for instance, chose to brand its model as an MMLLM rather than a VLM, potentially to "own the category" and optimize for search engine optimization (SEO) <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.

## Key Components

An MMLLM typically consists of three major architectural components:
1.  **Image Encoder:** Processes the input image to extract visual features <a class="yt-timestamp" data-t="24:54:59">[24:54:59]</a>.
2.  **Vision-Language Connector (Projector):** Bridges the visual features from the image encoder to a format compatible with the [[large_language_models_and_their_applications | large language model]] <a class="yt-timestamp" data-t="25:07:00">[25:07:00]</a>.
3.  **Language Model:** A [[large_language_models_and_their_applications | decoder-only language model]] that consumes visual tokens and text tokens to generate text responses <a class="yt-timestamp" data-t="26:26:00">[26:26:00]</a>.

## Training Process

MMLLMs undergo a two-stage training pipeline:
1.  **Pre-training:** This stage involves training on a large mix of datasets <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>.
2.  **Supervised Fine-tuning (SFT) / Instruction Tuning:** A subsequent stage where the model is further trained on smaller, task-specific datasets <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a> <a class="yt-timestamp" data-t="52:50:00">[52:50:00]</a>.

### Data Mix
A crucial aspect of pre-training is the careful mix of data types <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>:
*   **Image Caption Data:** Consists of images paired with relatively short, highly relevant captions <a class="yt-timestamp" data-t="53:41:00">[53:41:00]</a>. This data type is most important for zero-shot performance <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. Synthetic captions (like those from the VCap 300M dataset) can significantly boost few-shot results <a class="yt-timestamp" data-t="42:29:00">[42:29:00]</a>.
*   **Interleaved Image-Text Documents:** Contains images interspersed within longer, more diverse text, where the images might be only loosely related to the surrounding text (similar to news articles) <a class="yt-timestamp" data-t="53:50:00">[53:53:00]</a>. This is instrumental for few-shot and text-on-text performance <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>.
*   **Text-Only Data:** Helps the [[large_language_models_and_their_applications | language model]] retain its ability to process text effectively, preventing it from over-focusing on vision <a class="yt-timestamp" data-t="56:56:00">[56:56:00]</a>.

For Apple's MM1 model, a mix of 45% captioned images, 45% interleaved image-text documents, and 10% text-only data was found to be optimal <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.

### Unfrozen Components
Unlike many other VLM papers that freeze pre-trained image encoders, Apple's MM1 models are pre-trained and fine-tuned with both the image encoder and the [[large_language_models_and_their_applications | language model]] entirely unfrozen <a class="yt-timestamp" data-t="01:01:14">[01:01:14]</a> <a class="yt-timestamp" data-t="01:35:56">[01:35:56]</a>. This allows gradients to propagate all the way down into the image encoder, leveraging a larger training budget <a class="yt-timestamp" data-t="01:36:19">[01:36:19]</a>.

### Loss Functions for Image Encoders
Image encoders can be trained with different types of losses:
*   **Contrastive Losses:** (e.g., CLIP) Endow the visual encoder with semantic knowledge by pulling similar representations closer and pushing dissimilar ones farther apart in the embedding space <a class="yt-timestamp" data-t="33:32:00">[33:32:00]</a> <a class="yt-timestamp" data-t="35:37:00">[35:37:00]</a>. This results in features that capture high-level semantic concepts, such as identifying different images of a pizza as having high similarity <a class="yt-timestamp" data-t="37:11:00">[37:11:00]</a>.
*   **Reconstructive Losses:** (e.g., DINOv2) Explicitly capture all parts of an image by trying to reconstruct the input, leading to more nuanced, low-level features that focus on fine details <a class="yt-timestamp" data-t="33:49:00">[33:49:00]</a> <a class="yt-timestamp" data-t="36:13:00">[36:13:00]</a>.

Apple developed its own CLIP-trained image encoder, a Vision Transformer (ViT-L) with a 378x378 pixel resolution, rather than relying on existing public encoders <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a> <a class="yt-timestamp" data-t="01:48:48">[01:48:48]</a>.

## Performance and Comparisons

Apple's MM1 models, up to 30 billion parameters, claim "state-of-the-art" results in pre-training metrics and competitive performance after supervised fine-tuning across various established multimodal benchmarks <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a> <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>. While they outperform older models like Flamingo and Emu, they are acknowledged as "competitive" rather than strictly "state-of-the-art" when compared against cutting-edge closed-source models such as GPT-4 Vision and Gemini Ultra <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a> <a class="yt-timestamp" data-t="01:31:06">[01:31:06]</a>.

One notable aspect of MM1's fine-tuning is its reliance on synthetic datasets generated by GPT-4 Vision <a class="yt-timestamp" data-t="01:19:31">[01:19:31]</a>. This suggests that MM1, and many other [[Overview of Multimodal Models | Vision Language Models]], are indirectly "distilled" from [[multimodal_capabilities_in_large_language_models_using_clip | GPT-4 Vision]], raising questions about data ownership and the complex chain of dependencies in model training <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>.

## Design Lessons and Challenges

Through extensive ablation studies, Apple identified several crucial design lessons <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>:
*   **Image Resolution and Token Count:** The image resolution has the highest impact on model performance, followed by model size <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a> <a class="yt-timestamp" data-t="42:11:00">[42:11:00]</a>. Increasing the number of image tokens (patches) fed to the [[large_language_models_and_their_applications | language model]] generally leads to better performance, though it introduces computational challenges, especially for multi-image inputs due to context length limitations <a class="yt-timestamp" data-t="01:36:30">[01:36:30]</a> <a class="yt-timestamp" data-t="01:40:01">[01:40:01]</a>.
*   **Vision-Language Connector Design:** Contrary to prior literature, the specific architecture of the vision-language connector (e.g., linear projector, C-abstractor, D-abstractor) has a "comparatively negligible performance" impact <a class="yt-timestamp" data-t="01:04:30">[01:04:30]</a> <a class="yt-timestamp" data-t="01:37:51">[01:37:51]</a>. This aligns with Rich Sutton's "bitter lesson," suggesting that scale and data are more important than intricate architectural choices <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.
*   **Data Composition:** A careful mix of image, text, and interleaved data is vital for optimal multimodal performance and retaining strong text capabilities <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Synthetic caption data provides a non-trivial boost to performance <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.
*   **Scaling Laws:** The model consistently improves as it is trained on more data and with higher image resolutions, suggesting that scaling continues to be the primary driver of performance <a class="yt-timestamp" data-t="01:33:30">[01:33:30]</a> <a class="yt-timestamp" data-t="01:49:16">[01:49:16]</a>.
*   **Mixture of Experts (MoE):** MM1 utilizes MoE variants with a high number of experts (e.g., 64 experts), where only a subset (e.g., top two) are activated per token <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>. This increases the total parameter count (capacity) while keeping the activated parameters relatively constant during inference, leading to improved performance <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a> <a class="yt-timestamp" data-t="01:32:08">[01:32:08]</a>.

### Hardware Secrecy
A notable omission in Apple's paper is any mention of the hardware used for training <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>. This contrasts with common practice in the field and might indicate a strategic decision by Apple, potentially due to the use of external hardware (like Nvidia GPUs or Google's TPUs) while they develop their own internal chip solutions for [[large_language_models_and_their_applications | large-scale deep learning]] <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a>. Apple's framework, AxLearn, is built on top of JAX and XLA <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>.

## Apple's MM1 Model

Apple's MM1 models are a family of [[Multimodal Language Models | multimodal models]] up to 30 billion parameters, including both dense models and [[efficiency_of_large_language_models | mixture of expert]] (MoE) variants <a class="yt-timestamp" data-t="01:14:47">[01:14:47]</a>. The paper is praised for its extensive detail on ablations and experiments, which is unusual for the typically secretive company <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a> <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

Despite the comprehensive disclosure, one internal, text-only supervised fine-tuning dataset was not publicly released <a class="yt-timestamp" data-t="01:22:42">[01:22:42]</a>. Apple also uses third-party tools for aspects like experiment tracking (Weights & Biases) <a class="yt-timestamp" data-t="01:40:05">[01:40:05]</a> and evaluation (Luther AI's LM Evaluation Harness) <a class="yt-timestamp" data-t="01:36:57">[01:36:57]</a>.