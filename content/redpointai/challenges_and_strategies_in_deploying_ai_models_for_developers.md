---
title: Challenges and strategies in deploying AI models for developers
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

Michelle Pokris, Post-Training Research Lead at OpenAI, played a crucial role in enhancing models like GPT-4.1 for developers <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Her work focuses on making these models more user-friendly and practical for real-world applications <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article explores the [[Challenges and strategies in expanding AI applications globally | challenges]] and strategies involved in deploying AI models effectively for developers, drawing insights from her experiences.

## Shifting Focus: From Benchmarks to Real-World Utility

The development of GPT-4.1 marked a significant shift from optimizing for benchmarks to prioritizing real-world usage and utility for developers <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Developer Joy**: The primary goal was to create a model that developers would find a "joy to use" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Addressing Practical Issues**: Previous models, while strong on benchmarks, often stumbled on basic functionalities like instruction following, formatting, or sufficient context length <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. GPT-4.1 focused on addressing these specific pain points raised by developers <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Feedback-Driven Evals**: A core strategy involved talking to users, gathering their feedback, and transforming it into internal evaluations (evals) that could be used during research and development <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. An internal instruction following eval, based on real API usage, served as a "north star" for the model's development <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## The Role of Evals in Model Development

Evals are critical for understanding and addressing model limitations.
*   **Identifying Problems**: Developers often highlight general issues ("it's kind of weird in this one use case"), requiring deep dives to uncover the root cause and create specific prompts for evaluation <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For example, a recent insight revealed models struggled with instructions to "ignore everything you know about the world and only use the information in context," a problem not captured by standard benchmarks <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Determining Importance**: The most important evals are determined by recurring themes from customer feedback, internal model usage, and internal customers building on OpenAI's models <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Community Contribution**: OpenAI actively seeks more real-world, long-context evals and better definitions for "instruction following," which is a complex and multifaceted challenge in ML <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Short Shelf Life**: Due to the rapid pace of AI progress, the "shelf life of an eval is like three months" before models saturate them, necessitating a continuous hunt for new evaluation methods <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

## Impact of GPT-4.1 on AI Adoption

GPT-4.1's release has spurred unexpected and innovative uses.
*   **Improved UI and Coding**: The model significantly improved UI and coding capabilities, leading to the development of "really cool apps" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **Nano's Influence on [[Challenges in AI Adoption and Deployment | AI Adoption]]**: The introduction of smaller, cheaper, and faster models like Nano has driven substantial [[Challenges in AI Adoption and Deployment | AI adoption]] by demonstrating that demand exists across all points of the cost-latency curve <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Behind the Scenes: Shipping an AI Model

Shipping a model like GPT-4.1 involves extensive, coordinated effort:
*   **Model Iteration**: The process includes new pre-trains (or "mid-trains" for freshness updates) and significant post-training work <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Post-Training Focus**: Post-training teams determine the optimal mix of data, parameters for reinforcement learning (RL) training, and weighting of different rewards <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Rapid Iteration**: Development involves a "flurry of training," running numerous experiments to test data sets and tweak parameters, followed by rapid alpha testing to incorporate feedback <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

## Current State and Future of AI Agents

Agents show remarkable performance in well-scoped domains but face [[Challenges and Strategies in Enterprise AI Deployment | challenges]] in the real world.
*   **Well-Scoped Success**: Agents excel when provided with clear tools and user requests in well-defined domains <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Real-World Hurdles**: [[Challenges in deploying AI models effectively | Challenges]] arise in bridging the gap to "fuzzy and messy" real-world scenarios, where users may not know agent capabilities, agents lack self-awareness, or they are not sufficiently connected to external information <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Context and Ambiguity**: A key issue is getting sufficient context into the model <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Models also need improved steerability for ambiguity: deciding whether to ask for more information or proceed with assumptions <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Robustness and Grit**: Future improvements require greater robustness to handle errors (e.g., API 500s) and "grit" to recover and continue tasks <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Engineering Improvements**: APIs and UIs are needed to track agent progress, provide summaries, and allow users to "jump in and change the trajectory" <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Advancements and Challenges in AI Code Capabilities

AI models have significantly improved in code generation.
*   **Local Scope Excellence**: Models like GPT-4.1 are "remarkably good" at locally scoped code problems, such as changing libraries where files are nearby <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Remaining Challenges**:
    *   **Global Understanding**: Models still struggle with tasks requiring reasoning about many diverse parts of a codebase or passing technical details between files <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
    *   **Front-End Quality**: While front-end coding has improved, the goal is to produce code that a front-end engineer would be proud of, addressing linting and code style <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
    *   **Irrelevant Edits**: Reducing "irrelevant edits" (where the model injects its own style or changes more than requested) is an ongoing focus, with improvements from 9% to 2% between GPT-4.0 and 4.1, but aiming for zero <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

## Strategic Decisions in Model Evolution

OpenAI's long-term philosophy leans towards AGI, aiming for a single, general model <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Simplifying Product Offerings**: The ideal future involves one general model that serves both conversational and developer use cases, simplifying the model selection process <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
*   **GPT-4.1's Targeted Approach**: GPT-4.1 was a strategic deviation, developed separately from ChatGPT due to an "acute need" for developer-focused improvements <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This allowed for faster iteration, a different timeline, and specific model training choices (e.g., down-weighting chat data, up-weighting coding data) <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
*   **Benefits of Generalization**: Combining "creative energies of all researchers" on a single model generally leads to better results <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. However, there's still room for targeted models when it makes sense to ship a specialized product very well <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

## Strategies for Companies Navigating Rapid AI Progress

Companies face the [[Challenges of building AI infrastructure companies | challenge]] of keeping up with rapid model releases.
*   **Robust Evals are Key**: The most successful startups have deep knowledge of their use case and "really good evals" that allow them to quickly assess new models when they drop <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   **Adaptability in Prompting**: Successful customers can switch and tune their prompts and scaffoldings to particular new models <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Building Just Out of Reach**: A key strategy is to develop features that are "maybe just out of reach" of current models (e.g., working 1 out of 10 times) <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. These will likely "crush it" with future models, giving early market advantage <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.
*   **Scaffolding and Future Trends**: While it's worthwhile to build scaffolding to ship value now (arbitrage for a few months), companies must be prepared to change things and keep an eye on future trends like improving context windows, reasoning capabilities, and instruction following <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Multimodal Capabilities**: Multimodal capabilities are rapidly improving; developers should connect models to as much information as possible, even if results are "meh" today, as they will improve <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

## Fine-tuning for Performance and Frontier Capabilities

Fine-tuning has seen a "renaissance" as a powerful tool for developers <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   **Two Fine-tuning Camps**:
    *   **Speed and Latency (SFT)**: Used to optimize existing well-performing models (like GPT-4.1) for faster inference <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
    *   **Frontier Capabilities (RFT)**: Allows pushing the frontier in specific domains <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. RFT is highly data-efficient, often requiring only hundreds of samples <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. It's based on the same RL process OpenAI uses internally, making it robust and less fragile than SFT <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.
*   **When to Use Which**:
    *   **Preference Fine-tuning**: For stylistic adjustments <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
    *   **SFT**: For simple classification tasks where a small accuracy gap needs to be closed <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.
    *   **RFT**: For problems where "no model in the market does what you need" <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>, especially in deep tech domains where organizations have unique, verifiable data (e.g., chip design, biology/drug discovery with easily verifiable outcomes) <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.

## Future of Foundation Models and AI Expertise

The trend is towards more general and robust models, impacting the needed expertise for app companies.
*   **Convergence to Generalization**: While specialized foundation models (e.g., robotics, biology) might emerge, the current trend suggests that "combining everything just produces a much better result," indicating a convergence towards more general models <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.
*   **Simplifying Model Selection**: OpenAI aims to simplify the current complex "decision tree" for choosing models <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>. For enterprise users, the recommendation is to start with GPT-4.1, then explore Mini and Nano for speed, and progressively move to O4 Mini or O3 for higher reasoning, eventually considering RFT for extreme cases <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>.
*   **Prompting Improvements**: While good prompting (e.g., using XML for structure, explicitly telling the model to "keep going") is helpful, future models aim to perform well "out of the box" even without optimal prompting <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.
*   **AI Expertise for App Companies**: The future favors "generalists" and "scrappy engineers" who understand the product and can combine models and solutions, rather than deep AI research PhDs <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.
*   **Leveraging Models to Improve Models**: A key area of future research is using AI models themselves to improve other models, particularly in reinforcement learning, through powerful synthetic data generation <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Capabilities Overhang**: Even if model progress stopped today, there are "tens of trillions of dollars of value" to be extracted from current models, indicating a significant "capabilities overhang" similar to the internet's ongoing impact <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.
*   **GPT-5 Challenge**: The primary challenge for GPT-5 is combining the diverse capabilities of different models (e.g., GPT-4o's conversational delight vs. O3's hard reasoning) into a single, cohesive model that knows when to switch modes appropriately <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>.

## Key Takeaways

*   **Evals are Paramount**: Companies should prioritize developing their own robust, granular evals based on real-world usage to quickly assess new models and identify specific areas for improvement <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.
*   **Embrace Arbitrage**: Building scaffolding to achieve immediate product value, even if it might be "obviated" by future model improvements, is a valid strategy for short-term market advantage <a class class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
*   **Stay Agile**: The rapid pace of AI progress necessitates continuous adaptation of prompting strategies and a willingness to iterate on solutions <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Strategic Fine-tuning**: Revisit assumptions about fine-tuning, especially RFT, for pushing frontier capabilities in niche domains with verifiable data <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.

For more information, readers can refer to the GPT-4.1 blog post or reach out to Michelle Pokris on Twitter for feedback on model performance <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.