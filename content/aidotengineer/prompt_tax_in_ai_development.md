---
title: Prompt Tax in AI Development
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

Developing agentic systems today introduces the concept of "prompt tax" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This concept describes the challenges and hidden costs associated with shipping products at the frontier of AI, where advancements are rapid, and the underlying models are constantly evolving <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## The Pain of Progress
The pace of AI model development is breathtaking, with new releases from labs like Anthropic, Google Gemini, and OpenAI occurring frequently <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. While these advances offer incredible opportunities to [[developing_custom_ai_tools_and_functions | bolt new functionality into applications]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, they also come with unintended consequences, as these probabilistic systems can behave unexpectedly <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This creates a constant tension between the opportunities new AI models present and the risks of introducing regressions or unforeseen issues into products <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### What is Prompt Tax?
Prompt tax is a hidden cost incurred when integrating new AI model functionalities into existing applications <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Unlike technical debt, which is often a trade-off for shipping quickly, prompt tax arises from the *desire* to upgrade to new models that unlock new capabilities <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The core challenge is the inherent uncertainty: you don't know exactly what will improve or what will break when a new model is implemented <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

As the number of domain-specific prompts in an agentic system grows, the "prompt tax" increases <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. When a new AI model is released, teams must:
1.  **Experiment rigorously:** Determine if the new model unlocks envisioned features or inspires new ideas <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
2.  **Assess prompt migration effort:** Understand the "prompt tax" required to adapt existing prompts to the new model <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
3.  **Address inherent fear:** Mitigate the anxiety caused by unknown unknowns when shipping a new AI model <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## Case Study: Orbital's Agentic System
Orbital, a company focused on automating real estate due diligence, provides a practical example of navigating the prompt tax <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Their agentic software, Orbital Co-Pilot, streamlines the process of reading legal documents and compiling information that lawyers previously performed manually <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

**Orbital's Journey and AI Model Evolution:**
Orbital has evolved its AI models significantly, starting with GPT-3.5 and moving through various versions of GPT-4, including 32K and Turbo 40, and also adopting "System 2" models like 01 preview and 04 mini <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

**Strategic Decisions:**
1.  **Optimizing for Prompting over Fine-tuning:** Orbital prioritized prompting to maximize development speed. This allowed them to quickly incorporate user feedback by adjusting prompts in real-time, especially crucial for finding product-market fit <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
2.  **Heavy Reliance on Domain Experts:** Real estate lawyers with decades of experience write many of the domain-specific prompts, effectively teaching the AI system their expertise <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
3.  **"Vibes over Evals":** While rigorous evaluation systems are ideal, Orbital has largely relied on subjective human feedback from domain experts to test systems prior to release, demonstrating significant growth in tokens, revenue, and user satisfaction <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This approach, however, faces scalability challenges as the product's surface area grows <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.

**Prompt Categories:**
Orbital's prompts fall into two main areas:
*   **Agentic Prompts:** Owned by AI engineers, these are system prompts that help the model choose and use tools <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Domain-Specific Prompts:** Used by real estate lawyers to teach the system expertise in the real estate domain <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. The number of these prompts has grown from near zero to over 1,000 <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Battle-Tested Tactics for Managing Prompt Tax

### Migrating Between System Models
When migrating from "System 1" models (e.g., GPT-40) to "System 2" models (e.g., 01 preview):
*   **Specify "What to Do" not "How to Accomplish":** System 2 models do not require specific instructions on *how* to perform a task; just define the objective <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Leaner Prompts:** Remove repetitive instructions previously needed for System 1 models <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Unblock the Model:** Avoid too many constraints with System 2 models. Give them a clear objective and allow them time to reason and plan <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Leveraging Model Strengths
*   **Thought Tokens for Debugging and Explainability:** While System 2 models are often preferred, System 1 models can be cheaper and faster <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. Their "thought tokens" can provide valuable insights for debugging or explaining complex legal matters to users <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Using System 2 Models for Prompt Migration:** Newer models can help migrate older domain-specific prompts to their own format, significantly reducing manual effort <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

### Deployment and Risk Mitigation
*   **Feature Flags for AI Model Upgrades:** Similar to software development, progressively rolling out new AI model upgrades with feature flags can mitigate risk <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   **Overcoming Change Aversion Bias:** Users often feel more anxiety towards a new system, even if it's superior, simply due to familiarity with the old one <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Articulating a change can heighten awareness of issues, sometimes outweighing the positives <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   **"Betting on the Model":** Teams should anticipate future AI model capabilities (smarter, cheaper, faster) and design features that will improve as models evolve. This prevents stagnation and allows products to grow with the models <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### Managing Uncertainty and Feedback
*   **Brave Shipping:** Given the probabilistic nature of AI models and the uncertainty of new capabilities, a team must be willing to "ship and then deal with the consequences" <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>. Mitigate risks, but overcome the inherent anxiety to get new models to users <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   **Strong, Fast Feedback Loops:** Implement systems that allow users to provide feedback directly (e.g., thumbs up/down) <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This feedback should be routed to AI engineers and domain experts quickly, enabling prompt changes and deployment to production within minutes or hours, rather than days or weeks <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   **Progressive Delivery (Upgrade Now, Fix on the Fly):** Roll out new models incrementally—internally, then to a limited user group, and gradually scale up <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. Adjust calibration based on feedback, scaling up until the feedback becomes minimal <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

## The Future of AI Engineering

Deis Havaris, CEO of Google DeepMind, emphasizes the unique challenge of the AI space: the underlying tech stack is evolving incredibly fast, unlike past revolutionary technologies that stabilized sooner <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. This means product designers and managers need a deep technical understanding to anticipate where technology will be in a year <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.

This presents a significant opportunity for "product AI engineers" – individuals or teams who understand customer problems and can connect the technical capabilities of models with real user needs <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Their ability to turn new model features into product solutions is incredibly promising for the future of the [[developing_custom_ai_tools_and_functions | AI engineering community]] <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

### Scaling Confidence
While "vibes" (subjective evaluation) have worked for Orbital thus far, the question remains whether this approach will [[scaling_ai_solutions_in_production | scale]] as the product's surface area increases <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. Evaluation (eval) systems are often seen as the answer, potentially alleviating challenges <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. However, for complex domains like real estate legal, evaluating correctness, style, conciseness, and citation accuracy across numerous prompts and edge cases can be prohibitively expensive, slow, and potentially impossible to keep pace with product velocity <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

To stay on the edge of the AI frontier and maximize opportunities, the emphasis is on **shipping now** <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. The anxiety about potential downsides may not materialize, or the [[impact_of_ai_on_development_workflow | progressive delivery]] approach of incremental rollouts and quick fixes can mitigate risks, ensuring that the benefits of new AI models are realized <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.