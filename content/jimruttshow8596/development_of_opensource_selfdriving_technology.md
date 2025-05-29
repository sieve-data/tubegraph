---
title: Development of opensource selfdriving technology
videoId: 2WmczROXzco
---

From: [[jimruttshow8596]] <br/> 

Comma.ai, founded by George Hotz, is a company developing an open-source self-driving car system [00:03:57]. The company aims to make advanced driver-assistance systems widely accessible and improve upon existing technologies through a human-centric, open-source approach [00:03:57].

## Early Influences and Motivation
George Hotz gained early recognition in hacker circles for being the first person to break the carrier lock on the iPhone at age 17 [00:01:23]. He later worked at Google's Project Zero, an elite team of white-hat hackers focused on finding "zero-day" exploits in widely distributed or critical infrastructure technologies [00:02:21]. A zero-day exploit is a previously unknown vulnerability in a piece of software [00:02:56]. Hotz's time at Project Zero led him to consider how to automate the process of finding vulnerabilities, inspiring his pursuit of software that could automate tasks, leading to his interest in AI [00:03:05].

The motivation for Comma.ai originated from a failed contract discussion with Elon Musk to build software for Tesla that could replace the Mobileye chip [00:04:41]. This experience led Hotz to decide to build an "autopilot clone" and sell it to car companies independently [00:05:13]. While building the software was relatively quick (a couple of months), selling it to car companies proved "impossible" [00:05:22].

## Comma.ai's Technological Approach

### Camera-Based Systems vs. Lidar
One of the key distinctions in [[advances_and_challenges_in_selfdriving_car_technology | self-driving car technology]] approaches is the debate between camera-only systems and those that integrate Lidar or other "penetrative sensing systems" [00:06:05]. Comma.ai, like Tesla, aligns with the camera-only approach, emphasizing that human beings, the only current system capable of Level 5 self-driving, only use two cameras (eyes) [00:06:20].

### Data-Driven Development
Comma.ai leverages a vast dataset for its development. The company possesses the second-largest driving dataset globally, after Tesla, with tens of millions of miles of diverse data collected from 10,000 weekly active users who upload data to them [00:19:12]. This diversity contrasts with companies like Waymo, which often collect data from limited geographic areas [00:19:30]. Despite the large dataset, Comma.ai typically only trains on about 5% of its data to allow for faster iteration due to diminishing returns [00:41:18].

### The "Behavioral Cloning" Problem
Initially, Comma.ai attempted a straight "supervised learning" approach where a camera would predict the steering wheel angle (f(x) = y, where x is the image and y is the steering angle) [00:10:46]. This approach failed because even with a great training set, the model would drift [00:11:04]. The core issue is that during training, the data is based on human driving ("human policy"), but when the machine takes control ("machine policy"), small errors accumulate over time due to temporal dependence of samples (IID samples are not truly IID) [00:11:17].

To address this, Comma.ai first added a "corrective pressure" algorithm that detected lane lines and centered the car [00:15:15]. However, the subjective nature of defining "lane lines" (where 50% of humans might disagree on their presence) led them to eventually remove reliance on lane lines from their system [00:15:38].

The solution to this "behavioral cloning" problem was to train in simulation using a "small offset simulator" [00:17:25]. This simulator reprojects human videos, allowing for small geometrical perturbations to simulate scenarios where the car deviates from the human-driven path [00:19:50]. This allows the model to learn corrective pressure and converge back to the desired path [00:18:11]. This contrasts with fully flexible game engine simulators that face challenges in simulating the behavior of other cars [00:20:09].

### World Model and Corner Cases
Hotz dismisses the criticism that [[advances_and_challenges_in_selfdriving_car_technology | self-driving cars]] will fail due to "a zillion corner cases" [00:12:43]. He argues that human drivers have seen far less data than modern systems are trained on [00:13:06]. Hotz suggests that incidents like the Uber self-driving car fatality were more indicative of classical software bugs (e.g., misclassification of an object as "unknown") rather than a failure of deep learning or an inability to handle corner cases [00:14:10]. While acknowledging that current systems lack the integrated "world model" and generalization capabilities of humans, this remains an area of active research in machine learning [00:14:40].

## Comma.ai's Product: The Comma 3X

The Comma 3X is a small device, costing $1250, that integrates into existing cars [00:23:06]. Installation is simple: it involves unplugging a camera cable behind the rearview mirror, using a Y-splitter to connect the Comma 3X, and plugging the original cable back in [00:21:42]. This process typically takes about 15 minutes [00:21:52].

The device works by intercepting and modifying messages sent by the car's existing camera system, effectively overriding the car's default lane-keeping assist messages to provide superior lane centering [00:21:59]. It maintains essential safety features like emergency braking by default [00:22:19].

### Capabilities
The system aims to make driving "chill" [00:37:10]. On interstate highways, it can typically drive for an hour without human intervention [00:24:53]. An experimental mode allows it to handle town driving, including stopping at stop signs and traffic lights, though it is acknowledged to be "a little worse than Tesla FSD" in urban environments [00:25:07]. Comma.ai's system is designed to provide smooth driving by applying less torque to the steering wheel compared to Tesla's system, leading to a less "jarring" experience for the user [00:36:51].

Currently, Comma.ai supports over 275 car models [00:21:00]. It does not use high-precision maps, relying instead on standard-definition maps similar to what a human would use, adhering to the philosophy that computers don't need "special stuff" beyond what humans use [00:26:06].

## Self-Driving Levels and Liability

The six levels of [[legal_and_regulatory_issues_for_selfdriving_tech | self-driving automation]] (Level 0 through Level 5) are often seen by George Hotz as more related to liability than actual capability [00:07:20].
*   **Level 2**: The human driver remains fully liable for decisions made by the car [00:07:25].
*   **Level 3**: Human is liable in certain scenarios [00:07:39].
*   **Level 4**: Human is not liable in specific, defined areas [00:07:43].
*   **Level 5**: The human is never liable [00:07:47].

Comma.ai explicitly states it has "no interest in ever going past Level 2" or taking on liability [00:48:39]. Their primary promise is that the car will never become uncontrollable; the driver can always override the system by steering or braking [00:49:52]. While Comma.ai encourages users to keep their eyes on the road at all times and employs a driver monitoring camera to ensure this, it does not officially dictate hands-on-wheel requirements, although it limits the maximum torque applied to the wheel [00:43:43].

Hotz's philosophy is that "the human is in control of the car at all times" [00:50:21]. This implies that if a crash occurs while using Comma.ai's software, the human driver is liable, similar to how power steering doesn't bear liability for a driver's actions [00:50:06]. Comma.ai does, however, distinguish between judgment calls and "functional safety" issues, such as a mechanical failure caused by their product, for which they would be liable [00:53:24].

## Comparison with Competitors

### Waymo and Cruise
Hotz views Waymo and Cruise as "fancy remote-control cars" rather than truly autonomous robots [00:06:24]. He characterizes them as "trackless monorails" operating in carefully mapped, defined regions (Level 4), and criticizes their high cost ($500,000 per robotaxi for Waymo) and reliance on centralized infrastructure, including constant cell phone network connectivity for human "operators" [00:26:54]. He argues that their business model assumes a static world without competition, which is unrealistic [00:32:46].

### Tesla
Tesla's approach is more analogous to Comma.ai's, focusing on selling products to consumers with positive unit economics [00:33:34]. Both Comma.ai and Tesla train their models in data centers, but the model then operates entirely locally on the car's hardware [00:39:10]. Tesla's system is estimated to use about 100 times more CPU power than Comma.ai's Comma 3X [00:35:27].

While Tesla may have more "high-end capabilities" and can execute more complex maneuvers like making right turns at lights, Comma.ai claims superiority in "usability" and providing a "chill" driving experience [00:35:56]. Tesla's system is known for "sketchy mistakes" like sudden braking or misidentifying lanes, which can be "jarring" for the user, whereas Comma.ai's system tends to become "shaky and unsure" when overwhelmed, which Hotz describes as more "humanlike" failure modes [00:36:19].

## Future Vision

George Hotz sees [[advances_and_challenges_in_selfdriving_car_technology | self-driving cars]] as a significant, albeit narrow, [[progress_and_direction_towards_developing_agi | AI problem]], serving as a "stepping stone" to more general-purpose robotics and "artificial life" [00:39:54]. The goal is to apply lessons learned from the relatively low-dimensional and data-rich domain of driving to higher-dimensional problems like general robotics (e.g., a robot making a sandwich) [00:46:21]. The long-term dream for Comma.ai is to sell a "comma body" – a $25,000 robot companion capable of cooking and cleaning [00:47:34].

## Tinygrad
Hotz is also the CEO of Tinygrad, an open-source machine learning framework [00:55:55]. Tinygrad aims to be a 100x simpler alternative to frameworks like TensorFlow and PyTorch, with a codebase of only 5200 lines [00:56:11]. It supports various hardware and can run complex models like Stable Diffusion and Llama [00:56:21]. Tinygrad's simplicity and generic approach to devices, data types, and operations make it highly adaptable and easy to port to new systems, including embedded devices and microcontrollers [00:56:44]. The long-term goal of Tinygrad is to build machine learning ASICs (Application-Specific Integrated Circuits), focusing on software first to inform hardware design and reduce reliance on third-party solutions for [[ai_security_and_reducing_dependency_on_third_parties | AI security]] [00:57:11]. Tinygrad is already used within Comma.ai's Openpilot to run models on devices [00:57:29].

For more information, visit Comma.ai at comma.ai or Tinygrad at tinygrad.org [00:58:00].