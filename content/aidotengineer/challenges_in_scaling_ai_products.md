---
title: Challenges in scaling AI products
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Developing and deploying generative AI products, especially those involving AI agents, presents a unique set of [[Challenges in AI Development | challenges]] when aiming for scale. Bloomberg, having invested in AI for 15-16 years, made a strategic pivot in 2023 to build on top of available large language models (LLMs) after the rise of ChatGPT and the open-source community, rather than solely developing their own from scratch <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This shift allowed them to focus on [[Challenges and strategies in AI production | solving the complexities]] of putting AI products into production <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Defining Tools vs. Agents
For clarity, the speaker defines "tools" as primarily cognitive architectures for language agents, while "agents" are more autonomous, possess memory, and can evolve <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This distinction is crucial for understanding the architecture of AI products being scaled.

## Context: Bloomberg's Operations
Bloomberg operates as a fintech company serving diverse financial clients, including research analysts, portfolio managers, and traders <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The company processes an immense volume of data daily: 400 billion ticks of structured data, over a billion unstructured messages, and millions of well-written documents like news, with over 40 years of historical data <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Core principles for Bloomberg's products, regardless of AI integration, are non-negotiable:
*   Precision <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   Comprehensiveness <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   Speed <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   Throughput <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   Availability <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   Protecting contributor and client data <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
*   Transparency <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

These principles ground the [[challenges_in_implementing_gen_ai_projects | challenges]] faced when building and [[scaling_ai_agents_in_production | scaling AI agents]] using current technology <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Case Study: Earnings Call Summarization
In 2023, Bloomberg focused on assisting research analysts by automatically answering common questions from public company quarterly earnings call transcripts <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
However, initial performance of out-of-the-box models was not ideal in terms of precision, accuracy, and factuality <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This necessitated significant MLOps work to implement:
*   Remediation workflows <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
*   Circuit breakers <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>
*   Continuous monitoring and remediation to ensure summary accuracy, especially since these summaries are published <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

Today's agentic architecture is "semi-agentic" due to a lack of full trust in autonomous systems <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Essential guardrails, such as prohibiting financial advice or ensuring factuality, are hard-coded and non-optional components of any agent <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Two Aspects of Scaling
Scaling AI products involves two primary considerations:

### 1. Embracing Fragility and Building Resilience
Unlike traditional software APIs or even earlier machine learning models with predictable input/output distributions, LLMs and compositions of LLMs (agents) introduce a significant degree of stochasticity and error multiplication <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This leads to fragile behavior, making it difficult to predict outcomes <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

Previously, with ML products like a news sentiment detector (built in 2009), the input and output spaces were well-defined, allowing for robust testing and monitoring. Even then, out-of-band communication with downstream consumers was necessary when model versions changed <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

For agentic architectures, the goal is to make daily improvements to agents, moving away from slow, batch-regression-test-based release cycles <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. When agents are composed, an error in one component (e.g., misinterpreting a query from "quarterly" to "monthly" data) can lead to compounding errors downstream <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

To address this, the strategy is not to rely on upstream systems being perfectly accurate, but to *factor in* their fragility and continuous evolution <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. Implementing independent safety checks within each agent, even across internal teams, allows for faster evolution of individual agents without complex handshake signals and sign-offs from all downstream callers <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. This resilience enables faster iteration and deployment.

### 2. Evolving Organizational Structure
The organizational structure should adapt to the demands of building AI agents, moving beyond traditional machine learning team structures <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Key questions arise:
*   How many agents to build? <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>
*   What should each agent do? <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>
*   Should agents have overlapping functionality? <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>

Initially, when product design is unclear and fast iteration is needed, a vertically aligned team structure (where one team handles a full product/agent) is beneficial <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This allows for rapid prototyping, shared code, data, and models <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

As understanding of individual products or agents matures—their use cases, strengths, and weaknesses—the organization can transition to a more horizontally aligned structure <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. This is when optimizations like performance increases, cost reductions, improved testability, and transparency become priorities <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. For example, guardrails (e.g., preventing financial advice) are implemented horizontally across all products, avoiding redundant effort across 50 different teams <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. It's crucial for an organization to determine the right time to create these horizontal functions and break down monolithic agents into smaller, more manageable pieces <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.

For a research analyst agent, this factorization means separate agents for understanding user queries and session context, figuring out necessary information, and generating answers with strict rigor <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. Non-optional guardrails are called at multiple points, reflecting the "semi-agentic" approach <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.