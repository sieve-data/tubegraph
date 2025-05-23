---
title: AI trajectory and scaling hypothesis
videoId: a42key59cZQ
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Here is the modified article with the added backlinks:

Gwern Branwen, an anonymous researcher and writer, has been a significant, albeit often behind-the-scenes, thinker in the field of Artificial Intelligence, particularly known for his early insights into the power of scaling Large Language Models (LLMs) [[large_language_models_and_transfer_learning | LLMs]]. This article outlines his perspective on the trajectory of AI development, the scaling hypothesis, and related concepts, based on his own words.

## The Scaling Hypothesis: Core Idea

The scaling hypothesis, in essence, posits that intelligence, or at least the capabilities demonstrated by AI models, can be significantly advanced by increasing the scale of three key components: compute, data, and parameters (model size) [[role_of_compute_in_ai_development | role of compute in AI development]]. Gwern came to believe that "maybe intelligence really is just a lot of compute applied to a lot of data, applied to a lot of parameters", and that this approach would lead to increasingly impressive results [[ai_scalability_and_breakthroughs | AI scalability and breakthroughs]].

The critical test for this hypothesis, in his view, was the leap from GPT-2 to GPT-3, one of the biggest scale-ups in neural network history. If scaling was bogus, GPT-3 would be unimpressive. If true, it would be significantly more impressive than GPT-2. The few-shot learning chart in the GPT-3 paper was a "holy shit" moment, confirming the power of scaling [[future_of_ai_challenges_and_opportunities | future of AI: challenges and opportunities]].

## Evolution of Gwern's Views on Scaling

### Initial Skepticism
In the mid-2000s, Gwern encountered the connectionist argument from thinkers like Moravec and Ray Kurzweil, who suggested that sufficient computing power could lead to AI matching the human brain. Initially, Gwern found this "very unlikely", believing that algorithms were complex and required deep insight, not just brute-force compute. This was a "build it and they will come" view of progress he didn't find correct at the time [[human_intelligence_vs_neural_network_intelligence | human intelligence vs neural network intelligence]].

### Influences and Early Observations
Shane Legg's extrapolations of Kurzweil and Moravec's work, predicting generalist systems around 2019 and human-ish agents by 2025, kept the idea in Gwern's mind. The successes of DanNet and AlexNet around 2012 made him reconsider if this was what Kurzweil, Moravec, and Legg had predicted: GPUs enabling better algorithms [[microsofts_breakthroughs_in_ai_and_quantum_computing | Microsoft's breakthroughs in AI and quantum computing]]. He began to think the idea was "not quite as stupid" as he'd initially thought.

Over the following years, he noticed a "gradual trickle of drops": datasets and models kept getting bigger, GPU usage increased, and neural networks expanded from niche uses to broader applications. This led to a growing realization that "maybe intelligence really is just a lot of compute applied to a lot of data, applied to a lot of parameters. Maybe Moravec and Legg and Kurzweil were right." [[impact_and_future_of_ai_in_economic_systems | impact and future of AI in economic systems]].

### Key Milestones
*   **DanNet and AlexNet (c. 2012):** Impressive connectionist successes that prompted Gwern to re-evaluate his skepticism.
*   **GPT-1:** The unsupervised sentiment neuron learning on its own was "pretty amazing" and a compute-centric view.
*   **GPT-2:** Prompted a "holy shit!" moment with its prompting and summarization capabilities, making him question if "we live in their world" (the world of scaling advocates).
*   **GPT-3 (2020):** This was the "crucial test" due to its massive scale-up. The few-shot learning chart on the first or second page of the paper solidified his conviction: "Holy shit, we are living in the scaling world." The widespread misinterpretation of GPT-3's results by others, who claimed it showed scaling worked badly, angered him and motivated him to write extensively on the topic [[challenges_and_opportunities_in_deploying_ai_at_scale | challenges and opportunities in deploying AI at scale]].

## Why Others Missed Scaling in 2020

Gwern identifies several reasons why many observers, even those writing bestselling books on AI, missed the significance of LLMs, GPT-3, and scaling laws in 2020 [[challenges_in_ai_alignment_and_potential_risks | challenges in AI alignment and potential risks]]:

1.  **Underappreciation of Prior Scaling Results:** Many were not paying attention to relevant prior results, such as how AlphaZero's discovery involved Bayesian optimization over hyperparameters, a compute-intensive process [[alphazero_and_efficient_search_techniques | AlphaZero and Efficient Search Techniques]]. The 2017 Baidu paper on scaling laws, showing they "just keep going and going forever, practically," was largely overlooked despite its importance [[ai_alignment_and_safety_concerns | AI alignment and safety concerns]]. Similarly, the scaling of BigGAN to 300 million images was not widely known.
2.  **Misconception about Algorithms vs. Compute:** Many shared Gwern's initial error of believing algorithms were more important than compute. This was partly due to the "systematic falsification of the actual origins of ideas in the research literature," which often downplays the role of trial-and-error and compute power [[ai_alignment_and_cooperation_challenges | AI alignment and cooperation challenges]].
3.  **Lack of Compute for Early Correct Ideas:** Historically, many correct ideas (e.g., ResNets conceptualized as early as 1988) failed to make an impact because the necessary compute power to train them effectively didn't exist, leading to their abandonment or being forgotten [[role_of_compute_and_infrastructure_in_the_future_of_ai_development | role of compute and infrastructure in the future of AI development]]. Without sufficient compute, researchers couldn't iterate enough to find working solutions or robust hyperparameters [[ai_for_science_and_societal_challenges | AI for Science and Societal Challenges]].

## Gwern's AI Timelines

*   **2005-2010:** AI seemed very far away, "well past like 2050," though potentially within his lifetime.
*   **Post-AlexNet/DanNet (c. 2012 onwards):** Timelines began "dropping at a rate of like 2 years per year, every year until now" as deep learning consistently overcame barriers [[forecasting_ai_progress_and_the_intelligence_explosion | forecasting AI progress and the intelligence explosion]].
*   **Periods of Overshoot:** Gwern felt people "over-updated on AlphaGo," and the subsequent fizzling of some big reinforcement learning efforts (post-Dota) made him think timelines might have overshot.
*   **Impact of GPT:** The arrival of GPT "basically erased all that" doubt, suggesting RL would be "the cherry on the cake" built by generative models. This aligns with LeCun's idea of learning fast on generative models and then using a bit of RL for specific tasks [[reinforcement_learning_from_human_feedback_rlhf | Reinforcement Learning from Human Feedback (RLHF)]].
*   **Current Perspective (for planning):** He mentions the Anthropic timeline of 2028 for AGI as a "good personal planning starting point". He suggests that an AI capable of writing a Gwern-quality essay might be possible in "two to three years," potentially without full AGI if it leverages his existing corpus [[future_of_agi_and_societal_implications | future of AGI and societal implications]].

## Implications of Scaling for Understanding Intelligence

### Intelligence as Search Over Turing Machines
Gwern suggests the success of scaling points to a "10,000 foot view of intelligence" where "all intelligence is is search over Turing machines". Learning and scaling involve searching over more and longer Turing machines [[neuroscience_and_ai_understanding_intelligence | neuroscience and AI: Understanding Intelligence]]. There is no "general master algorithm" or "special intelligence fluid," but rather a "tremendous number of special cases that we learn and we encode into our brains". Variation in human intelligence is attributed to having more "compute in order to do search over more Turing machines for longer" [[human_and_ai_intelligence_comparison | Human and AI intelligence comparison]]. This explains why there's no "IQ gland"; the brain learns many individual specialized problems which are then recombined for fluid intelligence. Similarly, large neural networks are like gigantic ensembles of small models [[mechanistic_interpretability_in_ai | mechanistic interpretability in AI]].

This view also helps explain why human-level intelligence is rare: encoding small, specific Turing machines directly via genes is often more adaptive and less expensive than a general, glitchy search process like human intelligence, especially in static niches or for short-lived organisms.

### Relationship between Human and Neural Network Intelligence
One of the biggest unresolved tensions in Gwern's worldview is the relationship between human intelligence and neural network intelligence [[artificial_intelligence_vs_human_intelligence | Artificial Intelligence vs Human Intelligence]]. He oscillates on whether they are two sides of the same coin, or if one is an inferior version of the other, considering aspects like memorization versus creativity, and sample efficiency. However, he refuses to believe they are "totally unrelated kinds of intelligence".

## Future of AI and Automation

### Automation in Companies: Bottom-Up
Gwern expects companies to be automated bottom-up, starting with workers and moving upwards, eventually leaving human executives to oversee AI firms [[ai_economic_and_political_impacts | AI Economic and Political Impacts]]. This is seen as more palatable and practical.

### The "Steve Jobs" Role for Humans
From an RL perspective, if humans are superior to AIs in some way, it's likely in "long-term vision" [[ai_alignment_and_potential_risks | AI alignment and potential risks]]. AIs might be too myopic for novel long-term strategy. This could lead to a paradigm with a human CEO (a "Steve Jobs-type") setting the vision and taste, while an AI corporation executes tasks and brings proposals for the CEO to approve or reject [[the_role_and_future_of_microsoft_in_the_context_of_global_technological_advancements | The role and future of Microsoft in the context of global technological advancements]]. Human-led firms might outcompete entirely AI firms due to this strategic advantage. Gwern sees his own last automatable "keystroke" as this "Steve Jobs-thing of choosing" among AI-generated proposals, like essays [[artificial_general_intelligence_and_ai_systems | Artificial General Intelligence and AI Systems]].

### Unit of Selection for AI Firms
Once individual models can be replicated perfectly, the unit of selection can move to larger groups or "packages of minds". These could be department-like units (e.g., programmer, manager, financial type, legal type) that work well together globally, even if the specific reasons are unquantifiable. Such packages could then be copied, evolved, and selected based on performance [[investments_and_economic_strategies_in_tech_development | Investments and Economic Strategies in Tech Development]].

## Agency in AI

Gwern believes agency is "in many senses, actually easier to learn than we would have thought ten years ago". However, current systems (LLMs primarily trained on internet scrapes) aren't explicitly learning agency; any agency observed is an "accidental byproduct". The fact that LLMs can achieve coherent action from behavior-cloning on text is "miraculous" [[impact_of_ai_on_software_development_and_productivity | Impact of AI on software development and productivity]]. The lack of robust agency is due to insufficient actual training data for it, like proper state-environment-result-reward sequences used in RL (e.g., Gato from DeepMind). Currently, the trend is to train LLMs and use as little RL as possible, rather than training agents in a dedicated RL manner [[the_concept_and_potential_of_agi_artificial_general_intelligence_in_mathematics | The concept and potential of AGI (Artificial General Intelligence) in mathematics]].