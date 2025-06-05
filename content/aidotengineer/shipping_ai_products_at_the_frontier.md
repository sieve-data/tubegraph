---
title: Shipping AI Products at the Frontier
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

Shipping products at the AI frontier involves a constant tension between the opportunities new AI models present and the risks of introducing regressions or unintended consequences into existing products <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This environment requires a deep understanding of evolving AI capabilities and strategic decision-making <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.

## The Pain of Progress and Prompt Tax

Developing with the rapid pace of AI model releases from companies like Anthropic, Google Gemini, and [[openais_approach_to_ai_deployment_and_enterprise_integration | OpenAI]] feels like having a birthday every month, with a plethora of new additions and functionalities <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. However, integrating these advances into applications introduces a "hidden prompt tax" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This tax refers to the unexpected consequences of using probabilistic AI systems that can behave unpredictably <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Shipping at the AI Frontier: Orbital's Experience

Orbital, a company with offices in New York and London, aims to [[scaling_ai_solutions_in_production | automate real estate due diligence]] to fast-forward property transactions <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Their [[scaling_ai_agents_in_production | agentic software]] significantly reduces the time required for lawyers to find critical information and compile paperwork for real estate transactions <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Orbital Co-pilot: An Agentic Product

In January 2024, Orbital launched "Orbital Co-pilot," their first [[scaling_ai_agents_in_production | agentic product]] designed to think like a real estate lawyer <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The product processes mountains of paperwork by first using OCR to structure documents, then an [[scaling_ai_agents_in_production | agentic system]] creates and executes a plan broken into subtasks, each involving multiple LLM calls to extract specific information like lease dates or annual rent <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. It provides citations for easy manual review by lawyers <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Since its commercialization 18 months prior to the discussion, Orbital's [[scaling_ai_agents_in_production | agentic product]] has seen substantial growth:
*   **Token Consumption**: Increased from less than a billion tokens to nearly 20 billion tokens consumed monthly on behalf of real estate lawyers <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This represents 20 billion tokens worth of work previously done manually <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Revenue**: Scaled from zero to multiple seven figures in annual recurring revenue <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Team Structure

Orbital's product engineering team, approximately 40 people, is structured with a product manager, designer, embedded domain experts (private practice real estate lawyers), software engineers, AI engineers, and a tech lead <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Model Migration and Strategic Decisions

Orbital has continuously migrated across various models, starting with GPT-3.5, then moving through System 1 models like GPT-4 32K (which enabled agentic systems due to its increased context window) and 4 Turbo, and eventually to System 2 models including 01 preview and 04 mini <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

Key decisions made during this process include:
*   **Optimizing for Prompting over Fine-tuning**: This choice maximized development speed, allowing real-time adjustments based on user feedback and rapid incorporation of changes into the [[scaling_ai_agents_in_production | agentic system]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Heavy Reliance on Domain Experts**: Experienced real estate lawyers write many of the prompts, translating decades of their expertise into the AI system <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **"Vibes over Evals"**: Despite the popularity of evaluation systems, Orbital primarily relies on human testing by domain experts before release, sometimes logging subjective feelings or basic regressions, rather than a rigorous objective evaluation system <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. The product's growth in tokens, revenue, and user feedback has validated this approach so far <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

Prompts are categorized into:
*   **Agentic Prompts**: Owned by AI engineers, these are system prompts that help the model choose and use tools <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Domain-Specific Prompts**: Used by real estate lawyers to instill domain expertise into the system <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. The number of domain-specific prompts has grown from near zero to over 1,000, which contributes to the "prompt tax" <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

When a new AI model is released, Orbital's team rigorously experiments with it to unlock new features or gain inspiration <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. They also assess the "prompt tax" required to migrate existing prompts to the new model and manage the inherent fear of unknown consequences <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

## Prompt Tax vs. Technical Debt

Prompt tax is distinct from technical debt. Technical debt often arises from optimizing for quick shipping with the intent to fix issues later <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Prompt tax, however, stems from the desire to upgrade to new models immediately to unlock valuable capabilities, despite the uncertainty of what might improve or break <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. The goal is to fix things on the fly and roll out new models optimally to maximize benefits while mitigating risks of regression <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

## Battle-Tested Tactics for Shipping AI Products

Orbital has developed several tactics:

### Adapting to System 1 vs. System 2 Models
*   **System 1 Models (e.g., GPT-4)**: Required specific instructions on *how* to accomplish tasks and often needed repeated instructions to ensure adherence <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **System 2 Models (e.g., 01 preview)**: Required stripping out specificity, making prompts leaner, and simply stating *what* to do. They perform better with clear objectives and freedom to reason through permutations <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Leveraging Thought Tokens
System 1 models often generate "thought tokens" which can be embedded for users to provide explainability (especially valuable for complex legal matters) or used by developers for debugging when issues arise <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

### Progressive Rollouts and Change Aversion Bias
Similar to feature flags in software development, new AI model upgrades can be progressively rolled out <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. However, a "change aversion bias" exists, where users have more anxiety about a new system (even if it's better) simply because it's unknown, leading them to actively look for issues <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This means simply announcing a change can heighten awareness and make perceived issues outweigh positives <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### Betting on the Model
The team mantra is "betting on the model," meaning product features should be designed with an eye towards where AI models will be in 3, 6, or 12 months – smarter, cheaper, faster, and with more capabilities <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. This ensures the product grows with AI advancements rather than stagnating <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

### Using System 2 Models for Prompt Migration
New System 2 models can be used to help migrate older domain-specific prompts, as they often "know themselves" and can suggest optimal adjustments, drastically reducing manual effort <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

### Making Tough Calls and Embracing Uncertainty
Given the probabilistic nature and new capabilities of AI models, there's inherent uncertainty when moving between them <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>. It requires a person or team willing to take on the risk, make the call to ship, and deal with consequences post-shipping, mitigating risks along the way <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Bravery is needed to overcome anxiety and ship <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

### Establishing Strong Feedback Loops
A robust feedback loop is crucial <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. Feedback, whether manual or collected via in-product UX (e.g., thumbs up/down), should be immediately sent to AI engineers and domain experts <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Orbital's system allows domain experts to evaluate feedback, identify necessary prompt changes, and push fixes to production in minutes or hours, resolving issues for all users <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

### The Challenge of a Rapidly Evolving Tech Stack
Deis Havaris, CEO of Google DeepMind, highlights that the underlying AI tech stack is evolving at an unbelievably fast pace, unlike previous revolutionary technologies like the internet or mobile <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. This presents a unique challenge for product development, as companies must decide what to "bet on" when the technology could be 100% better in a year <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. It necessitates "deeply technical product people" (product designers and managers) who can anticipate where the technology will be in the future to design products that leverage those future capabilities <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

### The Rise of Product AI Engineers
There's a significant opportunity for "product AI engineers" who understand customer problems and can connect technical capabilities of models to solve real user problems <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. Having this "connective tissue" embedded within an AI engineer or team is a promising proposition for the future of the AI engineering community <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.

## Paying the Prompt Tax: Shipping with Confidence

The meta-question for those building [[scaling_ai_agents_in_production | agentic systems]] is how to gain more confidence to ship at the [[state_of_the_ai_frontier_in_2025 | frontier]] as AI advances and product surface areas expand <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. While Orbital has built its product mostly on "vibes" (human testing and rapid feedback) so far <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>, the question remains whether this scales indefinitely as product complexity grows <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

### The Role of Eval Systems
An evaluation system might alleviate some of this concern, but for complex LLM applications with numerous edge cases (e.g., correctness, style, conciseness, citation accuracy in legal contexts), building a comprehensive eval system can be prohibitively expensive, slow, and potentially impossible to maintain alongside rapid product velocity <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

### Progressive Delivery as a Solution
Progressive delivery is a potential way forward: "upgrade now and fix on the fly" <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. This involves rolling out new models internally first, then to a limited number of progressive users, scaling up incrementally based on feedback <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. The rollout can be calibrated by the amount of feedback received, dialing it back if internal teams are swamped, until feedback is minimal <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

The central thesis for staying on the [[state_of_the_ai_frontier_in_2025 | AI frontier]] is to "buy now" – ship new models and capabilities into [[scaling_ai_agents_in_production | agentic products]] and get them into users' hands <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. The anxiety about potential downsides may not materialize, or progressive rollout tactics can manage the "payment" of prompt tax by addressing issues incrementally <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

This approach ensures continuous innovation and maximizes the opportunities presented by new AI models, even if the exact cost of the prompt tax is determined on a case-by-case basis after shipping <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.