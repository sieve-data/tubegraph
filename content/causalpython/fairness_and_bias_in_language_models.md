---
title: Fairness and bias in language models
videoId: sljBU_HFnFs
---

From: [[causalpython]] <br/> 

Research presented at the Triple AI conference in Vancouver explored the challenges of fairness and bias within [[large_language_models | large language models]] (LLMs) and potential solutions. This work investigates how biases emerge from training data and methods to mitigate them <a class="yt-timestamp" data-t="18:49:00">[18:49:00]</a>.

## Sources of Bias in LLMs

One significant source of bias in [[large_language_models | LLMs]] stems from the data they are trained on <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. Emily McMillan, an independent researcher, highlights that while [[large_language_models | LLMs]] are trained on vast amounts of data, this data is ultimately a subsampled representation of the real world <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

> "If there's sampling then there is potential for sample selection bias" <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>
> — Emily McMillan

This sample selection bias can lead to "missing data problems," where important information, possibly considered "common sense reasoning" by humans, is absent because "no one's taking the time to write down what is obvious" <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. Researchers are encouraged to consider the data generating process and not assume data sets are independently and identically distributed (IID), regardless of size <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

## Mitigating Bias in LLMs

Abd Rahman Zed, a PhD candidate at Mila, focuses his research on [[adversarial_robustness_and_fairness_in_ai_models | fairness in language models]], addressing how [[large_language_models | LLMs]] can learn biases and even exacerbate existing societal biases <a class="yt-timestamp" data-t="18:49:00">[18:49:00]</a>. His work aims to understand why these biases occur, how to measure them, and ultimately how to mitigate them, covering biases related to gender, race, religion, and more <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>.

A paper co-authored by Zed proposes a method for reducing bias through "pruning [[large_language_models | large language models]]" <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. The core idea is that specific parts within an [[large_language_models | LLM]] are responsible for bias <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. By identifying and removing these parts, the model can become less biased <a class="yt-timestamp" data-t="19:30:00">[19:30:00]</a>.