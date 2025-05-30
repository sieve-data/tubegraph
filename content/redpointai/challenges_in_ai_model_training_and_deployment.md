---
title: Challenges in AI model training and deployment
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

OpenAI's approach to AI model development, particularly with GPT-4.1, prioritizes real-world utility and developer experience over benchmark performance alone <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Michelle Pokris, Post-Training Research Lead at OpenAI, emphasized that the goal was to create a model that is a "joy to use for developers" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Focus on Real-World Usage over Benchmarks

Traditional model optimization for benchmarks can lead to models that perform well on paper but "stumble over basic things" in practice, such as not following instructions, having weird formatting, or insufficient context length <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. To address this, OpenAI focused on direct developer feedback <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, transforming it into actionable evaluations (evals) for research <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

A "long leadup" to model training was dedicated to "getting our house in order on evals" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. An internal instruction following eval, based on real API usage and user feedback, served as a "north star" during development <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Challenges in Evaluation Development
Identifying the most critical evals is challenging because users often don't provide a comprehensive list, but rather describe "weird" edge cases <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. A significant amount of work involves talking to users to extract key insights <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. For example, it was discovered that models needed to learn to ignore world knowledge and solely use in-context information for specific user needs, a requirement not captured by standard benchmarks <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

Decisions on which evals to pursue are based on recurring customer themes, internal model usage, and feedback from internal customers building on the models <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. OpenAI actively seeks more real-world, long-context evals, which are difficult to create <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, and better definitions for "instruction following," as it encompasses "hundreds of different things" for users <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

A surprising challenge emerged where one alpha user preferred an earlier version of GPT-4.1 over the final shipping version, despite all evals showing improvement. This highlighted how niche use cases might not be covered by standard metrics <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## The Model Shipping Process

Shipping a model like GPT-4.1 involves a large team <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The latest release included semi-new pre-trained models: a "mid-train" freshness update for the standard size, and new pre-trains for the mini and nano models <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

### Post-Training and Iteration
The post-training team focuses on determining the best mix of data, optimal parameters for Reinforcement Learning (RL) training, and appropriate weighting of different rewards <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
The development of GPT-4.1 involved:
1.  Identifying developer pain points with previous models <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
2.  Approximately three months focused on evaluation <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
3.  A "flurry of training" for the subsequent three months, involving running "tons of experiments" with different datasets and parameter tweaks <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
4.  Linking these experiments with new pre-trains <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
5.  About one month of rapid alpha testing, training, and incorporating feedback <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Challenges in Model Development and Evaluation Lifespan
A key challenge is the short "shelf life of an eval," which is about three months due to rapid progress and quick saturation of benchmarks <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This necessitates continuous hunting for new evaluation methods <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. While some benchmarks like SWEBench for code and Ader evals remain useful, many become saturated and lose their utility <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

## Rapid AI Progress and Adaptability

Staying current with the rapid pace of AI model releases (a new model seemingly drops every month) is a significant challenge for companies <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
Best practices for companies using these APIs include:
*   **Strong Evals**: The most successful startups "know their use case really well" and have robust evals, allowing them to quickly test new models <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   **Flexible Prompts and Scaffolding**: Customers who can easily switch and tune their prompts and scaffolding to particular models are highly successful <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
*   **Building for the Near Future**: Develop products that are "just out of reach" of current models <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. If a problem achieves a 10% pass rate with current models and can be fine-tuned to 50%, it's likely a future model will "crush it" in a few months, making such companies first to market <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

### Scaffolding and Future Trends
Companies often build extensive scaffolding around current model limitations to make products work today <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. While this arbitrage is worthwhile for shipping immediate value <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>, it's crucial to be prepared for changes as model capabilities improve, potentially obviating existing scaffolding <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. Key trends to monitor include:
*   **Improving Context Windows**: These will continue to get better <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.
*   **Enhanced Reasoning Capabilities**: Models will become better at complex reasoning <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
*   **Better Instruction Following**: This will consistently improve <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>.
*   **Natively Multimodal Models**: Models are becoming "so natively multimodal" and easy to use with different data types, meaning connecting models to as much information as possible, even with current mediocre results, will yield better outcomes in the future <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.

## Fine-Tuning and Model Capabilities
Fine-tuning has seen a "renaissance" <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. It's generally categorized into two camps:
1.  **Fine-tuning for speed and latency**: Using models like GPT-4.1 and then fine-tuning them (SFT) for faster, cheaper inference, making them a "workhorse" <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
2.  **Fine-tuning for frontier capabilities (RFT)**: With Reinforcement Learning from Feedback (RFT), users can "push the frontier" in specific niche areas with remarkable data efficiency (hundreds of samples) <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. RFT is particularly useful for teaching agents workflows or decision processes, and in deep tech where unique, verifiable data allows for "absolute best results" <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.

RFT is essentially the same RL process OpenAI uses internally for model improvement and is "less fragile" than SFT <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.
Mental model for fine-tuning:
*   **Stylistic changes**: Use Preference Fine-Tuning <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.
*   **Simple accuracy gaps**: Use SFT (e.g., closing a 10% error gap for classification with a model like Nano) <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
*   **No market model works**: Turn to RFT for problems where no existing model can meet the need <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
Verifiable domains such as chip design, biology, and drug discovery (where outcomes, even if long-term, are verifiable) are strong candidates for RFT <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.

## Overhyped vs. Underhyped Areas in AI
*   **Overhyped**: Benchmarks, especially agentic ones that are saturated or where reported "absolute best numbers" differ from realistic usage <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
*   **Underhyped**: Companies' own evals and using real usage data to understand what's working <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>.
Michelle's personal view on fine-tuning shifted from being a "bear" to recognizing RFT's value for pushing the frontier in specific domains <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. This change was influenced by the fact that RFT provides access to the same reinforcement learning algorithms used internally for model training, enabling users to achieve capabilities previously exclusive to OpenAI <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.

## Future of Model Development and OpenAI's Strategy
The "shelf life of an eval" being only about three months points to the continuing challenge of evaluating progress <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. New benchmarks, like successors to SWEBench, will be necessary as existing ones become saturated <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Generalization vs. Specialization
OpenAI's general philosophy leans towards the "G in AGI," aiming for "one model that's general" <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. The goal is to simplify product offerings and model selection (e.g., in ChatGPT) <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. However, for GPT-4.1, a decision was made to "decouple from ChatGPT" due to an "acutely need" from developers, allowing for faster training, feedback, and shipment on a different timeline <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This allowed specific choices like removing ChatGPT-specific datasets and significantly upweighting coding data <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

Despite this targeted approach, the expectation is generally to simplify in the future, as models improve when "creative energies of all researchers at OpenAI are working on them" <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. There is "room for both" targeted and general models, and OpenAI may pursue targeted releases again if demand exists <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. The trend of cross-domain generalization, where capabilities in one area benefit others, supports the generalist approach <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

Regarding specialized foundation models (e.g., robotics, biology), the current trend observed internally is that "combining everything just produces a much better result," supporting the idea of general models <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.

### Challenges in GPT-5 Development
The core challenge for GPT-5 is combining the distinct capabilities of different models <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>. For example, GPT-4 is excellent for chat, matching tone, and conversational flow, while GPT-3 excels at hard reasoning problems <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>. The task is to train a single model that can be a "delightful chitchat partner" but also know when to engage in deep reasoning, which involves "zero-sum decisions" on data weighting <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.

## Internal Process and Future Research
OpenAI is focused on improving its "speed of iteration" in research <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>. This involves running more experiments with fewer GPUs to quickly determine if a job is working <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. This is not purely an infrastructure problem; it also involves ML challenges to ensure training at sufficient scale for signal detection <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.

A major area of excitement is using models to make models better, particularly in reinforcement learning <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>. This leverages "synthetic data," which has been an "incredibly powerful trend" <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>. The more powerful models become, the easier it is to improve future models <a class="yt-timestamp" data-t="00:33:28">[00:33:28]</a>.

### Conclusion
The field of AI model training and deployment is characterized by rapid advancements and evolving challenges. From the constant need for fresh evals to the strategic balancing act between specialized and generalized models, the process requires deep understanding of both technical capabilities and user needs. The trend toward more data-efficient fine-tuning and the use of AI to improve AI itself suggests a future of continued innovation and capability expansion. Michelle Pokris estimates that even if model progress stopped today, there would still be "10 years of building at least" to extract value from existing capabilities <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>.