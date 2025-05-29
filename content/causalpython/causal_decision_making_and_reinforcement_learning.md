---
title: Causal decision making and reinforcement learning
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

The podcast, *Causal Bandits*, explores the intersection of causality and machine learning, particularly in the context of decision making and reinforcement learning. Dr. Robert Ness, a Senior Researcher at Microsoft Research, shares insights on how [[causal_inference_and_decision_theory | causal inference]] and [[causal_analysis_and_decision_making | causal analysis]] can enhance traditional machine learning approaches.

## Evolution Towards Causality
Dr. Robert Ness began his educational journey in economics before moving to statistics and eventually focusing on [[causal_inference_and_decision_theory | causal inference]] and computation [01:16:11]. His initial attraction to statistics stemmed from his natural aptitude for it and the process of modeling data and building models [02:07:07].

His experience in systems biology during his PhD was pivotal [03:23:28]. He preferred studying natural phenomena, like systems biology, over financial markets because natural sciences offer a "ground truth" to model [03:38:15]. This pursuit led him to [[causal_discovery_and_learning | causal discovery]] algorithms and structure learning, aiming to reconstruct biological pathways from single-cell data [04:56:00].

### Challenges in Applied Causal Discovery
A significant challenge in applying [[causal_discovery_and_learning | causal discovery]] to biological data was making the results practically useful for laboratory analysts and biologists [05:41:20]. Researchers typically don't just want a causal directed acyclic graph (DAG); they want to use it for practical applications like discovering new biomarkers or informing drug discovery [07:01:40]. This led Dr. Ness to adapt [[causal_discovery_and_learning | causal discovery]] methods towards experimental design, where the DAG is an intermediate step to a final outcome, often incorporating uncertainty and sequential workflows [07:26:08].

Evaluating the correctness of a discovered causal structure without a known ground truth was addressed by turning to Bayesian-style reasoning [09:18:00]. This approach allows for dealing with uncertainty and incorporating prior knowledge about the system's size, shape, or disallowed interactions [09:24:26].

## Causal Decision Making and Reinforcement Learning
[[causal_inference_and_decision_theory | Causal decision theory]] is often contrasted with empirical decision theory, which traditionally focuses on maximizing expected utility conditional on action [11:12:12]. However, with a more mature understanding of causal models, their [[integration_of_causal_thinking_in_machine_learning | integration into end-to-end analysis]] is becoming prevalent in automated decision theory [11:47:00].

### Causal Bandits
In settings like causal bandits, causal knowledge can be applied to optimize systems with unknown causal factors that would lead to suboptimal decisions with traditional bandit methods [12:30:30]. This involves scenarios where a confounder has an adversarial relationship with the system, and the goal is to estimate a causal effect in a setting that might not be fully identified [12:13:00].

### [[reinforcement_learning_and_causal_structures | Causal Reinforcement Learning]]
[[reinforcement_learning_and_causal_structures | Causal reinforcement learning]] (Causal RL) addresses how to use causal assumptions to gain sample efficiency in learning [13:04:00]. This is crucial in high-dimensional settings where sample efficiency can make intractable problems tractable [13:14:00]. It also aids in credit assignment, where understanding how a policy led to an outcome can be posed as a causal question using attribution or root cause analysis methods [13:21:00].

Traditional deep reinforcement learning, especially model-free approaches, often model everything as a Markov Decision Process (MDP), folding all information into a "state" variable and ignoring causal nuances [17:31:00]. This approach can be sufficient for maximizing reward [18:16:00]. However, there are cases where actions that maximize expected reward without considering how they change the environment differ from actions that maximize expected reward when causal factors are accounted for [18:28:00]. [[causal_analysis_and_decision_making | Causal analysis and decision making]] can help understand when these differences occur [18:40:00].

Causal RL is particularly valuable when:
*   Maximizing outcomes under circumstances not seen in training data [19:05:00].
*   Actions that maximize outcomes are different when accounting for the system's causal nuances [19:16:00].
*   The state variable may not contain all information required for causal identifiability, leading to biases or suboptimal "associative" decisions rather than "interventional" ones [19:54:00].

Dr. Ness emphasizes the need to find practical scenarios where causal models are definitively necessary, moving beyond "toy problems" that only prove traditional methods' limitations [21:28:00].

### Human-like Decision Making in AI
A key area of interest is making algorithms capable of human-like decision making and [[causal_reasoning_in_ai | causal reasoning in AI]] [13:57:00]. Humans often reason about hypothetical scenarios, known in [[causal_inference_and_decision_theory | causal inference]] as potential outcomes, which is a very sample-efficient way of learning without direct experience [14:46:00]. Causal models provide a language for building algorithms that can perform these kinds of advanced reasoning capabilities [15:06:00].

An AGI system, from a causal perspective, would need to reason about cause and effect [29:45:00]. This involves observing human reasoning abilities, modeling them computationally, and designing tasks to compare algorithmic and human performance [30:21:00]. [[causal_inference_and_decision_theory | Causal inference theory]] is crucial for specifying the assumptions and inductive biases that enable conclusions beyond observed data [31:16:00].

The goal of emulating human reasoning in AI is not always about objective correctness but about alignment with human processes, even if those processes include cognitive biases [33:18:00]. A flexible model would allow for turning these biases on or off [34:48:00]. For example, humans engage in counterfactual simulation less for the absence of actions or events, which is an economical heuristic but not always "sound" [35:52:00]. Algorithmic reasoning can remedy such inefficiencies [37:15:00].

### Probabilistic Programming and Causal Identification
Dr. Ness's work, including a paper with Seyed Mohammad Taheri and Karen Sachs, demonstrates that if an intervention distribution is identified using the rules of do-calculus, a probabilistic programming framework can produce a valid sampling procedure [39:29:32]. This means that latent variable models, often modeled with graphs, can be used for [[causal_inference_and_decision_theory | causal inference]] if identification can be proven [40:06:00]. Tools like `y0` in Python (or `RCI` in R) can verify if a causal query is identifiable given a DAG and observed variables [41:21:00].

This bridge allows users of probabilistic programming languages (like PyMC or Pyro) to leverage their high-dimensional capabilities for [[causal_inference_and_decision_theory | causal queries]] [44:50:00].

### [[generative_ai_and_causal_reasoning | Generative AI and Causal Reasoning]]
The next big thing in causality could be [[causal_discovery_and_learning | causal representation learning]] [49:48:00]. This involves learning latent representations that correspond to actual causes in the data-generating process, allowing for identification based on causal criteria like modularity and invariance [50:07:00].

A prime example is [[generative_ai_and_causal_reasoning | generative AI]] [51:02:00]. When interacting with models like Midjourney or Stable Diffusion, users often want to make precise, localized changes (e.g., changing glasses color without altering other scene elements) [51:10:00]. This requires [[causal_reasoning_in_ai | causal reasoning in AI]]: the model should understand that changing glasses color only affects elements causally downstream of the glasses, not unrelated parts of the image [51:59:00]. Currently, this is difficult, often leading to unwanted artifacts [52:21:00]. If models could operate semantically on learned causal abstractions, such fine-grained control would be significantly easier [52:40:00].

## Large Language Models and Causality
The debate around whether Large Language Models (LLMs) learn a "world model" essentially refers to whether they learn a Structural Causal Model (SCM) [55:00:00]. The [[causal_hierarchy_theorem | Causal Hierarchy Theorem]] (also known as Pearl's Causal Ladder) outlines three levels of causal questions:
1.  **Associational**: Observational statistics.
2.  **Interventional**: Estimating causal effects.
3.  **Counterfactual**: Reasoning across hypothetical worlds [55:50:00].

The theorem states that answering questions at a certain level requires assumptions at that same level [56:31:00]. While LLMs can empirically answer various causal questions (associational, interventional, counterfactual) [57:07:00], they are known to "hallucinate" [57:44:00]. The challenge is to ensure reliable causal reasoning [58:01:00].

For LLMs to reliably answer counterfactual questions, they must possess level three assumptions, which could be embedded in training data (unlikely for current models), model architecture, learned parameterization, or explicitly in the prompt [58:43:00]. Research aims to incorporate causal information into the Transformer architecture itself, providing theoretical guarantees similar to those obtained with latent variable models using do-calculus [01:00:08:00]. This would allow for more controlled and predictable generation, enabling users to "turn knobs" for specific, causally-informed adjustments to the output [01:01:56:00].

This direction in research seeks to improve models not just by scaling data, but by leveraging inherent structure within the data, such as code repositories with their history, commits, and executable behavior [01:04:18:00]. This approach focuses on "depth" of information rather than just "breadth" [01:05:17:00].

## Future of Causality
Dr. Ness believes that causal questions are enduring and will not be made obsolete by new deep learning architectures [01:16:11]. The future of causality, particularly its [[role_of_causal_discovery_and_reinforcement_learning | role of causal discovery and reinforcement learning]], lies in continued development of fundamental theory and its practical application.