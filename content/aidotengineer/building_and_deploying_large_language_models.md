---
title: Building and deploying large language models
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Bloomberg has been investing in AI for nearly 15-16 years [00:00:44]. In late 2021, as [[large_language_models_and_selfimprovement | LLMs]] began capturing imagination, Bloomberg decided to build its own [[development_of_qwen_large_language_models | large language model]] [00:00:36]. This development took all of 2022 [00:00:50]. By 2023, they had learned extensively about model construction, data set organization, and performance evaluation, which they documented in a paper [00:00:55].

However, with the rise of open-weight and open-source communities, particularly ChatGPT, Bloomberg pivoted its strategy to build on top of already available models, given their numerous use cases [00:01:06].

## Bloomberg's AI Organization

Bloomberg's AI efforts are organized as a special group reporting to the Global Head of Engineering [00:01:42]. This group collaborates closely with their data counterparts, product teams, and the CTO in cross-functional settings [00:01:47]. The team comprises approximately 400 people across 50 teams in London, New York, Princeton, and Toronto [00:01:58].

## Generative AI Product Development

Bloomberg has been [[building_and_scaling_ai_use_cases_with_openai | building products]] using generative AI for 12 to 16 months, with a significant commitment to this effort [00:02:12]. This journey has involved solving numerous [[challenges_and_solutions_in_using_large_language_models | challenges]] to deliver current solutions [00:02:23]. The speaker notes optimism about advancements in addressing these challenges, emphasizing a realistic approach to shipping products today [00:02:47].

### Defining Tools and Agents

Internally, it was challenging to standardize the vocabulary for "agent" and "tool" [00:03:12]. The speaker clarified definitions based on a paper titled "Cognitive Architectures for Language Agents" [00:03:17]:
*   A **tool** is defined as being on the left-hand side of the spectrum [00:03:20], representing cognitive architectures for language agents.
*   An **agent** is more autonomous, possesses memory, and can evolve, residing on the right-hand side of the spectrum [00:03:30].

### Bloomberg's Context

Bloomberg is a fintech company serving clients in finance, a diverse field with varied archetypes of professionals [00:03:51]. Bloomberg both generates and accumulates vast amounts of unstructured and structured data, including news, research, documents, and market data [00:04:17]. Daily, they receive 400 billion ticks of structured data, over a billion unstructured messages, and millions of well-written documents, with more than 40 years of historical data [00:04:34].

#### Non-Negotiable Product Principles
Given its presence in finance for over 40 years, Bloomberg's products adhere to strict non-negotiable principles [00:06:15]:
*   **Precision, Comprehensiveness, Speed, Throughput, Availability** [00:06:25]
*   **Data Protection:** Safeguarding contributor and client data [00:06:30]
*   **Transparency:** Ensuring clarity throughout product development [00:06:36]

These principles significantly influence the [[challenges_and_solutions_in_using_large_language_models | challenges]] faced when [[building_and_scaling_ai_use_cases_with_openai | building agents]] using current AI capabilities [00:06:41].

## Case Study: Research Analyst and Earnings Call Summaries

To illustrate product development, the speaker focused on the archetype of a research analyst [00:05:12]. Research analysts are experts in specific areas (e.g., AI, semiconductors, technology) [00:05:23]. Their daily tasks include:
*   Search and discovery
*   Summarization (especially with unstructured data) [00:05:40]
*   Data and analytics (structured data) [00:05:46]
*   Communication with colleagues [00:05:52]
*   Building models (requiring data normalization and programming) [00:06:00]

### Earnings Call Summarization Product
A key initiative started in 2023 was assisting research analysts with scheduled quarterly earnings calls from public companies [00:06:50]. These calls discuss company health and future prospects, often involving presentations and Q&A segments [00:07:05]. During earnings season, many such calls occur daily, requiring analysts to stay updated [00:07:17].

Bloomberg uses AI to generate transcripts of these calls [00:07:30]. Recognizing that analysts are interested in specific questions relevant to a company's sector, Bloomberg aimed to provide answers to these questions for the analysts [00:07:38]. This allows analysts to quickly gauge if a deeper dive is necessary [00:07:50].

#### Challenges in Bringing the Product to Market
Despite the seemingly simple concept, significant effort was required to launch the product while adhering to Bloomberg's principles [00:08:00]:
*   **Performance:** Out-of-the-box performance regarding precision, accuracy, and factuality was not sufficient [00:08:11].
*   **MLOps:** Extensive work was done to build remediation workflows and circuit breakers [00:08:19].
*   **Impact of Errors:** Since summaries are published and widely seen, any error has a significant impact [00:08:32].
*   **Continuous Improvement:** Performance is constantly monitored and remediated to improve summary accuracy, involving robust CI/CD processes [00:08:38].

### Current Agentic Architecture: Semi-Agentic

The current products are built with a "semi-agentic" architecture [00:08:54]. This means that while some components are autonomous, full autonomy is not yet trusted [00:09:03]. Mandatory guardrails are implemented, such as preventing financial advice (e.g., if a user asks "should I invest in...", the system must catch it) [00:09:09]. These guardrails ensure factual correctness and are non-optional, hard-coded checks for any agent [00:09:19].

## Scaling Large Language Models

Scaling [[integration_of_large_language_models_in_development | large language models]] involves two key aspects: improving agent evolution and rethinking organizational structure.

### 1. Improving Agent Evolution: Embracing Fragility
For agents to evolve quickly, especially since initial builds may not be optimal, a robust improvement process is essential [00:09:50]. Traditionally, well-built software (like matrix multiplication libraries) had precisely documented APIs, predictable inputs, and error codes [00:10:07]. Even with machine learning models 20 years ago, despite some inherent stochasticity in outputs, working with them was manageable due to controlled input and output distributions (e.g., news sentiment products with known news sources and language) [00:10:41].

However, when [[integration_of_large_language_models_in_development | using LLMs]] and agents (which are compositions of LLMs), errors can multiply significantly, leading to fragile behavior [00:11:18]. This fragility means that relying solely on upstream systems for accuracy is problematic, as they are constantly evolving [00:14:23]. For example, a minor error in an NLP tool (like missing a character, leading to monthly data instead of quarterly) can cause a downstream agent to output an incorrect answer that is hard to detect if the underlying data isn't exposed [00:13:49].

Instead of demanding perfect accuracy from upstream components, it's more effective to *factor in* their potential fragility and implement independent safety checks and guardrails within each agent [00:14:26]. This approach allows individual agents to evolve faster without complex, burdensome "handshake signals" with every downstream caller, thus accelerating the development and release of new agents [00:15:00]. This promotes resilience and speed in the development process [00:15:23].

### 2. Organizational Structure: Rethinking Conway's Law
Traditional machine learning and software development often see organizational structure mirroring software factorization [00:15:38]. However, with new tech stacks and product types, this needs rethinking [00:15:57]. Key questions arise:
*   How many agents should be built?
*   What should each agent do?
*   Should agents have overlapping functionality? [00:16:06]

Initially, when product design is uncertain and fast iteration is needed, collapsing organizational silos and software stacks is beneficial [00:16:46]. This allows teams to iterate quickly, sharing code, data, and models [00:17:01].

As understanding of a product or agent matures (its use cases, strengths, and weaknesses), and as more agents are built, the organization can return to foundational software and organizational principles [00:17:10]. This involves optimizing for performance, cost reduction, testability, and transparency [00:17:29]. This leads to a shift towards horizontal teams for shared functionalities, like guardrails [00:17:39]. Bloomberg, for instance, horizontally manages guardrails to prevent every team from having to define how to handle veiled financial advice inputs [00:17:41]. The decision of when to introduce horizontal structures and break down monolithic agents into smaller pieces depends on the organization's specific context and maturity [00:18:01].

### Current Research Agent Architecture Example

For a research analyst agent, the current architecture is factorized [00:18:24]:
*   An agent is responsible for taking user input and session context, deeply understanding the query, and determining what information is needed [00:18:28].
*   Another agent handles answer generation with strict rigor around well-formed answers [00:18:41].
*   The system is semi-agentic, with non-optional guardrails invoked at multiple points, providing no autonomy in these areas [00:18:49].
*   It builds upon years of traditional and modern data manipulation techniques, evolving from sparse to dense and hybrid indices [00:18:59].