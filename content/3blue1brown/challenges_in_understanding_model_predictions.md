---
title: Challenges in understanding model predictions
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

Understanding why a [[large_language_models_and_their_function | large language model]] (LLM) makes specific predictions can be incredibly challenging <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>. This difficulty stems from the complex nature of how these models are designed and trained.

## The Probabilistic Nature of Predictions

A [[large_language_models_and_their_function | large language model]] operates as a sophisticated mathematical function designed to predict the next word in any given piece of text <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. Instead of predicting a single word with certainty, it assigns a probability to all possible next words <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

When constructing a chatbot, the model repeatedly predicts the next word based on user input <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. While the model itself is deterministic <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>, its output can vary for the same prompt because it may randomly select less likely words along the way to make the output appear more natural <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This variability contributes to the difficulty in pinpointing the exact cause of a specific response.

## Emergent Behavior from Parameter Tuning

The behavior of a language model is entirely determined by its continuous values, known as [[role_of_parameter_tuning_in_machine_learning_models | parameters]] or weights <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. [[large_language_models_and_their_function | Large language models]] can have hundreds of billions of these [[role_of_parameter_tuning_in_machine_models | parameters]] <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

No human manually sets these [[role_of_parameter_tuning_in_machine_learning_models | parameters]]; they begin randomly <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. Instead, they are refined through an extensive training process <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. An algorithm called backpropagation is used to tweak these [[role_of_parameter_tuning_in_machine_learning_models | parameters]], making the model more likely to choose correct words and less likely to choose incorrect ones based on trillions of examples <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. This massive scale of computation for training makes the process mind-boggling, potentially taking over 100 million years even with a billion operations per second <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.

Additionally, after initial pre-training, chatbots undergo further training using reinforcement learning with human feedback (RLHF) <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. Human workers flag and correct unhelpful or problematic predictions, further adjusting the model's [[role_of_parameter_tuning_in_machine_learning_models | parameters]] to align with user preferences <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

While researchers design the overall framework and operations, such as those in [[role_of_transformers_in_language_models | transformers]] <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a> (which use "attention" to refine word meanings <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a> and feed-forward neural networks <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>), the specific behavior of the model is an "emergent phenomenon" <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>. This emergence arises from the tuning of its hundreds of billions of [[role_of_parameter_tuning_in_machine_learning_models | parameters]] during training <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. This complex interplay of vast numbers of parameters and continuous refinement makes it exceptionally difficult to determine the precise reasons behind any given prediction <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.