---
title: trend in causal AI focusing on practical challenges
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

A noticeable and growing trend in [[Causality in AI | causal AI]] research is its increasing focus on practical challenges faced by individuals implementing these methods <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This shift moves away from abstract discussions of causality towards particular scenarios where [[causal discovery and inference in AI | causal inference]] or [[causal discovery and inference in AI | causal discovery]] is desired <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The aim is to leverage the unique nature of specific situations to ensure valid and useful [[causal discovery and inference in AI | causal inferences]] <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Leveraging Non-IID Data

A significant aspect of this trend involves research into leveraging non-IID (independently and identically distributed) data, specifically "exchangeable" data <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **IID Data**: Means data points are independently and identically distributed <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Exchangeable Data**: A weaker condition where IID data is a special case <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Not all exchangeable data is IID <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

When data is exchangeable but not IID, it becomes possible to perform [[causal discovery and inference in AI | causal inference]] or [[causal discovery and inference in AI | causal discovery]] in situations where it would otherwise be impossible with IID data <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. A common real-world scenario producing exchangeable data is when data originates from multiple environments <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

Under the condition of exchangeable data, researchers can identify causal relationships, perform [[causal discovery and inference in AI | causal discovery]], and estimate causal effects in a broader range of circumstances <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. This approach expands the capabilities for [[causal discovery and inference in AI | causal inference]], especially in situations where necessary assumptions (like no confounding) are not fully met <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This can lead to partial identification, sensitivity analysis, or methods to detect and adjust for confounding <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Key Research Papers

Several papers exemplify this new direction in [[advancements in causal modeling and AI | causal modeling and AI]]:

### "Causal Definiteness"

*   **Authors**: C. Guo, V. Tu, B. Schölkopf, and F. Huszár <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Publication**: Accepted at NeurIPS last year <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Concept**: Makes use of the definiteness theorem <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Contribution**: Demonstrates that information about the causal structure behind observed data can sometimes be inferred if the data is exchangeable but not IID <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### "Doof: Causal Effects for Exchangeable Data"

*   **Status**: Recently published and still under review <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Focus**: Concentrates on causal effects within exchangeable but not IID data <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Application**: Particularly relevant when data comes from multiple environments <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Contribution**: Shows that under exchangeable data conditions, [[causal discovery and inference in AI | causal relationships]] can be identified, [[causal discovery and inference in AI | causal discovery]] performed, and causal effects estimated in a broader set of circumstances <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### "Detecting Hidden Confounding in Observational Data Using Multiple Environments"

*   **Authors**: R. Carlson and J. K. <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Publication Date**: From 2022 <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Concept**: Utilizes the idea of multiple different environments <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Contribution**: Demonstrates that hidden confounding in observational data can sometimes be detected under specific circumstances, provided data from these different environments is available <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

These research directions are significantly expanding the [[Causal AI and machine learning intersection | causal toolbox]], especially by leveraging multiple environments and non-IID data to make [[causal discovery and inference in AI | causal inferences]] more robust and applicable <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.