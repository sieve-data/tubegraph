---
title: Large language model confidence estimation
videoId: m7k6mzxyZrg
---

From: [[hrishikeshyadav8883]] <br/> 

A new paper proposes a method for large language model (LLM) confidence estimation via a blackbox approach, providing various ways and parameters for estimation <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This method significantly outperforms existing processes on benchmark datasets designed for LLMs, such as TriviaQA and SQuAD <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Models and Benchmarks

The proposed resolution is refined on three major LLMs: Flan-T5, OPT, and LLaMA <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The paper addresses the problem of evaluating and ranking models, especially since LLMs can sometimes be untrustworthy <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Methodology

The confidence model for LLMs described in the paper is primarily based on a zero-shot approach <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. It leverages [[improving_llm_performance_with_logistic_regression | logistic regression]] to predict the confidence of an LLM's response being correct <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Prompt Perturbation Strategies

The research introduces six prompt perturbation strategies designed to modify tokens in each operation:
*   Stochastic decoding <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
*   Paraphrasing <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Sentence permutation <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Entity frequency amplification <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   Stop word removal <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   Split response <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

Features are engineered based on the semantic diversity and syntactic similarity of responses obtained from these prompt perturbations <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. A [[improving_llm_performance_with_logistic_regression | logistic regression]] model is then trained on these features to predict the correctness confidence of an LLM response <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Performance and Key Findings

The interpretable [[improving_llm_performance_with_logistic_regression | logistic regression]] model achieves state-of-the-art performance in estimating confidence across four benchmark datasets <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The prediction accuracy or benchmark performance improves by more than 10% <a class="yt-timestamp" data-t="00:03:59">[00:04:05]</a>.

Key findings include:
*   **Crucial Features**: Stochastic decoding, sentence permutation, and entity frequency amplification are crucial features for estimating variability <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This highlights the importance of output variability, ordered bias, and brittleness to redundant information in LLM responses <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Universal Confidence Model**: For a given dataset, important features are shared across different LLMs, suggesting the possibility of a universal confidence model <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Generalization**: A confidence model trained on one LLM generalizes well to other LLMs on the same data, allowing a single model to be used for multiple LLMs <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This capability enables ranking competing LLMs <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Limitations

Despite its advancements, the approach has certain limitations:
*   **Ground Truth Requirement**: The approach requires at least some LLM responses to be close to the ground truth to obtain reasonable confidence or results <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Language Dependency**: Insights are based on English datasets <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Performance might vary for datasets in other languages, pointing to [[multilinguality_issues_in_language_models | multilinguality issues]] in LLMs <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Evaluation Metrics**: The use of ROUGE scores for testing response reliability can be error-prone <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Adversarial Risks**: If an adversary is aware of the features used, they could potentially induce misplaced trust in LLM responses <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Although no access to the LLM's logic or internals is required, the confidence estimates, though accurate, can be imperfect <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This should be considered when applying the approach in high-stakes situations <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Conclusion

This paper provides a valuable framework for preparing benchmark datasets and understanding how confidence estimators depend on various factors in natural language processing applications <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. The study uses an encoder-decoder architecture design <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.