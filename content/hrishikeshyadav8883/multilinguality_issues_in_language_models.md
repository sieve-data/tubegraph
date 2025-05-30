---
title: Multilinguality issues in language models
videoId: m7k6mzxyZrg
---

From: [[hrishikeshyadav8883]] <br/> 

When developing methods for [[large_language_model_confidence_estimation | large language model confidence estimation]], a significant limitation arises concerning their applicability across different languages <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Language Dependence in Confidence Estimation

The current approach for estimating confidence in Large Language Model (LLM) responses, specifically a method involving [[improving_llm_performance_with_logistic_regression | logistic regression]] based on prompt perturbation strategies and feature engineering <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, derives its insights predominantly from English datasets <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This raises concerns that the findings and the model's effectiveness might differ when applied to datasets in other languages <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

This discrepancy is identified as a "multilinguality issue" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Many LLMs may not exhibit the same level of performance or robustness in multilingual contexts as they do with English-centric data <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Therefore, the proposed confidence estimation framework may need further adaptation or evaluation for broader multilingual applicability.