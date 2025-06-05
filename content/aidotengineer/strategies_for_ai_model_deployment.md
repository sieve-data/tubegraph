---
title: Strategies for AI Model Deployment
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

Building and deploying agentic AI systems today, or in the near future, necessitates understanding the concept of "prompt tax" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The rapid pace of advancements in AI models, with new releases from companies like Anthropic, Google Gemini, and OpenAI, introduces new functionalities but also carries a hidden "prompt tax" due to unintended consequences and the probabilistic nature of these systems <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This creates a constant tension between leveraging opportunities from new models and mitigating risks like regressions or unexpected behavior <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## The "Prompt Tax"

The "prompt tax" refers to the hidden costs and efforts involved when new AI models are released. It’s akin to getting a new bike: exciting new freedom, but with the potential for unexpected falls <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. As AI models become more capable, integrating their functionality into existing applications can lead to unforeseen challenges <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Unlike technical debt, which often results from optimizing for quick shipping, prompt tax stems from the desire to immediately [[scaling_ai_solutions_in_production | upgrade and incorporate]] new capabilities offered by models <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The challenge lies in the unknowns: what will improve and what will break <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. The goal is to maximize benefits while mitigating risks by fixing issues on the fly <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Shipping at the Frontier: Orbital's Experience

Orbital, a company focused on automating real estate due diligence, provides a practical example of navigating AI model deployment <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Their agentic software, Orbital Co-pilot, helps real estate lawyers process vast amounts of paperwork, finding "needles in a haystack" to identify red flags before property transactions <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Growth and Model Evolution
Since commercializing their agentic product 18 months ago, Orbital has seen a dramatic increase in token consumption, from less than a billion to nearly 20 billion tokens monthly, handling work previously done manually by lawyers <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. They have also scaled from zero to multiple seven figures in annual recurring revenue <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Orbital has migrated through various models, starting with GPT-3.5, moving to GPT-4 32K (which enabled agentic systems due to its increased context window despite being expensive), and then to newer versions like 4 Turbo 40, 4.1, and system 2 models like 01 preview to 04 mini <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Strategic Decisions for Deployment
Orbital made three key decisions in their [[Best Practices for Building AI Systems | AI system building]]:
1.  **Optimizing for Prompting over Fine-Tuning**: This approach maximized development speed, allowing real-time adjustments to prompts based on user feedback. Changes could be incorporated quickly, which was crucial for finding product-market fit and continues to enable rapid feature shipping <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
2.  **Heavy Reliance on Domain Experts**: Private practice real estate lawyers, with decades of experience, were embedded in the team and actively wrote many of the prompts. This allowed their expertise to be directly taught to the AI system <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
3.  **"Vibes" over Formal Evals**: While acknowledging the importance of rigorous [[best_practices_for_ai_evaluation | evaluation systems]], Orbital prioritized subjective testing by domain experts before release. This approach, though controversial, has supported significant growth in tokens, revenue, and user feedback <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Evaluation often involves manual review, subjective feeling, and logging potential regressions in spreadsheets, rather than comprehensive, objective systems <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Prompt Management
Orbital categorizes prompts into two areas:
*   **Agentic Prompts**: Owned by AI engineers, these are system prompts that help the model choose and use tools <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Domain-Specific Prompts**: Used by real estate lawyers, these teach the system expertise in the real estate domain <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

The number of domain-specific prompts has grown from near zero to over 1,000, which contributes to the "prompt tax" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. When a new AI model is released, the team rigorously experiments with it to unlock envisioned features or inspire new ideas <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. They also assess the prompt tax required to migrate existing prompts to the new model and manage the inherent fear of unknown unknowns that shipping a new model entails <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

## Battle-Tested Tactics for AI Model Deployment

Based on 18 months of experience, Orbital has developed several [[best_practices_for_ai_deployment_and_optimization | best practices for AI deployment and optimization]]:

*   **Migrating from System 1 to System 2 Models**:
    *   **Specificity vs. Objective**: System 1 models required specific instructions on "how to" accomplish tasks, while System 2 models only need a clear objective of "what to do" <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   **Leanness**: Redundant instructions for System 1 models can be removed for System 2 models <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
    *   **Unblocking the Model**: System 2 models perform better with fewer constraints, given time to think and reason through context <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Leveraging System 1 Models**: Despite favoring System 2, System 1 models can be cheaper and faster. Their "thought tokens" can be embedded for user explainability (especially in legal domains) or used for debugging issues based on experimentation or user feedback <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Progressive Rollouts with Feature Flags**: Similar to traditional software development, feature flags can mitigate risk when rolling out new AI model upgrades. This helps address "change aversion bias," where users inherently feel more anxiety about a new system, even if it has upsides <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   **"Betting on the Model" Mantra**: This involves designing software features by anticipating future AI model capabilities (smarter, cheaper, faster, more capable) rather than current limitations. This ensures the product evolves with the models <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **AI-Assisted Prompt Migration**: Utilizing System 2 models to help migrate existing domain-specific prompts, as the new model "knows itself" and can often suggest optimizations, drastically reducing manual effort <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
*   **Courage to Ship**: Given the inherent uncertainty with probabilistic models and new capabilities, a team must be willing to take on risk, ship, and then deal with consequences, mitigating as much as possible beforehand <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   **Strong Feedback Loops**: Building a system for immediate user feedback (e.g., thumbs up/down) that goes directly to AI engineers and domain experts allows for rapid identification, prompt adjustment, and deployment of fixes, sometimes in minutes or hours <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

## The Challenge of a Rapidly Evolving Tech Stack

Demis Hassabis, CEO of Google DeepMind, highlights that the underlying AI tech stack is evolving at an "unbelievably fast" pace, unlike previous revolutionary technologies like the internet or mobile which eventually stabilized <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. This unique challenge for product development means companies must decide what to "bet on" when capabilities could be 100% better in a year <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>. This requires product people with deep technical understanding to anticipate future AI capabilities and design products accordingly <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

This environment presents a significant opportunity for "product AI engineers" – those who understand customer problems and can connect technical capabilities of models to solve real user problems <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

## Paying the Prompt Tax: Moving Forward

The meta-question for organizations is: what gives us more confidence to ship at the AI frontier <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>? While "vibes" have worked for Orbital thus far, relying on domain experts and real-time user feedback, the question remains whether this approach will scale as the product's surface area increases <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.

The possibility of using a formal [[best_practices_for_ai_evaluation | evaluation system]] is considered, but its complexity, cost, and slowness due to numerous edge cases and the probabilistic nature of LLMs (especially in legal contexts requiring correctness, style, conciseness, and citation accuracy) make it a potentially impossible task to scale with product velocity <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. This directly relates to [[cost_considerations_in_ai_agent_deployment | cost considerations in AI agent deployment]] and [[cost_and_efficiency_in_deploying_ai_systems | cost and efficiency in deploying AI systems]].

**Progressive Delivery** emerges as a strong candidate for future [[scaling_ai_agents_in_production | scaling AI agents in production]] and managing prompt tax <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. This involves:
1.  Rolling out internally first <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
2.  Then to a limited number of progressive users <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>.
3.  Incrementally scaling to more users based on incoming feedback <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.
4.  Dialing back if teams get overwhelmed by feedback until minimal changes are needed at 100% rollout <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.

The central thesis for staying at the cutting edge of AI is to "buy now" – embrace and ship new model capabilities immediately <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. While there's inherent anxiety, the potential for downside risk may not always materialize, or it can be managed through progressive rollout strategies <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.