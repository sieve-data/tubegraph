---
title: Combining multiple vision encoders for improved performance
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

The field of [[vision_language_models_and_encoders | Vision Language Models]] (VLMs) is actively exploring methods to enhance model performance. One approach involves combining different pre-trained [[vision_language_models_and_encoders | vision encoders]] to leverage their unique strengths [[03:12]].

## Ensemble of Vision Encoders

Several research groups are investigating the efficacy of using multiple [[vision_language_models_and_encoders | visual encoders]] within a single multimodal model. The idea is that different [[vision_language_models_and_encoders | vision encoders]], trained on diverse datasets with varied objectives, will capture distinct types of visual information [[03:00]].

For instance, the Huawei paper, "From Clip to Dino: Visual Encoders Shout in Multimodal Large Language Models" (though later retracted), proposed feeding an input image into *two* different [[vision_language_models_and_encoders | Vision Transformers]]:
*   [[vision_transformer_encoders_and_pretraining | CLIP]] (Contrastive Language-Image Pre-training) from OpenAI, which is good at capturing [[pretraining_and_scaling_laws_for_vision_encoders | global semantic information]] [[30:28]].
*   Dino (specifically DinoV2) from Meta, which was trained with a self-supervised objective and excels at "fine-grained pixel information" [[30:34], [39:51]].

By combining the embeddings from both [[vision_language_models_and_encoders | vision encoders]], the model effectively creates an "ensemble" of [[vision_language_models_and_encoders | visual encoders]], aiming for a more robust and comprehensive understanding of the image [[31:08]]. The expectation is that the combined output will be superior to any single encoder individually [[31:28]].

### Multi-Level Feature Fusion

Beyond simply combining the final outputs of different [[vision_language_models_and_encoders | vision encoders]], some approaches also leverage "intermediate features" from within the encoder's architecture [[31:54]]. These features represent different levels of abstraction:
*   **Lower layers** capture "low-level detailed information" like edges and textures, which are helpful for fine-grained tasks [[32:04], [38:32]].
*   **Higher layers** encode "more high-level semantic" and global concepts [[32:11]].

The "Comm" paper, for example, used a "multi-level feature fusion" approach by taking features from various layers (e.g., Layer 12 and Layer 24) of both [[vision_transformer_encoders_and_pretraining | CLIP]] and DinoV2 [[32:01], [38:41]]. This strategy acknowledges that different layers' representations are useful for different tasks [[01:24:12]].

## Benefits and Trade-offs

While combining [[vision_language_models_and_encoders | vision encoders]] can lead to improved performance, there are important considerations:

*   **Improved Accuracy**: The "Comm" paper demonstrated a slight improvement in Visual Question Answering (VQA) accuracy when combining [[vision_transformer_encoders_and_pretraining | CLIP]] and Dino, as well as using multi-layer features [[01:25:50]]. For instance, [[vision_transformer_encoders_and_pretraining | CLIP]] alone achieved 68.8 VQA accuracy, while the combination of [[vision_transformer_encoders_and_pretraining | CLIP]] and Dino (with multi-layer features) reached 70.45 [[01:25:37]].
*   **Increased Complexity and Cost**: Using multiple [[vision_language_models_and_encoders | visual encoders]] significantly increases the model's size and computational requirements during both training and inference. This added complexity and cost may not always justify the marginal performance gains [[01:26:50]]. For a 1.65 point improvement in VQA accuracy, running a model that is "twice the size" incurs higher GPU costs and longer training times [[01:26:50], [01:27:25]].

## Connection to [[new_techniques_in_vision_encoder_integration | Vision Encoder Integration]]

The method of combining multiple [[vision_language_models_and_encoders | vision encoders]] is an aspect of [[new_techniques_in_vision_encoder_integration | new techniques in vision encoder integration]]. These techniques often involve using a small "connector" component, typically a Multi-Layer Perceptron (MLP) or a cross-attention module, to bridge the [[vision_language_models_and_encoders | vision encoder]] outputs to the [[vision_language_models_and_encoders | large language model]] [[02:52], [03:09], [03:38]]. In most cases, these [[vision_language_models_and_links | vision encoders]] are kept frozen (parameters are not updated during training) to reduce computational burden [[02:03]]. While some models might try more complex connectors, like a small [[vision_transformer_encoders_and_pretraining | Vision Transformer]] layer, experiments have shown that simpler methods, such as a single linear layer or MLP, often suffice and provide no significant benefit from added complexity [[01:31:52], [01:32:00]].