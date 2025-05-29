---
title: Challenges and advancements in autonomous driving
videoId: 2WmczROXzco
---

From: [[jimruttshow8596]] <br/> 

This article explores the landscape of autonomous driving technology, focusing on the approaches, challenges, and future visions presented by George Hotz, founder of comma.ai <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## George Hotz: Background and Motivation

George Hotz, a precocious individual selected for the Johns Hopkins Center for Talented Youth, gained early recognition in hacker circles <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>. At age 17, he was the first to break the carrier lock on the iPhone <a class="yt-timestamp" data-t="01:24:25">[01:24:25]</a>. Later, he was recruited into Google's Project Zero, an elite team of white-hat hackers tasked with finding "zero-day" exploits in widely distributed technologies <a class="yt-timestamp" data-t="02:20:53">[02:20:53]</a>. A zero-day exploit is a previously unknown vulnerability in software <a class="yt-timestamp" data-t="02:53:30">[02:53:30]</a>. Hotz's work at Project Zero led him to think about automating vulnerability discovery, a recurring theme in his life <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. This desire for automation eventually motivated him to found comma.ai <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

Hotz initially considered a contract to build software for Tesla to replace the Mobileye chip, which Intel later acquired <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. When that contract didn't materialize, he decided to build an autopilot clone himself, intending to sell it to car companies <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. Building the clone took a couple of months, but selling it to car companies proved impossible <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. Mobileye chips run proprietary perception algorithms to detect lane lines and cars, enabling Advanced Driver-Assistance Systems (ADAS) features <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.

## Core Philosophy: Camera-Only Approach

A key philosophical fork in autonomous driving technology is between those who believe it can be achieved with only cameras and those who advocate for additional sensing systems like LiDAR <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. Hotz firmly believes in the camera-only approach, drawing an analogy to human driving:
> "There's one system that can drive cars and its human beings... A human has two cameras" <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.

This aligns with Elon Musk's contrarian viewpoint against LiDAR <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>. Hotz asserts this is now the "correct" viewpoint, though Waymo still utilizes LiDAR <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

## Levels of Self-Driving Automation

The six levels of self-driving automation (Level 0 through Level 5) often describe liability rather than capability <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.
*   **Level 2**: The human driver is still fully liable for the car's decisions <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. It entails supervision of the car <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
*   **Level 3**: The human is liable in certain scenarios <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.
*   **Level 4**: The human is not liable in specific, defined regions, such as cities <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.
*   **Level 5**: The human is never liable, implying full automation where one could sleep in the back seat <a class="yt-timestamp" data-t="07:47:00">[07:47:47]</a>.

Hotz views predictions of full automation (Level 5) being "two years away" as hubris, referencing Google's early prototype without a steering wheel <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.

## Human Driving: A Tough Benchmark

Humans are surprisingly good drivers <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. In most civilized countries, there's about one fatality per 100 million miles driven <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>. This performance sets a very high bar for autonomous systems <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. Hotz emphasizes that humans are "absurdly good drivers," noting that most people drive thousands of times without a crash <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

## Addressing [[challenges_of_ai_modeling_and_simulation | Challenges of AI Modeling and Simulation]]

### The Behavioral Cloning Problem
Initial attempts to build self-driving software involved using a camera to predict steering wheel angle via supervised learning (f(x)=y, where x is the image and y is the steering angle) <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. This approach failed on the road despite low training and test set loss <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. The reason is the "behavioral cloning" problem: the model is not acting in the world during training <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. Data is collected from human driving ("human policy"), but the machine's slight errors ("Epsilon error") accumulate over time because actions at time T affect input data at time T+1, violating the Independent and Identically Distributed (IID) assumption <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>.

### Solution: Simulation and Corrective Pressure
To address this, comma.ai initially added a small amount of corrective pressure by detecting lane lines and adjusting based on the car's position <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>. However, the reliance on lane lines was problematic due to their ambiguous definition and lack of a physics-based standard <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>. They eventually removed the dependency on lane lines <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.

The ultimate solution for behavioral cloning is training in simulation <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>. In a simulator, the model trains with data driven by its own policy, allowing it to learn how to correct itself and converge <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>. They use a "hugging test" in an Unreal Engine simulator to measure how quickly the car returns to the center of a lane after being initialized off-center <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>.

### Data Collection and Unique Simulation Approach
comma.ai boasts the second-largest driving dataset globally after Tesla, with 10,000 weekly active users uploading data, resulting in tens of millions of diverse miles <a class="yt-timestamp" data-t="19:12:00">[19:12:00]</a>. Unlike Waymo's hand-coded game engine simulator, comma.ai's "small offset simulator" is reprojective <a class="yt-timestamp" data-t="19:45:00">[19:45:00]</a>. It takes human video and applies small geometric perturbations to simulate driving in slightly different positions, addressing the challenge of modeling other cars' behavior <a class="yt-timestamp" data-t="19:50:00">[19:50:50]</a>.

## comma.ai's Product and Capabilities

comma.ai offers an [[opensource_selfdriving_car_technology | opensource selfdriving car technology]] system called Openpilot <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. The comma 3x device, costing $1250 <a class="yt-timestamp" data-t="23:06:00">[23:06:00]</a>, supports 275 car models <a class="yt-timestamp" data-t="21:03:00">[21:03:00]</a>. Installation is simple: it involves unplugging a camera cable behind the rearview mirror, using a Y-splitter, and plugging in the comma device. This process takes about 15 minutes <a class="yt-timestamp" data-t="21:31:00">[21:31:00]</a>. The device is not "hacking" the car; it intercepts and improves messages from the car's existing camera system <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. It selectively blocks or passes messages, ensuring emergency braking remains active by default <a class="yt-timestamp" data-t="22:17:00">[22:17:00]</a>.

The system significantly enhances existing driver assistance <a class="yt-timestamp" data-t="23:55:00">[23:55:00]</a>. Instead of just keeping a car within lane lines (which can be jerky), comma.ai applies smooth torque to keep the car centered, even on unmarked roads, emulating human driving <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>. On interstate highways, it can drive for an hour or more without human intervention <a class="yt-timestamp" data-t="24:50:00">[24:50:00]</a>. An experimental mode can handle city driving, stopping at stop signs and lights, performing 90-degree turns and highway interchanges <a class="yt-timestamp" data-t="25:05:00">[25:05:00]</a>.

## [[comparison_between_commaai_and_competitors_like_tesla_and_waymo | Comparison Between Comma.ai and Competitors Like Tesla and Waymo]]

### Waymo
Waymo's approach relies on super high-resolution mapping and operates in defined, carefully mapped regions, characteristic of a Level 4 system <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>. Hotz describes Waymo's vehicles as "trackless monorails" due to their reliance on centralized infrastructure and remote operation <a class="yt-timestamp" data-t="28:46:00">[28:46:00]</a>. Their systems require multiple operators for each car and stop if the cell phone network goes down, highlighting their fragility and centralization <a class="yt-timestamp" data-t="29:36:00">[29:36:00]</a>. Waymo has "hilariously negative unit economics" with their $500,000 robo-taxis, making them vulnerable to cheaper, decentralized solutions <a class="yt-timestamp" data-t="32:18:00">[32:18:00]</a>. As of December 2023, Waymo had only logged 7 million miles in no-driver mode <a class="yt-timestamp" data-t="30:30:00">[30:30:00]</a>.

### Tesla
Tesla also uses a camera-only approach and processes most data locally on the vehicle, without remote assistance <a class="yt-timestamp" data-t="39:08:00">[39:08:00]</a>. However, Tesla trains its models in data centers, similar to comma.ai <a class="yt-timestamp" data-t="39:14:00">[39:14:16]</a>. Tesla applies significantly more CPU power (about 100x more) to the real-time problem than comma.ai, using dedicated silicon and consuming more power <a class="yt-timestamp" data-t="35:16:00">[35:16:00]</a>. Tesla has a larger dataset, with an estimated 3.3 billion miles logged for autopilot, compared to comma.ai's over 100 million <a class="yt-timestamp" data-t="40:35:00">[40:35:00]</a>.

From a functional standpoint, Tesla has more high-end capabilities and can execute complex maneuvers like navigating intersections and making turns at lights <a class="yt-timestamp" data-t="37:56:00">[37:56:00]</a>. However, Tesla's system can make "sketchy mistakes," such as phantom braking or misinterpreting lanes, leading to jarring experiences for the user <a class="yt-timestamp" data-t="36:22:00">[36:22:00]</a>. Hotz attributes this to Tesla's more rigid, "modernist" approach, relying on object localization and Model Predictive Control (MPC) planners, which can snap between local minima, causing abrupt actions <a class="yt-timestamp" data-t="38:19:00">[38:19:00]</a>.

In contrast, comma.ai's system is focused on "making driving chill" <a class="yt-timestamp" data-t="37:09:00">[37:09:00]</a>. Their torque limits are lower, resulting in smoother, safer driving <a class="yt-timestamp" data-t="36:43:00">[36:43:00]</a>. When overwhelmed, comma.ai's system becomes "shaky and unsure," similar to human failure modes, rather than jerking the wheel or slamming brakes <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>.

## [[legal_and_regulatory_aspects_of_autonomous_vehicles | Legal and Regulatory Aspects of Autonomous Vehicles]]

comma.ai operates as a Level 2 system <a class="yt-timestamp" data-t="41:14:00">[41:14:00]</a>. In the U.S. automotive industry, manufacturers self-certify compliance with standards <a class="yt-timestamp" data-t="42:41:00">[42:41:00]</a>. comma.ai self-certifies compliance with ISO 26262 and other standards, particularly regarding torque limits and braking force <a class="yt-timestamp" data-t="42:53:00">[42:53:00]</a>.

For a Level 2 system, the human remains in control of the vehicle at all times <a class="yt-timestamp" data-t="43:16:00">[43:16:00]</a>. comma.ai guarantees that the car will never become uncontrollable; users can always use the brakes or overpower the steering <a class="yt-timestamp" data-t="43:21:00">[43:21:00]</a>. If a crash occurs, the liability lies with the human driver <a class="yt-timestamp" data-t="43:37:00">[43:37:00]</a>.

comma.ai also implements a driver monitoring system, which uses a camera to ensure the driver's eyes are on the road at all times <a class="yt-timestamp" data-t="44:03:00">[44:03:00]</a>. This system is designed to be non-intrusive and provide helpful alerts, preventing alert fatigue <a class="yt-timestamp" data-t="44:40:00">[44:40:00]</a>. Telemetry data is opt-out, but users are encouraged to upload it as a "common good" to improve the system <a class="yt-timestamp" data-t="45:37:00">[45:37:00]</a>.

Hotz emphasizes that comma.ai's system is designed not to be an insurance company and has no interest in taking liability beyond Level 2 <a class="yt-timestamp" data-t="48:40:00">[48:40:00]</a>. While their software could potentially enable a 10x reduction in accidents, the decision to provide a Level 5 liability layer is left to others who might use their open-source software <a class="yt-timestamp" data-t="49:01:00">[49:01:00]</a>.

## [[future_directions_and_challenges_for_ai_and_agi | Future Directions and Challenges for AI and AGI]]

Hotz views self-driving cars as a stepping stone to [[future_directions_and_challenges_for_ai_and_agi | general-purpose robotics]] <a class="yt-timestamp" data-t="40:08:00">[40:08:00]</a>. While self-driving cars are a significant narrow AI problem, they are easier than general robotics because:
1.  It's simpler to gather large datasets of good driving from the car's perspective <a class="yt-timestamp" data-t="46:32:00">[46:32:00]</a>.
2.  Driving is a low-dimensional problem (steering and acceleration), unlike a multi-dimensional robot arm <a class="yt-timestamp" data-t="46:56:00">[46:56:00]</a>.

The long-term dream for comma.ai is to sell a "comma body"—a $25,000 robot companion capable of cooking and cleaning <a class="yt-timestamp" data-t="47:34:00">[47:34:00]</a>.

Hotz also leads Tinygrad, a machine learning framework that competes with TensorFlow and PyTorch <a class="yt-timestamp" data-t="55:55:00">[55:55:00]</a>. Tinygrad distinguishes itself by its extreme simplicity, with a codebase of only 5200 lines, yet capable of running complex models like stable diffusion and Llama <a class="yt-timestamp" data-t="56:11:00">[56:11:00]</a>. Its simplicity is designed to facilitate translation to custom hardware (ASICs) <a class="yt-timestamp" data-t="57:08:00">[57:08:00]</a>. Tinygrad is already used in Openpilot to run models on the device <a class="yt-timestamp" data-t="57:29:00">[57:29:00]</a>.