---
title: Improving LLM performance with logistic regression
videoId: m7k6mzxyZrg
---

From: [[hrishikeshyadav8883]] <br/> 

A recent paper explores a method for [[large_language_model_confidence_estimation | Large language model confidence estimation]] via a blackbox approach, aiming to improve the performance of Large Language Models (LLMs) by estimating their response confidence <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This method reportedly outperforms various processes on benchmark datasets, particularly for LLMs in question-answering tasks like SQuAD <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Methodology

The core of this approach involves using logistic regression to predict the confidence of an LLM's response being correct <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The resolution tuning for this model was done on three major models: Vicuna 13B, LLaMA, and FLAN <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Prompt Perturbation Strategies

The method introduces six prompt perturbation strategies as part of its process to enhance LLM performance and estimate confidence <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. These strategies are designed to modify tokens in each operation and include:
*   Stochastic decoding <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
*   Paraphrasing <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   Sentence permutation <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Entity frequency amplification <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   Stop word removal <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   Split response <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

These [[strategies_for_enhancing_llm_response_accuracy | strategies for enhancing LLM response accuracy]] involve manipulating natural language inputs <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Feature Engineering

Features for the logistic regression model are engineered based on the semantic diversity and syntactic similarity of responses obtained from these prompt perturbations <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Performance and Findings

By building an interpretable logistic regression model based on these features, the researchers achieved state-of-the-art performance in estimating confidence across four benchmark datasets <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The model showed an improvement of more than 10% in prediction accuracy on benchmarks <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

Key findings include:
*   **Crucial Features**: Stochastic decoding and sentence permutation, along with entity frequency amplification, are crucial for estimating variability, indicating the importance of output variability and robustness to redundant information <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Shared Features**: For a given dataset, important features are shared across different LLMs, suggesting the possibility of a universal confidence model <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Generalizability**: A confidence model trained on one LLM generalizes well to other LLMs on the same data. This allows for a single confidence model to be used across multiple LLMs, which is beneficial for ranking competing LLMs <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## Limitations

Despite its advancements, the approach has limitations:
*   **Ground Truth Requirement**: The approach requires at least some LLM responses to be close to the ground truth to obtain reasonable confidence estimations <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Language Dependence**: Insights are primarily based on English datasets, and results might vary for data in other languages, pointing to a [[multilinguality_issues_in_language_models | multilinguality issue]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Error Proneness**: Using prompt rods for testing response reliability, or other metrics, can be error-prone <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Adversarial Inducement**: An adversary aware of the features could potentially induce misplaced trust in the model <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. While direct access to the LLM's logic is not needed, confidence estimates, though accurate, can be imperfect, which should be considered in high-stakes applications <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## Conclusion

This paper presents an interesting framework for understanding how confidence estimation depends on various factors and how improved models can be built for benchmarking LLM datasets <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. The approach uses a blackbox design for its confidence estimator <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.