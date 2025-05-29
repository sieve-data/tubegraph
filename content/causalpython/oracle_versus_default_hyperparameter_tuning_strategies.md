---
title: Oracle versus default hyperparameter tuning strategies
videoId: vW2vB6e-Mm8
---

From: [[causalpython]] <br/> 
Hyperparameter tuning plays a crucial role in the effectiveness of machine learning models, particularly in the domain of causal AI. The choice of hyperparameters can significantly impact the robustness and accuracy of causal discovery algorithms.

## The Challenge of Hyperparameter Choice in Causal Structure Learning
[[Impact of hyperparameters on causal structure learning | Hyperparameters]] are recognized as critically important in supervised machine learning, with many methods being highly sensitive to their selection <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This sensitivity extends to causal structure learning, which aims to recover causal graphs from observational data <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. A key challenge is that causal structure learning is unsupervised in nature, meaning there's no prior information about the causal graphs; only the dataset is available <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

A simple bivariate example (variables X and Y) demonstrates this sensitivity:
*   Two regression functions are fitted: X on Y and Y on X <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   The causal direction is inferred based on which regression line has a lower prediction error <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   The number of regression parameters, which is a hyperparameter, can significantly alter the concluded causal direction <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Changes in this hyperparameter can lead to incorrect conclusions <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## Strategies for Hyperparameter Selection
Research explored various hyperparameter selection strategies across different simulated settings and a real dataset, evaluating metrics like structural Hamming distance, false positives, and false negatives <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The strategies included:
*   **Oracle**: Utilizing the best possible hyperparameter values, assuming perfect knowledge <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Worst Case**: Employing the worst possible hyperparameter values <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Default Values**: Using default values proposed by the algorithm authors or within software packages <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Derived Defaults**: Default values derived across all simulations <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Key Findings on Tuning Strategies
### Performance of Default Values
A surprising finding is that default values, unlike in standard machine learning, perform remarkably close to Oracle cases in causal structure learning <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This suggests that for causal structure learning, the out-of-the-box settings might be more effective than expected.

### Oracle Performance and Algorithm Selection
Even when all algorithms have access to the Oracle (optimal hyperparameters), their performance still varies <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This emphasizes that [[Developing Effective Machine Learning Models | algorithm selection]] remains crucial, regardless of hyperparameter tuning <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Furthermore, even with near-optimum parameters, there is still room for improvement across all algorithms <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Worst-Case Scenarios and Method Safety
The extent to which methods can perform poorly in worst-case hyperparameter scenarios varies, indicating the "safety of use" for different methods <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Neural network-based methods, known for their volatility and sensitivity to hyperparameters, appeared particularly risky in these cases <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Error Types with Optimal Tuning
With Oracle cases, the number of false positives reduces significantly, often to zero <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. The remaining errors are primarily due to false negatives (missing edges) <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This implies that in well-specified parameter cases, the edges identified by the algorithms can generally be trusted, even if some true edges are missed <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Tuning in Double Machine Learning
For [[AB Testing and Machine Learning Models | Double Machine Learning (DML)]] frameworks, hyperparameter tuning for nuisance estimation is critical <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
Key findings in DML hyperparameter tuning:
*   Tuning machine learning methods for nuisance estimation on the full data or DML algorithm folds is preferred for small sample sizes over a train-test split <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   Tracking a predictive loss on the outcome (Y) can help identify the appropriate causal model and structural assumptions for specific data <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   Combining losses from both nuisance estimates (propensity score and outcome model) can indicate the right parameter tuning to achieve a small loss on the causal parameter of interest <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   The choice of machine learning method (e.g., Lasso, Random Forest, boosting algorithms) heavily depends on the data generating process <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   Automated machine learning algorithms, such as those within the Flamel framework, may be suitable for tuning across various data generating processes <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

## Practical Implications
Practitioners choosing algorithms for causal inference should consider not only their dataset but also how [[Impact of hyperparameters on causal structure learning | hyperparameter tuning]] impacts the optimal algorithm choice <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. Factors like confidence in parameter optimality or the risk-sensitivity of the case should guide the selection towards either potentially optimal but volatile methods or safer alternatives <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Increased work on practical applications is hoped to reduce skepticism and encourage wider adoption of causal machine learning in industry <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.