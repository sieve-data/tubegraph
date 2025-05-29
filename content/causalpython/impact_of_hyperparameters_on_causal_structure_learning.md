---
title: Impact of hyperparameters on causal structure learning
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 

## Introduction

Research into the impact of hyperparameters on [[causal_model_evaluation_and_selection | causal structure learning]] addresses how parameter choices affect the accuracy and robustness of algorithms designed to recover causal graphs from observational data <a class="yt-timestamp" data-t="00:30:32">[00:30:32]</a>. This is a critical area, especially given that many machine learning methods, upon which [[structural_causal_models_and_machine_learning | causal structure learning]] relies, are highly sensitive to parameter selection <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.

## Motivation and Problem Statement

Parameters in supervised machine learning are recognized as very important, with many methods being sensitive to their choice <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. Currently, methods for recovering causal graphs from observational data do not perform optimally, especially in applications with real datasets <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. A key question investigated is whether these struggles in application are due to hyperparameter choice <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. It's important to note that [[causal_model_evaluation_and_selection | structure learning]] is unsupervised in nature, meaning there is no prior information about causal graphs; only the dataset is available <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

### Simple Bivariate Example

A simple example involves two variables, X and Y. Two regression functions are fitted: X on Y and Y on X <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. The causal algorithm determines the causal direction based on which regression line has a lower prediction error <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. The number of regression parameters (coefficients) acts as a hyperparameter. As this hyperparameter changes, the concluded causal direction can also change, leading to incorrect answers for certain parameter values <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. This demonstrates how hyperparameter choice can lead to different answers and potential mistakes <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

## Research Approach

The study involved various simulated settings and one real dataset, utilizing a popular data generator called Syn <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. Three main metrics were measured:
*   Structural Hamming Distance (lower is better) <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>
*   False Positives of edges (lower is better) <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>
*   False Negatives of edges (lower is better) <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>

Regarding hyperparameter selection, traditional tuning methods are either non-existent or highly experimental <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. The study used four choices for hyperparameter values in simulated settings:
1.  **Oracle**: The best possible hyperparameter values <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
2.  **Worst**: The worst possible hyperparameter values <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
3.  **Default (Author-proposed)**: Values proposed by the algorithm authors or within packages <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.
4.  **Default (Derived)**: Values derived across all simulations <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

## Key Findings

*   **Default Values Perform Well**: Surprisingly, default hyperparameter values performed very close to the Oracle cases <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. This contrasts with standard machine learning, where default values often perform poorly <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
*   **Algorithm Selection Remains Important**: Even with Oracle hyperparameter access, algorithms still differ in performance, indicating that [[causal_model_evaluation_and_selection | algorithm selection]] is crucial regardless of parameters <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   **Room for Improvement**: Even with near-optimum parameters (Oracle), there is still room for improvement across all algorithms <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.
*   **Safety of Use (Worst-Case Scenarios)**: The extent to which methods can perform badly varies. Methods with lower values in worst-case scenarios are considered safer to use <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. For example, neural network-based methods appear fairly risky due to their volatility and sensitivity to hyperparameters <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Trustworthiness of Found Edges**: In well-specified parameter cases (even with Oracle), the number of false positives reduces almost to zero <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>. This means remaining mistakes are mainly due to false negatives. Practically, this implies that the edges and graphs produced by algorithms, even if some edges are missing, can generally be trusted as true <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

## Practical Implications for Practitioners

When selecting algorithms, practitioners should consider not only the dataset but also how hyperparameter tuning might impact the optimal choice <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. If a case is risk-sensitive, it might be better to focus on safer methods <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. The best algorithmic choice varies not only across dataset settings (e.g., graph size, edge density) but also with the quality of parameters considered (e.g., if tuning is possible versus worst-case scenarios) <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. Some methods might be preferred if tuning is possible, while others are safer in worst-case hyperparameter specifications <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

Oliver Schwendemann further highlights that in [[structural_causal_models_and_machine_learning | causal machine learning]], especially within the double machine learning framework, performance is significantly influenced by tuning choices, including hyperparameters for nuisance estimation and the choice of the [[causal_model_evaluation_and_selection | causal model]] <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>. Tuning machine learning methods on the full data or folds of the double machine learning algorithm are preferred options in small sample sizes over a train-test split <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>. To select the right [[causal_model_evaluation_and_selection | causal model]] and structural assumptions, tracking a predictive loss on the outcome variable (Y) can be useful, as it often correlates with the loss on the causal parameter without needing an Oracle estimate <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>. Combining losses from nuisance estimates (e.g., propensity score and outcome model) can also indicate optimal parameter tuning <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>. The choice of the machine learning method depends heavily on the data generating process <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. Automated machine learning algorithms, such as those within the Flamel framework, may offer a good fit for various data generating processes <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

## Further Information

For more information, the work can be found by searching for "D. Malansky" on Google Scholar, X, or LinkedIn (@d_mclansky) <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>. Oliver Schwendemann's work can be found by typing "hyper parameter tuning for causal inference with double machine learning" into Google <a class="yt-timestamp" data-t="13:24:00">[13:24:00]</a>, or by visiting the `douml` package website at docs.dml.org <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.