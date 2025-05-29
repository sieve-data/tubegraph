---
title: Role of reinforcement learning in causal inference
videoId: y59_XLOnmgI
---

From: [[causalpython]] <br/> 

[[causal_inference_and_its_applications | Causal inference]] is a field that draws from multiple disciplines, and reinforcement learning (RL) is considered one of these contributing areas <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. In fact, some perspectives view reinforcement learning as a "flavor" of [[causal_inference_and_its_applications | causal inference]], or vice versa <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.

## Similarities between RL and Causal Inference

At its core, reinforcement learning involves an agent interacting with an environment to maximize a specific metric through a series of actions <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>. This framework closely mirrors [[causal_inference_and_its_applications | causal inference]]:
*   The "environment" in RL can be likened to the set of covariates in [[causal_inference_and_its_applications | causal inference]] <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.
*   The "actions" in RL are analogous to "treatments" in [[causal_inference_and_its_applications | causal inference]] <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   Both fields aim to identify the optimal actions or treatments that maximize a desired outcome <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

This inherent similarity allows for the transfer of concepts and techniques between the two domains <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>.

## Applications and Benefits

One significant benefit of this connection is the ability to utilize techniques from reinforcement learning for [[causal_inference_and_its_applications | causal inference]] tasks, especially in business contexts where interventions can be controlled <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>, <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

### Offline Policy Evaluation
A key technique borrowed from RL is **offline policy evaluation** <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. This allows for:
*   Evaluating a new policy (a different set of decisions) using historical data, even if that policy has never been implemented in a real-world setting <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>, <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.
*   Estimating how different actions would have performed on existing data <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>.

### Personalization and Decision-Making
RL frameworks can naturally fit problems requiring personalization or heterogeneous treatment effects <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>, <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. For example:
*   In debt collection, identifying which types of customers are most likely to respond positively to a call (i.e., have a higher incremental impact on payment probability) <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   In cross-selling, determining which customers would benefit most from a prime credit card offer (i.e., have the highest incrementality in conversion probability) <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.

These scenarios focus on optimizing actions for specific individuals rather than average effects, aligning well with the decision-making focus of RL <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.

## Challenges and Considerations

### Avoiding Confounding and Bias
A significant challenge when integrating RL and [[causal_inference_and_its_applications | causal inference]] is addressing confounding <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.
*   Reinforcement learning agents can be susceptible to confounding bias, learning associational relationships rather than causal ones if not carefully managed <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>, <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>.
*   For instance, an RL agent might learn that calling customers leads to high payment rates if it only calls customers who were likely to pay anyway (e.g., those only a few days late) <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>. This is correlation, not causation <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.

### The Role of Human Oversight
To mitigate these biases, it is often beneficial to have a "human in the loop" who oversees the model's retraining process <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>, <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. This human can implement techniques to debias the data <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.

Techniques to correct for bias:
*   Instead of deterministic actions, making them probabilistic (e.g., an action has a probability of being taken, or a probability of not being taken) <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>, <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.
*   Using propensity scores to correct for biases introduced by non-randomized actions <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>, <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>.

### Evaluation Metrics for Causal Models
Developing robust evaluation metrics for [[causal_reinforcement_learning | causal reinforcement learning]] models is challenging because causal quantities are inherently unobservable <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>, <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. Unlike traditional [[machine_learning_and_causality | machine learning]] where cross-validation and predictive metrics (like AUC) are straightforward <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>, evaluating the "best" [[causal_inference_and_its_applications | causal model]] requires different approaches <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>. The goal is to adapt the "meat grinder framework" (trying many models and picking the best performing one) from [[machine_learning_and_causality | machine learning]] to [[causal_inference_and_its_applications | causal inference]] <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

Key issues:
*   **Cross-validation for [[causal_inference_and_its_applications | causal models]]**: How to perform it effectively <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.
*   **Feature selection**: Determining what variables to include or exclude from a [[causal_inference_and_its_applications | causal model]] remains difficult <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>, <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

Ultimately, having a trusted, unbiased dataset (preferably randomized data) for validation is crucial for evaluating [[causal_inference_and_its_applications | causal models]] <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. This allows for greater confidence in the performance metrics, even if the training data is less pristine <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.

## Conclusion

The intersection of reinforcement learning and [[causal_inference_and_its_applications | causal inference]] offers powerful tools for optimizing decision-making processes in complex systems. While challenges remain, particularly in bias mitigation and evaluation, the shared underlying principles and the potential for mutual enrichment make this a promising area of development for applied causality.