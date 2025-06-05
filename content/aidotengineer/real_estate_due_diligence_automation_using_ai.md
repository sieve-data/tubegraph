---
title: Real estate due diligence automation using AI
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

Orbital is a company with offices in New York and London, whose mission is to [[ai_in_workflow_automation | automate]] real estate due diligence to accelerate property transactions <a class="yt-timestamp" data-t="02:01:06">[02:01:06]</a>. This process is critical because homes and offices are constantly developed, bought, and sold, involving real estate lawyers in due diligence <a class="yt-timestamp" data-t="02:08:46">[02:08:46]</a>.

## The Problem: Manual Due Diligence
Traditionally, real estate lawyers perform due diligence by reading "mountains of paperwork" and "hunting for needles in a haystack" to identify red flags for clients before transactions can proceed <a class="yt-timestamp" data-t="02:17:40">[02:17:40]</a>. This manual process is time-consuming and inefficient <a class="yt-timestamp" data-t="02:19:12">[02:19:12]</a>.

## The Solution: Orbital Copilot
Orbital developed an [[building_and_leveraging_ai_for_automated_problem_solving | agentic system]] called Orbital Copilot, launched in January 2024, which "thinks like a real estate lawyer" <a class="yt-timestamp" data-t="03:17:34">[03:17:34]</a>. This [[ai_in_workflow_automation | Agentic software]] significantly reduces the time required to find critical information and compile necessary paperwork for real estate transactions <a class="yt-timestamp" data-t="02:29:08">[02:29:08]</a>.

### How it Works
The Orbital Copilot demo illustrates the automation of a long-running task previously performed manually by lawyers <a class="yt-timestamp" data-t="03:46:04">[03:46:04]</a>:
1.  **Report Selection and Document Upload** <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>: Users select a report type (e.g., occupational lease) and upload documents (e.g., deed, lease) <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
2.  **OCR and Structuring** <a class="yt-timestamp" data-t="04:17:28">[04:17:28]</a>: The system first performs Optical Character Recognition (OCR) on documents containing handwritten and typed text to structure the data <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
3.  **Agentic Task Execution** <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>:
    *   The [[building_and_leveraging_ai_for_automated_problem_solving | agentic system]] creates a plan, breaking it into many subtasks <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.
    *   Each subtask is its own [[building_and_leveraging_ai_for_automated_problem_solving | agentic system]] involving multiple LLM calls <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.
    *   The system is given objectives, such as finding the lease date or current annual rent <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
    *   It reads legal documents to find appropriate answers <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
4.  **Report Generation and Review** <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>: Once all subtasks are complete, a final report is generated for manual review by a lawyer <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>. Citations can be clicked to go back to the original ground truth <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
5.  **Download and Client Delivery** <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>: The final word report can be downloaded, stored, and sent to a client to progress the transaction <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

## Impact and Results
Since commercializing its [[building_and_leveraging_ai_for_automated_problem_solving | agentic agent]] 18 months ago, Orbital has seen significant growth <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>:
*   **Token Consumption:** From burning less than a billion tokens monthly to consuming almost 20 billion tokens every month on behalf of real estate lawyers <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. This represents 20 billion tokens worth of work previously done manually <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
*   **Revenue Growth:** From zero revenue to multiple seven figures in annual recurring revenue, which continues to scale <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

## Technical Approach and Challenges
Orbital's journey involved migrating through various LLM models, starting from GPT-3.5 and moving through GPT-4 32K, 4 Turbo 40, 4.1, and system 2 models like 01 preview to 04 mini <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.

### Key Decisions
1.  **Optimize for Prompting over Fine-tuning:** This approach maximized development speed, allowing real-time adjustments to prompts based on user feedback to quickly incorporate changes and find product-market fit <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
2.  **Heavy Reliance on Domain Experts:** Private practice real estate lawyers, with decades of experience, are embedded in the team and write many prompts <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. They effectively teach the [[building_and_leveraging_ai_for_automated_problem_solving | AI system]] their expertise <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
3.  **"Vibes over Evals":** While an evaluation system is on the roadmap, Orbital has achieved significant growth in tokens, revenue, and user feedback largely based on subjective human testing by domain experts before release <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>. This involves subjective feel, logging regressions in spreadsheets, but nothing "terribly comprehensive" <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.

### Prompt Taxonomy
Prompts are categorized into two areas <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>:
*   **[[building_and_leveraging_ai_for_automated_problem_solving | Agentic]] Prompts:** Owned by [[ai_in_workflow_automation | AI engineers]], these are system prompts that help the model choose which tools to use and when <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.
*   **Domain-Specific Prompts:** Used by real estate lawyers to impart real estate expertise to the system <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. The number of these prompts has grown from near zero to over 1,000 <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.

### The "Prompt Tax"
The increase in prompts leads to a "prompt tax" <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. When a new [[leveraging_ai_tools_for_efficiency_and_scalability | AI model]] is released, Orbital rigorously experiments with it <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>. This involves:
*   Unlocking envisioned features with new capabilities <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.
*   Assessing the "prompt tax" required to migrate existing prompts <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.
*   Dealing with inherent fear due to unknown unknowns when shipping a new [[leveraging_ai_tools_for_efficiency_and_scalability | AI model]] <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.

The "prompt tax" is distinct from technical debt; it's the cost of upgrading to new models that offer new capabilities but also introduce uncertainty about what will improve or break <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>.

### Battle-Tested Tactics
Orbital has developed several tactics for navigating the rapidly evolving [[leveraging_ai_tools_for_efficiency_and_scalability | AI landscape]] <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>:
*   **Adapting Prompts for System 2 Models:** For newer, more capable models (System 2 like 01 preview), prompts need to be less specific, leaner, and avoid repeating instructions, focusing on clearly stating *what* to do rather than *how* <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>. They also benefit from being "unblocked" with clear objectives and time to reason <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.
*   **Utilizing Thought Tokens:** Though System 1 models are often cheaper and faster, their thought tokens can be embedded for user explainability (especially useful for real estate lawyers needing to understand complex legal reasoning) or for debugging <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.
*   **Progressive Rollout with Feature Flags:** Similar to software development, new AI model upgrades can be rolled out progressively to mitigate risk, though "change aversion bias" can heighten anxiety <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
*   **"Betting on the Model":** The team mantra is to anticipate future [[leveraging_ai_tools_for_efficiency_and_scalability | AI model]] advancements (smarter, cheaper, faster, more capabilities) and build features that will improve as models become more capable <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.
*   **Using System 2 Models for Prompt Migration:** Newer models, being inherently more capable, can assist in migrating older domain-specific prompts, significantly reducing manual human effort <a class="yt-timestamp" data-t="15:45:00">[15:45:00]</a>.
*   **Decisive Shipping:** Given the probabilistic nature and uncertainty of new [[leveraging_ai_tools_for_efficiency_and_scalability | AI models]], teams need to be brave enough to ship and deal with consequences, mitigating risks along the way <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
*   **Strong Feedback Loops:** Rapid feedback from users (manual or via in-product UX like thumbs up/down) is crucial <a class="yt-timestamp" data-t="17:10:00">[17:10:00]</a>. This feedback is sent to [[ai_in_workflow_automation | AI engineers]] and domain experts, allowing prompt changes and production deployments in minutes or hours <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>.

### The Challenge of Rapid Technological Evolution
Deis Havaris, Chief Exec of Google DeepMind, highlights that the underlying [[leveraging_ai_tools_for_efficiency_and_scalability | AI tech stack]] is evolving "unbelievably fast," unlike previous revolutionary technologies <a class="yt-timestamp" data-t="18:17:00">[18:17:00]</a>. This poses a unique challenge for product development, as companies must decide what to "bet on" when the technology could be "100% better in a year" <a class="yt-timestamp" data-t="18:55:00">[18:55:00]</a>. This requires deeply technical product people who understand where the technology might go to design future-proof products <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.

## Paying the Prompt Tax: Future Considerations
The meta-question for [[building_and_leveraging_ai_for_automated_problem_solving | agentic product]] developers is how to gain more confidence when shipping at the [[leveraging_ai_tools_for_efficiency_and_scalability | AI frontier]] <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>. While Orbital has scaled successfully on "vibes" (human review and rapid feedback), it's uncertain if this will scale indefinitely as the product surface area grows <a class="yt-timestamp" data-t="21:03:00">[21:03:00]</a>.

The possibility of an evaluation (eval) system is considered <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>. However, the complexity of evaluating LLM outputs in real estate legal contexts (correctness, style, conciseness, citation accuracy, edge cases vs. happy paths) makes building a comprehensive eval system prohibitively expensive and slow, possibly an impossible task given rapid product velocity <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>.

### Progressive Delivery
A potential way forward is progressive delivery, rolling out new models internally first, then to a limited number of users, and incrementally scaling up based on feedback <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>. This allows for "fixing on the fly" <a class="yt-timestamp" data-t="22:39:00">[22:39:00]</a>.

### Conclusion
To stay at the [[leveraging_ai_tools_for_efficiency_and_scalability | AI frontier]] and maximize opportunities from new model capabilities, it's essential to ship products and get them into users' hands quickly <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>. The "prompt tax" (the cost of adapting to new models) and anxiety over potential downsides may not always materialize, or can be managed through strategies like incremental rollouts and rapid feedback loops <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.