---
title: RT2 Robotic Transformer for Vision Language Action Models
videoId: Utv0XpXUGQE
---

From: [[hu-po]] <br/> 

RT2 (Robotic Transformer Number Two) is a vision-language-action (VLA) model developed by Google DeepMind, a result of the combined Google Brain and Google DeepMind teams <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This model integrates language (text), vision (images), and robot actions to enable end-to-end robotic control <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. It is largely a continuation of work seen in papers like "Language Models are General Pattern Machines," offering a more applied version of that research <a class="yt-timestamp" data-t="02:05:05">[02:05:05]</a>.

## Core Concepts

*   **Vision-Language-Action (VLA) Model**
    RT2 is categorized as a [[vision_language_models_in_ai_agents | Vision language models in AI agents]] <a class="yt-timestamp" data-t="06:55:05">[06:55:05]</a>. This means it processes both visual inputs (images) and language inputs (text) to directly generate robot actions <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. The model expresses actions as text tokens, fitting both natural language responses and robotic actions into the same format <a class="yt-timestamp" data-t="06:21:05">[06:21:05]</a>.

*   **End-to-End Robotic Control**
    "End-to-end" in robotics refers to a system that processes raw sensor data (e.g., images) and directly outputs control commands for the robot's joints <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. This contrasts with traditional modular robotics systems like ROS, which involve multiple separate modules for vision, planning, and control <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. RT2 aims for this direct integration, allowing the model to go all the way from image/sensor input to actual motor control signals <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. While the final inference is end-to-end, its training involves pre-training steps and a separate [[applications_in_vision_transformers | Vision Transformers]] component <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

*   **Generalization and Emergent Capabilities**
    A primary goal of RT2 is to boost generalization, which is the ability to adapt to tasks outside of its pre-training data distribution <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. The model is also designed to enable "emergent behaviors," meaning it can perform unexpected actions or reasoning not explicitly trained on, particularly in novel situations <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. However, it's important to note that the emergent capabilities are primarily in semantic understanding and visual concepts, not in acquiring new physical motions or generalizing outside its trained action space <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

*   **Semantic Reasoning**
    RT2 exhibits rudimentary semantic reasoning, allowing it to interpret complex commands like "picking up the smallest or largest object" or "the one closest to another object" <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. This capability stems from the vast common-sense knowledge gleaned from internet-scale language and vision data <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

## Architecture and Methodology

RT2 adapts previously proposed Vision Language Models (VLMs), specifically Google's Pali-X and PaLM-E, for robotic control <a class="yt-timestamp" data-t="44:06:00">[44:06:00]</a>.

### Action Tokenization
A key innovation is representing robot actions as text tokens, treating them like natural language tokens <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>. The action space consists of:
*   Six degrees of freedom (6DoF) for positional (X, Y, Z) and rotational (Euler angles) displacement <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>.
*   A gripper command (extension/distance) <a class="yt-timestamp" data-t="0:5:05">[0:5:05]</a>.
*   A discrete command for terminating the episode <a class="yt-timestamp" data-t="0:5:08">[0:5:08]</a>.

These continuous dimensions are discretized into 256 bins each, allowing them to be encoded as tokens <a class="yt-timestamp" data-t="48:27:00">[48:27:00]</a>. For models like PaLM-E, which can represent integers up to 1000 as unique tokens, this is straightforward <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a>. For others, like Pali-X (similar to Llama 2), individual digits of numbers might be separate tokens <a class="yt-timestamp" data-t="50:52:00">[50:52:00]</a>. To integrate these, RT2 "overwrites" 256 of the least frequently used tokens in the VLM's existing vocabulary (e.g., obscure Unicode symbols, rare emojis) to represent robot actions <a class="yt-timestamp" data-t="53:04:00">[53:04:00]</a>.

### Co-Fine-Tuning
Instead of naive fine-tuning solely on robotics data, RT2 uses a "co-fine-tuning" approach <a class="yt-timestamp" data-t="56:46:00">[56:46:00]</a>. This involves balancing robot trajectory data with the original web-scale vision-language data during training <a class="yt-timestamp" data-t="56:55:00">[56:55:00]</a>. This prevents catastrophic forgetting of the vast knowledge acquired during pre-training on web data, ensuring the model retains its broad understanding of abstract visual concepts while learning low-level robot actions <a class="yt-timestamp" data-t="57:01:00">[57:01:00]</a>. The ratio of robot to web data is balanced in each training batch, often by increasing the sampling weight for robot data <a class="yt-timestamp" data-t="57:09:00">[57:09:00]</a>.

### Output Constraints
To ensure the robot receives valid actions, RT2 constrains its output vocabulary. When prompted with a robot action task, the model is only allowed to sample valid action tokens <a class="yt-timestamp" data-t="59:38:00">[59:38:00]</a>. For standard vision-language tasks, it retains the full range of natural language tokens <a class="yt-timestamp" data-t="59:46:00">[59:46:00]</a>. This is partly managed by a specific task token that indicates whether the model should generate a natural language response or a robot action <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.

### Chain of Thought Reasoning
By augmenting training data to include a "plan" step (e.g., "Instruction: I'm hungry. Plan: Pick chocolate. Action: [robot action tokens]"), RT2 can perform multi-stage semantic reasoning <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. This "in-context" Chain of Thought prompting allows the model a place to plan its actions in natural language first, leading to more sophisticated command interpretation <a class="yt-timestamp" data-t="01:27:51">[01:27:51]</a>.

## Technical Details and Challenges

*   **Model Size and [[scaling_of_language_models_and_vision_transformers | Scaling of language models and vision transformers]]**
    The largest RT2 model uses 55 billion parameters, while a smaller variant uses 5 billion <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. The research explores if [[impact_of_large_language_models_on_robotic_capabilities | Impact of Large Language Models on Robotic Capabilities]] varies with parameter count <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

*   **Inference Speed and Latency**
    Running such large models for real-time robotic control is challenging <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. The 55-billion-parameter model runs at 1-3 Hertz (1-3 times per second), while the 5-billion-parameter model achieves around 5 Hertz <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>. This latency is a bottleneck, even for smaller models, due to messaging overhead in cloud-based deployments <a class="yt-timestamp" data-t="01:06:34">[01:06:34]</a>.

*   **Cloud-Based Deployment**
    To overcome hardware limitations on robots, RT2 models are deployed as a multi-TPU (Tensor Processing Unit) cloud service <a class="yt-timestamp" data-t="01:02:17">[01:02:17]</a>. The robot sends requests to this cloud service and receives actions in return, enabling computationally intensive models to be used <a class="yt-timestamp" data-t="01:04:51">[01:04:51]</a>.

*   **Simplified Perception**
    RT2's end-to-end approach potentially removes the need for highly calibrated cameras or complex 3D laser sensors (LIDAR) <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>. The model can implicitly learn to adapt to sensor quirks, which is crucial for consumer-grade robots <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>.

## Evaluation and Results

RT2 was extensively evaluated with 6,000 trials on a real 7-degrees-of-freedom mobile manipulator in an office kitchen environment <a class="yt-timestamp" data-t="01:07:14">[01:07:14]</a>. The robotic data was collected over 17 months using 13 robots <a class="yt-timestamp" data-t="01:08:03">[01:08:03]</a>.

The evaluation focused on generalization across:
*   **Unseen Objects:** Novel items the robot had not seen before <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.
*   **Unseen Backgrounds:** Different table textures or patterns <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.
*   **Unseen Environments:** Distinct physical locations (e.g., kitchen sink, office chair) <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.

### [[Comparison of RT2 with Previous Robotics Methodologies | Comparison of RT2 with Previous Robotics Methodologies]]
RT2's performance was compared against state-of-the-art baselines like RT1, VC1, R3M, and Moo <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>.
*   RT2 consistently outperformed these baselines, particularly in generalization tasks <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. For example, while RT1 might achieve 90% pick accuracy in seen environments, its performance could drop to 40% with a different background, whereas RT2 maintains much higher performance across varying conditions <a class="yt-timestamp" data-t="01:12:50">[01:12:50]</a>.
*   Fine-tuning alone was less effective than co-fine-tuning, and training from scratch on only robot data yielded significantly worse results <a class="yt-timestamp" data-t="01:22:47">[01:22:47]</a>.

### Emergent Capabilities (from [[integration_of_vision_language_models_in_robotics | Integration of Vision Language Models in Robotics]])
RT2 inherits capabilities from its web-scale pre-training, including:
*   **Multilingual Understanding:** Instantly understanding commands in different languages <a class="yt-timestamp" data-t="01:21:25">[01:21:25]</a>.
*   **Human Recognition:** Recognizing specific individuals or people with certain attributes (e.g., "move the Coke can to the person with glasses") <a class="yt-timestamp" data-t="01:21:30">[01:21:30]</a>.
*   **Conceptual Understanding:** Interpreting nuanced instructions like "pick up the bag that's about to fall off the table" <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>, or understanding categories like "land animal" vs. "aquatic animal" <a class="yt-timestamp" data-t="01:43:39">[01:43:39]</a>.
*   **Symbol Understanding and Reasoning:** Distinguishing between different objects, even if unseen in training, and applying basic logical reasoning <a class="yt-timestamp" data-t="01:21:12">[01:21:12]</a>.

Notably, while the model demonstrates strong semantic and visual generalization, its physical skills remain limited to the distribution of motions seen in the robot training data (e.g., predominantly "pick down" actions on a table) <a class="yt-timestamp" data-t="01:29:30">[01:29:30]</a>.

## Future Directions

*   **Acquiring New Skills:** Future work should explore how robots can acquire entirely new physical skills, potentially from videos of humans performing diverse actions <a class="yt-timestamp" data-t="01:29:41">[01:29:41]</a>.
*   **Efficiency:** Addressing the high computational cost and real-time inference bottleneck through techniques like quantization and distillation to enable models to run on lower-cost hardware or at higher frequencies <a class="yt-timestamp" data-t="01:30:39">[01:30:39]</a>.
*   **Cloud Robotics:** Leveraging advancements in internet speed and cloud computing to facilitate real-time inference for robots, where the bulk of the computation is offloaded to the cloud <a class="yt-timestamp" data-t="01:30:57">[01:30:57]</a>.
*   **Open-Source Models:** The paper expresses a hope for more open-source [[large_language_models_in_robotics | large language models in robotics]] and fine-tuning APIs to become available, fostering broader research and development <a class="yt-timestamp" data-t="01:31:30">[01:31:30]</a>.

The authors believe that [[vision_language_models_and_object_manipulation | Vision language models and object manipulation]] are a key to unlocking the future of robotics, leading to general-purpose home robots within the next five to ten years <a class="yt-timestamp" data-t="01:34:50">[01:34:50]</a>.