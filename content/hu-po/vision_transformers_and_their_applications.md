---
title: Vision Transformers and their applications
videoId: MVWYTFs9M-s
---

From: [[hu-po]] <br/> 

## What are Vision Transformers?

A [[vision_transformer_encoders_and_pretraining | Vision Transformer]] (ViT) is a type of [[vision_transformer_encoders_and_pretraining | Transformer]] model used as a vision encoder [01:00:04] [01:00:27]. It processes images by breaking them into small "patches" [01:00:30]. These patches are then treated like a sequence or "sentence" and fed into the Transformer's attention blocks [01:00:34]. Each patch acts as a token, and the Transformer's self-attention mechanism allows different parts of the image to "pay attention" to other parts [01:56:56] [00:56:56]. The basic architecture of a ViT consists of stacked Transformer layers, each containing a self-attention operation followed by a fully connected Multi-Layer Perceptron (MLP) [00:55:28].

## Introducing i-JEPA

The Image-based Joint Embedding Predictive Architecture (i-JEPA) is a non-generative, self-supervised approach to learning highly semantic image representations [00:06:52] [00:31:38]. Developed by Meta AI and academic institutions, including Yann LeCun, it aims to produce rich image embeddings without relying on handcrafted data augmentations [00:16:16] [00:37:36] [01:55:48].

### Key Concepts

*   **Semantic Representations:** i-JEPA focuses on creating image representations (vectors of numbers, also called embeddings) that capture the content of an image rather than its texture, color, or visual appearance [00:07:07] [00:27:00].
*   **Non-Generative:** Unlike methods that reconstruct pixel-level details, i-JEPA predicts in an abstract representation space, thus avoiding the computational cost and bias associated with pixel-level reconstruction [00:31:52] [00:36:00] [01:16:17] [01:55:54]. This design choice is believed to lead the model to learn more semantic features [00:27:32].
*   **Self-Supervised Learning:** i-JEPA uses a self-supervised task, meaning it doesn't require explicit human labeling [00:08:40] [00:09:10]. The model generates its own training signals [02:10:38].

### Architectural Components

i-JEPA utilizes three main components, all based on [[vision_transformer_encoders_and_pretraining | Vision Transformer]] architectures [01:00:01] [01:55:18]:

1.  **Context Encoder (Fθ):** A [[vision_transformer_encoders_and_pretraining | Vision Transformer]] that processes a specific "context block" (a chunk) of an image [00:55:19] [01:11:55].
2.  **Target Encoder (Fθ̄):** Another [[vision_transformer_encoders_and_pretraining | Vision Transformer]] whose weights are updated via an exponential moving average (EMA) of the context encoder's weights [01:02:14]. This ensures the target encoder is a "smoother" version of the context encoder, providing a stable target for learning [01:17:56] [01:59:53].
3.  **Predictor (Gφ):** A lightweight, narrow [[vision_transformer_encoders_and_pretraining | Vision Transformer]] that takes the context encoder's output and [[role_of_positional_embeddings_in_transformers | positional embeddings]] as input [01:00:34]. It then predicts the representations of various "target blocks" in the same image [01:00:39].

### Self-Supervision Strategy

The core idea of i-JEPA is simple: given a single context block, predict the representations of various target blocks within the same image [00:09:17] [01:11:17].

*   **Masking Strategy:** The process involves masking out portions of the image to create a self-supervised task [00:53:45]. i-JEPA uses a "multi-block masking strategy," where multiple, possibly overlapping, target blocks are randomly sampled [01:06:06] [01:53:06]. This strategy is crucial for guiding the model to learn semantic representations [01:00:41] [01:55:00].
*   **Context and Target Blocks:** The context block is a single, randomly sampled portion of the image [01:09:32]. The target blocks are derived from the original image and their representations are computed by the target encoder [01:05:07]. To ensure a non-trivial prediction, any overlapping regions between the context and target blocks are removed [01:11:37].

### Loss Function and Training

*   **Prediction in Representation Space:** Unlike [[vision_transformers_vs_convolutional_networks | Masked Autoencoders (MAE)]] that predict in pixel space, i-JEPA predicts in a learned representation space [00:58:16] [01:10:07]. This means the model generates *embeddings* of the missing patches, not the pixel values themselves [01:16:17].
*   **L2 Loss:** The loss function is a simple L2 distance (squared Euclidean distance) between the predicted patch representations and the actual target patch representations [01:16:27]. This L2 loss encourages the predicted embeddings to be close to the true embeddings, driving the model to learn meaningful representations [01:16:53].
*   **Optimization:** The parameters of the predictor and the context encoder are updated using gradient-based optimization (e.g., AdamW optimizer) [01:17:49] [01:58:28]. The target encoder's weights are then updated through the EMA of the context encoder's weights [01:17:54].

## Performance and Applications

i-JEPA demonstrates strong performance across various computer [[vision_language_models_and_encoders | vision]] tasks while being computationally efficient.

### Image Classification

*   **ImageNet 1K:** i-JEPA achieves strong linear probing performance on ImageNet 1K, a benchmark dataset with 1,000 classes [01:13:31] [01:52:50]. Its results are competitive with or surpass other self-supervised methods like MAE, CAES, and Data2Vec, especially in semi-supervised settings with limited labeled data (e.g., 1% ImageNet 1K labels) [01:27:00] [01:27:52] [01:31:07].
*   **Computational Efficiency:** A significant advantage of i-JEPA is its reduced computational cost during pre-training. It requires fewer epochs and GPU hours compared to pixel-reconstruction methods like MAE, and is faster than other view-invariant methods like iBOT [01:13:14] [01:28:40]. For example, training a ViT Huge 14 on ImageNet takes under 72 hours using 16 A100 GPUs [01:09:50] [01:10:47]. This efficiency is largely attributed to predicting in representation space rather than image space [00:23:25] [01:31:22].

### Low-Level Vision Tasks

i-JEPA also performs well on low-level [[vision_language_models_and_encoders | vision]] tasks, such as object counting and depth prediction [01:01:01] [01:35:57]. This suggests that its learned representations are robust and applicable to a wide range of tasks beyond classification [01:31:01].

### Scaling Properties

The paper explores the impact of increasing model size and pre-training dataset size. Generally, larger models and larger datasets lead to better performance, although this scaling relationship isn't always perfectly linear [01:41:30] [01:42:00].

## Design Philosophy and Challenges

### The Role of Priors

i-JEPA's developers emphasize their goal of learning representations "without relying on handcrafted data augmentation" [00:16:16]. They argue that common augmentations like scaling, cropping, and color jittering encode "prior knowledge" into the training process [00:24:57] [00:42:00]. By avoiding these, i-JEPA aims for a less rigid inductive bias, theoretically making it applicable to a wider set of tasks and modalities beyond images [00:27:34] [00:37:09]. However, even masking strategies inherently introduce a prior, as they assume semantic meaning is preserved when parts of an image are removed [00:50:02].

### Hyperparameter Sensitivity

The performance of i-JEPA is sensitive to certain hyperparameters, particularly the size and aspect ratio of the sampled context and target blocks [02:01:54]. Ablation studies show that optimal ranges for these parameters lead to significantly better results, indicating that careful tuning is required [02:02:18].

### Addressing Model Collapse

Like other [[vision_language_models_and_encoders | joint embedding]] architectures, i-JEPA faces the challenge of "representation collapse," where the model produces constant outputs regardless of the input [00:42:35]. To prevent this, i-JEPA leverages an asymmetric architectural design between the context and target encoders [00:44:26] [01:13:00], as well as the use of the exponential moving average for updating the target encoder's weights [01:02:22] [01:19:02].