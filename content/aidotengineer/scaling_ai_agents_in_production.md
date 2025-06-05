---
title: Scaling AI agents in production
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Method, a company focused on aggregating and enhancing liability data for fintechs, banks, and lenders, faced significant challenges in acquiring specific liability data points like auto loan payoff amounts or mortgage escrow balances <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. Traditional data partners offered no central API, and direct bank integrations would take years <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

## Initial Approaches and Their Limitations

Initially, many companies addressing this problem relied on inefficient manual processes <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. This involved offshore teams of contractors calling banks, authenticating, gathering information, proof-checking it, and then integrating it into financial platforms <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

This manual approach presented several [[challenges_in_scaling_ai_products | scaling challenges]]:
*   **Inefficiency and Expense**: One person could only handle one task at a time, requiring more hires to scale <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   **Slowness**: The synchronous nature of human calls made the process very slow <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
*   **Human Error**: Significant potential for inaccuracies, requiring additional teams for fact-checking and proof-checking <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. Surfacing inaccurate financial information was a major concern <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.

Conceptually, this process resembled an API with request, authentication, and response validation components, highlighting the core problem of making sense of unstructured data <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

### The Rise of LLMs as a Solution

With the "Cambrian explosion" of AI following OpenAI's GPT-4 announcement, Method saw a potential solution <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>. Advanced LLMs, particularly post-GPT-4 models, proved highly effective at parsing unstructured data for tasks like summarization and classification <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

Method quickly developed an [[building_effective_ai_agents | agentic workflow]] using GPT-4, which performed very well in initial controlled tests <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. It was particularly good at extracting multiple data points from a single API call <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

## Challenges with Scaling LLM-Based Agents

While promising, scaling the GPT-4 solution in production quickly exposed significant challenges:
*   **Exorbitant Costs**: The first month in production with GPT-4 incurred a cost of $70,000 <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. Although the value was immense, this was unsustainable <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. Optimization for caching was difficult due to variability in responses and constant prompt tweaks <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.
*   **Prompt Engineering Limitations**: As use cases scaled, prompt engineering proved insufficient <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. GPT, despite its intelligence, wasn't a financial expert and required extremely detailed, specific instructions and examples <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. Prompts became long, convoluted, and difficult to generalize, leading to a "cat and mouse" game where fixes for one scenario broke others <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. There was also a lack of prompt versioning <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.
*   **Latency**: The baseline latency of GPT-4 was too slow for concurrent scaling <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>.
*   **AI Errors (Hallucinations)**: Similar to human errors, AI agents produced hallucinations that were difficult to catch <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.

Despite these issues, the system remained in production for specific use cases where its performance was excellent <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.

## Method's Scaling Requirements

The challenge shifted from merely parsing unstructured data to [[scaffolding_ai_agents_for_scalability | building a robust and scalable agentic workflow]] <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>. Method's target requirements for their real-time agentic workflow were:
*   **Volume**: At least 16 million requests per day <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
*   **Concurrency**: At least 100,000 concurrent loads <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   **Latency**: Sub-200 milliseconds to handle real-time operations <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.

## OpenPipe's Solution: Custom Model Fine-Tuning

OpenPipe partnered with Method to address these common issues of quality, cost, and latency <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.

### Benchmarking Existing Models
To understand the baseline, OpenPipe benchmarked existing models under production conditions <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>:
*   **Error Rates**:
    *   GPT-4: ~11% <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>
    *   O3 Mini: ~4% <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>
    *(Error rates were measured by comparing agent outputs to human-verified correct answers from the agentic workflow)* <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>
*   **Latency**:
    *   GPT-4: ~1 second <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>
    *   O3 Mini: ~5 seconds <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>
*   **Cost**: Interestingly, O3 Mini was slightly more expensive for Method's specific use case despite its lower per-token cost, due to generating many more "reasoning tokens" and longer outputs <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.

### Defining Target Performance
Method's specific needs for their real-time system and internal checks helped define target performance:
*   **Error Rate**: Around 9% was acceptable, given additional plausibility checks after the model output <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
*   **Latency**: A hard latency cut-off was essential for the real-time agent workflow <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.
*   **Cost**: Given the very high volume of requests, cost was a critical factor <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.

Neither GPT-4 nor O3 Mini could meet all three requirements simultaneously. GPT-4 fell short on error rate and cost, while O3 Mini failed on cost and especially latency <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>.

### The Role of Fine-Tuning
When off-the-shelf models fail to meet production requirements through prompt engineering alone, [[best_practices_for_building_ai_agents | fine-tuning]] custom models becomes a powerful tool <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>. It requires more engineering investment than just prompting but can significantly "bend the price-performance curve" <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.

### Results with Fine-Tuning
OpenPipe fine-tuned an 8 billion parameter LL 3.1 model for Method, leading to significant improvements that met and exceeded their targets <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>:
*   **Quality (Error Rate)**: The fine-tuned model achieved significantly better accuracy than GPT-4, surpassing the 9% error rate threshold <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>. This was made easier by using production data and models like O3 Mini to generate training outputs <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   **Latency**: Moving to a much smaller 8 billion parameter model drastically reduced latency, making it much easier to deploy in a low-latency way <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>. This also opens the possibility of collocating the model with application code to eliminate network latency <a class="yt-timestamp" data-t="15:49:00">[15:49:00]</a>.
*   **Cost**: The smaller fine-tuned model resulted in a "much, much lower cost," far exceeding Method's viability thresholds <a class="yt-timestamp" data-t="16:03:00">[16:03:00]</a>.

## Key Takeaways for [[implementing_ai_agents_in_daily_operations | Implementing AI Agents in Daily Operations]]

*   **Simplicity and Cost-Effectiveness**: It's possible to start with the cheapest available model and fine-tune it <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. Method leveraged their existing production data from GPT-4 for fine-tuning, avoiding the need to acquire new data <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. Buying custom GPUs isn't always necessary <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.
*   **Patience and Openness**: [[role_of_engineering_teams_in_ai_agent_production | Productionizing AI agents]] requires a degree of openness and patience from both engineering and leadership teams <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. Unlike traditional code, AI agents take time to become production-ready and provide desired responses consistently, as they are not "write once, never break" systems <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.