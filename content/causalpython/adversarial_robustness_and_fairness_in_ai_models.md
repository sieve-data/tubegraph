---
title: Adversarial Robustness and Fairness in AI Models
videoId: Y4wMksHyMFg
---

From: [[causalpython]] <br/> 

Research presented at AAAI 2024 explored the intersection of [[causality_in_ai | causality]], robustness, and [[fairness_and_bias_in_language_models | fairness]] in responsible AI models, proposing that these properties should not be studied independently due to their inherent connections <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

## Connecting Robustness and Fairness

Traditionally, [[fairness_and_bias_in_language_models | fairness]] and robustness have been treated as separate concerns in AI literature <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. However, this work argues that they are closely related <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

*   **Adversarial Robustness** aims to ensure that a model's label prediction does not change even when individual data points are subtly perturbed <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. The goal is for the model to remain robust against such perturbations <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Individual [[fairness_and_bias_in_language_models | Fairness]]** dictates that two similar individuals should receive similar decisions from an AI model <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

The connection becomes clear when considering perturbations on sensitive attributes for [[fairness_and_bias_in_language_models | fairness]] <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. This means ensuring that two individuals, who are similar except for a perturbation in a sensitive attribute, receive similar outcomes from the model <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. Perturbations can also define similarity between data points <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

## Incorporating Causal Structure

A critical aspect of this research is accounting for the [[causality_in_ai | causal structure]] of data <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. Unlike typical adversarial robustness where perturbations might be uniform or within a defined "ball" <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>, [[causality_in_ai | causal]] relationships mean that sensitive and non-sensitive features are often interdependent <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This implies that one feature cannot be perturbed without affecting others <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

The paper proposes a new metric that defines similarity between data points by incorporating:
*   General perturbations <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>
*   Sensitive attribute perturbations <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>
*   The underlying [[causality_in_ai | causal structure]] <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>

This metric allows for creating perturbations inspired by [[advancements_in_causal_modeling_and_ai | causal literature]], specifically counterfactuals, to achieve both robustness and [[fairness_and_bias_in_language_models | fairness]] simultaneously within a [[causality_in_ai | causal-aware]] framework <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

## Key Findings and Real-World Impact

The research demonstrates that it is indeed possible to develop AI models that are simultaneously robust, fair, and [[causality_in_ai | causal-aware]] <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

*   **Interconnected Properties**: [[fairness_and_bias_in_language_models | Fairness]], robustness, and [[causality_in_ai | causal awareness]] are deeply connected and should not be considered in isolation <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   **Deployable Models**: For real-world deployment, AI models must account for all these dimensions to be truly responsible <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **No Significant Performance Cost**: A key takeaway is that incorporating these properties does not significantly degrade model performance <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. The optimization structure and performance remain comparable <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

This work suggests that developers can build more responsible AI models without incurring substantial computational or performance costs, making them more viable for real-world applications <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.