---
title: Challenges and bottlenecks in selfdriving cars
videoId: Ctuf2Y0MrcA
---

From: [[redpointai]] <br/> 

The development of autonomous vehicles (AVs) presents both significant advancements and persistent [[challenges_and_opportunities_in_ai_development | challenges and opportunities in AI development]]. While there's a potential future where human-driven cars are seen as "crazy" given the accident rates and complexity <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>, achieving widespread, safe, and reliable self-driving capability still involves addressing several critical issues.

## Role of AI Models and Limitations
Waymo, a leader in self-driving technology, was developing its systems long before the recent explosion of large language models (LLMs) and diffusion models <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. These new models have not required Waymo to discard existing technology, but rather enhance it by providing a "better teacher" and more information to existing models <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

Key contributions of LLMs and Vision Models (VMS) to autonomous driving include:
*   **World Knowledge**: Providing semantic understanding of the environment, such as recognizing different types of emergency vehicles or understanding accident scenes, which might not be frequently encountered in collected driving data <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. This leverages external data sources like the web to enhance the driver's capabilities <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
*   **Reasoning Capabilities**: Large pre-trained models, with extensive visual and text data, enhance the system's ability to reason <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

However, these AI models are not a complete solution. There are aspects of self-driving that require capabilities beyond the AI model itself:
*   **Safety and Regulatory Compliance**: Strict contracts on safety and regulatory constraints must be expressed explicitly, not implicitly, outside the AI model <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>. An external layer verifies that the AI's proposed driving plan meets all safety and compliance requirements, ensuring the car behaves reasonably at all times <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>. This "checking layer" provides essential guardrails <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.

## Current State and Remaining Challenges

The current state of autonomous vehicles, particularly for companies like Waymo, shows "not many big blockers" in terms of fundamental capabilities <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>. Challenges like driving in fog or on highways have been largely addressed <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>. However, some areas like driving in snow are yet to receive full attention <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.

The predominant [[challenges_in_ai_adoption_and_deployment | challenges in AI adoption and deployment]] now revolve around **scaling** <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. Specifically, managing the "long tail of problems" that arise when self-driving cars operate for millions of miles <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>. Events a human driver might encounter once in a lifetime become weekly or monthly occurrences for an autonomous fleet, making "exceptional and weird" situations common <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>. Solving this long tail is a primary focus, with AI and large model capabilities expected to accelerate solutions <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

To address these rare "long-tail" scenarios, Waymo utilizes:
*   **Simulation**: Extensive use of simulation to synthesize scenarios that are known to potentially happen but rarely observed in real-world data <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.
*   **Scenario Modification**: Modifying real-world scenarios where "nothing really bad happened" to make them worse, such as introducing drunk or actively adversarial drivers, to make the system more robust and reactive <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>.

## Needed Technical Advances

One significant [[breakthroughs_in_autonomous_vehicle_technology | technical advance]] that could "completely yet again change the landscape" for autonomous driving is the development of **reliable, physically realistic World models** <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>. These models would allow for simulating the real world with physical realism and accurate rendering, akin to a "digital twin" of the world for AVs <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>.

While early "Proto-World models" like Sora or Veo can predict video sequences that seem physically reasonable <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>, the challenge lies in making them **controllable** and **physically realistic** while remaining rich and plausible <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>. Current models struggle with long-tail problems, as they are not yet good at generalizing to rare events <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.

A major bottleneck in World model building, especially for functional applications like autonomous driving, is the deep question of **causality** <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. While models can learn correlations and generate plausible videos, achieving controllability requires the model to understand causality – how an input change leads to a specific output <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>. Injecting causality into AI models has historically been a struggle in machine learning <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>. It's uncertain if this will require new architectures or simply proper data engineering and inductive biases <a class="yt-timestamp" data-t="46:46:00">[46:46:00]</a>.

## Sensor Suite Debate
Waymo uses a rich sensor suite of cameras, LiDAR, and radar, which are "remarkably complimentary" due to their orthogonal strengths and weaknesses, allowing for cross-verification <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>. This approach contrasts with other companies that started with simpler, cheaper L2 (driving assistance) systems and are attempting to climb to L4 (full autonomy) <a class="yt-timestamp" data-t="23:17:00">[23:17:00]</a>.

Waymo's strategy was to "possibly over-sensorize" initially to solve the hard problem and then inform decisions on cost reduction and simplification <a class="yt-timestamp" data-t="24:20:00">[24:20:00]</a>. The argument for using only cameras (like humans with eyes) is countered by the belief that the bar for L4 driving is "above human level" <a class="yt-timestamp" data-t="26:32:00">[26:32:00]</a>. Waymo's safety reports indicate they are already safer than the average human driver <a class="yt-timestamp" data-t="26:46:00">[26:46:00]</a>. The necessity of a complex sensor suite for superhuman performance remains a key question for the coming years <a class="yt-timestamp" data-t="27:31:00">[27:31:00]</a>.

## Milestones and Future Trajectory
The autonomous vehicle industry has a history of over-optimism, as evidenced by the 1995 transcontinental autonomous ride that achieved 99% autonomy, leading many to believe commercial deployment was imminent <a class="yt-timestamp" data-t="28:32:00">[28:32:00]</a>. It took 30 years to reach the point of commercial deployment <a class="yt-timestamp" data-t="29:17:00">[29:17:00]</a>.

Today, Waymo has validated its technology in cities like Phoenix and San Francisco, and user feedback indicates strong product love <a class="yt-timestamp" data-t="29:32:00">[29:32:00]</a>. The main barrier remaining is scaling <a class="yt-timestamp" data-t="30:09:00">[30:09:00]</a>. Therefore, the next major milestones will be focused on **expansion** into various geographies, such as Waymo's initial data collection and left-side driving experiment in Tokyo <a class="yt-timestamp" data-t="30:16:00">[30:16:00]</a>. This involves not just technological adaptation but also managing the logistics of setting up operations and building trust with local communities and regulators <a class="yt-timestamp" data-t="21:36:00">[21:36:00]</a>.