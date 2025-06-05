---
title: Role of AI in research and data analytics
videoId: b2GqTDWtg6s
---

From: [[aidotengineer]] <br/> 

Bloomberg, a company with over 15 years of investment in [[Strategies for effective AI implementation | AI]], has significantly leveraged artificial intelligence, particularly large language models (LLMs) and agents, to enhance its research and data analytics capabilities. The company's efforts began with building its own large language model in 2022, learning about data organization and evaluation, before pivoting to build on top of open-source and open-weight models as the landscape evolved <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Bloomberg's Data Landscape
Bloomberg operates as a large data organization, generating and accumulating vast amounts of both unstructured and structured data <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Daily, this includes:
*   400 billion ticks of structured data <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>
*   Over 1 billion unstructured messages <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
*   Millions of well-written documents, including news <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>

This data spans over 40 years of history, providing a massive information base for their financial clients <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## The Research Analyst Archetype
AI efforts at Bloomberg are often focused on specific user archetypes, such as the research analyst in finance <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. These analysts are experts in particular areas (e.g., AI, semiconductors, electric vehicles) and perform diverse activities daily <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>:
*   **Search and Discovery & Summarization:** Working extensively with unstructured data <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Data and Analytics:** Engaging with structured data <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Communication:** Dispersing and gathering information with colleagues <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Model Building:** Normalizing data, programming, and generating models <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Early AI Products: Earnings Call Summaries
In 2023, Bloomberg identified an opportunity to use AI to assist research analysts with scheduled quarterly earnings calls <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. With many calls happening daily during earnings season, analysts need to stay informed <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. AI is used to:
1.  Generate transcripts of these calls <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  Answer sector-specific questions for analysts based on the transcripts, providing quick insights on company health and future outlook <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## Challenges and Principles in AI Product Development
Building AI products at Bloomberg involves adhering to non-negotiable principles due to the nature of finance <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>:
*   **Precision, Comprehensiveness, Speed, Throughput, Availability** <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   **Data Protection:** Safeguarding contributor and client data <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Transparency:** Ensuring clarity throughout the process <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

These principles mean that raw [[Challenges and solutions in AI driven data processing | AI performance]] "out of the box was not great" in terms of precision, accuracy, and factuality <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Significant MLOps work is required to build remediation workflows and circuit breakers, as errors have an outsized impact on publicly published summaries <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Continuous monitoring and remediation improve accuracy <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

Bloomberg's current agentic architecture is "semi-agentic" because there isn't full trust for complete autonomy <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. [[Strategies for effective AI implementation | Guard rails]] are a classic example, ensuring that the system does not offer financial advice or produce non-factual content <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Scaling AI Solutions

### Dealing with Fragility and Stochasticity
Scaling AI in research and data analytics involves addressing the fragility of LLM-based agents, which are compositions of LLMs where errors can multiply <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. Unlike traditional software with well-documented APIs or even early ML models with predictable input/output distributions, LLMs introduce more stochasticity <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

> "It is easier to not count on the upstream systems to be accurate but rather factor in that they will be fragile and they'll be evolving and just do your own safety checks." <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>

This means that downstream systems and agents must build in their own safety checks rather than relying solely on upstream accuracy <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. This approach allows individual agents to evolve faster without extensive "handshake signals" or sign-offs from every downstream caller <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. For example, an agent tasked with fetching US CPI data for the last five quarters can misinterpret "Q" (quarter) as monthly data if a single character is missed, leading to incorrect results that are hard to catch without exposing the raw data <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Organizational Structure for AI Development
The [[Leadership and Organizational Strategies for AI Integration | organizational structure]] for building AI agents also needs to evolve <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. Initially, when product design is uncertain and fast iteration is needed, vertically aligned teams that "collapse the software stack" are effective <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This allows for rapid iteration and sharing of code, data, and models <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

As understanding of a product or agent matures, and many agents are built, the organization can shift towards more horizontal structures to optimize for performance, cost reduction, testability, and transparency <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. For example, guard rails, like preventing financial advice, are implemented horizontally across teams to avoid redundant efforts <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. This involves breaking down monolithic agents into smaller, more specialized pieces <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

### Current Research Agent Architecture
Today, a research agent at Bloomberg demonstrates this evolved structure <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>:
*   An agent understands user queries and session context, figuring out what information is needed <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This is factored out as its own agent, reflected in the organizational structure <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.
*   Answer generation, with its rigor for well-formed answers, is also factored out as a separate component <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.
*   Non-optional guard rails are called at multiple points, ensuring no autonomy in critical safety aspects <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
*   The system builds upon years of traditional and modern data manipulation techniques, including evolved indexing systems <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.