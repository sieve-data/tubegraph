---
title: The future of AI in robotics and its impact
videoId: Ctuf2Y0MrcA
---

From: [[redpointai]] <br/> 

Vincent Van, a distinguished engineer at Waymo and former founder and leader of Google's robotics team, provides insights into the current state and [[the_future_and_current_state_of_ai_agents | future potential of AI]] in robotics and autonomous vehicles. His expertise spans both these fields, offering a unique perspective on their integration and impact <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## AI in Autonomous Vehicles: Waymo's Approach

Waymo, a pioneer in self-driving technology, has been working on autonomous vehicles long before the recent explosion of advances in Large Language Models (LLMs) and diffusion models <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Integration of LLMs and VLM
The advent of LLMs and Vision-Language Models (VLMs) has not rendered Waymo's existing technology obsolete; rather, these models act as an enhancement <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. They facilitate the creation of "teacher models" – large-scale models that can ingest vast amounts of data, including internet data, to build a comprehensive understanding of the Waymo driver, car behavior, and the environment <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This "World Knowledge" provides semantic understanding, allowing the autonomous system to recognize elements like police cars or accident scenes, even in new cities where specific local data might be scarce <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. LLMs also enhance the reasoning capabilities of these systems <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Limitations and Safety
While AI models are powerful for generating driving plans, aspects like strict safety contracts and regulatory compliance are still managed externally, outside the AI model <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This allows for explicit verification that the AI-proposed plan meets all safety and compliance requirements <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Current Challenges and Future Breakthroughs
A primary challenge for autonomous vehicles today is scaling to handle "long-tail problems" – rare, exceptional, or difficult scenarios that a human driver might encounter once in a lifetime but an autonomous fleet experiences regularly due to millions of miles driven <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Waymo addresses this through extensive simulation and synthesizing scenarios to validate their models against potential issues not yet observed in real-world data <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

A significant technical advance that could revolutionize autonomous driving is the development of reliable, physically realistic [[future_potential_of_autonomous_ai_agents_in_various_fields | world models]] <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. These models would allow for highly accurate and controllable simulations of the real world, serving as a "digital twin" for autonomous driving <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. While video prediction models like Sora or Vo are "proto world models," the challenge lies in making them controllable and ensuring physical realism, especially for long-tail problems where current models are not yet proficient <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. A key hurdle to achieving this is injecting causality into models, moving beyond mere correlation <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

### Sensor Suite
Waymo employs a comprehensive sensor suite including cameras, Lidars, and Radars <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. These sensors are complementary, with their individual strengths and weaknesses offsetting each other, providing critical redundancy and allowing for cross-validation of data <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>. This approach contrasts with others that prioritize simpler, cheaper sensor setups for L2 driving, aiming to scale up later <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>. Waymo's strategy involved initially "over-sensorizing" to solve the harder problem first, then using the collected data to inform cost reduction <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.

The performance bar for L4 (fully autonomous) driving is considered to be *above* human level <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>. Waymo's safety reports indicate they are already safer than the average human driver, with fewer collisions and reported injuries <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>. This "superhuman" capability is seen as a business requirement for successful L4 driving <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### Milestones and Expansion
The next major milestones for autonomous vehicles will be centered around expansion into new geographies <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. Waymo is, for example, beginning data collection in Tokyo, marking their first international expansion and a foray into left-side driving <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>. The robustness and portability of their models across different cities are proving remarkable, with much of the effort in new cities focused on evaluation, regulatory compliance, and community engagement to build trust <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

## Broader Robotics Space

The robotics field is still "chasing the nominal use case" – striving to achieve a generalized robot capable of performing diverse tasks <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>. Unlike autonomous driving, which has reached commercial deployment after decades, general-purpose robotics has not yet had its "1995 ride" moment (referencing the first transcontinental autonomous drive) <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.

### Impact of Large Models
The application of LLMs and VLMs to robotics has been surprisingly effective <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>. A key breakthrough has been the ability to quickly translate high-level, common-sense knowledge (e.g., how to make coffee, objects on a table) from chat models into actionable plans for robots <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. This is partly because robot actions can be viewed as another "language," allowing the leverage of multimodal and multilingual large models for generalization <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.

### Generalization and Data Acquisition
A significant challenge in robotics is generalizing motion and skills, as many robot demos are highly specific to a single task <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>. There are two main approaches to building generalized robotic models:
1.  **Hardware-Centric:** Building the most capable humanoid robot first, then developing the software <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>.
2.  **Software-First:** Building general intelligence and trusting it can be retargeted to new platforms <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a>.

The software-first path, exemplified by efforts like RTX, has shown faster progress due to its focus on efficient data acquisition <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>. The bottleneck in robotics remains acquiring high-quality data at scale <a class="yt-timestamp" data-t="00:39:55">[00:39:55]</a>.

While simulation is valuable for locomotion and navigation, the "sim-to-real gap" has made it less effective for complex manipulation tasks due to the difficulty of accurately tuning physics and achieving diverse contact experiences <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>. Consequently, scaling physical operations to collect real-world data has been a more effective approach for manipulation <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

New data acquisition strategies are crucial, including kinesthetic teaching, puppeteering, and teleoperation <a class="yt-timestamp" data-t="00:44:34">[00:44:34]</a>. A desired future capability is "third-party imitation," where robots can learn from watching videos of humans <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>. Multimodal models have already accelerated visual information transfer to robots (e.g., recognizing Taylor Swift without specific training) <a class="yt-timestamp" data-t="00:45:48">[00:45:48]</a>, shifting the focus to acquiring motion and physical skills data <a class="yt-timestamp" data-t="00:46:39">[00:46:39]</a>.

### Unanswered Questions in Robotics
Key questions for the [[the_future_and_current_state_of_ai_agents | future of robotics]] include:
*   Can motion be generalized across different actions and environments, similar to how perception generalizes <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>?
*   Are there fundamental differences between robotics and other areas of AI that will require new techniques, or will existing large model architectures suffice <a class="yt-timestamp" data-t="00:48:35">[00:48:35]</a>? For example, diffusion models, effective for video generation, also work well for motion generation in robotics <a class="yt-timestamp" data-t="00:49:10">[00:49:10]</a>.
*   Will scaling laws, similar to those observed in LLMs, apply to robotics models, even if constants differ <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>?

## Broader [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | AI Reflections]] and Impact

### Reasoning Capabilities
The evolution of reasoning capabilities in LLMs, particularly through "chain-of-thought" prompting, has been a significant development <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>. This allows users to access expert-level knowledge (e.g., complex physics or legal information) instantly, fundamentally changing how information is accessed and utilized <a class="yt-timestamp" data-t="00:54:27">[00:54:27]</a>.

### Applications of AI
[[future_applications_of_ai_in_workplace_automation | AI models]] are highly effective in domains where problems are hard to generate but easy to verify, such as coding or math <a class="yt-timestamp" data-t="00:56:02">[00:56:02]</a>. This "actor-critic" model, where a generative model proposes a solution and another system verifies it, is broadly applicable <a class="yt-timestamp" data-t="00:56:41">[00:56:41]</a>. In autonomous driving, it's easier to verify a plan against hard constraints than to generate it from scratch <a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>.

[[future_of_software_development_and_ai | Reasoning capabilities]] of AI will impact multi-step problems requiring credit attribution <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>. The preferred paradigm for AI development now involves bootstrapping with a large model, extensive supervised learning, and then using reinforcement learning (RL) for fine-tuning to achieve expert performance <a class="yt-timestamp" data-t="00:59:04">[00:59:04]</a>.

### Future Directions
Key questions for the next 12-24 months in the broader LLM space include:
*   The progress of "world models" and controllable video/world generation, potentially leading to purely generative video games <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>.
*   Whether current large multimodal architectures can effectively create good world models, or if new architectural leaps are needed <a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>.
*   The significant compute investments required for these next steps <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>.

### Overhyped vs. Underhyped
Humanoid robotics is viewed as both overhyped and underhyped <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. While there's significant investment, success is not guaranteed, risking a "humanoid winter" if patience runs out <a class="yt-timestamp" data-t="01:02:30">[01:02:30]</a>. However, it's also underhyped because the field needs to succeed for the broader progress of robotics <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>. Progress in LLM and robotics models is expected to accelerate even further <a class="yt-timestamp" data-t="01:03:16">[01:03:16]</a>.

### [[role_of_ai_in_future_business_operations | Societal Impact]] and [[policy_implications_of_ai_advancements | Policy Implications]]
There's a potential future where humans look back at today's reliance on human-driven cars as "crazy" due to the high accident rates <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>. The expectation is that autonomous vehicles will surpass human safety levels <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>.

While many homes already have "robots" (e.g., dishwashers, washing machines) <a class="yt-timestamp" data-t="01:05:40">[01:05:40]</a>, general-purpose mobile manipulators (like Rosie from The Jetsons) will take much longer to become commonplace <a class="yt-timestamp" data-t="01:05:53">[01:05:53]</a>. The bar for household robots is extremely high regarding safety and preventing damage to the home environment <a class="yt-timestamp" data-t="01:06:11">[01:06:11]</a>. More immediate applications for mobile robots are expected in structured environments like logistics, industrial settings, last-mile delivery, offices, and hospitals, where costs of damage can be more easily managed <a class="yt-timestamp" data-t="01:07:28">[01:07:28]</a>.

One under-talked implication of [[future_trends_in_ai_hardware_and_software | AI progress]] is its transformative effect on education <a class="yt-timestamp" data-t="01:08:15">[01:08:15]</a>. AI offers a "magical tool" for interactive and engaging learning, moving beyond concerns about cheating to unlock new pedagogical approaches <a class="yt-timestamp" data-t="01:08:40">[01:08:40]</a>.

Another exciting, under-discussed area is the use of AI techniques to design new products, particularly in industries not traditionally associated with technology. An example is using AI to design plant-based cheese, exploring the "design space" for non-animal-based products that could have a massive environmental impact <a class="yt-timestamp" data-t="01:10:40">[01:10:40]</a>. This highlights the potential of "AI plus something you don't think about when you think about technology" <a class="yt-timestamp" data-t="01:11:54">[01:11:54]</a>.