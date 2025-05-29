---
title: Causality in marketing and decisionmaking
videoId: eCtLAt-6yps
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast featured Dr. Andrew Lawrence, Director of Research at Calin, to discuss his work in [[causality_in_science_and_industry | causality]] and [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]], with a particular focus on its [[applications_of_causal_models_in_business_and_marketing | applications in business and marketing]] and [[causal_inference_and_decision_making | decision making]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Andrew Lawrence's Background and Journey to Causality

Dr. Andrew Lawrence's journey into [[causality_and_causal_models | causality]] began after his PhD from the University of Bath <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. His PhD focused on Bayesian non-parametrics <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, which, while not directly tied to [[causality_and_causal_models | causality]], provided a strong foundational knowledge to quickly grasp the topics <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. He describes [[causality_and_causal_models | causality]] as "figuring out the right way to factor the joint distribution" <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>, emphasizing the importance of understanding the "true data generating process" or "information flow" between variables <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This focus on thinking about structures and conditional dependencies was transferable from his generative modeling and latent variable model research <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

## Associative vs. Causal Models

A key distinction in [[causality_in_marketing | business and marketing]] is between associative (or predictive) models and causal models <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Prediction vs. Decision-Making
[[machine_learning_versus_causal_inference_for_decisionmaking | Machine learning versus causal inference for decision-making]] is a crucial comparison <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Associative models excel at "blind prediction" or passively observing a system <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. However, they fail when an intervention occurs because the underlying data generating process changes, leading to a shift from an observational to an interventional distribution <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>, <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

*   **Associative Models**:
    *   Minimize in-sample error <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   Can overfit and fail to generalize to out-of-sample data if covariates aren't truly driving the target <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   Examples: Generative AI (ChatGPT, Midjourney) for creative tasks where errors are less critical <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Facebook's facial recognition; if incorrect, users can correct it without major repercussions <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

*   **Causal Models**:
    *   Essential for [[causal_inference_and_decision_making | decision making]] and generalization to unseen data <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
    *   Crucial in high-value or safety-critical domains like healthcare, where minimizing in-sample error isn't sufficient <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
    *   [[causality_in_marketing | Causality in marketing]] is critical for multi-million dollar campaigns where models predicting advertising influence need to be accurate to prevent loss of trust <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

## Causal Lens's Approach to Causal Models

Calin, where Dr. Lawrence works, follows the Pearl School of [[causality_and_causal_models | causality]] and focuses on Structural Causal Models (SCMs) <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Structural Causal Models (SCMs)
Calin developed its own SCM, called CausalNet <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. A typical workflow for applying SCMs involves:
1.  **Iterating on the Graph with Customers**: Incorporating domain knowledge, especially regarding the hierarchy of variables (e.g., age influencing marketing channels, which influence click-through rate) <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>, <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This ordering helps substantially reduce the search space of possible graphs <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
2.  **Causal Discovery Algorithms**: Utilizing a suite of algorithms including:
    *   Constraint-based <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>
    *   Score-based (e.g., for all continuous data) <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>, <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>
    *   Continuous optimization <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>
    *   Model-based (e.g., LinGAM) <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>
    These methods can only recover a Markov equivalence class of graphs, so multiple iterations with customer input are often needed <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
3.  **Fitting the SCM**: CausalNet uses different backends for training the functional forms of connections between variables <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>, <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>:
    *   PyTorch (stochastic gradient descent) <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>
    *   CVXPy (convex optimization, with limitations on functional dependencies) <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>
    *   Pyro (for distributional inference using stochastic variational inference) <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>

### Edge Functions and Extrapolation
Calin employs "shape-constrained edges" to ensure models extrapolate reliably beyond the training domain <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>. This includes:
*   **Linear Edges**: Predictable extrapolation <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>.
*   **Monotonic Edges**: Force a continuous increase or decrease, preventing arbitrary loops <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.
*   **Monotonic with Saturation**: Ensures marginal increases do not "blow up to infinity" <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.
*   **Piecewise Linear Edges**: Linear association away from training domain <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

This approach builds trust in the models as customers can inspect relationships and understand how the model will behave in extreme scenarios (e.g., Black Swan events) <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>, <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. It allows for the incorporation of expert knowledge in a less restrictive way, simplifying the model while ensuring trust <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>, <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.

## Addressing Challenges in Causal Inference

### Unbiased Effect Estimators
Calin developed a method to train SCMs using the motivation behind "double machine learning" (DML) <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. DML typically applies to specific treatment-outcome pairs but Calin extended it to learn functional dependencies across the entire SCM, enabling unbiased estimates of treatment effects between *any* pair of variables within the model <a class="yt-timestamp" data-t="00:30:45">[00:30:45]</a>, <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>. This involves a "training graph" that defines the order of node training and data splitting to prevent bias propagation <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

### Uncertainty Quantification
While Bayesian inference is a go-to for uncertainty quantification <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>, Calin has also explored conformal prediction, integrating it into their causal impact package <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>, <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. This package, which historically uses Bayesian State-Space models, now uses conformal prediction for uncertainty estimations in time series data with mixed interventional and observational periods <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>, <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

### Dealing with Incorrect DAGs
The "fear of not finding the perfect DAG" is common for those new to [[causality_and_causal_models | causality]] <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>, <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>. Dr. Lawrence advises:
*   **Validation**: Use training, validation, and test splits to assess predictive information (for rung one problems) or compare estimated effects with interventional data <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>.
*   **Problem-Specific Focus**: A full DAG is not always necessary <a class="yt-timestamp" data-t="00:32:34">[00:32:34]</a>. The focus should be on the relevant treatment effect.
*   **Prior Knowledge**: Incorporating domain knowledge (e.g., hierarchical ordering of variables, known or forbidden edges) significantly reduces the search space for causal graphs, which is an NP-hard problem <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>, <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>, <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>. For example, defining source nodes (like age) and sink nodes (like click-through rates) can halve the number of score computations in algorithms like A* <a class="yt-timestamp" data-t="00:48:12">[00:48:12]</a>.

### Scalability of Causal Discovery
One project involved extending the A* pathfinding algorithm for causal discovery, aiming for scalability to hundreds of nodes <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>, <a class="yt-timestamp" data-t="00:42:40">[00:42:40]</a>. The A* method, an exact search score-based method using Bayesian Information Criterion (BIC), assumes linearity and Gaussian additive noise <a class="yt-timestamp" data-t="00:42:53">[00:42:53]</a>, <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>. An extension, A* superstructure, uses graphical lasso as an initial filtering step to prune the potential parent graphs, reducing the search space <a class="yt-timestamp" data-t="00:44:34">[00:44:34]</a>, <a class="yt-timestamp" data-t="00:47:41">[00:47:41]</a>.

### Limitations of DAGs
The formalism of Directed Acyclic Graphs (DAGs) can seem limiting, especially with hidden confounding in complex systems like [[causality_in_marketing | marketing]] or social phenomena <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>, <a class="yt-timestamp" data-t="00:52:34">[00:52:34]</a>. However, identifiability in causal terms is not limited to DAGs <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>. Causal discovery methods can resolve up to a Markov equivalence class of graphs, which can be encoded into mixed graph types like Completed Partial Directed Acyclic Graphs (CPDAGs) or Partial Ancestral Graphs (PAGs) <a class="yt-timestamp" data-t="00:53:13">[00:53:13]</a>, <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>. Inference can be performed directly on these mixed graph types <a class="yt-timestamp" data-t="00:53:45">[00:53:45]</a>.

### Algorithmic Recourse
Beyond identifying effects, Calin also works on problems like algorithmic recourse, where the goal is to determine the optimal set of interventions to reverse an unfavorable decision or maximize revenue <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>, <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

## Real-world Applications and Challenges

Dr. Lawrence has worked on various real-world [[applications_of_causal_models_in_business_and_marketing | applications of causal models in business and marketing]]:

*   **Supply Chain Management**:
    *   **Challenges**: Lack of causal sufficiency (unmeasured variables), highly non-stationary data, and varying scales of effects <a class="yt-timestamp" data-t="00:55:55">[00:55:55]</a>.
    *   **Approach**: Extensive pre-processing (e.g., fractional differences) to stationarize data before applying standard causal discovery techniques <a class="yt-timestamp" data-t="00:56:45">[00:56:45]</a>, <a class="yt-timestamp" data-t="00:57:19">[00:57:19]</a>. Focus on interventions for marginal gains <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.
*   **Manufacturing**:
    *   **Advantages**: Often has an underlying physical system with constrained component flows, making information flow easier to model <a class="yt-timestamp" data-t="00:57:36">[00:57:36]</a>, <a class="yt-timestamp" data-t="00:57:58">[00:57:58]</a>.
    *   **Applications**: Primarily root cause analysis for anomalous outcomes like poor yield rates <a class="yt-timestamp" data-t="00:58:20">[00:58:20]</a>.

[[causal_reasoning_in_decisionmaking | Causal reasoning in decision-making]] is greatly aided by presenting information as a causal graph, which intuitively conveys how information flows through a system and the assumptions made <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>, <a class="yt-timestamp" data-t="01:16:10">[01:16:10]</a>.

## General Advice and Resources

Dr. Lawrence emphasizes that one doesn't need to be an expert on everything in [[causality_and_causal_models | causality]] or [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>. The key skills are quickly distilling information, understanding fundamental methods, and rapid prototyping <a class="yt-timestamp" data-t="00:59:39">[00:59:39]</a>, <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. Motivation should guide one's focus <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.

### Recommended Resources for Learning Causality
*   **Brady Neal's tutorial/online course**: Very approachable <a class="yt-timestamp" data-t="01:13:25">[01:13:25]</a>.
*   **"Elements of Causal Inference" book**: More advanced <a class="yt-timestamp" data-t="01:13:41">[01:13:41]</a>.
*   **"The Book of Why" by Judea Pearl**: More narrative and contextual <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>.
*   **Christopher Bishop's "Machine Learning and Pattern Recognition"**: Good for fundamental concepts <a class="yt-timestamp" data-t="01:11:44">[01:11:44]</a>.
*   Numerous online resources, summer school lectures, papers, and textbooks <a class="yt-timestamp" data-t="01:14:06">[01:14:06]</a>.

## The Future of Causality

Dr. Lawrence firmly believes that the future is causal, especially in domains where decisions are high-value or safety-critical <a class="yt-timestamp" data-t="01:26:04">[01:26:04]</a>. In scenarios where errors are detrimental to life or revenue, [[importance_of_understanding_causal_inference_for_decision_making | understanding causal inference for decision making]] is essential <a class="yt-timestamp" data-t="01:26:12">[01:26:12]</a>.

> "You're essentially going to overfit...and then as soon as anything changes slightly, if you intervene, you're representing the completely wrong distribution." <a class="yt-timestamp" data-t="01:18:51">[01:18:51]</a>

## Causal Lens Product Philosophy

Causal Lens provides a cloud platform for [[causal_inference_and_decision_making | decision making]] that allows users to launch Jupiter Lab sessions and utilize their proprietary packages <a class="yt-timestamp" data-t="01:20:04">[01:20:04]</a>.
*   **Modularity**: Packages are designed to be modular and use-case agnostic, avoiding a monolithic solution <a class="yt-timestamp" data-t="01:20:48">[01:20:48]</a>.
*   **Open-Source Integration**: Users can easily integrate open-source tools (e.g., Huawei's G-Castle, networkX, PyTorch, scikit-uplift) into their workflows <a class="yt-timestamp" data-t="01:20:17">[01:20:17]</a>, <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a>. This allows for a flexible "Melting Pot" environment where data scientists can use familiar tools alongside Causal Lens's offerings <a class="yt-timestamp" data-t="01:23:55">[01:23:55]</a>, <a class="yt-timestamp" data-t="01:24:14">[01:24:14]</a>.
*   **Maintained and Documented**: The company aims to provide well-documented, well-tested, and frequently updated implementations of promising causal techniques <a class="yt-timestamp" data-t="01:21:20">[01:21:20]</a>.

Causal Lens is also moving more into open-source contributions, including their front-end app-building framework, Dara, and their Causal Graph library <a class="yt-timestamp" data-t="01:27:31">[01:27:31]</a>, <a class="yt-timestamp" data-t="01:27:58">[01:27:58]</a>. Their GitHub repository also contains code from papers like the time series causal discovery work <a class="yt-timestamp" data-t="01:28:11">[01:28:11]</a>. Dr. Lawrence encourages continuous communication within the causal Python community to spark new ideas <a class="yt-timestamp" data-t="01:25:57">[01:25:57]</a>.