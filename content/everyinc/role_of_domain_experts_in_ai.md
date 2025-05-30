---
title: Role of domain experts in AI
videoId: exzPO4hAD9s
---

From: [[everyinc]] <br/> 

Traditional approaches to building machine learning defensibility for companies often fall short. Instead, success in the age of generative AI will be achieved by integrating [[Applying agency in AI development | domain experts]] directly into the AI development workflow, leveraging their specialized knowledge to define and refine problems that AI systems solve <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a> <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a> <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

## Prompt Engineering as Domain Knowledge
PromptLayer, a prompt engineering platform, focuses on building workflows for iterating on Language Model (LM) applications <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a> <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. The core theory of prompt engineering, according to Jared Zim, co-founder and CEO of PromptLayer, is about "putting domain knowledge into your LM system" <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

The process involves three primitives:
*   **The Prompt:** The instructions given to the AI <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **The Eval:** Methods for testing the AI's responses <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **The Dataset:** Sample data used for testing and iteration <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

While the prompt itself or the dataset might be automated, the evaluation (eval) or defining the problem scope remains critical <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a> <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>. For example, in building an AI math tutor, there is no "one prompt that rules them all" because effective tutoring requires specific knowledge and approaches <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a> <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

## Computational Irreducibility and AI
The concept of *computational irreducibility*, derived from Stephen Wolfram's work, posits that in solving a problem, certain parts can be simplified or sped up, but there's an "irreducible" part that cannot be collapsed or simplified <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a> <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>. For AI, this means even with the most advanced tools, defining *what* problem to solve remains the hard, irreducible part <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a> <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

This leads to the idea that there's no single "best" answer or solution, especially in complex domains <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a> <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>. Just as there isn't "one prompt to rule them all," there isn't one perfect data set for a given domain <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. Different contexts and perspectives will yield different optimal solutions <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

> [!QUOTE] Jared Zim
> "The LM is getting more complicated, not less. Let's not think about how it works, all I want to think about is how do I map the inputs to the outputs I want, and if you're not getting the outputs you want that's a skill issue." <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>

## The Rise of the Non-Technical Prompt Engineer
A key observation from PromptLayer's experience is the emergence of the "non-technical prompt engineer" <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. For example, a parenting coach app utilized a former teacher (with 15 years of experience) to edit prompts <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a> <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. This individual, despite being non-technical, could refine the AI's responses based on their extensive domain expertise, ensuring appropriate and contextually relevant advice for parents <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

This highlights a shift in value proposition:
*   Companies will win not by hiring the best ML engineers, but by working with [[Applying agency in AI development | domain experts]] <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   [[Challenges in building AI tools | Defensibility in AI]] comes from the unique definition of the problem and the integration of specialized knowledge, not just the underlying machine learning <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a> <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
*   Fields like AI teachers, therapists, doctors, and lawyers require input from experts in those domains, as engineers lack the necessary specific knowledge <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a> <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Practical Approaches to AI Development
[[Practical approaches to AI | Building AI tools]] effectively requires a disciplined approach, akin to the scientific method:
*   **Iteration:** Focus on quickly trying things and iterating based on results <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a> <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
*   **Operational Focus:** Prioritize how prompts can be edited and improved operationally, rather than trying to discover a single "correct" prompt <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a> <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   **Prompt Routing:** Instead of stacking messages in one massive prompt, it's often better to build a workflow (DAG/graph) that routes queries to specific prompts designed to do "one thing and do one thing really well" <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a> <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. This compartmentalization makes testing and collaboration easier <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

### Evaluation (Evals)
For evaluations, a common approach is:
1.  **Back-testing:** Running new prompts against historical data (e.g., the last 1,000 or 10,000 prompt responses) to see how results change <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. The most valuable insight is often that something has changed drastically <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.
2.  **Ground Truth Metrics:** If a clear "ground truth" exists (e.g., thumbs up/down, sale made, ticket closed), A/B testing and direct metric anchoring can be used <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.
3.  **Heuristics without Ground Truth:** For tasks without a definitive "right" answer (like summarizing calls), domain experts must articulate the heuristics they use to evaluate quality <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. This involves breaking down the human "eyeballing" process into measurable characteristics <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

### Data Sets
Data sets can be built through:
*   **Back-tests:** Using historical prompt responses <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.
*   **Ground Truth Creation:** Manually creating desired outputs (e.g., a perfect email summary) that then serve as principles for evaluation <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a> <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. This "hard work" of defining correctness is where value is created <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a> <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
*   **Synthetic Generation:** Artificially generating data to bootstrap datasets <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

## Broader Implications for AI and Knowledge Work
The emphasis on domain experts extends beyond technical prompt engineering. It reflects a shift in how value is created and distributed in the AI era.
*   **Distribution of Knowledge:** AI applications take the knowledge of an expert and distribute it, whether for writing tweets or providing parenting advice <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.
*   **Human Perspective:** Data-driven approaches are essential, but the perspective embedded in how data is collected and loops are designed is crucial and not neutral <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. A human with domain expertise has developed a refined perspective over thousands of "data gathering loops" <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **[[Role of AI in creative work | Single-Use Software]] & Content Creation:** AI lowers the cost of creating highly specific tools and content that might not have warranted development previously <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a> <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This allows for personalized or niche "stories" (like an NPR-style talk show about an obscure topic) that were too expensive to produce <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
*   **Challenges in General Purpose AI:** Large, general-purpose AI models often rely on lengthy, run-on system prompts ("prompt debt") that accumulate rules and exceptions <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a> <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. This "overfitting" makes them less clear and concise <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. For general purpose tools, explicit routing to different models or prompts based on user intent (as seen with Snapchat AI or ChatGPT's evolution) is a more effective strategy than a single monolithic prompt <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a> <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

The fundamental limits of AI are often tied to the challenge of defining the problem for the AI to solve <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>. True "intelligence" in AI systems might involve the ability to connect disparate pieces of information that humans naturally link, a capability that current models like o1 (despite their mathematical prowess) sometimes lack <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>. The core problem solved by LLMs is the transformation between language and data <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a> <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. Everything else is about how this technology is hooked up to real-world data and problems <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.