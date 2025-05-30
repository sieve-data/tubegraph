---
title: Blackbox access to models
videoId: m7k6mzxyZrg
---

From: [[hrishikeshyadav8883]] <br/> 

This article discusses a paper focused on estimating the confidence of Large Language Models (LLMs) through blackbox access <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The paper proposes various ways and parameters for this estimation <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, demonstrating that its approach outperforms existing methods on benchmark datasets <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Problem of LLM Trust and Evaluation

A significant challenge with LLMs is the inability to fully trust their outputs <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Furthermore, there are difficulties in evaluating and ranking competing models effectively <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Confidence estimation plays a crucial role in addressing these issues <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Existing confidence models for LLMs are often based on zero-shot learning across given data <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Methodology

The approach in this paper makes use of logistic regression for confidence estimation <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Prompt Perturbation Strategies

Six major prompt perturbation strategies are introduced <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>:
-   Stochastic decoding <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
-   Paraphrasing <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
-   Sentence commutation <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
-   Entity frequency amplification <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
-   Stop word removal <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
-   Split response <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

These strategies involve modifying tokens in each operation <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Feature Engineering

Features are engineered based on the semantic diversity and syntactic similarity of responses obtained from the prompts <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. A logistic regression model is then trained on these features to predict the likelihood of an LLM response being correct <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Models and Benchmarks

The fine-tuning of the resolution function is done on three major models:
-   GPT-3 <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
-   Flan <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
-   Llama 7B <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

Benchmark datasets include Q or SQUAD <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, and the approach was evaluated on four major datasets <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Key Findings and Improvements

The paper demonstrates state-of-the-art performance in estimating confidence, with improvements of over 10% on prediction or benchmark results <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Interpretable Confidence Model
An interpretable confidence model was prepared <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Features such as stochastic decoding, sentence permutation, and entity frequency amplification are crucial for estimating variability, indicating the importance of output variability, ordered bias, and brittleness to redundant information <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Generalization Across LLMs
A significant finding is that a confidence model trained on one LLM generalizes well to other LLMs on the same dataset <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This enables the use of a single confidence model for multiple LLMs <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, which is beneficial for ranking competing LLMs <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Universal Confidence Model
For a given dataset, important features are shared across different LLMs, suggesting the possibility of a universal confidence model <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Limitations

>[!WARNING]
>The approach has several limitations:
>-   It requires at least some LLM responses to be close to the ground truth to obtain reasonable confidence or results <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
>-   Insights are based on datasets in English <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. They might vary for datasets in other languages, highlighting [[multilinguality_issues_in_language_models | multilinguality issues]] <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Many LLMs may not perform as well for multi-lingual tasks <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
>-   The use of ROUGE for testing responsibility, among other metrics, can be error-prone <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
>-   The approach is vulnerable to adversaries who might be aware of the features used and could potentially induce misplaced trust <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. While blackbox access does not require knowledge of the LLM's internal logic, confidence estimates, though accurate, can be imperfect <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This needs to be considered in high-stakes applications <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## Conclusion

This paper provides an interesting approach for anyone looking to prepare a framework for benchmark datasets <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. It offers insights into how confidence estimators depend on various factors and how improved models can be built using natural language processing techniques <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.