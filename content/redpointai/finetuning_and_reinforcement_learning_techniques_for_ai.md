---
title: Finetuning and reinforcement learning techniques for AI
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

Michelle Pokris, the post-training research lead for GBT 4.1 at OpenAI, played a crucial role in enhancing these models for [[developers_approach_to_ai_models_and_agents | developers]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Her work has focused on making models more practical for real-world usage and utility, moving beyond mere benchmark optimization <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Focus on Real-World Utility

The primary goal for GBT 4.1 was to create a model that is "a joy to use for [[developers_approach_to_ai_models_and_agents | developers]]" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Unlike models optimized solely for benchmarks, which may falter on basic tasks like following instructions or formatting, GBT 4.1 prioritized practical application <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

To achieve this, OpenAI focused on:
*   Gathering [[customer_feedback_and_ai_model_refinement | customer feedback]] and transforming it into actionable evaluations (evals) for research <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   Developing an internal instruction-following eval based on real API usage and user input, serving as a guiding "north star" during development <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   Identifying recurring themes from [[customer_feedback_and_ai_model_refinement | customer feedback]] and internal model usage to prioritize which evals to pursue <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

An interesting insight from [[customer_feedback_and_ai_model_refinement | user feedback]] was the need for models to ignore pre-existing world knowledge and *only* use information provided in context, a capability not typically measured by standard benchmarks <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

> "The shelf life of an eval is like three months unfortunately like progress is so fast things are getting saturated so quickly" <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

Michelle emphasizes the continuous need for new evals, particularly for long-context real-world scenarios and more nuanced instruction following <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Post-Training and Model Development
The process of shipping a model like GBT 4.1 involves a large team and significant effort <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. The three models (standard, mini, nano) are either "mid-trains" (freshness updates) or new pre-trains <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

Michelle's team focuses on [[PostTraining Model Optimization in AI | post-training]] <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>, which involves:
*   Determining the optimal mix of data <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   Setting the best parameters for RL (Reinforcement Learning) training <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Weighting different rewards <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

This process involves a flurry of [[experimentation_in_ai_and_data_science | training]] and running "tons of [[experimentation_in_ai_and_data_science | experiments]]" to see how different datasets or parameter tweaks impact performance <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. An alpha testing phase, typically lasting about a month, allows for rapid training and feedback incorporation <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Fine-Tuning: Enhancing AI Models

[[Fine tuning models for better outcomes | Fine-tuning]] is a critical technique for improving AI model performance and adaptability. Michelle categorizes [[Fine tuning models for better outcomes | fine-tuning]] into two main camps:

### 1. Fine-tuning for Speed and Latency (SFT)
This approach aims to reduce latency and improve speed, making models like 4.1 operate faster at a fraction of the cost <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. It remains the "workhorse" of OpenAI's SFT (Supervised Fine-Tuning) offering <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. If a model works well but needs to be faster, users should consider fine-tuning mini and nano models <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.

### 2. Fine-tuning for Frontier Capabilities (RFT)
RFT (Reinforcement Learning from Feedback/Human Feedback) allows users to push the frontier of what a model can do in a specific domain <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
*   **Data Efficiency**: RFT is "so data efficient" that it can achieve significant improvements with as few as "hundred samples or something on that order" <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. This contrasts with earlier assumptions that massive datasets were always required for fine-tuning <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.
*   **Internal Process**: RFT uses "basically the same RL process" that OpenAI uses internally to improve its own models, indicating its effectiveness and robustness compared to SFT <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.
*   **Use Cases**: RFT works well for:
    *   Teaching an [[Effectiveness of AI agents in specific tasks | agent]] how to select a workflow or reason through a decision process <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
    *   Applications in deep tech where organizations possess unique, verifiable data, such as chip design or drug discovery in biology <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

Michelle's view on fine-tuning has evolved from being skeptical to recognizing RFT's value for pushing capabilities in specific domains <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>.

### When to use which Fine-tuning Method:
*   **Preference Fine-tuning**: For stylistic adjustments <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   **SFT**: For simpler tasks where the model gets a small percentage wrong (e.g., 10% of cases in classification) and you want to close that gap <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.
*   **RFT**: For problems where "just no model in the market does what you need" <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>, especially with verifiable data.

## The Evolution of AI Models and Agents

OpenAI's strategy generally leans into the "G" in AGI (Artificial General Intelligence), aiming for a single, general model <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. However, GBT 4.1 was a specific instance where a "particularly acute need" for [[developers_approach_to_ai_models_and_agents | developers]] led to decoupling its development from ChatGPT <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This allowed for faster training, quicker feedback loops, and specific [[ai_model_pretraining_and_finetuning_decisions | model training choices]], such as upweighting coding data and removing ChatGPT-specific datasets <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>. Despite this specific approach, the long-term goal is simplification and convergence towards more general models <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

### State of AI Agents
[[Effectiveness of AI agents in specific tasks | Agents]] currently perform "remarkably well in well-scoped domains" where tools are available and user intent is clear <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. The challenge lies in bridging the gap to the "fuzzy and messy real world," where users may not know what an [[Effectiveness of AI agents in specific tasks | agent]] can do, or the [[Effectiveness of AI agents in specific tasks | agent]] lacks awareness of its own capabilities or real-world context <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

Future improvements for [[Effectiveness of AI agents in specific tasks | agents]] include:
*   **Engineering Side**: APIs and UIs that make it easier to follow an [[Effectiveness of AI agents in specific tasks | agent]]'s actions, provide summaries, and allow users to intervene and change trajectory <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **Model Side**: Enhanced robustness and "grit" to handle errors (e.g., API 500s) without getting stuck <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Ambiguity Handling**: Making it easier for [[developers_approach_to_ai_models_and_agents | developers]] to tune whether a model should ask for more information or proceed with assumptions when faced with ambiguity <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### AI in Code
GBT 4.1 and other models show "remarkably good" performance in code when the problem is "locally scoped" (e.g., changing a library where files are close) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. However, challenges remain in:
*   **Global Context**: Reasoning about many parts of complex code <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   **Technical Detail Transfer**: Passing extremely technical details between files <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Front-end Coding**: While improved, further enhancement is needed to produce "beautiful" code that front-end engineers would be proud of, addressing linting and code style <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Irrelevant Edits**: Reducing instances where the model changes more than requested or injects its own style <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

## Future of AI Research and Application

### Multimodality and Generalization
Michelle emphasizes the rapidly improving multimodal capabilities of the new pre-trains <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. Many things that didn't work previously now function seamlessly, suggesting that connecting models to "as much information about your task as possible" will yield better results over time <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. The trend points towards generalization, where combining different capabilities produces "a much better result" <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.

### Personalized Learning through AI
[[Personalized learning through AI | Enhanced memory]] is a key aspect of future models, allowing AI to learn about individual users <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. This means a user's ChatGPT experience will be "so different" from another's, adapting to personal preferences and becoming more useful <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. Increased steerability via custom instructions will also allow users to fine-tune AI personalities <a class="yt-timestamp" data-t="00:39:25">[00:39:25]</a>.

### AI in Language Learning
Beyond general applications, AI is making strides in specific fields. While not explicitly mentioned as "[[AI in language learning | language learning]]", the ability of AI to personalize and adapt to user styles suggests potential for tailored educational experiences, similar to how it can adapt to individual preferences in general conversation <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.

### Accelerating Research
A significant area of focus for OpenAI is using AI models to make other models better <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>, particularly in reinforcement learning where signals from models can guide improvements <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. This includes improving the speed of [[experimentation_in_ai_and_data_science | iteration]], allowing researchers to run more [[experimentation_in_ai_and_data_science | experiments]] faster with fewer resources <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>. Synthetic data has been an "incredibly powerful trend" in this regard <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.

### Outlook on AI Progress
Michelle believes that AI model progress will continue at a rapid pace, similar to the last year, without slowing down or undergoing an immediate "fast takeoff" <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. She estimates that even if model progress completely stopped now, there would be "10 years of building at least" to extract value from existing capabilities <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>. This "capabilities overhang" is compared to the internet, which continues to integrate into the world <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.

### Combining Model Capabilities
The future GPT-5 aims to combine the diverse strengths of models like GPT-4o (great conversationalist, tone matching) and O3 (strong reasoning, deep thinking) <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. The challenge is balancing these capabilities, ensuring the model remains a "delightful chitchat partner" while knowing "when to reason" without unnecessary delays <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.

## Recommendations for Companies and Developers

*   **Prioritize Evals**: The most successful startups have deep knowledge of their use cases and robust evals <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. This enables them to quickly assess new models when they drop <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   **Adapt Prompts and Scaffolding**: Be prepared to switch prompts and scaffoldings to tune them to particular models <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Build Just Out of Reach**: Focus on use cases that are "maybe just out of reach" of current models or work inconsistently (e.g., 1 out of 10 times) <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. If fine-tuning shows a 10% pass rate that can be boosted to 50%, it's likely a candidate for a future model to "crush it" <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Embrace Scaffolding**: It is "super worth it" to build scaffolding to ship value to users, even if it's a few months of arbitrage before core capabilities improve <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. However, keep future trends in mind (e.g., improving context windows, reasoning, instruction following) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Modular Systems**: Make systems modular and easy to plug in different solutions to move faster in the long run <a class="yt-timestamp" data-t="00:30:47">[00:30:47]</a>.
*   **Generalist Skills**: Michelle is "long generalists," believing that strong product understanding and scrappy engineering skills will be more important than deep AI research expertise for app-layer companies <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.

### Prompting Tips for 4.1
*   **Structured Prompts**: Using XML or other structured formats can significantly improve model performance <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.
*   **"Keep Going"**: Explicitly instructing the model to "keep going" or "please don't come back to me until you've solved the problem" can lead to "remarkably better performance" <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>. OpenAI aims to train future models to inherently exhibit this behavior <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.

## Conclusion

Michelle Pokris encourages [[developers_approach_to_ai_models_and_agents | developers]] and power users to provide [[customer_feedback and AI model refinement | feedback]], especially when models aren't working well with specific prompts, to help continuously improve the models <a class="yt-timestamp" data-t="00:46:12">[00:46:12]</a>.