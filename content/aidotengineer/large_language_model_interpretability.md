---
title: Large language model interpretability
videoId: VhPfM_aGBVc
---

From: [[aidotengineer]] <br/> 

Anthropic, an AI safety and research company, focuses on building safe and effective [[large_language_models_and_selfimprovement | large language models]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. A distinguishing research direction for Anthropic is interpretability <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This involves reverse engineering the models to understand how and why they are thinking <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, and developing capabilities to steer them for specific use cases <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Stages of Interpretability Research

Interpretability research is still in its early stages <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. It is approached in stages that build upon each other <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>:

*   **Understanding** Grasping [[large_language_models_and_selfimprovement | AI]] decision-making <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Detection** Understanding specific behaviors and assigning labels to them <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Steering** Influencing the [[large_language_models_and_selfimprovement | AI]]'s input <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Explainability** Unlocking business value from interpretability methods <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Methods and Goals

Anthropic's interpretability team uses methods to understand feature activations at the model level <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. They have published research on "Monosemanticity" and "Scaling Monosemanticity" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. As the technology improves, it could lead to better detection landscapes, providing a deeper grasp of model thinking and behavior <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>, and even discovering "sleeper agents" for safety reasons <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Interpretability is expected to provide significant improvements in [[large_language_models_and_selfimprovement | AI]] safety, reliability, and usability in the long term <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Examples

*   **Feature Activation:** When a model is asked about NBA scores and responds with "Steph Curry scored 30 points," it activates a specific feature, like "feature number 304: famous NBA players" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This represents a group of neurons activating in a recognizable pattern identified across all mentions of famous basketball players <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Model Steering (Golden Gate Claude):** An example of steering the model was with "Golden Gate Claude" <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. By amplifying the activation in the "Golden Gate" direction, if a user asked, "What should I paint my bedroom?", Claude would respond with suggestions like "paint it red like the Golden Gate Bridge" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.