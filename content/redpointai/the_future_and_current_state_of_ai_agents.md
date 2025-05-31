---
title: The future and current state of AI agents
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

Michelle Pokris, a post-training research lead at OpenAI, played a crucial role in improving GPT-4.1 for developers, focusing on real-world usage over benchmarks <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Her work has significantly impacted the [[current_state_and_future_of_ai_agent_frameworks | current and future state of AI agents]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Current State of AI Agents

[[effectiveness_of_ai_agents_in_specific_tasks | AI agents]] currently work remarkably well in well-scoped domains where the model has the necessary tools and the user's request is clear <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. Common successful use cases include scenarios where tools are available and user intent is explicit <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

However, the main challenge lies in bridging the gap to the "fuzzy and messy real world" <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This includes situations where users may not know what the agent can do, the agent lacks awareness of its own capabilities, or it's not sufficiently connected to real-world information <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. Michelle Pokris believes that much of the core capabilities for agents are already present, but the difficulty lies in providing sufficient context to the model <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

A key area for improvement is handling ambiguity, allowing developers to tune whether the model should ask for more information or make assumptions when faced with unclear requests <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Benchmarks for function calling and agentic tool use often show models being "misgraded" or encountering ambiguous cases, suggesting that the underlying models are often doing the right thing but are limited by context or instruction adherence from user models <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Future Developments for AI Agents

To advance agents, improvements are needed on both the engineering and model sides <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

### Engineering Side
*   **APIs and UIs**: Easier interfaces are required to monitor agent actions, view summaries of their activities, and intervene to change their trajectory <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. An example of this steerability exists in OpenAI's "Operator" product <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Model Side
*   **Robustness and "Grit"**: Models need to be trained for greater resilience when things go wrong, such as API errors, preventing them from getting "stuck" <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Longer-term Task Execution**: While underlying model capabilities are strong, the full potential isn't realized due to insufficient connection of context or tools <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. [[future_of_ai_agents_in_software_development | Coding agents]] are expected to emerge soon, given that models like GPT-4.1 already exceed many human benchmarks in areas like SWEBench <a class="yt-timestamp" data-t="00:35:22">[00:35:22]</a>.
*   **Generalization**: The ability to supervise long runs in code is a key capability <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>. Models like GPT-4.1 can already integrate developer-specified tools into their chain of thought, allowing them to use previous tool calls and outputs for continued reasoning <a class="yt-timestamp" data-t="00:35:44">[00:35:44]</a>. This means that agentic capabilities, like for customer support, are largely "there" and just need to be integrated into cohesive products <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>.

### Role of Fine-Tuning
Fine-tuning, particularly Reinforcement Learning from Human Feedback (RFT), is seen as a powerful way to push the frontier in specific domains <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. RFT is data-efficient, requiring only hundreds of samples <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.

Examples of effective RFT applications include:
*   Teaching an agent to select a workflow <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
*   Guiding an agent's decision-making process <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>.
*   [[future_potential_of_autonomous_ai_agents_in_various_fields | Deep tech applications]] in fields like chip design or biology (e.g., drug discovery) where verifiable data allows for absolute best results <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.

Michelle Pokris suggests that if a model's current pass rate is low (e.g., 10%) but can be significantly improved with fine-tuning (e.g., to 50%), it indicates a capability "right on the cusp" that a future model will likely master <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

### Generalization vs. Specificity
While OpenAI's immediate goal for GPT-4.1 was a targeted model for developers, the long-term philosophy leans towards the "G" in [[future_of_artificial_general_intelligence_agi | AGI]], striving for a single, general model that can handle various tasks <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. The belief is that combining efforts on one general model yields better results <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

However, there's still room for targeted approaches when an acute need arises, as was the case with GPT-4.1 being decoupled from ChatGPT to accelerate development and make specific training choices like upweighting coding data <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. Michelle Pokris acknowledges that more targeted models might be pursued again depending on demand <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

Regarding specialized foundation models (e.g., [[the_future_of_ai_in_robotics_and_its_impact | robotics]] or biology), there's a strong belief that generalization improves capabilities, and combining everything produces a much better overall result <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.

### Role of Developers and Companies
Companies are advised to stay on top of rapid AI progress by developing strong internal evaluations (evals) for their specific use cases <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. This enables them to quickly assess new models and adapt their prompts and scaffoldings <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. Michelle Pokris suggests building features that are "just out of reach" of current models, as new model releases can quickly enable them <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

While scaffolding to make products work today is valuable (offering "arbitrage" for a few months), companies should be prepared to change things as core capabilities like context windows, reasoning, and instruction following continue to improve <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. [[developers_approach_to_ai_models_and_agents | Multimodal]] capabilities are also rapidly improving, making it worthwhile to connect models to as much information as possible, even if initial results are modest <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.

For app layer companies, strong AI expertise may not be as crucial as understanding the product and being "scrappy engineers" who can combine models and solutions <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>. The most successful [[developers_approach_to_ai_models_and_agents | developers]] and startups are those who deeply understand their problem, have comprehensive evaluations for subcomponents, and design modular systems <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.

## Personalization and AGI

The trend of enhanced memory in models means that future ChatGPT experiences will be highly personalized, adapting to individual users and their preferences <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. Increased steerability through features like custom instructions will also allow users to fine-tune the model's "personality" <a class="yt-timestamp" data-t="00:39:25">[00:39:25]</a>.

The ultimate goal of combining different model families (like 4.0's conversational strengths and 03's reasoning capabilities) into a single model, such as GPT-5, is a significant research challenge. The difficulty lies in striking the right balance to be a delightful conversationalist while also knowing when to engage in deep reasoning <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>.

Michelle Pokris believes that even if model progress stopped today, there would still be at least 10 years of value to build from existing capabilities <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>.