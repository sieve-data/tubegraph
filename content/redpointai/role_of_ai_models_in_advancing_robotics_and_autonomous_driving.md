---
title: Role of AI models in advancing robotics and autonomous driving
videoId: Ctuf2Y0MrcA
---

From: [[redpointai]] <br/> 
[[The future of AI models and open source development | The Role of AI Models in Advancing Robotics and Autonomous Driving]]

Vincent Vuk, a distinguished engineer at Waymo and former leader of Google's robotics team, discusses the transformative impact of AI models on autonomous vehicles and the broader field of robotics. He shares insights into Waymo's technological advancements, the challenges of scaling autonomous driving, and the future potential of generalized robotics.

### Impact of LLMs and Foundation Models on Autonomous Vehicles

The advent of Large Language Models (LLMs) and foundation models has significantly influenced autonomous vehicle technology at Waymo, building upon existing systems rather than replacing them [01:40:53]. These models act as "teacher models," large-scale systems running in the cloud that assimilate vast amounts of data, including internet data, to understand the Waymo driver, car behavior, and the environment [02:00:30]. This comprehensive "World Knowledge" is then distilled into the onboard models of the vehicle, providing better supervision and more information [02:55:01].

A key contribution of LLMs and Vision Models (VMs) is the incorporation of semantic understanding, such as recognizing police cars or emergency vehicles in new cities, or identifying accident scenes, even if Waymo's collected driving data hasn't encountered them frequently [03:22:04]. This knowledge, drawn from the web, enhances the driver's capabilities and reasoning [04:42:01]. The large scale and pre-training of these models on extensive visual and text data also directly improve performance, as "bigger is always better" [04:45:00].

However, AI models are not exclusively relied upon for every aspect of self-driving. Strict safety and regulatory constraints are often handled by explicit, verifiable systems built *outside* the core AI model [05:30:00]. This allows the AI to propose driving plans, which are then checked externally to ensure compliance and safety [05:50:00].

### Transition to Waymo and Similarities with Robotics

Vincent Vuk's move to Waymo was influenced by a personal experience taking Waymo rides after an accident, finding the product "magical" and "applicable to everybody" [07:00:00].

At its core, an autonomous car functions as a robot, sharing similar inputs (sensors, cameras) and outputs (actuation like steering and acceleration) with manipulation robots [08:31:00]. The main distinction lies in the "operational domain" [09:09:00]. While general robotics research often focuses on achieving a nominal behavior (e.g., making a robot pick up an object or make coffee) [09:18:00], autonomous driving has already achieved a functional, commercially viable system [09:58:00]. The primary challenges in autonomous driving are now about scaling and addressing "the long tail of problems" that become common occurrences across millions of miles driven [11:11:00].

### Current State and Future Challenges in Autonomous Driving

Current challenges in autonomous driving are largely not "big blockers" [10:31:00], but rather involve scaling solutions for edge cases like driving in snow or fog, or on highways [10:37:00]. These "long tail" problems, which might occur once in a human's lifetime, happen weekly or monthly for an autonomous fleet [11:50:00]. Waymo addresses this through extensive simulation, synthesizing scenarios corresponding to known potential problems, and modifying real-world data to create "worse" scenarios (e.g., drunk or adversarial drivers) to train the system [12:37:00].

A significant [[advancements_and_potential_of_video_and_robotics_models | technical advance]] that could reshape autonomous driving is the development of reliable, physically realistic [[advancements_and_potential_of_video_and_robotics_models | World models]] [14:05:00]. These models would allow for highly accurate simulation of the real world, akin to a "digital twin" [15:31:00]. Examples like Sora or Veo, which perform video prediction, are considered "proto [[advancements_and_potential_of_video_and_robotics_models | World models]]" [14:49:00]. The key challenge in World models is making them controllable and ensuring they understand causality—that specific inputs lead to predictable outputs [17:30:00].

Waymo's research approach balances pushing the state-of-the-art internally with leveraging external academic and institutional research [18:52:00]. They have released the Waymo Open Datasets to steer research focus towards relevant problems in autonomous vehicles [19:35:00]. The models are remarkably robust and portable across different cities, with much of the effort in new deployments focused on evaluation and gaining community trust rather than re-adapting the core model [20:30:00].

### Sensor Suite and the "Superhuman" Bar

Waymo's vehicles utilize a rich sensor suite of cameras, lidars, and radars, which are complementary and provide redundancy for cross-validation [22:30:00]. This contrasts with some other approaches that prioritize simpler, cheaper sensor setups for L2 (driving assistance) systems [23:31:00]. Waymo's strategy has been to "over-sensorize" initially to solve the harder problem and gather data, then work on cost reduction and simplification with informed decisions [24:20:00].

Vuk emphasizes that the bar for L4 (fully autonomous) driving is "above human level" [26:37:00]. Waymo's safety reports indicate they are already safer than the average human driver, with fewer collisions and injuries [26:46:00]. This "superhuman" performance is seen as a business requirement for successful L4 deployment [27:10:00].

### Broader Robotics and [[The future of AI in robotics and its impact | The Future of AI]]

In the broader robotics space, the goal is still to achieve a "generalized robot to do anything we want" [31:35:00]. While progress has been rapid, a convincing generalist system, comparable to the 1995 transcontinental autonomous drive that seemed to indicate readiness, is not yet present [31:53:00]. A significant technical question remains: generalizing motion, as opposed to just perception [32:30:00].

LLMs have been surprisingly effective in robotics, particularly in bringing "Common Sense knowledge" (e.g., a cup goes on a table, a microwave is in the kitchen) that was previously difficult to inject [34:31:00]. The realization that robot actions can be viewed as "just a different language" [35:55:00], leveraging the same multimodal large models used for human languages, has been a breakthrough [36:10:00].

The future of robotics will likely involve both generalized "teacher" models that are easily retargetable, and specialized models optimized for single tasks [37:04:00]. This mirrors the trend in large language models where generic capabilities are refined through instruction tuning or fine-tuning for specific applications [37:22:00].

### Approaches to Robot Models and Data Acquisition

There are two main approaches to building generalized robotic models:
1.  **Hardware-centric**: Building the most capable robot first, then developing the intelligence [38:58:00].
2.  **Software-first**: Building intelligence first, trusting it can be retargeted to new platforms [39:15:00].

Vuk has confidence in the software-first path, partly due to work on RTX, emphasizing that data acquisition is the primary bottleneck in robotics [39:52:00]. Relying on expensive, complex hardware for data collection limits scalability [40:07:00].

While simulation works well for locomotion and navigation, manipulation has struggled with the "sim-to-real gap" [41:15:00]. It's often been more effective to scale physical operations to collect real-world data, despite the monetary cost [42:27:00]. However, he notes that many academic labs are more invested in simulation [43:09:00].

Effective human-robot interaction (HRI) for data acquisition is crucial [44:02:00]. Methods include kinesthetic teaching, puppeteering, teleoperation with gloves, or synthesizing behaviors in simulation [44:34:00]. [[The future of AI in robotics and its impact | Third-party imitation]], learning from watching videos of people, is a promising but unsolved area, requiring models to infer causality from observation [45:05:00]. The ability of [[The future of AI models and open source development | big multimodal models]] to transfer visual information (e.g., recognizing Taylor Swift without explicit training) has accelerated data acquisition [45:48:00]. The remaining challenge is acquiring motion and physical skill data [46:33:00].

### Unanswered Questions and Future Directions

Key questions for the next few years include:
*   Can models generalize motion in the same way they generalize perception? [48:06:00]
*   Are there fundamental differences between robotics and other AI areas that will require new techniques? [48:32:00] (Currently, diffusion models for motion generation seem to follow similar scaling laws as other large models [49:06:00])
*   How far will the "World model" thrust go, enabling controllable video and world generation? [59:43:00]
*   Will current multimodal architectures suffice for good World models, or will new architectures be needed? [01:00:21:00]

Vuk foresees a future where every computer could become a generative model, possibly requiring massive investments in compute infrastructure [01:00:59:00].

### Broader [[Implications of autonomous AI agents | Implications]] of AI Progress

Vuk believes LLM and robotics model progress will accelerate [01:13:11:00]. He envisions a future where self-driving cars exceed human drivers, making manual driving seem "crazy" given accident rates [01:03:56:00].

He highlights the underappreciated [[implications_of_autonomous_ai_agents | impact of AI on education]] [01:15:00]. Beyond concerns about cheating, AI agents offer a "magical tool" for interactive and engaging learning experiences [01:08:40:00].

He is particularly excited about [[future_trends_in_ai_and_multimodal_models | AI applications in designing new products]] that might seem "out of left field," such as plant-based cheese, which can have a massive impact on sustainability and daily life [01:10:04:00]. He suggests that AI + non-technology domains will be where many exciting things happen [01:11:54:00].