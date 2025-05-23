---
title: AI's economic impact and the future of white-collar work automation
videoId: 64lXQP6cs5M
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The rapid advancements in Artificial Intelligence (AI), particularly in language models, are poised to have a significant economic impact, primarily through the automation of white-collar tasks. This article outlines the predicted timelines, mechanisms, economic shifts, and societal adaptations discussed in a recent podcast episode featuring Sholto Douglas and Trenton Bricken from Anthropic.

## Timelines for White-Collar Automation

Predictions for the automation of white-collar work vary by task complexity and the specificity of the application, but a general trend towards significant automation in the near future is anticipated.

### Software Engineering
Software engineering is identified as one of the first areas to see substantial automation.
*   Conclusive evidence of real software engineering agents doing real work is expected by the end of the current year (stated as 2025 in the podcast) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   Within the next year, software engineering agents are predicted to be capable of performing close to a day's worth of work for a junior engineer, or a couple of hours of competent, independent work <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   This rapid progress is partly due to the verifiable nature of software engineering (e.g., code compilation, passing tests), which lends itself well to Reinforcement Learning (RL) with clean reward signals [[reinforcement_learning_rl_in_language_models_and_its_impact_on_software_engineering]] <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   The development of tools like Claude Code <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a> and GitHub integrations for AI [[the_future_of_programming_and_ai_tools_like_github_copilot]] <a class="yt-timestamp" data-t="01:34:44">[01:34:44]</a> will facilitate async work dispatch to AI agents, moving beyond human-in-the-loop IDE work <a class="yt-timestamp" data-t="01:35:38">[01:35:38]</a>.

### General Computer Use and Specific White-Collar Tasks
Beyond software engineering, automation is expected for a range of general computer-based tasks.
*   **Photoshop:** By May of the following year (2026), it's predicted that AI will be able to perform sequential effects in Photoshop, including selecting specific parts of a photo <a class="yt-timestamp" data-t="01:05:21">[01:05:21]</a>.
*   **Flight Booking:** This task is expected to be "totally solved" by the same timeframe [[future_of_ai_interaction_in_everyday_life_and_personalization]] <a class="yt-timestamp" data-t="01:05:34">[01:05:34]</a>.
*   **Planning (e.g., weekend getaways):** Models are already capable of this to some extent, but reliability is the main hurdle <a class="yt-timestamp" data-t="01:05:46">[01:05:46]</a>. An internal demo showed an AI successfully planning a camping trip, navigating a US government booking site, and considering weather patterns [[ai_systems_and_planning_mechanisms]] <a class="yt-timestamp" data-t="01:06:09">[01:06:09]</a>.
*   **Taxes and Visas:**
    *   Autonomously doing taxes with a high degree of trust is *not* expected by May 2026 <a class="yt-timestamp" data-t="01:08:49">[01:08:49]</a>. However, AI is expected to be able to click through TurboTax and fill out boxes by then <a class="yt-timestamp" data-t="01:09:04">[01:09:04]</a>.
    *   By the end of 2026, AI is predicted to reliably handle tasks like filling out receipts for company expense reports [[the_future_of_programming_and_ai_tools_like_github_copilot]] <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. The ability to perform the entire tax process (including inbox searching and expense categorization) by end of 2026 depends on whether someone at an AI lab prioritizes this specific application for RL <a class="yt-timestamp" data-t="01:10:33">[01:10:33]</a>.
    *   By the end of 2026, AI is expected to have enough awareness to bring attention to areas where it feels unreliable <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

### The "Drop-in White-Collar Worker"
A significant milestone will be the emergence of AI as a "drop-in white-collar worker."
*   This is considered very likely within two years, and "almost overdetermined in five" [[impact_of_ai_on_software_development_and_productivity]] <a class="yt-timestamp" data-t="01:57:19">[01:57:19]</a>, <a class="yt-timestamp" data-t="01:57:29">[01:57:29]</a>.
*   This level of automation is anticipated even if algorithmic progress stalls, provided enough of the right kinds of data are available, as the economic incentive is overwhelmingly strong <a class="yt-timestamp" data-t="02:03:39">[02:03:39]</a>, <a class="yt-timestamp" data-t="02:03:44">[02:03:44]</a>. Even if every task needs to be "hand spoon-fed" to the model, it's considered economically worthwhile [[challenges_and_opportunities_in_deploying_ai_at_scale]] <a class="yt-timestamp" data-t="02:03:20">[02:03:20]</a>.

## Mechanisms Enabling Automation

Several factors are driving these automation capabilities:
*   **Reinforcement Learning (RL) with Verifiable Rewards:** A major breakthrough has been RL from Verifiable Rewards, or RL with a clean reward signal (e.g., passing unit tests in coding, correct math answers) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This is more effective than RL from human feedback (RLHF), as humans can be poor judges and have biases <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Feedback Loops:** The ability to give models a good feedback loop is crucial for performance <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. If a task can be structured with such a loop, models tend to perform well; otherwise, they struggle [[ai_alignment_and_potential_risks]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Data Availability:**
    *   For many white-collar tasks, especially computer use, the challenge is representing everything in the token input space for the model [[challenges_and_methodologies_in_ai_training_and_data_usage]] <a class="yt-timestamp" data-t="01:02:55">[01:02:55]</a>.
    *   The existence of vast datasets like GitHub for software engineering has accelerated progress in that domain. A similar abundance of data for other tasks (e.g., "mocap of everyone's actions") could solve robotics at a similar rate to software engineering <a class="yt-timestamp" data-t="02:05:12">[02:05:12]</a>.
*   **Tooling and Integration:** A significant portion of current bottlenecks is related to tooling and connecting the necessary "pipes" for AI to access systems, use GPUs, and operate within secure sandboxes <a class="yt-timestamp" data-t="01:36:04">[01:36:04]</a>.

## Economic Implications

The automation of white-collar work will lead to profound economic shifts.
*   **Compute and Energy as Key Resources:**
    *   Compute is predicted to become the most valuable resource in the world <a class="yt-timestamp" data-t="01:58:53">[01:58:53]</a>. A country's GDP will be dramatically affected by the amount of compute it can deploy [[role_of_compute_in_ai_development]] <a class="yt-timestamp" data-t="01:58:56">[01:58:56]</a>.
    *   If intelligence becomes a raw input into economies, energy is the resource directly underneath it. Ensuring abundant energy (e.g., solar) will be crucial for access to "intelligence on tap" [[energy_transitions_and_renewable_energy_challenges]] <a class="yt-timestamp" data-t="02:02:28">[02:02:28]</a>, <a class="yt-timestamp" data-t="02:02:40">[02:02:40]</a>.
*   **Shift in Labor Value and Moravec's Paradox:**
    *   Moravec's Paradox suggests that tasks difficult for humans (like complex calculations) are easy for AI, while tasks easy for humans (like fine motor skills) are hard for AI [[human_intelligence_vs_neural_network_intelligence]] <a class="yt-timestamp" data-t="02:03:58">[02:03:58]</a>.
    *   This could lead to a dystopian scenario where AIs automate cognitive white-collar work, and the most valuable thing humans can do is perform physical tasks, becoming "human meat robots" controlled by AI <a class="yt-timestamp" data-t="02:04:53">[02:04:53]</a>. This is seen as a potential decade-long phase if robotics development lags <a class="yt-timestamp" data-t="02:05:42">[02:05:42]</a>.
    *   However, it's argued that Moravec's Paradox might be "fake" in the long run, with the current robotics lag primarily due to a lack of equivalent rich data sets like the internet/GitHub for physical tasks [[impact_of_ai_on_software_development_and_productivity]] <a class="yt-timestamp" data-t="02:05:09">[02:05:09]</a>.
*   **Importance of Robotics for Material Abundance:** To translate AI capabilities into increased material quality of life and avoid a period where human labor value plummets without corresponding material gains, significant investment in robotics is necessary [[ai_for_science_and_societal_challenges]] <a class="yt-timestamp" data-t="02:05:58">[02:05:58]</a>, <a class="yt-timestamp" data-t="02:06:11">[02:06:11]</a>.
*   **Inference Compute as a Bottleneck:**
    *   With widespread deployment, inference compute (running the trained models) could become a major bottleneck <a class="yt-timestamp" data-t="02:00:02">[02:00:02]</a>. Current estimates suggest around 10 million H100 equivalents globally, rising to 100 million by 2028, but this might be insufficient if AI adoption is widespread and valuable <a class="yt-timestamp" data-t="01:19:22">[01:19:22]</a>.
    *   This could lead to a period of being "dramatically inference bottlenecked" around 2027-2028 [[the_timeline_and_technological_progress_towards_agi_by_2027]] <a class="yt-timestamp" data-t="01:20:05">[01:20:05]</a>, <a class="yt-timestamp" data-t="02:22:33">[02:22:33]</a>.

## Policy and Societal Adaptation

Navigating this transition will require proactive policy and societal adjustments.
*   **For Nation-States:**
    *   **Secure Compute and Energy:** Invest in data centers and energy production (e.g., "tile the desert with solar panels") to ensure access to compute, which underpins future economic activity [[data_center_energy_requirements_and_scaling]] <a class="yt-timestamp" data-t="01:59:05">[01:59:05]</a>, <a class="yt-timestamp" data-t="02:02:40">[02:02:40]</a>.
    *   **Invest in AI Eco-system:** Support a portfolio including foundation models, robotics, and supply chains [[investments_and_economic_strategies_in_tech_development]] <a class="yt-timestamp" data-t="01:59:27">[01:59:27]</a>.
    *   **Track Automation:** Governments should break down economic functions into measurable tasks and track AI's progress on them to anticipate impacts <a class="yt-timestamp" data-t="02:07:08">[02:07:08]</a>.
    *   **Promote AI Deployment:** Make it easy to deploy AI, potentially through "special economic zones" <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
    *   **Prevent Capital Lock-in:** Proactively implement policies to prevent a situation where wealth concentrates solely with those who held capital before widespread AI deployment <a class="yt-timestamp" data-t="01:59:39">[01:59:39]</a>. This includes thinking about how to share the proceeds of the AI-driven economy broadly <a class="yt-timestamp" data-t="02:07:39">[02:07:39]</a>.
*   **Preserving Economic and Political Systems:** Human leverage in an AI-dominated future relies on the survival of current economic and political systems (contracts, legal institutions, financial rails) [[economic_growth_and_ai]] <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>. This requires these systems to remain efficient and not overly onerous, so AI-driven firms operate within them <a class="yt-timestamp" data-t="02:08:44">[02:08:44]</a>.
*   **Avoiding Zero-Sum Military Races:** Turning AGI into a national security issue (e.g., "Manhattan Project for AI") risks redirecting AI development towards military tech and provoking international arms races, which is a dramatically worse outcome than a consumer free-market landscape focused on improving human life [[the_geopolitical_stakes_of_agi_development]] <a class="yt-timestamp" data-t="02:09:15">[02:09:15]</a>, <a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a>.
*   **Pull Forward Upsides:** Proactively invest in areas like biology research and robotics data collection to accelerate positive outcomes like novel medicines and material abundance [[ai_for_science_and_societal_challenges]] <a class="yt-timestamp" data-t="02:01:11">[02:01:11]</a>, <a class="yt-timestamp" data-t="02:07:43">[02:07:43]</a>.

## Advice for Individuals

Individuals should prepare for a world with significantly increased leverage due to AI.
*   **Embrace Leverage:** Think about what problems or causes could be tackled if one had substantially more engineering or organizational power <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   **Technical Depth:** Continue to study foundational fields like CS, biology, and physics [[the_role_of_applied_mathematicians_and_their_impact_on_various_fields]] <a class="yt-timestamp" data-t="02:17:09">[02:17:09]</a>. AI provides an "infinite perfect tutor" to facilitate learning [[exploring_the_future_of_society_and_economy_with_ai]] <a class="yt-timestamp" data-t="02:17:24">[02:17:24]</a>.
*   **Adapt Workflows:** Be willing to discard old workflows and critically evaluate how AI can automate or accelerate current tasks. "Be lazier" by finding ways for AI to do toilsome work <a class="yt-timestamp" data-t="02:17:35">[02:17:35]</a>, <a class="yt-timestamp" data-t="02:17:42">[02:17:42]</a>.
*   **It's Not Too Late:** Exponential progress means new opportunities constantly arise; it's never too late to get involved, as previous expertise may become less relevant, and general intelligence and drive are highly valued [[potential_future_scenarios_of_artificial_intelligence_development]] <a class="yt-timestamp" data-t="02:18:19">[02:18:19]</a>, <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

The overarching message is that significant automation of white-collar work is imminent, bringing both immense opportunities and challenges that require proactive adaptation from individuals, organizations, and governments.