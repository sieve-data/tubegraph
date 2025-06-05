---
title: Agent development life cycle
videoId: 0vBKv9yAQi4
---

From: [[aidotengineer]] <br/> 

Sierra, a conversational AI platform for businesses, focuses on [[building_effective_agents | building and improving agents]] for various customer experience touchpoints, including sales, subscription management, and product recommendations <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Initially known for chat experiences and customer service, Sierra is expanding into phone interactions, which are projected to be the majority of interactions by the end of the year <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Evolution of AI Development

The rapid evolution of AI highlights the need for robust development processes. While AI development has roots in earlier decades, the recent surge in capabilities has occurred largely within the last decade <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Early examples of AI development, such as the speaker's work on Google Lens in 2016, focused on tasks like distinguishing Chihuahuas from blueberry muffins or identifying plants <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This early stage often felt like a "slot machine," with unpredictable results due to the non-determinism of inputs or outputs <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

Today's Google Lens, a result of consistent, step-by-step iteration over a decade, demonstrates advanced capabilities like visual shopping, language translation, and math homework assistance <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This progress underscores the importance of a structured process for iterative improvement, similar to the software development life cycle (SDLC) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## The Need for a Specialized Life Cycle

Traditional software is deterministic, fast, cheap, rigid, and governed by strict logic <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. However, large language models (LLMs) pose unique [[challenges_in_ai_agent_development | challenges in AI agent development]] <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>:
*   **Non-deterministic:** They can produce varied outputs for the same input <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Slow and expensive:** Running LLMs can incur significant time and cost <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Flexible and creative:** LLMs can reason through problems and exhibit flexibility <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

Sierra developed the Agent Development Life Cycle (ADLC) to leverage LLMs' strengths while integrating traditional software where beneficial <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

## Sierra's Agent Development Life Cycle (ADLC)

The ADLC is Sierra's process for [[building_effective_agents | building and improving AI agents]] <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. It is designed for iterative refinement with customers in production to ensure productivity and robustness <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

### Key Components of the ADLC

1.  **Quality Assurance (QA):**
    *   **Experience Manager:** Customers have access to Sierra's Experience Manager, which allows them to view every conversation an agent has and high-level performance reports in real time <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
    *   **Feedback Mechanism:** If an agent like Duncan Smothers provides incorrect information (e.g., inventory), users can report the issue <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
    *   **Issue to Test:** Reported issues lead to the filing of a problem and the creation of a new test <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   **Continuous Improvement:** Once a test passes, a new release can be made, leading to an agent evolving from a handful of tests at launch to hundreds and then thousands over time <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

2.  **Beyond Correction:** The ADLC also enables agents to go "above and beyond" <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. For instance, Chubbies agents have a budget to delight customers, potentially allowing an agent to arrange for shorts to be DoorDashed from a retail location if unavailable online <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

3.  **AI-Enhanced Development:** A year ago, these processes were largely manual <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. With advancements in AI, Sierra is now able to add AI to each part of the ADLC, accelerating improvements <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

4.  **Scalability:** The ADLC becomes more effective with larger customers <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. While an agent like Duncan might handle hundreds of thousands of requests, other customers manage tens of millions, making velocity and change management incredibly valuable <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

5.  **Adapting to Industry Changes:** The fast-moving AI space, with model upgrades, new paradigms like reasoning models, and multimodality, constantly impacts the ADLC <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. Reasoning models, in particular, act as a force multiplier, allowing for more effective application of AI to development, testing, and QA <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

### Case Study: Chubbies and Duncan Smothers

Chubbies partnered with Sierra to create Duncan Smothers, an [[ai_agents_and_agentic_workflows | AI agent]] representing their business <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Duncan Smothers is capable, empathetic, and engaging, assisting with a variety of customer cases on the Chubbies website <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>:
*   **Sizing and Fit:** Empathetically helps customers with questions, asks for waist size, and offers product recommendations <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Inventory Tracking:** Informs customers about stock availability and helps them choose new items <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Package Tracking and Refunds:** Provides multiple tracking numbers and can issue refunds, demonstrating autonomous actions <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

These capabilities allow Chubbies to help more customers more quickly and with higher satisfaction <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Building and Recruiting AI Teams

Sierra employs dedicated agent engineering and agent product management functions that work closely with customers like Chubbies <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. The importance of [[building_and_recruiting_ai_teams | finding talent]] for these roles is highlighted by the speaker's experience meeting Shawn at the AI Engineering World's Fair, which led to Shawn joining Sierra <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This demonstrates the [[importance_of_timing_in_recruiting | value of serendipitous connections]] in building strong AI teams.

## Voice Agents and Responsive Design

Sierra launched voice capabilities in October, allowing large customers like SiriusXM to answer phone calls immediately every time <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. Sierra's approach to voice is akin to responsive web design: the same underlying platform and agent code can adapt to various channels and modalities (e.g., chat, phone) <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. While customization (different phrasing, parallel requests for lower latency) is possible, the core functionality works out of the box <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

## Designing with Empathy in AI

Building with AI is fascinating because LLMs, like humans, can be unpredictable, slow, and not great at math, yet they allow designers to have empathy in a new way <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. By understanding the limitations and characteristics of LLMs (e.g., processing transcribed text with delay), developers can design more robust and effective experiences for [[ai_agents_and_agentic_workflows | AI agents]] <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This perspective helps in [[ai_product_development_iteration | creating a richer and more robust AI product]] <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.