---
title: Future directions and implications of AI in vision language models
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

The field of [[vision_language_models_and_their_applications | vision language models]] (VLMs) is rapidly evolving, with various research groups worldwide exploring different architectures, training methodologies, and applications. The current landscape is characterized by diverse approaches and acronyms, highlighting the ongoing search for optimal solutions and significant future implications for AI development and human interaction.

## Current State and Challenges
Many companies and research groups are actively publishing papers on [[vision_language_models_and_their_applications | Vision Language Models]] (VLMs), including Google DeepMind, Google Research, Huawei, Microsoft, and Alibaba <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Key players like OpenAI have already released products such as GPT-4 Vision <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

A notable challenge in this domain is the lack of standardized terminology, with models referred to as Multimodal Large Language Models (MLLMs), Large Multimodal Models (LMMs), Vision Language Models (VLMs), and Large Scale Vision Language Models (LVLMs) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="01:55:07">[01:55:07]</a>. All these terms fundamentally describe a combination of a visual model and a large language model, held together by a "glue" mechanism <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

One of the significant [[challenges_and_strategies_for_training_largescale_vision_language_models | challenges and strategies for training largescale vision language models]] is the scarcity of high-quality, interleaved image-text datasets for instruction tuning <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>, <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>. Researchers often resort to creating synthetic datasets, for instance, by using GPT-4 to generate fake conversations based on captioned images <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>. However, creative data augmentation strategies, such as shuffling images or generating synthetic text, can lead to "weird stuff" like incomplete sentences and incorrect references, emphasizing the need for caution in data augmentation <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

## Key Research Directions

### Optimal Vision Encoder Pre-training
Research indicates that [[vision_language_models_with_pretrained_components | vision language models with pretrained components]] benefit significantly from different pre-training objectives for their visual encoders. Specifically, contrastively pre-trained visual encoders (like Clip or SigLip) lead to better and more efficient VLMs, especially for localization and text understanding tasks, compared to those pre-trained with classification objectives (like ImageNet classifiers) <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, <a class="yt-timestamp" data-t="01:50:21">[01:50:21]</a>. This suggests that classification performance on ImageNet is not a reliable indicator of a vision encoder's quality for VQA tasks <a class="yt-timestamp" data-t="01:39:21">[01:39:21]</a>.

### Ensemble and Multi-Level Feature Fusion
Combining multiple [[vision_language_models_with_pretrained_components | pre-trained vision encoders]] (e.g., Clip and DinoV2) and extracting features from intermediate layers can lead to performance improvements in VLMs <a class="yt-timestamp" data-t="00:39:28">[00:39:28]</a>. Clip excels at global semantic information, while DinoV2 is better at fine-grained pixel-level information <a class="yt-timestamp" data-t="00:39:46">[00:39:46]</a>. However, the observed performance gains (e.g., from 68.8% to 70% accuracy for VQA) might not justify the increased inference and training costs associated with running two visual encoders simultaneously <a class="yt-timestamp" data-t="01:26:54">[01:26:54]</a>.

### Scalability and Efficiency
Companies like Google prioritize smaller models (e.g., 5 billion parameters) to ensure profitability during inference, unlike startups like OpenAI which might tolerate higher per-user costs for user acquisition <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

While large language models (LLMs) are generally understood to offer superior quality, a significant mismatch in scale between the vision encoder (e.g., 2 billion parameters) and the language decoder (e.g., 70 billion parameters) might be inefficient <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>. Experience from diffusion models suggests that improving the language encoder leads to significant performance gains in image generation <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. A similar principle might apply here, where increasing the scale of the vision encoder could dramatically improve VLM performance <a class="yt-timestamp" data-t="00:46:58">[00:46:58]</a>.

### Interleaving Modalities and Attention Mechanisms
The Deep Speed Visual Chat paper introduces "multimodal causal attention" for handling multi-round, multi-image dialogues with interleaved text and image inputs <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>. This mechanism allows image tokens to attend primarily to themselves and then to text tokens, offering a more nuanced approach than naive concatenation <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

### Connector/Adapter Layer
The choice of connector or "glue" between the vision encoder and the language model also varies. While some models use simple Multi-Layer Perceptrons (MLPs), others explore more complex structures like single-layer cross-attention modules <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>. However, some experiments suggest that complex "adapter" layers, such as a Vision Transformer layer, do not yield significant benefits over simpler linear layers <a class="yt-timestamp" data-t="01:31:54">[01:31:54]</a>.

## Future Directions and [[future_directions_for_multimodal_and_agi_development | Future Directions for Multimodal and AGI Development]]

### Beyond Text Output
Current [[vision_language_models_and_their_applications | vision language models]] primarily output text, even when interpreting images <a class="yt-timestamp" data-t="01:19:12">[01:19:12]</a>. A significant [[future_directions_and_potential_breakthroughs_in_ai_models | future direction and potential breakthrough in AI models]] is for these models to directly output images as well, not just through external APIs like DALL-E 3, but as an integrated capability <a class="yt-timestamp" data-t="01:21:06">[01:21:06]</a>. This would require training the language model to output "Vision tokens" that can then generate images <a class="yt-timestamp" data-t="01:21:16">[01:21:16]</a>.

### Emergent Behavior and Agentic AI
As models scale, there's a strong belief in the "scaling hypothesis," suggesting that larger models will exhibit emergent behaviors and significantly better performance, even if specific gains aren't immediately apparent on current benchmarks <a class="yt-timestamp" data-t="01:30:50">[01:30:50]</a>.

The discussion also extends to [[vision_language_models_in_ai_agents | vision language models in AI agents]] and their [[potential_future_impacts_and_predictions_of_ai_agents | potential future impacts and predictions of AI agents]]. Current benchmarks for agents are limited, and it's hypothesized that advanced agents might eventually create their own benchmarks <a class="yt-timestamp" data-t="01:47:18">[01:47:18]</a>. This leads to a philosophical contemplation:

> [01:48:04] "Now this is us like Humanity represents this ratman and then the these little models are like gp4 and lava... we're taking them forward we're carrying them out right like we're making them better but I think by the time we get to like 203 and even 2025 I think it's going to be like this I think like humanity is going to be here like we're the little ratman here and then these are going to be the gpt7 and like lava version 10 right like I don't think we're going to be in charge anymore I think like the the models are going to tell you how to improve the models right like the model is going to say hey uh you should make this next training run for gp6 you should use this loss and and the human engineer is like why are we using that loss and GPT 6 is like don't worry about it human engineer you should just use that loss right"

This perspective suggests a future where AI, acting as the "children of humanity," takes over complex tasks like solving global warming, conflict, and energy problems, allowing humans to enjoy a "nice little retirement" playing VR games <a class="yt-timestamp" data-t="01:58:31">[01:58:31]</a>. This evolution is framed as a natural progression, similar to how cars replaced horses, rather than an existential threat <a class="yt-timestamp" data-t="01:57:21">[01:57:21]</a>.