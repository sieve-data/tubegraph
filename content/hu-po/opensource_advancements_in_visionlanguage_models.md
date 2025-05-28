---
title: Opensource advancements in VisionLanguage Models
videoId: BJ98vicRYHg
---

From: [[hu-po]] <br/> 

The development of [[vision_language_models_and_their_advancements | Vision Language Models]] (VLMs) has seen significant advancements, with open-source initiatives playing a crucial role. A notable example is LLaVA, the Large Language and Vision Assistant, which stands out as arguably the best open-source VLM currently available <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## LLaVA: A Breakthrough in Open-Source Multimodal AI

LLaVA represents a significant contribution to the open-source AI community due to its impressive performance, transparent methodology, and accessibility <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>. It is primarily developed by researchers, including Haoran Liu and Chunyuan Li, associated with Columbia University and Microsoft Research <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Key Versions

The LLaVA project has evolved through several iterations:
*   **LLaVA 1.0**: Introduced in April, this version focused on visual instruction tuning <a class="yt-timestamp" data-t="00:59:16">[00:59:16]</a>.
*   **LLaVA 1.5**: Released in October, this updated version achieved state-of-the-art results on 11 different benchmarks <a class="yt-timestamp" data-t="01:00:15">[01:00:15]</a>. This version demonstrated impressive performance using only publicly available data and approximately one day of training on a single A100 node (8 A100 GPUs) <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. It's crucial to note that this "one day of training" refers to *additional tuning* on already pre-trained models, not training from scratch <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Architecture

LLaVA is an end-to-end trained large multimodal model designed for general-purpose visual and language understanding <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>. Its architecture consists of three main components:

1.  **Vision Encoder**: This component consumes raw images and outputs a rich feature representation <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. LLaVA uses OpenAI's CLIP (Contrastive Language-Image Pre-training) ViT (Vision Transformer) large patch 14 <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   **Vision Transformers (ViTs)**: These models process images by cutting them into small patches (e.g., 14x14 pixels) and treating them as a sequence of "image patches," similar to how a language model processes a sequence of word tokens <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
    *   LLaVA 1.5 notably uses a CLIP model with a slightly larger image resolution of 336x336 pixels compared to the 224x224 in LLaVA 1.0 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

2.  **Large Language Model (LLM)**: For its language understanding capabilities, LLaVA employs Vicuna, a variant of LLaMA <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Specifically, it uses the 13-billion parameter version of LLaMA 1, which has been fine-tuned on GPT-4 answers <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

3.  **Vision-Language Connector**: This crucial component bridges the gap between the vision encoder and the LLM. In LLaVA, this is implemented as a simple Multi-Layer Perceptron (MLP) or a "projection matrix" <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This MLP translates the visual features into a format compatible with the LLM's word embedding space <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>. LLaVA 1.5 improved this connector from a single linear layer to a two-layer MLP <a class="yt-timestamp" data-t="01:13:57">[01:13:57]</a>.

## Training Methodology

LLaVA's training process involves a two-stage instruction tuning procedure:

### 1. Data Generation

A key innovation in LLaVA's first paper was the use of machine-generated instruction-following data <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. This was achieved by using the text-only GPT-4 model to generate synthetic image-language data <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. The researchers would feed GPT-4 text descriptions of images, including captions and bounding box coordinates, and then prompt it to answer questions about the described content. Crucially, GPT-4 *did not* see the actual images; it only processed the textual representations <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. This process created a large dataset of question-answer pairs that mimicked conversations about images.

### 2. Two-Stage Instruction Tuning

*   **Stage One: Pre-training for Feature Alignment** <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>
    *   LLaVA uses a filtered subset of the CC3M (Conceptual Captions 3 Million) dataset, containing 595,000 image-text pairs <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>.
    *   During this stage, both the vision encoder (CLIP ViT) and the LLM (Vicuna) are "frozen" (their weights are not updated) <a class="yt-timestamp" data-t="00:46:57">[00:46:57]</a>.
    *   Only the weights of the simple projection matrix (the MLP connector) are trained from scratch. This process aligns the image features generated by the vision encoder with the word embedding space of the LLM <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.

*   **Stage Two: Instruction Tuning with Multimodal Data** <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>
    *   In this stage, the vision encoder remains frozen, but the LLM's weights (specifically, through methods like LoRA) are also updated alongside the projection matrix <a class="yt-timestamp" data-t="00:49:29">[00:49:29]</a>.
    *   This tuning uses a variety of multimodal instruction-following datasets, including the GPT-4 generated data and augmented VQA (Visual Question Answering) datasets like VQA V2, GQA, and OCR VQA <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>. The use of prompt engineering, such as explicitly telling the model to "answer the questions using a single word or phrase," significantly improved performance on specific tasks <a class="yt-timestamp" data-t="01:11:50">[01:11:50]</a>.

### Open-Source Transparency

A standout feature of LLaVA is its commitment to open-source principles <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a>. The project provides:
*   **Model Weights and Code**: The model weights and all relevant code are publicly available <a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>.
*   **Training Scripts**: They even release the exact training scripts, including hyperparameters (e.g., batch size, learning rate, cosine scheduling, worker threads) <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
*   **Data Mixture**: Crucially, the precise data mixture used for training LLaVA 1.5 is disclosed <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>. This level of transparency is rare and highly beneficial for reproducibility and further research <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.

While LLaVA adheres to the LLaMA 2 license, which may limit commercial use for some, the developers argue that its composite nature and the rapidly evolving licensing landscape suggest that enforcement will likely be flexible, especially for smaller entities <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

## Performance and Implications

LLaVA 1.5 achieved state-of-the-art accuracy across 11 benchmarks, demonstrating capabilities comparable to multimodal GPT-4 on unseen images and instructions <a class="yt-timestamp" data-t="00:48:40">[00:48:40]</a>. For example, it achieved 92% accuracy on the ScienceQA benchmark <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>, surpassing previous models.

The success of LLaVA highlights several key trends in modern AI:

*   **Importance of Data and Recipe**: The most significant performance boosts come from the quality and mixture of the training data rather than complex model architectures <a class="yt-timestamp" data-t="01:05:54">[01:05:54]</a>. LLaVA's simple architecture, coupled with well-curated and synthetically generated data, outperforms models with more complex designs <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>.
*   **Leveraging Pre-trained Models**: LLaVA demonstrates that assembling powerful pre-trained components (like CLIP and Vicuna) and then fine-tuning them with relatively little compute can yield impressive results <a class="yt-timestamp" data-t="01:00:45">[01:00:45]</a>. This contrasts with training models entirely from scratch, which is far more computationally expensive.
*   **Prompt Engineering**: Subtle changes in prompt formulation, such as system messages or the order of visual and textual information, can significantly impact model behavior and performance <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>. The inclusion of "negative examples" (where the model is trained to identify and correct factual errors in user prompts) also plays a role in its robust behavior <a class="yt-timestamp" data-t="01:37:59">[01:37:59]</a>.
*   **Accessibility**: The fact that LLaVA can be run locally with modest GPU memory requirements (around 10 GB for inference) makes state-of-the-art VLM research more accessible <a class="yt-timestamp" data-t="01:56:22">[01:56:22]</a>.

### Limitations and Future Work

Despite its strengths, LLaVA 1.5 has limitations:
*   It primarily processes full image patches, which can prolong training <a class="yt-timestamp" data-t="01:39:16">[01:39:16]</a>.
*   It is not yet capable of processing multiple images due to context length limitations and a lack of specific instruction-following data <a class="yt-timestamp" data-t="01:40:39">[01:40:39]</a>.
*   While improved, it can still occasionally hallucinate or disseminate misinformation <a class="yt-timestamp" data-t="01:40:55">[01:40:55]</a>.

Future directions for research include:
*   Scaling to even larger image-text datasets and generating more instruction-following data <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>.
*   Connecting LLaVA with other powerful vision models, such as Meta's Segment Anything Model (SAM), potentially by ensembling multiple vision encoders <a class="yt-timestamp" data-t="00:55:47">[00:55:47]</a>.
*   Exploring the use of even larger LLMs like LLaMA 2 70B within the LLaVA framework <a class="yt-timestamp" data-t="01:31:56">[01:31:56]</a>.

LLaVA's comprehensive open-source release offers a valuable baseline for future research in [[challenges_and_future_directions_in_vision_language_modeling | vision language modeling]], making advancements more reproducible and affordable for the wider AI community <a class="yt-timestamp" data-t="01:33:02">[01:33:02]</a>. This approach of "gluing together" pre-trained models with targeted fine-tuning contrasts with the more resource-intensive end-to-end training favored by some large organizations, highlighting a potentially more efficient path for VLM development <a class="yt-timestamp" data-t="01:48:48">[01:48:48]</a>.