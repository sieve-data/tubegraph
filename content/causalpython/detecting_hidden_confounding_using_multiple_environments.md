---
title: Detecting hidden confounding using multiple environments
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

## A New Trend in Causal AI
A significant new trend in Causal AI focuses on addressing practical challenges faced during the implementation of causal methods <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This approach shifts from abstract causal reasoning to specific scenarios, aiming to leverage the unique nature of situations to ensure valid and useful [[challenges_in_identifying_causal_relationships | causal inference]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Leveraging Exchangeable Data
A key aspect of this trend involves utilizing data that is *exchangeable* but not necessarily independently and identically distributed (IID) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. While all IID data is exchangeable, not all exchangeable data is IID <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. This fact can be leveraged to perform [[causal_inference_and_discovery_with_exchangeable_data | causal inference]] or causal discovery in situations where it would otherwise be impossible with IID data <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

One real-world scenario where exchangeable data often arises is when data is collected from multiple environments <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## Detecting Hidden Confounding
One paper that aligns with this new trend is "Detecting hidden confounding in observational data using multiple environments" (2022) by Rickard Carlson and Jesse K <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. This work shows that it is possible to detect hidden confounding in observational data under certain circumstances, particularly when data is available from different environments <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

This research direction expands capabilities for [[challenges_in_causal_analysis_in_different_settings | causal inference]] in situations where not all necessary assumptions are met, such as the presence of confounding variables <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. Approaches like [[understanding_partial_identification_in_causal_analysis | partial identification]], sensitivity analysis, or detecting confounding to adjust the analysis become possible <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

This overall trend of leveraging multiple environments and non-IID data significantly enhances the causal toolbox available to researchers <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.