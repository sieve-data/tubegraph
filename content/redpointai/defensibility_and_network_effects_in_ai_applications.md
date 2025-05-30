---
title: Defensibility and network effects in AI applications
videoId: P6y0gr-W2-k
---

From: [[redpointai]] <br/> 

The concept of defensibility in AI applications, particularly at the application layer, is a recurring theme among industry experts. While early discussions focused on proprietary models or unique datasets, the conversation has evolved to emphasize different aspects such as user experience, product velocity, and most importantly, network effects <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Shifting Focus from Models to Applications

Initially, the value of model companies was perceived to stem from their ability to be the sole provider of a model for a period, allowing them to build products on top of it. However, this period of exclusive advantage has proven to be much shorter than anticipated <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The focus has largely shifted to what engineers can achieve *above* the model layer to augment its capabilities <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. The overwhelming consensus is that application development, sometimes colloquially referred to as "GPT wrappers," is now the most interesting area <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Product-Market Fit First
A key principle is to prioritize building something users desire before worrying about [[strategic_considerations_for_ai_application_developers | differentiation]] <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This contrasts with earlier assumptions that inherent advantages like Apple's position would guarantee success in consumer AI, which was not the case <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Sources of Defensibility

### Network Effects
Network effects are considered paramount for long-term defensibility <a class="yt-timestamp" data-t="00:39:16">[00:39:16]</a>. Companies often prioritize the single-player experience, neglecting the multiplayer aspects that can foster strong network effects <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>.

A prime example is Chai Research, a character AI competitor that, despite not having its own proprietary models, has outlasted competitors by building a network of users submitting models <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. This approach turns the company into a marketplace, leveraging the "choke point" at the protocol layer between users and model providers <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a>.

### Brand and Velocity
Rapid brand recognition and product velocity are crucial <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>. Companies that quickly become synonymous with an entire category gain significant advantage in customer access <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>. This allows them to command higher Average Contract Values (ACVs), even doubling them, due to the premium associated with being a leading brand <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>.

The ability to move quickly, develop a broad product, and adapt to new model releases every few months is an "existential event" for companies <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>. This emphasis on execution, user experience, and speed is reminiscent of successful traditional SaaS companies, relying on a multitude of small, compounding advantages rather than a single revolutionary feature <a class="yt-timestamp" data-t="00:42:30">[00:42:30]</a>.

### Unique Data and Stateful AI
While general-purpose models tend to dominate, specific use cases leveraging unique datasets can offer defensibility <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. Examples include robotics, biology, and material science, where proprietary data or processes (like wet labs) are essential <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

Furthermore, "stateful AI" or memory in AI applications, akin to databases, is seen as a potentially interesting area for investment and defensibility <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

## Implications for Investment

*   **Application Layer over Infrastructure (sometimes)**: The application layer is generally considered more interesting than bare-metal infrastructure, as it allows companies to charge for utility rather than just cost, avoiding the "cost plus" pricing model often seen in infrastructure <a class="yt-timestamp" data-t="00:47:14">[00:47:14]</a>.
*   **Targeting Cost Centers**: Early AI applications often found success in areas where businesses were already comfortable outsourcing to BPOs (Business Process Outsourcing) due to cost-cutting objectives <a class="yt-timestamp" data-t="00:32:28">[00:32:28]</a>. These areas, like customer support, implicitly signal a willingness to accept some performance cuts for cost savings <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>.
*   **Focus on Revenue Growth**: The next wave of AI applications is expected to focus more on revenue growth rather than just cost cutting <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>. Applications that demonstrably increase top-line revenue, such as those in AI go-to-market, will likely prove even more defensible, as businesses are willing to pay more for clear ROI <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>.
*   **Tolerance for Imperfection**: In certain applications, such as voice AI for scheduling or intake, 100% precision is not required for a great product <a class="yt-timestamp" data-t="00:33:19">[00:33:19]</a>. Even with 75% effectiveness, significant value and increased revenue can be generated, as many existing processes have much lower success rates <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This allows for viable products even as [[understanding_predictability_and_effectiveness_of_ai | model reliability]] continues to improve <a class="yt-timestamp" data-t="00:33:46">[00:33:46]</a>.

## Overhyped and Underhyped Areas

*   **Overhyped**: Agents frameworks are seen as overhyped, with the market still seeking stability rather than a proliferation of frameworks <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. The focus should be on establishing protocols rather than embedding them within frameworks <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Underhyped**: Stateful AI/memory and Private Cloud Compute (PCC) are considered underhyped. PCC, especially for handling larger LLMs while maintaining privacy and on-device security, is seen as having significant potential due to the need for multi-tenant architectures with single-tenant guarantees in GPU-constrained environments <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Unanswered Questions

A major unanswered question is the extent to which Reinforcement Learning (RL) can be successfully applied to non-verifiable domains, such as legal contracts or outbound sales <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a>. If RL remains limited to verifiable domains, it could lead to a future where fully autonomous AI excels in areas like coding and math, while human involvement remains necessary for tasks like writing sales emails <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.

Another key question revolves around the scalability of AI, specifically concerning hardware and [[cost_efficiency_and_accessibility_in_ai_technologies | availability of GPUs]]. The "rule of nines" suggests that achieving higher reliability (e.g., from 90% to 99%) requires an order of magnitude increase in compute every 2-3 years, raising concerns about continued reliance on a few dominant hardware providers like Nvidia <a class="yt-timestamp" data-t="00:51:34">[00:51:34]</a>.

Finally, the emerging need for "agent authentication" – a new form of SSO for agents – remains an open question, as current systems are not designed to differentiate between human and AI actions on websites <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>.