---
title: Future of Humanoid Robots and LLMs
videoId: 1Gl93N2nhcE
---

From: [[hu-po]] <br/> 

The field of [[robotics_and_automation_advancements | robotics]] has historically faced challenges due to its nature as a chain of different technologies—including hardware, vision sensors, vision algorithms, and control algorithms—with performance limited by the weakest link <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Traditional robotic systems required explicit programming for every action, making it difficult for non-engineers to use them and limiting robots to very specific, repetitive tasks <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. However, [[use_of_large_language_models_in_robotics | large language models]] (LLMs) have emerged as a potential solution to these long-standing [[challenges_and_future_directions_in_robotic_development | challenges in robotic development]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Large Language Models in Robotics

[[Use of Large Language Models in Robotics | Large language models]] introduce a crucial "fuzziness" that allows robots to interpret tasks described in natural language, moving beyond rigid, precise instructions <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This capability enables non-robotics experts to give high-level commands, which the LLM then breaks down into executable steps <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Google's Palm-SayCan

Google Research's "Everyday Robots" group, though recently defunded, developed "Palm-SayCan" as a robotics algorithm that combines the understanding of language models with the capabilities of a helper robot <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This system utilizes Google's Palm LLM, similar to how OpenAI uses GPT and Meta uses Llama <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

The Everyday Robots were mobile manipulators, featuring a Roomba-like base, a tower with a depth sensor (similar to an autonomous vehicle's LiDAR), a pan-tilt-twist head for vision, and a single arm with multiple degrees of freedom and a pincer gripper <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

#### Chain of Thought Prompting

A key technique employed by Palm-SayCan is "Chain of Thought prompting," a method within prompt engineering <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. By adding phrases like "let's think step by step" to a prompt, the LLM is compelled to produce a step-by-step solution to the requested task, leading to a fundamentally different and more useful output for robotics <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

For example, a complex instruction like "I just worked out, can you bring me a drink and a snack to recover?" is split into subtasks such as:
1.  Find water <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>
2.  Pick up the water <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>
3.  Bring it to you <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>
4.  Put down the water <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>
5.  Find an apple <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>
6.  Pick up Apple <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>
7.  Bring it to you <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>
8.  Put down the apple <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>

This breakdown allows the robot to understand and execute tasks that involve both navigation (localization) and manipulation (grasping/placing) <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. The LLM scores the likelihood that each subtask makes progress towards the high-level request <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

#### Affordance Model

An "affordance model" works in conjunction with the LLM to score whether each step is physically possible for the robot within its environment <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. The combined score, considering both relevance from the LLM and possibility from the affordance model, determines the robot's next action <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

## Vision Language Models (VLMs) in Robotics

Another significant advancement comes from the integration of [[application_of_vision_language_models_in_robotics | vision language models]] (VLMs), which are pre-trained on captioned images from the internet and are adept at relating visual information to text descriptions <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

### Open World Object Manipulation (Moo)

The paper "Open World Object Manipulation using Pre-trained Vision Language Models" introduces "Moo" (Manipulation of Open World Objects) <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. Moo leverages pre-trained VLMs to extract object-identifying information from language commands and conditions the robot's policy on the current image, the instruction, and the extracted object information <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

This approach addresses the challenge of robots encountering objects they have never seen firsthand <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. Unlike older paradigms where every object or task had to be explicitly programmed, VLMs enable [[generalization_in_robotics_using_language_models | generalization in robotics using language models]] through fuzzy matching, allowing robots to identify and interact with novel objects <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

#### Zero-Shot Generalization and Input Modalities

Moo demonstrates "zero-shot generalization," meaning it can perform tasks on novel object categories and in new environments without any additional fine-tuning <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. The system utilizes an "open vocabulary object detector" like Owl-ViT (a vision Transformer) to link natural language with visual objects, providing bounding box or keypoint indicators of object locations in the camera space <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

Beyond text, Moo can generalize to other non-language-based input modalities, such as finger pointing at an object or providing a stock image of the target <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. This is particularly useful for objects hard to describe in words or when many visually similar objects are present <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.

The actual robot manipulation policy (the neural network controlling the arm) is trained on human demonstrations, typically through "behavior cloning," where humans control the robot in VR to grab diverse objects <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. The VLM then assists by identifying the specific part of the image the robot needs to grab <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

## Impact of Data and Compute

A fundamental truth in machine learning and AI, including [[embodied_reinforcement_learning_and_llms | embodied reinforcement learning and LLMs]], is that increased performance strongly correlates with larger dataset sizes and model capacity <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. The advancements seen in robotics, particularly with LLMs and VLMs, are a direct result of the increasing availability of data (from the internet, digital cameras, cell phones) and enhanced computing power (GPUs) <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.

In experiments, Moo significantly outperforms previous methods like RT1 in pick percentage for both seen (92% vs. 54%) and unseen objects (75% vs. 25%), demonstrating its robust generalization capabilities even in distracting environments <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>.

## Future Outlook

While past predictions for robots in homes (e.g., ASIMO in 2000) vastly underestimated the complexity of real-world robotics <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>, current advancements suggest a promising future for [[the_potential_future_and_challenges_of_ai_agents | AI agents]] and humanoid robots. The integration of LLMs provides the crucial "missing piece" – the ability for robots to understand natural language and translate it into actionable tasks <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.

With hardware continuously improving (cheaper motors, cameras, laser scanners) and significant breakthroughs in software for understanding human commands, the [[prospects_of_humanoid_robotics_and_reinforcement_learning | prospects of humanoid robotics and reinforcement learning]] are increasingly optimistic. It is plausible that within five to ten years, robots capable of assisting with tasks like fetching items or cleaning up after toddlers could become a reality in homes <a class="yt-timestamp" data-t="00:47:17">[00:47:17]</a>. The ability to talk to a robot in natural language signifies an exciting future for [[robotics_and_automation_advancements | robotics and automation advancements]] <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.