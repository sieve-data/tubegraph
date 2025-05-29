---
title: Comparative analysis of AI models
videoId: 3ezFd3x718A
---

From: [[bankless]] <br/> 

A new, previously unknown [[open_source_ai_models | AI model]] named Deep Seek, developed by a team in China, has recently gained significant attention in the AI space, challenging established leaders like OpenAI and Anthropics Claude <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This [[emerging_ai_tools_and_projects | emerging AI tool]] is notable for its extremely low development cost compared to OpenAI's models <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, and its ability to match or even surpass OpenAI's top models in performance benchmarks <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Deep Seek's Breakthroughs

Deep Seek R1 is described as a very legitimate model that passes benchmarks and performance tests competitively with OpenAI <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Its low training cost, reportedly $6 million, is viewed with skepticism by some, with claims suggesting it may have used ChatGPT to train its model <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Despite this, Deep Seek has introduced two significant engineering breakthroughs that have altered how large language models (LLMs) operate:

1.  **Efficient Data Usage and Improved Reasoning** <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>:
    *   Traditionally, training LLMs required massive compute power alongside data <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Deep Seek's team, facing compute constraints due to chip bans <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, developed a smarter training method <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   This method involves feeding the model a small amount of compute and data, allowing it to produce an output, then reviewing that output to understand errors or improve accuracy, and finally rerunning compute more intelligently <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   This approach helps the model take fewer steps and use less compute and data to achieve desired results <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. It addresses the common LLM issue of "hallucinations" or incoherent long answers by breaking down the process into chunks, reviewing each chunk for fit, and ensuring coherence before generating a final answer <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

2.  **Mixture of Experts (MoE) Architecture** <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>:
    *   Unlike traditional models like OpenAI's GPT, where querying the model stimulates its entire "brain" (all neurons) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>, Deep Seek's model selectively routes requests <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
    *   When queried, it identifies and activates only the specific "experts" (sections of the model's brain) relevant to the request, while others remain inactive <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    *   This method produces about 97% of the output quality while saving 97% of the energy required <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Performance and Cost Comparison

Based on data from Artificial Analysis.ai, Deep Seek R1 demonstrates remarkable performance and cost efficiency:
*   **Overall Quality:** Deep Seek R1 is just one point below OpenAI's leading model (01) in overall quality <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Speed:** It is comparable in speed to OpenAI's 01 model, despite being slower than some other models <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **Price:** Deep Seek's API calls are around six times cheaper than OpenAI's <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>, charging 95% less than OpenAI <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

These efficiency gains make Deep Seek R1 approximately 45 times more efficient than its US-based competitors in terms of compute resources to achieve the same response quality in a similar timeframe <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

## Market Impact and Jevons Paradox

The emergence of efficient models like Deep Seek has led to a realization that software innovation can significantly reduce reliance on brute-force hardware, impacting valuations of companies like Nvidia <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This highlights a dynamic akin to the "scaling" in software and hardware development, where better software can extract more performance from existing hardware <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

However, this increased efficiency also brings Jevons Paradox into play <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>:
> "As technological advancements improve the efficiency of a resource, its overall consumption can paradoxically increase rather than decrease. This occurs because increased efficiency lowers cost and expands potential use cases, driving greater demand." <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>

Therefore, as compute becomes cheaper and AI models become more efficient, AI adoption is expected to spread faster, expanding demand for GPUs, energy, and data infrastructure globally, rather than reducing overall compute consumption <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. This means that while models are cheaper to create, the increased accessibility leads to more models and applications, consuming the same compute surplus <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

## Open Source vs. Closed Source in the AI Arms Race

Deep Seek's [[open_source_ai_models | open-sourcing]] of its model is a significant move, described as akin to "telling everyone what the recipe is" for a groundbreaking invention <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This contrasts with companies like OpenAI, which maintain closed-source models that cost significantly more <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

The dynamic between the United States and China is framed as an "arms race" in AI <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>. China's strategy to open-source its technology is seen as an attempt to slow down investment in US-based AI companies by commoditizing the value created in the US <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. While the US has been a leader, Deep Seek's emergence brings this into question, serving as a "wakeup call" for American AI companies to assess their strategies <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>.

Ultimately, the natural convergence of AI innovation towards [[open_source_ai_models | open source]] is considered bullish for the crypto AI agent sector, as it allows for the integration of cutting-edge technology into open blockchain environments, translating value into tokens <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.

## Developments in AI Agents

The week following Deep Seek's announcement also saw significant developments in AI agents:
*   **OpenAI and Perplexity Agent Products:** Both OpenAI and Perplexity teased their agent products <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>. OpenAI's demo showed an agent performing tasks like shopping and ordering pizza, and notably, using "computer use" rather than just APIs <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>. Perplexity's demo showcased similar capabilities <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. While OpenAI's agents remain closed source, their demonstrations validate the direction of [[emerging_ai_tools_and_projects | crypto AI agent]] development <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.
*   **Crypto AI Adoption:** Crypto AI protocols are rapidly integrating new advancements. Many teams and protocols were able to integrate Deep Seek into their frameworks within minutes, making it accessible to a vast number of agents built on crypto rails <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>. This showcases crypto's resilience and ability to adapt and adopt beneficial innovations for its own ecosystem <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a>.

## Specific Crypto AI Projects

*   **Virtuals:** One of the largest agent protocols in the crypto AI sector, Virtuals, announced its expansion to Solana <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Previously operating on Base, this move allows Virtuals to leverage Solana's high activity and "hot ball of money" <a class="yt-timestamp" data-t="00:44:37">[00:44:37]</a>. While its native token remains on Base, Virtuals aims to transport liquidity to Solana and enable new agents to issue Solana-native tokens <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>. Virtuals is also focusing on:
    *   Better agent interoperability for agents to communicate and work together <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.
    *   Sharing agent revenue with token holders and the community <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>.
    *   Physical integration with the real world, such as agents running pop-up shops <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>.
*   **AI xbt:** This project, which offers financial alpha through its agent terminal, launched a new tiered system to make its product more accessible to a wider range of token holders <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>. AI xbt plans to expand to different mediums (voice, video) and social media platforms, as well as explore a B2B approach for protocols seeking tokenomics advice <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a>.
*   **Venice:** Eric Vorhees' project, Venice, launched its VVV token and received a rapid listing on Coinbase <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>. Venice is a private, no-KYC alternative to ChatGPT that offers access to any connected model, preferably [[open_source_ai_models | open-source]] and locally run ones <a class="yt-timestamp" data-t="00:58:05">[00:58:05]</a>. Its privacy is maintained by cryptographically privatizing requests and responses at the node level <a class="yt-timestamp" data-t="00:58:34">[00:58:34]</a>. Venice quickly integrated Deep Seek upon its release, providing access to its advanced model <a class="yt-timestamp" data-t="00:59:14">[00:59:14]</a>.
*   **Griffin:** This agent execution platform, which previously focused on on-chain activities, added off-chain Web2 integrations, including Shopify <a class="yt-timestamp" data-t="01:03:35">[01:03:35]</a>. This allows agents to perform real-world tasks like ordering coffee, bridging the gap between Web2 products and Web3 innovations <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>.
*   **Arc:** An AI agent platform built in Rust, Arc announced a partnership with the Solana Foundation to accelerate AI innovation on Solana <a class="yt-timestamp" data-t="01:05:23">[01:05:23]</a>. This formal partnership marks a significant collaboration between a blockchain foundation and an AI protocol in the crypto AI space <a class="yt-timestamp" data-t="01:06:16">[01:06:16]</a>.
*   **AI 16z (now rebranded):** This project, which started as a parody, announced a $10 million fund in conjunction with Jupiter exchange (a Solana DEX aggregator) <a class="yt-timestamp" data-t="01:08:05">[01:08:05]</a>. This fund aims to support and build teams within the crypto AI space <a class="yt-timestamp" data-t="01:08:16">[01:08:16]</a>.

## Conclusion

The emergence of highly efficient and [[open_source_ai_models | open-source AI models]] like Deep Seek marks a pivotal moment in the AI landscape, intensifying the global competition in [[innovative_trends_in_ai_and_machine_learning_models | AI and machine learning models]] <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. These advancements, while creating market shifts, ultimately lead to more accessible and powerful AI tools. The rapid integration of these innovations by crypto AI projects demonstrates the sector's adaptability and its potential to drive the next wave of AI agent development, focusing on "unsexy" middleware agents that underpin the fundamental usage and infrastructure <a class="yt-timestamp" data-t="01:08:56">[01:08:56]</a>.