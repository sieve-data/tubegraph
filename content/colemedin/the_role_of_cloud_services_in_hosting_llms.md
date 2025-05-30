---
title: The role of cloud services in hosting LLMs
videoId: EMuBqcO048E
---

From: [[colemedin]] <br/> 

Running large language models (LLMs) locally presents significant challenges due to high hardware demands and associated costs <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. While powerful LLMs like [[using_llama_for_llms | Llama 3.1]] can be downloaded and self-hosted, they require incredibly powerful hardware, such as GPUs costing at least $2,000, even for the weakest versions <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This doesn't include the continuous electricity costs for 24/7 operation <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Challenges of Self-Hosting Local LLMs Directly
The upfront cost of self-hosting powerful LLMs can be hundreds or thousands of dollars <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Users might experience slow response times or timeouts if their hardware isn't sufficient <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Although local LLMs offer the most flexibility, privacy, and cost-effectiveness at scale (by avoiding per-token fees), reaching that scale with self-hosting can be a "painful" process initially <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. For more detail on these issues, see [[challenges_and_costs_of_selfhosting_local_llms | Challenges and Costs of Self-Hosting Local LLMs]].

## Cloud Hosting as a Flexible Alternative
To mitigate the initial investment and maintenance burdens, using GPU machines in the cloud is a recommended alternative <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Cloud hosting offers greater flexibility compared to building and maintaining a physical server, allowing for easier upgrades as new GPUs are released <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Cost of Cloud Services
Cloud GPU machines can cost more than a dollar per hour, which can quickly add up <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. However, services like RunPod offer competitive pricing <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. For example, an A40 instance with 48 GB of vRAM, sufficient for running [[using_llama_for_llms | Llama 3.1 70B]], costs $0.39 per hour in RunPod's secure cloud <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This translates to approximately $280 per month for continuous use <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Recommended Cloud Providers
*   **RunPod**: Offers competitive pricing and a variety of GPU options <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   **DigitalOcean**: While currently pricier with fewer options, it is expected to expand its offerings in the future <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## A Hybrid Strategy for LLM Deployment
A simple yet effective strategy involves starting with a pay-per-token model for self-hostable LLMs and later scaling to self-hosting those same models on cloud hardware when it becomes economically advantageous <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This approach avoids a large initial investment while allowing businesses to scale efficiently without switching LLMs, which can have "unintended consequences" for an application <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Starting with Per-Token Services (e.g., Groq)
Services like Groq enable users to pay per token for "super fast openly available LLM inference" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Groq is noted for its speed (e.g., 1,200 tokens per second) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> and affordability, often being free for light requirements due to an "indefinite free tier" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Groq's pricing for [[using_llama_for_llms | Llama 3.1 70B]] is $0.59 per million tokens, equating to approximately 1.69 million tokens per dollar <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This is considered extremely affordable compared to closed-source models like GPT-4o or Claude 3.5 Sonnet, and even other services offering [[using_llama_for_llms | Llama 3.1]] <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

Although Groq hosts the LLM, it's generally considered better for data privacy than sending data to closed-source models that might train on user data <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. For highly private data, using mock data is recommended during proof-of-concept development when using services like Groq, switching to private data once self-hosting <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Determining the Switch Point to Cloud Hosting
There is a "calculable time" when it becomes more cost-effective to switch from paying per token with services like Groq to hosting one's own LLM in the cloud <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This calculation depends on the average number of tokens per prompt, which can be tracked by the application's backend <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

For an example, using an A40 instance on RunPod costing $280 per month, and Groq's rate of 1.69 million tokens per dollar for [[using_llama_for_llms | Llama 3.1 70B]]:
*   **Cost of cloud instance (monthly)**: $280 <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>
*   **Tokens per dollar (Groq)**: 1,690,000 <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>
*   **Example average tokens per prompt**: 5,000 <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>

Using these figures, approximately 338 prompts can be made per dollar on Groq (1,690,000 tokens / 5,000 tokens/prompt) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
Multiplying this by the monthly cost of the RunPod instance ($280), it means Groq would cost more after approximately 94,640 prompts per month (338 prompts/$ * $280) <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
Dividing by 30 days, this means if an application makes about 3,155 prompts per day, it becomes more economical to self-host the LLM in the cloud <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. This threshold can be met quickly, for instance, if 3,000 users each make one prompt per day <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

> [!tip] Customizing the Calculation
> You can make this calculation very accurate to your specific use case by determining:
> *   The desired instance with RunPod (or other cloud provider) and its exact pricing <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
> *   The precise pricing for your chosen model in a per-token service like Groq <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
> *   The average number of tokens per prompt for your application <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

This strategic approach allows businesses to work with local LLMs effectively, avoiding significant upfront costs, and then scale to completely self-hosting in the cloud, potentially saving "thousands and thousands of dollars" once an application reaches thousands of users <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.