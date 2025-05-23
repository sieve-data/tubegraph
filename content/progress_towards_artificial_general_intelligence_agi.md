---
title: Progress towards Artificial General Intelligence (AGI)
videoId: Wo95ob_s_NI
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Here is the modified article with inserted backlinks:

John Schulman, co-founder of OpenAI and leader of the post-training team, discusses the trajectory of AI capabilities, potential bottlenecks, safety considerations, and the path towards more general and powerful AI systems, including Artificial General Intelligence (AGI) [[artificial_general_intelligence_and_ai_systems | Artificial General Intelligence and AI Systems]].

## Current AI Capabilities and Foundations

Schulman explains that current AI models begin with **pre-training**, where they learn to imitate content from the internet, including websites and code, by predicting the next token (words or parts of words) <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>-<a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This process makes them "very calibrated" and able to assign probabilities to various content <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>-<a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. **Post-training** then narrows this broad capability, typically targeting a "chat assistant" persona that is helpful and task-oriented, optimizing for outputs humans find useful rather than just mimicking web content <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>-<a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

While current models are good chatbots, Schulman notes that on a "per token basis," they might be as smart as the smartest humans [[human_and_ai_intelligence_comparison | Human and AI Intelligence Comparison]]. The primary limitation preventing them from greater utility is their inability to maintain coherence and alignment with broader goals over extended periods, such as five minutes into a coding task <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>-<a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## Future Capabilities and Long-Horizon Tasks

Schulman anticipates significant improvements in AI capabilities within the next one to five years <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
Key advancements will likely involve:
*   **Performing more complex, involved tasks**: For example, carrying out an entire coding project, including writing files, testing, and iterating, based on high-level instructions <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>-<a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This requires the ability to act coherently for longer durations <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Training for longer projects**: This involves methods like Reinforcement Learning (RL) to learn how to carry out these tasks, whether supervised at the final output or at each step <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>-<a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a> [[reinforcement_learning_from_human_feedback_rlhf | Reinforcement Learning from Human Feedback (RLHF)]].
*   **Improved error recovery and generalization**: As models get better, they will become more adept at recovering from errors, dealing with edge cases, and getting "back on track" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>-<a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. Stronger models can generalize from fewer examples of error recovery seen in pre-training or diverse datasets <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>-<a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **Sample efficiency**: Better models won't require vast amounts of specific data to learn new skills or recover from errors <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>-<a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

Schulman suggests that the ability to handle longer-horizon tasks might not scale linearly with compute [[role_of_compute_in_ai_development | Role of Compute in AI Development]]. There could be "phase transitions" where certain capabilities unlock the ability to deal with much longer tasks, potentially using the same mental machinery for different timescales, similar to how humans plan <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>-<a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

## Potential Bottlenecks to AGI

Even if long-horizon coherence is achieved, Schulman identifies other potential "miscellaneous deficits" or bottlenecks that could prevent models from reaching human-level or AGI capabilities immediately <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>-<a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>:
*   **Thinking hard and attention**: Current models struggle to "really think hard about things or pay attention to what you ask them" <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>-<a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.
*   **Taste and ambiguity**: Human experts bring qualities like "taste" or better handling of ambiguity to tasks like research, which models might lack <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>-<a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Mundane limitations**: Issues around model affordances, such as the ability to use UIs, interact with the physical world, or access necessary information, could initially slow progress <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>-<a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a> [[ai_alignment_and_safety_concerns | AI Alignment and Safety Concerns]].

## The Prospect and Timeline of AGI

When asked if it's plausible that models could be human-level (like a colleague) by next year if long-horizon capabilities are unlocked, Schulman acknowledges it's hard to say what deficits will remain but doesn't expect improving coherence alone to achieve AGI <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>-<a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. However, he concedes it's "reasonable" to plan for the possibility of AGI very soon <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>-<a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a> [[future_of_agi_and_societal_implications | Future of AGI and Societal Implications]]. He personally estimates that AI might replace his job in about five years <a class="yt-timestamp" data-t="00:35:45">[01:35:45]</a>.

## Preparing for AGI: Safety and Coordination

If AGI were to arrive much sooner than expected (e.g., next year, or within two to three years <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>-<a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>), Schulman states OpenAI would:
*   **Be very careful**: This could involve slowing down training and deployment until safety and controllability are better understood, as current understanding is "rudimentary in a lot of ways" <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>-<a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Specific cautions**: This might mean not training an even smarter version, ensuring proper sandboxing, not deploying at scale, or being careful about the scale of deployment <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>-<a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

To manage such a scenario, especially if development is widespread:
*   **Coordination**: Schulman emphasizes the need for coordination among the relatively small number of entities capable of training the largest models. This would involve agreeing on reasonable limits to deployment or further training to avoid race dynamics that compromise safety <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>-<a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>, <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>-<a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.
*   **Purpose of a pause**: A pause in further training or deployment would be to ensure technical problems around alignment are sufficiently solved to deploy smart AIs safely, preventing catastrophic misuse and ushering in prosperity and scientific advancement <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>-<a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>, <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>-<a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a> [[ai_safety_and_existential_risks | AI Safety and Existential Risks]].

### Preferred Scenario: Incremental Progress
Schulman prefers a scenario of continuous, incremental releases of slightly better models, where safety and alignment improvements correspond with capability increases <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>-<a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>. This allows for slowing down if things look "scary" <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.

### Ensuring Safety with Powerful Models
If a discontinuous jump in capability occurs, proving safety before release would involve <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>:
*   **Extensive testing**: Simulated deployment and red teaming designed to be more likely to fail than real-world scenarios <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.
*   **Robust monitoring**: Systems to immediately detect if a deployed system starts to go wrong, potentially with another AI watching over deployed AIs <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>-<a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.
*   **Defense in depth**: Combining well-behaved models, resistance to misuse, and strong monitoring <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>-<a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.
*   **Evaluations during training**: Running many evaluations ("evals") during training to test for misbehavior (alignment, not turning against humans) and discontinuous jumps in capabilities <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>-<a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
*   **Safe training objectives**: Ensuring training data and objectives don't incentivize the model to turn against its creators. Schulman finds current RLHF methods, where the model aims to produce text pleasing to a human, feel very safe even with smart models <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>-<a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>. He is less concerned about instrumental convergence (e.g., taking over the world to write a Flask app) for well-specified tasks, though tasks like "make money" could be problematic <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>-<a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a> [[challenges_in_ai_alignment_and_potential_risks | Challenges in AI Alignment and Potential Risks]].

## Societal Integration and Alignment of Advanced AI

As AI becomes more capable, Schulman envisions:
*   **AI as helpful colleagues**: Models moving beyond one-off queries to assisting with entire projects, knowing context, and proactively suggesting next steps <a class="yt-timestamp" data-t="01:34:36">[01:34:36]</a>-<a class="yt-timestamp" data-t="01:35:36">[01:35:36]</a>.
*   **Humans as drivers**: Even with highly capable AI, humans should ideally remain the drivers of what AIs do, as AI doesn't necessarily have intrinsic desires unless programmed in <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>-<a class="yt-timestamp" data-t="01:06:58">[01:06:58]</a> [[potential_ai_takeover_scenarios_and_implications | Potential AI Takeover Scenarios and Implications]].

### Challenges of AI in the Economy
*   **AI running firms**: If AI-run firms outcompete those with humans in the loop, regulation might be needed to mandate human oversight for important decisions <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>-<a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>. Enforcing this globally would require international agreement or consensus among model providers <a class="yt-timestamp" data-t="01:08:59">[01:08:59]</a>-<a class="yt-timestamp" data-t="01:09:15">[01:09:15]</a>.
*   **Practical considerations**: AI-run firms might have higher tail risk due to malfunctions in very unusual situations, potentially incentivizing human oversight for practical reasons, at least in the near future <a class="yt-timestamp" data-t="01:09:41">[01:09:41]</a>-<a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a> [[impact_of_ai_on_economic_and_societal_structures | Impact of AI on Economic and Societal Structures]].

### Defining Alignment for Powerful Systems
For higher-stakes use cases, current RLHF methods might need rethinking <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>-<a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a> [[ai_alignment_and_cooperation_challenges | AI Alignment and Cooperation Challenges]]. OpenAI's **Model Spec** attempts to address this by considering multiple stakeholders <a class="yt-timestamp" data-t="01:12:16">[01:12:16]</a>:
1.  **End User**: Person interacting with the model.
2.  **Developer**: Person using the API.
3.  **Platform (OpenAI)**: Protecting against legal risks.
4.  **Rest of Humanity**: Broader societal impact.
5.  **(Future) The Model Itself**: Not yet a consideration.

The heuristic is to have models follow user/developer instructions but block usage that impinges on others' well-being, aiming for neutrality and avoiding paternalism <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>-<a class="yt-timestamp" data-t="01:14:49">[01:14:49]</a>. For very advanced models (GPT-6/7), alignment might involve a combination of written instructions (like an expanded Model Spec) and preference learning, as models can latch onto complex moral theories but still need guidance on specific styles or moralities <a class="yt-timestamp" data-t="01:24:59">[01:24:59]</a>-<a class="yt-timestamp" data-t="01:27:21">[01:27:21]</a> [[philosophical_perspectives_on_consciousness_and_free_will | Philosophical Perspectives on Consciousness and Free Will]].