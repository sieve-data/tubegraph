---
title: Counterfactual reasoning and probabilities
videoId: zTJFUaLjxfE
---

From: [[causalpython]] <br/> 

[[Counterfactual Explanations and Model Explainability | Counterfactual thinking]] involves imagining hypothetical worlds and building causal models for them, as we cannot truly experience or run experiments in these alternative realities. Instead, we estimate what might happen in these worlds based on observations from our own <a class="yt-timestamp" data-t="02:10:10">[02:10:10]</a>.

## Foundations in Causality
The work on counterfactual reasoning often aligns with the third rung of Judea Pearl's "Ladder of Causation" <a class="yt-timestamp" data-t="01:46:16">[01:46:16]</a>. This concept resonates with Konrad Lorenz's idea that "thinking is acting in imaginary space," as it describes how we mentally simulate actions and their potential outcomes <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.

## Challenges in Counterfactual Inference
A central issue in [[Challenges of Causal Inference and Counterfactual Thinking | causal inference]] and [[Counterfactual Explanations and Model Explainability | counterfactual reasoning]] is the "fundamental problem of causal inference" <a class="yt-timestamp" data-t="03:49:09">[03:49:09]</a>. This problem arises because one cannot observe outcomes for different treatments on the same individual at the same time. For instance, you cannot give a person medicine and see if they get better, and then go back in time to see what would have happened if they hadn't taken the medicine <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. While it's relatively straightforward to estimate average effects at a population level through methods like randomized controlled trials, obtaining precise point estimates or identifying individual-level [[Potential Outcomes and Causal Identification | counterfactual probabilities]] is difficult <a class="yt-timestamp" data-t="04:06:04">[04:06:04]</a>.

Early work by Jin Tian and Judea Pearl established bounds on [[Potential Outcomes and Causal Identification | counterfactual probabilities]] like the probability of necessity (PN), probability of sufficiency (PS), and probability of necessity and sufficiency (PNS) <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. Though these bounds are mathematically proven to be "tight" (meaning no better bounds can be achieved without further assumptions), they are often too loose to be practically useful for decision-making <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

### Narrowing Bounds through Assumptions
The primary challenge is how to narrow these bounds, ideally to the point where [[Potential Outcomes and Causal Identification | counterfactual probabilities]] can be "point identified" <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. This requires making additional [[Role of assumptions in causal inference | assumptions]] that are both reasonable and applicable to a specific scenario <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.

#### The Monotonicity Assumption
One such helpful [[Role of assumptions in causal inference | assumption]] is **monotonicity** <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. This assumption implies that there is "no possibility of harm" in a counterfactual sense <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.
*   **Example**: If you take medicine for an illness, monotonicity assumes that the medicine will not prevent you from getting better when you *would* have recovered on your own had you not taken it <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>. If the probability of such a "negative counterfactual effect" is zero, then monotonicity holds <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
*   **Benefits**: When monotonicity is assumed, probabilities of benefit and harm, as well as probabilities of necessity and sufficiency, can be point identified <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.

#### Practical Challenges of Applying Monotonicity
A key challenge in applying monotonicity is knowing when it truly holds <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>. While it's rare to confirm monotonicity solely from data, it's often more feasible to *disprove* it based on available data <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. Ongoing research aims to:
1.  Develop tests to definitively show when monotonicity *does not* hold <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.
2.  Quantify the extent to which monotonicity is violated, allowing for narrower bounds on [[Potential Outcomes and Causal Identification | counterfactual probabilities]] even when it doesn't strictly hold <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. This is akin to "putting a bound on the bound" <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.

## Applications of Counterfactual Reasoning in Decision-Making
The core motivation for this research is to enable better [[causal_inference_and_decision_making | decision-making]] at individual and policy levels through [[Causal Reasoning in DecisionMaking | counterfactual reasoning]] <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

### The Unit Selection Framework
Developed by Angley and Judea Pearl, the **unit selection framework** is a valuable tool, particularly in marketing, that leverages [[Counterfactual Explanations and Model Explainability | counterfactual reasoning]] <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. It allows users to specify the value placed on four different types of responders to a "treatment" (e.g., showing an ad):
*   **Compliers**: Buy the product if shown the ad, but not if not shown <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>.
*   **Always Takers**: Buy the product regardless of whether they see the ad <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.
*   **Never Takers**: Do not buy the product regardless of whether they see the ad <a class="yt-timestamp" data-t="22:07:00">[22:07:00]</a>.
*   **Defiers**: Do not buy the product if shown the ad, but *would* buy it if not shown <a class="yt-timestamp" data-t="22:13:00">[22:13:00]</a>.

Marketers want to advertise to compliers (positive value) and avoid defiers (strong negative value). While A/B testing can identify which ad performs better *on average*, it can be "severely suboptimal" for specific business strategies because it doesn't differentiate between these response types <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>. The unit selection framework, by incorporating user-defined values for each response type, provides bounds on the overall expected value of advertising to a specific subpopulation, allowing for more optimal decisions <a class="yt-timestamp" data-t="25:51:00">[25:51:00]</a>. This framework can be applied using observational and/or experimental data <a class="yt-timestamp" data-t="25:39:00">[25:39:00]</a>.

## The Path to Causal Inference
Scott Muller's personal journey into [[Probabilistic modeling and Bayesian frameworks | causality]] was profoundly influenced by Judea Pearl's "Book of Why" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Having previously been involved in software development and business, where he relied on high-level statistics, reading the book revealed a profound gap in his understanding of data interpretation and [[Causal Reasoning in DecisionMaking | decision-making]] <a class="yt-timestamp" data-t="37:15:00">[37:15:00]</a>. He realized he had likely made suboptimal decisions in the past due to this lack of causal insight <a class="yt-timestamp" data-t="37:34:00">[37:34:00]</a>. This realization highlighted the fundamental nature of causal and counterfactual thinking for human reasoning <a class="yt-timestamp" data-t="37:55:00">[37:55:00]</a>.

## Integrating Causality into AI
A key missing element in the pursuit of Artificial General Intelligence (AGI) and "super intelligence" is the explicit integration of causality into machine learning models and architectures <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>. Simply scaling up existing models or relying on emergent properties (like causality emerging from predicting the next word) is viewed as insufficient <a class="yt-timestamp" data-t="39:41:00">[39:41:00]</a>. The mathematical and scientific principles of [[Probabilistic modeling and Bayesian frameworks | causality]] need to be "baked in" to these systems to enable truly powerful reasoning capabilities <a class="yt-timestamp" data-t="40:33:00">[40:33:00]</a>. This approach is essential for [[benchmarking_causal_reasoning_in_ai | benchmarking causal reasoning in AI]].

## Future Directions
Current research focuses on improving [[Causal inference and decision making | decision-making]] by developing methods to identify or sufficiently narrow bounds on [[Potential Outcomes and Causal Identification | counterfactual probabilities]] <a class="yt-timestamp" data-t="42:49:00">[42:49:00]</a>. This includes finding reasonable [[Role of assumptions in causal inference | assumptions]] that are useful for practitioners <a class="yt-timestamp" data-t="45:11:00">[45:11:00]</a>.

For those starting in challenging fields like [[Probabilistic modeling and Bayesian frameworks | causality]] or entrepreneurship, the advice is to learn [[Counterfactual Explanations and Model Explainability | counterfactual analysis]] <a class="yt-timestamp" data-t="53:03:00">[53:03:00]</a>. This skill can help in making critical decisions, such as whether to persevere through obstacles, pivot, or even exit a venture <a class="yt-timestamp" data-t="52:27:00">[52:27:00]</a>.