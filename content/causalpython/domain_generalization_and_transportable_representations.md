---
title: Domain Generalization and Transportable Representations
videoId: Y4wMksHyMFg
---

From: [[causalpython]] <br/> 

Kevin Sha, a fifth-year PhD student at the Causal AI Lab at Columbia University, discusses his colleagues' work on "transportable representations for domain generalization" at AAAI 2024 <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## The Problem: Domain Generalization

In statistical tasks like classification, a model is trained on a "source domain" but needs to be used in a "target domain" which is different <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. If a model blindly uses all features from the source domain, it may not produce accurate results in the target domain <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The goal is to develop a classifier capable of generalizing across different environments <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Transportability and Representation

The concept of "transportability" is central to this work, defined as being invariant across domains <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The aim is for the classifier itself to be invariant across domains <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

While using only causal features might seem like a straightforward approach for invariance <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, it's not always the best strategy <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Often, more information can be leveraged to achieve better generalization <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The paper proposes mapping features (X) to a representation (R) such that the prediction of 'y' given 'R' is transportable and invariant across domains <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This representation (R) can be more informative than just the causal parents while remaining transportable, leading to improved predictions in the target domain <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Without a Causal Graph

The paper's first half explains how to achieve this with some knowledge of causal mechanisms <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The second half addresses scenarios where a causal graph is unavailable, requiring other statistical assumptions based on available data <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Even without a causal diagram, guarantees can be provided for obtaining an invariant representation across domains <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Real-World Impact

This work is crucial for real-world applications where data cannot be collected directly in the intended domain of use <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. An example is healthcare, where studies might be conducted in a lab setting, but the model needs to apply to humans <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Ignoring domain differences can lead to inaccurate results <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Leveraging [[Large language models and causality | causal understanding]] of a system is vital for achieving strong predictive performance even when domains differ <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.