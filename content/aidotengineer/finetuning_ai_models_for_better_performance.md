---
title: Finetuning AI models for better performance
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Finetuning AI models is a powerful technique used to optimize their performance for specific use cases, often addressing challenges related to quality, cost, and latency in [[scaling_ai_solutions_in_production | production environments]] <a class="yt-timestamp" data-t="08:42:15">[08:42:15]</a>. This approach involves building custom models tailored to an application's unique needs <a class="yt-timestamp" data-t="13:39:58">[13:39:58]</a>.

## Challenges with Off-the-Shelf Models

Method, a company that collects and centralizes liability data, faced significant [[challenges_with_early_ai_models_and_improvements | challenges]] when attempting to extract specific liability data points (e.g., payoff amounts, escrow balances) using existing data sources <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. There was no central API, and direct bank integrations would take years <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. The traditional method involved manual, inefficient, and error-prone offshore teams making phone calls to banks <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

The company initially turned to [[advancements_in_ai_model_technology_and_performance | advanced LLMs]] like GPT-4, which excelled at parsing unstructured data <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a> and worked well in controlled environments <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. However, [[scaling_ai_solutions_in_production | scaling]] GPT-4 in production led to several issues:
*   **High Costs** GPT-4 incurred a cost of $70,000 in the first month of production traffic <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. While valuable, this cost was unsustainable <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   **Prompt Engineering Limitations** Prompt engineering proved insufficient for complex use cases, requiring overly detailed and convoluted instructions <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. This led to a "cat and mouse chase" where fixes for one scenario broke another <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.
*   **Latency** GPT-4's baseline latency was slow, preventing concurrent [[scaling_ai_solutions_in_production | scaling]] <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
*   **AI Errors** Hallucinations were difficult to catch, leading to inaccurate financial information <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

Despite these issues, GPT-4 remained in production for specific use cases where it performed well <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. The problem then shifted to how to [[scaling_ai_solutions_in_production | scale]] this system robustly <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>. Method aimed for 16 million requests per day, 100K concurrent load, and sub-200 millisecond latency <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>.

## Benchmarking Existing Models

Before considering fine-tuning, it's crucial to benchmark existing production models to understand their performance against specific business requirements <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. For Method, [[building_custom_evaluations_for_better_ai_performance | evaluation metrics]] included:

*   **Error Rate:**
    *   GPT-4: 11% error rate <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.
    *   O3 Mini: 4% error rate <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.
    *   Error rates were measured by comparing agent outputs to human-verified correct data <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. Method's target error rate was around 9%, as they had additional plausibility checks <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
*   **Latency:**
    *   GPT-4: Around 1 second <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.
    *   O3 Mini: About 5 seconds for their task <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
    *   Method required sub-200 millisecond latency for its real-time agentic workflow <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>.
*   **Cost:**
    *   O3 Mini, despite lower per-token cost, was more expensive than GPT-4 for Method's use case due to generating many more reasoning tokens <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>.
    *   Cost is highly dependent on volume and use case <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.

Neither GPT-4 nor O3 Mini met all three requirements for Method's production needs <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>.

## The Power of Fine-Tuning

When off-the-shelf models or prompt engineering prove insufficient, fine-tuning becomes a viable solution <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>. Fine-tuning is considered a "power tool" that requires more engineering investment than simple prompting but can significantly improve the price-performance curve <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.

OpenPipe collaborated with Method to fine-tune a custom model, demonstrating significant improvements:
*   **Improved Quality (Error Rate):** The fine-tuned model achieved an error rate significantly better than GPT-4 <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>. This is now easier to achieve by using production data and a "teacher model" (like O3 Mini) to generate outputs for training <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>.
*   **Reduced Latency:** By moving to a much smaller, fine-tuned model (e.g., an 8 billion parameter LL3.1 model), latency was drastically reduced <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>. Fewer calculations lead to lower latency, and models can even be deployed within an organization's own infrastructure to eliminate network latency <a class="yt-timestamp" data-t="15:47:00">[15:47:00]</a>. For most customers, models of this size or smaller are sufficient <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>.
*   **Lower Costs:** The smaller fine-tuned model resulted in a much lower cost <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>, far exceeding Method's cost thresholds and making the solution economically viable <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>.

## When to Fine-Tune

Fine-tuning is a powerful tool to be used when prompt engineering with existing models cannot achieve the required reliability numbers <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>. It allows for a strong bend in the price-performance curve, enabling large-scale production deployment <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>.

## Productionizing AI Agents

[[finetuning_and_production_stability_of_open_ai_models | Productionizing AI agents]] requires a level of openness and patience from engineering and leadership teams <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. Unlike traditional software development where code is expected to work without breaking, AI agents take time to become production-ready and consistently deliver desired responses <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>. For Method, fine-tuning enabled them to use a cheaper, faster model, leveraging existing GPT-generated data for training without needing to acquire their own GPUs <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>.