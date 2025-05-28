---
title: Inference cost and efficiency in AI
videoId: MVWYTFs9M-s
---

From: [[hu-po]] <br/> 

## Understanding AI Model Inference Costs

The cost and efficiency of running artificial intelligence (AI) models, particularly large language models (LLMs), are significant considerations in their deployment and scalability <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### GPT-4's Ensemble Approach

Recent reports suggest that GPT-4 is not a single model but an ensemble of eight models, each with approximately 220 billion parameters <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This strategy of using multiple models to enhance performance is known as model ensembling or a mixture model, a common practice in Kaggle competitions to achieve marginal performance gains <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

> [!NOTE] Model Ensembling
> In model ensembling, multiple versions of a model are trained on slightly different data subsets, increasing output variety for the same input. Selecting the best output from these diverse models generally yields better results than using a single "best" model <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

This architectural choice significantly impacts [[large_language_models_and_inference_efficiency | inference efficiency]] and cost. While Google's Bard performs inference on a single model, GPT-4 reportedly conducts 16 inferences for a single query <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This means OpenAI's inference cost for GPT-4 could be 16 times higher than Bard's <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>, aligning with public statements about the expense of GPT-4 inference <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

Historical evidence from OpenAI's own work, such as the 2021 Codex paper, shows a precedent for generating multiple samples (e.g., 100 solutions per token) and filtering them down to find the best output <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This indicates a consistent strategy of leveraging multiple model outputs for improved performance.

## Efficient Inference in Self-Supervised Learning

The paper "Self-Supervised Learning from Images with a Joint Embedding Predictive Architecture" (IJEPA) explores methods for [[efficient_memory_management_in_ai_systems | efficient memory management in AI systems]] and inference in computer vision <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### IJEPA's Approach

IJEPA introduces a non-generative, self-supervised learning approach that predicts missing image information in an abstract representation space (also known as latent or embedding space) <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. This contrasts with traditional generative methods that predict in pixel or token space <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

> [!TIP] Key Efficiency Principle
> Performing predictions and calculating losses in a low-dimensional representation space rather than the high-dimensional image space significantly reduces computational cost and memory requirements <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. This approach is also used in diffusion models to optimize performance <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>.

IJEPA uses a Vision Transformer (ViT) architecture for its context encoder, target encoder, and predictor <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. While ViTs break images into patches, the memory footprint and compute scale with the number of patches, as this effectively determines the sequence size for the Transformer <a class="yt-timestamp" data-t="01:11:38">[01:11:38]</a>.

### Computational Savings

The IJEPA method demonstrates substantial computational efficiency. Training a ViT-Huge on ImageNet using 16 A100 GPUs takes less than 72 hours <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>. The technique requires fewer pre-training epochs compared to pixel reconstruction methods <a class="yt-timestamp" data-t="01:38:17">[01:38:17]</a>, leading to significant compute savings in practice <a class="yt-timestamp" data-t="01:38:19">[01:38:19]</a>.

For instance, IJEPA requires less than 1,200 GPU hours for pre-training a ViT on ImageNet, which is over two times faster than a ViT-Small pre-trained with iBOT and over 10 times more efficient than a ViT-Huge pre-trained with MAE <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>. This efficiency is partly due to avoiding the overhead of handcrafted data augmentations, which are typically performed on the fly during training <a class="yt-timestamp" data-t="01:28:09">[01:28:09]</a>.

### Model Complexity and Performance

While IJEPA might introduce additional inference steps by running multiple encoders and a predictor, these components operate in a lower-dimensional representation space. This makes them less computationally intensive compared to a single decoder that reconstructs in image space <a class="yt-timestamp" data-t="01:39:12">[01:39:12]</a>. The L2 loss function used in IJEPA is also simpler and more efficient to compute than complex reconstruction losses often used in pixel space <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

The balance between model size and dataset size also impacts performance and efficiency. While generally, larger models and larger datasets lead to better performance, there can be trade-offs due to overfitting with large models on small datasets <a class="yt-timestamp" data-t="01:42:09">[01:42:09]</a>. The IJEPA paper highlights that performance improvements are notably tied to dataset size scaling rather than just model size <a class="yt-timestamp" data-t="01:41:20">[01:41:20]</a>.

The choice of masking strategy and block sizes for context and target images also significantly impacts performance. IJEPA's "multi-block masking" strategy, for example, proves crucial for learning semantic representations and shows substantial performance differences compared to other masking approaches <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. However, model performance can be highly sensitive to these hyperparameter choices <a class="yt-timestamp" data-t="02:02:01">[02:02:01]</a>.

Overall, IJEPA demonstrates that achieving high-quality semantic image representations without heavy reliance on data augmentation and by predicting in representation space can lead to a simpler, faster, and more [[parallelizable_training_and_efficient_inference | computationally efficient training process]] <a class="yt-timestamp" data-t="02:13:24">[02:13:24]</a>.