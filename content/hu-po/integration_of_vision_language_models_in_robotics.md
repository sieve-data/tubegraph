---
title: Integration of Vision Language Models in Robotics
videoId: Utv0XpXUGQE
---

From: [[hu-po]] <br/> 

The integration of [[vision_language_models | Vision language models]] (VLMs) into robotics aims to leverage broad knowledge from internet-scale data to enhance robot capabilities, particularly in generalization and semantic reasoning. A prominent example of this integration is the [[rt2_robotic_transformer_for_vision_language_action_models | RT2 Robotic Transformer 2]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## RT2: A Vision Language Action Model

[[rt2_robotic_transformer_for_vision_language_action_models | RT2]] is described as a vision language action model, meaning it incorporates text (language), images (vision), and robot actions <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Developed by Google DeepMind and Google Brain, it aims to combine the strengths of these merged teams <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The core idea behind [[rt2_robotic_transformer_for_vision_language_action_models | RT2]] is to learn from diverse web data—such as code, newspapers, and chess—and apply this knowledge to robotic control <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This approach is largely a continuation of work seen in other [[large_language_models_in_robotics | large language models in robotics]] papers, like "Language Models are General Pattern Machines," but in a more applied context <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## End-to-End Robotic Control

A key aspect of [[rt2_robotic_transformer_for_vision_language_action_models | RT2]] is its focus on "end-to-end" robotic control <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. End-to-end refers to a system that processes inputs directly from sensors (like images) and outputs direct control commands to the robot's joints, without intermediate control models <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. The goal is to enable a single model to map robot observations to actions while benefiting from large-scale pre-training on web data <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

This approach contrasts significantly with modular robotics frameworks like ROS (Robot Operating System) <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Historically, ROS used many separate computational modules (e.g., for vision, path planning, control), which communicated with each other <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. While modularity aimed for separate improvements, the trend in [[large_language_models_in_robotics | large language models in robotics]] points towards single, integrated models for achieving general AI <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## Action Tokenization

A novel aspect of [[rt2_robotic_transformer_for_vision_language_action_models | RT2]] is expressing robot actions as text tokens <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This allows actions to be incorporated directly into the training set alongside natural language tokens, treating them as another "language" <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. The robot's action space is discretized into 256 bins for each dimension <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>. The action vector includes six dimensions for positional and rotational displacement (X, Y, Z translation, and Euler angles for rotation), a gripper extension command, and a command to terminate the episode <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

To integrate these actions into existing [[vision_language_models | VLM]] tokenizers, [[rt2_robotic_transformer_for_vision_language_action_models | RT2]] overwrites the 256 least frequently used tokens in the model's vocabulary to represent these discrete action bins <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>. This approach allows the VLM to generate actions directly as part of its token sequence output <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>.

## Training Methodology

[[rt2_robotic_transformer_for_vision_language_action_models | RT2]] utilizes [[vision_language_models_with_pretrained_components | Vision language models with pretrained components]] like Pali-X and PaLM-E, which are designed for open-vocabulary visual question answering (VQA) and visual dialogue <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>. These models are co-fine-tuned on both internet-scale [[vision_language_models_and_their_applications | vision language tasks]] (VQA data) and robotic trajectory data <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

Co-fine-tuning is a critical detail: instead of fine-tuning only on robot data (which could lead to catastrophic forgetting of the general knowledge), [[rt2_robotic_transformer_for_vision_language_action_models | RT2]] balances the ratios of robot and web data in each training batch <a class="yt-timestamp" data-t="00:56:49">[00:56:49]</a>. This ensures that the model is exposed to both abstract visual concepts and low-level robot actions simultaneously, maintaining generalization <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>.

### Inference and Model Size

The largest [[rt2_robotic_transformer_for_vision_language_action_models | RT2]] model tested has 55 billion parameters, while a smaller version has 5 billion parameters <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>. Running such large models on typical robot hardware or desktop machines for real-time control is currently infeasible <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>. To address this, [[rt2_robotic_transformer_for_vision_language_action_models | RT2]] models are deployed as a multi-TPU (Tensor Processing Unit) cloud service, allowing the robot to query the service over a network <a class="yt-timestamp" data-t="01:02:17">[01:02:17]</a>. The 55-billion-parameter model operates at 1-3 Hertz (updates per second), while the 5-billion-parameter model runs at around 5 Hertz <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>.

## Emergent Capabilities and Generalization

[[rt2_robotic_transformer_for_vision_language_action_models | RT2]] demonstrates significant improvements in generalization compared to prior methods <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. It can adapt to novel objects, backgrounds, and environments not seen in its specific robot training data <a class="yt-timestamp" data-t="01:09:51">[01:09:51]</a>. For example, it can interpret commands like "move the banana on top of the flag of Germany" <a class="yt-timestamp" data-t="00:30:39">[00:30:39]</a>, or understand human recognition like "move the Coke can to the person with glasses" <a class="yt-timestamp" data-t="01:10:05">[01:10:05]</a>. This points to [[vision_language_models_in_ai_agents | emergent semantic reasoning]] capabilities inherited from the web-scale [[vision_language_models_and_their_applications | vision language models]]' pre-training <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

A notable [[impact_of_large_language_models_on_robotic_capabilities | impact of large language models on robotic capabilities]] is the ability to interpret commands not present in the robot training data and perform rudimentary reasoning, such as picking the smallest or largest object, or the one closest to another object <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The inclusion of Chain-of-Thought reasoning (where the model generates an internal "plan" in natural language before executing actions) further enables multi-stage semantic reasoning for more complex tasks <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>.

However, a key limitation is that while semantic and visual understanding generalizes, the robot does not acquire new abilities to perform novel physical motions <a class="yt-timestamp" data-t="01:29:24">[01:29:24]</a>. The model's physical skills remain constrained to the distribution of skills (e.g., pick and place variants) seen in the robot training data <a class="yt-timestamp" data-t="01:30:15">[01:30:15]</a>.

## Future Directions

The [[future_directions_and_implications_of_ai_in_vision_language_models | future directions and implications of AI in vision language models]] in robotics include exploring how new physical skills can be acquired, possibly by training on large corpuses of human videos and motion libraries <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. Addressing computation costs for real-time, high-frequency control is another challenge, with potential solutions in quantization and distillation techniques, or relying on cloud robotics and improving internet latency <a class="yt-timestamp" data-t="03:09:39">[03:09:39]</a>.

The authors express a hope for more open-source models to become available, indicating a desire within the research community for broader accessibility and collaboration in the field <a class="yt-timestamp" data-t="03:31:38">[03:31:38]</a>.