---
title: Strategies for enhancing LLM response accuracy
videoId: m7k6mzxyZrg
---

From: [[hrishikeshyadav8883]] <br/> 

This article discusses a paper focused on estimating [[large_language_model_confidence_estimation | Large Language Model (LLM) confidence]] through a blackbox approach, aiming to improve LLM performance and address issues in model evaluation and ranking <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Approach Overview

The paper utilizes a novel approach to estimate LLM confidence, diverging from traditional zero-shot methods <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. It makes use of [[improving_llm_performance_with_logistic_regression | logistic regression]] for confidence estimation <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The resolution tuning was performed on three major models: LLaMA (13B), Flan, and PaLM (7B) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Prompt Perturbation Strategies

Six main prompt perturbation strategies were introduced to modify tokens in responses <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>:

*   Stochastic decoding <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
*   Paraphrasing <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Sentence commutation <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Entity frequency amplification <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
*   Stop word removal <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   Split response <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

### Feature Engineering and Model Training

Features are engineered based on the semantic diversity and syntactic similarity of the responses generated from the prompts <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. An [[improving_llm_performance_with_logistic_regression | logistic regression]] model is then trained on these features to predict the correctness of an LLM's response <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Key Findings

The interpretable confidence model achieved state-of-the-art performance in estimating confidence across four benchmark datasets <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>, showing an improvement of over 10% in prediction for the benchmark <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

Significant findings include:
*   **Crucial Features:** Features such as stochastic decoding, sentence permutation, and entity frequency amplification are crucial for estimating variability and indicate the importance of output variability or ordered bias <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Universal Confidence Model:** For a given dataset, important features are shared across different LLMs, suggesting the possibility of developing a "universal confidence model" <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Generalizability:** A confidence model trained on one LLM generalizes well to other LLMs on the same dataset. This enables the use of a single confidence model for multiple LLMs, which is highly beneficial for ranking competing LLMs <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Limitations

Despite its advancements, the approach has certain limitations:
*   **Ground Truth Requirement:** The method requires at least some LLMs to be close to the ground truth to obtain reasonable confidence results <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Language Dependency:** The insights derived are based on English datasets and may vary for datasets in other languages, highlighting potential [[multilinguality_issues_in_language_models | multilinguality issues in language models]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Adversarial Awareness:** If an adversary is aware of the features used, they could potentially induce misplaced trust <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. While the approach does not require access to the logic or internals of the LLM, the confidence estimates, though accurate, can be imperfect, which should be considered in high-stakes applications <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.