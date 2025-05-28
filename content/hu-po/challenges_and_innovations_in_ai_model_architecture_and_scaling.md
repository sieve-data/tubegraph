---
title: Challenges and innovations in AI model architecture and scaling
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 

Apple's release of the MM1 model paper in March 2024, detailing their approach to building multimodal large language models (MLLMs), offers significant insights into the [[role_of_model_architecture_and_data_scale | role of model architecture and data scale]] in achieving performant AI systems <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. This paper, unusually transparent for Apple, outlines crucial design lessons and highlights ongoing challenges in AI model development <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>, particularly concerning architecture, data, and computational constraints <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

## Apple's MM1 Model: A Deep Dive into MLLM Development

MM1 (Multimodal One) is a family of multimodal models, scaling up to 30 billion parameters, that process both image and text data to produce text <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a> <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a> <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>. While Apple prefers the term "multimodal large language models," the community often refers to these as Vision Language Models (VLMs) <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. The paper is extensive, detailing ablations, experiments, learning rates, and data sets, providing a comprehensive look at their methodology <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a> <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

The MM1 models demonstrate impressive capabilities, including:
*   Counting objects in images <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.
*   Optical Character Recognition (OCR), even with small, handwritten, or shifted text <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>.
*   Multi-image reasoning and enhanced in-context learning <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>.
*   The crucial ability to "say no" or indicate when information is not present, counteracting common hallucination tendencies in LLMs <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a> <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.
*   Interleaving text and images to answer complex questions <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>.

## Core Design Decisions and Their Impact

Apple's research on MM1 identifies three major axes of design decisions for MLLMs <a class="yt-timestamp" data-t="21:27:00">[21:27:00]</a>:

1.  **Architecture**: Investigating different pre-trained image encoders and connection methods to LLMs <a class="yt-timestamp" data-t="21:35:00">[21:35:00]</a>.
2.  **Data**: Considering various data types and their relative mixture weights <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>.
3.  **Training Procedure**: Determining which parts of the model to train at each stage <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.

### Key Lessons from Ablation Studies

Apple's extensive ablations led to several crucial design lessons <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>:

> [!TIP] **Image Resolution is Paramount**
> The image resolution has the highest impact on the final performance of the model, followed by model size and training data composition <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a> <a class="yt-timestamp" data-t="42:11:00">[42:11:00]</a>. Increasing image resolution from 224x224 to 336x336 significantly improves performance <a class="yt-timestamp" data-t="42:18:00">[42:18:00]</a> <a class="yt-timestamp" data-t="58:58:00">[58:58:00]</a>. The more visual tokens (patches) used from an image, the better the performance, though this increases computational challenge, especially for multi-image input <a class="yt-timestamp" data-t="45:15:00">[45:15:00]</a> <a class="yt-timestamp" data-t="46:28:00">[46:28:00]</a>.

> [!NOTE] **Vision Language Connector Design is Less Critical**
> Surprisingly, the design of the vision language connector (or projector), which bridges visual features to the LLM, has a "comparatively negligible performance" impact <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a> <a class="yt-timestamp" data-t="29:28:00">[29:28:00]</a> <a class="yt-timestamp" data-t="49:40:00">[49:40:00]</a>. This finding supports the "bitter lesson" in AI, suggesting that complex architectural innovations in this component might be less impactful than raw scale and data <a class="yt-timestamp" data-t="49:53:00">[49:53:00]</a>. Simple linear projectors work almost as well as more complex convolutional or deformable attention-based abstractors <a class="yt-timestamp" data-t="51:25:00">[51:25:26]</a>.

> [!TIP] **Careful Data Mixture for Optimal Performance**
> For large-scale multimodal pre-training, a careful mix of data types is crucial <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a> <a class="yt-timestamp" data-t="52:47:00">[52:47:00]</a>. Apple uses:
> *   45% captioned images (short text, high relevance to image) <a class="yt-timestamp" data-t="26:18:00">[26:18:00]</a> <a class="yt-timestamp" data-t="53:44:00">[53:44:00]</a>.
> *   45% interleaved image-text documents (longer, more diverse text, less relevance to surrounding image, like news articles) <a class="yt-timestamp" data-t="26:20:00">[26:20:00]</a> <a class="yt-timestamp" data-t="53:50:00">[53:50:00]</a>.
> *   10% text-only data <a class="yt-timestamp" data-t="26:23:00">[26:23:00]</a>.
>
> Interleaved data is instrumental for few-shot and text-on performance, while captioning data is crucial for zero-shot performance <a class="yt-timestamp" data-t="54:27:00">[54:27:00]</a>. The inclusion of text-only data prevents the language model from "forgetting" how to read text and ensures attention on text tokens <a class="yt-timestamp" data-t="56:56:00">[56:56:00]</a>.

> [!NOTE] **Synthetic Data Provides a Non-Trivial Boost**
> Synthetic captions, like those from the VCap 300M dataset, significantly improve performance, particularly for few-shot learning <a class="yt-timestamp" data-t="42:29:00">[42:29:00]</a> <a class="yt-timestamp" data-t="58:16:00">[58:16:00]</a>. Even a relatively small proportion (7%) of synthetic data can yield a 2-4% boost, which is greater than the impact of increasing the image encoder capacity <a class="yt-timestamp" data-t="58:34:00">[58:34:00]</a> <a class="yt-timestamp" data-t="59:06:00">[59:06:00]</a>.

## Innovations in Training Procedures

Apple employs a two-stage training pipeline: pre-training followed by supervised fine-tuning (SFT) <a class="yt-timestamp" data-t="21:58:00">[21:58:00]</a>.

> [!INFO] **Unfrozen Encoders During Training**
> Unlike many other VLM papers that freeze pre-trained image encoders, Apple trains both the LLM and the visual encoders entirely unfrozen during both pre-training and supervised fine-tuning <a class="yt-timestamp" data-t="47:03:00">[47:03:00]</a> <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a> <a class="yt-timestamp" data-t="1:01:06">[01:01:06]</a> <a class="yt-timestamp" data-t="1:35:56">[01:35:56]</a>. This allows gradients to propagate all the way down into the image encoder weights, potentially leading to better overall performance. This approach, however, requires substantial computational resources <a class="yt-timestamp" data-t="47:27:00">[47:27:00]</a>.

> [!INFO] **Mixture of Experts (MoE) for Scalability**
> MM1 includes Mixture of Expert (MoE) variants up to 30 billion parameters, with 64 experts in some configurations <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a> <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>. MoE models scale the total number of model parameters while keeping the activated parameters (those used during inference) constant, typically by using only a subset (e.g., top two) of experts for any given token <a class="yt-timestamp" data-t="1:10:42">[01:10:42]</a> <a class="yt-timestamp" data-t="1:12:50">[01:12:50]</a>. While MoE helps increase model capacity without proportional inference cost, it introduces challenges related to memory management and ensuring balanced expert utilization during training <a class="yt-timestamp" data-t="1:13:00">[01:13:00]</a> <a class="yt-timestamp" data-t="1:14:00">[01:14:00]</a>. Apple’s models with MoE uniformly outperform their dense counterparts, indicating its potential for further scaling <a class="yt-timestamp" data-t="1:32:04">[01:32:04]</a>.

## Computational and Data Challenges

### Hardware Secrecy and [[Computational Challenges in Training Large Models | Computational Constraints]]

A notable omission from the MM1 paper is any mention of the hardware used for training <a class="yt-timestamp" data-t="27:30:00">[27:30:00]</a>. This secrecy, likely due to Apple's desire to eventually use their own chips for AI training, implies they currently rely on external hardware like Nvidia GPUs or Google's TPUs <a class="yt-timestamp" data-t="28:17:00">[28:17:17]</a> <a class="yt-timestamp" data-t="1:03:05">[01:03:05]</a>. Training large MLLMs demands substantial resources, and even Apple uses a smaller base configuration (e.g., 3 billion parameters) for most ablation studies to manage costs, extrapolating findings to larger models (e.g., 30 billion parameters) <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a> <a class="yt-timestamp" data-t="23:19:00">[23:19:00]</a>. The assumption that hyperparameter sweeps on small models directly apply to large models remains an open question in the community <a class="yt-timestamp" data-t="23:32:00">[23:32:00]</a> <a class="yt-timestamp" data-t="1:09:24">[01:09:24]</a>.

> [!WARNING] **The "Bitterness" of Scale**
> The paper reinforces the "Rich Sutton bitter lesson" that architectural design choices for components like the vision language connector have negligible impact compared to the scale of the data and model capacity <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a> <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a> <a class="yt-timestamp" data-t="1:34:25">[01:34:25]</a>. This implies an ongoing "arms race" driven by computational resources rather than novel algorithmic ideas <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a> <a class="yt-timestamp" data-t="50:18:00">[50:18:00]</a>.

### Data Provenance and Openness

While the MM1 paper is largely open, it acknowledges an internal, non-publicly available text-only supervised fine-tuning dataset, similar to ShareGPT <a class="yt-timestamp" data-t="1:22:50">[01:22:50]</a>. Furthermore, a significant innovation is the use of GPT-4 Vision-generated data sets for supervised fine-tuning, effectively "distilling" the capabilities of GPT-4 Vision into MM1 <a class="yt-timestamp" data-t="1:19:08">[01:19:08]</a> <a class="yt-timestamp" data-t="1:20:46">[01:20:46]</a>. This practice, common across many VLM models, raises complex questions about data ownership, copyright, and the tangled chain of AI model dependencies <a class="yt-timestamp" data-t="1:21:12">[01:21:12]</a> <a class="yt-timestamp" data-t="1:21:37">[01:21:37]</a>.

## Performance and Future Outlook

MM1 achieves state-of-the-art results compared to other *published pre-training results* from models like Flamingo and EMU2 <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a> <a class="yt-timestamp" data-t="1:17:16">[01:17:16]</a>. However, when compared to top closed models like GPT-4 Vision and Gemini Ultra, MM1's performance is competitive but not superior <a class="yt-timestamp" data-t="1:30:52">[01:30:52]</a> <a class="yt-timestamp" data-t="1:31:40">[01:31:40]</a>.

The scaling laws continue to hold, indicating that increased data, longer pre-training, and higher image resolution lead to better performance <a class="yt-timestamp" data-t="1:33:30">[01:33:30]</a> <a class="yt-timestamp" data-t="1:49:17">[01:49:17]</a>. This suggests that future advancements in AI model architecture and scaling will primarily depend on continued investments in [[ai_algorithms_and_computational_constraints | computational constraints]] and data acquisition <a class="yt-timestamp" data-t="1:49:43">[01:49:43]</a>.

Apple's foray into transparent AI research with MM1 is a positive development for the open-source community <a class="yt-timestamp" data-t="1:50:50">[01:50:50]</a>. By sharing detailed methodologies and lessons learned, they contribute to the collective understanding of effective [[model_architecture_and_data_quality_in_ai | model architecture and data quality in AI]], potentially accelerating the development of more powerful and accessible open-source models <a class="yt-timestamp" data-t="1:51:11">[01:51:11]</a>.