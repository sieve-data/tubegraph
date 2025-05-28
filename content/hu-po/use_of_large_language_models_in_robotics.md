---
title: Use of Large Language Models in Robotics
videoId: 1Gl93N2nhcE
---

From: [[hu-po]] <br/> 

[[large_language_models_in_machine_learning_research | Large language models]] (LLMs) are being integrated into robotics systems to achieve significantly improved performance, addressing long-standing challenges in the field <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Historically, robotics has faced limitations due to being a "chain of technologies," where overall performance is constrained by the weakest link among hardware, vision sensors, vision algorithms, and control algorithms <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. LLMs offer a potential solution to these problems, particularly in enabling robots to operate effectively in real-world scenarios <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Everyday Robots and PaLM-SayCan

Google Research's "Everyday Robots" group developed robots designed for assistive tasks <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. These robots typically feature a Roomba-like base with a tall tower, a depth sensor (similar to those on autonomous vehicles), a pan-tilt head for visual focus, and a single arm with a pincer gripper <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

Google's [[llm_large_language_models_development | language model]], PaLM (Pathways Language Model), is utilized in a robotics algorithm called PaLM-SayCan <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. PaLM-SayCan combines the understanding capabilities of [[large_language_models_in_machine_learning_research | language models]] with the real-world capabilities of a helper robot <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Chain of Thought Prompting

A key technique employed by PaLM-SayCan is "Chain of Thought prompting" <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This is a method within prompt engineering that structures a prompt to guide the [[large_language_models_in_machine_learning_research | large language model]] to produce a step-by-step solution <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. For instance, adding "let's think step by step" to a prompt forces the LLM to show its work and provide a sequence of actions <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This approach generates a fundamentally different and more useful output for robotic tasks <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

Traditionally, programming robots involved explicitly describing every movement, trajectory, and force in code, making it difficult for non-robotics engineers to use them and limiting them to highly specific, repetitive tasks <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. [[large_language_models_in_machine_learning_research | Large language models]] introduce "fuzziness," allowing tasks to be described in natural language <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. PaLM-SayCan leverages this by taking a high-level human command, like "I just worked out, can you bring me a drink and a snack to recover?" <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, and splitting it into executable subtasks through Chain of Thought reasoning <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

### Affordance Model

The [[large_language_models_in_machine_learning_research | large language model]] (acting as the robot's internal monologue) scores the likelihood of individual skills progressing towards completing the high-level request <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. An "affordance model" evaluates whether each potential step is physically possible for the robot within its environment <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. The combined score, considering both relevance (from the LLM) and possibility (from the affordance model), determines the robot's next action <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

Example breakdown for "bring me a drink and a snack":
*   **Find water**: Localization task <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Pick up the water**: Grasping/manipulation task <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Bring it to you**: Movement/localization task <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Put down the water**: Manipulation task <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

The robot alternates between movement and manipulation tasks based on these decomposed instructions <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

## Open-World Object Manipulation (Moo)

Another significant advancement is "Manipulation of Open World Objects" (Moo), which focuses on enabling robots to follow instructions involving object categories they have never seen firsthand <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. This addresses the impracticality of having robots gain first-hand experience with every conceivable object <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

### Role of Vision Language Models

Moo leverages pre-trained [[multimodal_large_language_models_vs_vision_language_models | Vision Language Models]] (VLMs) like CLIP or BLIP <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. These models, trained on captioned images from the internet, are highly effective at relating visual input with semantic captions <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. For example, they can associate the word "fish" with the visual representation of a fish in an image <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. This allows a robot to "pick up the fish" even if it doesn't understand "fish" as a concept, but rather as a segmented part of its point cloud identified by the VLM <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

### Moo's Approach and [[generalization_in_robotics_using_language_models | Generalization]]

Moo interfaces robotic policies with these pre-trained VLMs <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. It extracts object-identifying information from language commands and conditions the robot's policy on the current image, instruction, and extracted object information <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. This enables "zero-shot [[generalization_in_robotics_using_language_models | generalization]]," meaning the robot can perform tasks with novel objects without additional fine-tuning <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

Moo uses an open-vocabulary object detector called Owl-ViT (Owl Vision Transformer) <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>. This Vision Transformer takes an image (split into patches like word tokens) and a text description to output a bounding box or key points indicating where the object resides in the RGB camera space <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

The robot's manipulation policy (the neural network dictating its actions) is trained on human demonstrations (behavior cloning) <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. Unlike end-to-end training where the entire system is trained from raw input to action, Moo conditions the manipulation policy on the output detections from the Owl-ViT <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>. The Owl-ViT itself is frozen (not fine-tuned for robotics) <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>. This modular approach allows the robot to adapt to unseen objects because the segmentation task representation generated by the VLM is consistent for both seen and novel objects <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>.

### Performance and [[large_language_models_llms_and_scaling | Scaling]]

Moo significantly outperforms previous systems like RT1 in picking objects, especially unseen ones. For seen objects, RT1 achieved a 54% pick rate, while Moo achieved 92%. For unseen objects, RT1 managed 25%, whereas Moo reached 75% <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>.

This increased performance is strongly correlated with larger dataset sizes and model capacity, a principle consistent across much of deep learning and AI <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. The availability of increased compute and increased data are fundamental drivers of progress in this field <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.

## Future Outlook

While robots are not yet common in homes, advancements like these suggest they could be within five to ten years <a class="yt-timestamp" data-t="00:47:17">[00:47:17]</a>. Hardware improvements, driven by industries like car manufacturing (motors), cell phones (cameras), and autonomous vehicles (laser scanners), have continually enhanced the robot technology stack <a class="yt-timestamp" data-t="00:47:26">[00:47:26]</a>. The significant leap in [[large_language_models_in_machine_learning_research | language models']] ability to understand natural language and convert it into a sequence of executable tasks for robots is seen as the "big missing piece" that is now in place <a class="yt-timestamp" data-t="00:48:09">[00:48:09]</a>. This capability could lead to robots that can assist with household tasks, such as grabbing items or cleaning <a class="yt-timestamp" data-t="00:48:38">[00:48:38]</a>.