---
title: Generative AI and financial data products
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Bloomberg, a fintech company with over 40 years of history, has been engaged in [[ai_and_data_investment | investing in AI]] for approximately 15 to 16 years <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. While they initially built their own large language model in 2022, they later pivoted their strategy to build on top of open-weight and open-source models after the emergence of ChatGPT <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

The company's AI efforts are organized as a specialized group reporting to the Global Head of Engineering <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This group collaborates closely with their data counterparts, product teams, and the CTO in cross-functional settings <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Bloomberg's extensive [[data_aggregation_and_enhancement_for_fintech | data aggregation and enhancement for fintech]] capabilities are a significant asset, handling 400 billion ticks of structured data and over a billion unstructured messages daily, with more than 40 years of historical data <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Building Generative AI Products in Finance

Bloomberg has been building products using generative AI and more agentic tools for 12 to 16 months <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

The company defines "tools" as cognitive architectures for language agents, while "agents" are more autonomous, possess memory, and can evolve <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Non-Negotiable Product Principles
Given its role in finance, Bloomberg's products adhere to several non-negotiable principles, regardless of AI integration <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>:
*   Precision <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   Comprehensiveness <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   Speed <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   Throughput <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   Availability <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   Protection of contributor and client data <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
*   Transparency <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

These principles inform the [[design_considerations_for_financial_ai_tools | design considerations for financial AI tools]] and the [[generative_ai_project_challenges_and_strategies | generative AI project challenges and strategies]] encountered when deploying AI agents.

### Use Case: Supporting Research Analysts
One primary focus for generative AI applications is supporting financial research analysts <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. Research analysts are typically experts in specific sectors like AI, semiconductors, or electric vehicles <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Their daily activities include:
*   Search and discovery <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
*   Summarization (especially of unstructured data) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>
*   Working with structured data and analytics <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Communication with colleagues <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Building models, which requires data normalization and programming <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>

#### Earnings Call Summaries
In 2023, Bloomberg identified an opportunity to use AI to summarize public company earnings calls <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. During earnings season, many such calls occur daily <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The goal was to generate transcripts and then use AI to answer common questions of interest to analysts within specific sectors, allowing them to quickly assess whether a deeper dive is needed <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Developing this product involved significant work on:
*   **Performance:** Initial out-of-the-box performance for precision, accuracy, and factuality was not high <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **MLOps:** Extensive work on remediation workflows and circuit breakers was necessary, as published summaries cannot contain errors due to their outsized impact <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Monitoring:** Constant monitoring, remediation, and CI/CD processes ensure summaries become more accurate over time <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

## [[challenges_in_scaling_generative_ai | Challenges in Scaling Generative AI]]

### Addressing Fragility and Stochasticity
When building agentic architectures, especially compositions of LLMs, errors can multiply, leading to fragile behavior <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. Unlike traditional machine learning models with well-defined input/output distributions, LLMs introduce more stochasticity <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

For instance, an agent tasked with retrieving structured data like US CPI for the last five quarters might dispatch to a tool that returns incorrect data due to a minor input error (e.g., monthly vs. quarterly data) <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. If a downstream workflow only displays the answer without the underlying table, it becomes difficult to catch such compounding errors <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

To mitigate this, Bloomberg implements "guard rails" <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. These are non-optional, coded checks for any agent <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. For example, Bloomberg doesn't offer financial advice, so any query asking for investment advice triggers a guardrail <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. The approach is to assume upstream systems will be fragile and evolving, building in safety checks downstream to ensure resilience <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. This allows individual agents to evolve faster without extensive "handshake signals" between teams every time an improvement is made <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

### Organizational Structure for Scaling
Scaling generative AI also requires rethinking organizational structure, moving beyond traditional machine learning team factorizations <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Initial Phase:** In the beginning, when product design is uncertain and fast iteration is key, it's easier to use vertically aligned teams (often called "full-stack" or "product teams") that share code, data, and models <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This allows teams to quickly build and figure things out <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   **Maturity Phase:** Once a product or agent's use case and capabilities are well-understood, and multiple agents are being built, the organization can move towards a more horizontally aligned structure <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This allows for optimization, increased performance, reduced cost, better testability, and transparency <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. For example, guard rails are handled horizontally, preventing each of 50 teams from independently figuring out how to refuse thinly veiled financial advice inputs <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. This involves breaking down monolithic agents into smaller, more specialized pieces <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

## Current Agentic Architecture for Research Analysts
Bloomberg's current architecture for [[knowledge_agents_in_financial_research | knowledge agents in financial research]] is "semi-agentic" <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. There isn't full trust for complete autonomy, so some pieces are autonomous while others are not <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

For a research analyst, the agent workflow involves:
1.  **Query Understanding:** An agent deeply understands the user's query, session context, and what information is needed to answer it <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This is factored out as its own agent and reflected in the organizational structure <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.
2.  **Tool Dispatch:** The agent figures out which domain to dispatch the query to and uses a tool (with an NLP front end) to fetch the data <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This process contributes to [[efficiency_improvements_with_ai_in_financial_analysis | efficiency improvements with AI in financial analysis]].
3.  **Answer Generation:** A separate agent handles answer generation, with strict rigor around what constitutes a well-formed answer <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.
4.  **Guard Rails:** Non-optional guard rails are called at multiple points in the process to ensure compliance with principles like factuality and avoiding financial advice <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

This architecture leverages years of traditional and modern data wrangling, including the evolution from sparse to dense and hybrid indices <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>. The use of agents and tools for fetching and processing data also ties into processes like [[generating_structured_data_with_ai_sdk | generating structured data with AI SDK]] and [[evaluating_generative_ai_workloads | evaluating generative AI workloads]].