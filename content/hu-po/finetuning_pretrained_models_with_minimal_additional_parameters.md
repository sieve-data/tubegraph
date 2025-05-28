---
title: Finetuning pretrained models with minimal additional parameters
videoId: YSGIENcFPSM
---

From: [[hu-po]] <br/> 

LLaMA-Adapter is a lightweight adaptation model designed to efficiently tune large language models (LLMs) like LLaMA into instruction-following models. It addresses the computational intensity and resource demands of traditional [[finetuning machine learning models | fine-tuning]] methods, which often involve overwriting vast numbers of parameters in already [[Pretraining and finetuning in AI models | pre-trained]] models <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

The paper, "LLaMA-Adapter: A Lightweight Adaptation Model to Efficiently Tune LLaMA into an Instruction-Following Model," was released on March 28, 2023, by researchers from Shanghai Artificial Intelligence Laboratory and the University of California, Los Angeles <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Key Features and Contributions

LLaMA-Adapter offers several advantages for [[finetuning machine learning models | fine-tuning]] LLMs efficiently:

*   **Parameter Efficiency** <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>:
    *   It introduces only 1.2 million learnable parameters upon the frozen LLaMA 7B model, as opposed to updating all 7 billion parameters <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   This allows the original LLaMA weights to be preserved, preventing the loss of hard-earned [[Pretraining and finetuning in AI models | pre-trained]] knowledge <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

*   **Training Efficiency** <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>:
    *   [[Training and finetuning processes for AI models | Fine-tuning]] costs less than one hour on eight A100 GPUs <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>, making it three times faster than Alpaca <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
    *   This is achieved by not needing to back-propagate gradients through the entire frozen base model <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.

*   **Flexible Adaptation** <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>:
    *   The approach allows for different "expert knowledge" to be integrated by plugging in specific adapters <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
    *   Storing only the 1.2 million parameter adapter, rather than a full 7 billion parameter model for each context, simplifies sharing and deployment <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

*   **Multimodal Extension** <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>:
    *   The method can be extended to process image inputs for multimodal reasoning by adding image tokens to the adaptation prompts <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

## How LLaMA-Adapter Works

LLaMA-Adapter introduces a novel approach to [[finetuning language models for specific tasks | fine-tuning]] that minimizes disruption to the pre-trained model while maximizing performance <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

### Learnable Adaptation Prompts

Instead of modifying the core LLaMA weights, LLaMA-Adapter prepends a set of learnable "adaptation prompts" to the input text tokens <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

*   **Placement**: These prompts are inserted into the topmost L layers of the [[Transformer scaling with tokenized model parameters | Transformer]] architecture <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. The choice of higher layers is strategic, as these layers represent more abstract and high-level concepts in the model, allowing for better tuning of language representations with higher-level semantics <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>, <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>. In practice, 30 out of 32 LLaMA layers have adapters <a class="yt-timestamp" data-t="00:53:57">[00:53:57]</a>.
*   **Concatenation**: The adaptation prompt (PL, with dimensionality K x C, where K is prompt length and C is feature dimension) is concatenated with the word tokens (TL, with dimensionality M x C) along the token dimension. This results in a combined input of (K+M) x C <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>, <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.
*   **Frozen Base Model**: The original LLaMA model parameters remain frozen during [[Training and finetuning processes for AI models | training]], meaning their weights do not change during back-propagation <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>. Only the adaptation prompts are learned <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### Zero-Initialized Attention with Gating

To prevent the new, randomly initialized adaptation prompts from disturbing the pre-trained knowledge at the beginning of [[Training and finetuning processes for AI models | training]], LLaMA-Adapter proposes a "zero-init attention mechanism with a learnable gating factor" (GL) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

*   **Initialization**: The gating factor (GL) is initialized to zero <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>. This ensures that at the start of [[Training and finetuning processes for AI models | training]], the adaptation prompts have no impact on the existing model, preserving the original LLaMA weights <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>, <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.
*   **Adaptive Control**: As [[Training and finetuning processes for AI models | training]] progresses, the gating factor adaptively controls the importance of the adaptation prompts' contributions to the attention scores <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. It progressively increases its magnitude, allowing more instructional semantics to be incorporated into LLaMA <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.
*   **Stability**: This mechanism contributes to more stable [[Training and finetuning processes for AI models | training]] and a significant performance gain (43% improvement in one ablation study) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>.
*   **Multiple Gates**: LLaMA-Adapter adopts multiple GLs, independently learned for different heads of the attention mechanism <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.

> [!NOTE]
> The zero-initialization strategy is also used in other models like ControlNet to prevent noise and instability when adding new parameters to a pre-trained network <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

### Training Details

LLaMA-Adapter was trained on the Alpaca 52k self-instruct demonstration dataset <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>, which contains 52,000 instruction-following examples derived from GPT-3.5 outputs <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. The model was trained for 5 epochs on A100 GPUs, utilizing a batch size of 64 <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.

## Multimodal Extension

LLaMA-Adapter can be extended to support multimodal inputs, specifically images, allowing it to perform tasks like visual question answering <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

*   **Visual Encoder**: It leverages a pre-trained visual encoder, such as Clip, to extract multi-scale global features from input images <a class="yt-timestamp" data-t="00:38:12">[00:38:12]</a>, <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Projection Network**: These image features are then concatenated and passed through a learnable projection network (simple MLPs) to match the dimensionality of the language tokens <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>, <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>.
*   **Image Tokens**: The resulting "image tokens" (IP) are element-wise added to the K-length adaptation prompts at all L inserted [[Transformer scaling with tokenized model parameters | Transformer]] layers <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>. This means the LLaMA model does not directly "understand" images; instead, it learns to interpret the *embeddings* generated by the visual encoder as additional context, akin to word tokens <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>.

> [!NOTE]
> The multimodal extension, while effective, requires loading the visual encoder (e.g., Clip, which can be ~600MB for a smaller model) in addition to the frozen LLaMA model (~13GB for 7B parameters) and the small adapter (~4.7MB) <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>, <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>.

## Advantages of this Approach

This [[finetuning and training curriculums in AI models | finetuning]] methodology, part of the broader field of [[finetuning machine learning models | parameter-efficient fine-tuning]] (PEFT), offers significant benefits:

*   **Computational Efficiency**: By only [[finetuning with quantized models | training]] a small number of additional parameters (1.2 million), the computational demands are drastically reduced compared to [[Training and finetuning processes for AI models | full model fine-tuning]] <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>, <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   **Prevention of Overfitting**: The small number of learnable parameters, combined with the frozen base model, makes LLaMA-Adapter robust to overfitting, even when [[finetuning machine learning models | fine-tuned]] on relatively small datasets like Alpaca 52k <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.
*   **Knowledge Preservation**: The zero-initialization gating mechanism ensures that the valuable [[Pretraining and finetuning in AI models | pre-trained]] knowledge within the base LLaMA model is preserved and not corrupted by new parameters <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.
*   **Scalability and Shareability**: This approach facilitates the sharing and deployment of instruction-following models, as only the small adapter needs to be distributed, not the entire large base model <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This is similar to how LoRA (Low-Rank Adaptation) models are shared for Stable Diffusion <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>, <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

## Comparison to Other Methods

LLaMA-Adapter stands in contrast to approaches like Stanford Alpaca, which [[finetuning machine learning models | fine-tune]] all parameters in an end-to-end manner <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. While full [[finetuning machine learning models | fine-tuning]] can be effective, it is computationally intensive and challenging to scale, especially for large [[Transformer scaling with tokenized model parameters | language models]] <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. The developer notes that full [[finetuning machine learning models | fine-tuning]] will likely become impractical for consumer hardware as models continue to grow <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

The lightweight adapter approach, with its minimal additional parameters and frozen base model, is seen as the likely [[future of finetuning and incontext learning | future of fine-tuning]] for large models <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>, <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.