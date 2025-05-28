---
title: Text Encoder Ensembles in Diffusion Models
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Text encoders play a crucial role in text-to-image diffusion models, specifically in deriving suitable representations from pre-trained models for text conditioning [00:54:48]. The text conditioning, often referred to as "C," is the input prompt provided by the user [00:54:53], and it also corresponds to the captions in training datasets [00:55:05]. The quality of the text encoder significantly predicts the final quality of the generated image [01:35:51].

## Utilizing Text Encoder Ensembles

Generally, [[scaling_and_training_techniques_for_diffusion_models | ensembles of models]] tend to outperform single models, particularly when they are trained with slightly different objectives on varied datasets [01:36:02]. For instance, features from different models like Clip, DYO, or Segment Anything represent distinct aspects of an image, and their combination yields superior results compared to individual features [01:36:10].

The primary motivation for using multiple text encoders is to enhance the overall model performance, aiming for [[performance_and_scalability_of_diffusion_models_with_transformers | state-of-the-art]] text encoding [01:37:40].

### Specific Text Encoders in Stable Diffusion 3

Stable Diffusion 3 (SD3) employs an ensemble of three distinct text encoders:
*   Clip G14 [00:55:18]
*   Clip L14 (Open Clip BG14) [00:55:36]
*   T5 XXL (Google's T5 1.1 XXL) [00:55:40]

These are pre-trained and used in a frozen state, meaning their weights are not updated during the diffusion model's training [00:55:11]. The outputs (embeddings) from these encoders are then concatenated together [00:57:51].

### Addressing Computational Costs

While ensembles improve performance, they demand more computational power and memory [01:36:26]. To mitigate this, SD3 implements several strategies:

#### Dropout during Training
During [[training_and_implementation_details_of_transformerbased_diffusion_models | training]], SD3 uses an aggressive dropout rate of 46% for individual text encoders [01:37:53]. This means that the output from one of the text encoders is sometimes replaced with zeros [01:38:09].
> [!NOTE] Robustness and Flexibility
> This dropout strategy makes the model robust to various permutations of text encoders [01:39:17]. At inference time, users can choose to use an arbitrary subset of the three encoders [01:38:28]. For example, if a user has a GPU with limited VRAM and cannot fit the large T5 XXL model, they can still run the model effectively using only the two Clip-based encoders by dropping out the T5 embeddings (replacing them with zeros) [01:39:00]. This results in only a "limited performance drop" [01:39:37].

#### Pre-computing Embeddings
To further speed up [[training_and_implementation_details_of_transformerbased_diffusion_models | training]], the text embeddings are pre-computed before the training process begins [02:03:54]. Instead of encoding text during each mini-batch, the entire dataset's captions are fed through the three text encoders once, and the pre-computed embeddings are then sampled for training [02:04:20].

### Specialized Contributions of Different Encoders

The different text encoders in the ensemble contribute unique strengths to the model's capabilities:

*   **Spelling:** The T5 text encoder is particularly important for accurately spelling words in generated images [01:40:01]. When the T5 encoder is removed, the model makes spelling mistakes [01:40:21]. This suggests that T5, possibly due to its different training objective (e.g., visual question answering), provides a more nuanced understanding of linguistic structures compared to Clip encoders [01:41:47].
*   **Nuance and Specificity:** The T5 encoder also enhances the model's ability to interpret nuanced textual instructions. For example, in a prompt like "a mischievous ferret with a playful grin squeezes itself into a glass jar," the T5 encoder helps ensure the ferret is explicitly *in* the jar. Without it, the model might generate an image of a ferret *around* the jar, failing to capture the "into" aspect [01:42:49]. In contrast, the Clip encoders are more focused on broader semantic understanding, such as the overall visual concept of "ferret" and "jar" [01:43:06].

This demonstrates that different text encoders, with their varied training methodologies, contribute distinct representations that, when combined, lead to a more comprehensive and capable [[scalable_diffusion_models_with_transformers | diffusion model]].