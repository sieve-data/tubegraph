---
title: Data aggregation and enhancement for fintech
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Method specializes in collecting and centralizing liability data from a wide range of sources, including credit bureaus, card networks like Visa and MasterCard, direct connections with financial institutions, and other third-party providers <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This raw data is then aggregated and enhanced before being served to customers <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Customer Use Cases
Method's customers are typically other [[Fintech Developments and Applications in Africa | fintechs]], banks, or lenders <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. They utilize this enhanced data for various debt management purposes, such as refinancing, loan consolidation, liability payments, and personal finance management <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Challenges in Data Acquisition
An early [[Challenges in data processing for finance professionals | challenge]] Method faced was fulfilling customer requests for liability-specific data points, such as the payoff amount on an auto loan or the escrow balance for a mortgage <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Research showed there was no central API to access these specific data points <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. While direct integration with banks was an option, it was estimated to take at least two years to achieve tangible results, which was not viable for an early-stage company aiming for rapid customer solutions <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Traditional Inefficient Methods
Prior to Method's solution, many companies relied on highly inefficient, manual processes to obtain this financial data <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>:
*   They would hire offshore teams of contractors <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   These teams would call banks on behalf of the company and the end consumer <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   They would authenticate with the banks and gather the necessary information <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   The collected data then required a proof-checking stage before integration into financial platforms for uses like underwriting <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

This manual approach had several significant drawbacks:
*   **Costly:** It requires hiring more people to scale, as one person can only perform one task at a time <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Slow:** The synchronous nature of the process makes it very slow <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Prone to Human Error:** High risk of human error, necessitating additional teams for fact and proof-checking, which could lead to inaccurate financial information being surfaced <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Leveraging AI for Data Enhancement
Method identified that the core problem was making sense of unstructured data, akin to an API with request, authentication, and response validation components <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. The emergence of advanced LLMs, particularly after GPT-4's announcement, presented a potential solution, given their proficiency in parsing unstructured data and tasks like summarization or classification <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

Method developed an agentic workflow using GPT-4 for data extraction <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Initial tests showed promising results, allowing for expansion of use cases and more information extraction from a single API call <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Challenges with Initial LLM Adoption
While effective, using GPT-4 at scale quickly revealed significant issues:
*   **High Cost:** The first month in production with GPT-4 incurred a cost of $70,000 <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Although the value was immense, this cost was a concern <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Prompt Engineering Limitations:** Scaling use cases quickly ran into walls with prompt engineering <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. GPT-4, despite its intelligence, lacked financial expertise, requiring detailed, lengthy, and convoluted instructions and examples for various use cases <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Prompts were hard to generalize, leading to a "cat and mouse chase" of fixes that broke other scenarios, and there was no prompt versioning <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Performance Issues:**
    *   **Caching Limitations:** Variability in responses and frequent prompt tweaks made optimization for caching difficult <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   **Slow Latency:** The baseline latency was slow, hindering concurrent scaling <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
    *   **AI Errors:** AI hallucinations, while different from human errors, were hard to catch <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

These issues prevented scaling the system reliably, despite its effectiveness for specific use cases <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

## Scaling with Open-Source Models and Fine-Tuning
The problem shifted from merely parsing unstructured data to building a robust, agentic workflow capable of handling high volume reliably, with targets of 16 million requests per day, 100K concurrent load, and sub-200 millisecond latency <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

OpenPipe partnered with Method to address these common [[Design considerations for financial AI tools | design considerations for financial AI tools]] around quality, cost, and latency <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Benchmarking and Goals
Initial benchmarks showed:
*   **Error Rate:** GPT-4 had an 11% error rate, while O3 mini had a 4% error rate <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Method's agentic workflow allowed for relatively easy measurement by comparing agent outputs to human-verified data <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Latency:** GPT-4 was around 1 second, while O3 mini took about 5 seconds for the specific task <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Cost:** While O3 mini had a lower per-token cost, it generated many more "reasoning tokens," making it slightly more expensive for Method's use case <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

Method's target requirements, considering their follow-up plausibility checks, were:
*   **Error Rate:** Around 9% <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Latency:** A hard latency cutoff due to the real-time nature of their agent system <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   **Cost:** Very important due to high volume <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

Neither GPT-4 nor O3 mini could meet all three requirements simultaneously <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

### Fine-Tuning as a Solution
Fine-tuning was identified as a powerful tool to bridge the gap, despite requiring more engineering investment than prompt engineering <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. OpenPipe worked on building custom models tailored to Method's specific use case <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

Through fine-tuning a smaller, 8-billion parameter LL3.1 model, they achieved significant improvements:
*   **Improved Accuracy (Lower Error Rate):** The fine-tuned model performed significantly better than GPT-4 and surpassed the required error rate threshold <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This was made easier by using existing production data from GPT-4 to generate outputs for training <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Reduced Latency:** Moving to a much smaller model greatly reduced latency due to fewer calculations. It also opened the possibility of deploying the model within Method's own infrastructure to eliminate network latency <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   **Lower Cost:** The smaller model resulted in a significantly lower cost, exceeding the cost thresholds Method had to make their operations viable <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. This removed unit economics concerns associated with larger models <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

This approach demonstrates how fine-tuning can "bend the price-performance curve" <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, enabling [[efficiency_improvements_with_ai_in_financial_analysis | efficiency improvements with AI in financial analysis]] and allowing [[AI tools for business efficiency | AI tools for business efficiency]] to scale to a very large production level with only a small engineering team <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. [[AI and data investment | Productionizing AI agents]] requires openness and patience, as unlike traditional code, AI agents evolve and require time to reach production readiness and consistent responses <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.