---
title: Structural causal models and graph theory
videoId: eCtLAt-6yps
---

From: [[causalpython]] <br/> 

## Introduction to Causal Models
Causality aims to capture the true data generating process, specifically understanding the direction of influence or information flow between variables <a class="yt-timestamp" data-t="03:01:14">[03:01:14]</a>. This involves figuring out the right way to factorize the joint distribution of observed data <a class="yt-timestamp" data-t="02:16:04">[02:16:04]</a>. While Bayesian non-parametrics, which focuses on generative modeling and learning latent variable models, doesn't directly tie into causality, it provides foundational knowledge for understanding these concepts <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>.

## Distinction from Associative Models
A fundamental difference between causal and associative models lies in their application: prediction versus decision-making <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. Associative models perform well in blind prediction scenarios where a system is passively observed and assumed to be stationary over time <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. However, when an intervention occurs—such as rebalancing a marketing budget or changing a manufacturing pipeline—the underlying data generating process shifts from an observational to an interventional distribution <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>. In such cases, an associative model is expected to fail because its underlying distribution has changed <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

The choice between these models often depends on whether the application is "safety critical" or "high value" <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>. For creative tasks like generating text or images, where errors have lower risk (e.g., GitHub Copilot, Midjourney), associative models can be incredibly useful <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. However, for applications like healthcare or multi-million dollar marketing campaigns, minimizing in-sample error alone is insufficient, and understanding the causal drivers is crucial for reliable generalization to unseen data <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.

## Building and Refining [[structural_causal_models_and_causal_discovery | Causal Models]] at CausalLens
At CausalLens, the focus is on the Pearl School of causality, working extensively with [[structural_causal_models_and_causal_discovery | Structural Causal Models]] (SCMs) <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. They have developed their own SCM, called CausalNet, to address customer problems <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>.

### Iterative Approach in Building Causal Models
A typical workflow involves an [[iterative_approach_in_building_causal_models | iterative approach]] with the customer to define the underlying causal graph <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. Customers often provide domain knowledge, sometimes even with full graphs or understanding of variable hierarchies (e.g., age driving other factors, channels of intervention like Instagram, and responses like click-through rates) <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. This initial ordering helps significantly reduce the search space of possible graphs <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>.

### [[structural_causal_models_and_causal_discovery | Causal Discovery]] Algorithms
CausalLens employs a suite of [[structural_causal_models_and_causal_discovery | causal discovery]] algorithms, including:
*   **Constraint-based methods** <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>
*   **Score-based methods** <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>
*   **Continuous optimization** <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>
*   **Model-based methods** (e.g., LinGAM) <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>

The choice of method depends on data characteristics (e.g., score-based exact search for continuous data, constraint-based methods with conditional mutual information for mixed categorical and continuous data) <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. Any [[structural_causal_models_and_causal_discovery | causal discovery]] method can only recover up to a Markov equivalence class of graphs, not a single DAG <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>. The iterative process involves sampling from this space and consulting with the customer to find a feasible graph that matches the observed data <a class="yt-timestamp" data-t="12:34:00">[12:34:00]</a>.

### Learning Functional Forms
After discovering the graph, a [[structural_causal_models_and_causal_discovery | Structural Causal Model]] is fitted to learn the functional forms of connections between variables <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. CausalLens uses various backends for this, including:
*   PyTorch (stochastic gradient descent) <a class="yt-timestamp" data-t="13:07:00">[13:07:07]</a>
*   CVXPY (convex optimization) <a class="yt-timestamp" data-t="13:11:00">[13:11:00]</a>
*   Pyro (for distributional forecasting/inference) <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>

These engines learn parameters like weights in a linear association (e.g., from X to Y) and support different aggregations at nodes (e.g., sum, sum with bias, higher-order interaction terms) <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.

One improvement built into their SCM implementation is a Double ML-inspired training routine <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>. While Double ML typically focuses on specific treatment-outcome pairs, CausalLens adapted it to train the entire SCM, allowing for unbiased effect estimates between any pair of variables within the model <a class="yt-timestamp" data-t="30:45:00">[30:45:00]</a>. This involves building a training graph that defines the order and data splits for training nodes, though it currently limits some functional dependencies to be linear <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>.

## Handling Challenges and Improving Robustness
### Out-of-Sample Extrapolation
A common challenge is when production data falls outside the training range <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>. To address this, CausalLens uses "shape-constrained edges" which force predictable extrapolation behavior <a class="yt-timestamp" data-t="23:36:00">[23:36:00]</a>. Examples include:
*   **Linear edges:** Predictable behavior as input moves to infinity <a class="yt-timestamp" data-t="23:52:00">[23:52:00]</a>.
*   **Monotonic edges:** Ensures continuous increase/decrease from the training domain <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.
*   **Monotonic with saturation:** Prevents blow-up by marginally increasing after a certain point <a class="yt-timestamp" data-t="24:17:00">[24:17:00]</a>.
*   **Piecewise linear edges:** Fits transition points within the training domain, then behaves linearly outside <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>.

These constraints build trust in the models as their behavior beyond observed data is known, unlike complex neural networks which can behave randomly in areas with no data <a class="yt-timestamp" data-t="24:44:00">[24:44:00]</a>.

### Incorporating Expert Knowledge
Expert knowledge can be incorporated to simplify models and increase trust <a class="yt-timestamp" data-t="25:48:00">[25:48:00]</a>. This doesn't mean imposing exact values or edges, but rather defining general properties (e.g., monotonicity) or hierarchies that restrict the search space <a class="yt-timestamp" data-t="26:01:00">[26:01:00]</a>. For example, knowing that "age" is a source node (nothing drives it) or "click-through rate" is a sink node (nothing is measured downstream from it) can substantially reduce the number of score computations in [[structural_causal_models_and_causal_discovery | causal discovery]] by half <a class="yt-timestamp" data-t="48:12:00">[48:12:00]</a>.

### Addressing Hidden Confounding and Non-Stationarity
Complex systems like supply chains often lack causal sufficiency, meaning not all interacting variables can be observed <a class="yt-timestamp" data-t="55:57:00">[55:57:00]</a>. Such systems can also be highly non-stationary <a class="yt-timestamp" data-t="56:08:00">[56:08:00]</a>. To address non-stationarity, techniques from time series analysis like fractional differences are used to preprocess data before applying standard [[structural_causal_models_and_causal_discovery | causal discovery]] methods <a class="yt-timestamp" data-t="56:47:00">[56:47:00]</a>.

While directed acyclic graphs (DAGs) can seem limiting due to the assumption of no hidden confounding, other mixed graph types like Completed Partial Directed Acyclic Graphs (CPDAGs), Maximal Ancestral Graphs (MAGs), and Partial Ancestral Graphs (PAGs) can encode Markov equivalence classes and allow for inference even with unobserved confounding <a class="yt-timestamp" data-t="53:08:00">[53:08:00]</a>.

## Specific Algorithms and Techniques
### Time Series [[structural_causal_models_and_causal_discovery | Causal Discovery]]
Research at CausalLens has explored [[structural_causal_models_and_causal_discovery | time series causal discovery]] by generating synthetic data to validate the sensitivity of methods to violated assumptions like linearity or Gaussian noise <a class="yt-timestamp" data-t="35:29:00">[35:29:00]</a>. This includes comparing vector autoregressive versions of LinGAM, NoTears, and PCMCI using different conditional independence testers, often evaluated by structural Hamming distance <a class="yt-timestamp" data-t="35:51:00">[35:51:00]</a>. This internal benchmarking helps understand how methods perform in real-world scenarios where theoretical guarantees (e.g., no hidden confounding, perfect conditional independence testers) are rarely met <a class="yt-timestamp" data-t="36:38:00">[36:38:00]</a>.

### A* Algorithm for [[structural_causal_models_and_causal_discovery | Causal Discovery]]
CausalLens has worked on extending the A* pathfinding algorithm for [[structural_causal_models_and_causal_discovery | causal discovery]] in continuous data <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a>. This exact search score-based method uses the Bayesian Information Criterion (BIC) for each node, assuming linearity and Gaussian additive noise, and causal sufficiency <a class="yt-timestamp" data-t="42:53:00">[42:53:00]</a>. The original papers (Triplet A*, A* Superstructure, Local A*) aim for scalability to hundreds of nodes <a class="yt-timestamp" data-t="42:23:00">[42:23:23]</a>.

### Graphical Lasso
Graphical Lasso is used as an initial filtering step in A* Superstructure to obtain a sparse skeleton (undirected graph) as a starting point for [[structural_causal_models_and_causal_discovery | causal discovery]] <a class="yt-timestamp" data-t="44:34:00">[44:34:00]</a>. It estimates a sparse representation of the precision matrix, assuming continuous variables are sampled from a centered multivariate Gaussian <a class="yt-timestamp" data-t="44:57:00">[44:57:00]</a>. This helps prune the potential parent graphs before running the A* search <a class="yt-timestamp" data-t="46:38:00">[46:38:00]</a>.

## Applications and Practical Considerations
[[applications_of_causal_models_in_biology_and_ai | Causal models]] are applied in various complex scenarios:
*   **Supply Chain Management:** Challenges include non-sufficiency (unobserved variables) and high non-stationarity <a class="yt-timestamp" data-t="55:51:00">[55:51:00]</a>. Focus is often on predictive capabilities and identifying interventions with marginal gains <a class="yt-timestamp" data-t="58:10:00">[58:10:00]</a>.
*   **Manufacturing:** This domain often works well with out-of-the-box [[structural_causal_models_and_causal_discovery | causal models]] due to more constrained physical systems (e.g., assembly lines, known component flows) <a class="yt-timestamp" data-t="57:31:00">[57:31:00]</a>. Use cases frequently involve root cause analysis for anomalous outcomes like poor yield rates <a class="yt-timestamp" data-t="58:24:00">[58:24:00]</a>.

When working with [[structural_causal_models_and_causal_discovery | causal graphs]], it's important to remember that:
*   The field is too vast for anyone to be an expert on everything; focus on areas of interest <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>.
*   [[evaluation_and_systematic_testing_of_causal_models | Evaluation]] and testing are crucial, including training, validation, and test splits to assess predictive information or estimated effects against interventional data <a class="yt-timestamp" data-t="29:39:00">[29:39:00]</a>.
*   A full DAG isn't always necessary; sometimes only local structure or drivers of a specific target variable are needed <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a>.
*   Causality can be scale-specific (time or spatial), meaning a seemingly cyclic effect at one resolution might be lagged at a finer resolution <a class="yt-timestamp" data-t="32:55:00">[32:55:00]</a>.
*   The "fear of the wrong DAG" can be mitigated by leveraging domain knowledge to reduce the search space and by validating models against data <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>.

## Product Philosophy and Modularity
CausalLens offers a cloud platform for decision-making that allows users to launch Jupyter Lab sessions with access to their packages, but also encourages integration with open-source tools <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. Their packages are designed to be modular and use-case agnostic, with a shared API to allow components (e.g., graph discovery, SCM training, decision intelligence engines like algorithmic recourse or root cause analysis) to be plugged in together <a class="yt-timestamp" data-t="01:20:48">[01:20:48]</a>. This enables users to build workflows combining familiar open-source methods with CausalLens's offerings <a class="yt-timestamp" data-t="01:23:50">[01:23:50]</a>.

The future of causality is seen in any domain where high-value or safety-critical decisions, actions, or optimal treatments are required, where errors are detrimental to life or revenue <a class="yt-timestamp" data-t="01:26:04">[01:26:04]</a>.