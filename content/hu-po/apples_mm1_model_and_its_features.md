---
title: Apples MM1 model and its features
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 

Apple has introduced its new **MM1 model**, a family of [[building_multimodal_models | multimodal models]] primarily focused on vision and language tasks <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Released on March 14, 2024, the associated paper is noted for its extensive detail, covering ablations, experiments, learning rates, and data sets <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This level of transparency is considered unusual for Apple, a company known for its secrecy <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Naming Convention
The paper describes MM1 as a "multimodal large language model" (MLLM) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The speaker, however, suggests that "Vision Language Model" (VLM) would be a more precise term, as MM1 primarily handles vision and text modalities, not all possible modalities like audio or vibration data <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This naming choice might reflect Apple's desire to "own the category" or influence search engine optimization (SEO) by introducing a new term, similar to their "spatial computing" branding for VR headsets <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## Key Design Decisions and Lessons Learned
Apple's comprehensive ablation studies identified several crucial design lessons for [[pretraining_and_finetuning_strategies_in_mm1 | building performant multimodal models]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
*   **Image Resolution**: Has the highest impact on final model performance <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.
*   **Visual Encoder Loss and Capacity**: A larger visual encoder is important for performance <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
*   **Visual Encoder Pre-training Data**: The composition and mix of data are critical <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.

### Image Encoder Pre-training
The image encoder, a Vision Transformer (ViT) Large 14, is trained using a [[pretraining_and_finetuning_strategies_in_mm1 | CLIP loss]] <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.
*   **Contrastive Losses**: Such as CLIP, endow the visual encoder with semantic knowledge by pulling similar representations closer and pushing dissimilar ones apart in the embedding space <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>.
*   **Reconstructive Losses**: Explicitly capture all parts of an image, leading to more nuanced and low-level features, like those from DinoV2 <a class="yt-timestamp" data-t="00:33:48">[00:33:48]</a>.
Apple chose to train its own image encoder from scratch, which is unusual for most academic or open-source VLM papers that typically use pre-trained and frozen encoders from other entities like Meta or OpenAI <a class="yt-timestamp" data-t="00:47:05">[00:47:05]</a>.

### Vision-Language Connector (Projector)
The design of the vision-language connector, or projector, which adapts visual features to be compatible with the large language model (LLM), has a comparatively negligible impact on performance <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This finding supports the "bitter lesson" in AI, suggesting that architectural intricacies matter less than data and scale <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>. Despite this, MM1 utilizes a C-abstractor for its connector, rather than a simpler linear projector <a class="yt-timestamp" data-t="01:00:47">[01:00:47]</a>.

### Pre-training Data Mix
A careful mix of image caption, interleaved image-text, and text-only data is crucial for achieving state-of-the-art few-shot results across multiple [[multimodal_model_benchmarks | benchmarks]] <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>.
*   **Captioning Data**: Contains relatively short text highly relevant to an image, lifting zero-shot performance <a class="yt-timestamp" data-t="00:53:41">[00:53:41]</a>.
*   **Interleaved Data**: Features substantially longer and more diverse text, often loosely related to surrounding images (e.g., news articles with pictures), instrumental for few-shot and text-only performance <a class="yt-timestamp" data-t="00:53:49">[00:53:49]</a>.
*   **Text-only Data**: Helps the LLM retain strong text-reading capabilities, preventing it from ignoring text and focusing solely on vision <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.

The final data mix for MM1's [[pretraining_and_finetuning_strategies_in_mm1 | pre-training]] consists of:
*   45% captioned images <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>
*   45% interleaved image-text documents <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>
*   10% text-only data <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>

Synthetic caption data, such as the vCap 300M dataset, provided a non-trivial performance boost (2-4%) in few-shot learning <a class="yt-timestamp" data-t="00:58:35">[00:58:35]</a>.

## Model Architecture
MM1 is a family of [[transformer_models_and_moes | multimodal models]] with sizes up to 30 billion parameters, including both dense models and [[transformer_models_and_moes | Mixture of Expert (MoE)]] variants <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
*   **Language Model**: A decoder-only language model is used, ranging from 1.2 billion parameters (for ablation studies) up to 30 billion parameters for the most performant models <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
*   **[[transformer_models_and_moes | Mixture of Experts (MoE)]]**: MM1 uses MoE variants with 32 and 64 experts. The "top-two gating" strategy means only two of the available experts are activated for any particular token, allowing the model to have greater capacity while keeping activated parameters constant during inference <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>. Load balancing techniques are employed during training to ensure all experts are utilized equally and prevent atrophy <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## Performance and Benchmarks
MM1 achieves competitive performance on established [[multimodal_model_benchmarks | multimodal benchmarks]] and state-of-the-art results on certain pre-training metrics <a class="yt-timestamp" data-t="00:40:41">[00:40:41]</a>.
*   **State-of-the-Art Claims**: MM1 (3B, 7B, 30B variants) outperforms older or more open models like Flamingo and Emu2 on specific benchmarks <a class="yt-timestamp" data-t="01:17:31">[01:17:31]</a>.
*   **Competitive Performance**: When compared against top models like GPT-4V and Gemini Ultra, MM1's performance is competitive but not consistently superior <a class="yt-timestamp" data-t="01:31:07">[01:31:07]</a>. For example, on a VQA benchmark, GPT-4V scored 78, Gemini Ultra 82, and MM1 30B chat scored 73 <a class="yt-timestamp" data-t="01:31:16">[01:31:16]</a>.
*   **Scaling Laws**: Performance consistently improves with increased image resolution, more image tokens, and additional pre-training steps, indicating that current models are not hitting a performance wall related to scale <a class="yt-timestamp" data-t="01:33:19">[01:33:19]</a>.

## Training Strategy
MM1 employs a two-stage [[pretraining_and_finetuning_strategies_in_mm1 | training pipeline]]: pre-training followed by supervised fine-tuning <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.
*   **Unfrozen Encoders**: Both the image encoder and the LLM are kept entirely unfrozen during both pre-training and supervised fine-tuning, allowing gradients to propagate throughout the entire model. This differs from many other VLM papers that freeze pre-trained encoders <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a>.
*   **Supervised Fine-tuning (SFT) Data**: The SFT data sets used, such as LLaVA, are largely generated by GPT-4 and GPT-4V <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>. This effectively means MM1 is "distilling" knowledge from GPT-4V <a class="yt-timestamp" data-t="01:20:47">[01:20:47]</a>. Apple also uses a small internal text-only dataset for SFT, similar to ShareGPT <a class="yt-timestamp" data-t="01:22:48">[01:22:48]</a>.
*   **Hardware (Undisclosed)**: The paper notably omits any mention of the hardware used for training (e.g., GPUs, TPUs) <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>. The speaker speculates this is intentional, perhaps to avoid acknowledging reliance on Nvidia GPUs or Google's TPUs while Apple works on its own proprietary chips <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.
*   **Frameworks**: Apple uses the AxLearn framework, built on top of Jax and XLA, for model development <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. For evaluation, they utilize an internal fork of the Luther AI LM evaluation harness <a class="yt-timestamp" data-t="01:36:59">[01:36:59]</a>. Weights and Biases is used for experiment tracking <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.

## Qualitative Examples
MM1 demonstrates impressive capabilities, including:
*   **Object Counting**: Accurately counts objects in an image <a class="yt-timestamp" data-t="01:24:24">[01:24:24]</a>.
*   **Optical Character Recognition (OCR)**: Successfully reads scene text, even if handwritten, fuzzy, or very small/large <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>.
*   **Refusal to Hallucinate**: The model can correctly state when an object is not present in an image, indicating proper tuning to avoid fabricating information <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>.
*   **Multi-Image Reasoning**: Can interleave text and multiple images, answering questions related to the combined context <a class="yt-timestamp" data-t="01:17:28">[01:17:28]</a>.
*   **Enhanced In-Context Learning & Few-Shot Chain-of-Thought**: Leveraging large-scale [[pretraining_and_finetuning_strategies_in_mm1 | pre-training]], MM1 exhibits strong in-context learning abilities, multi-image reasoning, and supports few-shot Chain-of-Thought prompting <a class="yt-timestamp" data-t="01:54:53">[01:54:53]</a>.

### Image Handling
MM1 supports various image resolutions <a class="yt-timestamp" data-t="01:39:06">[01:39:06]</a>. For very large input images, it can downsample the image, or resize and divide it into four sub-images to manage computational load <a class="yt-timestamp" data-t="01:42:08">[01:42:08]</a>. While the paper states support for square resolutions (e.g., 378x378, 672x672), examples show it can process non-square images, suggesting complex internal handling such as dynamic cropping or multi-cropping strategies to preserve information <a class="yt-timestamp" data-t="01:42:51">[01:42:51]</a>.