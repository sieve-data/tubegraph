---
title: Breakthroughs in autonomous vehicle technology
videoId: Ctuf2Y0MrcA
---

From: [[redpointai]] <br/> 

Autonomous vehicle technology has seen significant advancements, with companies like Waymo leading the charge. Vincent Vanhoucke, a distinguished engineer at Waymo and former lead of Google's robotics team, provides insights into the current state and future trajectory of this field <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Impact of AI Models on Autonomous Driving

The recent [[Role of AI models in advancing robotics and autonomous driving | foundation model revolution]], including large language models (LLMs) and visual models (VMS), has profoundly influenced autonomous vehicle development <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. These models allow for the creation of "teacher models" that process vast amounts of data, including internet data, to build comprehensive models of the Waymo driver, car behavior, and the environment <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This approach enriches existing systems without requiring a complete overhaul, essentially providing every model with a better teacher and more information <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

A key contribution of LLMs and VMS is "World Knowledge," which encompasses semantic understanding of the surrounding environment <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a> <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. For example, these models can recognize what a police car or an accident scene looks like, even if Waymo's internal driving data hasn't frequently encountered such scenarios in a new city <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a> <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This external knowledge from the web enhances the driver's capabilities <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

However, AI models are not exclusively relied upon for all aspects of self-driving <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Aspects related to strict safety contracts and regulatory constraints are expressed explicitly, outside the AI model <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a> <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This "checking layer" or "guard rails" ensures that the AI-proposed driving plan meets all safety and compliance requirements <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a> <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## Waymo's Journey and Challenges

Vincent Vanhoucke's transition to Waymo was partly accidental, driven by his personal experience using the service during an injury <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a> <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. He found the product "magical" and an AI system that easily touched everyone <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a> <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

At its core, an autonomous car is a robot, sharing the same inputs (sensors, cameras) and outputs (actuation like steering and acceleration) as a manipulation robot <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a> <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The major difference lies in the operational domain <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. While general [[The future of AI in robotics and its impact | robotics]] still focuses on achieving nominal behavior (e.g., picking up an object, making coffee) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a> <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>, autonomous driving has a working nominal system at a commercial product level of safety and performance <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a> <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

The primary [[Challenges and bottlenecks in selfdriving cars | challenges and bottlenecks in selfdriving cars]] for Waymo today revolve around scaling <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. While issues like driving in snow are solvable with more attention <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>, the "long tail" of rare, exceptional, and difficult problems dominates the equation <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a> <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. What a human driver might encounter once in a lifetime, Waymo cars experience weekly or monthly <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. Waymo addresses these long-tail problems through extensive simulation and by synthesizing scenarios, often modifying real-world events to make them worse (e.g., "make all the drivers drunk drivers" or "actively adversarial") <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a> <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## The Future: Reliable World Models

A critical technical advance that could fundamentally change the autonomous driving landscape is the development of reliable, physically realistic world models <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a> <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. These models would enable the simulation of the real world with high physical realism and accurate scene rendering <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a> <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Current [[Advancements and potential of video and robotics models | video prediction models]] like Sora or Vio are proto-world models that can unroll plausible futures, but lack the physical realism and controllability needed for autonomous driving <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a> <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. The challenge is to make these models controllable, physically realistic, rich in detail, and plausible in visual appearance and object behavior <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a> <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

The main obstacle to building effective world models is the deep question of causality <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. While current models can generate plausible videos by learning correlations, achieving controllability requires understanding causality – how an input change leads to a specific output <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a> <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.

## Waymo's Research and Sensor Strategy

Waymo actively conducts significant research, often leading the state-of-the-art in AI, acknowledging that they cannot always rely on the broader community for solutions to bespoke AV problems <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a> <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. Their Waymo Open Datasets, for instance, were designed to steer academic research toward relevant AV challenges <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.

Waymo's models demonstrate remarkable robustness and portability across different cities, with adaptations mostly focusing on thorough evaluation and ensuring no critical differences are missed (e.g., variations in emergency vehicle appearance) <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a> <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

Waymo employs a comprehensive sensor suite, including cameras, lidars, and radars <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a> <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. These sensors are highly complementary, with their strengths and weaknesses balancing each other out, providing crucial redundancy and orthogonal data for verification <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a> <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

Unlike companies that start with L2 driving assistance and attempt to scale up to L4 (fully autonomous) with economic constraints on sensors, Waymo historically chose to "over-sensorize" from the start <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a> <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a> <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>. This strategy allowed them to solve the harder problem first, gathering essential data to inform future cost reduction and simplification efforts <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a> <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. The argument that humans drive with only eyes and don't need lidar is countered by the conviction that the bar for L4 driving is *above* human level <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a> <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a> <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>. Waymo's safety reports indicate they are already safer than the average human driver, with fewer collisions and injuries <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>. This "superhuman" performance is seen as a business requirement for successful L4 driving <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a> <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

## Milestones and Future Trajectory

The history of autonomous vehicles highlights the difficulty of predicting timelines. The first transcontinental autonomous drive in 1995 achieved over 99% autonomy, leading to initial over-optimism <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a> <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>. It took 30 years to reach commercial deployment <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>.

Currently, Waymo has achieved technology validation in cities like Phoenix and San Francisco, along with strong user validation <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a> <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. The next milestones will focus on expansion into new geographies <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. Waymo has begun collecting data in Tokyo, marking their first international experiment and initial foray into left-side driving <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.

> [!NOTE] Trust is more than just technology.
> Waymo emphasizes building trust with local communities through respectful operations and supporting the areas they work in, recognizing that public trust is crucial for deployment <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a> <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

## [[Future trends in AI hardware and software | Future Trends in AI and Robotics]]

### Generalization in Robotics

A significant question in [[The future of AI in robotics and its impact | robotics]] is the ability to generalize motion and actions, similar to how models generalize visual inputs <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>. While current robot demonstrations often perform a single task, the goal is for robots to generalize diverse skills <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a> <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>.

The application of LLMs to [[Role of AI models in advancing robotics and autonomous driving | robotics]] has been a pleasant surprise <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. The key breakthrough is the ability of LLMs to provide "Common Sense knowledge" (e.g., a cup goes on a table, a microwave is in the kitchen) that was historically difficult to inject into robotics <a class="yt-timestamp" data-t="00:34:35">[00:34:35]</a> <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>. This high-level, albeit fuzzy, language-based knowledge can be quickly translated into actionable robot plans <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>. Furthermore, recognizing robot actions as another form of language or "dialect" allows leveraging multimodal and multilingual large models for robot control <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a> <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>.

### Approaches to Robotics Development

There are two main approaches to developing robots:
1.  **Hardware-Centric**: Building the most capable humanoid robot first, then developing the software <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>. This path can be very expensive and difficult to scale due to the complexity of operationalizing wobbly, costly robots for data acquisition <a class="yt-timestamp" data-t="00:40:07">[00:40:07]</a> <a class="yt-timestamp" data-t="00:40:13">[00:40:13]</a>.
2.  **Software-First**: Building intelligence and trusting that it can be easily retargeted to new platforms <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a>. This approach, exemplified by the RTX project, allows faster progress by optimizing for data collection and execution speed, especially since the fundamental problem of robotic manipulation is not yet solved <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a> <a class="yt-timestamp" data-t="00:40:41">[00:40:41]</a>.

While simulation is valuable for locomotion and navigation due to a smaller sim-to-real gap, it has been less successful for manipulation <a class="yt-timestamp" data-t="00:41:12">[00:41:12]</a> <a class="yt-timestamp" data-t="00:41:19">[00:41:19]</a>. The cost of setting up diverse, realistic, and tuned physics environments for manipulation simulation is very high <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>. Scaling physical operations to collect large amounts of real-world data has proven to be a faster path <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

### Data Acquisition and Human-Robot Interaction

A critical bottleneck in robot learning is data acquisition <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. Effective methods include kinesthetic teaching, puppeteering, and teleoperation with gloves <a class="yt-timestamp" data-t="00:44:36">[00:44:36]</a>. A desired but currently unsolved method is "third-party imitation," where robots learn by observing videos of humans, which again relies on inferring causality from observation <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a> <a class="yt-timestamp" data-t="00:45:23">[00:45:23]</a>.

The advent of large multimodal models has accelerated data by enabling visual information transfer to robots <a class="yt-timestamp" data-t="00:45:45">[00:45:45]</a>. For instance, a robot can move a Coke can towards a picture of Taylor Swift without explicit teaching about Taylor Swift, as that knowledge is embedded in the multimodal model <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>. The remaining challenge is acquiring motion data for physical skills <a class="yt-timestamp" data-t="00:46:39">[00:46:39]</a>.

### [[AI Integration in Consumer Devices and Robotics | AI in Consumer Devices and Robotics]]

While robots exist in homes (e.g., dishwashers, washing machines), consumer interest in mobile manipulators like the "Rosie robot" is still some way off <a class="yt-timestamp" data-t="00:55:50">[00:55:50]</a>. The bar for a robot in a home is extremely high due to the need for safety and preventing damage <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a> <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>. Roomba-like robots have succeeded because they operate in low-risk areas <a class="yt-timestamp" data-t="00:56:41">[00:56:41]</a>. More immediate applications for mobile robots are expected in logistics, industrial, near-home spaces (e.g., last-meter delivery), office, and hospital environments where there is scale and infrastructure to manage potential incidents <a class="yt-timestamp" data-t="01:07:31">[01:07:31]</a>.

### Under-talked Implications of AI

A significant, yet under-discussed, implication of [[Implications of autonomous AI agents | AI progress]] is its transformative effect on education <a class="yt-timestamp" data-t="01:08:12">[01:08:12]</a>. AI offers an interactive and engaging tool for learning that goes beyond concerns about cheating <a class="yt-timestamp" data-t="01:08:34">[01:08:34]</a>.

## Overhyped and Underhyped in AI

Vincent Vanhoucke views humanoid robotics as both overhyped and underhyped <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. While there are significant investments and potential for a "humanoid winter" if success isn't achieved, it is also underhyped in that those in robotics should be working on it because "we can't afford not to make them work" <a class="yt-timestamp" data-t="01:02:30">[01:02:30]</a> <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a> <a class="yt-timestamp" data-t="01:02:48">[01:02:48]</a>.

Progress in both LLM and robotics models is expected to accelerate <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a> <a class="yt-timestamp" data-t="01:03:16">[01:03:16]</a>.

An exciting area of AI startups and research is the application of AI techniques to design new products, such as plant-based cheese <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a> <a class="yt-timestamp" data-t="01:10:40">[01:10:40]</a>. This represents using AI to explore design space for non-animal based products with massive impact potential <a class="yt-timestamp" data-t="01:10:53">[01:10:53]</a> <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>.

## Key Questions for the Future

Key questions for the next few years include:
*   Can motion be generalized in the space of actions, similar to perception? <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>
*   Are there fundamental differences between robotics and other areas of AI that will require new techniques? <a class="yt-timestamp" data-t="00:48:35">[00:48:35]</a> (Currently, many techniques like diffusion models from video generation are working well in robotics <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.)
*   Will scaling laws continue to apply to large models in autonomous driving, or will they hit limits? <a class="yt-timestamp" data-t="00:49:46">[00:49:46]</a> (So far, similar log-linear growth patterns are observed as in LLMs, albeit with different constants <a class="yt-timestamp" data-t="00:49:56">[00:49:56]</a>.)
*   How far can the "world model" thrust take us, especially with controllable video and world generation? <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a> If current large multimodal architectures cannot produce good world models, a new architectural leap may be necessary <a class="yt-timestamp" data-t="01:00:21">[01:00:21]</a>.
*   What are the computational demands for creating "digital twins" of anything, and will massive investments in [[Challenges and innovations in AI hardware | compute]] be justified? <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a> <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>.

> [!NOTE] Vincent Vanhoucke's Blog
> Vincent Vanhoucke shares his insights and "random thoughts about machine learning" on his Medium blog <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.