---
title: Counterfactual Explanations and Model Explainability
videoId: Y4wMksHyMFg
---

From: [[causalpython]] <br/> 

## Introduction to Counterfactual Explanations

[[Explainable AI and Feature Importance | Counterfactual explanations]] are a method used to understand the behavior of blackbox models <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. They operate without needing to "open" the model, instead focusing on how inputs to a model need to change to produce different outputs <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. While the term "counterfactual" can have a [[Causality and Causal Models | causal]] meaning, its [[Causality and Causal Models | causal]] implication is often implicit in much of the existing literature <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Faithfulness vs. Plausibility

Past work on [[Explainable AI and Feature Importance | counterfactual explanations]] has largely focused on *plausibility* <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. Plausibility means that the generated counterfactual explanation appears intuitive, makes sense to human decision-makers, and is consistent with the true data generating process <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>, <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This ensures explanations look like actual data points within a high-density region of the data distribution <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

However, a key insight is that focusing solely on plausibility can lead to a loss of *faithfulness* <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Faithfulness, in this context, means that the explanation accurately reflects how the blackbox model actually behaves <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. If only plausible explanations are shown, while other less intuitive but equally valid (in the model's eyes) explanations exist, it risks "whitewashing" the model by presenting a misleading view of its internal workings <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This work prioritizes faithfulness first, with plausibility as a secondary consideration <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

> "We are... committing the risk of whitewashing a blackbox model because we're showing something that's plausible, an explanation that pleases us, but it doesn't necessarily reflect accurately how the model behaves." <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>

### Illustrative Example: MNIST Digits

Consider a simple Multi-Layer Perceptron (MLP) classifier for MNIST digits <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. If the model correctly classifies an image as a "9" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, the task for a [[Explainable AI and Feature Importance | counterfactual explanation]] generator is to determine what changes are necessary for the model to predict a "7" instead <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

Different approaches can produce various "valid" counterfactuals, meaning the classifier confidently predicts them as a "7" <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>, <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Some of these may resemble adversarial attacks, which are not intuitively recognizable as a "7" <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Other approaches, like "Revise" which uses a variational autoencoder, generate counterfactuals that are genuinely plausible and look like a "7" <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The challenge arises when less plausible, yet still valid (to the model), explanations are suppressed in favor of only the human-pleasing plausible ones <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

## Approach for Faithful Explanations

Instead of relying on surrogate models to derive better explanations, this work focuses on leveraging properties intrinsic to the model itself <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. The goal is to obtain plausible counterfactuals directly from the model, provided the model has learned plausible explanations for its data <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

This is achieved by borrowing ideas from:
*   **Energy-based modeling** to characterize the generative capacity of the classifier <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>, <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Conformal prediction** to quantify predictive uncertainty <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>, <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

Both these approaches are model-agnostic, allowing application to virtually any differentiable classifier <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## Relation to Causal Counterfactuals

It is important to note that the definition of "faithfulness" here differs from the "assumption of faithfulness" used in [[Causality and Causal Models | causal discovery]] <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

[[Causality and Causal Models | Causal counterfactual explanations]] exist, notably through work by Kimi et al. and B Shop, which leverage [[Causality and Causal Models | causal knowledge]] to generate causally valid counterfactuals <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. This [[Causality and Causal Models | causal knowledge]] can lead to more efficient generation of counterfactuals at a smaller cost to individuals <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. However, the described work takes a different path, focusing on model properties rather than external [[Causality and Causal Models | causal knowledge]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.