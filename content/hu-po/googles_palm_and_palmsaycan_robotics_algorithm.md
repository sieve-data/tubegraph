---
title: Googles Palm and Palmsaycan Robotics Algorithm
videoId: 1Gl93N2nhcE
---

From: [[hu-po]] <br/> 

Large Language Models (LLMs) are being integrated into robotics systems to significantly improve performance, particularly in understanding and executing complex tasks in the real world <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Robotics traditionally struggles with its reliance on a chain of technologies—hardware, vision sensors, vision algorithms, and control algorithms—where performance is limited by the weakest link <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a> <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. LLMs offer a potential solution to these limitations <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Palm-SayCan

Palm-SayCan is a robotics algorithm developed by Google that integrates Google's state-of-the-art LLM, Palm, with the real-world capabilities of a helper robot <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a> <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Palm is Google's equivalent to OpenAI/Microsoft's GPT or Meta/Facebook's Llama <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### The Everyday Robots Platform

The research on Palm-SayCan was conducted by Everyday Robots, a group within Google Research <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Their robots are designed with a Roomba-like base, a tower, a depth sensor (similar to a Velodyne LiDAR sensor on autonomous vehicles), a head with pan-tilt and twist capabilities to choose what to look at, and a single arm with multiple degrees of freedom and a pincer gripper <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. While the Everyday Robots division was largely defunded, the research spirit continues <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> <a class="yt-timestamp" data-t="00:46:32">[00:46:32]</a>.

### How Palm-SayCan Works

Palm-SayCan enables robots to understand complex instructions that require reasoning by splitting prompts into subtasks <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This is achieved through [[chain_of_thought_prompting_in_robotics | Chain of Thought prompting]], a technique in prompt engineering that forces the LLM to "show its work" and provide a set of steps for a given task <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a> <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. For example, adding "let's think step by step" to a prompt changes the LLM's output fundamentally <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a> <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

Historically, programming robots required explicit, precise instructions for every trajectory and position, making it impossible for non-robotics engineers to use them effectively and limiting robots to very specific, repetitive jobs <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a> <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. LLMs introduce "fuzziness," allowing tasks to be described in natural language <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a> <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

#### Task Interpretation and Execution

When given a high-level command like "I just worked out, can you bring me a drink and a snack to recover?" <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, Palm-SayCan interprets it and breaks it down into more precise, executable sub-instructions <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a> <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

The LLM determines the user's intent (e.g., "I will bring a water bottle and an apple") <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. It then uses [[chain_of_thought_prompting_in_robotics | Chain of Thought prompting]] to interpret instructions and score the likelihood that an individual skill will progress towards completing the high-level request <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a> <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

#### The Affordance Model

An "affordance model" evaluates whether each potential step is physically possible for the robot within its environment <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a> <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. The LLM then determines the relevance of that action to the original command <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. A combined score (relevance + possibility) dictates the robot's chosen action <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a> <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

For the "drink and snack" task, the steps generated are:
*   Find water (localization task) <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a> <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>
*   Pick up the water (grasping/manipulation task) <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a> <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>
*   Bring it to you (navigation task) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a> <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>
*   Put down the water (manipulation task) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a> <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>
*   Find an Apple (localization task) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a> <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>
*   Pick up Apple (manipulation task) <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a> <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>
*   Bring it to you (navigation task) <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>
*   Put down the apple (manipulation task) <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a> <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>

## Manipulation of Open World Objects (Moo)

A key challenge in robotics is dealing with an "infinite" amount of objects and scenarios that a robot might encounter, making it impractical to pre-program or give first-hand experience for every possibility <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a> <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. The Moo (Manipulation of Open World Objects) approach addresses this by leveraging pre-trained [[application_of_vision_language_models_in_robotics | Vision Language Models (VLMs)]] <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a> <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

### Role of Vision Language Models

VLMs like CLIP (Contrastive Language-Image Pre-training) and BLIP (Image Captioning Model) are trained on captioned images from the internet <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a> <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. They excel at relating visual information to text descriptions, allowing a robot to identify objects described in natural language, even if it has never seen them firsthand <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a> <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a> <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.

### Moo's Pipeline

Moo interfaces robotic policies with these pre-trained models. The process involves:
1.  **Instruction:** A human gives a command (e.g., "move green Sprite can near Blue Plate") <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a> <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.
2.  **Object Detection (Owl-ViT):** An "open vocabulary object detector" called Owl-ViT (a Vision Transformer) links natural language with objects in a visual image <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a> <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. It takes the robot's camera image and the object descriptions (e.g., "Blue Plate," "green Sprite can") and outputs bounding box indicators (or key points) of where the objects reside <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a> <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>. Owl-ViT is a frozen model, meaning it's not fine-tuned on robot-specific data <a class="yt-timestamp" data-t="00:30:45">[00:30:45]</a> <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.
3.  **Policy Conditioning:** The robot's policy (the neural net that produces actions, trained through reinforcement learning) is conditioned on the current image, recent history, the instruction, and the extracted object information from Owl-ViT <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a> <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a> <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a> <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
4.  **Action Execution:** The policy outputs an action, which includes the mode (e.g., picking or moving), base movement (rotation, X/Y movement), and arm joint movements (for a 7-degree-of-freedom arm) <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a> <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a> <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>.

### [[generalization_in_robotics_using_language_models | Generalization]] and Performance

Moo demonstrates significant [[generalization_in_robotics_using_language_models | zero-shot generalization]] (performing tasks without additional fine-tuning) to novel object categories and environments <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a> <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. While the robot's physical skills (e.g., grasping, navigating) are trained through behavior cloning from human demonstrations on a limited set of objects (e.g., 106 objects for gripping) <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a> <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a> <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>, the VLM's ability to recognize and segment novel objects allows the robot to perform actions on them <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

Compared to earlier systems like RT1, Moo shows substantially better pick percentages for both seen and unseen objects (e.g., 92% vs. 54% for seen, 75% vs. 25% for unseen) <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a> <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a>. RT1 was brittle when faced with unseen objects because its language embeddings struggled to generalize beyond its limited training data <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>. Moo's segmentation mask representation, being identical for both seen and unseen objects, simplifies this [[generalization_in_robotics_using_language_models | generalization]] <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>.

### Input Modalities

Beyond natural language, Moo can also receive object specifications via:
*   **Finger pointing:** A human can directly point at an object <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a> <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Clicking on image:** Users can click on a specific part of the robot's camera image <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Image query:** Providing a stock image of the target object is effective when objects are hard to describe verbally or when many visually similar objects are present <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a> <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>. This often involves using a generative VLM like Pally to create an image caption that Owl-ViT can then use <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a>.

### Training and [[dynamic_scene_handling_in_robotics | Dynamic Scene Handling]]

Moo utilizes data from previous robot systems like RT1, combined with newly added diverse "pick data" covering 90 different object categories <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a> <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. The system can handle randomized distractor objects and
[[dynamic_scene_handling_in_robotics | changes in the environment]] (e.g., if an object is moved), demonstrating robustness in challenging settings <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a> <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.

## Broader Implications and Future Outlook

The success of LLMs in robotics highlights a fundamental truth in AI: [[ai_algorithms_and_computational_constraints | increased performance correlates strongly with larger datasets and greater model capacity]] <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a> <a class="yt-timestamp" data-t="00:37:11">[00:37:11]</a>. Advancements in digital cameras, cell phones, and GPUs have provided the foundational technologies for vast amounts of data and increased compute, fueling progress across deep learning <a class="yt-timestamp" data-t="00:38:06">[00:38:06]</a> <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>.

While early predictions for home robots were drastically underestimated (e.g., ASIMO in 2000) <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a> <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>, the current wave of [[robotics_and_automation_advancements | robotics and automation advancements]], particularly with the integration of LLMs for high-level instruction interpretation, suggests that robots capable of assisting in homes within five to ten years may be plausible <a class="yt-timestamp" data-t="00:47:17">[00:47:17]</a> <a class="yt-timestamp" data-t="00:48:28">[00:48:28]</a>. The combination of cheaper hardware components (motors, cameras, laser scanners) and the breakthrough in language understanding provides a missing piece for developing general-purpose robots that can take natural language commands <a class="yt-timestamp" data-t="00:47:24">[00:47:24]</a> <a class="yt-timestamp" data-t="00:48:01">[00:48:01]</a>.