---
title: Pretraining scaling laws for vision encoders
videoId: 5qkjxDzEaaw
---

From: [[hu-po]] <br/> 

**Vision encoders** are the initial neural network modules designed to process and interpret images, effectively serving as the visual cortex for [[challenges_and_strategies_for_training_largescale_vision_language_models | vision-language models]] (VLMs) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. They transform image content into vector representations <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## Training Paradigm Shift
Traditionally, many [[Pretrained Vision Transformers and KOCO | vision encoders]] like CLIP and SigLIP were trained using [[comparison_of_contrastive_vs_classification_pretraining_for_vision_encoders | contrastive losses]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This method involves pulling similar data points closer and pushing dissimilar ones further apart in an embedding space <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>, <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

A recent paper by Apple introduces a new approach: training large [[Pretrained Vision Transformers and KOCO | vision encoders]] with a simple **auto-regressive objective** <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This method is akin to how [[scaling_of_language_models_and_vision_transformers | language models]] (LLMs) are pre-trained using "next token prediction" <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

In this auto-regressive setup, vision encoders are paired with a multimodal decoder that generates raw image patches and text tokens <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The encoder processes an image into a vector, which the decoder then reconstructs into an image using patches <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>, <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>, <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The model aims to reconstruct shifted inputs, similar to predicting the next token <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>, <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

> [!NOTE] Simplicity is Key
> The simplicity of the auto-regressive pre-training objective allows for training on even larger datasets and for longer durations <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, potentially overcoming some [[challenges_in_training_large_computer_vision_models | challenges in training large computer vision models]] <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

## Confirmation of Scaling Laws
A significant finding is that the **scaling properties** observed in [[scaling_of_language_models_and_vision_transformers | large language models]] trained with auto-regressive objectives also apply to [[Pretrained Vision Transformers and KOCO | vision encoders]] <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>, <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>, <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

These scaling laws state:
*   Given a fixed [[pretraining_and_finetuning_in_ai_models | pre-training]] dataset size, increasing the number of parameters consistently leads to an improvement in validation loss <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   The optimal model size varies depending on the pre-training compute budget <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   Larger models may perform worse if severely undertrained but improve consistently as the compute budget increases <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>, <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

For vision encoders, lower validation cross-entropy (a measure of model performance, similar to perplexity in LLMs) indicates greater "intelligence" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This loss decreases as more samples are fed to the model and with more parameters <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, though diminishing returns are observed at a certain point <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Implications for Future Vision Models
The confirmation of these scaling laws suggests that [[Pretrained Vision Transformers and KOCO | vision encoders]] will continue to improve significantly in performance and capabilities as more resources are invested in their [[pretraining_and_finetuning_in_ai_models | pre-training]] <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>, <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>, <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This continuous improvement in the foundational visual component has broad implications for the advancement of all [[challenges_and_strategies_for_training_largescale_vision_language_models | vision-language models]] and their applications <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>, <a class="yt-timestamp" data-t="00:57:55">[00:57:55]</a>.