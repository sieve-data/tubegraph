---
title: Building and scaling large language models
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Bloomberg began seriously investing in large language models (LLMs) in late 2021, though the company has been investing in AI for nearly 15-16 years <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Initially, Bloomberg dedicated 2022 to [[building_scalable_ai_systems | building their own large language model]], learning about data organization and [[evaluating_language_model_performance | evaluation]] during this process <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. However, with the rise of ChatGPT and the open-weight and open-source communities, Bloomberg pivoted its strategy in 2023 to focus on building on top of existing available models <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Bloomberg's AI Organization

Bloomberg's AI efforts are structured as a specialized group within engineering, reporting to the Global Head of Engineering <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This group works in cross-functional settings with data counterparts, product teams, and the CTO's office <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. The AI team comprises approximately 400 people across 50 teams, located in London, New York, Princeton, and Toronto <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

The company has been actively [[experiments_with_large_language_models_and_ai_assisted_work | building products using generative AI]] for 12 to 16 months, with a significant focus on developing more [[large_language_models_in_ai_agents | agentic tools]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Defining Tools vs. Agents

For internal clarity, Bloomberg distinguishes between "tools" and "agents" based on the paper "Cognitive Architectures for Language Agents" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Tool**: Refers to the "left-hand side" of the spectrum, implying less autonomy <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **[[Large language models in AI agents | Agent]]**: Represents the "right-hand side" of the spectrum, characterized by greater autonomy, memory, and the ability to evolve <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Bloomberg's Data Scale and Principles

As a FinTech company, Bloomberg deals with a massive scale of financial data:
*   They generate and accumulate both unstructured data (news, research, documents, slides) and structured data (reference data, market data) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   Daily, they receive 400 billion ticks of structured data, over a billion unstructured messages, and millions of written documents including news <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   This data spans over 40 years of history <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

Due to the nature of finance, certain product principles are non-negotiable:
*   **Precision, Comprehensiveness, Speed, Throughput, Availability** <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Protecting contributor and client data** <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Transparency** <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
These principles must be maintained regardless of whether AI is used <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Scaling Agentic Architectures

When [[building_scalable_ai_systems | scaling LLM-based agents]], two primary aspects are crucial:

### 1. Embracing Fragility with Robust Guardrails
Traditional software, like generalized matrix product APIs, is robust and well-documented <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Machine learning APIs, while generally well-intentioned in defining input/output distributions, introduce a degree of stochasticity <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. However, with LLMs and their compositions into agents, errors multiply significantly, leading to fragile behavior <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

For instance, a news sentiment product built in 2009 had predictable input (news wires, language, editorial guidelines) and output distributions, allowing for careful testing and deployment risk assessment <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. Downstream consumers were notified of model changes and encouraged to re-test <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

In contrast, modern [[large_language_models in AI agents | agentic architectures]] require daily improvements, making traditional batch regression testing and extensive release cycles impractical <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Errors can compound, especially in downstream workflows where data may not be fully exposed <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

The key to scaling is to **factor in that upstream systems will be fragile and evolving**, and implement independent safety checks and guardrails at each stage <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. This allows individual agents to evolve faster without extensive coordination and sign-offs from every downstream caller <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

For example, Bloomberg's agentic products are "semi-agentic" because full autonomy is not yet trusted <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Essential guardrails, such as prohibiting financial advice or ensuring factuality, are hard-coded and mandatory <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### 2. Rethinking Organizational Structure

Traditional machine learning teams often have a software factorization reflected in their organizational structure <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. However, when [[building_scalable_ai_systems | building with LLMs]] and new tech stacks, this structure needs to be re-evaluated <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.

*   **Early Stages (Product Discovery)**: It's beneficial to have vertically aligned, collapsed teams and software stacks to facilitate rapid iteration and product design discovery <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This fosters fast iteration and sharing of code, data, and models <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
*   **Later Stages (Optimization and Scale)**: Once the product design and agent use cases are understood, the organization can transition to a more horizontal structure <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This allows for optimization, performance improvement, cost reduction, increased testability, and transparency <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. For instance, common guardrails like filtering financial advice queries should be horizontally managed across teams to avoid redundant effort <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. This also enables breaking down monolithic agents into smaller, more manageable pieces <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

## Example: Research Analyst Agent

For a research analyst, a current agent architecture looks like this:
*   An agent deeply understands the user's query and session context <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   It determines the necessary information and dispatches to a tool, often with an NLP front end, to fetch data <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
*   Answer generation has its own agent, with strict rules for well-formed answers <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.
*   Non-optional guardrails are called at multiple points, ensuring no autonomy where core principles are concerned <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   The system builds upon years of traditional and modern data management techniques <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.

This approach reflects the understanding that to successfully scale and deploy [[large_language_models in AI agents | AI agents]], organizations must adapt their technical and structural mindsets to prioritize resilience and disciplined factorization.