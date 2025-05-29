---
title: Benchmarking in causal machine learning
videoId: zFeAtV7AN0A
---

From: [[causalpython]] <br/> 

Benchmarking is a critical and often underappreciated topic within both machine learning (ML) in general and [[causal_inference_and_machine_learning | causal machine learning]] specifically <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. The definition of a benchmark itself is a point of disagreement among researchers <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. This challenge is further complicated when incorporating causality and large language models (LLMs) <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

## Challenges in Benchmarking Causal Models

A significant hurdle in benchmarking causal models is the lack of readily available real-world applications and specific testbeds <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. While causality is inherent in various fields like medicine, astronomy, and bioinformatics, obtaining true causal benchmarks remains problematic <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

Indeed, the question of a benchmark for causal models is fundamentally a question for benchmarking science itself <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. While causal models provide testable implications, it is rarely feasible to test all implications at once, except for very small models <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

There's a "layer of illusion" when comparing traditional ML to [[causal_machine_learning_compared_to_traditional_methods | causal machine learning]] <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. While traditional ML can be "tested" using metrics like accuracy and F1 scores, these tests often don't answer the core questions of interest in causality <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

Another core problem is the often unknown "ground truth causal graph" in real-world scenarios due to complexity, confounders, and noise variables <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. This makes defining and testing against a true causal graph difficult <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. Progress in benchmarking is seen as progress for the entire [[causal_inference_and_machine_learning | causal machine learning]] community <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

## Relevant Works and Perspectives

### Oscar Cio's Critical Review
Oscar Cio's talk provided a critical review of [[causal_inference_and_machine_learning | causal inference]] benchmarks for LLMs <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. His presentation gave an overview of existing benchmarks and highlighted what is missing from them <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

### Alessandro Palmarini's Work
Alessandro Palmarini, in co-authorship with Melanie Mitchell, presented work on comparing humans, GPT-4, and GPT-4V on abstraction and reasoning tasks using the ARC Benchmark <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. Their findings showed that GPT-4 struggled with abstraction and reasoning tasks, achieving only about 25% accuracy, which was lower than human performance <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. Attempts to improve performance through prompting did not significantly increase results <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. This work suggests that the ARC Benchmark, if causally modified, could serve as a valuable benchmark <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

### Angelica Romano's Work: CRAB
Angelica Romano's talk focused on assessing the strength of causal relationships between real-world events, which is also a benchmark-related topic <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. Her work introduced the Causal Reasoning Assessment Benchmark (CRAB), which uses real-world data from natural language narratives <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>. This dataset was curated with the help of Mechanical Turk <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>. The CRAB benchmark offers a clean and curated real-world dataset, contrasting with the synthetic data often used in the causal community <a class="yt-timestamp" data-t="00:25:22">[00:25:22]</a>. Researchers are encouraged to explore this benchmark for their work <a class="yt-timestamp" data-t="00:25:37">[00:25:37]</a>.

> [!NOTE] Causal Reasoning Assessment Benchmark (CRAB)
> CRAB is a real-world, curated dataset for assessing causal relationships in natural language narratives, offering a valuable alternative to synthetic data for benchmarking [[causal_inference_and_machine_learning | causal machine learning]] models <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.

## Survey Results on LLMs and Causality

A survey conducted before and after a workshop on causality in LLMs revealed interesting shifts in participants' beliefs:

| Question                                              | Before Workshop | After Workshop |
| :---------------------------------------------------- | :-------------- | :------------- |
| Do you believe that LLMs can reason causally?         | ~50% Yes        | ~33% Yes       |
| Are implicit causal world models part of what LLMs have learned? | ~75% Yes        | ~63% Yes       |

The workshop made participants more skeptical about the causal reasoning capabilities of LLMs <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>. This increased skepticism is viewed positively as it encourages further research to answer these complex questions <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. Despite increased skepticism on direct causal reasoning, a majority still believe that LLMs implicitly learn causal models, creating a paradox that highlights the nuance of whether LLMs can "talk causality" without truly "being causal" <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>.