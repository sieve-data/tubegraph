---
title: AI developments in hardware and software advancements
videoId: _kRg-ZP1vQc
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The progress of Artificial Intelligence (AI) is driven by a combination of advancements in computer hardware, software (algorithms), and the increasing investment in both. These factors can create powerful feedback loops, potentially leading to an "intelligence explosion" [[intelligence_explosion_and_its_implications | intelligence explosion and its implications]]. This article outlines the key dynamics and components of these advancements as discussed by Carl Shulman.

## Core Dynamics: Input-Output Curves and Labor

A core concept for understanding AI progress is the idea of "input-output curves" [[ai_trajectory_and_scaling_hypothesis | AI trajectory and scaling hypothesis]]. While it becomes increasingly difficult to improve technologies like computer chips as physical limits are approached (diminishing returns), the nature of the labor performing this work is crucial.

Historically, human labor has been the primary input for these advancements. A paper, "Are Ideas Getting Harder to Find?", analyzed periods where computing productivity increased massively (e.g., a million-fold) but required a significant increase in human investment and labor (e.g., 18-fold) [[human_and_ai_labor_dynamics | human and AI labor dynamics]].

However, if AI systems begin to perform this research and development work, the dynamic changes. An increase in computing performance can translate directly to an increase in the "effective labor supply" [[artificial_intelligence_vs_human_intelligence | Artificial Intelligence vs Human Intelligence]]. If a million-fold compute increase was used to run AIs replacing human scientists, the 18x increase in labor demand becomes trivial. Data suggests that historically, for chip improvements, there were over four doublings of compute performance for each doubling of human labor input required. This implies that more compute is generated than is needed to overcome the increasing difficulty of research, allowing the surplus to accelerate further progress.

## Key Drivers of AI Progress

AI advancement relies on three main interacting pillars: hardware technology, software/algorithmic progress, and investment.

### 1. Hardware Advancements

Hardware progress encompasses improvements in chip efficiency and the sheer amount of hardware being deployed.
*   **Chip Efficiency:** Humans have been developing new computer chips and software, historically leading to Moore's Law (though it's now slowing). Epoch, an AI forecasting research group, estimates a doubling of hardware efficiency roughly every two years, potentially faster for AI-specific workloads [[innovations_and_challenges_in_ai_hardware | Innovations and Challenges in AI Hardware]]. Newer chips like the H100s are significantly better than their predecessors (A100s).
*   **Investment in Hardware:** A significant recent trend is the massive increase in spending on computer hardware specifically for training large AI models.
*   **Hardware Production:** Companies like NVIDIA design chips (fabless), while TSMC fabricates them, and ASML provides lithography equipment [[semiconductor_industry_and_trade_secrets | Semiconductor Industry and Trade Secrets]]. Tens of thousands work at NVIDIA, over 70,000 at TSMC. There's room to redirect existing fab capacity (much of which is not currently for AI chips) towards AI.
*   **Limits to Hardware Progress:** If Moore's Law ends and chip technology freezes, further compute availability would come from building more of the existing chips. This could lead to economies of scale, as R&D costs are amortized over larger production runs. However, energy costs for running chips would eventually become a limiting factor [[data_center_energy_requirements_and_scaling | Data center energy requirements and scaling]].

### 2. Software and Algorithmic Advancements

Improvements in AI software and algorithms allow for more to be done with the same hardware.
*   **Nature of Software:** Software can be copied freely, unlike hardware which requires manufacturing for each unit.
*   **Rate of Progress:** Research by Tamay Besiroglu ("Are models getting harder to find?") suggests the doubling time for workers driving software advances is several years, while effective compute from algorithmic progress doubles faster. Epoch's data (mainly using ImageNet datasets) indicates an algorithmic progress doubling time of less than one year [[large_language_models_and_transfer_learning | Large Language Models and Transfer Learning]]. This translates to roughly two or three doublings of "effective compute" from software progress annually.
*   **Interaction with Compute:** Abundant compute can enable more experiments, leading to the discovery of better algorithms. Thus, some apparent software improvements are enabled by hardware availability.
*   **Impact:** Software improvements are potentially more disruptive than hardware improvements because they can be immediately applied to all existing GPUs [[impact_of_ai_on_software_development_and_productivity | Impact of AI on software development and productivity]].

### 3. Increased Investment and Budgets

The financial resources allocated to AI development are a critical enabler.
*   **Recent Growth:** Epoch reports that budgets for training large AI models have seen a doubling time of around six months in recent years, a tremendous acceleration.
*   **Scale of Investment:** Training models like GPT-4 can cost tens to hundreds of millions of dollars. Training runs costing a billion dollars are considered highly likely, and even up to a hundred billion dollars is plausible if performance continues to scale and open new market opportunities.
*   **Revenue Feedback Loop:** Profitable AI applications can generate revenue that funds even larger and more capable subsequent models, creating a financial feedback loop. The ultimate value of AGI, potentially automating a significant portion of the $100 trillion global economy, justifies massive investment [[the_potential_economic_and_social_impacts_of_agi | The potential economic and social impacts of AGI]].

## The AI Feedback Loop: AI Improving AI

A crucial aspect of the intelligence explosion theory is the idea that AI itself will begin to contribute significantly to its own advancement.

*   **Mechanism:** AI can assist in designing better hardware and, more critically, developing more advanced AI software [[ai_trajectory_and_scaling_hypothesis | AI trajectory and scaling hypothesis]]. For instance, AI could automate parts of the chip design process currently done by thousands of engineers at companies like NVIDIA.
*   **Threshold for Significance:** The feedback loop becomes powerful when AI's contributions to research productivity are substantial (e.g., boosting human researcher productivity by 50-100% or more). This doesn't require AI to be "human-level" in all aspects but capable enough to significantly accelerate the innovation cycle. A system just as good as a human but with AI advantages (e.g., speed, scalability, vast "education") would already be deep into an intelligence explosion.
*   **Examples of AI Contributions:**
    *   **Synthetic Data and Curricula:** AIs could design optimized training data and learning curricula for other AIs, far beyond what humans could manually create. This is analogous to AlphaZero generating its own high-quality training data through self-play [[alphazero_and_efficient_search_techniques | AlphaZero and Efficient Search Techniques]].
    *   **Self-Improvement Dialogues:** Anthropic's "Constitutional AI" demonstrated models improving their responses by "talking to themselves" and then being trained on these improved responses.
    *   **Exploiting AI Advantages:** AIs are cheap to run in massive quantities, can perform extensive search (like AlphaGo), and can be omnidisciplinary, quickly learning new domains. Computer science is a particularly suitable area for AI to excel due to the digital environment and rapid feedback from interpreters [[ai_for_science_and_societal_challenges | AI for Science and Societal Challenges]].

## Acceleration and the Intelligence Explosion

The combined effect of these advancements can lead to a rapid acceleration in AI capabilities.
*   **Compounding Effects:** If the doubling time for effective compute from software innovations (e.g., 8 months) is halved to 4 months due to AI contributions, and then further halved as AI becomes even more effective, progress can become extremely rapid.
*   **Resource Redirection:** The current era is characterized by a significant redirection of resources (talent, compute, capital) towards AI. This "scale-up" is a one-time event; if it doesn't yield AGI or the start of an intelligence explosion, future progress might revert to a slower grind dependent on general economic growth [[economic_growth_and_technological_acceleration | Economic growth and technological acceleration]].
*   **Current Trajectory:** The history of AI compute shows an exponential increase, with more than half of the total compute increase (over 24 orders of magnitude since 1952) occurring since 2010. This means the field is traversing the potential "orders of magnitude" of input required for AGI much more quickly than in the past [[forecasting_ai_progress_and_the_intelligence_explosion | Forecasting AI progress and the intelligence explosion]].

The primary focus of this AI-driven R&D would initially be on further software improvements, as these can immediately enhance the capabilities of all existing hardware [[impact_of_ai_on_future_technology_and_society | Impact of AI on future technology and society]]. This self-reinforcing cycle of improvement is the core of the "intelligence explosion" hypothesis.