---
title: Comparison between commaai and competitors like Tesla and Waymo
videoId: 2WmczROXzco
---

From: [[jimruttshow8596]] <br/> 

comma.ai is a company founded by George Hotz that offers an [[opensource_selfdriving_car_technology | open-source self-driving car system]] <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This system aims to enable cars to drive autonomously using an approach that differs significantly from competitors like Waymo and Tesla <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## Core Philosophy and Approach

comma.ai's core philosophy for autonomous driving is based on emulating human driving behavior using only cameras <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. The company believes that humans, who only have two cameras (eyes), are the only truly Level 5 capable driving system <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Their system, known as Openpilot, is designed to make driving "chill" <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a>.

Instead of relying on high-precision maps or additional sensors like LiDAR, comma.ai focuses on predicting "where a human drive the car" given the road conditions <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a> <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>. This approach is more holistic and aims to determine the action rather than building a detailed "world model" with precise localization of objects <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

A key aspect of comma.ai's development is its use of a massive, diverse dataset collected from its 10,000 weekly active users who upload driving data <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a> <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. This dataset is the second largest in the world after Tesla's <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. They also use a unique "small offset simulator" that perturbates human video data rather than relying on a hand-coded game engine <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

## Comparison with Waymo

Waymo's approach to self-driving cars is distinct from comma.ai's:
*   **Sensor Suite**: Waymo utilizes LiDAR and other "more penetrative sensing systems" in addition to cameras <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Mapping**: Waymo invests heavily in "super high resolution mapping" <a class="yt-timestamp" data-t="00:26:48">[00:26:48]</a>, aiming for centimeter-level precision <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>. This is seen as a "super fragile" system by Hotz <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.
*   **Operating Domain**: Waymo operates as a Level 4 system, meaning it functions within defined, carefully mapped regions <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>. Hotz describes them as "trackless monorails" operating with "virtual rails" <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
*   **Remote Control**: Waymo and Cruise cars frequently rely on human operators making decisions from a call center <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a> <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>. Their dependence on cellular networks means they stop if connectivity is lost <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>.
*   **Unit Economics**: Waymo has "hilariously negative unit economics," with Robo-taxis potentially costing $500,000 <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a> <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>. This contributes to the [[impact_of_ai_advancements_on_various_industries | economic non-viability]] of their approach, leading to a "race to the bottom" in the market <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a> <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.
*   **Miles Driven**: As of December 2023, Waymo had driven only 7 million miles in no-driver mode <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a> <a class="yt-timestamp" data-t="00:40:26">[00:40:26]</a>. In contrast, comma.ai has driven over 100 million miles <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.

## Comparison with Tesla

Tesla's Full Self-Driving (FSD) system shares more similarities with comma.ai than Waymo:
*   **Sensor Suite**: Both rely primarily on cameras, with Tesla famously denouncing LiDAR <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Unit Economics**: Both Tesla and comma.ai are profitable businesses selling products to consumers today <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a> <a class="yt-timestamp" data-t="00:34:11">[00:34:11]</a>.
*   **Local Processing**: Both systems process data and run their models locally on the car's device, without relying on real-time internet connectivity for driving decisions <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a> <a class="yt-timestamp" data-t="00:39:08">[00:39:08]</a>.
*   **Miles Driven**: Tesla has logged an estimated 3.3 billion miles in engaged autopilot mode, significantly more than comma.ai's 100 million miles and Waymo's 7 million miles <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a> <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.

Despite these similarities, key differences exist:
*   **Computational Power**: Tesla's system uses about 100x more CPU power than comma.ai's comma 3X device <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>. Tesla also trains on 4,000 GPUs compared to comma.ai's 40 GPUs <a class="yt-timestamp" data-t="00:35:49">[00:35:49]</a>.
*   **Functional Capability vs. Usability**:
    *   **Tesla**: Has greater "high-end capabilities" and can navigate complex scenarios like right turns at lights and highway interchanges without disengagement <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a> <a class="yt-timestamp" data-t="00:37:47">[00:37:47]</a>. However, its driving experience is often described as "jarring" and prone to "sketchy mistakes" like phantom braking or mis-tracking lanes <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a> <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>. Tesla's failure modes are more abrupt, akin to a "powerful optimizer" snapping between local minima <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>.
    *   **comma.ai**: While not as feature-rich in complex urban navigation, comma.ai focuses on a "smooth driving is safe driving" principle <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>. Its system is designed to be "chill" and can drive for hours on highways without intervention <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>. When overwhelmed, comma.ai's system becomes "shaky and unsure," a more human-like failure mode <a class="yt-timestamp" data-t="00:38:16">[00:38:16]</a>.
*   **Underlying Algorithms**: Tesla's "end-to-end" approach still relies on a "rigid MPC (Model Predictive Control) cost-based planner" <a class="yt-timestamp" data-t="00:38:26">[00:38:26]</a>. comma.ai's latest model directly predicts where a human would drive <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **Marketing**: Tesla's "full self-driving" label is seen as "nuts" and "overselling" compared to comma.ai's more cautious approach <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>.

## [[legal_and_regulatory_aspects_of_autonomous_vehicles | Legal and Regulatory Aspects]]

The "levels of self-driving automation" (Level 0 through Level 5) primarily dictate liability rather than capability <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Level 2**: Human is still fully liable for decisions <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Level 3**: Human is liable in certain scenarios <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Level 4**: Human is not liable in specific operational design domains (e.g., cities) <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Level 5**: Human is never liable, representing full automation <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

comma.ai explicitly states it has "no interest in ever going past Level 2" or taking on liability <a class="yt-timestamp" data-t="00:48:39">[00:48:39]</a>. They self-certify compliance with automotive standards and ensure their system never makes the car uncontrollable <a class="yt-timestamp" data-t="00:42:43">[00:42:43]</a> <a class="yt-timestamp" data-t="00:43:17">[00:43:17]</a>. The user is always in control, with the ability to easily override the system <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>. A driver monitoring camera ensures the user keeps their eyes on the road <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>.

The company's stance on liability is that "the human is in control of the car at all times" <a class="yt-timestamp" data-t="00:50:21">[00:50:21]</a>, and therefore, the human is responsible for any incidents <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>. This contrasts with companies aiming for higher levels of autonomy, where liability shifts away from the driver.

## [[challenges_and_advancements_in_autonomous_driving | Technical Challenges and Advancements]]

One of the initial [[challenges_and_advancements_in_autonomous_driving | challenges]] faced by comma.ai was the "behavioral cloning problem" <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. A model trained on human driving data (supervised learning) fails to drive in the real world because small "Epsilon errors" accumulate over time, leading to divergence <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This occurs because the training data is based on human policy, not machine policy, violating the Independent and Identically Distributed (IID) assumption of machine learning <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

comma.ai addressed this by adding a "corrective pressure" based on lane lines, though these were eventually removed as a non-physics-based and ambiguous definition <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a> <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. The core solution involves training in simulation, where the model's own policy generates data, allowing it to learn to correct itself and converge <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

Hotz dismisses the common criticism from AI gurus like Gary Marcus that autonomous driving is impossible due to "a zillion corner cases" <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. He argues that even rare corner cases are abundant in datasets of hundreds of millions of miles, and humans operate with far less data <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. The problem is not a lack of "general intelligence" – a "meaningless term" – but rather the accumulation of errors over time and the current lack of a robust integrated "world model" that humans possess <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a> <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

Recent advancements in Transformers are enabling new simulator technologies, including comma.ai's move to a "third Paradigm" that is more generic <a class="yt-timestamp" data-t="00:48:04">[00:48:04]</a> <a class="yt-timestamp" data-t="00:54:56">[00:54:56]</a>. The company also utilizes Tinygrad, a simplified machine learning framework, to train and deploy models efficiently on various hardware <a class="yt-timestamp" data-t="00:55:58">[00:55:58]</a> <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>.

## Future Vision

comma.ai views self-driving cars as a "stepping stone" to general purpose robotics and "artificial life" <a class="yt-timestamp" data-t="00:54:49">[00:54:49]</a> <a class="yt-timestamp" data-t="00:39:54">[00:39:54]</a>. While driving is a "narrow AI" problem <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>, its relative ease of data collection and low dimensionality make it a good starting point for building more complex systems, such as a "robot companion" capable of making sandwiches and cleaning <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a> <a class="yt-timestamp" data-t="00:47:28">[00:47:28]</a>. The ultimate goal is to build software that is a "10x better driver than a human" <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>.