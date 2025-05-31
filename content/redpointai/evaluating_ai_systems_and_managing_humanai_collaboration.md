---
title: Evaluating AI Systems and Managing HumanAI Collaboration
videoId: NLFboNNKCME
---

From: [[redpointai]] <br/> 

Successfully deploying AI in enterprise settings requires careful [[evaluating_ai_progress_with_roi | evaluation]] and strategic management of [[humanai_interaction_in_education_and_society | human-AI collaboration]].

## Barriers to Enterprise AI Deployment
Despite initial excitement, Generative AI hasn't been "ready yet for prime time" in many enterprises <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. A key challenge is the difference between compelling demos and actual production deployments <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. Many demos are built on small, curated datasets (e.g., 20 PDFs) and fail when scaled to real-world data (e.g., 10,000 PDFs), often due to "hill climbing directly on the test set" <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This highlights the importance of addressing not only the machine learning aspects but also deployment challenges like risk, compliance, and security <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## Human-AI Interaction in Enterprise
A critical question for enterprises is whether to put AI systems directly in front of customers, and the answer often requires caution <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. The higher the value of a use case, the riskier it becomes to directly expose it to customers <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

Instead of full replacement, the focus should be on finding the optimal "ratio of AI to human" <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. This means:
*   **Keeping humans in the loop:** AI should solve problems that are "within reach now" and gradually become more complicated over time <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
*   **Providing tools, not replacements:** For instance, instead of an AI making investment decisions, it should provide great tools to help investors make better decisions <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
*   **Avoiding generalists for specialized tasks:** In an enterprise, you often know exactly what you want from the user and don't want a generalist AI <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Specialization is key <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, using a generalist AI system for performance reviews in the European Union is heavily sanctioned <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Evaluating AI Systems in Practice
There is currently no universally recognized "right way to evaluate systems that enterprises can rely on" <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>. Many companies don't take evaluation seriously enough, often relying on small spreadsheets with high variance <a class="yt-timestamp" data-t="02:53:53">[02:53:53]</a>.

### Challenges in Evaluation
*   **Lack of clear objectives:** A significant problem is that many developers "don't understand what they want" from the AI system <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>. It's crucial to define what "success" looks like in a prototype setting before productionizing <a class="yt-timestamp" data-t="02:37:34">[02:37:34]</a>.
*   **Complexity of full pipelines:** A complete AI system involves multiple components (extraction, retrieval, ranking, generation, post-training, alignment), and evaluating the end-to-end performance is challenging <a class="yt-timestamp" data-t="02:20:51">[02:20:51]</a>.

### Future of Evaluation
A future [[challenges_and_strategies_in_enterprise_ai_deployment | evaluation framework]] needs to be accessible to AI developers who are good at calling APIs, rather than requiring traditional machine learning or statistical testing knowledge <a class="yt-timestamp" data-t="03:12:14">[03:12:14]</a>.

The process typically involves:
1.  **Extracting information** from large-scale data (tens or hundreds of thousands of documents) without failure <a class="yt-timestamp" data-t="02:20:20">[02:20:20]</a>. This "boring stuff" at the beginning of the pipeline is crucial but often overlooked <a class="yt-timestamp" data-t="02:26:17">[02:26:17]</a>.
2.  **Employing sophisticated retrieval mechanisms**, such as a "mixture of retrievers," not just a single dense vector database <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
3.  **Contextualizing the language model** with this information <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
4.  **Applying post-training techniques** on top of the language model <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Importance of Post-Training and Alignment
[[approaches_to_ai_safety_and_alignment | Alignment]] is a "super interesting problem area" focused on making systems maximally useful for end-users <a class="yt-timestamp" data-t="01:16:01">[01:16:01]</a>. Post-training, which includes alignment, is where much of the "magic happens" to make a pre-trained model good at a specific task <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

*   **RLHF (Reinforcement Learning from Human Feedback):** While effective, RLHF is expensive and slow because it requires training a separate reward model and extensive human preference data, which becomes increasingly costly for specialized use cases <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
*   **KTO (Kahneman-Tversky Optimization) and APO (Anchored Preference Optimization):** These methods aim to break the dependency on reward models and explicit preference pairs, allowing for direct optimization on feedback without needing data annotation <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. KTO optimizes directly from implicit feedback like thumbs up/down <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. APO addresses under-specification in preference data by leveraging the model's own quality, ensuring the system learns the right information from rankings <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

This integrated system, custom alignment, and specialization approach are crucial for enterprises to see "real ROI" from AI deployments <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.