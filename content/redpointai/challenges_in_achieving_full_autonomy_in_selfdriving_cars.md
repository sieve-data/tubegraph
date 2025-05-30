---
title: Challenges in achieving full autonomy in selfdriving cars
videoId: Ctuf2Y0MrcA
---

From: [[redpointai]] <br/> 

The field of autonomous vehicles (AVs) has seen significant advancements, with systems like Waymo operating commercially in certain areas <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. However, achieving full, widespread autonomy still presents several complex challenges. Vincent Vu, a distinguished engineer at Waymo and former head of Google's robotics team <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, highlights key technical and operational hurdles.

## The Role and Limitations of AI Models

The recent "foundation model revolution," involving large language models (LLMs) and visual-multimodal models (VMMs), has significantly impacted autonomous vehicle technology <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Benefits of LLMs/VMMs
These models enhance AV capabilities by providing:
*   **World Knowledge:** A semantic understanding of the world, including recognizing various police cars or emergency vehicles even in new cities where specific data hasn't been collected <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. They can interpret complex scenes like accident sites, understanding the semantic context <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Enhanced Reasoning:** Pre-training on vast amounts of visual and text data improves their reasoning capabilities <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Scalability:** Larger models generally lead to better performance <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. These models act as "teacher models" to distill data into onboard car models <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Areas Where AI Models Fall Short
While powerful, AI models are not ideal for all aspects of self-driving:
*   **Safety and Regulatory Constraints:** Aspects requiring strict contracts on safety or regulatory compliance are best expressed in an explicit, verifiable way, rather than implicitly within an AI model <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>, <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. This allows for verification that the proposed driving plan meets safety and compliance requirements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Verification Layer:** A "checking layer" or "guard rails" are needed around the output of reasoning models to ensure safe and well-behaved actions <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## Key Challenges for Full Autonomy

The primary hurdles for widespread autonomous driving relate to **scaling**, the **long tail of rare problems**, and the development of [[advancements_in_simulation_and_world_modeling_for_autonomous_technology | advanced world models]].

### Scaling and the "Long Tail" of Problems
Waymo's experience, driving millions of miles, reveals that rare, exceptional events become common occurrences <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Rare Scenarios:** While an average human driver might experience a specific difficult situation once in a lifetime, an AV fleet encounters it every week or month <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Overcoming Edge Cases:** Problems like driving in snow or fog, or on highways, are primarily scaling challenges rather than fundamental blockers <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. The focus is on solving for this "long tail" of problems <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### Addressing Long-Tail Problems: Simulation and Synthetic Data
Since there isn't a massive amount of real-world data for these rare scenarios, Waymo uses:
*   **Simulation:** Extensive use of simulation to test models <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **Synthesizing Scenarios:** Generating scenarios that could happen but haven't been observed <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Modifying Real Scenarios:** Taking real-world risky situations (where nothing bad happened) and modifying them to be worse (e.g., making other drivers "drunk" or "adversarial") to stress-test the system and improve reactivity <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

### The Need for Physically Realistic World Models
A significant technical advance that could "completely change the landscape" is the development of reliable, physically realistic [[advancements_in_simulation_and_world_modeling_for_autonomous_technology | world models]] <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   **Goal:** To simulate the real world with physical realism and accurate rendering, creating a "digital twin" of the environment <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>, <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   **Current State:** Proto-world models like Sora or Vo can predict future video frames that seem physically reasonable <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. However, they are not yet controllable or useful enough for precise functional uses <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>, <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Challenge of Causality:** A core issue is teaching models to understand causality – how an input change leads to a specific output <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>, <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. While LLMs show signs of causal reasoning through "chain of thought," it's not yet clear if new architectures are needed or just better data engineering <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>, <a class="yt-timestamp" data-t="00:47:05">[00:47:05]</a>.

### Sensor Suites and the "Superhuman" Bar
Waymo utilizes a rich sensor suite (cameras, lidars, radars) due to their complementary strengths and weaknesses, enabling cross-validation of data <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
*   **Business Strategy:** Waymo chose to "over-sensorize" initially to solve the hard problem first, allowing them to gather data and inform future cost reduction decisions <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>. This contrasts with L2 driving systems that prioritize lower cost <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
*   **Beyond Human Level:** The bar for L4 autonomous driving is considered "above human level" <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>. Waymo's safety reports indicate they are already safer than the average human driver, with fewer collisions and injuries <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>. This "superhuman" performance is seen as a business requirement for successful L4 driving <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>. The question remains whether this can be achieved with a simpler sensor suite <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>. Redundancy in sensing is likely to remain important <a class="yt-timestamp" data-t="00:25:47">[00:25:47]</a>.

### Human Trust and Public Acceptance
Beyond technology, integrating AVs into society requires building trust with the local community and addressing logistical challenges of entering new cities <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

> [!NOTE] Building trust is "a lot more than just technology" <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

## The Broader Robotics Context

Autonomous cars are fundamentally robots <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>, and lessons from general robotics apply.

### Current State of General Robotics
Unlike autonomous driving, which has a "nominal system that works," the general robotics space is still "chasing the nominal use case" – getting a generalized robot to do anything desired <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>, <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>.
*   **Lack of Generalization in Motion:** While robots can generalize based on visual inputs, they struggle with generalizing motion or "skills" <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>, <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.
*   **Path to Commercial Success:** Commercial success might come from highly optimized, task-specific robots, but the broader vision of general-purpose AI robots (e.g., making coffee, tidying rooms) still requires breakthroughs <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.

### Impact of LLMs on Robotics
The application of LLMs and VMMs to robotics has been a significant surprise, particularly in overcoming the "common sense knowledge" bottleneck <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>, <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.
*   **Common Sense:** LLMs provide robots with everyday knowledge (e.g., a cup goes on the table, not the floor) that was previously difficult to inject <a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>.
*   **Action as Language:** The realization that robot actions can be viewed as a different "language" or "dialect" allows leveraging multimodal and multilingual models for robotic control <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. This means the same "machinery" for language processing can apply to robot actions <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

### Approaches to Building Robot Models
Two main approaches exist for developing robot models:
1.  **Hardware-Centric:** Building the most capable humanoid robot first, then programming tasks <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>. This can be very expensive and hard to operationalize for data acquisition <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a>.
2.  **Software-First:** Building the intelligence first, with the trust that it can be retargeted to different hardware platforms <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a>. This path, exemplified by work like RTX, focuses on data acquisition speed and scalability <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.

### Simulation vs. Real-World Data for Robotics
*   **Locomotion and Navigation:** Simulation has been highly effective in these contexts due to a manageable "sim-to-real gap" <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>.
*   **Manipulation:** It has been difficult to get sufficient diversity and quality of experience from simulation for manipulation tasks, especially regarding contact physics <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>. The effort required to make simulation realistic for manipulation is very high <a class="yt-timestamp" data-t="00:42:10">[00:42:10]</a>.
*   **Scaling Real-World Data:** For manipulation, scaling physical operations to collect large amounts of real-world data has been a faster path <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

### Data Acquisition in Robotics
A crucial bottleneck is acquiring data at scale, particularly motion data for physical skills <a class="yt-timestamp" data-t="00:39:55">[00:39:55]</a>, <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a>.
*   **Methods:** Strategies include kinesthetic teaching, puppeteering, or teleoperation <a class="yt-timestamp" data-t="00:44:36">[00:44:36]</a>.
*   **Third-Party Imitation:** A promising but unsolved area is learning from passively watching videos of people doing tasks, which again links back to the challenge of inferring causality from observation <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>.
*   **Visual Information Transfer:** Multimodal models have significantly accelerated data acquisition by transferring visual knowledge (e.g., knowing who Taylor Swift is without specific training data) <a class="yt-timestamp" data-t="00:45:45">[00:45:45]</a>.

## Future Outlook

The trajectory of autonomous driving and robotics will be determined by how these [[challenges_in_aidriven_research_and_novel_planning | challenges in AI-driven research and novel planning]] are addressed. Progress in LLMs and robotics models is expected to accelerate <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>.

> [!NOTE] The biggest milestone for self-driving cars now is expansion across geographies, demonstrating robustness in diverse environments <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>. Waymo is exploring international deployments, like driving on the left side of the road in Tokyo <a class="yt-timestamp" data-t="01:00:28">[01:00:28]</a>.

The long-term vision is a future where humans look back and consider driving cars by hand "crazy" due to the level of accidents <a class="yt-timestamp" data-t="01:03:54">[01:03:54]</a>. This requires continuous innovation in [[integration_of_ai_in_autonomous_vehicles | integration of AI in autonomous vehicles]] and broader robotic systems.