---
title: Papers on practical challenges in causal research
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

A notable trend in Causal AI research is the increasing focus on addressing [[challenges_in_causal_analysis_in_different_settings | practical challenges]] encountered when implementing causal methods in real-world scenarios <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This shift moves beyond abstract theoretical considerations to concentrate on specific situations where causal inference or discovery is desired <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The goal is to identify and leverage the unique nature of these situations to ensure that causal inferences are both valid and useful <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

This evolving direction expands the capabilities of [[tools_and_frameworks_for_causal_analysis | causal analysis]], particularly in circumstances where traditional assumptions, such as Independently and Identically Distributed (IID) data, may not be fully met <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

## Key Papers Illustrating this Trend

Several papers exemplify this practical approach, particularly by utilizing data characteristics like exchangeability and insights from multiple environments.

### 1. Causal Definability

*   **Authors:** C. Guo, V. Tobias, Bernard Schölkopf, and F. Huszár <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>
*   **Publication:** Accepted at NeurIPS 2023 <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>

This paper, titled "Causal Definability," leverages the definability theorem from probability theory <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Its core contribution is demonstrating that information about the underlying causal structure of observed data can sometimes be inferred, even if the data is not IID <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The key assumption here is that the data is *exchangeable*, which is a weaker condition than IID (all IID data is exchangeable, but not all exchangeable data is IID) <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. This approach allows for causal inference or discovery in scenarios where it would otherwise be impossible with IID data <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Bernard Schölkopf, a co-author, is recognized for his significant contributions to causality, causal machine learning, and machine learning in general <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### 2. Doof: Causal Effects for Exchangeable Data

*   **Status:** Under review <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>

This paper continues the exploration of exchangeable data that is not IID <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. A common real-world scenario where exchangeable data might be obtained is from multiple environments <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. The authors show that under the condition of exchangeable data, it is possible to identify causal relationships, perform causal discovery, and estimate causal effects in a broader range of circumstances <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### 3. Detecting Hidden Confounding in Observational Data Using Multiple Environments

*   **Authors:** Rickard Carlson and Jesse K. <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>
*   **Publication Year:** 2022 <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>

This paper builds on the idea of leveraging data from multiple different environments <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. The authors demonstrate that it is sometimes possible to detect [[challenges_in_identifying_causal_relationships | hidden confounding]] in observational data under specific circumstances, provided data from these distinct environments is available <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

This capability is crucial for addressing [[challenges_of_causal_inference_and_counterfactual_thinking | challenges of causal inference]] when certain assumptions are not met, such as the presence of unobserved confounders <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. By detecting confounding, researchers can perform partial identification, conduct sensitivity analysis, or adjust their analysis to accurately reflect the presence of hidden variables <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Conclusion

The growing emphasis on these types of papers signifies a valuable expansion of the causal toolbox, enabling more robust and applicable causal inferences in complex real-world settings where ideal conditions may not exist <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.