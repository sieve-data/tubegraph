---
title: Training and finetuning processes for AI models
videoId: BJ98vicRYHg
---

From: [[hu-po]] <br/> 

The development of state-of-the-art AI models like LLaVA (Large Language and Visual Assistant) showcases innovative [[technical_aspects_of_ai_model_training_and_finetuning | training and finetuning processes]] that prioritize efficiency and accessibility <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. These methodologies highlight a shift in AI research from creating complex model architectures to focusing on strategic data utilization and modular design <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>.

## LLaVA: A Case Study in Efficient Training

LLaVA is an open-source vision-language model, generally considered the best available in its category <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. It achieves state-of-the-art performance on 11 different benchmarks using only publicly available data and approximately one day of training on a single A100 node (eight A100 GPUs) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. While this training time is impressive, it's crucial to note that LLaVA leverages heavily [[pretraining_and_finetuning_in_ai_models | pre-trained models]] <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Architectural Components

LLaVA's architecture is surprisingly simple, connecting a vision encoder and a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>:

*   **Vision Encoder**: An OpenAI CLIP ViT-L/14 (Vision Transformer Large, patch size 14) with an increased image resolution of 336x336 pixels <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>. CLIP models are [[pretraining_and_finetuning_in_ai_models | pre-trained]] on vast image-text pairs using a contrastive loss to learn semantic relationships between images and text <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   **Large Language Model (LLM)**: Vicuna 13B, which is a variant of Llama 1 <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Vicuna itself is [[finetuning_machine_learning_models | finetuned]] on GPT-4 responses, which means much of its "intelligence" is derived from GPT-4's extensive [[pretraining_and_finetuning_in_ai_models | pre-training]] <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   **Vision Language Connector**: A simple Multi-Layer Perceptron (MLP) acts as the bridge, converting visual features into a format consumable by the language model <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. This component is the *only* part trained from scratch in LLaVA's initial stage <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>.

## Two-Stage Instruction Tuning Procedure

LLaVA employs a two-stage [[finetuning_and_training_curriculums_in_ai_models | instruction tuning]] process <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>:

1.  **Stage One: Pre-training for Feature Alignment** <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>
    *   **Objective**: Align the image features from the vision encoder with the LLM's word embedding space <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>. This stage is analogous to training a compatible visual tokenizer for the frozen LLM <a class="yt-timestamp" data-t="00:48:38">[00:48:38]</a>.
    *   **Data**: A filtered subset of CC3M (595k image-text pairs) <a class="yt-timestamp" data-t="00:45:27">[00:45:27]</a>. These pairs are treated as single-turn conversations where the model describes an image based on its caption <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.
    *   **Trainable Parameters**: Only the MLP projection matrix (W) is trained in this stage, while both the vision encoder and the LLM are kept frozen <a class="yt-timestamp" data-t="00:46:57">[00:46:57]</a>. This significantly reduces memory and compute requirements, making it feasible to train on consumer GPUs <a class="yt-timestamp" data-t="00:47:17">[00:47:17]</a>.

2.  **Stage Two: End-to-End Visual Instruction Tuning** <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>
    *   **Objective**: Train the model to follow human intent in visual tasks by generating multi-turn conversation data <a class="yt-timestamp" data-t="00:51:27">[00:51:27]</a>. The model is trained to predict the assistant's answer autoregressively <a class="yt-timestamp" data-t="00:38:46">[00:38:46]</a>.
    *   **Data**: 158k unique language-image instruction-following data sets, with conversation-style data used for [[finetuning_and_training_curriculums_in_ai_models | multi-turn conversations]] <a class="yt-timestamp" data-t="00:51:27">[00:51:27]</a>. This includes synthetically generated data from GPT-4 (text-only) <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a> and existing Visual Question Answering (VQA) datasets like ScienceQA <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>, GQA <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>, OKVQA, OCRVQA, and TextCaps <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
    *   **Trainable Parameters**: In this stage, both the projection layer (W) and certain parameters within the Vicuna LLM (through a LoRA adaptation) are updated, while the visual encoder remains frozen <a class="yt-timestamp" data-t="00:49:32">[00:49:32]</a>, <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.

## The Role of Data Quality and Training Recipe

A key takeaway from LLaVA's success is the paramount importance of the data mix and the "training recipe" <a class="yt-timestamp" data-t="01:06:42">[01:06:42]</a>. The paper's transparency in providing the exact data mixture and training scripts is highly valued in the open-source community <a class="yt-timestamp" data-t="01:03:47">[01:03:47]</a>, <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>.

*   **Synthetic Data Generation**: GPT-4 (text-only) was used to generate multimodal instruction-following data, enabling the model to learn conversational patterns even without direct visual input during data generation <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>, <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Prompt Engineering in Data**: Subtle differences in prompt formatting within the instruction tuning data (e.g., "answer the question using a single word or phrase") significantly impact the model's output and generalization <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>, <a class="yt-timestamp" data-t="01:38:09">[01:38:09]</a>.
*   **Scaling and Performance**: Adding more fine-tuning data and increasing the LLM size (e.g., from 7B to 13B parameters) are shown to provide the most significant performance boosts, more so than complex architectural changes <a class="yt-timestamp" data-t="01:05:34">[01:05:34]</a>, <a class="yt-timestamp" data-t="01:31:56">[01:31:56]</a>.

## [[challenges_and_methodologies_in_ai_training | Challenges and Methodologies in AI Training]]

*   **Pre-trained Model Dependency**: While LLaVA's training is efficient, it heavily relies on the immense computational resources and data used to [[pretraining_and_finetuning_in_ai_models | pre-train]] foundational models like CLIP and Llama <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Prompt Engineering Importance**: The sensitivity of language models to system messages and the order of input information (e.g., image first or question first) highlights that [[finetuning_language_models_for_specific_tasks | prompt engineering]] is a critical, almost "alchemical," aspect of model performance <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>.
*   **Generalization vs. Specialization**: Fine-tuning models for narrow tasks (e.g., short vs. long context length) can lead to a loss of their broader general capabilities, suggesting a need for more generalized approaches to model development <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>.
*   **Hallucination**: Despite improvements, LLaVA can still occasionally "hallucinate" or disseminate misinformation, a common challenge in large AI models <a class="yt-timestamp" data-t="01:40:56">[01:40:56]</a>.

LLaVA's success demonstrates that by wisely combining powerful [[finetuning_pretrained_models_with_minimal_additional_parameters | pre-trained models with minimal additional parameters]] and strategically curating instruction tuning data, it's possible to achieve state-of-the-art performance with significantly less computational expense than training from scratch <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. This approach makes advanced AI research more accessible and reproducible <a class="yt-timestamp" data-t="01:33:02">[01:33:02]</a>.