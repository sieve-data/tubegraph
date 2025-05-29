---
title: Challenges in causal discovery and uncertainty quantification
videoId: eCtLAt-6yps
---

From: [[causalpython]] <br/> 

Causal inference, a field focused on understanding cause-and-effect relationships, faces significant [[Challenges of implementing causality in research and industry | challenges]] in both discovering causal structures and quantifying the uncertainty associated with these findings. Dr. Andrew Lawrence, Director of Research at Causal Lens, discusses these hurdles and the approaches his team takes to address them <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.

## Causal Discovery: Unveiling the Data Generating Process

At its core, causality aims to identify the true data-generating process, understanding the direction of influence and information flow between variables <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a> <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a> <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. This often means moving beyond mere prediction to enable decision-making based on interventions <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

### Methods and Approaches
Causal discovery involves identifying the underlying graph structure (a Directed Acyclic Graph, or DAG) that represents these relationships. Common approaches include:
*   **Constraint-based methods** <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>
*   **Score-based methods** <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>
*   **Continuous optimization methods** <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>
*   **Model-based methods** (e.g., LinGAM) <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>

At Causal Lens, the process of discovering these causal graphs is highly iterative, often involving collaboration with domain experts <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>. This iterative process combines customer domain knowledge with a suite of [[Causal discovery and learning | causal discovery algorithms]] <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

### Challenges in Causal Discovery
Several [[Challenges in causal machine learning compared to traditional methods | challenges]] impede effective causal discovery:
*   **Markov Equivalence Class**: Causal discovery algorithms can typically only recover a Markov equivalence class of graphs, not a single, definitive DAG <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. This means multiple graph structures could explain the observed data.
*   **Data Types**: The choice of algorithm can depend on the data type. Score-based exact search works well for all continuous data, but constraint-based methods (like those using conditional mutual information) might be better for mixed categorical and continuous data <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.
*   **Lack of Ground Truth**: A significant problem in the [[Advancements in probabilistic programming and causal discovery | causal discovery literature]] is the scarcity of real-world datasets with known ground truth causal structures <a class="yt-timestamp" data-t="39:00:00">[39:00:00]</a>. This often leads to benchmarking against simulated dags, which may not reflect real-world properties <a class="yt-timestamp" data-t="38:08:00">[38:08:00]</a>.
*   **Assumptions of Algorithms**: Many algorithms, like the PC algorithm, assume no hidden confounding and perfect conditional independence testers <a class="yt-timestamp" data-t="36:55:00">[36:55:00]</a>. In reality, hidden variables are almost always present, and conditional independence cannot be measured with 100% certainty <a class="yt-timestamp" data-t="37:00:00">[37:00:00]</a>. Assumptions like linearity and Gaussian additive noise can also limit applicability <a class="yt-timestamp" data-t="44:05:00">[44:05:05]</a>.
*   **Scalability**: Discovering Bayesian networks is an NP-hard problem, with the space of graphs growing super-exponentially with the number of nodes <a class="yt-timestamp" data-t="49:57:00">[49:57:00]</a>. This makes scaling to hundreds of nodes computationally intensive.
*   **Implicit Assumptions**: Modern data culture sometimes promotes complex architectures without explicit consideration of data origins or underlying meaning <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. This leads to implicit, often strong, assumptions about the data-generating process, which can be detrimental if incorrect <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

### Strategies to Address Discovery Challenges
*   **Incorporating Domain Knowledge**: Expert knowledge can significantly reduce the search space. Examples include:
    *   **Hierarchical Knowledge**: Defining a hierarchy of variables (e.g., age at the top, marketing channel further down) can substantially restrict possible graphs <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a> <a class="yt-timestamp" data-t="28:13:00">[28:13:00]</a>.
    *   **Source/Sink Nodes**: Identifying guaranteed source nodes (no incoming edges) or sink nodes (no outgoing edges) can halve the number of score computations needed for algorithms like A* <a class="yt-timestamp" data-t="48:12:00">[48:12:00]</a>.
    *   **Known/Forbidden Edges**: Explicitly encoding known or forbidden edges prunes the search space <a class="yt-timestamp" data-t="47:06:00">[47:06:00]</a> <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>.
*   **Suite of Algorithms**: Instead of relying on a single method, using a family of [[Causal discovery and learning | causal discovery algorithms]] allows for comparing different results and finding what works best for specific data characteristics <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a> <a class="yt-timestamp" data-t="28:46:00">[28:46:00]</a>.
*   **Focus on Local Structure**: For many problems, it's not necessary to find a full DAG for all variables; understanding specific local structures around a target variable can be sufficient <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a> <a class="yt-timestamp" data-t="50:39:00">[50:39:00]</a>.
*   **Adapting Algorithms**: Modifying existing algorithms (e.g., for time series causal discovery) to generate synthetic data for validating their sensitivity to broken assumptions helps understand their real-world applicability <a class="yt-timestamp" data-t="35:29:00">[35:29:00]</a>. An example is the use of the [[Causal discovery and learning | A* algorithm]] (Triplet A*, A* superstructure, Local A*) for exact search on continuous data, combined with graphical lasso for initial parent set filtering <a class="yt-timestamp" data-t="42:00:00">[42:00:00]</a> <a class="yt-timestamp" data-t="44:50:00">[44:50:00]</a>.
*   **Time and Spatial Scale**: Causality can be scale-specific. A cyclic relationship at a fine time scale might appear as a direct effect at a coarser scale, and models can be adapted to this resolution <a class="yt-timestamp" data-t="32:55:00">[32:55:00]</a>.

## Uncertainty Quantification

Understanding the uncertainty in causal estimates is crucial, especially in safety-critical or high-value domains.

### Methods for Uncertainty Quantification
*   **Bayesian Inference**: Historically, Bayesian non-parametrics offered a strong foundation for uncertainty quantification <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a> <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   **Conformal Prediction**: More recently, [[Uncertainty quantification in causal machine learning | conformal prediction]] has emerged as a popular framework, demonstrating successful integration with causal methods to provide valid intervals <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a> <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
    *   Causal Lens has integrated conformal prediction into its [[Uncertainty quantification in causal machine learning | causal impact package]], which also uses quantile regression and bootstrapping for uncertainty estimation in time series analysis <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a> <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.
*   **Double ML (Debiased Machine Learning)**: This technique helps obtain unbiased effect estimators by splitting data and regressing residuals, mitigating bias produced as an artifact of the method <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a> <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Causal Lens has developed a method to train Structural Causal Models (SCMs) inspired by Double ML, ensuring unbiased estimates for any pair of treatment-outcome variables within the SCM <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. This, however, might lead to a slight loss in predictive accuracy <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

### Challenges in Uncertainty Quantification
*   **Time Series Data**: Applying conformal prediction to time series data presents challenges as its original implementations focused on IID (independent and identically distributed) data, and further research is needed for non-stationary scenarios <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a> <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **Balancing Bias and Estimation**: There's often a trade-off between minimizing causal bias and achieving optimal statistical estimation <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

## Broader Practical Challenges and Solutions

### Generalization and Extrapolation
Associative models, while good at predicting within the training domain, often fail when intervening in a system or stepping outside the training data, as the underlying data-generating process changes <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a> <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. Causal models, by focusing on the true drivers, aim for better generalization <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

To address extrapolation beyond observed data ranges, Causal Lens uses **shape-constrained edges** in their SCMs <a class="yt-timestamp" data-t="23:36:00">[23:36:00]</a>. These include:
*   **Monotonic edges**: Force the relationship to increase or decrease monotonically <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.
*   **Monotonic with saturation**: Increases initially then marginally, preventing blow-up to infinity <a class="yt-timestamp" data-t="24:17:00">[24:17:00]</a>.
*   **Piecewise linear edges**: Linear association beyond the training domain <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>.

These constraints build trust in models by ensuring predictable behavior in unseen scenarios, unlike complex neural networks that can behave randomly outside the training domain <a class="yt-timestamp" data-t="24:44:00">[24:44:00]</a>.

### [[Challenges in implementing causal analysis in practice | Complexity of Real-World Systems]]
*   **Sufficiency and Non-stationarity**: In complex systems like supply chains, it's impossible to capture all interacting variables (lack of causal sufficiency) <a class="yt-timestamp" data-t="55:57:00">[55:57:00]</a>. Data is often highly non-stationary, requiring techniques like fractional differencing to make it stationary for causal discovery <a class="yt-timestamp" data-t="56:10:00">[56:10:00]</a>.
*   **Varied Use Cases**: Different domains (e.g., manufacturing vs. supply chain) present distinct challenges. Manufacturing, with its constrained physical systems, often lends itself well to root cause analysis <a class="yt-timestamp" data-t="57:36:00">[57:36:00]</a>. Supply chain, being at a massive scale, might focus more on marginal gain interventions <a class="yt-timestamp" data-t="58:10:00">[58:10:00]</a>.

### Model Evaluation
*   **Validation and Testing**: Like any model, causal models require robust validation. This involves training, validation, and test splits to evaluate predictive information and compare estimated effects with observed interventional data <a class="yt-timestamp" data-t="29:43:00">[29:43:00]</a>.
*   **Interpreting Results**: Presenting causal graphs to non-technical users can be very intuitive, helping them understand information flow and underlying model assumptions <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>.

### Software and Tools
*   **Modularity and Flexibility**: Building modular causal packages allows users to select specific techniques applicable to their problem <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a> <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. Causal Lens's platform allows users to integrate open-source tools (e.g., Huawei's G-Castle, networkX, PyTorch, Pyro) alongside their proprietary packages, providing a flexible "Melting Pot" for data scientists <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.
*   **Documentation and Maintenance**: Well-documented, tested, and regularly updated packages (e.g., with monthly release cadences) are crucial for practical application <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

> [!INFO] Communication Challenges
> Effective communication between researchers, developers, and practitioners is vital for advancing the field. Sharing new ideas and practical applications, as fostered by events like NeurIPS and Clear, is key <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. This direct interaction often uncovers new approaches and applications, such as using rank deficiency to estimate latent confounders <a class="yt-timestamp" data-t="01:25:21">[01:25:21]</a>.

The future of fields requiring high-value or safety-critical decision-making, like healthcare or finance, must be causal. While associative models are valid for less risk-heavy use cases, true impact and reliability in crucial scenarios demand a causal approach <a class="yt-timestamp" data-t="01:26:04">[01:26:04]</a>.

To learn more about Andrew Lawrence, his team, and Causal Lens, visit their [research page](https://www.causallens.com/) or their [GitHub repository](https://github.com/causallens) <a class="yt-timestamp" data-t="01:26:54">[01:26:54]</a>.