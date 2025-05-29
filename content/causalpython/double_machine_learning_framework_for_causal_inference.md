---
title: Double machine learning framework for causal inference
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 
The Double Machine Learning (DML) framework is a significant approach within [[Causality and Machine Learning | causal machine learning]], particularly for estimating causal effects. It addresses challenges related to hyperparameter tuning and model selection in [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] applications for causal inference <a class="yt-timestamp" data-t="09:01:04">[09:01:04]</a>.

### Core Concept

The fundamental idea behind Double Machine Learning is that while predictive [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] can sometimes fail at causal inference tasks, it's also possible that causal inference itself struggles with the predictive aspects <a class="yt-timestamp" data-t="09:11:01">[09:11:01]</a>. Theoretically, DML should yield good results if it employs good estimators, sample splitting, and Neyman orthogonal scoring functions <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

However, practical success also hinges on various tuning choices, such as:
*   Hyperparameters for the nuisance estimation (e.g., estimation of influence functions) <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.
*   The selection of the [[structural_causal_models_and_machine_learning | causal model]] <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>.
*   The choice of the base learner (e.g., Lasso, Random Forest) <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

### Hyperparameter Tuning and Model Selection in DML

Research suggests that tuning [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] methods for nuisance estimation on the full dataset or on the folds of the DML algorithm is preferable for small sample sizes, as opposed to using a train-test split <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.

Key findings related to hyperparameter tuning for DML include:
*   **Predictive Loss for Model Selection**: To identify the appropriate [[structural_causal_models_and_machine_learning | causal model]] and its underlying structural assumptions for specific data, practitioners can monitor a predictive loss on the outcome variable (Y). Comparing this loss across different [[structural_causal_models_and_machine_learning | causal models]] can help, as the direction of advantage in this metric often correlates with the loss on the causal parameter, without needing an Oracle estimate <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.
*   **Combined Nuisance Loss**: A combined loss from both nuisance estimates—the propensity score of treatment assignment and the outcome model on Y—can indicate suitable parameter tuning, leading to a small loss on the causal parameter of interest <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

### Choice of Base Learners

The effectiveness of the chosen [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] method within DML is highly dependent on the specific data generating process (DGP) <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. For instance:
*   Lasso may perform well in linear settings <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>.
*   Boosting algorithms might be preferable in highly non-linear settings <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.

Automated [[causal_ai_and_machine_learning | machine learning]] algorithms, such as those within the Flamel framework, have shown promise in adapting well across various DGPs, making them a potentially valuable tool for practitioners <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

### Impact and Practical Application

The goal of this research is to provide better guidance for practitioners using the DML framework and [[Causal Machine Learning in Medicine and Industry | causal machine learning]] in general, especially in business or industry settings <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>. This guidance covers tuning choices like [[structural_causal_models_and_machine_learning | causal models]], hyperparameters, and [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] methods <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. The broader aim is to encourage more widespread adoption of [[Causal Machine Learning in Medicine and Industry | causal machine learning]] in industry by addressing existing skepticism and providing practical application insights <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>.

### Related Tools and Further Research

*   **`dml` package**: A software package for double machine learning is available with documentation and examples at `docs.dml.org` <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.
*   **`Double ML Deep`**: This paper explores integrating deep learning into the DML framework, allowing nuisance estimations to use not only tabular data but also images and texts. This opens up possibilities for applications like price elasticity estimation using product images or descriptions <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>.

### Broader Context: Hyperparameter Choice in Causal Structure Learning

The importance of hyperparameter choice extends beyond DML to general causal structure learning <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. Many [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] methods are highly sensitive to parameter selection <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. In causal structure learning, which recovers causal graphs from observational data, current methods often struggle in real-world applications due to their reliance on [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] and the potential impact of hyperparameter choices <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. Causal structure learning is unsupervised, meaning there is no prior information about the causal graphs <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

A simple bivariate example demonstrates how changing the number of regression parameters (a hyperparameter) can alter the inferred causal direction, leading to incorrect conclusions <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. This highlights the potential for errors due to hyperparameter selection <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

#### Findings on Hyperparameter Impact:
*   **Default Values**: Surprisingly, in causal structure learning, default hyperparameter values often perform very close to "Oracle" (best possible) cases, which contrasts with standard [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]] where defaults frequently perform poorly <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Oracle Performance**: Even with Oracle hyperparameter access, algorithms still vary in performance, indicating that algorithm selection remains crucial regardless of parameter tuning <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   **Worst-Case Performance**: The extent to which methods can perform badly (worst possible hyperparameter values) varies, which can be interpreted as the "safety of use" for different methods <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. Neural network-based methods, for example, appear riskier in these scenarios due to their known volatility and sensitivity to hyperparameters <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **False Positives vs. False Negatives**: With optimal or near-optimal parameter settings, the number of false positives in causal discovery can be reduced almost to zero. This means that while some edges might be missing (false negatives), the identified edges can generally be trusted as true <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.

#### Implications for Practitioners:
*   When selecting algorithms, practitioners should consider not only the dataset but also how hyperparameter tuning might influence the optimal choice <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   For risk-sensitive applications, focusing on "safer" methods (those with lower worst-case performance) might be preferable <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   The best algorithmic choice can vary significantly across different dataset settings (e.g., graph size, edge density) and depending on the quality of parameter tuning available <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>.