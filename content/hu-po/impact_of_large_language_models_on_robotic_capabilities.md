---
title: Impact of Large Language Models on Robotic Capabilities
videoId: Utv0XpXUGQE
---

From: [[hu-po]] <br/> 

The RT-2 (Robotic Transformer number two) model, developed by Google DeepMind, represents a significant advancement in [[large_language_models_in_robotics | robotic capabilities]] by creating a vision-language-action model <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This model integrates language (text), vision (images), and robot actions into a single framework <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## RT-2: A Vision-Language-Action Model

RT-2 is designed as an end-to-end system for robotic control <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This means it processes raw sensor inputs, like images, directly to generate control commands for the robot's joints <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The goal is to enable a single, end-to-end trained model to map robot observations (images, joint states, sensor data) to actions (position or velocity control signals) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Integration of Large Language Models

A core innovation in RT-2 is representing robot actions as text tokens <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. These action tokens are incorporated directly into the model's training set in the same way as natural language tokens <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This allows the model to leverage large-scale pre-training on web data, including language and vision-language datasets <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

The process involves "co-fine-tuning" state-of-the-art vision-language models, such as Google's Pali-X and PaLM-E, on both robotic trajectory data and internet-scale vision-language tasks like visual question answering (VQA) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a> <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>. This co-fine-tuning method prevents catastrophic forgetting by balancing the ratios of robot and web data in each training batch <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>. To integrate action tokens, RT-2 overwrites the 256 least frequently used tokens in the VLM's existing vocabulary <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>.

When the model is prompted for a robot action, its output vocabulary is constrained to only valid action tokens <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>. The action space is discretized into 256 bins for each dimension (e.g., X, Y, Z translations, three rotational axes, and gripper state), plus a command for terminating the episode <a class="yt-timestamp" data-t="00:46:57">[00:46:57]</a> <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.

### Emergent Capabilities and Generalization

RT-2 exhibits remarkable emergent capabilities and improved generalization due to its internet-scale training <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. It shows significantly improved generalization to novel objects, the ability to interpret commands not present in robot training data, and rudimentary semantic reasoning <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. Examples include picking up the smallest/largest object or one closest to another object <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, or understanding nuanced commands like "move the banana on top of the flag of Germany" <a class="yt-timestamp" data-t="00:30:39">[00:30:39]</a>.

Furthermore, by incorporating Chain of Thought reasoning, RT-2 can perform multi-stage semantic reasoning, such as determining which object to pick up as a hammer or which drink is best for someone tired <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This involves providing an additional "plan" step in the prompt, allowing the model to internally reason in natural language before generating actions <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

While RT-2 generalizes well in semantic and visual understanding, its physical skills (robot motions) are still limited to the distribution of skills seen in the robot training data <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a> <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>. For instance, if trained only on downward picking motions, it cannot unscrew a light bulb from a ceiling <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.

### Challenges and Solutions for Real-time Inference

A significant challenge for [[large_language_models_in_robotics | large language models in robotics]] is their size and the [[efficiency_of_large_language_models | inference speed]] required for real-time control <a class="yt-timestamp" data-t="01:00:39">[01:00:39]</a> <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. The largest RT-2 model evaluated has 55 billion parameters, making it infeasible to run directly on standard robot GPUs <a class="yt-timestamp" data-t="01:00:43">[01:00:43]</a>.

To overcome this, Google DeepMind deployed RT-2 models as a "cloud service" on multi-TPU (Tensor Processing Unit) clusters <a class="yt-timestamp" data-t="01:02:18">[01:02:18]</a>. The robot queries this cloud service over the network <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. The 55 billion parameter model can run at 1-3 Hertz (1-3 times per second), while a smaller 5 billion parameter version runs at around 5 Hertz <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>. The relatively small difference in frequency despite a 10x difference in parameter size suggests that network latency and communication overhead remain bottlenecks <a class="yt-timestamp" data-t="01:06:07">[01:06:07]</a>.

## Comparison with Prior Robotic Systems

The trend towards single, end-to-end trained models like RT-2 contrasts sharply with traditional modular robotics approaches, such as ROS (Robot Operating System) <a class="yt-timestamp" data-t="01:12:21">[01:12:21]</a>. ROS-based systems often involve dozens of separate modules (e.g., vision, control) communicating with each other <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>. While modularity aimed to simplify debugging, it often led to complex issues like race conditions and stale information <a class="yt-timestamp" data-t="01:15:33">[01:15:33]</a>.

RT-2's end-to-end approach eliminates the need for complex, hand-crafted control modules and removes requirements like camera calibration, making robots potentially more robust and easier to deploy in varied environments like homes <a class="yt-timestamp" data-t="01:18:42">[01:18:42]</a> <a class="yt-timestamp" data-t="01:19:49">[01:19:49]</a>. Prior works in [[integration_of_vision_language_models_in_robotics | VLM integration in robotics]] often addressed only higher-level planning, relying on separate low-level controllers that didn't benefit from semantic knowledge <a class="yt-timestamp" data-t="01:18:41">[01:18:41]</a>. RT-2 aims to bring that rich semantic knowledge directly into low-level control <a class="yt-timestamp" data-t="01:19:28">[01:19:28]</a>.

## Future Outlook

The success of RT-2 highlights the potential of [[large_language_models_and_their_applications | large language models and their applications]] to revolutionize robotics. The development of "generalist robots" capable of handling diverse tasks is considered the "Holy Grail" <a class="yt-timestamp" data-t="01:16:05">[01:16:05]</a>.

Current [[challenges_and_approaches_in_adapting_large_language_models_for_specific_tasks | challenges and strategies for training large-scale vision-language models]] include:
*   **Acquiring new physical skills**: Future work should focus on training data that enables new robotic motions, such as videos of humans performing varied actions <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a> <a class="yt-timestamp" data-t="01:29:47">[01:29:47]</a>.
*   **Computational costs**: Further exploration of quantization and distillation techniques is needed to enable models to run at higher rates or on lower-cost hardware, or faster internet speeds to support cloud robotics <a class="yt-timestamp" data-t="01:30:39">[01:30:39]</a>.

The speaker expresses a "spicy take" that autonomous home robots might become widespread before fully autonomous vehicles, as home robots face fewer safety regulations and can more easily adopt end-to-end LLM-driven systems <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>. The belief is that home robots will "leapfrog" the modular development typical of autonomous vehicles <a class="yt-timestamp" data-t="01:41:17">[01:41:17]</a>.