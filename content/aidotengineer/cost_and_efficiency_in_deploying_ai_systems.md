---
title: Cost and efficiency in deploying AI systems
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Deploying AI systems, especially those relying on Large Language Models (LLMs) and intelligent agents, presents significant challenges related to cost, efficiency, and scalability in production environments <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Method, a company that aggregates and enhances liability data for fintechs, banks, and lenders <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, faced these challenges when trying to extract specific financial data points like payoff amounts or escrow balances <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Initial Challenges and Traditional Approaches

Method's customers required liability-specific data points that were not available via a central API from credit bureaus, card networks, or financial institutions <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Directly integrating with banks would take years, which was not feasible for an early-stage company needing to build fast <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

Competitors often rely on inefficient manual processes involving offshore teams of contractors <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. These teams would call banks, authenticate, gather information, and then have it proof-checked and integrated into financial platforms <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

This traditional approach was:
*   **Inefficient and not scalable**: One person could only do one thing at a time, requiring more hires to scale <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Expensive**: Direct correlation between scale and labor cost <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Slow**: The synchronous nature of human interaction <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Prone to Human Error**: High risk of inaccurate financial information being surfaced, necessitating additional teams for fact-checking <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

The core problem was making sense of unstructured data, which conceptually resembled an API interaction with request, authentication, and response validation components <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Adoption of AI Agents and Early Hurdles

With the "Cambrian explosion" of AI following OpenAI's GPT-4 announcement <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, Method saw an opportunity. Advanced LLMs, particularly post-GPT-4, are excellent at parsing unstructured data for tasks like summarization and classification <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Method quickly built an agentic workflow using GPT-4, which worked well for initial use cases <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

However, scaling this solution revealed significant challenges:

### [[cost_considerations_in_ai_agent_deployment | Cost Considerations]]
*   **High API Costs**: Method's first month in production with GPT-4 resulted in a bill of $70,000 <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Although the value derived was immense, this created significant concern for leadership <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Lack of Optimization**: Due to the variability in responses and constant prompt tweaks, caching could not be optimized, making each API call costly <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Prompt Engineering Limitations
*   **Scaling Difficulty**: Prompt engineering "only takes you so far" <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Lack of Domain Expertise**: While smart, GPT-4 is not a financial expert, requiring "really detailed instructions and examples" for specific use cases <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Convoluted Prompts**: Prompts became long, convoluted, and difficult to generalize <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Instability**: Fixing one scenario would break another, leading to a continuous "cat and mouse chase" without proper prompt versioning <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### General Scaling Challenges
*   **Latency**: The baseline latency of GPT-4 was too slow for concurrent scaling <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   **AI Errors (Hallucinations)**: Similar to human errors, AI models introduced "hallucinations" that were difficult to catch <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

Despite these issues, Method continued using GPT-4 for specific use cases where it performed well <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The problem then shifted from data interpretation to [[scaling_ai_solutions_in_production | building scalable AI systems]] capable of handling high volume reliably <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Defining Production Requirements and Benchmarking

Method aimed for significant scale:
*   16 million requests per day <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>
*   100K concurrent load <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>
*   Minimal latency (sub-200 milliseconds) for real-time agentic workflows <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>

OpenPipe collaborated with Method to address these challenges, focusing on quality, cost, and latency <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. They benchmarked existing models under real production conditions:

| Model    | Error Rate | Latency   | Cost (relative) | Notes                                           |
| :------- | :--------- | :-------- | :-------------- | :---------------------------------------------- |
| GPT-4    | 11%        | ~1 second | Higher          | Good quality but high cost, slower              |
| O3 Mini  | 4%         | ~5 seconds | Even Higher     | Better quality but much slower, surprisingly more expensive due to reasoning tokens <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a> |

Method's target requirements were:
*   **Error Rate**: Around 9% was acceptable due to additional post-processing checks <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Latency**: A hard cut-off was necessary for the real-time agent system <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Cost**: Very important due to the high volume of requests <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

Neither GPT-4 nor O3 Mini met all three critical requirements for production deployment <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

## Fine-tuning as a Solution for [[efficiency_and_smart_execution_in_ai_systems | Efficient and Cost-effective AI]]

[[best_practices_for_ai_deployment_and_optimization | Fine-tuning]] emerged as a "power tool" to overcome these limitations <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. While it requires more engineering investment than prompt engineering, it significantly "bends the price performance curve" <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

The benefits of fine-tuning for Method's specific use case were:
*   **Improved Quality**: A fine-tuned model achieved significantly better accuracy than GPT-4, easily surpassing the 9% error rate threshold <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This was made easier by using existing production data and models like O3 Mini as "teacher models" <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   **Lower Latency**: By deploying a much smaller model (e.g., an 8 billion parameter LL 3.1 model), latency was drastically reduced <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. This allows for fewer sequential calculations and potential co-location with application code to eliminate network latency <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   **Significantly Reduced Cost**: The smaller, fine-tuned models resulted in a much lower per-unit cost <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. This made the solution viable for Method's unit economics and high volume <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>, aligning with [[costeffective_ai_strategies | cost-effective AI strategies]].

## Key Takeaways for [[building_and_scaling_ai_use_cases_for_enterprises | Enterprise AI and ROI Challenges]]

*   **Simplicity and Cost-Effectiveness**: It is possible to achieve production-ready AI agents using the cheapest available models, fine-tuned for specific use cases. This approach avoids the need to purchase dedicated GPUs <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Patience and Openness**: Productionizing AI agents, unlike traditional software, requires patience and openness from engineering and leadership teams. AI models evolve and improve over time, and getting to a production-ready state requires continuous iteration and acceptance that the system might not always behave deterministically like traditional code <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
*   **Strategic Fine-tuning**: Fine-tuning is a powerful tool for [[best_practices_for_building_ai_systems | building scalable AI systems]] that can significantly improve performance and reduce costs when off-the-shelf models and prompt engineering fall short <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. It enables organizations to reach large-scale production deployments, as demonstrated by Method <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.