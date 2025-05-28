---
title: Chain of Thought Prompting in Robotics
videoId: 1Gl93N2nhcE
---

From: [[hu-po]] <br/> 

[[robotics_and_automation_advancements | Robotics]] has traditionally faced challenges in real-world application due to the complexity of programming a chain of different technologies, including hardware, vision sensors, vision algorithms, and control algorithms, where performance is limited by the weakest link <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. Large language models (LLMs) have emerged as a potential solution to these problems, improving overall performance in robotic systems <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

## How LLMs Address Robotic Challenges

Traditionally, programming a robot required explicit, precise instructions for every movement and action, such as exact trajectories and positions <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. This meant that only [[challenges_in_endtoend_robotic_learning | robotics engineers]] could effectively use robots, and any change in task required extensive reprogramming, limiting robots to very specific, repetitive jobs <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.

LLMs introduce a "fuzziness" that allows for tasks to be described in natural language, enabling non-experts to give high-level instructions to robots <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. This represents a significant advancement, as LLMs can convert these high-level human commands into a set of precise, executable instructions for the robot <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.

## Palm-SayCan: Google's Approach

Google's research project, Palm-SayCan (combining their Palm LLM with a helper robot), utilizes [[chain_of_thought_in_ai_models | Chain of Thought prompting]] to enable robots to perform complex tasks <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.

### Robot Hardware
The robots used by Google's Everyday Robots (a group that has since been largely defunded <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>) consisted of:
*   A Roomba-like base <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.
*   A depth sensor (similar to a Velodyne LiDAR sensor) mounted under the robot's "chin" for depth perception <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   A head with pan, tilt, and twist capabilities, allowing the robot to choose what to look at <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   A single arm with multiple degrees of freedom and a pincer gripper <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

### Chain of Thought Prompting in Action
[[chain_of_thought_in_ai_models | Chain of Thought prompting]] is a prompt engineering technique that forces an LLM to "show its work" by providing a set of steps to perform a requested task <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. A simple example is adding "let's think step by step" to a prompt <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. This technique yields a fundamentally different and often better answer from the LLM <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.

When a human gives a complex command like "I just worked out, can you bring me a drink and a snack to recover?" <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>, Palm-SayCan interprets this <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a> using [[chain_of_thought_reasoning_in_ai | Chain of Thought reasoning]] to split the prompt into manageable subtasks <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>:
1.  Find water (localization task) <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.
2.  Pick up the water (grasping/manipulation task) <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.
3.  Bring it to you (navigation task) <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.
4.  Put down the water (manipulation task) <a class="yt-timestamp" data-t="12:49:00">[12:49:00]</a>.
5.  Find an Apple <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.
6.  Pick up Apple <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.
7.  Bring it to you <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.
8.  Put down the apple <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.

### Affordance Model
Palm-SayCan incorporates an "affordance model" that scores the possibility of each step for the robot within its environment <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>. This model, likely a neural network, determines if an action (e.g., "find water") is feasible <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>. The LLM then scores the relevance of the action to the original command, and a combined score guides the robot's actions, ensuring both relevance and possibility <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.

## Manipulation of Open World Objects (MOO)

Another significant development is "Manipulation of Open World Objects" (MOO), which focuses on [[robotic_control_and_semantic_reasoning | allowing robots to handle objects they have never seen before]] <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. This addresses the impracticality of robots having first-hand experience with every possible object <a class="yt-timestamp" data-t="14:34:00">[14:34:00]</a>.

### Leveraging Vision-Language Models
MOO uses pre-trained vision-language models (VLMs) like Clip or Blip, which have been trained on captioned images from the internet <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>. These VLMs are adept at relating visual images to textual captions, allowing them to identify objects in an image based on descriptions <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>.

MOO works by:
1.  Extracting object-identifying information from a natural language command using a VLM like Owl-ViT (an open vocabulary object detector) <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>.
2.  Conditioning the robot's policy (the neural network controlling its actions) on the current image, the instruction, and the extracted object information <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>. This allows the robot to "grab this part of the image" identified by the VLM <a class="yt-timestamp" data-t="19:59:00">[19:59:00]</a>.

### Comparison to End-to-End Learning (RT1)
Earlier systems, such as RT1, were often trained end-to-end via [[challenges_in_endtoend_robotic_learning | behavior cloning]] from human demonstrations <a class="yt-timestamp" data-t="28:31:00">[28:31:00]</a>. This meant the entire system, from input (human command, image) to output (robot action), was trained as one unit <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>. However, RT1 was brittle when faced with previously unseen objects because it relied on novel language embeddings <a class="yt-timestamp" data-t="28:03:00">[28:03:00]</a>.

MOO, in contrast, uses a frozen VLM (like Owl-ViT) which is not fine-tuned for the robot but provides consistent object detection <a class="yt-timestamp" data-t="30:45:00">[30:45:00]</a>. The manipulation policy is conditioned on these VLM detections, making generalization to unseen objects simpler <a class="yt-timestamp" data-t="28:19:00">[28:19:00]</a>. MOO demonstrates significantly better performance on both seen (92% vs. 54% for RT1) and unseen objects (75% vs. 25% for RT1) <a class="yt-timestamp" data-t="39:31:00">[39:31:00]</a>.

### Input Modalities
MOO can generalize to other non-language-based input modalities for specifying objects of interest, such as:
*   **Finger pointing**: Allowing a human to simply point at an object <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>.
*   **Clicking on an image**: Selecting a specific part of the image <a class="yt-timestamp" data-t="22:01:00">[22:01:00]</a>.
*   **Image-based querying**: Providing a stock image of the target object, especially useful when objects are hard to describe in words or when many similar objects are present <a class="yt-timestamp" data-t="41:37:00">[41:37:00]</a>.

### Data and Model Capacity
A strong correlation has been established between increased performance and larger data set sizes and model capacity in machine learning and AI <a class="yt-timestamp" data-t="37:04:00">[37:04:00]</a>. This foundational principle, driven by advancements in the internet, digital cameras, cell phones, and GPUs, contributes significantly to the progress in areas like [[dynamic_scene_handling_in_robotics | robotic manipulation]] <a class="yt-timestamp" data-t="38:06:00">[38:06:00]</a>.

## Future Outlook

While past predictions about robots in every home (e.g., ASIMO in 2000 <a class="yt-timestamp" data-t="20:45:00">[20:45:00]</a>) vastly underestimated the complexity of real-world robotics, the emergence of LLMs and their ability to interpret natural language for robot control is a crucial missing piece <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a>.

With hardware continuously improving (cheaper motors, cameras, laser scanners) due to advancements in various industries, and the new ability of LLMs to convert human commands into executable tasks, the future of [[challenges_and_future_directions_in_robotic_development | robotics]] seems promising <a class="yt-timestamp" data-t="47:24:00">[47:24:00]</a>. Although robots may not be in every home within a year, the speaker optimistically suggests their widespread presence in five to ten years <a class="yt-timestamp" data-t="47:11:00">[47:11:00]</a>.