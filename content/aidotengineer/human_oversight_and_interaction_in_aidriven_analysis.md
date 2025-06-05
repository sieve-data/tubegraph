---
title: Human oversight and interaction in AIdriven analysis
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Brightwave, a company specializing in research agents for the financial domain, focuses on how AI can digest large volumes of content to assist professionals in tasks like due diligence, competitive deal processes, and financial analysis <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This work often involves thousands of pages of content and demands rapid conviction and the identification of critical risk factors <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. While AI agents can accelerate efficiency by orders of magnitude <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>, the role of human oversight and interaction remains crucial.

## The Indispensable Role of Human Oversight

Despite advancements, purely automated AI models, particularly "non-reasoning models," often perform "greedy local search," which can lead to significant error rates when calls are chained together <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. For example, a 5-10% error rate in extracting organizations from an article can exponentially increase the likelihood of error in subsequent steps <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. Achieving "globally optimal outputs" by making "locally suboptimal decisions" is still an open research problem for AI systems <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

[[human_approval_in_agent_processing | Human oversight]] is considered extremely important in these systems <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. This is because human analysts possess unique access to non-digitized information, such as direct conversations with management or insights from portfolio managers <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. This "taste making" ability allows humans to contextualize and prioritize information in ways AI cannot <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.

## Human-AI Interaction and Steering

Interacting with language models, often described as a "skill," involves steering their outputs <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. In multi-turn conversations, each response can be thought of as a selection of "reactions" that nudge the model's activations towards solving the problem at hand <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. This process is akin to a "human orchestrated Chain of Thought" <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.

Users can directly influence the AI's behavior:
*   **Decomposition:** Decomposing research instructions into multiple sub-themes allows for more granular and specific queries, leading to higher-fidelity and information-dense outputs <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>.
*   **Self-Correction:** Models can self-correct when asked about the factual entailment or nature of an output (e.g., "is this actually an organization?") <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>. However, performing this as a secondary call is often more effective than embedding it in the initial prompt, as models tend to be "credulous" of their initial outputs <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.
*   **Nudging and Directives:** Humans can actively "nudge the model with directives" or select "interesting threads" for the AI to further investigate <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

## Product Design for Seamless Collaboration

A critical design challenge for AI-driven analysis is how to "reveal the thought process of something that's considered 10,000 pages of content to a human in a way that's useful and legible" <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This involves more than just UI/UX or product architecture problems that existed previously <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

Key design patterns observed in AI-driven analysis include:
*   **Mimicking Human Workflow:** AI agents should mimic the human decision-making process, decomposing tasks in a way a person would naturally approach them, such as looking for public market comparables or assessing relevant document sets <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.
*   **Scaffolding Workflows:** Products need to provide scaffolding to orchestrate workflows and shape system behavior, specifying intent and reducing the burden on the user to become a "prompting expert" <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.
*   **Transparency and Auditability:** The AI's analysis should be presented as a "surface" or "high dimensional data structure," allowing users to "turn over that cube" and see the "receipts" or audit trail of how conclusions were reached <a class="yt-timestamp" data-t="18:44:00">[18:44:00]</a>.
*   **Details on Demand:** Users need the ability to get "details on demand" <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. This includes:
    *   Clickable citations that provide additional context about the source and the model's reasoning <a class="yt-timestamp" data-t="17:40:00">[17:40:00]</a>.
    *   Structured interactive outputs that allow users to "pull the thread" and ask for more information <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>.
    *   The ability to highlight any passage of text and ask for implications or further details <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.
    *   Presenting findings in a structured way (e.g., fundraising timelines, ongoing litigation) where users can click to investigate specific points of interest <a class="yt-timestamp" data-t="19:07:00">[19:07:00]</a>. This acts like a "magnifying glass for text" <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>.

## The Latency Trap and User Learning

A significant challenge in [[usercentric_ai_design_and_feedback_loops | user-centric AI design]] is the "latency trap" <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. If the feedback loop for user interaction is long (e.g., 8-20 minutes), users will have fewer opportunities to engage with the system and refine their mental model of how their prompts elicit specific behaviors <a class="yt-timestamp" data-t="12:49:00">[12:49:00]</a>. This limits their faculty with the system and product <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.

The "final form factor" of products in this class, such as Brightwave's research agent, is still being determined, but the design problem is extremely interesting <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>. The focus is on providing a continuous, interactive surface where users can explore and refine the AI's analysis <a class="yt-timestamp" data-t="18:14:00">[18:14:00]</a>.