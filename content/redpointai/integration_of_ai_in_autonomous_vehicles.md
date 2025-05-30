---
title: Integration of AI in autonomous vehicles
videoId: Ctuf2Y0MrcA
---

From: [[redpointai]] <br/> 

Vincent Vanhoucke, a distinguished engineer at Waymo, discusses the evolving landscape of [[integration_of_ai_in_autonomous_vehicles | autonomous vehicles]] and [[prospects_and_challenges_in_robotics_and_ai_integration | robotics]] with the integration of AI, particularly large language models (LLMs) and visual models (VMS) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Impact of LLMs and VMS on Autonomous Vehicles

The recent advancements in foundation models, including LLMs and VMS, have influenced Waymo's technology without necessitating a complete overhaul of existing systems <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This "foundation model revolution" allows for the creation of very large-scale "teacher models" that can incorporate all available driving data, in addition to internet data <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This teacher model is then used to train and distill data into the onboard models of the car <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This approach allows for a different mode of supervision for existing models, and provides the foundation for evolving towards bigger, higher-capacity, and more expressive models <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

The primary contribution of LLMs and VMS to autonomous driving is "World Knowledge" – the semantic understanding of the world <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This includes recognizing elements like police cars or emergency vehicles, even in new cities where they might look different <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. These models also understand accident scenes, leveraging vast web data to provide semantic context that might not be present in Waymo's direct driving data <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This extensive pre-training on visual and text data enhances the reasoning capabilities of the autonomous driver <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

While AI models are central, there are aspects of self-driving that require explicit, external control, particularly concerning safety and regulatory compliance <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. A "checking layer" or "guard rails" ensures that the AI's proposed driving plan meets strict requirements for safety and general good behavior <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This allows the system to leverage AI's power for strategy while maintaining verifiable safety standards <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Transition to Waymo and Robotics Parallels

Vanhoucke's personal experience with Waymo's product after an accident highlighted its "magical" and universally applicable nature, influencing his decision to join the company <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

He identifies the core problem of autonomous driving as similar to [[prospects_and_challenges_in_robotics_and_ai_integration | robotics]]: perception, planning, and actuation <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. An autonomous car is essentially a robot with sensors (cameras) as input and actuation (steering, acceleration) as output <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. The main difference lies in the operational domain <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. While [[prospects_and_challenges_in_roobtics_and_ai_integration | robotics]] research often chases nominal behavior (e.g., getting a robot to perform a task), autonomous driving has reached a commercial product level where the challenge is primarily about scaling <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

## Current State and Challenges in Autonomous Vehicles

Currently, there are few "big blockers" for autonomous vehicles <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. While Waymo currently avoids driving in snow, it's more due to a lack of current focus rather than an insurmountable technological hurdle <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Most problems like fog or highway driving have been addressed over time <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. The major [[challenges_in_achieving_full_autonomy_in_selfdriving_cars | challenges in achieving full autonomy in self-driving cars]] now revolve around scaling, specifically addressing the "long tail of problems" that arise when driving millions of miles <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Rare human driving experiences become common occurrences for a large fleet of autonomous vehicles, demanding solutions for these exceptional and difficult scenarios <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

To solve these long tail problems, Waymo heavily utilizes simulation and synthesizes scenarios that correspond to potential issues, even if they haven't been observed in the real world <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. They also modify existing risky scenarios to make them worse, such as introducing drunk or adversarial drivers, to make the car more reactive and understand worst-case scenarios <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### Future Technical Advances and Research

A significant technical advance that could transform the landscape for [[integration_of_ai_in_autonomous_vehicles | autonomous driving]] is the development of reliable, physically realistic World models <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. These models would enable simulating the real world with precise physical realism and accurate scene rendering <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Current video prediction models like Sora or Veo are "proto-World models" that can unroll plausible futures <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. The key is making these models controllable, physically realistic, rich, and plausible in terms of visuals and behavior <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. A "digital twin of the world" for autonomous driving could be a game-changer <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

The main factor hindering World model development is injecting causality <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. While models can learn correlations for plausible videos, control requires understanding how actions lead to outcomes <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This challenge of injecting causality into machine learning models has been a long-standing struggle <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

Waymo's research strategy involves a trade-off between pushing the state-of-the-art internally and leveraging external research <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>. For bespoke problems unique to AVs, Waymo steers the conversation, for example, by releasing the Waymo Open Datasets, which are standard for AV research <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. As Waymo is at the forefront of AV AI, they often have to build the next thing themselves rather than relying on the broader community <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

When entering a new city, Waymo's models are remarkably robust and portable <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. The primary effort is focused on extensive evaluation to ensure the models are robust to local variations (e.g., different emergency vehicle designs) and to convince regulators and the community of their thoroughness <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>. Logistics and building trust with the local community are also crucial <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.

### Sensor Suites and the Superhuman Bar

Waymo's autonomous cars use a complementary sensor suite of cameras, lidars, and radars <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. The diversity of these sensors provides cross-verification, allowing the system to identify and investigate disagreements between different sensor inputs <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

Historically, AV companies have pursued two approaches: starting with Level 2 driving assistance systems with economic constraints on sensor costs, or starting with a highly sensorized approach to solve the hardest problem first <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>. Waymo chose the latter, prioritizing solving the complex problem with abundant sensor data, which now provides the data to inform cost reduction and simplification efforts <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.

The sensor story is also about redundancy, which is unlikely to disappear <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>. While humans can drive with just eyes, the bar for Level 4 (L4) autonomous driving is *above* human level <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>. Waymo's safety reports indicate they are already safer than the average human driver, with fewer collisions and injuries <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>. This "superhuman" performance is seen as a business requirement for successful L4 driving <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>.

> [!info] Superhuman Performance
> The speaker notes a viral video of a Waymo car avoiding an incident with a falling scooter, highlighting the "superhuman" displays of Waymo driving <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. Once society observes such capabilities, it becomes difficult to accept a lower, human-level standard <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>.

## Milestones and Future Outlook

A significant historical milestone is the 1995 transcontinental autonomous ride, which achieved over 99% autonomy, leading to premature assumptions that full self-driving was imminent <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>. It took 30 years to reach commercial deployment, highlighting the difficulty in predicting timelines <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>.

Current milestones for autonomous vehicles include technological validation in cities like Phoenix and San Francisco, and strong user validation, where people "love" the product <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>. The main focus moving forward is on scaling and expansion into various geographies, such as the initial international experiment of data collection in Tokyo, which involves driving on the left side of the road <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>.

## Broader Robotics Space and AI Integration

In the broader [[prospects_and_challenges_in_robotics_and_ai_integration | robotics]] space, the challenge remains getting a generalized robot to perform any desired task <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>. While progress has been rapid, a "convincing generalist system" has not yet emerged <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. One key question is the ability to generalize motion and skills, as many robot demos are specialized for single tasks, even if randomized in environment <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>. A commercially successful robot might be highly optimized for a single use case <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.

The application of LLMs to [[prospects_and_challenges_in_robotics_and_ai_integration | robotics]] has been surprising <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>. The ability to quickly translate high-level natural language instructions (e.g., "make coffee") into actionable plans for a robot, leveraging the common-sense knowledge embedded in LLMs, was a breakthrough <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>. The realization that robot actions could be considered a "different language" or "dialect" of AI, similar to English or Chinese, allowed the leverage of existing large multimodal and multilingual model machinery <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.

### Generalizable vs. Task-Specific Models

The future of [[prospects_and_challenges_in_robotics_and_ai_integration | robotics]] models is likely to involve both generalizable "teacher" models and task-optimized versions <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. This parallels the instruction tuning paradigm in large language models, where generic capabilities are developed and then quickly adapted for specific tasks through prompting or fine-tuning <a class="yt-timestamp" data-t="00:37:23">[00:37:23]</a>. The ideal scenario would be prompting-style adaptation at test time <a class="yt-timestamp" data-t="00:38:19">[00:38:19]</a>.

Approaches to building powerful generalized robot models vary:
*   **Hardware-centric**: Building the most capable humanoid robot first, then expecting it to accomplish tasks <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>.
*   **Software-first**: Building the intelligence first, then trusting it can be retargeted to new platforms <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a>.

Vanhoucke gained confidence in the software-first approach from the RTX project, as it allows for faster progress by optimizing for data collection speed <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>. Operationalizing expensive, wobbly robots for data acquisition is a significant hurdle <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a>.

### Simulation vs. Real-World Data

The debate between using purely simulated data versus teleoperated real-world data in robotics is ongoing <a class="yt-timestamp" data-t="00:40:58">[00:40:58]</a>. While simulation has been effective for locomotion and navigation where the "sim2real gap" is manageable, it has been challenging for manipulation due to the difficulty in replicating diverse experiences and contact quality <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>. The cost of setting up diverse, representative, and physically realistic simulation environments for manipulation is very high <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a>. Vanhoucke's experience suggests that scaling physical operations to collect real-world data is often a faster path for manipulation, avoiding the sim2real gap <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>.

### Data Acquisition Flywheels and Human-Robot Interaction

A crucial element for [[prospects_and_challenges_in_robotics_and_ai_integration | robotics]] is a flywheel for acquiring data at scale <a class="yt-timestamp" data-t="00:43:33">[00:43:33]</a>. Human-robot interaction (HRI) for data acquisition is a rich but under-discussed area <a class="yt-timestamp" data-t="00:44:05">[00:44:05]</a>. Strategies include kinesthetic teaching, puppeteering, teleoperation with gloves, and synthesizing behaviors in simulation <a class="yt-timestamp" data-t="00:44:34">[00:44:34]</a>.

A desired development is "third-party imitation"—the ability for robots to learn from observing videos of people <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. This ties back to the World model challenge of inferring causality from observation <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>. The transfer of visual information from large multimodal models to robots has been a significant accelerator, as robots can now understand concepts like "Taylor Swift" without explicit training <a class="yt-timestamp" data-t="00:45:45">[00:45:45]</a>. The remaining challenge is acquiring the right kind of motion data for physical skills <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a>.

Injecting causality into models may not require new architectures but rather proper data engineering and inductive biases <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. Scaling laws observed in large models for behavior and perception suggest that the same log-linear growth patterns apply to autonomous driving models, albeit with different constants <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>.

## Reflections on AI Progress and Future Implications

### Changed Minds
Vanhoucke has been particularly fascinated by the evolution of reasoning capabilities in AI, especially the impact of "chain of thought" thinking <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>. He gives a personal example of using Gemini to quickly solve a physics problem for a science fiction story that he had pondered for a decade <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. This highlights the newfound accessibility to vast knowledge and reasoning capabilities, leading to the question of what other unasked questions could now be easily answered <a class="yt-timestamp" data-t="00:54:27">[00:54:27]</a>.

### Broad Applicability of AI
The ability to generate plausible answers for problems that are "hard to generate for but easy to verify" (e.g., coding, math) is broadly applicable <a class="yt-timestamp" data-t="00:55:58">[00:55:58]</a>. This "actor-critic" model, seen in reinforcement learning, can turn the hard problem of generation into the easier problem of verification, enabling applications beyond just coding or math, including autonomous driving <a class="yt-timestamp" data-t="00:56:37">[00:56:37]</a>.

Areas where these models will be effective include multi-step processes requiring credit attribution <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>. This is likened to "RL done right," where large models and supervised learning provide a strong bootstrap, with reinforcement learning used for fine-tuning to achieve expert-level reasoning <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>.

### Top-of-Mind Questions
*   The progression of the "World model" thrust, aiming for controllable video and World generation <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>. This could lead to purely generative video games <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.
*   Whether current large multimodal model architectures are sufficient for good World models, or if new architectural leaps are needed <a class="yt-timestamp" data-t="01:00:21">[01:00:21]</a>.
*   The potential for models to act as digital twins of anything, effectively turning every computer into a generative model, which will require massive compute investments <a class="yt-timestamp" data-t="01:00:42">[01:00:42]</a>.

## Quick Fire Round

### Overhyped/Underhyped
*   **Humanoid Robotics**: Both overhyped and underhyped <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. It's overhyped by large investments not yet justified by current capabilities, risking a "humanoid winter" if patience runs out <a class="yt-timestamp" data-t="01:02:09">[01:02:09]</a>. However, it's also underhyped because the potential impact is massive, and those in [[prospects_and_challenges_in_robotics_and_ai_integration | robotics]] "can't afford not to make them work" <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>.

### Predictions
*   **LLM Model Progress**: More progress this year than last year <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>.
*   **Robotics Models Progress**: More progress this year <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a>.
*   **Self-driving car rides exceeding human drivers in the US**: Hopes that in the future, human driving will seem "crazy" given the accidents it generates <a class="yt-timestamp" data-t="01:03:54">[01:03:54]</a>. The question is whether this happens in his lifetime <a class="yt-timestamp" data-t="01:04:21">[01:04:21]</a>.
*   **Go-to thing when new model comes out**: Checks LLM leaderboards to see where it stands on metrics, rather than relying on "vibes" <a class="yt-timestamp" data-t="01:04:52">[01:04:52]</a>. Focuses on whether the model helps in daily life or business <a class="yt-timestamp" data-t="01:05:30">[01:05:30]</a>.
*   **Most Americans having a robot in their house**: Already have robots like dishwashers, but mobile manipulators like Rosie will take a long time <a class="yt-timestamp" data-t="01:05:39">[01:05:39]</a>. Household robots need to justify their "square footage" and meet extremely high safety standards <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. Roomba's success is attributed to its contained area of operation <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>. More immediate applications are likely in logistics, industrial settings, near-home spaces (e.g., last-meter delivery), office environments, and hospitals where scale exists and there are established protocols for addressing minor damage <a class="yt-timestamp" data-t="01:07:28">[01:07:28]</a>.
*   **Under-talked about implications of AI progress**: Its impact on education <a class="yt-timestamp" data-t="01:08:12">[01:08:12]</a>. The focus on cheating ignores the potential for AI to be a "magical tool to learn things" through interactive, engaging conversations <a class="yt-timestamp" data-t="01:08:34">[01:08:34]</a>.

### Exciting AI Startups/Research
*   **Cheese**: Specifically, startups designing plant-based cheese using AI techniques <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>. This involves designing new products that are cheaper, more sustainable, and can have a massive impact due to the scale of animal farming and milk production <a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a>. An AI-based blue cheese is already served in top restaurants <a class="yt-timestamp" data-t="01:11:29">[01:11:29]</a>. The speaker finds "AI plus something you don't think about when you think about technology" to be particularly exciting <a class="yt-timestamp" data-t="01:11:54">[01:11:54]</a>.

To learn more about Vincent Vanhoucke's thoughts on machine learning, you can visit his blog on Medium <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>.