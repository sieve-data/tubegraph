---
title: Model ensembling in machine learning
videoId: MVWYTFs9M-s
---

From: [[hu-po]] <br/> 

Model ensembling, also known as a mixture model, is a strategy in machine learning that uses [[Model training and evaluation methods | multiple models]] to improve final performance <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This approach aims to achieve better overall results than using a single "best" model <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## How Model Ensembling Works
In a typical ensembling scenario, multiple versions of the same model are trained, often on slightly different subsets of the data <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. When given the same input, these models produce a variety of outputs <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. A selection mechanism, such as a value function, then chooses the best output from the ensemble <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### Key Characteristics
*   **Multiple Models:** The core idea is to leverage the strengths of several models rather than relying on one <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Varied Training:** Models in an ensemble can be trained on different data subsets or with slight variations in [[Finetuning machine learning models | fine-tuning]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Improved Performance:** Ensembling is particularly effective for squeezing out the last few percentage points of performance <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Examples and Applications

### GPT-4
Recent reports suggest that [[GPT4 ensemble of models | GPT-4]] is not a single [[Large language models in machine learning research | model]], but an [[GPT4 ensemble of models | ensemble of eight models]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Each of these models is estimated to have roughly 220 billion parameters <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This ensemble approach helps explain the high performance of [[GPT4 ensemble of models | GPT-4]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

This ensembling strategy also clarifies why Sam Altman frequently mentions the high inference costs associated with [[GPT4 ensemble of models | GPT-4]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. While a single model like Bard performs one inference per query <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, [[GPT4 ensemble of models | GPT-4]] reportedly performs 16 inferences for a single query <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>, <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This means inference for [[GPT4 ensemble of models | GPT-4]] could be 16 times more expensive than for Bard <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Furthermore, this ensembling strategy has been observed in OpenAI's past work, such as the 2021 paper on Codex, where they generated 100 samples per token and then filtered them down <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Kaggle Competitions
Model ensembling is very popular in Kaggle competitions, where participants aim to achieve the highest possible performance <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Competitors often train numerous versions of a model on slightly varied data subsets to maximize their final score <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.