---
title: Application of Vision Language Models in Robotics
videoId: 1Gl93N2nhcE
---

From: [[hu-po]] <br/> 

Large Language Models (LLMs) are being integrated into robotic systems to significantly improve performance <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Historically, robotics has faced challenges due to its nature as a "chain out of different technologies" like hardware, vision sensors, and control algorithms, where performance is limited by the weakest link <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. LLMs offer a potential solution to these real-world robotics problems <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Google's Everyday Robots and Palm-SayCan

Google Research's "Everyday Robots" group, though recently defunded, developed robots designed for daily tasks <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. These robots typically feature a Roomba-like base, a tower with a depth sensor (similar to an autonomous vehicle's Velodyne sensor), a head with pan, tilt, and twist capabilities, and a single arm with a pincer gripper <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

Google utilizes its own language model, Palm (similar to OpenAI's GPT or Meta's Llama), for robotic applications <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Palm-SayCan is a robotics algorithm that combines the understanding of language models with the capabilities of a helper robot <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Chain of Thought Prompting

A key technique used by Palm-SayCan is "Chain of Thought prompting" <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This is a prompt engineering method that enables a large language model to produce an output with specific properties <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. By adding phrases like "let's think step by step" to a prompt, the LLM is compelled to show its work and provide a series of steps to perform a task, yielding a fundamentally different answer <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

Robots traditionally struggled with complex instructions requiring reasoning because they needed explicit, detailed programming down to exact trajectories and positions <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This meant only robotics engineers could use them, and they were constrained to very specific, repetitive jobs <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. [[use_of_large_language_models_in_robotics | Large language models]] introduce a "fuzziness" that allows tasks to be described in natural language <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. Palm-SayCan then splits these high-level natural language commands into subtasks using Chain of Thought reasoning, which the robot can then execute <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

For example, a command like "I just worked out, can you bring me a drink and a snack to recover?" is interpreted by Palm-SayCan, which internally "talks to itself" saying, "The user has asked for a drink and a snack. I will bring a water bottle and an apple" <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. The LLM scores the likelihood that each individual skill makes progress towards completing the high-level request <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Affordance Model

The system incorporates an "affordance model," which scores whether each step is possible for the robot within its environment <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. The LLM assesses the relevance of a proposed action to the original command, and a combined score (relevance + possibility) determines the robot's next action <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

Tasks are broken down into granular robot commands:
*   **Find water:** A localization task (move around until the object is found) <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Pick up the water:** A grasping/manipulation task <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Bring it to you:** A navigation task (moving with the Roomba base) <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Put down the water:** A manipulation task <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## Open World Object Manipulation (MOO)

A significant challenge in robotics is enabling robots to follow instructions involving object categories they have never seen firsthand <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. It's impractical to have robots experience every possible semantic combination, such as "pink stuffed whale" <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

[[vision_language_models_and_their_advancements | Vision Language Models]] (VLMs), like CLIP or BLIP, capture vast semantic information from internet data (e.g., captioned images) <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. They excel at relating visual information (images) with textual descriptions (captions) <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.

The "Manipulation of Open World Objects" (MOO) approach interfaces robotic policies with these pre-trained [[vision_language_models_and_encoders | Vision language models]] <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. This allows robots to complete instructions for object categories they have not seen firsthand <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. MOO demonstrates "zero-shot generalization," meaning it works out of the box without additional fine-tuning for specific tasks <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

### MOO Pipeline

1.  **Instruction from LLM:** A human command (e.g., "move green Sprite can near Blue Plate") is processed by an LLM to generate a precise instruction <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.
2.  **Object Detection with [[vision_language_models_and_encoders | Owl-ViT]]:** An open-vocabulary object detector, [[vision_language_models_and_encoders | Owl-ViT]] (a Vision Transformer), links natural language object descriptions to visual images <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. It takes the robot's camera image and the object names (e.g., "Blue Plate," "green Sprite can") and outputs bounding box indicators or key points for where the objects reside in the camera space <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. [[vision_language_models_and_encoders | Owl-ViT]] is "frozen" (not fine-tuned) for the robot <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.
3.  **Conditioned Robot Policy:** The robot's policy (a neural network that produces actions) is conditioned on the current image, the instruction, and the extracted object information from [[vision_language_models_and_encoders | Owl-ViT]] <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. This policy dictates how the robot moves its hand <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
    *   The policy outputs actions for different modes (navigating or manipulating), base movements (rotation, X, Y), and arm joint angles (seven degrees of freedom) <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.
    *   The robot's manipulation policy itself is trained on human demonstrations (behavior cloning), involving physically controlling the robot to grasp 106 diverse objects <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
    *   Unlike `RT1`, which was brittle with unseen objects due to end-to-end training, MOO's use of a standardized segmentation task representation from [[vision_language_models_and_encoders | Owl-ViT]] simplifies [[generalization_in_robotics_using_language_models | generalization]] <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>.

### Input Modalities

MOO also generalizes to non-language-based input modalities, such as finger pointing <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. Additionally, a generative [[vision_language_models_and_encoders | Vision Language Model]] like Pally or BLIP can generate an image caption from an uploaded image, which is then provided to [[vision_language_models_and_encoders | Owl-ViT]] to generate a mask for MOO <a class="yt-timestamp" data-t="00:41:09">[00:41:09]</a>. Image-based querying is particularly useful when objects are hard to describe in words or when many visually similar objects are present <a class="yt-timestamp" data-t="00:41:43">[00:41:43]</a>.

### Performance

MOO significantly outperforms `RT1` in pick percentage for both seen and unseen objects:
*   **RT1:** 54% (seen), 25% (unseen) <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>
*   **MOO:** 92% (seen), 75% (unseen) <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>

This improved performance is largely attributed to increased data set sizes and model capacity, a fundamental truth in machine learning <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

## [[Challenges and future directions in vision language modeling | Challenges and Future Outlook]]

Despite historical overestimations of robotics capabilities (e.g., ASIMO robot in 2000) <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>, the current advancements, especially with [[use_of_large_language_models_in_robotics | Large Language Models]], suggest a breakthrough <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. The ability to talk to robots in natural language represents a crucial missing piece <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.

Hardware advancements, such as cheaper motors, cameras (from cell phones), and laser scanners (from autonomous vehicles), have also consistently improved the robotic technology stack <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>. The combination of these hardware improvements with the "step function improvement" in language models' ability to understand natural language and translate it into tasks could lead to functional household robots within 5-10 years <a class="yt-timestamp" data-t="00:47:57">[00:47:57]</a>.