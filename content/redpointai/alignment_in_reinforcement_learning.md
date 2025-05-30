---
title: Alignment in reinforcement learning
videoId: NLFboNNKCME
---

From: [[redpointai]] <br/> 

[[trends_in_alignment_research_and_ai_safety | Alignment]] is a crucial problem area in AI, focusing on making systems maximally useful for end-users <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

## Reinforcement Learning from Human Feedback (RLHF)

[[the_role_of_reinforcement_and_finetuning_in_ai | RLHF]] was the "secret sauce" that made ChatGPT effective <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. While instruction [[finetuning_approaches_and_considerations_in_ai | tuning]] (SFT) can capture human preferences at the next token level, [[the_role_of_reinforcement_and_finetuning_in_ai | RLHF]] is designed to capture preferences at the full sequence level <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

However, [[the_role_of_reinforcement_and_finetuning_in_ai | RLHF]] presents two main challenges <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>:
1.  **Reward Model Training** <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>: It requires training a separate, high-quality reward model to propagate rewards back to the sequence, which is expensive and the model is not used in actual generations <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
2.  **Preference Data Acquisition** <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>: Obtaining preference data (e.g., thumbs up/down feedback) necessitates additional data annotation, which is slow and costly, especially for more specialized use cases <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

## Advancements in Alignment Optimization

To address the limitations of traditional [[the_role_of_reinforcement_and_finetuning_in_ai | RLHF]], research has focused on optimizing directly from feedback without needing to train a reward model or perform extensive data annotation <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>:

*   **DPO (Direct Preference Optimization)** <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>: This method focuses on training without a separate reward model, making the process more efficient <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **KTO (Kahneman-Tversky Optimization)** <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>: Developed at Contextual AI, this approach breaks the dependency on preference pairs by optimizing directly on feedback without requiring data annotation <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. It is based on the behavioral economist utility theory and prospect theory <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **CLARE (Contrastive Learning for Alignment with Revisions)** <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>: This method addresses the "under-specification" problem in preference datasets <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. Instead of just ranking options, CLARE contrasts revisions, where a small difference between two options represents a specific "fix," making the preference signal much tighter <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **APO (Anchored Preference Optimization)** <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>: Building on CLARE, APO incorporates the quality of the model being trained into the optimization process <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. If the model is better than the preference data, it learns only the ranking information ("this one is better than this one") rather than the specific "right answer" from the data, which may be suboptimal <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. APO provides more control over how data quality impacts model quality after [[finetuning_approaches_and_considerations_in_ai | training]] <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

## Practical Application in Enterprise AI

At Contextual AI, [[trends_in_alignment_research_and_ai_safety | alignment]] work is often focused on the core model during [[finetuning_approaches_and_considerations_in_ai | post-training]] <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. By leveraging algorithms like KTO and APO, Contextual AI can learn directly from customer feedback, such as thumbs up/down mechanisms in deployments, which was not feasible with standard [[the_role_of_reinforcement_and_finetuning_in_ai | RLHF]] <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.

This [[trends_in_alignment_research_and_ai_safety | alignment]] process tailors models to specific business use cases, moving beyond generalist AI to specialized, customized solutions <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. This specialization helps models pass the "production bar" for enterprise deployments, leading to measurable Return on Investment (ROI) <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. It reflects a "[[compound_ai_systems_and_their_development | systems]] over models" approach, where the aim is to deliver integrated [[compound_ai_systems_and_their_development | systems]] that solve specific problems, rather than just providing general models <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.