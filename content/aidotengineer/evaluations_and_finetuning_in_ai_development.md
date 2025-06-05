---
title: Evaluations and finetuning in AI development
videoId: VhPfM_aGBVc
---

From: [[aidotengineer]] <br/> 

Developing AI applications successfully requires careful consideration of [[evaluating_ai_system_performance | evaluations]] and strategic application of [[finetuning_ai_models_for_specific_use_cases | fine-tuning]]. These elements are crucial for ensuring models perform as expected and deliver real business value.

## The Importance of Evaluations

[[importance_of_evaluations_in_ai_projects | Evaluations]] are fundamental to guiding AI development towards desired outcomes <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. They provide empirical data to understand how changes in model functions (e.g., prompt engineering, prompt caching) affect performance <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

### Common Mistakes in AI Evaluation

A frequent error in AI development is to build a robust workflow or architecture first, and only *then* consider building evaluations <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This approach is suboptimal because evaluations should ideally guide the entire development process <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

Other common pitfalls include:
*   **Struggling with data problems** preventing effective eval design <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Claude can assist with data cleanup and reconciliation for evaluation purposes <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **"Trusting the vibes"** instead of rigorously testing on representative samples <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. It's essential to have enough samples to ensure statistical significance and predict performance in production environments <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### Best Practices for Designing Evaluations

Effective [[steps_to_create_effective_evaluations_for_ai_applications | evaluations]] help navigate the "latent space" of possible model behaviors, guiding developers to an optimized point faster than competitors <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

Key practices include:
*   **Setting up telemetry** to back-test architectures in advance <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   **Designing representative test cases** that include unusual or "silly" examples to ensure models respond appropriately or reroute questions <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

### Defining Metrics for Success

Organizations often face a trade-off between intelligence, cost, and latency <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Defining this balance in advance for a specific use case is crucial <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

*   **Customer Support Example:** For a customer support agent, speed (e.g., response within 10 seconds) might be prioritized over extensive intelligence, as customers tend to leave if responses are too slow <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. User experience (UX) solutions, like a "thinking box" or redirection, can help manage latency <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
*   **Financial Research Example:** For a financial research analyst agent, accuracy and comprehensive answers might be paramount, even if it takes 10 minutes to generate a response, given the high stakes of financial decisions <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.

The stakes and time sensitivity of the decision should drive optimization choices <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

### Case Study: Intercom and Finn 2

Intercom, an AI customer service platform, partnered with Anthropic to enhance their AI agent, Finn <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   **Initial Sprint:** Applied AI teams ran a two-week sprint with Intercom's data science team, comparing Finn's hardest prompts against prompts optimized with Claude <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Optimization Phase:** Following positive initial results, a two-month sprint focused on [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] and optimizing all prompts to maximize Claude's performance <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Results:** Benchmarks showed Anthropic's model outperforming their previous LLM <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Finn 2, powered by Anthropic's model, can solve up to 86% of customer support volume (51% out of the box) <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. It also improved human-like interaction by allowing adjustments to tone and answer length, and showed strong policy awareness (e.g., refund policies) <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

## Finetuning AI Models

[[finetuning_ai_models_for_specific_use_cases | Fine-tuning]] is often considered a "silver bullet," but it comes with significant costs and limitations <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

### When to Approach Finetuning with Caution

```ad-warning
Fine-tuning involves "brain surgery" on the model, which can limit its reasoning abilities in domains outside of what it was specifically fine-tuned for <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
```

It is recommended to try other approaches first before resorting to [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. Many developers attempt fine-tuning without a clear [[evaluations_versus_traditional_metrics_in_ai | evaluation]] set or success criteria <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. [[finetuning_ai_models_for_specific_use_cases | Fine-tuning]] should only be pursued if the desired intelligence cannot be achieved through other methods in a specific domain <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.

The wide variance in success rates for [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] means that the effort and cost involved must be clearly justified <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Don't let the pursuit of [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] slow down your initial progress; integrate it later if necessary <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

### Alternatives to Finetuning

Beyond basic prompt engineering, various features and architectures can significantly improve use case success without immediate fine-tuning:
*   **Prompt Caching:** Can lead to a 90% cost reduction and 50% speed increase without sacrificing model intelligence <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Contextual Retrieval:** Drastically improves performance by feeding relevant information to the model more effectively, reducing processing time <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
*   **Citations:** Can be an out-of-the-box solution <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.
*   **Agentic Architectures:** An architectural decision that can enhance model capabilities <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.

These methods offer powerful ways to optimize AI model performance before considering the complexities and costs associated with [[finetuning_ai_models_for_specific_use_cases | fine-tuning]].