---
title: Causal inference and individual treatment effects
videoId: zTJFUaLjxfE
---

From: [[causalpython]] <br/> 

Scott Muller's work primarily focuses on making better decisions at both the individual and population levels, leveraging [[causal_inference_and_machine_learning | causal inference]] and counterfactual reasoning <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This endeavor directly addresses the **fundamental problem of causal inference**: the inability to observe multiple outcomes for the same individual under different treatments <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. For instance, one cannot observe if a person takes a medicine and recovers, then go back in time to see what would have happened had they *not* taken it <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. While average effects can be estimated at a population level through methods like randomized controlled trials, obtaining precise individual-level estimates or identifying specific counterfactual probabilities remains a significant challenge <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Counterfactual Probabilities and Their Bounds

Historically, Jin Tian and Judea Pearl introduced mathematical bounds on various counterfactual probabilities, such as the probability of necessity, probability of sufficiency, and the probability of necessity and sufficiency <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Although these bounds have been proven mathematically tight (meaning no better bounds can be derived without further information), they are often too broad to be useful for practical decision-making <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Muller's research aims to narrow these bounds, ideally to a point of identification, by exploring what additional [[assumptions_in_causal_inference | assumptions in causal inference]] can be reasonably made for specific scenarios <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## The Monotonicity Assumption

One such helpful assumption is **monotonicity** <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This assumption implies that there is **no possibility of harm in the counterfactual sense** <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Example: Medicine and Harm
Consider a medicine <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>:
*   **Harm** would occur if taking the medicine *prevents* a person from getting better, but if they *hadn't* taken it, their own immune system *would have* healed them <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   If the probability of this negative counterfactual effect is zero (i.e., this scenario is impossible), then the monotonicity assumption holds <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This can be known through the underlying biological mechanisms of the medicine or by definition in certain scenarios <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

When monotonicity can be assumed, it allows for point identification of important counterfactual probabilities, such as the probability of benefit, probability of harm (which would be zero), probability of necessity, and probability of sufficiency <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Challenges in Application
A key challenge in applying monotonicity is knowing if it truly exists in the data <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. While it is rare to definitively *confirm* monotonicity from data alone, it is often much more feasible to *disprove* it <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. There are tests that can show a definite lack of monotonicity, and weaker tests that suggest its presence under specific conditions <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Even when monotonicity is violated, research can determine the limits of its violation, which still allows for narrower bounds on counterfactual probabilities, thus aiding better decision-making <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This concept is akin to "putting a bound on the bound" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## The Unit Selection Framework

Developed by Angley and Judea Pearl, the unit selection framework is particularly valuable for personalized decision-making, such as in marketing <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. It allows assigning a "weight or value" to different types of responders based on their counterfactual behavior <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

### Responders in Marketing (Ad Example)
Using a marketing example where the "treatment" is showing an ad and the "response" is buying a product <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>:

1.  **Complier:** Buys the product if shown the ad, but *not* if not shown the ad <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. (Ideal target for advertising).
2.  **Always Taker:** Buys the product *whether or not* they see the ad <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
3.  **Never Taker:** Does *not* buy the product *whether or not* they see the ad <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
4.  **Defier:** Buys the product if *not* shown the ad, but does *not* buy if shown the ad <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. (The group to avoid advertising to).

Marketers typically want to advertise to compliers. While it generally doesn't matter if you advertise to always or never takers, there might be a negative value due to advertising costs (e.g., fees per email, discounts) <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. Defiers, however, can represent a strong negative value, potentially greater than the positive value from a complier <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.

Traditional A/B testing, while common in marketing, focuses on average performance across groups <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. The unit selection framework, by incorporating individual-level counterfactual reasoning, allows for more optimal advertising strategies by identifying and valuing these different response types <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>. Even though individual treatment effects are not identifiable, combining observational and experimental data can provide useful bounds on the overall value of advertising to a subpopulation, enabling better decisions <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

## Bridging Theory to Practice

Scott Muller emphasizes the importance of translating theoretical advancements in causality into accessible tools for practitioners <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. With his background in software development <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>, he aims to contribute to open-source projects like DoWhy, which provides a consistent API for [[causal_inference_and_machine_learning | causal inference]] methods, similar to scikit-learn for general [[machine_learning_and_treatment_effect_estimation | machine learning and treatment effect estimation]] <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. The goal is to enable domain experts (e.g., in econometrics, biology, marketing) to utilize complex causal models without needing extensive software development expertise, perhaps through graphical user interfaces or integrations into existing popular software <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

## Causality and AI

Muller views [[causal_inference_and_machine_learning | causality]] as a core component necessary for achieving artificial general intelligence (AGI) and superintelligence <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>. Observing how babies understand basic causal relationships (e.g., blocks falling when supported) <a class="yt-timestamp" data-t="00:38:10">[00:38:10]</a>, he believes that the mathematics and science of causality must be "baked in" to [[machine_learning_and_causal_inference_methodologies | machine learning and causal inference methodologies]] to enable powerful reasoning, rather than simply scaling up current models <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>. His current research in [[causal_inference_and_decision_theory | causal inference and decision theory]] is aimed at developing this expertise to later apply to AI architectures <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>.

## Lessons from Business

Scott Muller's transition from computer science and successful businesses into [[causal_inference_and_machine_learning | causal inference]] was prompted by reading "The Book of Why" by Judea Pearl <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>. He realized that despite his success, he had made poor decisions in the past due to a lack of proper data interpretation and causal reasoning <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. This experience instilled in him a deeper understanding of what constitutes a "reasonable assumption" in a given scenario, which is crucial for narrowing the bounds of counterfactual probabilities and making more optimal decisions <a class="yt-timestamp" data-t="00:44:18">[00:44:18]</a>.

## Acknowledgements

Scott Muller expresses immense gratitude to two key mentors:

*   **Judea Pearl:** His PhD advisor, whom he considers one of the great minds in history, like Isaac Newton or Albert Einstein, due to his foundational scientific contributions, especially to the future of [[causal_inference_and_machine_learning | science]] and AI <a class="yt-timestamp" data-t="00:46:06">[00:46:06]</a>. Pearl's intellectual guidance and entertaining personality have been invaluable <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.
*   **Klaus Schaeffer:** His undergraduate computer science professor who became a friend and early investor in two of Muller's businesses, including AppFolio <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>. Schaeffer provided significant resources, introductions, and mentoring, teaching lessons about "irrational exuberance" in entrepreneurship – recognizing when passion is necessary to overcome tough times without being derailed by unrealistic expectations <a class="yt-timestamp" data-t="00:49:01">[00:49:01]</a>.

## Advice for Navigating Challenges

Muller's advice for those starting in challenging or complex fields, like [[causal_inference_and_machine_learning | causality]] or starting a company, is nuanced <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>. He acknowledges that sometimes, it is necessary to "stop" or "be derailed" if one is heading in a wrong direction <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a>. The core challenge is discerning whether an obstacle is a temporary "speed bump" requiring perseverance or a sign that a fundamental change in direction is needed <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.

For business decisions (e.g., pushing forward, pivoting, or exiting), his advice is to **learn counterfactual analysis** <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>. This approach aids in making informed decisions by evaluating hypothetical scenarios <a class="yt-timestamp" data-t="00:53:03">[00:53:03]</a>. In academia, struggling with an idea might signal that the path is not viable, necessitating a change in approach <a class="yt-timestamp" data-t="00:53:33">[00:53:33]</a>. He finds high-impact, hard problems particularly exciting, viewing them as puzzles <a class="yt-timestamp" data-t="00:54:08">[00:54:08]</a>. His personal drive stems from believing a solution is attainable and a strong desire to find it <a class="yt-timestamp" data-t="00:55:11">[00:55:11]</a>.

For more information on Scott Muller's work, his papers are listed on Judea Pearl's website at UCLA, and he is active on Twitter <a class="yt-timestamp" data-t="00:56:37">[00:56:37]</a>.