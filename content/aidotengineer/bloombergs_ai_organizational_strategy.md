---
title: Bloombergs AI organizational strategy
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Bloomberg, a company with nearly 15 years of investment in [[AI in Workplaces | AI]], has evolved its strategy for integrating AI into its operations and product development, particularly with the advent of large language models (LLMs) and agentic architectures <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Evolution of AI Development at Bloomberg
Initially, Bloomberg undertook the ambitious project of building its own large language model, a process that occupied the entirety of 2022 <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This effort provided significant learning on model construction, data organization, and performance evaluation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, with the rapid advancements in the open-source community, particularly after the emergence of ChatGPT, Bloomberg strategically pivoted <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The focus shifted to building products on top of existing external models, leveraging the vast array of use cases within Bloomberg <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Bloomberg's AI Organizational Structure
Bloomberg's AI efforts are organized as a specialized group reporting to the Global Head of Engineering <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This group collaborates extensively with Bloomberg's robust data organization, as well as product and CTO teams in cross-functional settings <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The AI team comprises approximately 400 people across 50 teams located in London, New York, Princeton, and Toronto <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Approach to Generative AI Product Development
Bloomberg has been building products using generative AI for 12 to 16 months, starting with more agentic tools <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. A key characteristic of their current products is their "semi-agentic" nature <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. This means some components operate autonomously, while others are not, reflecting a cautious approach due to a lack of full trust in complete autonomy <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Non-Negotiable Principles
When [[implementing_ai_in_enterprises | implementing AI]] in their products, especially in the financial sector, Bloomberg adheres to strict non-negotiable principles <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>:
*   **Precision and Comprehensiveness**: Ensuring high accuracy and completeness of information <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Speed and Throughput**: Delivering information quickly and efficiently <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Availability**: Ensuring continuous access to services <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Data Protection**: Safeguarding contributor and client data <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Transparency**: Maintaining clear visibility throughout the AI-driven processes <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

These principles act as crucial "guard rails" in their AI systems. For instance, any system must prevent offering financial advice, reflecting a core business constraint <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Scaling AI Initiatives
Bloomberg's approach to scaling AI initiatives focuses on two main aspects: dealing with system fragility and evolving organizational structure <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

### Addressing Fragility and Evolving Systems
The composition of LLMs into agents significantly multiplies potential errors, leading to fragile behavior <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. Unlike traditional software with well-defined APIs and predictable outcomes, or even early machine learning models with manageable stochasticity, agentic architectures introduce high variability <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

To counteract this, Bloomberg emphasizes building resilient systems by not relying on upstream systems for perfect accuracy <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. Instead, they factor in the inherent fragility and continuous evolution of upstream components <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. This involves implementing independent safety checks and robust monitoring (e.g., MLOps, CI/CD for remediation workflows and circuit breakers) within each agent <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This mindset allows individual agents to evolve faster without complex, time-consuming handshake signals or sign-offs from every downstream consumer before release <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

### [[Enterprise leadership and organizational alignment for AI initiatives | Organizational Structure]] for Scaling
Bloomberg has rethought its [[building_ai_teams | organizational structure]] to accommodate the demands of new AI tech stacks and products <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.

*   **Initial Phase (Vertical Alignment)**: In the early stages of product design, when understanding is limited and rapid iteration is crucial, Bloomberg favors vertically aligned teams <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This approach encourages fast iteration, and sharing of code, data, and models within a dedicated team focused on a specific product or agent <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

*   **Mature Phase (Horizontal Alignment)**: As the understanding of a product or agent's use cases matures and more agents are built, the organization transitions to more horizontal structures <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This allows for optimization, performance increases, cost reduction, improved testability, and enhanced transparency <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. Shared services, like universal guard rails (e.g., preventing financial advice), are centralized horizontally to avoid redundant efforts across numerous teams <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. This also enables the breaking down of monolithic agents into smaller, more manageable pieces <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

## Example: Research Analyst Agent
For a research analyst, Bloomberg's AI architecture for query understanding and answer generation is highly factorized <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. An agent deeply understands user queries and session context to determine the necessary information <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This is then dispatched to specialized tools, often with an NLP front-end, to fetch structured data <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. Answer generation is also a distinct, factored-out process with rigorous standards for well-formed answers <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Non-optional guard rails are called at multiple points, ensuring no autonomy where critical principles are concerned <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>. The system also leverages years of traditional and modern data wrangling techniques, including hybrid indices <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.