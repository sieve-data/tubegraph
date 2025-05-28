---
title: Selfsupervised learning
videoId: MVWYTFs9M-s
---

From: [[hu-po]] <br/> 

Self-supervised learning (SSL) is a machine learning approach where a system learns to capture relationships within its inputs without requiring explicit, human-provided labels <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a> <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. Unlike supervised learning, which requires a target label for every input (e.g., a class, bounding box, or segmentation for an image), SSL automatically generates its own targets from the input data <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a> <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. A common example is a masked task, where a portion of the input is hidden, and the model attempts to reconstruct the missing part <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Families of Approaches

There are two primary families of approaches in self-supervised learning for images:

1.  **Invariance-Based Methods** <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>:
    *   These methods train an encoder to produce similar embeddings (vector representations) for two or more "views" of the same input image <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
    *   "Views" typically refer to augmented versions of the original image, created using [[handcrafted_data_augmentation | handcrafted data augmentation]] techniques like scaling, cropping, or color jittering <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
    *   The goal is to pull together representations of semantically similar images and push apart those of semantically dissimilar ones <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a> <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.
    *   **Pros**: Can produce high-[[semantic_versus_low_level_representations | semantic representations]] <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
    *   **Cons**: Introduce strong biases due to the specific data augmentations used, which may hinder generalization to different downstream tasks or modalities <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a> <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. Data augmentation itself can also be computationally expensive <a class="yt-timestamp" data-t="01:28:09">[01:28:09]</a>.

2.  **Generative Methods (Reconstruction-Based)** <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a> <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>:
    *   These approaches aim to reconstruct a corrupted or masked portion of the input signal directly <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a> <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
    *   A common technique involves masking out random patches of an image and training a model (often an encoder-decoder architecture) to reconstruct the missing pixels <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a> <a class="yt-timestamp" data-t="00:49:35">[00:49:35]</a>.
    *   **Pros**: Require less prior knowledge than invariance-based methods and can generalize more easily across modalities <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.
    *   **Cons**: Often produce representations of a lower semantic level because the model dedicates significant capacity to reconstructing pixel-level details (like texture and color) rather than high-level content <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a> <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.

## Joint Embedding Predictive Architectures (JEPA)

A third conceptual category, and the focus of the IGEPA paper, is the **Joint Embedding Predictive Architecture (JEPA)** <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a> <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>. This approach combines elements of both invariance-based and generative methods.

*   **Core Idea**: Predict missing information in an abstract [[feature_space_motion_supervision_in_GANs | representation space]] (or embedding space) rather than directly in pixel space <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a> <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a>.
*   **Mechanism**: Given a *context block* from an image, the model predicts the *representations* of various *target blocks* from the same image <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a> <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>.
*   **Benefits of Predicting in Representation Space**:
    *   **Computational Efficiency**: Significantly reduces computation and memory needs compared to pixel-level reconstruction, leading to faster training <a class="yt-timestamp" data-t="01:19:11">[01:19:11]</a> <a class="yt-timestamp" data-t="01:39:27">[01:39:27]</a>.
    *   **Semantic Focus**: By eliminating the need to reconstruct unnecessary pixel-level details, the model is forced to learn more [[semantic_versus_low_level_representations | semantic features]] <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a> <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.
*   **Architecture (IGEPA Specifics)** <a class="yt-timestamp" data-t="00:55:16">[00:55:16]</a>:
    *   Uses [[Vision Transformers | Vision Transformers]] (ViT) for the context encoder, target encoder, and predictor <a class="yt-timestamp" data-t="00:55:19">[00:55:19]</a>.
    *   **Context Encoder ($F_\theta$)**: Processes the visible context block from the image <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.
    *   **Target Encoder ($F_{\bar{\theta}}$)**: Produces the true representations of the target blocks. Its weights are updated via [[Model ensembling techniques | exponential moving average]] (EMA) of the context encoder's weights, acting as a form of regularization and helping prevent [[representation_collapse | representation collapse]] <a class="yt-timestamp" data-t="01:02:12">[01:02:12]</a> <a class="yt-timestamp" data-t="01:17:54">[01:17:54]</a> <a class="yt-timestamp" data-t="01:59:53">[01:59:53]</a>.
    *   **Predictor ($G_\phi$)**: Takes the context encoder's output and positional tokens (indicating the location of the masked targets) to predict the representations of the target blocks <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a> <a class="yt-timestamp" data-t="01:14:52">[01:14:52]</a>.
    *   **Loss Function**: An L2 distance (squared Euclidean distance) between the predicted representations and the true target representations <a class="yt-timestamp" data-t="01:16:26">[01:16:26]</a>. This simple loss encourages the model to generate accurate abstract representations without needing to match exact pixel values <a class="yt-timestamp" data-t="01:19:09">[01:19:09]</a>.

## Key Concepts and Considerations

*   **Image Representations / Embeddings**: A vector of numbers that represents an image, aiming to capture its content <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **[[Semantic_versus_low_level_representations | Semantic vs. Low-Level Representations]]**:
    *   **High Semantic**: Embeddings that represent the high-level content or meaning of an image (e.g., "this is a flamingo") <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
    *   **Low Semantic**: Embeddings that capture fine-grained details like texture, color, and visual appearance <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. IGEPA aims for high semantic representations <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.
*   **Masking Strategy**: Crucial for defining the self-supervised task. IGEPA uses a multi-block masking strategy, where multiple (e.g., four) possibly overlapping blocks are randomly sampled from the target representations <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a> <a class="yt-timestamp" data-t="01:06:36">[01:06:36]</a>. The size and aspect ratio of these blocks are found to be highly sensitive hyperparameters <a class="yt-timestamp" data-t="02:01:33">[02:01:33]</a>.
*   **Energy-Based Models (EBMs)**: A framework under which self-supervised learning can be understood. EBMs assign a low "energy" (scalar value) to compatible inputs and high energy to incompatible ones <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. In latent space, points that are closer together (low distance) have low energy <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **[[Representation_collapse | Representation Collapse]]**: A common issue in self-supervised learning where the model produces a constant output regardless of the input. Solutions include contrastive losses, minimizing informational redundancy, or using asymmetric architectures <a class="yt-timestamp" data-t="00:42:35">[00:42:35]</a> <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a>.
*   **[[Model_ensembling_techniques | Exponential Moving Average (EMA)]]**: Used to update the target encoder's weights, averaging over time to stabilize training and prevent collapse <a class="yt-timestamp" data-t="01:02:12">[01:02:12]</a> <a class="yt-timestamp" data-t="01:17:54">[01:17:54]</a>.
*   **[[Comparison with other selfsupervised and supervised models | Evaluation Benchmarks]]**: Models are often evaluated on downstream tasks like ImageNet 1K classification using linear probing (freezing the pre-trained encoder and training a small linear classifier on top) or fine-tuning <a class="yt-timestamp" data-t="01:28:57">[01:28:57]</a> <a class="yt-timestamp" data-t="01:29:07">[01:29:07]</a>. Other tasks include object counting and depth prediction <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a> <a class="yt-timestamp" data-t="01:35:57">[01:35:57]</a>.

## IGEPA Performance

IGEPA demonstrates strong performance on various image tasks, often matching or slightly surpassing previous state-of-the-art self-supervised methods like Masked Autoencoders (MAE), Context Autoencoders (CAE), and Data2Vec <a class="yt-timestamp" data-t="01:25:52">[01:25:52]</a> <a class="yt-timestamp" data-t="01:33:09">[01:33:09]</a>. Its primary advantage lies in its computational efficiency, requiring significantly less GPU hours for pre-training compared to methods that predict in pixel space or rely heavily on data augmentations <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a> <a class="yt-timestamp" data-t="01:40:01">[01:40:01]</a>.

IGEPA is a notable step towards simpler, faster, and more generalizable self-supervised learning techniques, particularly for visual representation learning <a class="yt-timestamp" data-t="02:13:20">[02:13:20]</a>.