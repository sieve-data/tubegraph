---
title: Joint embedding predictive architecture
videoId: MVWYTFs9M-s
---

From: [[hu-po]] <br/> 

[[gpt4_ensemble_model_structure | GPT-4 Ensemble Model Structure]] was revealed to be an [[model_ensembling_techniques | ensemble of eight models]], each approximately 220 billion parameters, likely fine-tuned on slightly different data [00:00:57]. This strategy, known as [[model_ensembling_techniques | model ensembling]] or a mixture model, is popular in Kaggle competitions to achieve marginal performance gains [00:01:38]. It involves training many different versions of the same model on slightly varied data subsets, leading to more diverse outputs, from which the best can be selected [00:01:53]. This approach explains the reported high inference cost of GPT-4, as it potentially performs 16 inferences for each query [00:02:32]. OpenAI's 2021 Codex paper also describes a similar strategy of generating multiple samples and then filtering them down [00:04:33].

## Self-Supervised Learning with IJEPA

The main topic is a paper titled "Self-Supervised Learning from Images with a Joint Embedding Predictive Architecture" (IJEPA) [00:06:08]. This paper, primarily from Meta AI Research (including Yann LeCun), Mila, McGill, and New York University, explores learning highly semantic image representations [00:06:14].

### Semantic Image Representations
Image representations, also called embeddings, are vectors of numbers representing an image [00:06:58]. "Highly semantic" implies that these embeddings are designed to represent the content of an image rather than superficial aspects like texture, color, or visual appearance [00:07:07]. The IJEPA approach achieves this without relying on handcrafted data augmentation [00:07:34], which typically involves manually altering image appearance (e.g., flipping, cropping, blurring) to expand training data [00:07:40].

### Self-Supervised Learning
IJEPA employs a non-generative, self-supervised learning approach [00:08:33]. Self-supervised learning formulates training tasks that do not require explicit data labeling, often by masking a part of the input and attempting to reconstruct it [00:08:40].

The core idea of IJEPA is simple: from a single context block of an image, predict the representations of various target blocks within the same image [00:09:15]. The masking strategy, which involves sampling sufficiently large and spatially distributed context and target blocks, is crucial for guiding the model to produce semantic representations [00:09:53].

### Performance and Efficiency
IJEPA, when combined with a [[ai_model_architecture_and_parallelism_strategies | Vision Transformer]] (ViT), can train a ViT-Huge on ImageNet using 16 A100 GPUs in under 72 hours [01:10:44]. This allows it to achieve strong performance across various downstream tasks like linear classification, object counting, and depth prediction [01:12:55].

A key efficiency gain comes from predicting in representation space rather than image space [01:14:51]. This concept is also utilized in diffusion models, which often perform diffusion in a [[generative_latent_spaces_in_ai | latent space]] to save compute [01:15:00]. IJEPA predicts in representation space, leading to significantly reduced computation needed for self-supervised training [01:31:22].

Compared to other methods:
*   IJEPA shows competitive or superior performance on ImageNet classification (top-1 accuracy between 78-79%) while being significantly faster than alternatives like MAE [01:16:16].
*   It requires fewer pre-training epochs and less computational effort [01:32:05].
*   It performs well on low-level vision tasks (object counting, depth prediction) where [[ai_model_architecture_and_parallelism_strategies | generative architectures]] often struggle [01:35:24].

### Architectures for Self-Supervised Learning
The paper categorizes self-supervised learning into three main types, described within the framework of energy-based models (EBMs) [01:17:14]:

1.  **Joint Embedding Architectures**: These optimize an encoder to produce similar embeddings for compatible inputs (e.g., two augmented views of the same image) and dissimilar embeddings for incompatible inputs [01:32:38]. The challenge is avoiding representation collapse, where the model outputs constant embeddings regardless of input [01:42:35]. Solutions include contrastive losses, minimizing informational redundancy, or [[combining_different_blocks_in_neural_network_architectures | asymmetric architectural design]] [01:43:53].
2.  **Generative Architectures**: These directly reconstruct a signal (Y) from a compatible signal (X) using a decoder network, possibly conditioned on a latent variable (Z) [01:33:26]. An example is masked image modeling, where parts of an image are masked, and the model reconstructs the missing content [01:09:07]. This approach often leads to lower semantic representations because the model expends capacity on reconstructing pixel-level details like texture and color [02:20:00]. The loss function is applied in image space [01:34:31].
3.  **Joint Embedding Predictive Architectures (JEPAs)**: This is IJEPA's category. JEPAs predict the embeddings of a signal (Y) from a compatible signal (X) using a predictor network, conditioned on an additional variable (Z) [01:35:07]. The key difference from generative methods is that the loss function is applied in embedding (representation) space, not input (pixel) space [01:52:00]. This encourages the model to learn more semantic features by eliminating the need to reproduce unnecessary pixel-level details [01:51:16].

### IJEPA Architecture and Training
IJEPA uses three [[ai_model_architecture_and_paralleliam_strategies | Vision Transformers]]: a context encoder ($F_\theta$), a target encoder ($F_{\bar{\theta}}$), and a predictor ($G_\phi$) [01:55:08].

*   **Context Encoder ($F_\theta$)**: Processes a masked input image (context block) to produce patch-level representations [01:11:46].
*   **Target Encoder ($F_{\bar{\theta}}$)**: Produces the actual patch-level representations of the target blocks [01:05:48]. Its weights (${\bar{\theta}}$) are updated via an [[ai_model_architecture_and_parallelism_strategies | exponential moving average]] (EMA) of the context encoder's weights (${\theta}$) [01:17:54]. This acts as a regularization technique, preventing representation collapse and stabilizing training [01:18:56].
*   **Predictor ($G_\phi$)**: A lightweight ViT that takes the context encoder's output and, conditioned on [[positional_embeddings_in_transformers | positional tokens]] (representing the location of the target blocks), predicts the representations of the target blocks [01:00:34].

The training objective is to minimize the L2 distance between the predicted patch representations from the predictor ($S_{\hat{Y}}$) and the actual patch representations from the target encoder ($S_Y$) [01:16:26]. This L2 loss is simple and effective [01:19:11]. The parameters of the predictor and context encoder are learned through gradient-based optimization [01:17:48].

### Key Design Choices and Ablation Studies
*   **Predicting in Representation Space**: This is IJEPA's crucial component. It leads to faster convergence and learning of higher-semantic representations compared to pixel reconstruction methods [01:55:53].
*   **Masking Strategy**: The paper investigates different masking strategies:
    *   **Multi-block masking**: Samples multiple (e.g., four) possibly overlapping target blocks from the image [01:06:36]. This strategy proved to be significantly more effective (e.g., 54% accuracy) than other masking types [01:54:58].
    *   **Rasterized block masking**: Splits the image into four quadrants, using one to predict the others [01:53:23].
    *   **Random masking**: Targets a set of random patches, with the context being the image complement [01:54:21].
    *   The choice of scale and aspect ratio for these blocks is highly sensitive and impacts performance significantly [02:01:23].
*   **Predictor Architecture**: The depth (number of layers) and width of the predictor also affect performance, but with diminishing returns for increased size [02:04:47].

IJEPA's approach highlights a path for learning general representations with [[combining_different_blocks_in_neural_network_architectures | joint embedding architectures]] without relying on handcrafted view augmentations [01:56:08]. The models trained with IJEPA are released, allowing further research and application [02:08:48].