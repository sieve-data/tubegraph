---
title: Role of large language models in robotics and selfdriving technology
videoId: Ctuf2Y0MrcA
---

From: [[redpointai]] <br/> 

The integration of [[understanding_language_models | large language models (LLMs)]] and vision models (VLM) is profoundly transforming the landscape of autonomous vehicles and robotics. These advanced models are not merely incremental improvements but are fundamentally reshaping how self-driving cars perceive and interact with the world, and how robots learn and generalize tasks <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## LLMs in Self-Driving: The Waymo Experience

Waymo, a pioneer in self-driving technology, has leveraged LLMs and VLM advancements without discarding their existing frameworks <a class="yt-timestamp" data-t="01:40">[01:40]</a>. The [[building_and_utilizing_large_language_models | foundation model revolution]] allows Waymo to build "teacher models" – large-scale models run in the cloud that ingest vast amounts of driving data and internet data <a class="yt-timestamp" data-t="01:48">[01:48]</a>. This "teacher" then trains and distills data into the onboard models of the autonomous car, providing a more informed mode of supervision <a class="yt-timestamp" data-t="02:22">[02:22]</a>.

### Key Manifestations and Benefits
*   **World Knowledge:** LLMs and VLMs introduce "World Knowledge," which is the semantic understanding of the environment <a class="yt-timestamp" data-t="03:14">[03:14]</a>. This allows the autonomous driver to recognize unfamiliar objects like different regional police cars or accident scenes, even if the car hasn't experienced them directly in its training data <a class="yt-timestamp" data-t="03:46">[03:46]</a>. This knowledge is derived from pre-training on extensive visual and text data from the web <a class="yt-timestamp" data-t="04:20">[04:20]</a>.
*   **Enhanced Reasoning:** The pre-training on diverse data significantly enhances the models' reasoning capabilities <a class="yt-timestamp" data-t="04:51">[04:51]</a>. Larger models are generally considered better, scaling up the ability to process and understand complex scenarios <a class="yt-timestamp" data-t="05:00">[05:00]</a>.

### Limitations and Safety
While LLMs offer significant advantages, they are not a complete solution for all aspects of self-driving <a class="yt-timestamp" data-t="05:11">[05:11]</a>.
*   **Safety and Regulatory Constraints:** Aspects related to strict safety contracts and regulatory constraints must be expressed explicitly, outside of the AI model <a class="yt-timestamp" data-t="05:37">[05:37]</a>. This external layer verifies that the AI-proposed driving plan meets all safety and compliance requirements, ensuring reasonable behavior at all times <a class="yt-timestamp" data-t="05:59">[05:59]</a>. This "checking layer" or "guard rails" around the reasoning models' output is crucial <a class="yt-timestamp" data-t="06:35">[06:35]</a>.

### Sensor Suite Strategy
Waymo uses a complementary suite of cameras, lidars, and radars <a class="yt-timestamp" data-t="02:30:57">[02:30:57]</a>. Each sensor type has unique strengths and weaknesses that complement each other, providing diversity for cross-validation <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.
*   Waymo's historical decision to "over-sensorize" was based on solving the harder L4 (fully autonomous) problem first <a class="yt-timestamp" data-t="02:41:50">[02:41:50]</a>. This approach generates the necessary data to inform decisions on cost reduction and simplification for future generations of cars <a class="yt-timestamp" data-t="02:48:07">[02:48:07]</a>.
*   **Redundancy:** The need for redundancy in sensors is unlikely to disappear, as different sensors provide diverse and complementary information for safety <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **Superhuman Performance:** The bar for L4 driving is considered "above human level" <a class="yt-timestamp" data-t="03:00:27">[03:00:27]</a>. Waymo's safety reports indicate they are safer than the average human driver, with fewer collisions and reported injuries <a class="yt-timestamp" data-t="03:05:02">[03:05:02]</a>.

### Scaling and Milestones
The main challenges for self-driving today revolve around scaling and addressing the "long tail" of rare, exceptional, and difficult problems <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>. As autonomous vehicles drive millions of miles, events that might occur once in a human's lifetime become common occurrences <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.
*   **Simulation:** Waymo heavily utilizes [[advancements_in_simulation_and_world_modeling_for_autonomous_technology | simulation]] and synthetic scenarios to validate models against potential problems that may not have been observed in the real world <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. They also modify real-world scenarios to make them more challenging (e.g., adversarial drivers) to improve the car's reactivity <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
*   **Future Milestones:** The next major milestones in autonomous vehicles will be centered on geographic expansion, such as Waymo's first international experiment driving on the left side of the road in Tokyo <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Advancements in [[advancements_in_simulation_and_world_modeling_for_autonomous_technology | Simulation and World Modeling]]
A significant technical advance that could change the landscape of autonomous driving is the development of reliable, physically realistic world models <a class="yt-timestamp" data-t="01:14:15">[01:14:15]</a>.
*   **Video Prediction Models:** Early "proto-world models" include video prediction models like Sora or Veo, which can unroll an image or scene into a plausible future <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   **Controllable and Physically Realistic Models:** The challenge is to make these models controllable and physically realistic, creating a "digital twin" of the world for autonomous driving <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **Causality:** A deep question at the heart of these world models is causality <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. While current models can generate plausible videos by learning correlations, understanding and injecting causality (how an input changes an output) is crucial for functional, controllable models <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This may come from proper data engineering and inductive biases rather than new architectures <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

## LLMs and General Robotics

An autonomous car is fundamentally a robot, sharing core problems of perception, planning, and actuation <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. However, general robotics is still "chasing the nominal use case" – how to get a generalized robot to perform any desired task <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

### Impact of LLMs on Robotics
The surprising breakthrough with LLMs in robotics is the rapid transition from a chatbot describing how to make coffee to an actionable plan for a robot <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.
*   **Common Sense Knowledge:** LLMs provide robots with common sense knowledge that was previously difficult to embed, such as knowing a cup belongs on a table, not the floor, or that a microwave is in the kitchen <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. This everyday knowledge, previously inaccessible, was brought together by LLMs <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
*   **Action as Language:** The realization that robot actions can be viewed as a "different language" (body actions instead of words) allows robotics to leverage the machinery of multimodal and multilingual [[building_and_utilizing_large_language_models | large language models]] <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

### Generalization and Specialization
The future of robotics models will likely involve both generalized and specialized approaches <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.
*   **Generalized Teacher Models:** The goal is to build a generalized "teacher" or backbone model that can be easily retargeted and optimized for single tasks <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. This is analogous to instruction tuning in LLMs, where generic capabilities are developed and then adapted via prompting or fine-tuning for specific tasks <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

### Hardware vs. Software Approaches
Two main approaches exist for [[prospects_and_challenges_in_robotics_and_ai_integration | building generalized robot models]]:
*   **Hardware-Centric:** Building the most capable humanoid robot first, then expecting it to accomplish tasks <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.
*   **Software-First:** Building general intelligence and trusting it can be retargeted to new platforms relatively easily <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.
    *   The "software-first" path, as demonstrated by work like RTX, is favored for faster progress due to the current bottleneck of data acquisition <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. Relying on expensive, wobbly robots for data collection is a significant challenge to scalability <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

### Simulation vs. Real-World Data
The debate between using simulation and teleoperated real-world data remains <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   **Locomotion and Navigation:** Simulation has been effective here, with the sim-to-real gap being manageable <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   **Manipulation:** Simulation struggles for manipulation due to the difficulty in replicating the diversity of experience, contact quality, and realistic physics <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. Scaling up physical operations to collect real-world data has proven to be a faster path for manipulation <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.

### Data Acquisition Bottlenecks and Solutions
*   **Human-Robot Interaction (HRI):** The HRI field needs to focus more on data acquisition strategies <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. Different methods include kinesthetic teaching, puppeteering, and teleoperation <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Third-Party Imitation:** Learning by observing videos of people performing tasks (third-party imitation) is a promising but currently unsolved area, requiring the ability to infer causality from observation <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
*   **Multimodal Models:** The transfer of visual information from large multimodal models to robots significantly accelerates data acquisition <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>. For example, a robot can understand "Taylor Swift" without explicit training data, because that knowledge is embedded in the larger model <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.

### Unanswered Questions and Future Directions
*   **Generalizing Motion:** A key question is whether robots can generalize motion and actions in the same way they generalize perception <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.
*   **Robotics as Another AI Language:** The hypothesis that robotics is "just another language of AI" appears to hold, with techniques like diffusion models from video generation proving effective for motion generation in robotics <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   **Scaling Laws:** [[building_and_utilizing_large_language_models | Scaling laws]] observed in [[use_and_evaluation_of_large_language_models_llms | large language models]] also apply to autonomous driving models, showing similar log-linear growth with data and size, suggesting that further scaling may continue to yield performance gains <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

## Broader Implications of AI Progress

The advancements in AI, particularly with LLMs, are poised to have a profound impact beyond autonomous systems.

*   **Impact on Education:** AI tools like Chat GPT are often discussed in the context of cheating, but their true potential lies in transforming education as interactive, engaging, and personalized learning tools <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **AI in Daily Life:** AI's application extends to seemingly unconventional areas, such as using AI techniques to design new products like plant-based cheese, which can have a massive impact on sustainability and daily life <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.
*   **Generalized Applicability:** The problem space of "hard to generate for, but easy to verify" is broad, allowing LLMs to be highly effective in diverse applications beyond coding and math <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. This generative-discriminative paradigm (actor-critic model) is applicable to many fields <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
*   **Reasoning and Reinforcement Learning (RL):** Anything multi-step that requires credit attribution can benefit from enhanced reasoning capabilities <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. The current paradigm suggests bootstrapping with a large model via supervised learning, then using RL for fine-tuning to achieve expert-level reasoning <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.