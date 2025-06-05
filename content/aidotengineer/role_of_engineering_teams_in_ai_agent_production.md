---
title: Role of engineering teams in AI agent production
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Engineering teams play a crucial role in bringing AI agents to production, navigating challenges from initial concept to large-scale deployment. This involves identifying needs, selecting appropriate models, benchmarking performance, and optimizing for key metrics like quality, cost, and latency.

## Method's Challenge: Automating Financial Data Aggregation

Method, a company that centralizes liability data from various financial sources, faced a significant challenge when customers requested more specific liability data points, such as payoff amounts for auto loans or escrow balances for mortgages <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. Traditional methods, like integrating directly with banks, would take years <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

The existing status quo in the industry involved companies hiring offshore contractor teams to manually call banks, authenticate, gather information, proof-check, and integrate the data <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. This manual process was inefficient, expensive, slow, and prone to human error, often resulting in inaccurate financial information <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. Conceptually, this task was seen by the engineering team as making sense of unstructured data <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.

## Initial AI Agent Development and Production Issues

With the announcement of GPT-4, Method's engineering team saw an opportunity to automate this process, leveraging advanced LLMs' ability to parse unstructured data <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>. They quickly developed an "agentic workflow" using GPT-4, which initially performed well and allowed for expanded use cases <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.

However, scaling this initial solution in production revealed significant [[challenges_in_ai_agent_development | challenges in AI agent development]]:
*   **High Costs**: The first month in production with GPT-4 incurred a cost of $70,000, which made leadership "unhappy," though the value provided was immense <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   **Prompt Engineering Limitations**: As use cases scaled, prompt engineering reached its limits. Despite GPT's intelligence, it wasn't a financial expert, requiring extremely detailed and lengthy instructions and examples <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>. This led to a "cat and mouse chase" where fixes for one scenario broke others, and there was no prompt versioning <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.
*   **Scaling Inefficiency**: The system couldn't scale concurrently due to slow baseline latency and the inability to optimize for caching given the variability in responses and constant prompt tweaks <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.
*   **AI Errors (Hallucinations)**: Similar to human errors, AI agents introduced "hallucinations" that were difficult to catch <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

The problem for the engineering team shifted from finding a solution for unstructured data to [[scaling_ai_agents_in_production | scaling AI agents in production]] and [[building_effective_ai_agents | building effective AI agents]] with a robust agentic workflow <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>. Method's target production figures were ambitious: 16 million requests per day, 100K concurrent load, and sub-200 milliseconds latency <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>.

## Collaborating for Production-Ready AI Agents

OpenPipe collaborated with Method to address these common [[challenges_and_strategies_in_ai_production | challenges and strategies in AI production]]: quality, cost, and latency <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>. The engineering approach involved:

1.  **Benchmarking Existing Models**:
    *   **Error Rates**: GPT-4 had an 11% error rate, while O03 Mini had a 4% error rate for Method's specific task <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. Error rates were measured by comparing agent outputs to human-verified real numbers <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
    *   **Latency**: GPT-4 responded in about one second, while O03 Mini took about five seconds for the specific task <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.
    *   **Cost**: O03 Mini was slightly more expensive than GPT-4 due to generating more reasoning tokens and longer outputs, despite a lower per-token cost <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>. Engineering teams should benchmark using real production conditions and diverse tasks <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>.

2.  **Defining Target Metrics**:
    *   Method's quality target was around a 9% error rate, as they had subsequent checks to filter out inaccuracies <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
    *   Latency was critical due to the real-time nature of the agentic workflow, requiring a hard cut-off <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.
    *   Cost was highly important given the very high volume of operations <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.

3.  **Implementing Fine-Tuning**:
    *   Neither GPT-4 nor O03 Mini met all three requirements for production deployment <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>.
    *   Fine-tuning was identified as a "power tool" for [[developing_ai_agents_for_productivity | developing AI agents for productivity]] when off-the-shelf models don't meet performance needs <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>. It requires more engineering investment than prompt engineering alone <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.
    *   By fine-tuning an 8-billion parameter LL 3.1 model, the team achieved:
        *   **Improved Accuracy**: Significantly better error rates than GPT-4, meeting the required threshold <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.
        *   **Lower Latency**: Much faster response times due to the smaller model, even allowing for potential collocation with application code to eliminate network latency <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.
        *   **Reduced Cost**: Substantially lower costs compared to larger models <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.

## Key Takeaways for Engineering Teams

The experience highlights several [[best_practices_for_implementing_ai_in_teams | best practices for implementing AI in teams]]:
*   **Simplicity and Optimization**: Engineers can achieve success with a specific use case by using the cheapest available model and fine-tuning it <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. Production data from initial LLM use (e.g., GPT-4) can be used for fine-tuning, eliminating the need to search for new datasets <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.
*   **No Need for GPU Ownership**: It's not necessary to buy proprietary GPUs for deployment <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.
*   **Openness and Patience**: [[challenges_in_creating_effective_ai_agents | Productionizing AI agents]] requires a level of openness and patience from engineering and leadership teams <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. Unlike traditional code that is expected to work flawlessly upon release, AI agents need time to become production-ready and consistently deliver desired responses <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.

In conclusion, engineering teams are central to the entire lifecycle of AI agent production, from identifying problems and evaluating solutions to optimizing performance and addressing [[technical_challenges_in_ai_agent_development | technical challenges in AI agent development]] like cost, latency, and error rates. Fine-tuning emerges as a powerful strategy to bend the price-performance curve and achieve the scale required for real-world applications <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.