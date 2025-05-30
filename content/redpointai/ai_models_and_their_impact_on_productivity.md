---
title: AI models and their impact on productivity
videoId: NoVMk_P6fgY
---

From: [[redpointai]] <br/> 

Arvin Duran, a leading professor in computer science at Princeton, provides insights into the substance versus hype surrounding AI, particularly regarding its impact on productivity and the future of work. His work, including the "AI Snake Oil" newsletter and book, delves into the practical applications and limitations of AI models <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Current State of AI Models and Productivity

AI models have demonstrated impressive results in domains with clear, verifiable answers, such as math and coding <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This progress is expected to continue in these specific areas <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. However, their ability to generalize beyond these narrow domains remains an open question <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Generalization Challenges and Benchmarks

Historically, technologies like reinforcement learning, which showed great promise in games like Atari, failed to generalize effectively outside of these confined environments <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Similarly, current reasoning models, while impressive on benchmarks like SweepBench (a Princeton-developed benchmark based on real GitHub issues), face challenges with "construct validity" <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This means what a benchmark measures can be subtly different from what is needed in the real world <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. For instance, high scores on bar or medical exams for [[advancements_and_implications_of_ai_models_like_o1 | OpenAI models]] don't fully translate to real-world legal or medical practice, as these professions involve more than just exam-taking <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

Real-world productivity improvements are not always directly proportional to dramatic improvements in benchmark scores <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Instead of solely relying on benchmarks or anecdotal "vibes," "uplift studies" – randomized control trials where one group uses a tool and another doesn't – can provide more concrete measures of impact on productivity <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Inference Scaling Flaws

A key area of research is [[trends_in_ai_model_training_and_deployment | inference scaling]], which questions how far reasoning models can scale their performance. One approach involves pairing a generative model with a verifier (e.g., unit tests for coding, automated theorem checkers for math) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. The hope is that traditional, non-stochastic verifiers can perfectly check millions of generated solutions <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. However, research on "inference scaling flaws" indicates that if the verifier is imperfect, inference scaling cannot progress very far, sometimes saturating within a few invocations <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This has significant implications for scaling models into domains like law or medicine that lack easy, perfect verifiers <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Agentic AI and Product-Market Fit

The term "agentic AI" covers a broad range of applications <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>:

*   **Generative Systems as Tools**: Examples like Google Deep Research generate reports or first drafts, acting as time-saving tools for expert users who review and validate the output <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. The cost of errors is low, as the human user is the final check <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. These generally have good product-market fit.
*   **Autonomous Action-Taking Agents**: These agents autonomously take actions on a user's behalf, such as booking flight tickets <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This is often considered a poor example for [[effectiveness_of_ai_agents | AI agent]] product-market fit due to several challenges <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>:
    *   **Eliciting Preferences**: Accurately understanding all user preferences (e.g., flight preferences) is highly challenging and often requires many rounds of interaction <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. An agent might still struggle to know these preferences without extensive, trusted prior interaction <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
    *   **High Cost of Errors**: Mistakes, such as booking the wrong flight or ordering food to the wrong address, are intolerable, even at a low error rate <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

The development of [[future_of_ai_agents_in_productivity_tools | AI agents]] requires a greater focus on human-computer interaction, not just technical problems <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. While dedicated "killer apps" for agents are anticipated, existing applications are gradually becoming more agentic by integrating search and code execution capabilities <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## The Future of AI and Productivity

### Hardware and Integration

The future of AI integration into daily life and the workplace is highly anticipated. While special-purpose apps like ChatGPT exist, higher-friction uses are giving way to more integrated models <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Examples include:

*   AI features integrated directly into software like Photoshop <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   Agents constantly monitoring computer or phone screenshots to offer improvements or integrate into workflows <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   AI integrated into wearable devices like glasses, offering real-time assistance (e.g., finding lost keys, language translation) <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

The specific form factor that "wins out" will significantly influence the development of these applications <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

### [[ai_and_its_impact_on_energy_consumption | Economic and Strategic Considerations]]

The [[economic_and_strategic_considerations_in_ai_model_deployment | economic impact of AI models]] is characterized by a push and pull between rapidly decreasing per-token inference costs and increasing inference-time compute (token usage) <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. It's predicted that token usage will continue to increase, likely compensating for the per-token cost decrease, leading to rising overall inference costs <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

Research on "AI agent Zoos," where agents collaborate on tasks, shows that even for simple tasks, millions of tokens are generated, as agents need to understand their environment, tools, and collaborators <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. While this is resource-intensive, for certain domains, it may still be preferable to alternatives <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

### Evaluation of Agents

The current state of [[effectiveness_of_ai_agents | AI agent]] evaluation largely mirrors that of chatbots, relying on static benchmarks. However, these benchmarks have limitations <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>:

*   **Capability-Reliability Gap**: A 90% benchmark score for agents that take actions on a user's behalf doesn't clarify if it means 90% of tasks are always correct or if 10% of attempts will lead to costly failures <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. This provides insufficient information for real-world deployment <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
*   **Safety**: While safety-specific benchmarks exist, safety should be an integral part of every benchmark <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. Running agents on real websites can lead to unintended consequences (e.g., spam), while simulated environments often lack realism <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Early agentic systems like AutoGPT have been reported to take unintended actions (e.g., posting on Stack Overflow) <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. Basic safety controls, like requiring human approval for every action, currently make agents impractical <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.

Benchmarks should be considered a necessary but not sufficient condition for agent quality <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>. The next step involves evaluating agents in semi-realistic environments with humans in the loop <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

### Organizational and Societal Impact

Similar to past technological shifts like the [[Industrial Revolution]] or the adoption of electricity, AI will necessitate a rethinking of how humans and machines collaborate <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>. It took decades to optimize factory layouts and labor organization after these past revolutions <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. The focus now is on forming "teams of humans and agents," embracing the "Jagged Frontier" idea that AI excels at certain tasks but lacks common sense in others <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. This necessitates hybridization. It is unclear whether existing human collaboration tools (Slack, email) are sufficient or if new tools are needed to visualize and manage agent actions <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.

#### Policy Implications

Export controls, particularly for hardware, have a mixed record of effectiveness <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>. For AI models, which are becoming smaller and more diffusible, such controls are even harder to enforce <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>. A key insight is that policy should focus more on "diffusion" – the adoption and reorganization of institutions, laws, and norms to leverage technology – rather than just "innovation" <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.

Despite claims of rapid adoption of generative AI, the "intensity of adoption" (e.g., half an hour to three hours per week of use) suggests slower integration than something like the PC <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. This could be because AI is not yet broadly useful, or because of policy gaps. For instance, students often view AI as a cheating tool, and education systems need to proactively teach productive ways to use AI and avoid pitfalls <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.

Past waves of AI (e.g., predictive AI in criminal justice, automated trading) show that when consequences arise, public outcry leads to regulation <a class="yt-timestamp" data-t="00:31:28">[00:31:28]</a>. The focus should be on what regulation looks like to balance safety, rights, and benefits, rather than a polarized debate on whether to regulate <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a>. A critical aspect of regulation is "explainability" – not necessarily mechanistic interpretability of a model, but understanding its training data, audits, and expected behavior in new settings <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.

#### [[Impact of AI advancements on business models | Economic and Societal Transformations]]

The [[impact_of_ai_advancements_on_business_models | internet]] era illustrates that technology can profoundly transform how tasks are performed (e.g., online search vs. libraries) without necessarily leading to massive increases in GDP or a complete change in job categories <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>. Bottlenecks shift. The [[Industrial Revolution]], however, fundamentally transformed the nature of work, moving from manual labor to what we now consider "work" <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>. AI could similarly automate many cognitive tasks, shifting human work towards "AI control," focusing on supervision, alignment, and managing the value-based aspects of decisions that AI cannot make morally <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.

There are concerns about [[ai_and_its_impact_on_energy_consumption | AI]] increasing inequality. Wealthier individuals and those with more resources can leverage AI more effectively, for instance, in education by monitoring usage or providing supplementary support <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>. Conversely, for other children, AI could contribute to addiction, similar to social media <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>. This creates a high variance in outcomes based on accessibility and supervision <a class="yt-timestamp" data-t="00:44:36">[00:44:36]</a>.

## Role of Academia

Academia has a crucial role in [[developing_and_utilizing_ai_models_in_the_tech_industry | AI development]] beyond pure technical innovation <a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>:

*   **Interdisciplinary Applications and Societal Impacts**: Scholars from various disciplines need to explore AI's applications and its societal consequences, striving for positive impacts <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.
*   **Counterweight to Industry**: Academia should act as a counterweight to industry interests, similar to the relationship between medical research and the pharmaceutical industry <a class="yt-timestamp" data-t="00:35:14">[00:35:14]</a>. While much of computer science aligns with industry innovation, a significant portion should explicitly aim to provide independent perspectives and explore different directions <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>.

Specific areas of academic interest include:

*   **AI for Science**: While some early claims are overblown, AI is already impacting scientists as a "thinking partner" for research, critiquing ideas, and enhancing literature searches through semantic search <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.
*   **AI and Human Minds**: Research explores the ethical reasoning of AI models and what AI can teach us about human cognition, and vice-versa <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>.

## Predictions for AI and Productivity

*   **Overhyped**: Autonomous agents are currently overhyped, despite their potential <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.
*   **Underhyped**: "Boring" applications like summarizing C-SPAN meetings for lawyers or translating old codebases (e.g., COBOL) to modern languages offer enormous, often overlooked, economic value <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>.
*   **Model Progress in 2025**: Whether progress will be "more" or "less" than in 2024 depends on one's perspective, as advancement in specific tasks (like coding) may surge while broader tasks (like translation) might not see similar leaps <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>.
*   **Future of Information Access**: Younger users may grow up expecting chatbots to be the primary way of accessing information, even with the risk of hallucination, valuing convenience over authoritative sources <a class="yt-timestamp" data-t="00:52:33">[00:52:33]</a>.
*   **Autonomous Agents by End of 2025**: It's predicted there will still be relatively few applications where AI autonomously performs tasks for users by the end of 2025; agentic workflows will mostly remain for generative tasks <a class="yt-timestamp" data-t="00:51:49">[00:51:49]</a>.
*   **Timeline to AGI (Transformative Economic Impacts)**: The timeline for "transformative economic impacts" (e.g., massive GDP impact) from AI is estimated to be decades out, not years <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.
*   **Policy Change**: A desired policy change would be to stop generically calling everything "AI" to bring clarity to discourse and reduce hype by specifying the application <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>.

> [!INFO] Arvin Duran's work and further insights can be found in his newsletter, "AI Snake Oil," which provides a balanced perspective on the positives and negatives of AI <a class="yt-timestamp" data-t="00:56:33">[00:56:33]</a>.