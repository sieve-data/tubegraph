---
title: Interleaving and blending techniques in multimodal models
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

[[multimodal_large_language_models_vs_vision_language_models | Vision-language models (VLMs)]] and [[multimodal_large_language_models_vs_vision_language_models | multimodal large language models (MLLMs)]] integrate visual and textual information to understand and generate content. Key to their functionality are interleaving and blending techniques, which govern how different modalities are combined and processed during training and inference <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

## Defining Modalities and Models
A modality refers to a specific type of data, such as text, image, or audio <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>. While the community has not yet settled on a specific acronym, these models are fundamentally combinations of some visual model and a [[multimodal_capabilities_in_language_models | large language model]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

Different terms used for these models include:
*   [[multimodal_large_language_models_vs_vision_language_models | Multimodal Large Language Models (MLLMs)]] <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>
*   Large Multimodal Models (LMMs) <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>
*   [[multimodal_large_language_models_vs_vision_language_models | Vision Language Models (VLMs)]] <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>
*   Large Scale Vision Language Models (LSVLMs) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>

## Core Components
Most [[building_multimodal_models | multimodal models]] generally follow a similar architectural pattern: an image input is processed by a [[multimodal_embeddings_and_clip_comparison | vision encoder]], and textual input by a text tokenizer/embedding module. These encoded representations are then fed into a [[multimodal_capabilities_in_language_models | large language model]] <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>. The connection between the vision encoder and the language model often involves a "fusion layer" or "adapter," which is a small neural network, commonly a Multi-Layer Perceptron (MLP) <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.

## Interleaving Modalities
Interleaving refers to the arrangement and combination of different modalities (images and text) within the input sequence to the [[multimodal_capabilities_in_language_models | large language model]].
*   **Deep Speed Visual Chat:** This Microsoft research group emphasizes the ability to adeptly manage interleaved image-text inputs in multi-image, multi-round dialogues <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>. They introduce an "Innovative Multimodal Causal Attention Mechanism" that allows for a more nuanced attention map, where image tokens can pay attention to only other image tokens, or text tokens, and vice-versa <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>. This contrasts with simpler approaches that might just concatenate image and text tokens <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
*   **Quen VL (Alibaba):** This model explicitly allows for "arbitrarily interleaved image text data" in its training phase, similar to Deep Speed's focus on mixed inputs <a class="yt-timestamp" data-t="00:47:55">[00:47:55]</a>.

## Blending Techniques and Architectures
Blending techniques involve how information from different encoders or different parts of encoders is combined to enrich the overall representation.

### Visual Encoder Fusion
*   **Comm Model (Huawei):** This paper explores combining [[multimodal_embeddings_and_clip_comparison | multiple vision encoders]] to improve performance. Specifically, it fuses visual embeddings from [[multimodal_embeddings_and_clip_comparison | CLIP]] (trained contrastively by OpenAI) and DinoV2 (a self-supervised [[multimodal_embeddings_and_clip_comparison | vision transformer]] by Meta) <a class="yt-timestamp" data-t="03:00:54">[03:00:54]</a>.
    *   The rationale is that different vision encoders capture different types of information (e.g., [[multimodal_embeddings_and_clip_comparison | CLIP]] for global semantic information, DinoV2 for fine-grained pixel information) <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>.
    *   They also emphasize "multi-level feature fusion," where features from intermediate layers of the [[multimodal_embeddings_and_clip_comparison | vision transformer]] blocks are combined, rather than just the final output <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>. This is based on the idea that shallow layers capture low-level details, useful for fine-grained tasks <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.
    *   While showing a slight improvement in Visual Question Answering (VQA) when combining [[multimodal_embeddings_and_clip_comparison | CLIP]] and DinoV2, the marginal gain might not justify the increased inference cost and complexity <a class="yt-timestamp" data-t="01:25:50">[01:25:50]</a>.

### Connecting Encoders to the Language Model (Adapters/Connectors)
*   **MLP vs. Cross-Attention:**
    *   Many models, like LLaVA, use a simple Multi-Layer Perceptron (MLP) to connect the [[multimodal_embeddings_and_clip_comparison | vision encoder]]'s output to the [[multimodal_capabilities_in_language_models | language model]] <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>. This MLP is often the only part that receives gradients during training, while the [[multimodal_embeddings_and_clip_comparison | vision encoder]] is frozen to save computational resources <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.
    *   [[chameleon_mixed_modal_model | Quen VL]] uses a "position-aware vision-language adapter" which is a single-layer cross-attention module, a more complex approach than a simple MLP <a class="yt-timestamp" data-t="00:49:19">[00:49:19]</a>. However, Deep Speed Visual Chat experimented with a [[multimodal_embeddings_and_clip_comparison | vision transformer]] layer as a projection layer between encoders but "did not observe any benefits," suggesting a simple linear layer or MLP might suffice <a class="yt-timestamp" data-t="01:31:54">[01:31:54]</a>.

## Data Blending and Augmentation
Given the scarcity of high-quality, interleaved image-text datasets, researchers employ data blending techniques:
*   **Synthetic Data Generation:** Models like LLaVA create synthetic instruction-tuning datasets by using [[multimodal_capabilities_in_language_models | large language models]] (e.g., GPT-4) to generate fake conversations about images <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>.
*   **Shuffling and Manipulation:** Deep Speed Visual Chat mentions experimenting with shuffling image IDs in datasets like Otter (a [[multimodal_capabilities_in_language_models | multimodal in-context instruction tuning]] dataset) to create new interleaved examples <a class="yt-timestamp" data-t="01:32:59">[01:32:59]</a>. However, such intricate data blending methods can lead to "deteriorated performances characterized by incomplete sentences and incorrect references," highlighting the challenge of maintaining data cleanliness and semantic integrity <a class="yt-timestamp" data-t="01:36:21">[01:36:21]</a>.

## Training Recipes and Observations
Different papers present varied training recipes that implicitly involve blending and interleaving strategies:
*   **[[chameleon_mixed_modal_model | Quen VL]]'s Multi-Stage Training:** This model employs a complicated multi-stage training recipe:
    1.  **Pre-training:** Freezing the [[multimodal_capabilities_in_language_models | language model]] and training the connector (cross-attention module) and [[multimodal_embeddings_and_clip_comparison | vision transformer]] <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>.
    2.  **Multi-task Pre-training:** Training with interleaved [[multimodal_capabilities_in_language_models | vision-language data]] and pushing gradients into everything <a class="yt-timestamp" data-t="00:52:44">[00:52:44]</a>.
    3.  **Supervised Fine-tuning:** Freezing the [[multimodal_embeddings_and_clip_comparison | vision encoder]] and only pushing gradients into the [[multimodal_capabilities_in_language_models | language model]] and cross-attention module <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.
*   **Importance of Pre-trained Components:**
    *   [[building_multimodal_models | Pali]] (Google) found that [[multimodal_embeddings_and_clip_comparison | contrastively pre-trained vision encoders]] (like [[multimodal_embeddings_and_clip_comparison | CLIP]]) lead to better and more efficient [[multimodal_large_language_models_vs_vision_language_models | vision language models]], especially for localization and text understanding tasks, compared to classification-based ones <a class="yt-timestamp" data-t="01:42:01">[01:42:01]</a>. This suggests that the initial training objective of the visual component significantly impacts its utility in a [[building_multimodal_models | multimodal context]] <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.
    *   Deep Speed observed that using a better [[multimodal_embeddings_and_clip_comparison | visual encoder]] (specifically, the one from [[chameleon_mixed_modal_model | Quen VL]], which is an [[multimodal_embeddings_and_clip_comparison | OpenCLIP]] fine-tuned by [[chameleon_mixed_modal_model | Quen VL]]) significantly improves the final model quality, partially due to higher output resolution <a class="yt-timestamp" data-t="00:59:04">[00:59:04]</a>.
*   **Model Size Mismatch:** There can be a mismatch in scales between the [[multimodal_embeddings_and_clip_comparison | vision encoder]] and [[multimodal_capabilities_in_language_models | language model]], e.g., a 2B visual encoder with a 70B [[multimodal_capabilities_in_language_models | Llama 2]] language decoder, which might be overkill and not yield optimal results <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>.

## Conclusion
Interleaving and blending techniques are crucial for enabling [[multimodal_capabilities_in_language_models | multimodal models]] to process and understand complex inputs that combine images and text. From nuanced attention mechanisms to fusing features from different [[multimodal_embeddings_and_clip_comparison | vision encoders]] and layers, researchers continue to refine how these modalities are integrated. However, challenges remain, particularly in the creation and cleanliness of blended datasets. The choice of pre-trained components (like [[multimodal_embeddings_and_clip_comparison | contrastively trained vision encoders]]) and the architecture of the connecting "adapter" layer also play significant roles in the overall performance and efficiency of these [[multimodal_large_language_models_vs_vision_language_models | models]].