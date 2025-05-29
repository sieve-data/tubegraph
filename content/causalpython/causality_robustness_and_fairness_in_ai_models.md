---
title: Causality Robustness and Fairness in AI Models
videoId: Y4wMksHyMFg
---

From: [[causalpython]] <br/> 

The fields of causality, robustness, and fairness are often studied independently in responsible AI literature. However, for a responsible AI model, properties like robustness and fairness need to be enforced simultaneously during training <a class="yt-timestamp" data-t="12:31:38">[12:31:38]</a>. This work explores the possibility of developing a model that is adversarially robust and fair, while also considering its underlying [[causal AI and machine learning | causal structure]] <a class="yt-timestamp" data-t="12:51:16">[12:51:16]</a>.

## Definitions and Connections
*   **Adversarial Robustness**: Focuses on perturbing an individual data point so that its label changes, aiming to make the model resilient to such perturbations <a class="yt-timestamp" data-t="13:01:21">[13:01:21]</a>.
*   **Individual Fairness**: States that two similar individuals should receive similar decisions from the model <a class="yt-timestamp" data-t="13:14:14">[13:14:14]</a>.

These two notions are highly connected <a class="yt-timestamp" data-t="13:21:56">[13:21:56]</a>:
*   Robustness can be considered in terms of fairness when the perturbation is on a sensitive attribute, ensuring two individuals with perturbed sensitive attributes remain similar <a class="yt-timestamp" data-t="13:26:01">[13:26:01]</a>.
*   Perturbation can also define similarity between data points <a class="yt-timestamp" data-t="13:39:13">[13:39:13]</a>.

## Approach and Contributions
The main idea is to create a metric that defines similarity between data points, accounting for perturbations on features and sensitive attributes, while also incorporating the [[Causality in Artificial Intelligence | causal structure]] where sensitive and non-sensitive features are related <a class="yt-timestamp" data-t="13:47:49">[13:47:49]</a>. Unlike typical adversarial robustness where perturbations are uniform (like a ball) and features can be perturbed independently <a class="yt-timestamp" data-t="14:10:04">[14:10:04]</a>, this work uses ideas from [[Causal AI and machine learning | causal literature]], specifically counterfactuals, to create perturbations <a class="yt-timestamp" data-t="14:29:43">[14:29:43]</a>.

By combining the concepts of:
1.  Counterfactual perturbations (from [[Causality and Machine Learning | causal literature]]) <a class="yt-timestamp" data-t="14:31:14">[14:31:14]</a>
2.  Twinned perturbations in robustness <a class="yt-timestamp" data-t="14:35:12">[14:35:12]</a>
3.  Perturbations for sensitive attributes in fairness <a class="yt-timestamp" data-t="14:37:46">[14:37:46]</a>

It is possible to train a model that is simultaneously fair and robust, and [[Causality in Artificial Intelligence | causal aware]] <a class="yt-timestamp" data-t="14:42:04">[14:42:04]</a>.

## Main Lessons and Real-World Impact
The key takeaway is that robustness, fairness, and causality should not be defined independently, as they are highly interconnected <a class="yt-timestamp" data-t="14:59:09">[14:59:09]</a>. For models to be deployed in real-world scenarios, they should account for all these dimensions <a class="yt-timestamp" data-t="15:07:05">[15:07:05]</a>. This work shows that it is possible to achieve this without significantly sacrificing performance or incurring high computational costs <a class="yt-timestamp" data-t="15:30:17">[15:30:17]</a>. This means models can be deployed that are better in terms of responsibility without being overly expensive <a class="yt-timestamp" data-t="15:53:14">[15:53:14]</a>.