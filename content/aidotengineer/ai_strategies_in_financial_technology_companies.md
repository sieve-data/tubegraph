---
title: AI strategies in financial technology companies
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Bloomberg, a financial technology (fintech) company, has been investing in [[AI in enterprise and startups | AI]] for almost 15 to 16 years <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The company's [[Leadership and Organizational Strategies for AI Integration | AI efforts]] are organized as a special group reporting to the Global Head of Engineering, collaborating closely with data, product, and CTO teams <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This group comprises approximately 400 people across 50 teams in London, New York, Princeton, and Toronto <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Evolution of AI Strategy

In late 2021, Large Language Models (LLMs) began capturing significant attention <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Bloomberg initially spent 2022 building its own LLM, gaining extensive knowledge in model construction, data organization, evaluation, and performance tuning <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. However, with the emergence of ChatGPT and the strong growth of the open-weight and open-source community, Bloomberg strategically pivoted to building on top of available external models and resources <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Defining AI Tools and Agents

Internally, Bloomberg distinguishes between "tools" and "agents" based on concepts from the paper "Cognitive Architectures for Language Agents" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>:
*   **Tools**: Function as cognitive architectures for language agents, typically on the left side of the spectrum, implying less autonomy <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Agents**: Are more autonomous, possessing memory and the ability to evolve <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Non-Negotiable Principles in Finance

As a fintech company serving diverse financial clients, Bloomberg adheres to strict non-negotiable principles for all its products, regardless of whether [[AI integration in financial systems at Ramp | AI is used]] <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>:
*   **Precision and Accuracy**: Ensuring correctness of information <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Comprehensiveness**: Providing thorough and complete data <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Speed and Throughput**: Delivering information quickly and efficiently <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Availability**: Ensuring consistent access to services <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Data Protection**: Safeguarding contributor and client data <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Transparency**: Maintaining clarity throughout the product development and output processes <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

Bloomberg manages and processes vast amounts of data daily, including 400 billion ticks of structured data and over a billion unstructured messages, with over 40 years of historical data <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Case Study: Earnings Call Summaries for Research Analysts

Bloomberg has been building products using generative [[AI tools in financial research and due diligence | AI tools]] for 12 to 16 months <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. An example product is the automated summary of public company earnings calls for research analysts <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. These calls include executive presentations and Q&A segments, with many occurring daily during earning season <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

The strategy involves using AI to answer sector-specific questions of interest to analysts, enabling them to quickly determine if a deeper dive is necessary <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Challenges and Solutions

Developing this product required significant effort in MLOps, particularly in building remediation workflows and circuit breakers <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Given that these summaries are published and errors have an outsized impact, continuous monitoring, remediation, and CI/CD processes are crucial to improve accuracy <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## Scaling AI Products and Organizational Structure

Scaling [[AI applications and customer success stories | AI product development]] at Bloomberg involves two key aspects:

### 1. Handling Fragility of AI Systems

Unlike traditional software with well-documented APIs, AI models, and especially compositions of LLMs (agents), introduce stochasticity and multiply errors <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This leads to fragile behavior <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

*   **Lessons from News Sentiment Product**: Even with controlled inputs (e.g., news wires with editorial guidelines) and clear outputs (e.g., sentiment scores), and robust training data, traditional ML models still required out-of-band communication with downstream consumers about model changes <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Challenge with Agentic Architectures**: For [[AI enhanced vs AI native organizations | agentic architectures]], the goal is to make improvements daily, not through slow batch regression testing cycles <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
*   **Strategy: Internal Safety Checks**: Instead of relying on upstream systems to be perfectly accurate and stable, Bloomberg's strategy is to factor in their potential fragility and evolution <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. This means building in internal safety checks and [[strategies for effective AI implementation | guard rails]] within each agent. This approach allows individual agents to evolve faster without extensive "handshake signals" with every downstream caller, ultimately leading to more resilient systems <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

### 2. Evolving Organizational Structure for Scaling

Traditional machine learning organization structures often reflect software factorization <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. However, with new tech stacks and product types, it's necessary to rethink this structure <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.

*   **Initial Phase (Vertical Alignment)**: In the early stages of product design where iteration speed is key and the product's exact nature is unknown, it's more effective to have vertically aligned teams <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This encourages fast iteration, and sharing of code, data, and models <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
*   **Scaling Phase (Horizontal Alignment)**: As products and agents mature and their use cases become clearer, the organization can shift towards horizontally aligned teams <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. This allows for optimization (e.g., increasing performance, reducing cost), improved testability, and transparency <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
    *   **Example: Guard Rails**: Functions like "guard rails" (e.g., preventing financial advice or ensuring factual accuracy) are centralized and handled horizontally across teams, rather than each of the 50 teams figuring them out independently <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. This is a crucial aspect of [[AI implementation and best practices | AI implementation best practices]].
*   **Decomposing Monolithic Agents**: Over time, monolithic agents can be broken down into smaller, more specialized pieces, reflected in the organizational structure <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

### Current Research Agent Architecture Example

A research agent at Bloomberg today exhibits a semi-agentic architecture <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. It processes user queries, understands session context, identifies needed information, and dispatches to relevant tools <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. Components like query understanding and answer generation are factored out as their own agents <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>. Non-optional guard rails are implemented at multiple points, ensuring no autonomy in critical areas, and it builds upon years of traditional and modern data management techniques <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.