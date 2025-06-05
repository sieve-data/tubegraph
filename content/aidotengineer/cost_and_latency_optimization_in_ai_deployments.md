---
title: Cost and latency optimization in AI deployments
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

This article explores the journey of Method, a company that aggregates and centralizes liability data, and their collaboration with OpenPipe to overcome challenges in [[scaling_ai_agents_in_production | scaling AI agents in production]] to over 500 million agents. The focus is on optimizing cost and latency in AI deployments <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Method's Core Business

Method collects and centralizes liability data from hundreds of sources, including credit bureaus, card networks (Visa, MasterCard), direct financial institutions, and third-party sources <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This enhanced data is served to customers, typically other fintechs, banks, or lenders, for debt management purposes such as refinancing, loan consolidation, liability payments, or personal finance management <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

OpenPipe assists in building, training, and deploying open-source models for practical use, enabling continuous model improvement using user and environmental signals from production <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Initial Challenges: Manual Data Collection

Early on, Method's customers requested liability-specific data points like payoff amounts on auto loans or escrow balances for mortgages <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Research revealed no central API for these data points <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Direct integration with banks would take years, which was not feasible for an early-stage company aiming for rapid deployment <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

The status quo for many companies obtaining this data involved hiring offshore teams of contractors <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. These teams would:
*   Call banks on behalf of the company and end-consumer <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   Authenticate with banks and gather information <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   Require human proof-checking before integration into financial platforms for underwriting or user surfacing <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

This manual process was highly inefficient and problematic for [[challenges_in_scaling_ai_products | scaling AI products]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>:
*   **Expensive:** One person can only do one task at a time, requiring more hires to scale <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Slow:** The synchronous nature of the process made it inherently slow <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Human Error:** Significant risk of human error, necessitating additional teams for fact-checking and proof-checking, with inaccurate financial information being the worst outcome <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

Conceptually, this process resembled an API with request, authentication, and response validation components <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. The core problem was making sense of unstructured data <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Embracing AI: GPT-4 as the Initial Solution

The announcement of GPT-4 by OpenAI, amidst the "Cambrian explosion" of LLM-enabled applications, presented a seemingly perfect solution for Method <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Advanced LLMs, particularly post-GPT-4, excel at parsing unstructured data for tasks like summarization and classification <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Method quickly developed an agentic workflow using GPT-4, which performed exceptionally well <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. They expanded use cases to maximize value from single API calls, testing different extractions in a controlled production environment <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### The Problem of Scale with Off-the-Shelf LLMs

As traffic increased, significant challenges emerged:

*   **Prohibitive Cost:** The first month in production with GPT-4 incurred a bill of $70,000 <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Despite leadership initially accepting this due to the immense value, it highlighted a major [[cost_considerations_in_ai_agent_development | cost consideration]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Prompt Engineering Limitations:** Prompt engineering quickly became a scaling bottleneck <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. While GPT-4 is intelligent, it lacked financial expertise, requiring highly detailed, generalized, and complex instructions with examples <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This led to a "cat and mouse" chase where fixes for one scenario broke others <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. The absence of prompt versioning exacerbated these issues <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Inefficiency and Scalability Issues:**
    *   **Costly:** Difficulty optimizing for caching due to variability in responses and frequent prompt tweaks <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Slow Latency:** Baseline latency was too high, hindering concurrent scaling <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    *   **AI Errors:** "Hallucinations" were difficult to catch, similar to human errors but in a different nature <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

Despite these issues, GPT-4 remained in production for specific use cases where it performed exceptionally well <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## The Shift in Problem: Scaling a Robust Agentic Workflow

The problem evolved from merely understanding unstructured data (solved by GPT) to building a robust, scalable agentic workflow that could handle significant volume reliably <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Method's target scale required:
*   At least 16 million requests per day <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   At least 100,000 concurrent load <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   Minimal latency (sub 200 milliseconds) for real-time agentic workflows <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

This led to the question of whether to invest in more GPUs or host their own models <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## OpenPipe's Approach: Benchmarking and Fine-Tuning

OpenPipe collaborated with Method to address the common issues of quality, [[cost_management_in_ai_projects | cost]], and latency in AI deployments <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Benchmarking Existing Models

OpenPipe began by measuring error rates, latency, and costs under real production conditions, using a diverse range of tasks and reasonable concurrency levels <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

*   **Error Rates:**
    *   GPT-4: ~11% error rate <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
    *   O3 Mini: ~4% error rate <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    *   Method could measure this easily by comparing the agent's final outputs (bank balances, etc.) against human-validated real numbers <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **Latency:**
    *   GPT-4: ~1 second to respond <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
    *   O3 Mini: ~5 seconds for their specific task <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Cost:**
    *   Despite O3 Mini having a lower per-token cost than GPT-4, it was found to be more expensive for Method's use case due to generating many more "reasoning tokens" and thus longer outputs <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

> [!NOTE] Recommendation for Benchmarking
> It's recommended to benchmark different models using simple Python scripts to categorize performance for your specific use case, especially when optimizing after an initial proof of concept <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This allows quick comparison as new models emerge <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

### Defining Target Requirements

Method's specific needs for their real-time agent system were:
*   **Error Rate:** Around 9% error rate was acceptable, as they had subsequent plausible checks for numbers <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Latency:** A strict latency cut-off was required for their real-time system <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This varies widely by customer, from days for background batch processes to sub-500ms for real-time voice applications <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **Cost:** Due to the high volume, cost was very important to Method <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Identifying the Gap

Neither GPT-4 nor O3 Mini could simultaneously meet all three requirements (quality, latency, and cost) <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. GPT-4 fell short on error rate and cost, while O3 Mini failed on cost and especially latency <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

## Fine-Tuning as a "Power Tool"

OpenPipe's solution involved fine-tuning and building custom models for Method's specific use case <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

> [!WARNING] When to Fine-Tune
> Fine-tuning is a "power tool" that requires more engineering investment than prompt engineering. It should only be pursued after benchmarking existing production models with simple prompting and determining they cannot meet the necessary performance numbers <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

Fine-tuning significantly "bends the price-performance curve" <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>:

*   **Error Rate Improvement:** Fine-tuning enabled Method to achieve significantly better error rates than GPT-4, surpassing their required threshold <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. This has become easier with models like O3 Mini, which allow using production data to generate outputs and train a smaller model (the "teacher model" approach) <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Reduced Latency:** Moving to a much smaller model (an 8 billion parameter LL 3.1 model in Method's case) dramatically lowered latency due to fewer sequential calculations <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. It also allows for deployment within one's own infrastructure, co-locating the model with application code to eliminate network latency <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. This contributes to [[efficiency_and_smart_execution_engines_in_ai_applications | efficiency and smart execution engines in AI applications]].
*   **Lower Cost:** The use of a significantly smaller, fine-tuned model resulted in a much lower cost, exceeding Method's target cost thresholds and eliminating concerns about unit economics <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This is a key aspect of [[leveraging_ai_tools_for_efficiency_and_scalability | leveraging AI tools for efficiency and scalability]] and [[customization_and_scalability_in_ai_models | customization and scalability in AI models]].

For the majority of OpenPipe's customers, an 8 billion parameter model or smaller is sufficient to meet quality targets <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

## Key Takeaways for AI Agent Deployment

*   **Simplicity and Focus:** It's not overly complicated to achieve scale. Identify a specific use case, leverage the cheapest suitable model, and fine-tune it <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. Method successfully used production data from GPT-4 for fine-tuning, avoiding the need to acquire new data <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **No Need for Personal GPUs:** Businesses don't necessarily need to buy their own GPUs for successful AI deployments <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. This is relevant to [[nvidia_ai_model_deployment_and_architecture | Nvidia AI model deployment and architecture]] and [[leveraging_existing_infrastructure_for_ai_integration | leveraging existing infrastructure for AI integration]].
*   **Patience and Openness:** Productionizing AI agents requires patience and openness from engineering and leadership teams <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>. Unlike traditional code, which is expected to "just work" after deployment, AI agents take time to become production-ready and consistently deliver desired responses due to their probabilistic nature <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.

Fine-tuning is a powerful method to achieve high reliability and bend the price-performance curve, enabling large-scale production deployments just like Method achieved <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.