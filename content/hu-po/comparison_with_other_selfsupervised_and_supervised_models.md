---
title: Comparison with other selfsupervised and supervised models
videoId: KSZiJ4k28b4
---

From: [[hu-po]] <br/> 

Dino V2 is an unsupervised method for training foundational computer vision models, aiming to produce all-purpose visual features from images alone <a class="yt-timestamp" data-t="01:32:01">[01:32:01]</a>. Its development involved revisiting existing approaches, combining different techniques, and scaling pre-training in terms of data and model size <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Approach and Feature Learning

Dino V2's features are learned using a [[selfsupervised_learning | discriminative self-supervised method]] that combines aspects of Dino and iBot losses with the centering of Swav <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. The training uses an image-level objective with cross-entropy loss between a student and teacher network, derived from different crops of the same image <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>. Additionally, a cross-entropy loss is applied between patch features on both networks for masked patches, combined with the image-level loss <a class="yt-timestamp" data-t="00:34:14">[00:34:14]</a>.

## Comparison to Text-Guided Models

The creators of Dino V2 argue that text-guided pre-training, such as that used in CLIP, limits the information retained about an image <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>. This is because captions only approximate the rich information in images, and complex pixel-level information may not surface with this supervision <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>. Dino V2, being an image-only model, aims to capture information at both the image and pixel level from images alone <a class="yt-timestamp" data-t="01:15:16">[01:15:16]</a>.

On specific [[evaluation_metrics_for_language_models | evaluation metrics]], Dino V2 shows compelling performance against CLIP:
*   In image classification benchmarks, Dino V2 (ViT-G) achieves around 83% accuracy, competitive with Eva CLIP (ViT-G) at 83% but surpassing CLIP (ViT-L) at 79% <a class="yt-timestamp" data-t="01:15:14">[01:15:14]</a>.
*   For monocular depth estimation, Dino V2's results are significantly cleaner and smoother qualitatively than CLIP's <a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>.
*   On domain generalization benchmarks where features are frozen, Dino V2's features are "much more general" <a class="yt-timestamp" data-t="01:25:28">[01:25:28]</a>. For example, on ImageNet-R, Dino V2 scores 75%, while Open CLIP scores 40% <a class="yt-timestamp" data-t="01:25:12">[01:25:12]</a>.
*   For video action recognition, specifically on the SSv2 dataset, Dino V2 sets a new state-of-the-art for self-supervised approaches, significantly outperforming Open CLIP <a class="yt-timestamp" data-t="01:27:11">[01:27:11]</a>.

## Comparison to Other Self-Supervised Models

The paper investigates whether [[selfsupervised_learning | self-supervised learning]] can learn all-purpose visual features when pre-trained on large, curated datasets <a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>. Dino V2 demonstrates improvements over existing self-supervised methods:
*   Dino V2's code runs approximately two times faster and uses one-third of the memory compared to the iBot implementation <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>.
*   In ablation studies adding technical components, each addition generally improves performance on K-NN or linear probing over the baseline iBot model <a class="yt-timestamp" data-t="01:04:39">[01:04:39]</a>.
*   Comparing Dino V2 to Dino V1, the speaker notes that Dino V2 is "not necessarily that much better than Dino V1 really it's just bigger" <a class="yt-timestamp" data-t="01:16:13">[01:16:13]</a>. However, Dino V2 clearly sets a new state-of-the-art among self-supervised approaches for video action recognition <a class="yt-timestamp" data-t="01:27:11">[01:27:11]</a>.

## Comparison to Supervised Models

Dino V2 aims to produce visual features that can close the performance gap with weakly supervised alternatives, without the need for fine-tuning <a class="yt-timestamp" data-t="01:53:10">[01:53:10]</a>.
*   The models are designed to generate visual features that work "out of the box" on any task without fine-tuning, achieving performance on downstream tasks that are significantly better than task-specific models <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   While Dino V2's features are competitive with the best openly available weakly supervised models <a class="yt-timestamp" data-t="02:21:47">[02:21:47]</a>, the paper shows that fine-tuning the backbone can still improve top-1 accuracy on the validation set by more than 2% <a class="yt-timestamp" data-t="01:17:54">[01:17:54]</a>. However, the speaker speculates that in the future, these foundational models might be so good that fine-tuning could degrade performance <a class="yt-timestamp" data-t="01:18:13">[01:18:13]</a>.
*   The study uses linear classifiers on top of frozen features for [[evaluation_metrics_for_language_models | evaluation metrics]] <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>, showing that the underlying information is readily available <a class="yt-timestamp" data-t="01:55:38">[01:55:38]</a>.

## Data Curation and Scale

A key aspect of Dino V2's development is the use of a dedicated, diverse, and curated image dataset, contrasting with typical uncurated data used in [[selfsupervised_learning | self-supervised learning]] literature <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. The `LVD-142M` dataset, comprising 142 million images, was built using an automatic pipeline to filter and rebalance data sets, utilizing data similarities instead of external metadata or text <a class="yt-timestamp" data-t="01:52:27">[01:52:27]</a>.

The paper found that:
*   Training on a curated set of images performs better on most benchmarks than training on uncurated data of the same size (142 million images) <a class="yt-timestamp" data-t="01:57:54">[01:57:54]</a>.
*   Larger models effectively utilize larger datasets; a big model trained on a small dataset will overfit <a class="yt-timestamp" data-t="02:01:58">[02:01:58]</a>.
*   Despite being ten times smaller (14 million images), ImageNet-22K achieved "very similar" or even slightly better performance on ImageNet-1K compared to the 142 million image `LVD-142M` dataset for smaller Vision Transformer (ViT-L) models <a class="yt-timestamp" data-t="02:01:10">[02:01:10]</a>. The speaker notes this is "crazy" as more data doesn't necessarily yield a huge boost when the dataset itself is less specific <a class="yt-timestamp" data-t="02:01:34">[02:01:34]</a>.

## Model Distillation

A significant technique used in Dino V2 is distillation, where a 1.1 billion parameter ViT model is trained and then used to distill a series of smaller models <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This approach is highlighted as being very good for saving training and compute budget <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   The paper shows that a distilled ViT-L model outperforms the same model trained from scratch <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>.
*   Even more counter-intuitively, the distilled smaller model "sometimes even outperforms the distillation Target" (the larger teacher model) on specific benchmarks like Oxford H and Paris H <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>. This suggests distillation can enhance performance beyond simply mimicking the teacher.

## Generalization and Emergent Properties

Dino V2 models demonstrate strong generalization capabilities, especially when their features are used in a frozen state:
*   The models show "stronger generalization" on alternative test sets compared to other methods <a class="yt-timestamp" data-t="01:14:41">[01:14:41]</a>.
*   Qualitative results on out-of-distribution examples, such as drawings or oil paintings, illustrate that Dino V2 can still perform monocular depth estimation and semantic segmentation relatively well, supporting the claim that its features transfer between domains <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   The model exhibits emergent properties, such as learning to separate foreground from background and even identifying semantic parts of objects (e.g., matching the head of an elephant to the head of a horse, or the wing of a plane to the wing of a bird), despite not being explicitly trained for such tasks <a class="yt-timestamp" data-t="01:45:52">[01:45:52]</a>, <a class="yt-timestamp" data-t="01:47:25">[01:47:25]</a>. This is likened to the emergence of capabilities in large language models <a class="yt-timestamp" data-t="01:55:12">[01:55:12]</a>.