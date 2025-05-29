---
title: Hyperparameter tuning for causal machine learning
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 

Hyperparameters play a crucial role in [[causal_machine_learning | causal machine learning]], particularly in areas like [[causal_structure_learning_and_its_challenges_with_hyperparameters | causal structure learning]] and double machine learning models <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores insights from leading researchers on hyperparameter tuning and its impact on causal discovery and effect estimation, drawing from discussions at Clear 2024's Causal Bandits Extra <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Robustness of Causal Structure Learning to Hyperparameter Choice

Dmytro Malashansky from the University of Essex presented work on the robustness of algorithms for [[causal_structure_learning_and_its_challenges_with_hyperparameters | causal structure learning]] to hyperparameter choice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Motivation and Challenges
In supervised machine learning, parameters are critical, and many methods are highly sensitive to their selection <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Currently, [[causal_structure_learning_and_its_challenges_with_hyperparameters | causal structure learning]]—recovering causal graphs from observational data—does not perform optimally, especially in real-world applications <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This struggle might be attributed to hyperparameter choice, especially since structure learning is unsupervised, meaning there is no prior information about the causal graphs <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Illustrative Example
A simple bivariate case with variables X and Y demonstrates this sensitivity <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. By fitting two regression functions (X on Y and Y on X) and comparing their prediction errors, a basic causal algorithm identifies the direction based on the lower error <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. However, as the number of regression parameters (a hyperparameter) changes, the determined causal direction can change, leading to incorrect conclusions <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This variability highlights how hyperparameter choice can lead to mistakes <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Study Methodology and Metrics
The study involved various simulated settings and a real dataset, using a popular data generator called Sy <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Three key metrics were measured:
*   Structural Hamming distance <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
*   False positives of edges <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
*   False negatives of edges <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>

Lower values are desirable for all metrics <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Since hyperparameter tuning methods for causal structure learning are currently limited or experimental, the study explored performance under different hyperparameter selection scenarios <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>:
1.  **Oracle:** Best possible hyperparameter values (assuming optimal access) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
2.  **Worst:** Worst possible hyperparameter values <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
3.  **Default (Algorithm/Package):** Default values proposed by algorithm authors or within packages <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
4.  **Default (Derived):** Default values derived across all simulations <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>

### Key Results
*   **Default Values Performance:** Surprisingly, default values in [[causal_structure_learning_and_its_challenges_with_hyperparameters | causal structure learning]] perform very close to Oracle cases, which contrasts with standard machine learning where defaults often perform poorly <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Algorithm Selection:** Even with Oracle access, algorithms still differ in performance, emphasizing that algorithm selection is crucial regardless of parameters <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Room for Improvement:** There is still significant room for improvement across all algorithms, even with near-optimal parameters <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Safety of Use:** The extent to which methods can perform poorly varies. Methods with lower worst-case values are considered safer to use <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Neural network-based methods, known for volatility, appear riskier in these scenarios <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Error Types with Oracle:** With Oracle cases, the number of false positives reduces almost to zero. Remaining mistakes are primarily due to false negatives, meaning that the edges identified by algorithms can be trusted, even if some true edges are missed <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This can be very useful in practical applications <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Variability of Optimal Choices:** The optimal algorithmic choice depends not only on dataset settings (e.g., graph size, edge density) but also on the quality of hyperparameter specification (e.g., whether tuning can be performed or if one must consider worst-case scenarios) <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Practical Impact
Practitioners selecting algorithms should consider both the dataset at hand and how hyperparameter tuning will impact the optimal choice <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. For risk-sensitive applications, focusing on safer methods might be preferable <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Hyperparameter Tuning for Double Machine Learning

Oliver Schwabe presented work on hyperparameter tuning for [[causal_machine_learning | causal machine learning]], specifically within the double machine learning framework <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Core Idea
While predictive machine learning often struggles with [[causal_inference_and_machine_learning | causal inference]] tasks, it's also possible that [[causal_inference_and_machine_learning | causal inference]] methods might fail at predictive machine learning due to tuning choices <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Double machine learning theoretically yields good results with strong estimators, sample splitting, and Neyman orthogonal scoring functions <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. However, this is heavily influenced by tuning choices, such as hyperparameters for nuisance estimation, the choice of the causal model, and the selection of the learner (e.g., Lasso, Random Forest) <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### Key Results
*   **Tuning Strategy:** For small sample sizes, tuning machine learning methods for nuisance estimation on the full data or on the folds of the double machine learning algorithm is preferred over a train-test split <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Causal Model Selection:** To identify the right causal model and structural assumptions for a given data set, tracking a predictive loss on the outcome (Y) and comparing it across different causal models can be effective <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. The direction of advantage in this metric often aligns with the loss on the causal parameter, which is beneficial because it doesn't require an Oracle estimate <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Combined Nuisance Loss:** Calculating a combined loss between both nuisance estimates (propensity score for treatment assignment and outcome model on Y) can indicate optimal parameter tuning to achieve a small loss on the causal parameter of interest <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Learner Choice:** The choice of the machine learning method depends significantly on the data generating process <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Lasso might perform well in linear settings, while boosting algorithms are preferable in heavily nonlinear settings <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Automated ML:** Automated machine learning algorithms, such as the Flaml framework, show promise in fitting well across various data generating processes, making them interesting for practitioners <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### Practical Impact
This work aims to provide better guidance to practitioners applying the double machine learning framework and [[causal_machine_learning | causal machine learning]] in general, in business or industry <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. The hope is to clarify tuning choices for causal models, hyperparameters, and machine learning methods, thereby increasing the application of [[application_of_causal_machine_learning_in_medicine | causal machine learning in industry]] <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## Causal Representation Learning

Simon Bing from TU Berlin discussed work on an identifiability result for [[causal_representation_learning | causal representation learning]] <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

### Main Contribution
The work aims to soften the common assumption in previous [[causal_representation_learning | causal representation learning]] research that environments are characterized by single-node interventions on latent variables <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. This new research allows for multi-node interventions (intervening on many nodes simultaneously) even when intervention targets are unknown, while still achieving identifiability <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

### Key Results
The main results characterize a specific notion of sparsity. By positing an underlying causal Structural Causal Model (SCM), the change in mechanisms affected by interventions from one environment to the next is assumed to be sparse <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. Key assumptions include a linear mixing function from latent to observed variables and sufficiently diverse and sparse intervention coverage across environments <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. By regularizing for this sparsity, the underlying causal variables can be recovered up to permutation and element-wise rescaling <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.

### Real-World Impact
The long-term goal is to apply [[causal_inference_and_machine_learning | causal inference]] and [[causal_representation_learning | causal representation learning]] to large-scale climate data, which involves high-dimensional measurements and heterogeneous data from different environments <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>. Since active interventions on climate are not possible, moving from single-node to multi-node interventional environment settings is an important first step towards extracting causal information and formulating causal models for macroclimate phenomena <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.