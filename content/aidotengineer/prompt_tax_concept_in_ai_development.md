---
title: Prompt tax concept in AI development
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

The "prompt tax" is a concept introduced for builders of agentic systems, referring to the hidden costs and unintended consequences of incorporating new AI model functionalities into applications <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It arises from the rapid advancement of AI models, which constantly introduce new capabilities but also bring the risk of regressions or unexpected behaviors in probabilistic systems <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This creates a tension between seizing new opportunities and mitigating risks when shipping products at the AI frontier <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## The Pain of Progress

Developing with the rapid pace of AI model progress feels like having a birthday every month, with major labs like Anthropic, Google Gemini, and OpenAI frequently releasing new models and functionalities <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This constant innovation, while beneficial, leads to the "hidden prompt tax" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Orbital's Experience at the AI Frontier

Orbital, a company with offices in New York and London, aims to automate real estate due diligence to expedite property transactions <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Their agentic software helps lawyers by radically reducing the time needed to find "needles in a haystack" within mountains of paperwork and compile necessary documents for real estate transactions <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Orbital Co-Pilot: An Agentic Product

In January 2024, Orbital developed its first agentic product, "Orbital Co-pilot," designed to think like a real estate lawyer <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
The product workflow involves:
1.  Selecting a report type <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  Uploading documents (e.g., deed, lease) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  OCR processing of documents with handwritten and typed text <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
4.  The agentic system creating a plan, breaking it into subtasks, each acting as its own agentic system with multiple LLM calls <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
5.  The system reading legal documents to find specific information (e.g., lease date, annual rent) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
6.  Generating a final report that lawyers can review quickly, with clickable citations to the source documents <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
7.  Downloading the report for storage and client delivery <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Since its commercialization 18 months prior, Orbital's agentic system has seen significant growth:
*   Token consumption: From less than 1 billion tokens to almost 20 billion tokens per month <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This 20 billion tokens worth of work was previously done manually by lawyers <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   Revenue: Scaled from zero to multiple seven figures in annual recurring revenue <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Model Migration and Key Decisions

Orbital has migrated through various models, starting with GPT-3.5 and progressing through GPT-4 versions (32K, Turbo 40, 4.1) and System 2 models (01 preview to 04 mini) <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

Three key decisions were made:
1.  **Optimize for prompting over fine-tuning**: This maximized the speed of development, allowing real-time prompt adjustments based on user feedback to be quickly incorporated <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
2.  **Heavy reliance on domain experts**: Private practice real estate lawyers with decades of experience write many prompts, teaching the AI system their expertise <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
3.  **"Vibes over evals"**: While an evaluation system is on the roadmap, growth has been driven by subjective human testing by domain experts and user feedback, rather than a rigorous, objective evaluation system <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Issues are sometimes logged in spreadsheets to track regressions from prior model changes, but the process is largely subjective <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

Orbital's prompts are divided into:
*   **Agentic prompts**: Owned by AI engineers, these are system prompts that help the model choose and use tools <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Domain-specific prompts**: Used by real estate lawyers to instill real estate expertise into the system <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

The number of domain-specific prompts has grown from near zero to over 1,000 <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. The [[cost_management_in_ai_projects | challenge]] is that "more prompts equals more prompt tax" <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## Dealing with New AI Models

When a new AI model is released, Orbital's team rigorously experiments with it to:
*   Unlock new features that have been envisioned <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   Determine if the new models are "fit for purpose" <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   Get inspired by new ideas <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   Assess the "prompt tax" required to migrate existing prompts to the new model <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

There is an inherent fear and unknown associated with shipping new AI models, as they can introduce regressions or unintended consequences <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

Prompt tax is distinct from technical debt <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Technical debt is often incurred by optimizing for shipping quickly and fixing later, where a feature might never find product-market fit or a prototype becomes core and needs rebuilding <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. Prompt tax, however, stems from the desire to upgrade to new models that unlock immense value but come with unknowns about what will improve or break <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. The goal is to fix things on the fly by progressively rolling out new models to users, gathering feedback, and quickly addressing issues to maximize benefits and mitigate risks <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

## Battle-Tested Tactics

Orbital has discovered several tactics over 18 months of migrating models:

*   **Migrating from System 1 (e.g., GPT-40) to System 2 models (e.g., 01 preview)**:
    *   System 1 models required specific instructions on *how* to accomplish tasks <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   System 2 models only need to be told *what* to do, with less specific or repeated instructions <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
    *   System 2 models prefer minimal constraints, a clear objective, and time to reason <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Leveraging System 1 Models**: While System 2 models are favored, System 1 models can be cheaper and faster <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. They also often provide "thought tokens" (internal reasoning) that can be embedded for user explainability (especially in complex legal domains) or used for debugging when something goes wrong <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Applying Feature Flags to AI Models**: Similar to software development, progressively rolling out AI model upgrades with feature flags helps mitigate risk <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. However, there's a "change aversion bias" and natural anxiety when moving to a new system, as users are hyper-aware of potential issues, which can sometimes outweigh the positives <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **"Betting on the Model" Mantra**: The team's mantra is to build for where AI models will be in 3, 6, or 12 months, assuming they will get smarter, cheaper, faster, and more capable <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. This ensures features improve as models evolve rather than stagnating <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   **Using System 2 Models for Prompt Migration**: Newer models can help migrate prompts created for older models, radically decreasing manual human effort <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Making Tough Calls and Shipping**: Despite the uncertainty of probabilistic models and new capabilities, it's crucial for teams to take on the risk, ship, and then deal with the consequences, mitigating risks along the way <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Bravery is needed to overcome the inherent anxiety of shipping new models <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   **Strong Feedback Loops**: Implementing rapid feedback loops (e.g., in-product thumbs up/down) is essential. Feedback should quickly reach AI engineers and domain experts, allowing prompt changes to be made and shipped to production within minutes or hours, fixing issues for all users <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

## The Uniquely Challenging AI Development Environment

Demis Hassabis of Google DeepMind highlights that a key [[challenges_in_ai_development | challenge in AI development]] is the unbelievably fast pace of underlying technology <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. Unlike previous revolutionary technologies like the internet or mobile, where the tech stack eventually stabilized, the AI tech stack itself is constantly evolving <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. This makes it uniquely challenging for product development, as what one bets on today could be 100% better in a year <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>. It requires deeply technical product people who can predict where the technology will be in a year to design products that leverage future capabilities <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. This environment fosters experimentation, and when something works, there's a need to "double down quick" <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

There is a significant opportunity for "product AI engineers" who understand both customer problems and the capabilities of AI models to turn them into real product features. This direct connection between technical understanding and user needs is incredibly powerful for the future of the AI engineering community <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

## Paying the Prompt Tax: Shipping with Confidence

The meta-question for AI developers is what gives them more confidence to ship at the frontier as AI advances and agentic product surface areas grow <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. While Orbital has built its product mostly on "vibes" (subjective human testing and real-time user feedback) <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>, the question remains whether this approach will scale as the product grows <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

### Eval Systems vs. Progressive Delivery

An eval system (rigorous, objective evaluation) might be the answer to bending the curve and pushing further <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. However, for complex domains like real estate legal, evaluating correctness, style, conciseness, and citations across all edge cases for probabilistic LLMs becomes prohibitively expensive, slow, and potentially an impossible task to keep up with product velocity <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

Progressive delivery, or "upgrade now and fix on the fly," offers a potential way forward <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. This involves:
*   Rolling out internally first <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
*   Then to a limited number of progressive users <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>.
*   Incrementally scaling up to more users based on feedback <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.
*   Dialing back if internal teams are swamped with feedback until feedback is minimal <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.

The central thesis for staying at the AI frontier is to "buy now" (ship new models and capabilities into the agentic product and to users) <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. The anxiety about potential downside risks may not materialize, or they can be managed through progressive rollout and quick fixes <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. The emphasis remains on staying at the frontier, accepting that whether the prompt tax needs to be fully paid later is determined on a case-by-case basis <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.