---
title: LLaVA  Large Language and Visual Assistant
videoId: BJ98vicRYHg
---

From: [[hu-po]] <br/> 

LLaVA, which stands for Large Language and Visual Assistant, is a significant open-source project that integrates [[llm_large_language_models_development | large language models]] (LLMs) with visual understanding capabilities <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. It is considered one of the best [[opensource_advancements_in_visionlanguage_models | open-source vision-language models]] available <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. LLaVA demonstrates impressive multimodal chat abilities, sometimes exhibiting behaviors akin to multimodal [[multimodal_large_language_models_vs_vision_language_models | GPT-4 Vision]] on unseen images and instructions <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

## Development and Versions

LLaVA is the result of multiple papers and extensive work, primarily by Haotian Liu and Chunyuan Li <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. Haotian Liu, a PhD student at Wisconsin, contributed significantly through internships at Microsoft Research <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

The project has evolved through two main iterations:
*   **LLaVA 1.0**: The first paper, titled "Visual Instruction Tuning," was released on April 17th <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.
*   **LLaVA 1.5**: The more recent continuation of the work, released on October 5th, brings significant improvements <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. LLaVA 1.5 achieves state-of-the-art (SoTA) results on 11 different benchmarks <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.

## Architecture

LLaVA represents a novel end-to-end trained [[multimodal_large_language_models_vs_vision_language_models | large multimodal model]] that combines a vision encoder and an LLM for general-purpose visual and language understanding <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

Its architecture comprises three main components:
1.  **Vision Encoder (Vision Backbone)**: This component consumes raw images and provides a rich feature representation of that image <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. LLaVA primarily uses OpenAI's [[comparison_of_different_vision_language_models | CLIP]] (Contrastive Language-Image Pre-training) ViT-L/14 Vision Transformer <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
    *   CLIP processes images by cutting them into patches (e.g., 14x14 pixels) and treating them as a sequence of image patches, similar to how text is handled <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.
    *   LLaVA 1.5 specifically upgraded to a CLIP model with a slightly larger image resolution (336x336 pixels compared to the original 224x224) <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>.
    *   CLIP models are pre-trained using a contrastive loss, pulling related images and text together in an embedding space while pushing unrelated ones apart <a class="yt-timestamp" data-t="08:57:00">[08:57:07]</a>.
2.  **[[llm_large_language_models_development | Large Language Model]] (LLM)**: LLaVA utilizes [[llm_large_language_models_development | Vicuna]], which is a variant of [[llm_large_language_models_development | LLaMA]] (specifically [[llm_large_language_models_development | LLaMA]] 1 13B parameters) <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>. Vicuna is fine-tuned on [[llm_large_language_models_development | GPT-4]] answers <a class="yt-timestamp" data-t="16:56:00">[16:56:00]</a>.
3.  **Vision-Language Connector**: This is a simple projection matrix, specifically a multi-layer perceptron (MLP) <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>. It connects the visual features from the vision encoder to the word embedding space of the LLM <a class="yt-timestamp" data-t="32:41:00">[32:41:00]</a>. This layer is the only part trained from scratch in LLaVA's architecture <a class="yt-timestamp" data-t="34:03:00">[34:03:00]</a>. In LLaVA 1.5, this connector was improved from a single linear layer to a two-layer MLP <a class="yt-timestamp" data-t="00:13:57">[01:13:57]</a>.

## Training Methodology

LLaVA employs a two-stage instruction tuning procedure <a class="yt-timestamp" data-t="41:14:00">[41:14:00]</a>:

1.  **Stage 1: Pre-training for Feature Alignment**:
    *   This stage focuses on aligning the image features with the pre-trained LLM's word embeddings <a class="yt-timestamp" data-t="48:34:00">[48:34:00]</a>.
    *   It uses a filtered subset of CC3M (Conceptual Captions 3 Million) image-text pairs, converted into single-turn instruction-following data (e.g., "describe this image") <a class="yt-timestamp" data-t="45:27:00">[45:27:00]</a>.
    *   During this stage, both the vision encoder and the LLM are frozen, meaning only the projection matrix (the MLP connector) is trained <a class="yt-timestamp" data-t="46:57:00">[46:57:00]</a>. This makes the training memory-efficient and allows it to run on consumer GPUs <a class="yt-timestamp" data-t="47:17:00">[47:17:00]</a>.

2.  **Stage 2: Fine-tuning for Instruction Following**:
    *   In this stage, the vision encoder remains frozen, but the weights of the LLM (Vicuna) are updated along with the projection layer <a class="yt-timestamp" data-t="49:25:00">[49:29:00]</a>.
    *   The LLM is fine-tuned using a LoRA (Low-Rank Adaptation) technique, which is merged with the final Vicuna model <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>.
    *   The data used for this stage includes 158K unique language-image instruction-following data sets, with conversations often being multi-turn <a class="yt-timestamp" data-t="51:27:00">[51:27:00]</a>.
    *   A significant portion of this data is machine-generated instruction-following data, created by prompting the language-only [[llm_large_language_models_development | GPT-4]] with image captions and bounding box descriptions to generate question-answer pairs <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>. The visual image itself is not used to prompt [[llm_large_language_models_development | GPT-4]] for this generation <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
    *   LLaVA 1.5 also incorporates additional academic task-oriented visual question answering (VQA) data, including [[comparison_of_different_vision_language_models | OCR]] VQA data sets, with specific response formatting <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>. This emphasizes the growing importance of data mixture and prompt engineering in [[llm_large_language_models_development | machine learning]] research <a class="yt-timestamp" data-t="01:06:42">[01:06:42]</a>.

The entire fine-tuning process for LLaVA 1.5 takes approximately one day on a single A100 node (8 A100 GPUs), specifically 6 hours for pre-training and 20 hours for visual instruction tuning <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>, <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

## Performance and Capabilities

LLaVA 1.5 achieves [[comparison_of_different_vision_language_models | state-of-the-art]] accuracy on 11 out of 12 benchmarks, including the Science QA benchmark where it reached 92% accuracy <a class="yt-timestamp" data-t="01:00:15">[01:00:15]</a>, <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. This performance is achieved with significantly less compute and training data compared to other methods <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

Key capabilities demonstrated by LLaVA include:
*   **Multimodal Chat**: LLaVA can engage in conversations based on images, sometimes exhibiting behaviors similar to [[multimodal_large_language_models_vs_vision_language_models | GPT-4 Vision]] <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **[[comparison_of_different_vision_language_models | OCR]] (Optical Character Recognition)**: The model can read and interpret text within images <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>. However, it may struggle with very tiny text compared to [[multimodal_large_language_models_vs_vision_language_models | GPT-4 Vision]], suggesting GPT-4V uses a higher resolution vision encoder <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.
*   **Factual Understanding**: LLaVA 1.5, when fine-tuned on appropriate data, can identify factual errors in prompts and correct the user <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.
*   **Multilingual Instructions**: Despite not being explicitly fine-tuned for it, LLaVA 1.5 can follow multilingual instructions, partly due to the multilingual nature of the underlying [[llm_large_language_models_development | language models]] like [[llm_large_language_models_development | LLaMA]] <a class="yt-timestamp" data-t="01:38:30">[01:38:30]</a>.

## Open-Source Nature and Reproducibility

A key aspect that distinguishes LLaVA is its commitment to transparency and reproducibility <a class="yt-timestamp" data-t="01:32:59">[01:32:59]</a>. The model and its code are publicly available <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
*   **Code and Model Weights**: The project releases all code, including the training scripts, and model weights <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. This level of transparency is considered "effectively as open source as you can get in 2023 in the AI space" <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **Data Mixture**: Crucially, the papers provide the exact data mixture used for training, including hyper-parameters and training recipes, which is vital for reproducibility <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>, <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>.
*   **Licensing**: While LLaVA follows the same license as [[llm_large_language_models_development | LLaMA]] 2, which has commercial restrictions in certain contexts, the composite nature of the model (using [[llm_large_language_models_development | GPT]]-generated data, [[comparison_of_different_vision_language_models | CLIP]], and [[llm_large_language_models_development | LLaMA]]) creates complex licensing scenarios <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Despite this, some interpret the enforcement of such licenses to be lax for smaller-scale or research use <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## Limitations and Future Outlook

Despite its impressive performance, LLaVA has acknowledged limitations:
*   **Context Length**: It struggles with processing multiple images due to the lack of sufficient instruction-following data and context length limitations <a class="yt-timestamp" data-t="01:40:39">[01:40:39]</a>.
*   **Problem-Solving**: While proficient in complex instructions, its problem-solving capabilities can still be limited in certain specific domains <a class="yt-timestamp" data-t="01:40:49">[01:40:49]</a>.
*   **[[challenges_with_large_language_models_and_hallucinations | Hallucination]]**: LLaVA is not exempt from occasionally disseminating misinformation or "[[challenges_with_large_language_models_and_hallucinations | hallucinating]]" <a class="yt-timestamp" data-t="01:40:56">[01:40:56]</a>.

Future directions for LLaVA and similar models include:
*   **[[large_language_models_llms_and_scaling | Scaling]] Data and Models**: Pre-training on larger image-text datasets and applying data generation pipelines to more extensive datasets can increase concept coverage <a class="yt-timestamp" data-t="01:53:41">[01:53:41]</a>. Scaling to larger [[llm_large_language_models_development | LLMs]] like [[llm_large_language_models_development | LLaMA]] 2 70B is expected to yield even better results <a class="yt-timestamp" data-t="01:31:56">[01:31:56]</a>.
*   **Integration with Other Vision Models**: Connecting LLaVA with other powerful vision models, such as Meta's Segment Anything Model (SAM), could enhance its capabilities <a class="yt-timestamp" data-t="01:54:22">[01:54:22]</a>. An ensemble approach, feeding outputs from multiple vision encoders into the [[llm_large_language_models_development | language model]], is also a promising area <a class="yt-timestamp" data-t="01:55:47">[01:55:47]</a>.
*   **Synthetic Data Generation**: Using existing [[llm_large_language_models_development | models]] (like [[multimodal_large_language_models_vs_vision_language_models | GPT-4 Vision]] or LLaVA itself) to generate new datasets for training even better [[llm_large_language_models_development | models]] is a growing paradigm <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>, <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. This creates a "virtuous cycle" of self-improvement <a class="yt-timestamp" data-t="01:46:42">[01:46:42]</a>.
*   **Prompt Engineering**: The importance of careful [[selfimprovement_and_planning_for_large_language_models | prompt engineering]] remains critical, influencing the model's ability to adjust output formats and follow instructions <a class="yt-timestamp" data-t="01:38:39">[01:38:39]</a>, <a class="yt-timestamp" data-t="01:11:17">[01:11:17]</a>.

LLaVA's success with a relatively simple architecture and accessible training requirements suggests that effectively combining powerful pre-trained components and curating high-quality fine-tuning data (especially synthetic data) is a highly effective approach in modern [[llm_large_language_models_development | AI research]] <a class="yt-timestamp" data-t="01:35:35">[01:35:35]</a>. This provides hope for [[opensource_advancements_in_visionlanguage_models | open-source advancements in vision-language models]] <a class="yt-timestamp" data-t="01:52:53">[01:52:53]</a>.