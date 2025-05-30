---
title: AI evaluations and benchmarking
videoId: NoVMk_P6fgY
---

From: [[redpointai]] <br/> 

Evaluating AI models is crucial for understanding their capabilities and limitations. Current evaluations show impressive results in specific domains, but challenges remain in generalizing performance and ensuring real-world utility <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

## Current State of AI Performance

AI models have demonstrated impressive results in domains with clear, correct answers, such as math, coding, and certain scientific tasks <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. This progress is expected to continue in these areas <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.

## Limitations of Benchmarks

Despite impressive benchmark scores, there are significant limitations in how these translate to real-world performance:

*   **Construct Validity:** Benchmarks may subtly differ from what is truly desired in real-world applications <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. For example, while [[ai_coding_and_software_engineering_advancements | SweepBench]], developed by Princeton colleagues, is considered a good benchmark using real GitHub issues, it's still a "far cry from the messy context of real-world software engineering" <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   **Failure to Generalize:** Historically, technologies like reinforcement learning, which showed promise in narrow domains like games, failed to generalize broadly <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. A major open question is how far current impressive performance can generalize beyond clear-answer domains <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **Real-world vs. Exam Performance:** While [[ai_models_and_their_impact_on_productivity | AI models]] show high scores on tests like the bar exam or medical exams, being a lawyer or doctor involves more than just taking exams, including eliciting information from patients <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>. Dramatic improvements in benchmarks do not always translate to dramatic improvements in human productivity <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.

### Inference Scaling Flaws

A paper titled "Inference Scaling Flaws" investigated the scaling of reasoning models, particularly when pairing a generative model with an imperfect verifier (e.g., unit tests in coding, automated theorem checkers in math) <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.
The hope was that traditional logic-based verifiers could be perfect, allowing models to generate millions of solutions until one passes tests <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. However, in reality, verifiers often have imperfect coverage <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. If the verifier is imperfect, inference scaling cannot get "very far," sometimes saturating within only about 10 invocations of the model, rather than millions <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. This has implications for scaling models into domains without easy verifiers, such as law or medicine <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.

## Evaluating AI Agents

Evaluating [[ai_product_market_fit_and_emerging_applications | AI agents]] presents unique [[challenges_and_strategies_in_ai_model_evaluation | challenges]]. The current state of evaluations for agents is similar to chatbots, using static benchmarks with relatively realistic tasks <a class="yt-timestamp" data-t="17:50:00">[17:50:50]</a>.

Key limitations include:

*   **Capability Reliability Gap:** Benchmarks often do not provide information on reliability. A 90% score might mean the agent is good at 9 out of 10 tasks and always accomplishes them correctly, or it might mean it fails 10% of the time at *any* task, potentially leading to costly actions like booking the wrong flight ticket <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>. This means benchmarks give little information about whether an agent can actually be used productively <a class="yt-timestamp" data-t="18:55:00">[18:55:00]</a>.
*   **Safety Concerns:** Safety should be an integral part of every benchmark, not just safety-specific ones <a class="yt-timestamp" data-t="19:05:00">[19:05:00]</a>. Some web benchmarks involve agents doing things on real websites, which can lead to spam or unintended actions <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. Early agentic systems have shown failures, such as ordering DoorDash to the wrong address, where even a 1-in-N error rate is intolerable <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>. Frameworks like AutoGPT have attempted to post questions on Stack Overflow, highlighting the lack of basic safety controls where the only way to prevent such actions is for the agent to escalate every action to a human for babysitting <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.
*   **Lack of Realism:** Simulated environments for web benchmarks lose much of the nuance of real websites, creating a gap without a middle ground <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a>.

### The AI Agent Zoo

A research team is building an "AI agent Zoo" where different [[ai_integration_and_product_development_strategies | AI agents]] collaborate on tasks in an environment <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. This offers a different way of evaluating agents, focusing on collaboration rather than isolated competition <a class="yt-timestamp" data-t="15:47:00">[15:47:00]</a>. Even for simple tasks like writing a joke (which are currently "awful"), these agents can generate millions of tokens, making progress through processes like understanding their environment, tools, and collaborators, and producing summaries <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>. This suggests that overall inference costs are likely to increase significantly <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>.

## Future of Evaluation

Benchmarks should be considered a *necessary but not sufficient* condition for evaluation <a class="yt-timestamp" data-t="21:44:00">[21:44:00]</a>. For example, testing the reliability of an agent by repeating the same task multiple times (e.g., Pass@K) is a more interesting measure <a class="yt-timestamp" data-t="21:14:00">[21:14:00]</a>.
The ideal approach involves using human-in-the-loop evaluations in semi-realistic environments for agents that perform well on benchmarks <a class="yt-timestamp" data-t="21:52:00">[21:52:00]</a>. The challenge is finding ways to keep humans in the loop without requiring constant babysitting <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>. This is a common challenge for managers with junior employees <a class="yt-timestamp" data-t="22:01:00">[22:01:00]</a>.

## Policy Implications and Diffusion

Policy discussions often focus too much on innovation and too little on the diffusion of technology <a class="yt-timestamp" data-t="26:09:00">[26:09:00]</a>. Diffusion involves how a country adopts new technology and reorganizes its institutions, laws, and norms to best leverage it <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>. While the U.S. might be doing well compared to other regions in terms of diffusion, the intensity of [[ai_models_and_their_impact_on_productivity | AI adoption]] (average usage time per week) is still low, possibly slower than PC adoption <a class="yt-timestamp" data-t="27:23:00">[27:23:00]</a>. This could be because AI is not yet useful to many people, or it could be addressed by policy interventions like integrating AI education into curricula <a class="yt-timestamp" data-t="28:30:00">[28:30:00]</a>.

### Learning from Past AI Waves

Lessons from past waves of AI highlight that when technologies lead to consequential decisions, public outcry and regulation often follow <a class="yt-timestamp" data-t="31:33:00">[31:33:00]</a>. The focus should be on what regulation should look like to balance safety, rights, and the benefits of AI <a class="yt-timestamp" data-t="32:14:00">[32:14:00]</a>.
A key aspect for regulation is **explainability**, which means understanding the data a model was trained on and the audits performed, to make statements about its expected behavior in new settings, rather than a "neat mathematical explanation" of every neuron <a class="yt-timestamp" data-t="33:01:00">[33:01:00]</a>.

## Role of Academia

Academia has a crucial role in [[ai_infrastructure_and_developer_tools | AI]], especially in areas beyond pure technical innovation <a class="yt-timestamp" data-t="34:52:00">[34:52:00]</a>. This includes:

*   **Interdisciplinary Research:** Thinking about AI applications across various disciplines and its societal impacts <a class="yt-timestamp" data-t="35:00:00">[35:00:00]</a>.
*   **Counterweight to Industry:** Academia can serve as a counterweight to industry interests, similar to the relationship between medical research and the pharmaceutical industry <a class="yt-timestamp" data-t="35:14:00">[35:14:00]</a>. While much of computer science focuses on producing ideas for industry, a portion should explicitly aim to provide an independent perspective <a class="yt-timestamp" data-t="35:47:00">[35:47:00]</a>.
*   **Areas of Interest:**
    *   **AI for Science:** Despite some overblown claims, AI is already having significant impacts on scientists, serving as a "thinking partner" for critiquing ideas, enhancing literature searches through semantic search, and creating domain-specific tools <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>.
    *   **AI and Human Minds:** Research explores the ethical reasoning of models, learning from human minds to build AI, and using AI as a tool to understand human minds better <a class="yt-timestamp" data-t="38:28:00">[38:28:00]</a>.

## Impact on Education

The future of education with AI will likely be closer to "not that much will change" fundamentally <a class="yt-timestamp" data-t="40:16:00">[40:16:00]</a>. Similar to the early excitement around online courses, AI will be used, but the core value of education still lies in creating social preconditions for learning, motivation, and individualized feedback, which is difficult for AI to fully recreate <a class="yt-timestamp" data-t="40:28:00">[40:28:00]</a>.
There is a high variance in how AI impacts children; while it can be positive for wealthier kids with supervision (e.g., using [[ai_powered_tutoring_tools | AI tutoring apps]] like Khan Academy or custom-built learning apps), for others, it could lead to addiction, similar to social media <a class="yt-timestamp" data-t="42:07:00">[42:07:00]</a>. Most of this [[ai_powered_tutoring_tools | AI learning]] for kids is expected to happen outside of traditional schooling, as schools may remain hesitant to adopt AI <a class="yt-timestamp" data-t="44:22:00">[44:24:00]</a>.

## Broader Societal Implications

The impact of AI on society might reconcile both optimistic and skeptical views, similar to the internet <a class="yt-timestamp" data-t="46:23:00">[46:23:00]</a>. While the internet transformed almost every cognitive task, its overall impact on GDP has been minimal, as new bottlenecks emerged <a class="yt-timestamp" data-t="46:51:00">[46:51:00]</a>.
With AI, many cognitive tasks may become automated. This could lead to a transformation in the definition of "work," where human jobs might shift towards "AI control" – supervising AI and making value-based decisions that AI cannot <a class="yt-timestamp" data-t="48:20:00">[48:20:00]</a>.

One "weird prediction" is that younger generations may come to expect chatbots as the primary way of accessing information, viewing traditional search (clicking on websites) as akin to going to a library <a class="yt-timestamp" data-t="52:34:00">[52:34:00]</a>. This requires preparing users with tools for fact-checking due to the statistical nature and potential for hallucination in chatbots <a class="yt-timestamp" data-t="52:56:00">[52:56:00]</a>.

From an investment perspective, the push and pull between decreasing per-token inference costs and increasing "inference time computes" (the amount of computation needed per query) makes it hard to predict the future <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>. However, it's likely that token usage will continue to increase in a way that more than compensates for per-token cost decreases <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>.

## Overhyped vs. Underhyped

*   **Overhyped:** [[ai_product_market_fit_and_emerging_applications | Agents]] are seen as overhyped, despite their potential <a class="yt-timestamp" data-t="49:57:00">[49:57:00]</a>.
*   **Underhyped:** "Boring" applications that bring significant economic value are underhyped. Examples include [[ai_coding_and_software_engineering_advancements | AI for summarizing C-SPAN meetings for lawyers]] <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a> and [[ai_coding_and_software_engineering_advancements | AI for translating old codebases like COBOL to modern languages]] <a class="yt-timestamp" data-t="53:49:00">[53:49:00]</a>. Another underhyped area is the integration of AI into everyday life in ways that "disappear," like in glasses, rather than as separate, high-friction apps <a class="yt-timestamp" data-t="54:03:00">[54:03:00]</a>.

Ultimately, understanding the "application" of AI, rather than just calling it "AI," would bring more clarity to discourse and reduce hype <a class="yt-timestamp" data-t="54:32:00">[54:32:00]</a>.