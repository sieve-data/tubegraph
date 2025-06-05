---
title: Balancing Progress and Risks in AI
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

Developing and shipping AI products at the frontier involves a "prompt tax" – the hidden costs and challenges associated with incorporating rapidly evolving AI models into applications <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This concept highlights the tension between the opportunities new AI models offer and the risks of introducing regressions or unintended consequences into products <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## The Pain of Progress

The pace of AI model releases is akin to having a birthday every month, with new advancements from major labs like Anthropic, Google Gemini, and OpenAI <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. While these [[advancements_in_ai_and_future_implications | advancements in AI]] offer incredible new functionality to integrate into applications, they also come with "unintended consequences" due to the probabilistic nature of these systems, which can behave unexpectedly <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Understanding the Prompt Tax

The prompt tax is distinct from technical debt <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Technical debt often involves optimizing for quick shipping with the intention to fix later, or dealing with prototypes that become core products and require rebuilding <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. In contrast, the prompt tax arises from the desire to upgrade to new models immediately to unlock new capabilities <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The challenge lies in the unknowns: it's unclear what will improve and what will break with each new model <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This requires a strategy of "fixing on the fly" and optimally releasing new models to users to gather feedback and mitigate risks <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

## Case Study: Orbital's Experience

Orbital, a company with offices in New York and London, aims to automate real estate due diligence to expedite property transactions <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This involves using AI to read extensive paperwork and find "red flags" for clients, a process traditionally done manually by real estate lawyers <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Their agentic software, "Orbital Co-pilot," supercharges this process by radically reducing the time to find crucial information <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Product Demonstration: Orbital Co-pilot

Orbital Co-pilot automates the manual tasks of lawyers, such as reading paperwork and compiling extracted information <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The process includes:
1.  Selecting a report type, such as an occupational lease report <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
2.  Uploading documents, like a deed and a lease (e.g., 100 pages total) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  OCR (Optical Character Recognition) of documents with handwritten and typed text to structure them <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
4.  The agentic system creating a plan, breaking it into subtasks, and using multiple LLM calls to find objectives (e.g., lease date, annual rent) by reading legal documents <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
5.  After completion, a final report can be quickly reviewed by a lawyer, with clickable citations to the "ground truth" documents <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
6.  The report can then be downloaded and sent to clients <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Growth and Evolution
Over 18 months, Orbital's agentic system has scaled significantly:
*   From burning less than a billion tokens to consuming almost 20 billion tokens monthly <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This represents 20 billion tokens worth of work previously done manually by lawyers, now automated <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   Revenue has grown from zero to multiple seven figures in annual recurring revenue <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

The company has migrated through various AI models, from GPT-3.5 and GPT-4 32K (which enabled agentic systems due to its increased context window) to 4 Turbo 40, 4.1, and system 2 models like 01 preview and 04 mini <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Key Development Decisions
Orbital made three key decisions in their AI development:
1.  **Optimize for Prompting Over Fine-Tuning**: This maximized development speed, allowing real-time prompt adjustments based on user feedback to be incorporated quickly, especially for finding product-market fit <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This is a [[best_practices_for_building_ai_systems | best practice for building AI systems]] to achieve rapid iteration.
2.  **Heavy Reliance on Domain Experts**: Private practice real estate lawyers with decades of experience write many of the prompts, imparting their expertise to the AI system <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
3.  **"Vibes Over Evals"**: Despite evaluation systems being popular, Orbital has primarily relied on subjective testing by human domain experts prior to release, focusing on a general "feel" of the system's performance, sometimes logging regressions in spreadsheets <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This approach, while less rigorous, has supported their rapid growth <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Prompt Management
Orbital categorizes prompts into two areas:
*   **Agentic prompts**: Owned by AI engineers, these are system prompts that help the model choose when and which tools to use <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Domain-specific prompts**: Used by real estate lawyers, these teach the system its expertise in the real estate domain <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

The number of domain-specific prompts has grown from near zero to over 1,000, creating a challenge where "more prompts equals more prompt tax" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Shipping at the AI Frontier

When a new AI model is released, the process involves rigorous experimentation by AI engineers and domain experts to unlock envisioned features or inspire new ideas <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. A key concern is assessing the prompt tax required to migrate existing prompts to the new model <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. There is an inherent fear of "unknown unknowns" when shipping a new AI model, which needs to be pinpointed and mitigated <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## Battle-Tested Tactics for Managing Prompt Tax

Orbital has developed several [[best_practices_for_building_ai_systems | best practices for building AI systems]] and managing the prompt tax over 18 months:

### Model Migration Strategies
*   **System 1 vs. System 2 Models**: When migrating from System 1 models (e.g., GPT-40) to System 2 models (e.g., 01 preview), the approach to prompts changes:
    *   System 1 models require specific instructions on *how* to accomplish tasks <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   System 2 models only need specification of *what* to do, with leaner prompts and fewer repeated instructions <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
    *   System 2 models thrive when "unblocked" – given clear objectives and time to reason and find appropriate plans without excessive constraints <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Enhancing Explainability and Debugging
*   **Thought Tokens**: Even with System 2 models, System 1 models can be useful for their thought tokens, which can be embedded for user explainability (especially in complex domains like real estate law) or used for debugging when something goes wrong <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

### Mitigating Risk in Deployment
*   **Feature Flags**: Similar to software development, feature flags can be used to progressively roll out new AI model upgrades, mitigating risk <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   **Addressing Change Aversion Bias**: There is often more anxiety associated with moving to a new system than staying with a known one, even if the new system has benefits <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Simply announcing a new model can heighten awareness and lead users to seek out issues, potentially outweighing the positives <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### Strategic Product Development
*   **"Betting on the Model" Mantra**: This involves designing products not just for current AI capabilities but anticipating future improvements in intelligence, cost, speed, and capabilities (3, 6, or 12 months out) <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. This allows products to grow with the models rather than stagnating <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Using System 2 Models for Prompt Migration**: Newer, more capable models can be used to help migrate domain-specific prompts originally created for older models, significantly reducing manual human effort <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. This aids in [[challenges_and_innovations_in_ai_engineering | challenges and innovations in AI engineering]].

### Decision-Making and Feedback
*   **Making Tough Calls and Shipping**: Given the uncertainty of probabilistic models and new capabilities, a team needs to be brave enough to take the risk, ship the product, and deal with consequences post-release, rather than being paralyzed by anxiety <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   **Strong Feedback Loop**: Establishing a rapid feedback loop, whether manual or built into the product's UX (e.g., thumbs up/down), is crucial <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. Feedback should quickly reach AI engineers and domain experts so they can identify prompt changes and ship fixes to production within minutes or hours, resolving issues for all users <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

## Expert Insights: Demis Hassabis on the Evolving Tech Stack

Demis Hassabis, CEO of Google DeepMind, highlights that the "underlying tech is moving unbelievably fast," which differs from previous revolutionary technologies like the internet or mobile, where the tech stack eventually stabilized <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. This constant evolution makes [[challenges_with_current_ai_implementation | current AI implementation uniquely challenging]] for product development, as what is 100% better in a year is unknown <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. It necessitates "deeply technical product people" who can predict where the technology will be in a year to design products that leverage future capabilities <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. When something works, there's a need to "double down quick" <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

## The Future of AI Engineering

There's a significant opportunity for "product AI engineers" who understand both customer problems and the capabilities of AI models <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. This connective tissue between technical understanding and user needs is incredibly promising for turning model capabilities into real-world product features that solve user problems <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

## Paying the Prompt Tax (or Shipping Now)

The meta-question for shipping at the AI frontier is what provides more confidence <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. As AI evolves and agentic product surface areas grow, maintaining confidence is key to continued [[advancements_in_ai_and_future_implications | innovation]] <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.

While Orbital has largely built its product on "vibes" complemented by real-time user feedback and rapid tooling, the question remains whether this approach will [[scaling_ai_solutions_in_production | scale AI solutions in production]] as the product surface area increases <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. An evaluation system could be an answer, potentially alleviating concerns and allowing further progress <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. However, evaluating complex aspects like correctness, style, conciseness, and citation accuracy across numerous edge cases for probabilistic LLMs can be prohibitively expensive, slow, and potentially impossible to keep pace with product velocity <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. This relates directly to [[ensuring_ai_accuracy_and_reducing_errors | ensuring AI accuracy and reducing errors]].

### Progressive Delivery
Progressive delivery is a potential way forward, embodying the "upgrade now and fix on the fly" approach <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. This involves:
*   Rolling out internally first <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
*   Then to a limited number of progressive users <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>.
*   Incrementally scaling up to 50% or 100% of users over time, calibrated by feedback volume <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>. This minimizes downside risks while maximizing benefits of new AI models <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

The central thesis for staying at the edge of the AI frontier and maximizing opportunities is to "buy now" – ship new models into agentic products and user hands quickly <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. The anxiety about potential downsides may not materialize, or progressive rollout tactics can manage feedback and fixes incrementally <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This highlights the [[challenges_and_opportunities_in_ai_adoption | challenges and opportunities in AI adoption]] and the [[challenges_and_opportunities_in_ai_and_agent_capabilities | challenges and opportunities in AI and agent capabilities]].