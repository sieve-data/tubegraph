---
title: Apples MM1 model
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 

Apple introduced its new MM1 model on March 14, 2024, marking a significant entry into the rapidly expanding field of artificial intelligence, particularly in [[overview_of_multimodal_models | multimodal models]] <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. While Apple is traditionally known for its hardware, like iPhones and MacBooks, this paper represents a surprising move towards transparency in AI research <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The paper, over 40 pages long, provides extensive detail on experiments, ablations, learning rates, and datasets used, which is unusual for the typically secretive company <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Naming Convention: MLLM vs. VLM

Apple refers to MM1 as a "multimodal large language model" (MLLM) <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. The speaker argues that "vision language model" (VLM) would be a more accurate term, as MM1 primarily handles vision and text modalities, not multiple modalities as "multimodal" implies <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This choice of terminology may be a deliberate branding strategy by Apple to "own the category" and optimize for search engine results, similar to their rebranding of VR/AR as "spatial computing" <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

## Qualitative Capabilities

MM1 demonstrates impressive capabilities, including:
*   **Counting**: Accurately counts objects in images <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Optical Character Recognition (OCR)**: Can read diverse text in images, including handwritten, fuzzy, or very small text <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. It can also handle numbers that are shifted or very large <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Refusing to Hallucinate**: The model can correctly state when information requested by the user is not present in the image, a sign of proper tuning to avoid common LLM hallucinations <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Multi-Image Reasoning**: Supports interleaved text and images, allowing it to answer questions related to multiple images presented in a sequence <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>.

## Model Architecture and Design Decisions

The development of MM1 involved three key axes of design decisions: architecture, data choices, and training procedure <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

### Image Encoder
MM1 uses a Vision Transformer (ViT) model, specifically ViT Large 14, as its image encoder <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>. This encoder is pre-trained with a Clip loss, a type of contrastive loss, on large datasets like DFN-5B and VCap-300M, with an image size of 336x336 pixels initially, scaled up to 378x378 pixels in the final model <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a> <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>.

*   **Contrastive vs. Reconstructive Losses**:
    *   **Contrastive loss** (like Clip) helps the visual encoder learn semantic knowledge by pushing similar concepts closer and dissimilar concepts further apart in an embedding space <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>.
    *   **Reconstructive loss** (like DinoV2) explicitly captures all parts of an image, leading to more nuanced, low-level visual features <a class="yt-timestamp" data-t="00:33:48">[00:33:48]</a>.
*   **Impact of Image Resolution and Token Count**: Image resolution has the highest impact on model performance, followed by model size and training data composition <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>. Increasing image resolution from 224 to 336 pixels significantly improves performance <a class="yt-timestamp" data-t="00:42:18">[00:42:18]</a>. The number of image tokens fed to the LLM (derived from patches of the image) also affects performance, with more tokens generally yielding better results <a class="yt-timestamp" data-t="00:45:12">[00:45:12]</a>.
*   **Ensemble Opportunity**: The speaker suggests that Apple missed an opportunity to use [[recent_advancements_in_multimodal_model_architectures | ensembles]] of image encoders (e.g., combining Clip and DinoV2 features) as seen in other [[overview_of_multimodal_models | multimodal models]] like MusePoly Visual Expert, which could provide more comprehensive visual information <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>. However, Apple may have opted for a simpler, single encoder solution for efficiency, especially with an eye towards on-device inference <a class="yt-timestamp" data-t="01:42:01">[01:42:01]</a>.

### Vision-Language Connector
The vision-language connector (also called a projector or abstractor) transforms the visual features from the image encoder into a format compatible with the language model <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>. A key finding from the paper is that the architectural design of this connector has a "comparatively negligible performance" impact <a class="yt-timestamp" data-t="01:00:44">[01:00:44]</a>. This aligns with the "bitter lesson" in AI, suggesting that scale and data are more important than complex architectural choices <a class="yt-timestamp" data-t="00:49:53">[00:49:53]</a>.

### Language Model (LLM)
MM1 employs a decoder-only language model, ranging in size from 3 billion to 30 billion parameters <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a> <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This model generates text tokens autoregressively <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>. The family of models includes [[ai_model_architecture_and_parallelism_strategies | Mixture-of-Experts (MoE)]] variants, with up to 64 experts <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. While more experts theoretically lead to better performance by increasing model capacity, they also introduce computational complexity, especially during inference <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>.

## Data Strategy

### Pre-training Data
MM1 uses a careful mix of data types for large-scale [[overview_of_multimodal_models | multimodal]] pre-training <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>:
*   **Captioning Data (45%)**: Consists of images paired with relatively short, highly relevant captions (e.g., CC3M, CC12M) <a class="yt-timestamp" data-t="00:53:16">[00:53:16]</a>.
*   **Interleaved Image-Text Documents (45%)**: Documents with longer, more diverse text and images that are loosely related, similar to news articles (600 million documents) <a class="yt-timestamp" data-t="00:53:27">[00:53:27]</a>.
*   **Text-Only Data (10%)**: Approximately 2 trillion tokens of pure text data <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. This is crucial for maintaining strong text-only performance and preventing the LLM from "forgetting" how to process text <a class="yt-timestamp" data-t="00:57:02">[00:57:02]</a>.
*   **Synthetic Captions**: The use of synthetic captions (e.g., VCap-300M, 300 million pairs) provides a non-trivial performance boost, particularly for few-shot learning <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a>.

### Training Procedure
Unlike many other VLM papers that freeze pre-trained image encoders, Apple pre-trains both the LLM and the visual encoders "entirely unfrozen" <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a>. This means gradients are propagated through the entire model, including the image encoder, which requires significant computational resources <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.

### Fine-tuning
After pre-training, the model undergoes a supervised fine-tuning stage <a class="yt-timestamp" data-t="01:18:51">[01:18:51]</a>.
*   **GPT-4 Vision Data**: A significant portion of the fine-tuning data is generated by GPT-4 Vision <a class="yt-timestamp" data-t="01:19:31">[01:19:31]</a>. This means MM1 effectively undergoes [[finetuning_with_quantized_models | distillation]] from GPT-4 Vision, where it learns to emulate GPT-4V's responses to images <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>.
*   **Internal Dataset**: Apple mentions one internal, text-only supervised fine-tuning dataset, which is similar to ShareGPT but not publicly available <a class="yt-timestamp" data-t="01:22:42">[01:22:42]</a>.

## Performance and Benchmarks

Apple claims "state-of-the-art" results compared to older, more open models like Flamingo and Emu2 <a class="yt-timestamp" data-t="02:09:52">[02:09:52]</a>. However, when compared against the strongest contemporary models like GPT-4V and Gemini Ultra, MM1 achieves "competitive performance" rather than state-of-the-art, often scoring slightly lower <a class="yt-timestamp" data-t="01:31:06">[01:31:06]</a>.

The scaling laws continue to hold, meaning increasing image resolution and pre-training steps (i.e., more data and longer training) consistently lead to better performance <a class="yt-timestamp" data-t="01:34:46">[01:34:46]</a>. This reinforces the idea that computational scale is the primary driver of performance improvements <a class="yt-timestamp" data-t="01:49:19">[01:49:19]</a>.

## Technical Details and Tools

*   **Framework**: Apple uses its internal Ax Learn framework, which is built on top of Jax and XLA, for large-scale deep learning model development <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>.
*   **Experiment Tracking**: Weights & Biases is used for experiment tracking <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>.
*   **Evaluation**: Luther AI's LM Evaluation Harness is used for multimodal pre-training evaluations <a class="yt-timestamp" data-t="01:36:57">[01:36:57]</a>.
*   **Hardware (Unspecified)**: The paper notably omits any mention of the hardware used for training <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. This leads to speculation that Apple might be using Nvidia GPUs or Google's TPUs, and that this omission is deliberate to avoid highlighting reliance on other companies' hardware while Apple likely develops its own <a class="yt-timestamp" data-t="01:03:55">[01:03:55]</a>.

## Key Learnings and Transparency

The paper distills several crucial design lessons:
*   Image resolution is paramount for performance <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>.
*   The vision language connector's architecture has a negligible impact <a class="yt-timestamp" data-t="01:34:25">[01:34:25]</a>.
*   A careful mixture of captioned, interleaved, and text-only data is crucial for optimal [[overview_of_multimodal_models | multimodal]] performance and strong text capabilities <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   Synthetic caption data significantly aids few-shot learning <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.

Apple's decision to publish such a detailed and open paper is a refreshing departure from its typical secrecy <a class="yt-timestamp" data-t="01:50:41">[01:50:41]</a>. This transparency, alongside Meta's contributions, offers valuable insights and models to the open-source community, fostering further development and competition in the AI space <a class="yt-timestamp" data-t="01:51:05">[01:51:05]</a>.