---
title: Application of causal methods in industry
videoId: eCtLAt-6yps
---

From: [[causalpython]] <br/> 

Dr. Andrew Lawrence, Director of Research at Causalens, discusses the [[practical_applications_of_causal_methods | application of causal methods in industry]], distinguishing them from associative models and outlining challenges and solutions in real-world scenarios. <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>

## Dr. Andrew Lawrence's Journey to Causality

Dr. Andrew Lawrence, Director of Research at Causalens, holds a PhD from the University of Bath, where his research focused on Bayesian non-parametrics, which provided a foundational knowledge for understanding causality <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. His adventure with causality began after his PhD when he joined Causalens in late 2019, learning on the job for four years <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. He found that the concepts of causality came quite naturally to him, seeing the motivation and understanding the underlying math <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

He likens causality to "figuring out the right way to factor the joint distribution" <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>, focusing on the direction of influence or information flow between variables <a class="yt-timestamp" data-t="03:18:00">[03:18:18]</a>. His background in generative modeling with Bayesian non-parametrics helped him grasp the concept of factorizing data into a latent space and making distributional assumptions <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

## Causal vs. Associative Models

A key distinction between causal and associative models lies in their application domains and capabilities <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>.

### Safety-Critical vs. Creative Applications
Associative models, especially deep learning algorithms, are successful in domains where minimizing in-sample error is paramount, like creative tasks <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. Examples include generative AI for text (e.g., ChatGPT) or images (e.g., Midjourney, DALL-E) <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>, or facial recognition on social media <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>. In these cases, errors might be inconvenient but not catastrophic <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.

However, in safety-critical or high-value domains, such as healthcare, simply minimizing in-sample error is insufficient <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>. If a model chooses the wrong covariates, it might fit well in the training domain but fall apart when encountering out-of-sample data, leading to severe consequences like a lawyer hallucinating cases or a multi-million dollar marketing campaign having zero effect <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. [[application_of_causal_ai_in_marketing_and_business | Marketing]] is a domain where causal methods are highly valuable because professionals often don't scrutinize structural assumptions, so even a roughly correct causal structure can significantly improve outcomes <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

### Prediction vs. Decision Making
Another fundamental difference is between blind prediction and decision-making <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.

*   **Prediction:** For passively observing a stationary system, associative models can perform well <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
*   **Decision Making (Intervention):** When an intervention occurs (e.g., rebalancing a marketing budget, updating a manufacturing pipeline, changing a supply chain), the underlying data generating process shifts from an observational distribution to an interventional distribution <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>. Associative models are not expected to predict accurately in such scenarios because their underlying distribution has changed <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>. Causal models, by capturing the true data generating process, can generalize to unseen data and predict the outcomes of interventions <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

## Causal Lens's Approach to Industrial Applications

Causalens, following the Pearl School of Causality, primarily works with Structural Causal Models (SCMs) <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. They have developed their own SCM called "Causal Net" for client problems <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.

### Structural Causal Models (SCMs) and Causal Net
The core of Causalens's work involves using SCMs to model the functional dependencies between variables <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>. For example, if X and Z drive Y in a graph, the SCM learns the weights or relationships from X to Y and Z to Y <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>. They offer various aggregation functions at nodes (e.g., sum, sum with bias, higher-order interaction terms like polynomial regression) <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

Causalens employs different backends for training their SCMs:
*   **PyTorch engine:** For stochastic gradient descent <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.
*   **CVXPy:** For convex optimization, which imposes limits on functional dependencies <a class="yt-timestamp" data-t="13:11:00">[13:11:00]</a>.
*   **Pyro engine:** For distributional forecasting and inference on nodes, using stochastic variational inference to estimate posterior distributions <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>.

### Iterative Causal Discovery
A typical workflow at Causalens involves an iterative process with customers to define the underlying causal graph <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>.

1.  **Domain Knowledge Integration:** Customers often bring significant domain knowledge, sometimes even with partial graphs or variable hierarchies <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. For instance, age would be at the top of a topological sort, influencing factors like advertising channels, which then affect click-through rates <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>. This hierarchical knowledge substantially reduces the search space of possible graphs <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>.
2.  **Causal Discovery Algorithms:** Causalens uses a suite of [[causal_discovery_algorithms_and_realworld_applications | causal discovery algorithms]], including constraint-based, score-based, and continuous optimization methods <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>. They are not tied to a single method, selecting based on data type (e.g., score-based for continuous data, constraint-based with conditional mutual information for mixed data) <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
3.  **Graph Refinement:** Since causal discovery methods can only recover up to a Markov equivalence class of graphs, it's an iterative process of sampling from the graph space and discussing feasibility with the customer <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>. This also involves evaluating how well a proposed DAG and SCM fit the observed data <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>.

### SCM Training and Enhancements
Causalens has developed an SCM training approach inspired by Double ML (Debiased Machine Learning) to address potential bias in effect estimation <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>. Instead of naively training each node's function independently, which can lead to biased treatment effects due to confounding <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>, they build a "training graph." This defines the order in which nodes are trained and which data splits to use, ensuring unbiased effect estimates across any pair of variables in the SCM <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>. While this may slightly reduce predictive accuracy, it provides unbiased estimates for interventions <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>.

### Uncertainty Quantification
For uncertainty quantification, Causalens has integrated methods like Conformal Prediction using the open-source Mappy library <a class="yt-timestamp" data-t="18:55:00">[18:55:00]</a>. This is specifically used within their causal impact package, which focuses on time series data where there's a mix of interventional and observational data <a class="yt-timestamp" data-t="19:07:00">[19:07:00]</a>. The approach allows them to estimate the effect of an intervention by training an SCM pre-intervention, then applying the "do operator" to predict post-intervention <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>. They also use quantile regression and simple bootstrapping for uncertainty estimation <a class="yt-timestamp" data-t="20:15:00">[20:15:15]</a>.

## [[challenges_in_implementing_causal_analysis_in_practice | Challenges in Practical Implementation]]

### Data Range Extrapolation
A common challenge in industrial applications is that training data may not cover the full range of expected production data <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>. To address this, Causalens uses "shape-constrained edges" in their SCMs <a class="yt-timestamp" data-t="23:47:00">[23:47:00]</a>. These include:
*   **Linear Edge:** Predictable extrapolation to infinity <a class="yt-timestamp" data-t="23:52:00">[23:52:00]</a>.
*   **Monotonic Edge:** Forces a monotonic increase or decrease beyond the training domain, preventing unexpected behavior <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.
*   **Monotonic with Saturation:** Allows for an initial increase then a marginal increase, preventing blow-up <a class="yt-timestamp" data-t="24:17:00">[24:17:00]</a>.
*   **Piecewise Linear Edges:** Fits transition points within the training domain, then extrapolates linearly <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>.

These constraints build trust in the models as customers can inspect and understand the behavior of relationships, especially during "Black Swan" events <a class="yt-timestamp" data-t="24:44:00">[24:44:00]</a>. This is a way of incorporating expert knowledge in a less restrictive manner than specifying exact values or edges, making the model more parsimonious and trustworthy <a class="yt-timestamp" data-t="25:48:00">[25:48:00]</a>.

### Non-Stationarity and Unobserved Confounding
[[challenges_of_implementing_causality_in_research_and_industry | Challenges of implementing causality in research and industry]] often include dealing with complex systems that are highly non-stationary and where not all variables can be observed (unobserved confounding) <a class="yt-timestamp" data-t="55:55:00">[55:55:00]</a>. For supply chain management, Causalens might use time series tools like fractional differencing to stationarize data before applying standard [[causal_discovery_algorithms_and_realworld_applications | causal discovery techniques]] <a class="yt-timestamp" data-t="56:45:00">[56:45:00]</a>.

### Addressing Hidden Confounding and Identifiability
[[causal_tools_and_methodologies_in_business_applications | Causal tools and methodologies in business applications]] are not always limited to directed acyclic graphs (DAGs) <a class="yt-timestamp" data-t="52:53:00">[52:53:00]</a>. Causal discovery methods can resolve up to a Markov equivalence class of graphs, which can be encoded into mixed graph types like completed partial directed acyclic graphs (CPDAGs) or partial ancestral graphs (PAGs) <a class="yt-timestamp" data-t="53:10:00">[53:10:00]</a>. Inference can be performed directly on these mixed graph types without needing to resolve to a single DAG <a class="yt-timestamp" data-t="53:46:00">[53:46:00]</a>. This is important when unobserved confounding is present, as PAGs are the typical output of methods like Fast Causal Inference (FCI) <a class="yt-timestamp" data-t="53:36:00">[53:36:00]</a>.

Incorporating prior knowledge, such as defining source or sink nodes, can significantly reduce the search space for [[causal_discovery_algorithms_and_realworld_applications | causal discovery algorithms]] <a class="yt-timestamp" data-t="48:01:00">[48:01:00]</a>. For example, explicitly defining a guaranteed source node (e.g., age) and a sink node (e.g., click-through rates) can reduce the number of score computations by half <a class="yt-timestamp" data-t="48:12:00">[48:12:00]</a>. Even partial information about an edge (e.g., a known edge, a forbidden edge) can lead to substantial speed-ups <a class="yt-timestamp" data-t="49:41:00">[49:41:00]</a>.

## Industry Use Cases

Causal methods are applied across various industries to solve specific problems:

### Manufacturing
In manufacturing, especially with physical systems like assembly lines, the underlying system is highly constrained, making it easier to model information flow <a class="yt-timestamp" data-t="57:31:00">[57:31:00]</a>. Here, [[causality_and_its_role_in_industrial_and_manufacturing_processes | causality and its role in industrial and manufacturing processes]] is often used for root cause analysis, identifying which step in a pipeline leads to anomalous outcomes like bad yield rates <a class="yt-timestamp" data-t="58:20:00">[58:20:00]</a>.

### Supply Chain Management
Supply chain management presents challenges due to its complexity, lack of sufficiency (not all variables can be captured), and high non-stationarity <a class="yt-timestamp" data-t="55:55:00">[55:55:00]</a>. Causal methods help in identifying interventions that can lead to marginal gains and understanding drivers of key performance indicators (KPIs) like throughput or lead times <a class="yt-timestamp" data-t="58:06:00">[58:06:00]</a>.

### Marketing
[[application_of_causal_ai_in_marketing_and_business | Causal AI in business applications]] for marketing campaigns can help identify optimal interventions or sets of interventions to maximize revenue, by understanding which levers to pull and at what level <a class="yt-timestamp" data-t="54:46:00">[54:46:00]</a>. This moves beyond simply predicting outcomes to recommending actions <a class="yt-timestamp" data-t="54:46:00">[54:46:00]</a>.

## Key Takeaways for Causal Practitioners

*   **Focus on the Goal:** Practitioners don't always need to find a full DAG for every problem; it depends on what specific causal effect they are trying to estimate <a class="yt-timestamp" data-t="32:31:00">[32:31:00]</a>.
*   **Validation:** For any model, including causal models, a validation phase with training, validation, and test splits is crucial <a class="yt-timestamp" data-t="29:39:00">[29:39:00]</a>. Predictive information can be assessed, and if interventional data is available, estimated effects can be compared to measured ones <a class="yt-timestamp" data-t="30:07:00">[30:07:00]</a>.
*   **Beware of Implicit Assumptions:** Complex "black-box" models often make very strong, implicit assumptions about the data generating process, which can be detrimental if those assumptions are wrong <a class="yt-timestamp" data-t="01:17:29">[01:17:29]</a>. Explicitly defining causal structures (e.g., with DAGs) makes assumptions transparent and can simplify the model while improving trust <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
*   **Modularity and Open Source:** [[evaluating_and_explaining_causal_models_in_industry | Evaluating and explaining causal models in industry]] is aided by modular packages and the ability to integrate open-source tools. Causalens's platform allows users to leverage their packages alongside open-source libraries (e.g., G-Castle for causal discovery, scikit-uplift for uplift metrics), fostering flexible workflows and accelerating development <a class="yt-timestamp" data-t="01:19:53">[01:19:53]</a>.

## Resources
*   **Online Course:** Brady Neal's online tutorial for causality <a class="yt-timestamp" data-t="01:13:25">[01:13:25]</a>.
*   **Textbooks:**
    *   *Elements of Causal Inference* <a class="yt-timestamp" data-t="01:13:41">[01:13:41]</a>
    *   *The Book of Why* by Judea Pearl <a class="yt-timestamp" data-t="01:13:48">[01:13:48]</a>
    *   Christopher Bishop's *Machine Learning and Pattern Recognition* <a class="yt-timestamp" data-t="01:11:44">[01:11:44]</a>
*   **Causalens Resources:**
    *   Research page: [causalens.com](http://causalens.com) <a class="yt-timestamp" data-t="01:26:58">[01:26:58]</a>
    *   Learning videos: YouTube <a class="yt-timestamp" data-t="01:27:22">[01:27:22]</a>
    *   Open-source packages: GitHub ([github.com/Cazallens](http://github.com/Cazallens)) <a class="yt-timestamp" data-t="01:28:08">[01:28:08]</a>, including Dara (front-end app building) and their Causal Graph library <a class="yt-timestamp" data-t="01:27:31">[01:27:31]</a>.