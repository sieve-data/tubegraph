---
title: Challenges and methodologies in AI training
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 

The development of advanced Artificial Intelligence models, particularly Multimodal Large Language Models (MLLMs), involves navigating numerous [[Challenges and strategies in model training and performance | challenges and strategic methodologies]]. Apple's MM1 model, released in March 2024, provides extensive insights into the [[Technical aspects of AI model training and finetuning | technical aspects]] and [[Training and finetuning processes for AI models | processes]] involved in building performant multimodal AI models. <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>

## MM1 Model Overview

Apple's MM1 is a family of multimodal models, scaling up to 30 billion parameters, and includes both dense models and Mixture of Experts (MoE) variants. <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a> Unlike Apple's typical secretive nature, the MM1 paper is notably comprehensive, detailing experiments, ablations, learning rates, and data sets. <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>

## Core Design Decisions in AI Training

According to the MM1 paper, three major axes of design decisions influence the performance of MLLMs:

1.  **Architecture:** Investigating different pre-trained image encoders and various methods of connecting them to Large Language Models (LLMs). <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>
2.  **Data Choices:** Considering different types of data and their relative mixture weights, particularly for pre-training and fine-tuning. <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>
3.  **Training Procedure:** Determining which parts of the model to train at what stage, including whether to train components from scratch or keep them frozen. <a class="yt:timestamp" data-t="00:22:03">[00:22:03]</a>

## Key Lessons and Insights

Through extensive ablation studies, Apple identified several crucial design lessons:

*   **Image Resolution:** This has the highest impact on model performance. Increasing image resolution from 224x224 to 336x336 pixels significantly boosts performance. <a class="yt-timestamp" data-t="00:42:10">[00:42:10]</a> <a class="yt-timestamp" data-t="00:58:58">[00:58:58]</a> Similarly, using more image tokens (e.g., 144 tokens over 64 tokens) from the vision encoder also leads to better performance, though with increased computational cost. <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>
*   **Vision Encoder Loss and Capacity:** A larger visual encoder (e.g., Vision Transformer Large) is important for performance. Apple opted to pre-train their own Vision Transformer (ViT) with a CLIP objective on large datasets, allowing them to train the image encoder from scratch and keep it unfrozen during MLLM pre-training and fine-tuning, unlike many other models. <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a> <a class="yt-timestamp" data-t="01:15:56">[01:15:56]</a>
*   **Vision-Language Connector (Projector) Design:** Surprisingly, the specific architecture and design choice of the connector (sometimes called a projector) that bridges visual features to the LLM has a "comparatively negligible performance impact." <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a> This aligns with the "bitter lesson" in AI, suggesting that architectural complexity often matters less than data scale and fundamental scaling. <a class="yt-timestamp" data-t="00:49:53">[00:49:53]</a>
*   **Data Mix:** A careful mixture of data types is crucial. <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>
    *   **Image-Caption Data:** (e.g., CC3M, CC12M) are essential for zero-shot performance, providing concise, highly relevant text to images. <a class="yt-timestamp" data-t="00:54:12">[00:54:12]</a>
    *   **Interleaved Image-Text Documents:** (e.g., web documents) contain longer, more diverse text with looser relevance, instrumental for few-shot and text-only performance. <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>
    *   **Text-Only Data:** Including a small percentage (e.g., 10%) of text-only data during pre-training and fine-tuning helps retain strong text-based performance and prevents the LLM from ignoring text. <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>
*   **Synthetic Caption Data:** Datasets like VCap 300M, which augment short captions into detailed paragraphs, provide a "non-trivial boost" to few-shot learning, even in relatively small proportions (7% of total caption data). <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a> <a class="yt-timestamp" data-t="00:58:38">[00:58:38]</a>
*   **Validation Loss:** The validation loss during training was not strongly correlated with downstream task performance, suggesting its limitations as a sole metric for model selection. <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>

### Training Processes and Considerations

*   **Two-Stage Training:** MM1 utilizes a standard two-stage [[Finetuning and Training Curriculums in AI Models | curriculum]]: a pre-training stage on large, diverse datasets, followed by a supervised fine-tuning (SFT) stage on smaller, task-specific datasets. <a class="yt-timestamp" data-t="01:18:51">[01:18:51]</a>
*   **Unfrozen Training:** A notable aspect of MM1's training is that both the image encoder and the LLM are pre-trained and fine-tuned "entirely unfrozen." This means gradients are pushed all the way down into the image encoder weights, allowing for greater adaptation, a practice often avoided by other models due to computational cost. <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a> <a class="yt-timestamp" data-t="01:35:58">[01:35:58]</a>
*   **Mixture of Experts (MoE):** MM1 includes MoE variants with up to 64 experts. While MoE models scale the total number of parameters, they keep the activated parameters constant during inference by only using a subset of experts (e.g., top two). This inflates model capacity efficiently but adds complexity in managing memory and requires load balancing techniques to prevent expert atrophy. <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>
*   **Hyperparameter Sweeps:** Large-scale training often involves hyperparameter sweeps. Apple conducts these extensive grid searches at smaller model scales (e.g., 3 billion parameters) and then assumes these optimal settings will apply to larger models (e.g., 30 billion parameters) due to computational constraints. <a class="yt-timestamp" data-t="02:29:50">[02:29:50]</a>
*   **Image Handling:** For high-resolution input, MM1 downsamples images and may divide resized images into four sub-images to manage computational load and context length. The model primarily supports square image resolutions. <a class="yt-timestamp" data-t="01:29:48">[01:29:48]</a> <a class="yt-timestamp" data-t="01:42:30">[01:42:30]</a>

## Software and Hardware Stack

Apple's choice of underlying frameworks reveals a [[Decentralized Training and AI Development | complex ecosystem]]:

*   **Framework:** MM1 models are trained using `ax-learn`, a library built on top of Jax and XLA, indicating Apple's alignment with Google's deep learning stack. <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>
*   **Experiment Tracking:** They utilize Weights & Biases for experiment tracking. <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>
*   **Evaluation:** For evaluation, they employ an internal fork of Luther AI's LM evaluation harness. <a class="yt-timestamp" data-t="01:36:57">[01:36:57]</a>
*   **Hardware:** A notable omission from the paper is any mention of the specific hardware used for training. This raises speculation that Apple might be using Nvidia GPUs or even Google's TPUs, rather than their own in-house silicon, to train these massive models. <a class="yt-timestamp" data-t="02:28:02">[02:28:02]</a> This secrecy might stem from a desire to only highlight their own hardware once it's capable of supporting such large-scale distributed training. <a class="yt-timestamp" data-t="02:28:48">[02:28:48]</a>

## Data Sourcing and Ethical Implications

The MM1 model's [[Training and finetuning processes for AI models | fine-tuning processes]] highlight complex data ownership and ethical dilemmas:

*   **GPT-4V Distillation:** A significant portion of the fine-tuning data for MM1 (and many other MLLMs) is synthetic data generated by GPT-4V. <a class="yt-timestamp" data-t="01:20:06">[01:20:06]</a> This effectively means MM1 is "distilling" knowledge from GPT-4V, a closed-source model whose own training data sources are not fully disclosed. <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>
*   **"Gordian Knot" of Data Ownership:** This practice creates a tangled "Gordian knot" of data dependencies and copyright, making it incredibly difficult to trace the original sources or establish clear ownership. <a class="yt-timestamp" data-t="01:21:45">[01:21:45]</a>
*   **Copyright and Training Data:** The growing trend of models training on data generated by other models, which in turn were trained on proprietary or web-scraped data, brings into question future intellectual property and regulatory challenges, contrasting with approaches like Japan's, which states AI training data and AI-generated content are immune from copyright lawsuits. <a class="yt-timestamp" data-t="01:23:55">[01:23:55]</a>

## Performance and Future Outlook

MM1 achieves competitive performance on established multimodal benchmarks but is not yet state-of-the-art compared to leading closed models like GPT-4V or Gemini Ultra. <a class="yt-timestamp" data-t="01:31:17">[01:31:17]</a> However, the paper demonstrates that model performance consistently improves with more pre-training data and increased scale (image resolution, training steps), suggesting that continued scaling will lead to stronger models in the future. <a class="yt-timestamp" data-t="01:33:50">[01:33:50]</a> Apple's unusual transparency in this paper is a positive development for the open-source community, providing valuable insights and best practices for future AI development. <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>