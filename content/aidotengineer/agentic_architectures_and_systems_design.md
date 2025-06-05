---
title: Agentic architectures and systems design
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

## Introduction to Agentic Systems at Bloomberg

Bloomberg began investing in AI approximately 15 to 16 years ago <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. In late 2021, Large Language Models (LLMs) started to capture significant attention <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The company spent 2022 building its own large language model and published a paper on their learnings in 2023 <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. However, with the rise of ChatGPT and the open-source community, Bloomberg pivoted its strategy to build on top of existing external models due to numerous use cases <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

Bloomberg's AI efforts are organized as a special group within engineering, collaborating closely with data, product, and CTO counterparts <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The organization consists of about 400 people across 50 teams in London, New York, Princeton, and Toronto <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For the past 12 to 16 months, they have been seriously building products using generative AI, focusing on more [[agentic_frameworks_and_their_applications | agentic]] tools <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Defining Agentic Systems: Agents vs. Tools

To clarify internal vocabulary, Bloomberg adopted definitions from a paper titled "Cognitive Architectures for Language Agents" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Tool**: Refers to the left-hand side of the spectrum in that paper, implying less autonomy <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Agent**: Refers to the right-hand side of the spectrum, indicating a system that is more autonomous, possesses memory, and can evolve <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Building Agentic Products at Bloomberg

Bloomberg is a fintech company serving diverse financial clients, including research analysts, portfolio managers, traders, and more <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. They handle vast amounts of structured and unstructured data, processing 400 billion ticks of structured data and over a billion unstructured messages daily, with more than 40 years of historical data <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Core principles for their products, regardless of AI usage, include precision, comprehensiveness, speed, throughput, availability, and protecting client data while ensuring transparency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. These non-negotiables heavily influence the challenges of building [[agentic_frameworks_and_their_applications | agents]] with current technologies <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Initial Approach: Earnings Call Summaries

In 2023, Bloomberg focused on helping research analysts by summarizing public company earnings call transcripts <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. These calls include presentations and Q&A segments, and numerous calls happen daily during earnings season <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. The goal was to automatically answer common questions of interest to analysts, enabling them to quickly assess whether a deeper dive is needed <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

Out-of-the-box performance (precision, accuracy, factuality) was not great <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Significant MLOps work was required to build remediation workflows and circuit breakers <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Since these summaries are published and seen by all clients, errors have a significant impact, necessitating constant performance monitoring and remediation through CI/CD <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Current "Semi-Agentic" Architecture

Bloomberg's current product architecture is "semi-agentic" <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. This means some components are autonomous, while others are not, reflecting a lack of full trust in complete autonomy <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

Key aspects of this architecture include:
*   **Guardrails**: These are non-optional and hard-coded components <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. For example, Bloomberg does not offer financial advice, so any query asking for investment advice must be caught <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Factual accuracy is another mandatory guardrail <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. These checks must be performed at multiple points within the system <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.

## Scaling Agentic Architectures

Scaling [[agentic_frameworks_and_their_applications | agents]] involves two primary aspects: addressing fragility and optimizing organizational structure.

### Addressing Fragility and Compounding Errors

When building [[agentic_frameworks_and_their_applications | agents]], especially those that are compositions of LLMs, errors multiply significantly, leading to fragile behavior <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

#### Comparison with Traditional ML Systems
In traditional machine learning products (e.g., a news sentiment product built in 2009), the input and output distributions are generally well-understood <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. For instance, news sentiment models know which news wires are monitored, the language, and editorial guidelines, allowing for clear input parameters and well-defined outputs <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. This allows for establishing risk, monitoring performance, and providing heads-up communication to downstream consumers about model changes <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. While there was still some stochasticity, it was manageable <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

#### Need for Resilience and Guardrails
In contrast, with [[agentic_frameworks_and_their_applications | agentic architectures]], the goal is to make daily improvements to agents, moving away from slow, batch regression test-based release cycles <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Downstream customers also make independent improvements, complicating coordination <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

An example highlights the problem: an agent correctly understands a query for "US CPI for the last five quarters" and dispatches to a tool, but the tool fetches monthly data instead of quarterly, leading to a wrong answer <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. If the raw data isn't exposed, a research analyst might not catch the error <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

> "It is easier to not count on the upstream systems to be accurate but rather factor in that they will be fragile and they'll be evolving and just do your own safety checks." <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>

Building in such [[agentic_frameworks_and_tool_integration | guardrails]] allows for faster iteration, as individual agents can evolve without constant handshaking or sign-offs from every downstream caller <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. This promotes a more resilient mindset <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

### Organizational Structure (Arc Structure) for Scalability

Traditional machine learning organizations have a specific software factorization reflected in their organizational structure, which needs to be rethought when building [[agentic_frameworks_and_their_applications | agentic]] products <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. Key questions arise: How many [[agentic_frameworks_and_their_applications | agents]] to build? What should each agent do? Should functionality overlap? <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. It's tempting to maintain existing software and organizational structures, but this can hinder progress <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

#### Early Stage: Vertical Alignment for Fast Iteration
In the beginning, when product design is uncertain, it is more effective to collapse the organizational and software stacks <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. Vertically aligned teams can iterate quickly, sharing code, data, and models to figure things out <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

#### Later Stage: Horizontal Alignment for Optimization
Once the single product or agent's use case is well understood, and its strengths and weaknesses are clear, the organization can shift <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. When building many such [[agentic_frameworks_and_their_applications | agents]], it's beneficial to return to the foundations of good software and organizational design <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. This includes optimizing for performance, cost reduction, testability, and transparency <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

This leads to the adoption of horizontal components. For example, [[agentic_frameworks_and_tool_integration | guardrails]] should be horizontal across all teams <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. The organization must determine the right time to create horizontals and break down monolithic [[agentic_enterprise_and_ai_agents | agents]] into smaller pieces <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

## Example: Research Analyst Agent Architecture

For the research analyst, the current architecture is semi-agentic <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. It is factorized into distinct agents reflecting the organizational structure:
*   An agent deeply understands the user's query and session context, determining the type of information needed <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   Another agent is responsible for answer generation, adhering to rigorous standards for well-formed answers <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
*   Non-optional [[agentic_frameworks_and_tool_integration | guardrails]] are applied at multiple points, providing no autonomy in these critical areas <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
*   These agents leverage years of traditional and modern data wrangling, including the use of sparse, dense, and hybrid indices <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.