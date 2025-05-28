---
title: Vision language models
videoId: uYb38g-weEY
---

From: [[hu-po]] <br/> 

[[Vision language models and their applications | Vision language models]] are a rapidly evolving area in AI, with models continually improving month over month <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. These models combine visual understanding with language processing to interpret complex information <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>.

## Current State and Challenges
One of the main challenges for [[Vision language models and their applications | Vision language models]] is accurately interpreting complex visual information, especially when it involves subtle manipulations or requires detailed understanding beyond surface-level features <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>. For example, a benchmark test involving an image of Barack Obama with Dwayne "The Rock" Johnson's face Photoshopped onto it proves difficult for most VLMs, as they tend to identify the person as Barack Obama due to the overwhelming visual cues from the original image <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Only Perplexity, utilizing GPT-4 Vision, successfully identified the image as digitally manipulated <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. This highlights a common issue where [[vision_language_models_and_their_applications | vision encoders]] can lose information during the conversion of images into vision tokens <a class="yt-timestamp" data-t="01:20:58">[01:20:58]</a>.

Proprietary models like GPT-4 Vision often perform well but may be subject to safety guardrails that prevent them from answering certain queries, such as identifying individuals in images <a class="yt-timestamp" data-t="00:59:52">[00:59:52]</a>. Open-source models are progressing but still face challenges in catching up to state-of-the-art closed-source models <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>.

## Key Architectures and Concepts

### Llava (Llama-based Vision Language Model)
Llava is a prominent [[Vision language models and their applications | VLM]] known for its open-source nature. Llava v1.6 is an improvement over v1.5, featuring increased input image resolution (from 336x336 to higher, though achieved by tiling images) <a class="yt-timestamp" data-t="01:30:29">[01:30:29]</a>, <a class="yt-timestamp" data-t="01:38:13">[01:38:13]</a>, and enhanced visual reasoning and [[vision_language_models_and_their_applications | OCR (Optical Character Recognition)]] capabilities due to better tuning data mixtures <a class="yt-timestamp" data-t="01:31:01">[01:31:01]</a>. The model also boasts improved visual conversation, world knowledge, and logical reasoning <a class="yt-timestamp" data-t="01:31:28">[01:31:28]</a>. Llava v1.6 is truly open-source, providing access to its code, data, and model weights <a class="yt-timestamp" data-t="01:31:48">[01:31:48]</a>. The 34B variant can be trained in one day using 32 A100 GPUs <a class="yt-timestamp" data-t="01:32:23">[01:32:23]</a>.

Llava models typically undergo a two-stage training procedure:
1.  **Stage 1:** Training a connector (an MLP) that projects image tokens from a frozen vision encoder (like CLIP Large) into the input domain of a frozen language model <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>. This adapts visual information into "pseudo text tokens" that the language model can understand <a class="yt-timestamp" data-t="01:43:30">[01:43:30]</a>.
2.  **Stage 2:** Fine-tuning the entire model (including the language model and connector) with instruction-tuned image-response datasets <a class="yt-timestamp" data-t="01:47:47">[01:47:47]</a>.

### Mixture of Experts (MoE) in VLMs
[[Vision language models with pretrained components | Mixture of Experts (MoE)]] models are a promising approach to scale model capacity without significantly increasing computational cost for *inference* <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>. They replace a single feed-forward network (FFN) within a Transformer block with multiple "experts" (each an MLP) and a "router" <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

*   **Experts:** These are individual Multi-Layer Perceptrons (MLPs) or Feed-Forward Networks (FFNs) <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.
*   **Router:** A key component that decides which subset of experts will process the feature embeddings (tokens) <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The router's parameters are trained in conjunction with other network parameters to learn appropriate routing <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>. Noise can be added to improve numerical stability and encourage routing diversity <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>.

**Types of MoE:**
*   **Sparse MoE:** Uses binary or hard assignment, meaning only selected experts (e.g., top-K, where K is typically 2) process the tokens, while others are "zeroed out" <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This approach can be non-differentiable, making gradient propagation challenging <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.
*   **Soft MoE:** Uses a soft assignment and weighted combinations of expert outputs <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. This is generally preferred for its differentiability, allowing for smoother gradient flow during training <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

**Router Variants:**
*   **Token Choice:** Matches experts to each token <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.
*   **Expert Choice:** Matches tokens to each expert <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. Empirically, expert choice routers perform better in sparse MoE for computer vision tasks <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

**Training MoE Models (MoE-Llava):**
MoE-Llava utilizes a three-stage training process <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>:
1.  **Stage 1:** Train the MLP (connector) between a frozen vision encoder (CLIP Large) and a frozen language model, using text-captioned images <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>.
2.  **Stage 2:** Train the entire language model (excluding the frozen vision encoder) using instruction-response image datasets <a class="yt-timestamp" data-t="00:40:32">[00:40:32]</a>.
3.  **Stage 3:** Experts (MLPs) are initialized from the previously trained FFNs, and only the MoE layers are trained, along with the router <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>. An auxiliary "differentiable load balancing loss" is applied to encourage experts to handle tokens in a balanced manner, preventing over-specialization to specific experts <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a>.

**Performance and Considerations:**
MoE models claim a "constant computational cost" by activating only a subset of parameters <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>. However, this "activated parameters" metric can be misleading. While fewer parameters are *active* during a single inference, the entire model (including all experts) must still be loaded into memory. This makes MoE potentially slower on single GPUs due to VRAM loading/unloading inefficiencies, but highly efficient for batched inference on multi-GPU server setups where experts can be sharded across different GPUs <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

Analysis of expert loading in MoE-Llava shows that different experts tend to be active in different layers of the model, with some focusing on early layers (low-level features) and others on later layers (higher-level abstractions) <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>. The experts also appear to focus equally on visual and text tokens, preventing modality-specific over-specialization <a class="yt-timestamp" data-t="00:59:10">[00:59:10]</a>.

### InternLM-XComposer2 (LoRA for Vision Encoder)
This model introduces a novel approach by using LoRA (Low-Rank Adaptation) to fine-tune the vision encoder itself, instead of relying on a separate MLP connector <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>. This partial LoRA approach allows for efficient adaptation of the vision model to produce more "tokeny and semantic" visual features, making them more compatible with language models <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.

### Moy Poly Visual Expert (Ensemble of Visual Encoders)
This paper proposes using an ensemble of diverse visual encoders ("poly visual experts") to overcome limitations of single visual components, such as insufficient capabilities and excessively long visual tokens <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>. Each expert (e.g., CLIP, DinoV2, Segment Anything Model (SAM), LayoutLMv3) contributes different strengths, such as semantic understanding, robust feature extraction, or segmentation <a class="yt-timestamp" data-t="01:09:52">[01:09:52]</a>.

Key aspects:
*   **Multiple Visual Encoders:** Instead of one, the model uses several, each specializing in different visual processing tasks (e.g., CLIP for semantic alignment, DinoV2 for self-supervised feature extraction, SAM for detailed segmentation) <a class="yt-timestamp" data-t="01:04:31">[01:04:31]</a>.
*   **Poly Expert Fusion Network:** This network unifies the outputs from different visual experts, which may have varying token counts and dimensionalities <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>. An MLP-based fusion method was found to be more effective and parameter-efficient than Q-Former based fusion <a class="yt-timestamp" data-t="01:23:42">[01:23:42]</a>.
*   **Positional Encoding Schemes:** The paper explores different strategies for positional encoding to reduce computational waste from lengthy image feature sequences <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>. Simplifying positional encodings (e.g., using the same encoding for all patches or for entire rows/columns) can significantly reduce memory and computation without significant performance degradation, suggesting that detailed positional embeddings might not always be necessary for vision encoders in VLMs <a class="yt-timestamp" data-t="01:21:50">[01:21:50]</a>.
*   **Expert Order:** The order in which the visual expert outputs are concatenated and fed into the language model affects the final output due to the language model's auto-regressive and position-aware characteristics <a class="yt-timestamp" data-t="01:24:24">[01:24:24]</a>.

This ensemble approach consistently shows superior performance over models using isolated visual encoders, with performance improving as more experts are integrated <a class="yt-timestamp" data-t="01:07:30">[01:07:30]</a>. This highlights a promising direction for enhancing VLM capabilities.

## Benchmarking and Performance Evaluation
[[benchmarking_vision_models | Benchmarking vision models]] is complex due to the rapid pace of development and varying evaluation metrics <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. Different papers often use slightly different benchmarks or calculation methods, making direct [[comparison_of_vision_architectures | comparison of vision architectures]] challenging <a class="yt-timestamp" data-t="01:33:17">[01:33:17]</a>. There's a need for standardized, comprehensive benchmarks specifically designed for modern VLMs, rather than relying on older classification tasks like ImageNet <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

The trend for achieving state-of-the-art performance in VLMs, similar to large language models, increasingly involves higher computational budgets and complex inference pipelines, rather than just architectural breakthroughs <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>. This suggests a future where performance is a function of computational resources, leading to a need for metrics like "state-of-the-art per compute budget" <a class="yt-timestamp" data-t="01:36:52">[01:36:52]</a>.

## Conclusion and Future Directions
[[Future directions and implications of AI in vision language models | Vision language models]] are continuously advancing, with promising concepts like [[vision_language_models_with_pretrained_components | Mixture of Experts]] and the integration of multiple visual encoders showing significant potential. While proprietary models like GPT-4 Vision set a high bar, open-source initiatives like Llava are making substantial progress in accessibility and capability <a class="yt-timestamp" data-t="01:42:48">[01:42:48]</a>. The idea of leveraging diverse [[vision_language_models_with_pretrained_components | vision encoders]] to enrich contextual understanding is a particularly powerful insight that is likely to become more common <a class="yt-timestamp" data-t="01:54:02">[01:54:02]</a>. Further research may explore the optimal ordering of multi-modal tokens within the language model's input sequence to maximize performance <a class="yt-timestamp" data-t="01:55:02">[01:55:02]</a>.