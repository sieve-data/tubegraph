---
title: Causal inference and discovery with exchangeable data
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

A new trend in Causal AI focuses on addressing practical challenges in implementing causal methods by leveraging the nature of specific situations to ensure valid and useful causal inferences <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>. This emerging direction expands the capabilities of [[causal_inference_and_its_applications | causal inference]] in situations where standard assumptions may not be met <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.

A key aspect of this trend involves the use of "exchangeable data," which is a weaker condition than Independent and Identically Distributed (IID) data <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>. While all IID data is exchangeable, not all exchangeable data is IID <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. By leveraging the properties of exchangeable data, it becomes possible to perform [[causal_inference_concepts_and_applications | causal inference]] or [[causal_discovery_algorithms | causal discovery]] in scenarios where it would otherwise be impossible with IID data <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. A common real-world scenario where exchangeable data arises is when data is collected from multiple environments <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.

## Key Papers and Concepts

Several papers highlight this trend:

*   **"Causal Definetti"** by C1 Guo, Victor Tu, Bernard Schölkopf, and Ference Huszár.
    *   Accepted at NeurIPS last year <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.
    *   Utilizes the Definetti theorem from probability theory <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.
    *   Demonstrates that information about the [[causal_discovery_and_analysis | causal structure]] behind observed data can sometimes be inferred if the data is exchangeable but not necessarily IID <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.

*   **"Doof" (Causal effects for exchangeable data)**.
    *   This paper was recently published and is currently under review <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.
    *   It also focuses on exchangeable but not IID data <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.
    *   The authors show that under the condition of exchangeable data, [[causal_discovery_and_analysis | causal relationships]] can be identified, and [[causal_discovery_algorithms_and_techniques | causal discovery]] and [[causal_inference_methods_and_applications | causal effect estimation]] can be performed in a broader range of circumstances <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.

*   **"Detecting Hidden Confounding in Observational Data using Multiple Environments"** by Rickard Karlsson and Jesse K.
    *   Published in 2022 <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.
    *   Explores the concept of multiple different environments <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.
    *   The paper reveals that hidden confounding in observational data can sometimes be detected under specific circumstances when data is available from these different environments <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

This approach offers the potential for partial identification, sensitivity analysis, or detection and adjustment for hidden variables in causal analysis <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.