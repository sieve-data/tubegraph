---
title: Transportable Representations and Domain Generalization
videoId: Y4wMksHyMFg
---

From: [[causalpython]] <br/> 

This article discusses the concept of transportable representations, a key area of research for achieving model generalization across different environments. This work was presented by Kevin Sha, a fifth-year PhD student at the Causal AI Lab at Columbia University, during AAAI 2024. <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>

## The Problem: Domain Generalization

A common challenge in machine learning is applying a model trained on data from a "source domain" to a "target domain" where the data distribution is different <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For example, if you train a classification model (predicting label `y` from features `X`) using source domain data, blindly applying it to a different target domain might not yield accurate results <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The core idea of this research is to develop a classifier capable of [[role_of_causality_in_generalization | generalizing]] across varied environments <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## What are Transportable Representations?

The central concept is "transportability" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Something is considered transportable if it remains invariant across different domains <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The goal is to create a classifier that exhibits this invariance <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

A naive approach might be to use only [[Abstractions and Causal Models | causal features]], as they are often invariant <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. However, this isn't always the optimal solution; sometimes, leveraging more information beyond just causal features can lead to better [[role_of_causality_in_generalization | generalization]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The research shows it's possible to find representations that are more informative than just [[Abstractions and Causal Models | causal parents]] while still being invariant across domains <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

The process involves mapping features `X` to a [[role_of_representation_learning_in_modern_ai | representation]] `R` using a function (e.g., `five of X`), and then predicting `y` based on this [[role_of_representation_learning_in_modern_ai | representation]] `R` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The paper outlines various methods to achieve this `R` such that the prediction `y` given `R` is transportable and invariant across domains <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Achieving Transportability

The paper details how to achieve these representations:
*   **With Causal Mechanisms**: The first half of the paper explains how to obtain transportable representations when some information about the [[Abstractions and Causal Models | causal mechanisms]] is known <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Without Causal Mechanisms**: The second half addresses scenarios where explicit [[Abstractions and Causal Models | causal diagram]] knowledge is unavailable. In such cases, other statistical assumptions can be made using only the available data to still guarantee an invariant [[role_of_representation_learning_in_modern_ai | representation]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This allows for better predictions in the target domain, even without a complete [[Abstractions and Causal Models | causal graph]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Real-World Impact

This work is crucial for real-world applications where data collection in the intended deployment domain is often infeasible <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. For example, in healthcare, models might be trained on lab data but need to generalize to human patients in complex settings <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Ignoring domain differences can lead to inaccurate results <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. By incorporating a [[Abstractions and Causal Models | causal understanding]] of the system, this research enables powerful predictive performance even when the application domain differs from the training domain <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.