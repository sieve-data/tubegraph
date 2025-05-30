---
title: State and future of AI agents
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

AI agents are artificial intelligence systems designed to perform tasks autonomously, often by interacting with tools and environments. Their capabilities have seen significant advancements, particularly with newer models like GPT-4.1. <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>

## Current State

[[effectiveness_of_ai_agents | Agents]] currently demonstrate remarkable effectiveness in well-scoped domains <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>, especially when they have access to the necessary tools and a clear understanding of the user's request <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This means that in environments where all the right tools are available and the user's intent is unambiguous, AI agents perform very well <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Challenges and Areas for Improvement

Despite their progress, several [[challenges_and_opportunities_in_aiagent_development | challenges remain]] in deploying AI agents effectively in the real world:

*   **Bridging to the Fuzzy Real World** <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>: A significant hurdle is connecting agents to the messy, ambiguous nature of real-world interactions <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. Users often don't know an agent's capabilities, and agents might lack awareness of their own limitations or crucial real-world information <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **Context Integration** <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>: It is difficult to feed all necessary context into the model <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Ambiguity Handling** <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>: Models need improved steerability regarding ambiguity. Developers should be able to tune whether a model asks for more information or proceeds with assumptions when faced with unclear instructions <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. An agent that constantly asks for confirmation can be annoying <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Tool and Context Connection** <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>: The full potential of current models is often not realized because they are not connected with enough context or tools <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. When examining failure cases in external benchmarks for function calling or agentic tool use, issues often stem from misgrading, ambiguity, or the user model not following instructions well enough <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Longer-Term Task Execution** <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>: Addressing multi-step, ambiguous tasks requires both engineering and model-side changes <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>:
    *   **Engineering Side** <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>: APIs and UIs must make it easier to monitor an agent's actions, provide summaries of its progress, and allow users to intervene and change its trajectory <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. OpenAI's "operator" feature is an example of this steerability <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    *   **Modeling Side** <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>: Models need increased robustness and "grit" to handle errors, such as API failures, without getting stuck <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

## Role of Model Advancements

Recent model releases, like GPT-4.1, have significantly impacted agent capabilities by improving instruction following and long context processing <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. The hypothesis behind cheaper, faster models like "nano" was to spur more [[enterprise_adoption_of_ai_agents | AI adoption]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>, and this has proven successful, demonstrating demand across various cost and latency points <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

For companies, staying ahead of rapid model progress requires:
*   **Robust Evals** <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>: The most successful startups have deep knowledge of their use case and strong evaluation metrics. This enables them to quickly test new models and adapt <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.
*   **Adaptable Prompting** <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>: Being able to switch and tune prompts and scaffolding for different models is crucial <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Building for the Near Future** <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>: Focus on use cases that are "just out of reach" of current models (e.g., those that work one out of ten times but could be improved to nine) <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. If a problem shows significant improvement with fine-tuning (e.g., 10% to 50% pass rate), a future model will likely solve it completely <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

### Reinforcement Learning from Human Feedback (RFT)

A significant development is the [[advancements_and_implications_of_ai_agents | RFT fine-tuning]] offering, which is data-efficient (requiring only hundreds of samples) and can push the frontier in specific domains <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. It is particularly effective for:
*   Teaching an agent to pick a workflow or work through a decision process <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
*   Applications in deep tech where organizations have verifiable data not available elsewhere, such as chip design or certain aspects of biology (e.g., drug discovery where outcomes are verifiable) <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.
*   Problems where no existing model in the market does what is needed <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

RFT uses a similar reinforcement learning process to what OpenAI uses internally for improving its models, making it robust and less fragile than supervised fine-tuning (SFT) <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.

## Future Outlook

The [[future_of_ai_agents_in_productivity_tools | future of AI agents]] is expected to see continued progress, with several key trends:

*   **Generalization vs. Specialization** <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>: OpenAI's general philosophy leans towards making one "general" model (the "G" in [[the_current_and_future_trajectory_of_agi_development | AGI]]) that can handle diverse use cases <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. While targeted models like GPT-4.1 for developers showed success by decoupling from ChatGPT to move faster and optimize for specific needs (e.g., upweighting coding data) <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>, the expectation is to simplify the product offering to one general model <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Combining capabilities across domains generally leads to better results <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.
*   **Increased Multimodality** <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>: Models are becoming natively multimodal and easier to use <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. Significant improvements in this area mean that many tasks that failed in previous models now work <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. It's advisable to connect models to as much task information as possible, even if results are "meh" today, as they will improve <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
*   **Enhanced Memory and Personality** <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>: Future models, especially in the context of [[the_future_of_ai_in_human_communication | human communication]], will increasingly leverage enhanced memory to adapt to user preferences and personalities <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>. Steerability features, like custom instructions, will allow users to tweak model personality <a class="yt-timestamp" data-t="00:39:25">[00:39:25]</a>.
*   **Leveraging AI to Improve AI** <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>: A key research area involves using models to improve other models, particularly in reinforcement learning, by using signals to determine if a model is on the right track <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>. Synthetic data has been an incredibly powerful trend in this regard <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.
*   **Specific Agentic Capabilities** <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>:
    *   **Coding Agents** <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>: Given that current models are already exceeding human performance on some coding benchmarks like SWEBench, coding agents are expected to arrive soon <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>. The ability to supervise long runs of code generation is already present <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.
    *   **Long Workflows (e.g., Customer Support)** <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>: Models like O3 already integrate developer-specified tool calls into their chain of thought, allowing them to use previous tool outputs to reason further <a class="yt-timestamp" data-t="00:35:44">[00:35:44]</a>. This capability makes agentic customer support and other long workflows feasible <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.
*   **Unlocking Existing Value** <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>: Even if model progress stopped now, there are potentially decades of building and value extraction possible from current capabilities, similar to how the internet continues to drive value <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>. Billion-dollar companies are still being built using models like 3.5 Turbo <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.

## OpenAI's Approach

OpenAI's "Power Users Research Team" focuses on understanding and improving models for discerning users, including developers <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>. This focus is strategic because what power users do today will become commonplace for median users a year from now <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

The challenge for future models like GPT-5 is combining diverse capabilities—such as being a delightful conversationalist (like GPT-4) and a rigorous problem-solver (like O3)—without sacrificing performance in either area <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. This involves striking the right balance when tailoring the model's training data, as optimizing for one aspect (e.g., coding) might entail downweighting others (e.g., chat data) <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.