---
title: exchangeable data versus IID data in causal inference
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

A notable trend in [[causal_inference_and_machine_learning | causal AI]] research focuses on addressing [[causal_inference_in_practical_applications | practical challenges]] in implementing causal methods, moving beyond abstract theoretical considerations <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This includes exploring scenarios where [[assumptions_in_causal_inference | causal inferences]] can remain valid and useful even when traditional assumptions, such as data being Independent and Identically Distributed (IID), are not met <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Understanding IID and Exchangeable Data

*   **IID (Independent and Identically Distributed) Data**: Data is considered IID if each data point is drawn independently from the same probability distribution <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This is a common assumption in many statistical and machine learning models.
*   **Exchangeable Data**: Data is exchangeable if its joint probability distribution remains the same regardless of the order in which the data points are observed <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   **Relationship**: Exchangeable data is a weaker condition than IID <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. All IID data is exchangeable, but not all exchangeable data is IID <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   **Implication**: When data is exchangeable but not IID, it is possible to leverage this fact to perform [[causal_inference_in_practical_applications | causal inference]] or [[assumptions_in_causal_inference | causal discovery]] in situations where it would be impossible if the data were strictly IID <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## Leveraging Exchangeable Data for Causal Inference

A key scenario where exchangeable data, particularly non-IID exchangeable data, arises is when data is collected from [[time_series_designs_and_causal_inference | multiple environments]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Research shows that under the condition of exchangeable data, it is possible to identify causal relationships, perform [[assumptions_in_causal_inference | causal discovery]], and estimate [[causal_inference_and_individual_treatment_effects | causal effects]] in a broader set of circumstances <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

This approach expands the capabilities of [[causal_inference_in_practical_applications | causal inference]], particularly in situations where all [[assumptions_in_causal_inference | necessary assumptions]] are not met <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For instance, in the presence of [[assumptions_in_causal_inference | hidden confounding]], leveraging multiple environments with non-IID exchangeable data can allow for:
*   Partial identification <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>
*   Sensitivity analysis <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>
*   Detection of confounding, enabling adjustments to the analysis <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>

## Key Research Papers

This emerging trend is exemplified by several papers:

*   **"Causal Definites"** by C1 Guo, Victor Veitch, Bernhard Schölkopf, and Ferenc Huszár: This paper, accepted at NeurIPS, demonstrates that information about the causal structure can sometimes be inferred from data if it is exchangeable but not IID, by utilizing the de Finetti theorem <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **"Doof: Causal Effects for Exchangeable Data"**: This paper further explores [[causal_inference_and_individual_treatment_effects | causal effects]] for exchangeable data, showing that causal relationships, discovery, and effect estimation can be identified under this condition <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **"Detecting Hidden Confounding in Observational Data Using Multiple Environments"** by Rickard Carlson and Jesse Koye: Published in 2022, this work shows that hidden confounding in observational data can be detected under certain circumstances if data is available from multiple different environments <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

This focus on leveraging multiple environments and non-IID data signifies an expansion of the [[causal_inference_in_practical_applications | causal toolbox]] to make more robust [[causal_inference_in_practical_applications | causal inferences]] <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.