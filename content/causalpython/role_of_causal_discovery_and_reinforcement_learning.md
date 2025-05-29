---
title: Role of causal discovery and reinforcement learning
videoId: y59_XLOnmgI
---

From: [[causalpython]] <br/> 

[[Reinforcement learning and causal structures | Reinforcement learning]] (RL) is considered by some to be a subset of [[Machine learning and causal inference methodologies | causal inference]] due to similarities in their underlying goals [00:24:07]. Both fields aim to optimize a metric through actions performed in an environment, aligning closely with [[Causal decision making and reinforcement learning | causal decision-making]] and optimization [00:24:26].

## Reinforcement Learning as a Flavor of Causal Inference

The core of [[reinforcement_learning_and_causal_structures | reinforcement learning]] involves an environment, a metric to optimize, and actions to maximize that metric [00:24:26]. This structure mirrors [[causal_discovery_and_inference_in_ai | causal inference]], where actions are considered "treatments" and the goal is to find the treatment that maximizes an outcome conditioned on covariates, which are analogous to the environment in RL [00:24:56].

This conceptual overlap allows for the application of [[reinforcement_learning_and_causal_structures | reinforcement learning]] techniques to [[causal_decision_making_and_reinforcement_learning | causal inference]] problems [00:25:17]. A notable example is **offline policy evaluation**, a technique from RL that enables the assessment of a hypothetical policy (a different set of decisions) using historical data, even if that policy was never actually implemented [00:25:25].

### Human in the Loop for Debiasing

While [[reinforcement_learning_and_causal_structures | reinforcement learning]] models can self-update, applying them in [[Machine learning and causal inference methodologies | causal inference]] often benefits from a human in the loop [00:26:02]. This human oversight is crucial for retraining models and debiasing data [00:27:50].

RL agents, if not managed carefully, can be susceptible to confounding and may learn [[reinforcement_learning_and_causal_structures | associational world models]] rather than truly causal ones [00:27:30]. For instance, a debt collection model might learn that calling people with low delinquencies leads to high payment rates. This is a correlation, not causation, as these individuals were likely to pay regardless of the call [00:28:10].

To prevent such issues, techniques like making actions probabilistic rather than deterministic can be employed, allowing for the use of propensity scores to correct biases [00:29:07]. This ensures that models learn from biased historical data in a way that satisfies [[causal_discovery_and_inference_in_ai | causal assumptions]], such as unconfoundedness [00:29:50].

An example of this integration is seen in debt collection strategies, where customers with varying delinquency levels need different treatments [00:26:44]. This scenario fits well within both [[reinforcement_learning_and_causal_structures | reinforcement learning]] and [[causal_decision_making_and_reinforcement_learning | causal inference]] frameworks, emphasizing the need for personalized action to maximize impact [00:27:05].

## [[Causal discovery and learning | Causal Discovery]] in Industry

[[Causal discovery and learning | Causal discovery]] is also finding its place in industry, particularly in analyzing complex systems [00:54:17].

### Applications and Challenges

[[Causal discovery algorithms and realworld applications | Causal discovery algorithms]] are often more effective in **enclosed systems** because many of them assume the absence of hidden confounding variables in the data [00:54:28]. These systems are typically well-documented, allowing for the incorporation of expert knowledge to build more complete causal graphs [00:54:48].

However, [[causal_discovery_and_learning | causal discovery]] is also valuable in more **open-ended settings** [00:55:04]. In such cases, the process is often iterative:
1.  **Collect expert knowledge:** Gather insights about the system [00:55:10].
2.  **Combine with algorithms:** Feed this knowledge into [[causal_discovery_algorithms and realworld applications | causal discovery algorithms]] [00:55:13].
3.  **Run algorithms:** Execute the algorithms to identify potential causal connections [00:55:16].
4.  **Test and compare:** Evaluate the results using existing data (e.g., randomized data, or by comparing distributions with a generative model) [00:55:20].
5.  **Reiterate:** Discuss findings with experts and refine the model iteratively [00:55:34].

### Real-World Example: Solar Panel Failure

A practical application of [[causal_discovery_and_learning | causal discovery]] can be seen in predictive maintenance for solar panels [00:55:51]. While a predictive model can forecast when a panel might fail, it doesn't explain *why* [00:56:10]. This is where [[causal_discovery_and_learning | causal discovery]] comes in, helping to identify the root cause of the problem (e.g., overheating, wind, sand) so technicians can address the specific issue [00:56:40].

In this context, [[causal_discovery_and_learning | causal discovery algorithms]] can identify connections within the system, determining which variables cause failures [00:57:33]. This learned [[structural_causal_models_and_causal_discovery | causal structure]] can then be used to train a [[structural_causal_models_and_causal_discovery | structural causal model]] capable of performing root cause analysis [00:58:01].

It's important to note that [[causal_discovery_and_learning | causal discovery]] from observational data generally requires additional assumptions [00:58:30]. However, in systems that are largely enclosed or where external forces can be quantified and expert knowledge is available, this iterative process can be a powerful first step in building models for root cause analysis [00:58:49].