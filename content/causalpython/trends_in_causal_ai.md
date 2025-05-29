---
title: Trends in causal AI
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

A significant and growing trend in [[causal_ai_and_machine_learning|causal AI]] and [[causal_ai_and_machine_learning|causal research]] is emerging, marked by an increasing number of academic papers on the topic <a class="yt-timestamp" data-t="01:49">[01:49]</a> <a class="yt-timestamp" data-t="05:17">[05:17]</a>. This trend signifies a shift towards addressing practical challenges encountered by those implementing [[causal_ai_in_medicine|causal AI]] methods <a class="yt-timestamp" data-t="05:44">[05:44]</a>.

## Characteristics of the Trend
This new direction in [[causal_ai_and_machine_learning|causal research]] is characterized by:
*   **Focus on Practical Scenarios** Instead of abstract discussions about [[Causality and AI Challenges and Opportunities|causality]], the emphasis is on specific scenarios where [[causal_inference_models_and_ai_workshops|causal inference]] or [[causal_inference_models_and_ai_workshops|causal discovery]] are of interest <a class="yt-timestamp" data-t="06:00">[06:00]</a> <a class="yt-timestamp" data-t="06:04">[06:04]</a>.
*   **Leveraging Situational Nature** Researchers are exploring creative ways to utilize the inherent nature of a situation to ensure that [[causal_inference_models_and_ai_workshops|causal inferences]] are both valid and useful <a class="yt-timestamp" data-t="06:15">[06:15]</a> <a class="yt-timestamp" data-t="06:26">[06:26]</a>.
*   **Use of Multiple Environments and Non-IID Data** A key aspect of this trend involves leveraging data from multiple environments and data that is "exchangeable but not IID" (independently and identically distributed) <a class="yt-timestamp" data-t="07:22">[07:22]</a> <a class="yt-timestamp" data-t="10:44">[10:44]</a>. This approach expands the capabilities of the [[causal_ai_in_medicine|causal toolbox]] <a class="yt-timestamp" data-t="10:50">[10:50]</a>.

## Key Publications Illustrating the Trend
Several papers exemplify this new trend by demonstrating how to achieve [[causal_inference_models_and_ai_workshops|causal inference]] even when traditional assumptions are not fully met.

### Causal Definites
*   **Authors:** C1 Guo, Victor Tu, Bernal Shulov, and Ference Husar <a class="yt-timestamp" data-t="06:37">[06:37]</a>.
*   **Publication:** Accepted at NeurIPS <a class="yt-timestamp" data-t="06:48">[06:48]</a>.
*   **Core Idea:** This paper makes use of the definetti theorem <a class="yt-timestamp" data-t="06:53">[06:53]</a>. It shows that information about the causal structure behind observed data can sometimes be inferred if the data is exchangeable, even if it is not IID <a class="yt-timestamp" data-t="07:08">[07:08]</a> <a class="yt-timestamp" data-t="07:22">[07:22]</a>. Exchangeable data is a weaker condition than IID, meaning all IID data is exchangeable, but not all exchangeable data is IID <a class="yt-timestamp" data-t="07:30">[07:30]</a> <a class="yt-timestamp" data-t="07:41">[07:41]</a>. This allows for [[causal_inference_models_and_ai_workshops|causal inference]] or [[causal_inference_models_and_ai_workshops|causal discovery]] in situations where it would otherwise be impossible with IID data <a class="yt-timestamp" data-t="07:56">[07:56]</a>.

### Doof: Causal Effects for Exchangeable Data
*   **Publication Status:** Recently published and currently under review <a class="yt-timestamp" data-t="08:25">[08:25]</a>.
*   **Core Idea:** Similar to "Causal Definites," this paper also focuses on exchangeable but non-IID data <a class="yt-timestamp" data-t="08:36">[08:36]</a>. It demonstrates that under this condition, [[causal_inference_models_and_ai_workshops|causal relationships]] can be identified, and [[causal_inference_models_and_ai_workshops|causal effect estimation]] can be performed in a broader range of circumstances <a class="yt-timestamp" data-t="08:58">[08:58]</a> <a class="yt-timestamp" data-t="09:00">[09:00]</a>. A common real-world scenario for exchangeable data is when data is collected from multiple environments <a class="yt-timestamp" data-t="08:46">[08:46]</a>.

### Detecting Hidden Confounding in Observational Data Using Multiple Environments
*   **Authors:** Rickard Carlson and Jesse K <a class="yt-timestamp" data-t="09:31">[09:31]</a>.
*   **Publication Year:** 2022 <a class="yt-timestamp" data-t="09:28">[09:28]</a>.
*   **Core Idea:** This paper explores the concept of multiple different environments <a class="yt-timestamp" data-t="09:44">[09:44]</a>. The authors show that under certain circumstances, hidden confounding in observational data can be detected if data is available from these distinct environments <a class="yt-timestamp" data-t="09:48">[09:48]</a> <a class="yt-timestamp" data-t="09:56">[09:56]</a>. This capability is significant for expanding [[causal_inference_models_and_ai_workshops|causal inference]] in situations where necessary assumptions are not fully met, potentially allowing for partial identification, sensitivity analysis, or adjustment of analysis based on detected confounding <a class="yt-timestamp" data-t="10:07">[10:07]</a> <a class="yt-timestamp" data-t="10:16">[10:16]</a>.