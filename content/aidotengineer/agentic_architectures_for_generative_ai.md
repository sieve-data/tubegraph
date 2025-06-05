---
title: Agentic architectures for generative AI
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

## Introduction to Agentic Architectures
The term "agentic landscape" describes the current state of AI development, particularly with the advent of Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. In the context of building [[Agentic Enterprise and AI | agentic enterprise]] applications, there's a distinction between "tools" and "agents" based on cognitive architectures for language agents <a class="yt-timestamp" data-t="03:17:10">[03:17:10]</a>:
*   **Tool:** Represents the simpler, less autonomous end of the spectrum <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
*   **Agent:** Characterized by being more autonomous, possessing memory, and having the ability to evolve <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

### Bloomberg's Journey into Generative AI
Bloomberg, a fintech company with a long history of investing in AI (almost 15-16 years), began building its own LLM in 2022 <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This effort involved significant work on data sets, evaluation, and performance optimization <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. However, with the rise of open-weight and open-source communities, Bloomberg strategically pivoted to building on top of existing LLM capabilities <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.

Bloomberg's AI efforts are organized as a special group within the Global Head of Engineering <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. This group works closely with data counterparts, product teams, and the CTO in cross-functional settings, comprising around 400 people across 50 teams in London, New York, Princeton, and Toronto <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. They have been building products using [[scaling_generative_ai_workloads | generative AI]], starting with more agentic tools, for 12 to 16 months, addressing numerous [[challenges_in_ai_for_architecture_design | challenges in AI architecture design]] <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

## Core Principles for Financial Applications
For a fintech company like Bloomberg, certain product aspects are non-negotiable <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. These include:
*   Precision <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>
*   Comprehensiveness <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>
*   Speed and throughput <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>
*   Availability <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>
*   Protecting contributor and client data <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>
*   Transparency <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>

These principles ground the [[challenges_in_ai_for_architecture_design | challenges faced when using AI]] to build agentic systems, requiring extensive work on remediation workflows and circuit breakers <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. Errors in public-facing summaries, for instance, have an outsized impact <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>. Continuous monitoring and CI/CD (Continuous Integration/Continuous Delivery) are essential for maintaining and improving accuracy <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.

## Agentic Architectures in Practice: The Research Analyst Example
Bloomberg's clients in finance are diverse, including research analysts, portfolio managers, sales, trading, and risk managers <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>. Research analysts, who are experts in specific areas like AI or semiconductors, perform tasks such as:
*   Search and discovery <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>
*   Summarization of unstructured data <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>
*   Working with structured data and analytics <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>
*   Communication to gather and disperse information <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>
*   Building models (data normalization, programming) <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>

Bloomberg generates and accumulates vast amounts of data, both unstructured (news, research, documents) and structured (reference and market data). Every day, they process 400 billion ticks of structured data, over a billion unstructured messages, and millions of well-written documents, with over 40 years of history <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

A key product developed in 2023 for research analysts helps process scheduled quarterly earning calls from public companies <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. These calls include executive presentations and Q&A segments <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. Given that many such calls occur daily during earning season, analysts need to stay informed <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. Transcripts are generated using AI, and Bloomberg identifies questions of interest for specific sectors to provide answers to analysts, allowing them to quickly assess whether a deeper dive is needed <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.

The performance of these products "out of the box" was not sufficient in terms of precision, accuracy, and factuality <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>. This necessitated significant investment in [[building_effective_ai_agents | MLOps]] to create remediation workflows and circuit breakers. Since these summaries are published, errors have a disproportionate impact <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.

### Semi-Agentic Architecture
Bloomberg's current product architecture for generative AI is "semi-agentic" <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. This means some parts are autonomous, while others are not, due to a lack of full trust in complete autonomy <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. Guardrails are a classic example of non-autonomous, mandatory components <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. For instance, Bloomberg does not offer financial advice, so any query like "should I invest in..." must be caught by a guardrail <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. Factual accuracy is another non-negotiable guardrail <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.

## [[scaling_generative_ai_workloads | Scaling Generative AI Workloads]]

### Dealing with Fragility and Stochasticity
When building agents, especially those that need to evolve rapidly, the inherent stochasticity of LLMs and compositions of LLMs can lead to significant fragility <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>. Unlike traditional software APIs (e.g., matrix multiplication) with well-defined inputs, error codes, and performance guarantees <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>, or even traditional machine learning APIs with somewhat known input/output distributions <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>, LLMs introduce multiplying errors <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.

For example, a news sentiment product built in 2009 had a well-understood input distribution (news wires, language, editorial guidelines) and a simple output space <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>. Training data was built from scratch, allowing for robust test sets and clear risk assessment <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. Despite these controls, out-of-band communication was still necessary to warn downstream consumers of model changes <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.

In [[developing_ai_agents_and_agentic_workflows | agentic architectures]], the goal is to make daily improvements without lengthy release cycles based on batch regression tests <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>. If an agent providing data (e.g., CPI for five quarters) makes a subtle error (e.g., fetching monthly instead of quarterly data), a downstream workflow relying on that data without exposing the raw table could easily miss the mistake <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.

The solution is not to rely on upstream systems being perfectly accurate, but to factor in their inherent fragility and evolution <a class="yt-timestamp" data-t="14:23:00">[14:23:00]</a>. Building in safety checks and guardrails at multiple points within the system enables individual agents to evolve faster without requiring extensive handshakes and sign-offs from every downstream consumer <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>. This shift in mindset fosters resilience and allows for more rapid iteration <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>.

### Organizational Structure for Building Agents
Traditional machine learning often leads to a specific software factorization reflected in organizational structure <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>. However, when [[developing_ai_agents_and_agentic_workflows | building new kinds of products]] with different tech stacks, this structure needs rethinking <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a>. Key questions arise:
*   How many agents should be built? <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>
*   What should each agent do? <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>
*   Should agents have overlapping functionality? <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>

Initially, when product design is uncertain and fast iteration is needed, a "collapsed" organizational structure with vertically aligned teams is beneficial <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>. This allows teams to figure things out, share code, data, and models, and iterate quickly <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>.

As understanding of a product or agent matures, and its use cases become clear, the organization can transition towards more horizontal alignment <a class="yt-timestamp" data-t="17:07:00">[17:07:00]</a>. This enables optimization for performance, cost reduction, testability, and transparency <a class="yt-timestamp" data-t="17:29:00">[17:29:00]</a>. For example, guardrails for preventing financial advice are a horizontal concern that shouldn't be re-figured out by every team <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>. Determining the right time to introduce horizontals and break down monolithic agents into smaller, specialized pieces is crucial <a class="yt-timestamp" data-t="18:04:00">[18:04:00]</a>.

### Example Research Agent Architecture
Today, a research agent's architecture might involve distinct agents for:
*   **User Intent Understanding:** Deeply understanding the user's query and session context to determine necessary information <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>. This is factored out as its own agent <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>.
*   **Answer Generation:** With rigorous standards for well-formed answers <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>. This is also factored out <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>.
*   **Guardrails:** Non-optional components called at multiple points to ensure adherence to principles like not offering financial advice <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.

These systems build upon years of traditional and modern data wrangling techniques, evolving from sparse to dense and hybrid indices <a class="yt-timestamp" data-t="18:59:00">[18:59:00]</a>.