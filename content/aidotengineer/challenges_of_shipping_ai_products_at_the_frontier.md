---
title: Challenges of shipping AI products at the frontier
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

Shipping products at the frontier of AI involves a constant tension between the opportunities new AI models present and the risks of introducing regressions or unintended consequences to existing products <a class="yt-timestamp" data-t="01:37:44">[01:37:44]</a>. The rapid pace of AI model development creates a unique set of [[challenges_of_launching_an_ai_product | challenges]] for companies building agentic systems <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="01:54:49">[01:54:49]</a>.

## The Pain of Progress: An Ever-Evolving Frontier
The rate of progress in AI model development is breathtaking, with major labs like Anthropic, Google Gemini, and OpenAI consistently shipping new models and functionalities <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a> <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>. While these advances offer incredible new functionalities to integrate into applications, they also come with unexpected and unintended consequences due to the probabilistic nature of AI systems <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a> <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. This constant evolution of the underlying tech stack makes product development uniquely challenging <a class="yt-timestamp" data-t="01:46:17">[01:46:17]</a> <a class="yt-timestamp" data-t="01:55:09">[01:55:09]</a>.

### Introducing the "Prompt Tax"
As new AI models advance, a "hidden prompt tax" emerges when their functionality is integrated into applications <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a> <a class="yt-timestamp" data-t="01:01:59">[01:01:59]</a>. This concept describes the effort required to adapt existing prompts and systems to new models, which can behave in unexpected ways <a class="yt-timestamp" data-t="01:01:59">[01:01:59]</a> <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>. More prompts equate to a higher prompt tax <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.

The prompt tax is not merely technical debt, which often arises from optimizing for speed with a plan to fix later <a class="yt-timestamp" data-t="10:32:04">[10:32:04]</a>. Instead, the prompt tax is driven by the desire to upgrade *now* to unlock new capabilities <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. However, the uncertainties of new models mean developers don't know exactly what will improve and what will break <a class="yt-timestamp" data-t="11:09:03">[11:09:03]</a>.

## Orbital's Journey: Shipping at the Frontier
Orbital, a company focused on automating real estate due diligence, provides a practical example of shipping AI products at the frontier <a class="yt-timestamp" data-t="01:56:07">[01:56:07]</a>. Their mission is to fast-forward property transactions by helping real estate lawyers quickly find "needles in a haystack" within mountains of paperwork <a class="yt-timestamp" data-t="02:01:09">[02:01:09]</a>.

### Orbital Co-Pilot
Orbital's first agentic product, Orbital Co-Pilot, was developed in January 2024 and designed to "think like a real estate lawyer" <a class="yt-timestamp" data-t="03:14:02">[03:14:02]</a>. The system automates tasks typically performed manually, such as reading documents, OCRing text, structuring information, and compiling reports <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>. The agentic system breaks down plans into subtasks, each using multiple LLM calls to achieve objectives like finding lease dates or annual rent <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

### Scaling and Evolution
Orbital has seen significant growth:
*   From burning less than a billion tokens 18 months ago to consuming almost 20 billion tokens monthly <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.
*   From zero revenue 18 months ago to multiple seven figures in annual recurring revenue <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

They have migrated through various models, starting with GPT-3.5 and evolving through different versions of GPT-4 and other system 2 models like 01 preview <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.

### Key Decisions in AI Development
Orbital made three crucial decisions to navigate the [[challenges_in_ai_development | challenges]] of AI development:
1.  **Optimize for Prompting over Fine-Tuning**: This maximizes development speed, allowing real-time adjustments to prompts based on user feedback <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
2.  **Heavy Reliance on Domain Experts**: Private practice real estate lawyers with decades of experience write many of the domain-specific prompts, effectively teaching the AI system their expertise <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.
3.  **"Vibes over Evals"**: Instead of a rigorous, objective evaluation system, they rely on subjective human testing by domain experts before release, logging potential regressions but without comprehensive metrics <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>. This approach has scaled surprisingly well due to real-time user feedback and quick tooling adjustments <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a> <a class="yt-timestamp" data-t="21:14:00">[21:14:00]</a>.

### The Prompting Process
Orbital uses two main types of prompts:
*   **Agentic prompts**: Owned by AI engineers, these are system prompts that help the model choose and use tools effectively <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.
*   **Domain-specific prompts**: Created by real estate lawyers, these teach the system expertise in the real estate domain <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. Orbital has grown from near zero to over 1,000 domain-specific prompts <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.

When a new AI model drops, Orbital's team rigorously experiments with it to unlock new features or gain inspiration <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>. A key step is calculating the "prompt tax" required to migrate existing prompts to the new model <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. There is also an inherent fear of unknown unknowns when shipping a new AI model <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.

## Battle-Tested Tactics for Navigating the Frontier
Orbital has developed several tactics to navigate the [[challenges_and_strategies_in_ai_production | challenges and strategies in AI production]]:

*   **Model Migration Strategy (System 1 vs. System 2)** <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>:
    *   **Specificity**: System 1 models required specific instructions on *how* to accomplish tasks; System 2 models need only a clear objective of *what* to do <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.
    *   **Leaner Instructions**: Repetitive instructions needed for System 1 models can be removed for System 2 models <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.
    *   **Unblocking the Model**: System 2 models prefer fewer constraints, allowing them time to reason and rationalize <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.
*   **Leveraging System 1 Models**: While System 2 models are favored, System 1 models can be cheaper and faster <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. Their "thought tokens" provide valuable explanability for users and aid in debugging when issues arise <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.
*   **Feature Flags for AI Model Upgrades**: Similar to progressive rollouts in software development, feature flags can mitigate risk when introducing new AI models <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
*   **Addressing Change Aversion Bias**: Users inherently feel more anxiety towards new systems due to unknown potential downsides, even if the previous system had known flaws <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>. Simply announcing a new model can heighten awareness and lead users to seek out issues <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.
*   **Team Mantra: "Bet on the Model"**: The team's mantra encourages imagining where AI models will be in 3, 6, or 12 months and building features that will improve as models become smarter, cheaper, and faster <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>. This future-oriented approach prevents stagnation and fosters growth <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>.
*   **Using System 2 Models for Prompt Migration**: New, more capable System 2 models can assist in migrating older, domain-specific prompts, drastically reducing manual human effort <a class="yt-timestamp" data-t="15:44:00">[15:44:00]</a>.
*   **Making Tough Calls and Shipping**: Despite the uncertainty of probabilistic models, teams must be brave enough to take risks, ship, and deal with consequences post-release, mitigating risks along the way <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
*   **Strong Feedback Loop**: Building systems that allow real-time user feedback (e.g., thumbs up/down) to reach AI engineers and domain experts quickly is crucial <a class="yt-timestamp" data-t="17:10:00">[17:10:00]</a>. This enables rapid identification of issues, prompt changes, and deployment of fixes, often within minutes or hours <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>.

## The Evolving Landscape and Future of AI Engineering
Demis Hassabis, CEO of Google DeepMind, highlights that the underlying AI tech stack is evolving incredibly fast, making it uniquely challenging for product development across companies of all sizes <a class="yt-timestamp" data-t="18:14:00">[18:14:00]</a>. This demands "deeply technical product people" who can predict where the technology will be in a year to design future-proof products <a class="yt-timestamp" data-t="19:05:00">[19:05:00]</a>.

This environment creates an opportunity for "product AI engineers" who understand both technical capabilities and customer problems, translating model capabilities into solutions for real user problems <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>.

## Paying the Prompt Tax: The "Ship Now" Imperative
The overarching question in this environment is: what gives teams more confidence to ship at the AI frontier <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>? As agentic product surface areas grow, the "vibes over evals" approach may become harder to scale <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>.

The [[challenges_in_building_ai_applications | challenges in building AI applications]] are exacerbated by the complexity of evaluating LLMs, especially in fields like real estate legal, where correctness, style, conciseness, and citation accuracy are all critical <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>. Creating comprehensive evaluation systems for all edge cases can be prohibitively expensive, slow, and potentially impossible given product velocity <a class="yt-timestamp" data-t="22:11:00">[22:11:00]</a>.

### Progressive Delivery
Progressive delivery offers a potential path forward: "upgrade now and fix on the fly" <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>. This involves rolling out new models internally first, then to a limited number of progressive users, incrementally scaling up based on feedback <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>. The goal is to calibrate the rollout based on feedback, scaling up until internal teams are swamped, then dialing back, until feedback is minimal at 100% user adoption <a class="yt-timestamp" data-t="22:50:00">[22:50:00]</a>.

The central thesis is that to stay on the edge of the AI frontier and maximize opportunities, companies must "buy now" – ship new capabilities into their agentic products and into users' hands <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>. While the prompt tax might seem daunting, the anxiety may not always be warranted, and progressive rollout tactics can mitigate downside risks <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>. Staying on the frontier means prioritizing shipping, even if the "payment" of the prompt tax is determined on a case-by-case basis <a class="yt-timestamp" data-t="24:23:00">[24:23:00]</a>.