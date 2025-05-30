---
title: Strategies for scaling AI with local LLMs
videoId: EMuBqcO048E
---

From: [[colemedin]] <br/> 

[[working_with_local_large_language_models | Running your own large language models locally]] is a popular trend, with dozens of powerful LLMs available for download and self-hosting <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach eliminates per-token costs and keeps data protected within your infrastructure <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While [[comparison_between_local_and_large_ai_models | local LLMs]] may not outperform top closed-source models like Claude 3.5 Sonnet, they are highly effective with the right setup <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Challenges of [[running_ai_agents_on_local_machines | Running Powerful Local LLMs]]

A significant challenge arises when attempting to use powerful [[working_with_local_large_language_models | local LLMs]], such as Llama 3.1, on personal hardware <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Initial attempts often result in long response times or timeouts, indicating insufficient hardware <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. [[running_ai_agents_on_local_machines | Running powerful local LLMs]] demands extremely robust hardware, specifically GPUs costing at least two thousand dollars, even for the weakest version of Llama 3.1 <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This doesn't include ongoing electricity costs <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Cloud-based GPU machines are an alternative, but can exceed a dollar per hour, accumulating costs quickly <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

While [[working_with_local_large_language_models | local LLMs]] offer flexibility, privacy, and scalability due to the absence of per-token fees, the initial investment can be hundreds or thousands of dollars <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Although they become the most affordable at scale, reaching that point can be difficult <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## A Phased Strategy for [[extending_local_ai_infrastructure | AI Integration]]

Unless a large initial investment is feasible, immediately [[extending_local_ai_infrastructure | running local AI]] is often unrealistic <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. A simple yet effective strategy involves two phases:

1.  **Pay-per-token with self-hostable models**: Utilize services that allow paying per token for openly available models at a low cost <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
2.  **Scale to self-hosting**: Transition to hosting these models on your own hardware when it becomes economically sensible <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

This approach ensures you only incur significant costs when beneficial and avoids switching LLMs, which can lead to unintended consequences <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Phase 1: Leveraging Groq for Cost-Effective Inference

For the initial phase, **Groq** is recommended as an AI service for paying per token <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

#### Advantages of Groq:

*   **Speed**: Groq boasts impressive speeds, capable of generating approximately 1,200 tokens per second (roughly 1,000 words per second), significantly faster than most LLMs <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Affordability**: It is "insanely cheap," often free for light requirements due to an indefinite free tier <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. For Llama 3.1 70B, it costs 59 cents per million tokens, equating to 1.69 million tokens per dollar <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This is significantly more affordable compared to closed-source models like GPT-4o and Claude 3.5 Sonnet, and even competitive with other services like Together AI <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Ease of Use**:
    *   **OpenAI API compatibility**: Integrate Groq by simply replacing the base URL in an OpenAI instance, adding your Groq API key, and selecting the model <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   **LangChain**: A `pip install langchain-groq` and setting an environment variable for the API key provides access to the `ChatGroq` instance <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   **n8n**: Groq is a natively supported option within n8n's tools agent node, requiring only the Groq API key for credentials <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

> [!WARNING] Data Privacy
> While Groq offers better privacy than closed-source models by not training on user data, it is still a third-party service <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. For highly private data during proof-of-concept development, consider using mock data until you transition to [[working_with_local_large_language_models | local, self-hosted LLMs]] <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### Phase 2: Determining the Switch to Self-Hosting

The transition from a pay-per-token model (like Groq) to [[running_ai_agents_on_local_machines | self-hosting your LLM]] occurs when the latter becomes more cost-effective <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

> [!INFO] Cloud vs. On-Premise
> While building a local machine is possible, paying for a GPU machine in the cloud is generally more flexible due to easier maintenance, no electricity costs, and simpler upgrades <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. Recommended cloud providers include RunPod and DigitalOcean <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. RunPod typically offers more competitive pricing compared to DigitalOcean <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

#### Calculation for Switch Point:

Let's calculate when it makes sense to switch, using an A40 GPU instance on RunPod as an example, which costs 39 cents per hour and has 48GB of VRAM, suitable for Llama 3.1 70B <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

1.  **Cost of Cloud Instance per Month**:
    *   Hourly Cost: $0.39 <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>
    *   `0.39 * 24 (hours/day) * 30 (days/month) = $280.80` per month <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

2.  **Groq Tokens per Dollar**:
    *   For Llama 3.1 70B, Groq provides 1.69 million tokens per $1 <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

3.  **Average Tokens per Prompt**:
    *   Prompts can vary greatly (few thousand to 20,000 tokens) <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
    *   For this example, we'll use a rough estimate of **5,000 tokens per prompt** <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. You can track this in your application to get an accurate average <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

4.  **Prompts per Dollar with Groq**:
    *   `1,690,000 (tokens/$1) / 5,000 (tokens/prompt) = 338` prompts per $1 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

5.  **Total Prompts at Which Self-Hosting Becomes Cheaper**:
    *   Multiply Groq's prompts per dollar by the monthly cost of the RunPod instance:
    *   `338 (prompts/$1) * 280.80 ($/month) = 94,958.4` prompts per month <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

    This means if your application makes over `94,958` prompts per month, it becomes more affordable to self-host on a cloud GPU instance like the A40 <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

6.  **Daily Prompt Threshold**:
    *   `94,958 (prompts/month) / 30 (days/month) = 3,165` prompts per day <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

    If your application reaches around 3,000 prompts per day, where, for instance, 3,000 users each make one call to your LLM, it becomes worthwhile to switch to [[extending_local_ai_infrastructure | self-hosting your LLM]] <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

This calculation can be made highly accurate by determining your specific average tokens per prompt and the exact pricing for your chosen model and cloud instance <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

By following this strategy, businesses can avoid large upfront investments, develop proofs of concept with affordable per-token services, and then scale to [[extending_local_ai_infrastructure | self-hosting LLMs]] to save thousands of dollars when user demand justifies it <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.