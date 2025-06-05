---
title: Challenges and solutions in scaling AI agents
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Building products using generative AI has presented numerous [[design_challenges_for_ai_agents | challenges]] that require resolution to effectively scale [[scaling_ai_agents_in_production | AI agents in production]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Bloomberg, a company with a 15-year history of investing in AI, pivoted its strategy in 2023 to build on top of existing large language models (LLMs) due to the rapid advancements in the open-weight and open-source communities <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Their AI efforts are organized as a special group within engineering, collaborating closely with data, product, and CTO teams, comprising about 400 people across 50 teams in various global locations <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Defining Agents and Tools
Internally, Bloomberg adopted a clear vocabulary for 'tools' and 'agents' based on the "Cognitive Architectures for Language Agents" paper <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>:
*   **Tool**: Refers to the cognitive architectures for language agents <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Agent**: Defined as more autonomous, possessing memory, and capable of evolving <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Bloomberg's Context: Finance and Non-Negotiables
As a fintech company, Bloomberg serves a diverse range of clients in finance <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The company generates and accumulates vast amounts of structured and unstructured data, including 400 billion ticks of structured data and over a billion unstructured messages daily, with 40 years of historical data <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

Non-negotiable aspects of Bloomberg's products include <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>:
*   Precision <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   Comprehensiveness <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>
*   Speed <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   Throughput and availability <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>
*   Protecting contributor and client data <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
*   Ensuring transparency <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

These principles ground the [[challenges_in_developing_ai_agents | challenges]] faced when building [[scaling_ai_agents_in_production | AI agents in production]] using current technologies <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Initial Product Development: Earnings Call Summarization
In 2023, Bloomberg began developing a product to help research analysts stay informed about quarterly earnings calls <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The goal was to automatically answer common questions of interest to analysts from earnings call transcripts <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Initial Challenges and Solutions
*   **Performance:** Out-of-the-box performance regarding precision, accuracy, and factuality was not satisfactory <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Remediation:** Significant MLOps work was required to build remediation workflows and circuit breakers <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This was critical because published summaries have an outsized impact if erroneous <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Monitoring:** Constant performance monitoring and CI/CD processes were implemented to ensure accuracy <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

The current architecture for products is "semi-agentic," meaning some pieces are autonomous while others are not, especially regarding guard rails like preventing financial advice or ensuring factuality <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## [[challenges_in_scaling_generative_ai | Challenges in Scaling Generative AI]] Agents

### 1. Fragility of Compositions of LLMs
When using LLMs, especially as compositions in agents, errors can multiply, leading to fragile behavior <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Increased Stochasticity:** Unlike traditional software APIs (e.g., matrix multiplication) or even early machine learning models (e.g., news sentiment APIs), LLMs introduce more stochasticity; it's harder to predict the exact output or if it will work <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Compounding Errors:** In an agentic workflow, a small error from one component (e.g., a missed character leading to monthly instead of quarterly data) can compound downstream, making it difficult to catch if only the final answer is displayed <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Rapid Evolution vs. Release Cycles:** The desire for agents to improve daily clashes with traditional batch regression test-based release cycles, especially when many downstream consumers rely on the outputs <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

#### Solution: Resilience Through Downstream Safety Checks
Instead of solely relying on upstream systems for accuracy, it's crucial to factor in that they will be fragile and evolving <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.
*   **Implement Downstream Checks:** Build in safety checks at the downstream level <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. This allows individual agents to evolve faster without requiring extensive handshake signals or sign-offs from every downstream caller <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Resilient Mindset:** A resilient mindset allows for faster iteration and independent evolution of individual agents <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### 2. Organizational Structure (Arc Structure)
Traditional machine learning and software development often have a specific factorization of software reflected in their organizational structure <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. With LLMs and agents, this needs rethinking.

#### Solution: Adapting Organizational Structure
*   **Early Stages (Vertical Alignment):** In the beginning, when product design is unclear and fast iteration is needed, it's easier to have vertically aligned teams (e.g., collapsed software stacks and organizational units) that can build, iterate rapidly, and share code, data, and models <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   **Mature Stages (Horizontal Alignment):** Once a single product or agent's use, strengths, and weaknesses are well understood, and many agents are being built, the organization can transition to more foundational software practices <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This includes creating horizontal teams for aspects like guard rails (e.g., preventing financial advice) to optimize performance, reduce cost, increase testability, and transparency <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>. This also involves breaking down monolithic agents into smaller, more manageable pieces <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

## Semi-Agentic Architecture Example
For a research agent, Bloomberg's current architecture features <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>:
*   An agent dedicated to understanding user queries and session context, then determining what information is needed <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   A separate agent for answer generation with strict guidelines for well-formed answers <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
*   Non-optional guard rails that must be called at multiple points, reflecting the "semi-agentic" nature where not all components are fully autonomous <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   Reliance on years of traditional and modern data wrangling and indexing techniques <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.

By proactively addressing the [[challenges_in_building_reliable_ai_agents | challenges in building reliable AI agents]] through resilient design and adaptive organizational structures, companies can effectively scale their AI agent capabilities.