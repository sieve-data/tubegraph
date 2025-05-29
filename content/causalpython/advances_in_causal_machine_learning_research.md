---
title: advances in causal machine learning research
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

This article explores recent [[advancements in causal modeling and AI | advancements in causal modeling and AI]], focusing on an emerging trend in [[causal_ai_and_machine_learning_intersection | Causal AI]] that addresses practical challenges in [[causal_inference_and_machine_learning | causal inference and machine learning]]. <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>

## Featured Researcher: Bernhard Schölkopf

Bernhard Schölkopf is highlighted as a significant contributor to [[causal_inference_and_machine_learning | causality]], [[causal_machine_learning | causal machine learning]], and [[machine_learning | machine learning]] generally. <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a> He was a former PhD student of Vladimir Vapnik, a "Godfather" of modern [[machine_learning | machine learning]], and initially worked on kernel methods in the field. <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a> Schölkopf later transitioned into [[causal_inference_and_machine_learning | causality]] and dedicates significant time to [[causal_research | causal research]] today. <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>

## A New Trend in Causal AI

A growing trend in [[causal_ai_and_machine_learning_intersection | Causal AI]] research is focusing more on the practical [[challenges_in_causal_machine_learning_compared_to_traditional_methods | challenges]] faced when implementing causal methods. <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a> This involves moving away from abstract causal concepts to concentrate on specific scenarios where [[causal_inference | causal inference]] or [[causal_discovery | causal discovery]] is desired. <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a> The goal is to leverage the nature of these situations to ensure valid and useful [[causal_inferences | causal inferences]]. <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>

A key aspect of this trend is the use of data that is **exchangeable but not Independent and Identically Distributed (IID)**. <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>
*   IID is a special case of exchangeable data; all IID data is exchangeable, but not all exchangeable data is IID. <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>
*   When data is not IID but is exchangeable, this fact can be leveraged to perform [[causal_inference | causal inference]] or [[causal_discovery | causal discovery]] in situations where it would otherwise be impossible with IID data. <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>
*   A real-world scenario producing exchangeable data is when data is collected from multiple environments. <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>

### Key Papers Illustrating This Trend

1.  **"Causal De Finetti"** <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>
    *   Authored by C. Guo, V. Titou, B. Schölkopf, and F. Huszár. <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>
    *   Accepted at NeurIPS, 2023. <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>
    *   This paper shows that information about the underlying [[causal_structure | causal structure]] can sometimes be inferred from data if the data is exchangeable but not IID. <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>

2.  **"DOOF: Causal Effects for Exchangeable Data"** <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>
    *   Published recently and currently under review. <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>
    *   This paper demonstrates that under the condition of exchangeable data, [[causal_relationships | causal relationships]] can be identified, and [[causal_discovery | causal discovery]] and [[causal_effect_estimation | causal effect estimation]] can be performed in a broader range of circumstances. <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>

3.  **"Detecting hidden confounding in observational data using multiple environments"** <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>
    *   Authored by R. Carlsson and J. K. <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>
    *   Published in 2022, this paper also incorporates the idea of multiple environments. <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>
    *   The authors show that [[hidden_confounding | hidden confounding]] in observational data can sometimes be detected under specific circumstances when data from different environments is available. <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>

These papers exemplify a direction that expands capabilities in [[causal_inference | causal inference]], particularly in situations where not all necessary assumptions (like the absence of confounding) are met. <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a> This allows for approaches like partial identification, sensitivity analysis, or the detection and adjustment for [[hidden_variables | hidden variables]] to be applied. <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a> This new trend leverages multiple environments and non-IID data to expand the existing [[causal_toolbox | causal toolbox]]. <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>

## Ask Me Anything (AMA) Session

Viewers were invited to participate in a spontaneous AMA session to ask questions about [[causality]] or the discussed papers. <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a> <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>