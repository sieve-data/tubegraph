---
title: detecting hidden confounding in observational data
videoId: GL1vSwhiFgc
---

From: [[causalpython]] <br/> 

A significant trend in causal AI research focuses on addressing practical challenges encountered when implementing causal methods <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This approach moves away from abstract causal theory to concentrating on specific scenarios where causal inference or discovery is needed <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The goal is to find creative ways to leverage the nature of a situation to ensure valid and useful causal inferences <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Leveraging Multiple Environments

One promising direction in this research involves utilizing data from [[exchangeable_data_versus_iid_data_in_causal_inference | multiple environments]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This approach aims to expand the capabilities of causal inference, especially in situations where not all necessary [[assumptions_in_causal_inference | assumptions]] are met, such as the presence of confounding <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Key Research Papers

Several papers highlight this trend:

*   **"Causal Definability"** by C. Guo and V. Tu, co-authored by B. Schölkopf and F. Huszár (2022 NeurIPS) <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. This paper demonstrates that it is sometimes possible to infer information about the causal structure from data, assuming the data is [[exchangeable_data_versus_iid_data_in_causal_inference | exchangeable]] but not independently and identically distributed (IID) <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Leveraging non-IID but [[exchangeable_data_versus_iid_data_in_causal_inference | exchangeable data]] allows for causal inference or discovery in scenarios where it would otherwise be impossible with IID data <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **"Doof: Causal Effects for Exchangeable Data"** (2023) further explores the use of [[exchangeable_data_versus_iid_data_in_causal_inference | exchangeable data]] for identifying causal relationships, performing causal discovery, and estimating causal effects across a broader set of circumstances <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **"Detecting Hidden Confounding in Observational Data Using Multiple Environments"** by R. Carlsson and J. K. (2022) directly addresses the challenge of hidden confounding <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This paper demonstrates that hidden confounding in observational data can sometimes be detected under specific conditions if data is available from [[exchangeable_data_versus_iid_data_in_causal_inference | multiple environments]] <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Implications for Causal Inference

The ability to detect hidden confounding through [[exchangeable_data_versus_iid_data_in_causal_inference | multiple environments]] expands the capabilities of causal inference in challenging situations <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. If confounding is detected, it allows for:

*   Partial identification <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   Sensitivity analysis <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   Adjusting analysis to reflect the presence of hidden variables <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

This new trend in causal AI, which leverages [[exchangeable_data_versus_iid_data_in_causal_inference | multiple environments]] and non-IID data, significantly expands the causal toolbox <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.