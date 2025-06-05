---
title: Scaling AI agents in production
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

This article explores the journey of Method, a fintech company, in [[scaling_ai_solutions_in_production | scaling AI solutions in production]] to over 500 million agents, detailing the [[challenges_and_solutions_in_scaling_ai_agents | challenges and solutions in scaling AI agents]] they faced and how OpenPipe assisted in optimizing their AI infrastructure.

## Method's Core Business and Initial Challenge

Method specializes in collecting and centralizing liability data from hundreds of sources, including credit bureaus, card networks (Visa, MasterCard), and direct connections with financial institutions <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. They aggregate and enhance this data for customers, typically other fintechs, banks, or lenders, who use it for debt management, refinancing, loan consolidation, liability payments, or personal finance management <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

An early challenge arose when customers requested liability-specific data points, such as payoff amounts for auto loans or escrow balances for mortgages <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. There was no central API available to retrieve this information <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, and direct bank integrations would take years <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### The Inefficient Status Quo

Existing companies providing similar services often relied on highly inefficient manual processes <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This involved hiring offshore teams of contractors to call banks, authenticate, gather information, proof-check it, and then integrate it into financial platforms <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Key problems with this manual approach included:
*   **Expense:** One person can only do one task at a time, requiring more hires to scale <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Slowness:** The synchronous nature of the process made it very slow <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Human Error:** Significant human error was involved, necessitating proof-checking teams and risking inaccurate financial information being surfaced <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

Conceptually, this process mirrored an API with request, authentication, and response validation components <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. The core problem was making sense of unstructured data <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Initial AI Solution: GPT-4 and Its Limitations

With the rise of LLMs like GPT-4, Method recognized their strength in parsing unstructured data, summarization, and classification <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. They developed an agentic workflow using GPT-4, which initially performed very well <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

However, as traffic increased, significant challenges emerged:

*   **High Cost:** The first month in production with GPT-4 incurred a cost of $70,000 <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. While the value was immense, this was a major concern for leadership <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Prompt Engineering Difficulties:**
    *   Prompt engineering offered limited scalability <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   GPT, despite its intelligence, was not a financial expert, requiring detailed instructions and examples <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   Prompts were hard to generalize, becoming long and convoluted <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
    *   A "cat and mouse chase" ensued, where fixing one scenario broke another <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   There was a lack of prompt versioning <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Scaling Challenges (Similar to Manual Process):**
    *   **Expense:** Inability to optimize for caching due to response variability and constant prompt tweaks <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   **Latency:** The baseline latency was slow, hindering concurrent scaling <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    *   **AI Errors:** Hallucinations were difficult to catch, posing a different nature of error compared to human errors <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

Despite these issues, GPT-4 was kept in production for specific use cases where it performed well <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## The Shift to [[building_scalable_ai_systems | Building Scalable AI Systems]]

The problem evolved from parsing unstructured data to [[building_scalable_ai_systems | building a robust]], [[building_and_improving_ai_agents | agentic workflow]] that could handle high volume reliably <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

Method's scaling targets were ambitious:
*   16 million requests per day <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>
*   100K concurrent load <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>
*   Minimal latency (sub-200 milliseconds) for real-time agentic workflows <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>

## OpenPipe's Role in Optimization

OpenPipe partnered with Method to address quality, cost, and latency issues, common challenges for many companies [[scaling_ai_solutions_in_production | scaling AI solutions in production]] <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### Benchmarking Existing Models

To begin, OpenPipe benchmarked existing models against Method's specific task:

*   **Error Rates:**
    *   GPT-4: ~11% <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
    *   O03 Mini: ~4% <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>
    *   Error rates were measured by comparing the agent's final outputs to human-verified correct data <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Latency:**
    *   GPT-4: ~1 second <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>
    *   O03 Mini: ~5 seconds <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
    *   Measurements were conducted under real production conditions with diverse tasks and concurrency levels <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Cost:**
    *   Surprisingly, O03 Mini was slightly more expensive than GPT-4 for Method's use case, despite a lower per-token cost <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This was due to O03 Mini generating significantly more "reasoning tokens," leading to longer outputs <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### Defining Performance Requirements

Method needed to define target performance metrics, knowing that post-processing checks provided a safety net:

*   **Error Rate:** Around 9% was acceptable, as additional checks would catch further errors <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Latency:** A hard latency cut-off was essential for the real-time agent system <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   **Cost:** Due to high volume, cost was a critical factor <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

Neither GPT-4 nor O03 Mini could meet all three requirements simultaneously <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. GPT-4 fell short on error rate and cost, while O03 Mini failed on cost and especially latency <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## The Solution: Fine-Tuning with OpenPipe

Fine-tuning is a "power tool" that requires more engineering investment than simple prompt engineering but is crucial when production models don't meet necessary performance benchmarks <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

OpenPipe fine-tuned a custom model for Method's specific use case, significantly bending the price-performance curve <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>:

*   **Improved Error Rate:** The fine-tuned model achieved significantly better accuracy than GPT-4, surpassing the required threshold <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This was made easier by using existing production data and a "teacher model" like O03 Mini to generate training data <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. The model deployed was an 8 billion parameter LL 3.1 model <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   **Lower Latency:** Moving to a much smaller (8 billion parameter) model drastically reduced latency due to fewer calculations <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. It also allowed for potential co-location with application code to eliminate network latency entirely <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Reduced Cost:** The significantly smaller model resulted in a much lower cost, exceeding Method's target cost thresholds and eliminating unit economics concerns <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

## Key Takeaways for [[building_and_improving_ai_agents | Building and Improving AI Agents]]

*   **Simplicity and Efficiency:** Method successfully used the cheapest available model and fine-tuned it using existing production data from GPT <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. There's no need to buy dedicated GPUs <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
*   **Patience for [[developing_and_optimizing_ai_agents | Productionizing AI Agents]]:** [[developing_and_optimizing_ai_agents | Productionizing AI agents]] requires openness and patience from engineering and leadership <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. Unlike traditional code that's expected to work flawlessly and not break, AI agents take time to become production-ready and provide desired responses <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

Fine-tuning is a powerful method to achieve desired reliability numbers and strongly bend the price-performance curve, enabling organizations to scale AI solutions to a very large degree in production <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.