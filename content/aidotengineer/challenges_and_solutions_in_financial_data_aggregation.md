---
title: Challenges and solutions in financial data aggregation
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Method specializes in collecting and centralizing liability data from numerous sources, including credit bureaus, card networks (Visa, MasterCard), direct financial institution connections, and other third-party providers <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This aggregated and enhanced data is then served to fintechs, banks, and lenders, who utilize it for debt management, refinancing, loan consolidation, liability payments, and personal finance management <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Challenge of Granular Financial Data
An early challenge for Method was the demand from customers for more specific liability data points, such as the payoff amount for an auto loan or the escrow balance for a mortgage <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Research revealed no central API existed to access these particular data points <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Directly integrating with banks was not feasible for an early-stage company, as it could take years to establish a solid connection <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Traditional, Manual Solutions and Their Drawbacks
Existing companies often address this by hiring offshore teams of contractors <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. These teams call banks, authenticate, gather information, proof-check it, and then integrate it into financial platforms for uses like underwriting <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

However, this manual process presents significant [[challenges_in_synthesizing_vast_financial_data | challenges]] <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>:
*   **Inefficiency and Lack of Scalability**: One person can only perform one task at a time, requiring more hires for scaling <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Slowness**: The synchronous nature of calls makes the process very slow <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **High Cost**: The need for more personnel increases operational expenses <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Human Error**: A high potential for human error necessitates additional teams for fact-checking and proof-checking, risking inaccurate financial information being surfaced <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

Conceptually, this manual process resembles an API, involving a request, authentication, and response validation <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. The core problem boils down to making sense of unstructured data <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Embracing AI for Unstructured Data
Method sought a tool adept at parsing unstructured data <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. The emergence of GPT-4 and the "Cambrian explosion" of LLM-enabled applications presented a perfect opportunity, as advanced LLMs are highly effective at tasks like summarization and classification of unstructured data <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

Method developed an [[challenges_and_solutions_in_building_ai_agents | agentic workflow]] using GPT-4, which initially performed exceptionally well, even for expanding use cases <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

### Initial AI Implementation: New Challenges
Despite initial success, scaling the GPT-4 solution introduced new [[challenges_and_solutions_in_using_large_language_models | challenges]] <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>:
*   **Exorbitant Cost**: The first month in production with GPT-4 incurred a cost of $70,000 <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. While leadership recognized the immense value, this cost was unsustainable long-term <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Prompt Engineering Limitations**: As use cases scaled, prompt engineering proved insufficient. GPT-4, while smart, lacked financial expertise, requiring excessively detailed and convoluted instructions and examples for various scenarios <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This led to a "cat and mouse chase" where fixes for one scenario broke others, compounded by a lack of prompt versioning <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Scaling Inefficiencies**:
    *   **Cost**: Caching was ineffective due to variability in responses and constant prompt tweaks <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   **Latency**: Baseline latency was slow, hindering concurrent scaling <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    *   **AI Errors**: Unlike human errors, AI hallucinations were difficult to catch <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

Although GPT-4 solved the core problem of parsing unstructured data for specific use cases, it presented significant [[challenges_and_solutions_in_ai_driven_data_processing | scaling challenges]] that prevented robust, high-volume deployment <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

## Scaling AI for Financial Data
The problem shifted from merely understanding unstructured data to building a robust [[knowledge_agents_in_finance_workflows | agentic workflow]] that could reliably handle high volumes <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Method's target figures for a scalable system included:
*   16 million requests per day <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>
*   100K concurrent load <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>
*   Minimal latency (sub-200 milliseconds) for real-time operations <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>

## OpenPipe and Fine-tuning as the Solution
OpenPipe collaborated with Method to address the issues of quality, cost, and latency, which are common concerns for companies using AI <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Benchmarking Existing Models
OpenPipe measured the performance of GPT-4 and O3 mini against Method's needs <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>:
*   **Error Rates**: GPT-4 had an 11% error rate, while O3 mini had a 4% error rate <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Error rates were measured by comparing agent outputs to human-verified correct data <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Latency**: GPT-4 responded in about 1 second, and O3 mini took about 5 seconds for Method's specific tasks <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Cost**: Surprisingly, O3 mini was slightly more expensive than GPT-4 for Method's use case, despite its lower per-token cost, because it generated many more "reasoning tokens" (longer outputs) <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

Method's target requirements were:
*   **Error Rate**: Around 9% error rate was acceptable due to downstream plausibility checks <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Latency**: A hard latency cut-off was necessary for the real-time agent system <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Cost**: High volume made cost a critical factor <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

Neither GPT-4 nor O3 mini met all three requirements <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

### The Power of Fine-tuning
OpenPipe's solution was to use fine-tuning to build custom models tailored to Method's specific use case <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Fine-tuning is a "power tool" that requires more engineering investment than simple prompt engineering but can significantly "bend the price-performance curve" <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

Fine-tuning leveraged Method's existing production data from GPT-4 to train a custom model, such as an 8-billion parameter LL 3.1 model <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

The results of fine-tuning were transformative <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>:
*   **Quality (Error Rate)**: The fine-tuned model achieved significantly better error rates than GPT-4 and surpassed Method's target threshold <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   **Latency**: Moving to a much smaller (8-billion parameter) model drastically reduced latency, enabling deployment in a low-latency manner with fewer calculations. This also opens possibilities for co-locating the model with application code to eliminate network latency <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
*   **Cost**: The smaller, fine-tuned model resulted in a much lower cost, far exceeding Method's cost thresholds and making the business viable from a unit economics perspective <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

## Key Takeaways for [[ai_strategies_in_financial_technology_companies | AI Integration in Financial Technology]]
*   **Simplicity and Cost-Effectiveness**: It's possible to use cheaper models and fine-tune them using existing production data, without needing to invest in GPUs <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   **Patience and Openness**: Productionizing AI agents requires openness and patience from engineering and leadership teams. Unlike traditional deterministic code, AI agents take time to become production-ready and deliver consistent results due to their probabilistic nature <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Fine-tuning as a Strategic Tool**: When prompt engineering with off-the-shelf models doesn't meet reliability targets, fine-tuning is a viable strategy to significantly improve the price-performance curve and achieve large-scale production deployment <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.