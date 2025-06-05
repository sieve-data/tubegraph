---
title: Strategies for adapting AI models and prompts
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

This article explores the concept of "prompt tax" and strategies for adapting AI models and prompts in rapidly evolving AI development environments, drawing insights from Orbital's experience in automating real estate due diligence.

## The Pain of Progress: The "Prompt Tax"
Developing with the current rate of AI progress feels like having a birthday every month, with new models and functionalities released by major labs like Anthropic, Google Gemini, and OpenAI at a breathtaking pace <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>. As these advancements are integrated into applications, a "hidden prompt tax" emerges <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>. This "prompt tax" refers to the effort and cost incurred when adapting existing prompts and systems to new, probabilistic AI models that can behave in unexpected ways <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>. Shipping product at the frontier of AI involves a constant tension between the opportunities new models offer and the risks of introducing regressions or unintended consequences <a class="yt-timestamp" data-t="01:37:38">[01:37:38]</a>.

## Shipping at the Frontier: Orbital's Experience
Orbital, a company automating real estate due diligence, aims to fast-forward property transactions by helping real estate lawyers find "needles in a haystack" within mountains of paperwork <a class="yt-timestamp" data-t="02:01:03">[02:01:03]</a>. Their agentic software, Orbital Co-pilot, thinks like a real estate lawyer, radically reducing the time needed to find red flags and compile necessary paperwork <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>.

### Orbital Co-pilot: A Case Study
The Orbital Co-pilot takes documents (e.g., deeds, leases) and first OCRs them for structured text <a class="yt-timestamp" data-t="04:17:17">[04:17:17]</a>. The agentic system then creates a plan, breaking it into subtasks, each an agentic system with multiple LLM calls <a class="yt-timestamp" data-t="04:30:30">[04:30:30]</a>. It extracts information like lease dates or annual rent, reading legal documents and providing clickable citations for lawyer review <a class="yt-timestamp" data-t="04:41:41">[04:41:41]</a>.

Over 18 months, Orbital has scaled its consumption from less than a billion tokens to nearly 20 billion tokens monthly, performing work previously done manually by lawyers <a class="yt-timestamp" data-t="05:34:34">[05:34:34]</a>. They also scaled from zero to multiple seven figures in annual recurring revenue <a class="yt-timestamp" data-t="06:06:06">[06:06:06]</a>.

### Evolution of AI Models and Key Decisions
Orbital started with GPT-3.5 and transitioned through various models, including GPT-4 32K (which enabled agentic systems due to its increased context window) and later models like 4 Turbo 40, 4.1, and system 2 models like 01 preview and 04 mini <a class="yt-timestamp" data-t="06:27:28">[06:27:28]</a>.

Three key decisions shaped their approach:
1.  **Optimize for Prompting over Fine-tuning**: This maximized development speed, allowing real-time adjustments to prompts based on user feedback, crucial for finding product-market fit and rapidly shipping features <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. This relates to [[customization_and_scalability_in_ai_models]].
2.  **Heavy Reliance on Domain Experts**: Private practice real estate lawyers, with decades of experience, write many of the prompts, imbuing the AI system with their expertise <a class="yt-timestamp" data-t="07:34:34">[07:34:34]</a>.
3.  **"Vibes over Evals"**: While acknowledging the desire for a rigorous evaluation system, their growth in tokens, revenue, and user feedback was achieved largely through subjective human testing by domain experts, sometimes logging regressions in spreadsheets, but not a comprehensive objective system <a class="yt-timestamp" data-t="07:57:57">[07:57:57]</a>.

Orbital's prompts are categorized into:
*   **Agentic Prompts**: Owned by AI engineers, these are system prompts that help the model choose which tools to use and when <a class="yt-timestamp" data-t="08:56:56">[08:56:56]</a>.
*   **Domain-Specific Prompts**: Used by real estate lawyers, these teach the system its expertise in the real estate domain <a class="yt-timestamp" data-t="09:09:09">[09:09:09]</a>.

The number of domain-specific prompts has grown from near zero to over 1,000, creating a significant "prompt tax" <a class="yt-timestamp" data-t="09:21:21">[09:21:21]</a>.

### The Process of Adopting New AI Models
When a new AI model is released:
1.  **Rigorous Experimentation**: AI engineers and domain experts experiment to unlock envisioned features, utilize new capabilities, and assess model fitness <a class="yt-timestamp" data-t="09:39:39">[09:39:39]</a>.
2.  **Prompt Tax Calculation**: Determine the effort required to migrate existing prompts to the new model <a class="yt-timestamp" data-t="10:04:04">[10:04:04]</a>.
3.  **Fear Management**: Address inherent fear of unknown unknowns and potential regressions by pinpointing and mitigating irrational anxieties before shipping <a class="yt-timestamp" data-t="10:10:10">[10:10:10]</a>.

### Prompt Tax vs. Technical Debt
The "prompt tax" is distinct from technical debt. While technical debt often optimizes for quick shipping with a plan to fix later (and potentially deleting features), prompt tax is driven by the desire to upgrade *now* to leverage new model capabilities, despite the uncertainty of what will improve and what will break <a class="yt-timestamp" data-t="10:32:32">[10:32:32]</a>. The goal is to fix things on the fly and progressively roll out the new model to maximize benefits while mitigating risks <a class="yt-timestamp" data-t="11:16:16">[11:16:16]</a>. This touches upon [[strategies_for_effective_ai_implementation]].

## Battle-Tested Tactics
Orbital has developed several tactics over 18 months for navigating AI model migrations:

### Prompting for System 1 vs. System 2 Models
When migrating from System 1 models (e.g., GPT-40) to System 2 models (e.g., 01 preview) <a class="yt-timestamp" data-t="12:02:02">[12:02:02]</a>:
*   **Specificity**: System 1 models required specific instructions on *how* to accomplish tasks; System 2 models need all that stripped out, only requiring specification of *what* to do <a class="yt-timestamp" data-t="12:12:12">[12:12:12]</a>.
*   **Leaner Prompts**: System 1 models often needed repeated instructions; these can be removed for System 2 models <a class="yt-timestamp" data-t="12:26:26">[12:26:26]</a>.
*   **Unblocking the Model**: System 2 models perform better with fewer constraints, given a clear objective and time to think, rationalize, and reason to find a plan and result <a class="yt-timestamp" data-t="12:40:40">[12:40:40]</a>. These are key [[reasoning_models_and_their_unique_prompting_requirements]].

### Leveraging "Thought Tokens"
System 1 models, while often cheaper and faster, provide "thought tokens." These can be embedded for user explainability (especially in complex domains like legal) or used for debugging when the system isn't working as expected <a class="yt-timestamp" data-t="13:07:07">[13:07:07]</a>.

### Progressive Delivery and Change Aversion Bias
Similar to feature flags in software development, progressively rolling out new AI model upgrades can mitigate risk <a class="yt-timestamp" data-t="13:46:46">[13:46:46]</a>. However, developers must be aware of "change aversion bias," where moving to a new system creates heightened anxiety and awareness of potential issues, sometimes outweighing the positives <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>. This highlights [[strategies_to_mitigate_ai_errors]].

### "Betting on the Model"
A team mantra adopted by Orbital is to "bet on the model" <a class="yt-timestamp" data-t="14:56:56">[14:56:56]</a>. This means designing SAS software and features not just for today's AI capabilities, but imagining where models will be in 3, 6, or 12 months (smarter, cheaper, faster, more capable) <a class="yt-timestamp" data-t="15:02:02">[15:02:02]</a>. This allows features to grow with model advancements rather than stagnating <a class="yt-timestamp" data-t="15:12:12">[15:12:12]</a>.

### Using AI to Migrate Prompts
System 2 models can assist in migrating prompts designed for prior models. By feeding a domain-specific prompt into the new model, it can help re-optimize and migrate the prompt, radically decreasing manual human effort <a class="yt-timestamp" data-t="15:45:45">[15:45:45]</a>. This is a practical [[techniques_for_improving_ai_model_efficiency]].

### Bravery and Rapid Feedback Loops
Given the inherent uncertainty of probabilistic models and new capabilities, teams need the bravery to make tough calls, ship, and deal with consequences after deployment, mitigating risks along the way <a class="yt-timestamp" data-t="16:12:12">[16:12:12]</a>.

A strong, rapid feedback loop is crucial <a class="yt-timestamp" data-t="17:10:10">[17:10:10]</a>. Orbital built a system where user feedback (e.g., thumbs up/down) is immediately sent to a domain expert. The expert evaluates it, identifies the prompt needing change, makes the change, and ships it to production, often in minutes or hours <a class="yt-timestamp" data-t="17:27:27">[17:27:27]</a>. This agile response helps in [[challenges_and_strategies_in_ai_production]].

## Challenges of Rapid AI Evolution
Demis Hassabis, CEO of Google DeepMind, highlights that the underlying AI tech stack is evolving "unbelievably fast," unlike the more stabilized tech stacks seen with the internet or mobile <a class="yt-timestamp" data-t="18:17:17">[18:17:17]</a>. This makes product development uniquely challenging, as capabilities can be 100% better in a year <a class="yt-timestamp" data-t="18:46:46">[18:46:46]</a>. It requires deeply technical product people who can anticipate future technology states to design products that will be relevant when released <a class="yt-timestamp" data-t="19:06:06">[19:06:06]</a>. This suggests a need for "product AI engineers" who understand both model capabilities and user needs <a class="yt-timestamp" data-t="19:57:57">[19:57:57]</a>.

## Paying the Prompt Tax and Shipping with Confidence
The meta-question for AI development is: What gives more confidence to ship at the frontier as AI advances and agentic product surface areas grow? <a class="yt-timestamp" data-t="20:38:38">[20:38:38]</a>.

While Orbital has scaled successfully on "vibes" (human testing and rapid feedback) so far, the question remains whether this will scale indefinitely as the product grows <a class="yt-timestamp" data-t="21:03:03">[21:03:03]</a>. An evaluation (eval) system could be an answer, but its complexity is high due to the probabilistic nature of LLMs and the need to evaluate correctness, style, conciseness, and citations across numerous prompts and edge cases, potentially making it prohibitively expensive and slow <a class="yt-timestamp" data-t="21:32:32">[21:32:32]</a>. This relates to [[strategies_for_ai_evaluation_and_troubleshooting]].

Progressive delivery—rolling out internally first, then to a limited number of progressive users, and incrementally scaling based on feedback—is a potential way forward to "upgrade now and fix on the fly" <a class="yt-timestamp" data-t="22:30:30">[22:30:30]</a>.

The central thesis is to "buy now" – to stay on the edge of the AI frontier, maximize opportunities from new model capabilities, and ship agentic products to users despite the anxiety of potential downsides <a class="yt-timestamp" data-t="23:37:37">[23:37:37]</a>. Whether the "prompt tax" is paid later on a case-by-case basis (e.g., through progressive rollouts and quick fixes) is yet to be determined <a class="yt-timestamp" data-t="24:10:10">[24:10:10]</a>.