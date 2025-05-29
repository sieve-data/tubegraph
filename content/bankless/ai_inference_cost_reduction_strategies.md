---
title: AI inference cost reduction strategies
videoId: OC61Vo4tAaE
---

From: [[bankless]] <br/> 

The landscape of [[AI innovation and emerging technologies | AI]] is rapidly evolving, particularly concerning the efficiency and cost-effectiveness of [[AI efficiency improvements and market implications | AI]] inference. Recent breakthroughs and ongoing developments suggest a significant shift towards reducing the compute resources required for [[AI Model Differences and Enhancements | AI models]], potentially leading to substantial cost reductions in the industry <a class="yt-timestamp" data-t="06:35:10">[06:35:10]</a>.

## DeepSeek's Efficiency Breakthroughs

The Chinese [[Open Source AI Models | AI lab]] DeepSeek has garnered significant attention for its V3 [[AI Model Differences and Enhancements | AI model]], which reportedly offers substantial efficiency gains <a class="yt-timestamp" data-t="01:29:05">[01:29:05]</a>. This model is reported to be 45 times more cost-efficient than US-based [[AI Model Differences and Enhancements | AI models]] and charges 95% less for API calls compared to ChatGPT <a class="yt-timestamp" data-t="01:32:04">[01:32:04]</a>. This implies that the industry may have been "massively over-provisioning compute resources" <a class="yt-timestamp" data-t="06:36:04">[06:36:04]</a>.

Key innovations contributing to DeepSeek's efficiency include:
*   **Optimized Attention Mechanism:** DeepSeek engineers realized that "KV key value caches and indices" stored during training were wasteful <a class="yt-timestamp" data-t="05:21:05">[05:21:05]</a>. By storing only a "very small subset of that data" in a compressed representation, they significantly saved memory and reduced data transfer, leading to faster calculations <a class="yt-timestamp" data-t="05:57:04">[05:57:04]</a>.
*   **Multi-Token Predictions (Speculative Decoding):** Instead of predicting one token (word) at a time, DeepSeek attempts to predict two or three tokens simultaneously <a class="yt-timestamp" data-t="05:30:05">[05:30:05]</a>. Although speculative, they achieve a 95% accuracy rate in these guesses, effectively doubling throughput for inference at no additional cost <a class="yt-timestamp" data-t="05:56:05">[05:56:05]</a>. This directly lowers inference costs, allowing them to charge significantly less for their API <a class="yt-timestamp" data-t="05:57:04">[05:57:04]</a>.
*   **Quantized Training:** DeepSeek found a way to train their models using a "smaller representation" of parameters end-to-end, rather than training at higher precision and then quantizing (rounding off numbers) later <a class="yt-timestamp" data-t="05:56:05">[05:56:05]</a>. This preserves model quality while significantly improving efficiency by reducing memory usage and accelerating calculations <a class="yt-timestamp" data-t="05:56:05">[05:56:05]</a>.

These gains are multiplicative, not just additive, leading to dramatic overall improvements in efficiency <a class="yt-timestamp" data-t="05:56:05">[05:56:05]</a>.

## Impact of Chain of Thought Models on Inference

The emergence of Chain of Thought models, such as OpenAI's O1 model, has shifted the compute balance towards inference <a class="yt-timestamp" data-t="06:10:05">[06:10:05]</a>. While traditional models primarily required processing power for training, Chain of Thought models can "compute at the time you give them a request" to provide better answers <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This means that although inference previously required less compute, these models can now consume far more intermediate "logic tokens" (scratchpad for internal thinking) to produce superior results <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This phenomenon can increase overall compute demand for inference <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## Specialized Hardware for Inference

Dedicated hardware optimized specifically for inference is proving to be a highly effective strategy for cost reduction:
*   **Grock (with a 'Q'):** This company has developed technology exclusively focused on inference, not training <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Their specialized hardware can achieve inference speeds of 1,500 tokens per second for models like Llama 3.37 billion, compared to 40-50 tokens per second on a standard desktop GPU <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Despite the high upfront cost of their servers, if kept busy, they are much cheaper to use than general-purpose GPUs <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
*   **Cerebus:** This company produces "wafer-scale chips" that are essentially one enormous chip, reducing the need for complex interconnects between multiple smaller GPUs for training <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

## Custom Silicon by Hyperscalers

Major cloud providers and [[AI and Human Intelligence | AI]] labs are developing their own custom [[AI Model Differences and Enhancements | AI]] chips for both training and inference. Companies like Amazon (with their Trinium chips), Microsoft, OpenAI, and Meta are investing heavily in this area <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

The motivation behind this is clear: Nvidia charges very high margins for its GPUs (up to 90% gross margin on data center revenue) <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. If a hyperscaler can make its own chip for 1X the cost of manufacturing, it can still cut the price by 50% to its customers and make a huge margin, or pass on those savings <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This significantly reduces their operational costs for serving [[AI agents in finance | AI]] requests.

>[!Note] Impact of Custom Silicon
> "It doesn't necessarily have to be better than Nvidia's stuff... if you can make it yourself for you know 1X what it costs then you can cut the price by 50% to your end customers you'll still make a huge margin..." <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>

## Softening Nvidia's Software Moat (CUDA)

Nvidia's CUDA software platform has been a significant barrier to entry for competitors, as it simplifies the complex task of programming thousands of GPU cores <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. However, this moat is being challenged by:
*   **Higher-Level Frameworks:** New frameworks like MLX (by Apple) and Triton are gaining momentum <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. These allow developers to express parallelized programming at a very high level, and then compile the code to run on different chips, not just Nvidia's <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **LLM-Assisted Code Porting:** [[AI Model Differences and Enhancements | LLMs]] are "unbelievably good" at porting code from one language to another <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This means developers could write algorithms using CUDA concepts, and then use an [[AI Model Differences and Enhancements | LLM]] to port that code to frameworks compatible with [[Comparative analysis of AI models | AMD GPUs]] or other specialized hardware, bypassing Nvidia's expensive chips <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

## The Role of Synthetic Data

While not directly a cost reduction strategy for inference, synthetic data generation is crucial for [[AI efficiency improvements and market implications | AI]] model training and long-term improvement. As high-quality human-generated data becomes scarce, [[AI Model Differences and Enhancements | LLMs]] can be used to generate new data, especially for logic, math, and computer programs <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

The key is verifiability:
>[!Quote] Jeffrey Emanuel
> "The exception to all that is if you're talking about like logic math computer programs because in those things the big difference is that you can verify that what you said is correct." <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>

This allows for the continuous generation of high-quality, correct training data, enabling models to become "super human" at quantitative tasks at a much faster rate <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. This ensures the continued development of more capable and potentially more efficient models down the line.

## Market Implications

These advancements in [[AI efficiency improvements and market implications | AI efficiency]] are causing significant market re-evaluations. Nvidia experienced a 20% drop, wiping out $600 billion in market value, as the market reacted to the prospect of reduced demand for high-cost hardware <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. Companies like OpenAI and Anthropic are likely to face pressure to cut their API prices significantly due to competition from more cost-effective solutions like DeepSeek <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>.

However, the "Jevons Paradox" suggests that increased efficiency can lead to increased overall demand for a resource <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. While individual tasks become cheaper, the lowered cost might spur so much more usage that the total demand for compute resources still rises. Nevertheless, the immediate effect is a "step function change" in efficiency that disrupts the previously anticipated, linear growth of hardware demand <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This means that even if the overall [[AI in the Crypto Space | AI]] "pie" grows, the market share and margins for dominant hardware providers like Nvidia could still decline rapidly as competition and cost-saving innovations flood the market <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.