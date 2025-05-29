---
title: Large language models LLMs learning limitations
videoId: yqKJ9pUQ6Q8
---

From: [[causalpython]] <br/> 

[[Large Language Models and causation | Large language models]] (LLMs) have introduced new considerations into the field of artificial intelligence, particularly concerning their ability to learn and reason about causality. While they show promise in certain areas, there are notable limitations to their learning capabilities, especially in comparison to human cognition and formal causal inference methods <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

## How LLMs Acquire Causal Knowledge

Unlike traditional models that learn solely from raw observational data, LLMs are trained on vast datasets of text produced by humans <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. This means they are exposed to content authored by people who inherently possess [[Causality and Large Language Models | causal models]] of the world <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Consequently, LLMs can "copy" these human-authored models <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>, rather than learning them directly from raw data in the environment <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

This distinction implies that LLMs are not necessarily constrained by the "ladder of causation" in the same way models learning purely from data are <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. However, their learning process often results in a "salad of associations among the causal model that were authored by people" <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>, functioning as a "new black box" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a> whose internal workings are not fully understood <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.

Andrew Linaman's perspective suggests that LLMs can learn "active causal strategies from passive data" <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a> because their training data, while largely observational, also includes descriptions of experiments or human interactions that implicitly convey interventional information <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

## Observed Limitations and Challenges

### Performance on Causal Benchmarks
[[Large language models and causality | LLMs]] show varied performance on causal benchmarks <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>:
*   They perform "pretty well on some causal benchmarks" <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
*   They perform "very very bad on other causal benchmarks" <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   They perform "much much poorer" when tasked with reasoning about abstract variables instead of concrete objects or "baby world" concepts <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

### Prompting and Reasoning
Experiments with LLMs on problems like the "firing squad" demonstrate their reliance on extensive prompting <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Even when the answer is derivable from the story, repeated assumptions are often needed for the LLM to get the correct answer <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. This highlights that users are "dealing with a black box" and are essentially experimenting to find "what kind of prompt will give you the answer that you expect" <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

### Data vs. Assumptions
A common misconception is that larger datasets can compensate for a lack of assumptions in establishing true causality <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>. However, "data cannot make up for assumptions" <a class="yt-timestamp" data-t="00:50:43">[00:50:43]</a>. Limitations in causal inference often persist in the asymptotic case, even with infinite data <a class="yt-timestamp" data-t="00:51:09">[00:51:09]</a>. The *type* of data (e.g., passive observation vs. interventional data) is more critical than its sheer size <a class="yt-timestamp" data-t="00:51:15">[00:51:15]</a>. Passive observation alone, even with infinite data, cannot establish causality at higher levels of the causal hierarchy <a class="yt-timestamp" data-t="00:51:20">[00:51:20]</a>. This concept is explored further in [[impacts_of_sample_selection_bias_in_llms | discussions about sample selection bias]].

### Concerns for the Future
There is concern that the focus on [[Large Language Models and causation | large language models]] might "cover the results in inference" <a class="yt-timestamp" data-t="00:47:57">[00:47:57]</a>, potentially burying the foundational importance of causal inference <a class="yt-timestamp" data-t="00:48:14">[00:48:14]</a>. However, there is also hope that the limitations of LLMs will inevitably lead researchers to "causal questions" when seeking to improve them <a class="yt-timestamp" data-t="00:48:31">[00:48:31]</a>, ultimately amplifying the role of causal inference <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.

## Towards More Capable AI
Future artificial general intelligence (AGI) systems are expected to learn causality in a similar way humans do, by combining different levels of understanding:
*   Level two (interventions) can be learned through experiments <a class="yt-timestamp" data-t="00:53:37">[00:53:37]</a>.
*   Level three (counterfactuals) involves hypothesizing and imagination <a class="yt-timestamp" data-t="00:53:40">[00:53:40]</a>.

This accelerated learning will be possible due to "great access on data and computation" <a class="yt-timestamp" data-t="00:54:04">[00:54:04]</a>. The [[application_of_large_language_models_llms_in_causal_discovery | application of large language models LLMs in causal discovery]] and [[logical_reasoning_in_large_language_models | logical reasoning in large language models]] remain active areas of research.