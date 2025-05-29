---
title: Root Cause Analysis in Causal Problem Formalization
videoId: bHbqe9q_s-A
---

From: [[causalpython]] <br/> 

## Introduction
Will Orchard from the University of Cambridge, who previously interned at Amazon in Tuan, is conducting research focused on root cause analysis (RCA). His work aims to formalize RCA as a [[causal_analysis_and_its_importance | causal problem]] and explore its application in real-world scenarios, particularly within microservice-based applications <a class="yt-timestamp" data-t="17:12">[17:12]</a>.

## Formalizing Root Cause Analysis
Orchard notes that much existing work on RCA has not adopted a [[causal_reasoning_and_structural_causal_models | causal perspective]], despite the term "cause" being inherent in its name <a class="yt-timestamp" data-t="17:40">[17:40]</a>. His approach involves finding a unifying [[causal_reasoning_and_structural_causal_models | causal description]] for various existing RCA methods <a class="yt-timestamp" data-t="17:52">[17:52]</a>.

RCA methods can be categorized based on the "causal hierarchy" regarding how they conceive of a root cause <a class="yt-timestamp" data-t="18:05">[18:05]</a>:
*   **Associational question** <a class="yt-timestamp" data-t="18:11">[18:11]</a>
*   **Interventional question** <a class="yt-timestamp" data-t="18:13">[18:13]</a>
*   **Counterfactual question** <a class="yt-timestamp" data-t="18:15">[18:15]</a>

In collaboration with Dominic Janzing, Orchard's specific focus is on the counterfactual approach to RCA <a class="yt-timestamp" data-t="18:21">[18:21]</a>.

## Challenges in Formalization
A primary challenge in formalizing any problem is determining the most effective way to frame the question to capture its underlying intuition <a class="yt-timestamp" data-t="18:40">[18:40]</a>. [[causal_analysis_and_its_importance | Causality]] can provide strong answers regarding the quality of explanations for a root cause <a class="yt-timestamp" data-t="18:58">[18:58]</a>.

Another significant challenge is ensuring that the formalization is practically applicable to real-world problems <a class="yt-timestamp" data-t="19:21">[19:21]</a>. This requires engaging with engineers who work with such data and have developed their own heuristics for problem-solving <a class="yt-timestamp" data-t="19:27">[19:27]</a>.

## Key Learnings and Insights
Orchard's work has revealed that the question "What is a root cause?" is profound and deeply connected to various concepts in [[causal_analysis_and_its_importance | causality]] <a class="yt-timestamp" data-t="19:47">[19:47]</a>. These connections include:
*   Explainability <a class="yt-timestamp" data-t="19:55">[19:55]</a>
*   Sufficiency and necessity of features <a class="yt-timestamp" data-t="19:57">[19:57]</a>
*   The relationship between anomalous or rare values and interventions <a class="yt-timestamp" data-t="20:02">[20:02]</a>

He also learned that engineers may initially be hesitant to adopt formal [[causal_analysis_and_its_importance | causal approaches]], requiring convincing of their utility <a class="yt-timestamp" data-t="20:23">[20:23]</a>.

## Desired Real-World Impact
A critical impact Orchard seeks is to address the current lack of standardized datasets for evaluating RCA methods <a class="yt-timestamp" data-t="20:48">[20:48]</a>. The absence of such datasets has led to many methods being developed and benchmarked using private, simulated data, making it difficult to compare approaches and understand the impact of formal problem definitions on benchmarking results <a class="yt-timestamp" data-t="20:54">[20:54]</a>.

By making datasets publicly accessible, Orchard hopes to:
*   Convince more people of the importance of [[causal_analysis_and_its_importance | causal approaches]] <a class="yt-timestamp" data-t="21:23">[21:23]</a>.
*   Facilitate understanding of which problem formalizations are most effective in practice <a class="yt-timestamp" data-t="21:26">[21:26]</a>.
*   Encourage the use of these datasets to advance understanding and consensus on the best approach to RCA <a class="yt-timestamp" data-t="21:31">[21:31]</a>.

## Finding the Work
Will Orchard's work, including his paper, is available on arXiv, and the associated dataset can be found on a Git repository <a class="yt-timestamp" data-t="21:51">[21:51]</a>. Searching for "Pet Shop data set Amazon" may help locate the dataset <a class="yt-timestamp" data-t="22:04">[22:04]</a>. His Google Scholar profile and Twitter (where he posts updates) are also resources <a class="yt-timestamp" data-t="21:59">[21:59]</a>.

## Recommended Causal Papers
Orchard finds inspiration in score-based [[causal_discovery_and_analysis | causal discovery]] methods, such as the SCORE and NoLiNGAM algorithms, particularly admiring the theoretical work on their identifiability results and the use of score matching for [[causal_discovery_and_analysis | causal discovery]] <a class="yt-timestamp" data-t="22:42">[22:42]</a>. He also notes a paper from NFP related to using heavy-tailed distributions for [[causal_discovery_and_analysis | causal discovery]] and identifiability, which he considers relevant to RCA <a class="yt-timestamp" data-t="23:05">[23:05]</a>.

<div style="font-size:80%; font-style:italic;">
This article is based on insights shared by Will Orchard at the Clear conference on causal learning and representation.
</div>