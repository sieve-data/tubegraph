---
title: AI infrastructure and tooling
videoId: P6y0gr-W2-k
---

From: [[redpointai]] <br/> 

*Unsupervised Learning*, a podcast by Redpoint Ventures, conducted a crossover episode with *Latace* (Laten Space), a technical newsletter and podcast for AI engineers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. *Laten Space* had over 2 million downloads in 2024 and is a go-to resource for understanding the cutting edge of [[AI infrastructure and startup opportunities | AI infrastructure]], tooling, and product <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This special episode features a discussion on what surprised them, what they are paying attention to, defensibility at the app layer, and public company outlooks <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Surprises in AI

### Model Evolution and Open Source
One significant surprise in the past year was the rapid advancement of models <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The release of new models right after Ilia's "scaling is dead" talk created a sense of "so back" in a short period <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This timing, where pre-training seemed to be "dying" and inference time became the "new scaling law," was noted as "suspiciously neat" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

A negative surprise was the relevance and adoption of open-source models in enterprises <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. While the local Llama community and hobbyists appreciate them, enterprise adoption of open-source models was estimated at only about 5% and decreasing <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Enterprises are primarily in "use case discovery mode," opting for what they perceive as the most powerful models <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

Conversely, another surprise was how quickly open source caught up on reasoning models, particularly DeepSeek <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This speed indicated that the time period for a closed-source model to have a compounding advantage is much shorter than anticipated <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. However, it was clarified that this was specific to DeepSeek's rapid catch-up, and there isn't a "team open source," but rather individual companies choosing to open source <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The ability to replicate what's already been done is cheaper than creating something fundamentally new <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. DeepSeek was considered overhyped because it primarily executed well on existing concepts rather than introducing fundamental innovations <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. DeepSeek's main unique contribution was providing full traces for open source models <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Application Layer Developments
Another surprise was that low-code builders did not capture the AI builder market <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Companies like Zapier, AirTable, Retool, and Notion, despite having the DNA and distribution, largely missed this shift <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. They focused on improving their existing baselines with AI features, rather than building from scratch with new AI paradigms <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. This led to the rise of "GPT rappers" — companies that build directly on top of powerful models <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The consensus shifted from making fun of "GPT rappers" to recognizing them as the most interesting development <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Overhyped vs. Underhyped

### Overhyped
*   **Agents Frameworks**: These are seen as overhyped, likened to the "jQuery era" rather than the "React" era of development <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. The underlying workloads are too fluid for stable frameworks <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Instead of frameworks, the focus should be on protocols, like MCP, which enabled Ajax <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **New Model Training Companies**: There is surprise at the continued emergence of new companies training models, despite the competitive landscape <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. Many pursue AGI, but it's unclear what unique gap they fill <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. Historically, general-purpose models tend to outperform hyper-specific ones in quality <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### Underhyped
*   **Memory (Stateful AI)**: Memory, beyond conversational memory, such as storing knowledge graphs that exceed context length, is significantly underhyped <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. A better memory abstraction could lead to smarter agents that learn on the job <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. This is an interesting space for VCs due to its resemblance to databases <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   **Private Cloud Compute (PCC)**: Apple's Private Cloud Compute (PCC) is under the radar but has potential <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. It brings on-device security to the cloud, which is crucial as large enterprises need multi-tenant architectures to access enough GPUs while maintaining single-tenant guarantees <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Application Areas**:
    *   **Customer Support**: Companies like Sierra are demonstrating significant product-market fit by tackling customer support, a major cost center for many businesses <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.
    *   **Voice AI**: In areas like scheduling and intake for home services, where businesses currently miss 50% of calls, an AI that is 75% effective can still drive significant revenue increase <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This highlights that 100% accuracy isn't always needed for high value <a class="yt-timestamp" data-t="00:33:19">[00:33:19]</a>.

## Product Market Fit in AI

Current categories with strong product market fit include:
*   **Coding Agents** (e.g., Cursor) <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>
*   **Customer Support Agents** (e.g., Sierra, Dekugan) <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>
*   **Deep Research/Search** (e.g., Perplexity, OpenAI's deep research) <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>
*   **Summarization of Voice and Conversation** (e.g., Granola, Monterey, Bridge) <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>

Emerging areas showing promise include:
*   Screen sharing assistance <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>
*   Outbound sales <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>
*   Hiring/recruiting <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>
*   Personalized teaching/education (e.g., Duolingo, Kamigo) <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>
*   Finance-specific applications <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>
*   Personal AI <a class="yt-timestamp" data-t="00:36:35">[00:36:35]</a>

The shift from AI being primarily about "cost cutting" to focusing more on "growth revenue" is noted <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. Initial AI apps focused on tasks easily outsourced (cost centers), but the next wave of apps may be more defensible by directly increasing top-line revenue <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.

## Defensibility at the App Layer
Defensibility at the application layer primarily comes from:
*   **Network Effects**: Prioritizing multiplayer experiences over single-player ones <a class="yt-timestamp" data-t="00:39:16">[00:39:16]</a>. Chai Research, a Character.AI competitor, is cited as an example, thriving due to its network of people submitting models, creating robustness against future changes <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.
*   **Brand**: Companies can quickly become synonymous with an entire category, gaining preferential access to customers <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>.
*   **Velocity and User Experience**: The ability to quickly build a broad product and adapt to new models (every 3-6 months) is critical <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>. This involves "a thousand small things" in user experience and design that compound over time <a class="yt-timestamp" data-t="00:42:06">[00:42:06]</a>. This approach is more analogous to traditional application SaaS defensibility, contrasting with the early "head fake" of relying on unique datasets or training custom models for defensibility <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a>.

## [[AI infrastructure and startup opportunities | AI Infrastructure]] Categories

The "LLM OS" concept encompasses several interesting [[AI infrastructure and startup opportunities | AI infrastructure]] categories:
*   **Code Execution**: A key area of focus for investment <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.
*   **Memory**: As discussed, stateful AI is underhyped <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>.
*   **Search**: Critical for augmented generation <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>.
*   **Security**: AI is needed on the defense side wherever it's used offensively (e.g., email security, identity) <a class="yt-timestamp" data-t="00:43:44">[00:43:44]</a>. This includes rethinking red teaming and leveraging models for semantic understanding in areas like binary inspection <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

The value in [[AI infrastructure and startup opportunities | AI infrastructure]] is more in the "infra around the model" rather than bare metal or capital-intensive model serving (like GPU clouds), which are considered less appealing for venture investment <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.

OpenAI and other large labs are increasingly encompassing parts of the developer and [[AI infrastructure and startup opportunities | AI infrastructure]] categories. For instance, search, once a distinct API (e.g., Perplexity), is now offered as an OpenAI API <a class="yt-timestamp" data-t="00:45:21">[00:45:21]</a>. This raises the question of whether model labs aim to be API companies or product companies <a class="yt-timestamp" data-t="00:46:18">[00:46:18]</a>. The application layer is currently seen as significantly more interesting than the [[AI infrastructure and startup opportunities | AI infrastructure]] layer, as it allows charging for utility rather than just cost-plus <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.

Specific areas struggling to gain significant traction as standalone businesses include:
*   **Finetuning Companies**: Unless wrapped into a broader enterprise AI services offering, finetuning alone is not seen as a large standalone opportunity <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>.
*   **AI DevOps/ASR (Autonomous System Response)**: While there's a lot of data, and the potential for self-healing apps exists, the technology isn't fully there yet for it to be a significant autonomous SRE solution <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>. It's largely still an anomaly detection problem, not a transformer LLM use case <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>.
*   **Voice Real-time Infrastructure**: While interesting, its ultimate market size is questioned <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>.

## Unanswered Questions and Future Implications

A significant unanswered question is the applicability of **Reinforcement Learning (RL)** to non-verifiable domains <a class="yt-timestamp" data-t="00:50:17">[00:50:17]</a>. While RL works in verifiable domains (like coding or mathematics), its success in areas like law (contracts), marketing, and sales is unclear <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>. If RL doesn't succeed in these areas, it could lead to a future where autonomous agents excel in verifiable tasks, but non-verifiable tasks still require human "taste makers" <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

Another critical question revolves around **hardware scaling and GPU dominance** <a class="yt-timestamp" data-t="00:51:48">[00:51:48]</a>. OpenAI's "rule of nines" suggests an order of magnitude increase in compute for each 9 (e.g., 90% to 99% reliability), occurring every 2-3 years <a class="yt-timestamp" data-t="00:51:35">[00:51:35]</a>. The availability of GPUs and the dominance of Nvidia (and its CUDA ecosystem) are major concerns <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. While AWS (Trainium), AMD, Microsoft, and Facebook are developing their own chips, the general-purpose nature of GPUs and the stability of the transformer architecture make them hard to displace <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>.

Finally, **Agent Authentication** is an emerging question <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>. When an agent accesses a website on a user's behalf, how does it indicate it's an agent, not the user? A new "SSO for agents" (Single Sign-On) is needed <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>. This raises questions about methods like scanning eyeballs, as proposed by Sam Altman <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>.