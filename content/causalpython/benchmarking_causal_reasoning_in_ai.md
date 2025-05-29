---
title: Benchmarking causal reasoning in AI
videoId: zFeAtV7AN0A
---

From: [[causalpython]] <br/> 

Benchmarking in the field of [[Causality in Artificial Intelligence | causal AI]] and machine learning is a complex and often underappreciated topic <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. It is crucial for assessing the capabilities of models, especially [[causal_ai_and_machine_learning | Large Language Models (LLMs)]], in understanding and performing causal reasoning <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Challenges in Benchmarking Causal Inference Models

A significant challenge in benchmarking [[Causal inference models and AI workshops | causal inference models]] for [[causal_ai_and_machine_learning | LLMs]] is the lack of a universally agreed-upon definition for a benchmark itself <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This complexity is compounded when integrating [[integration_of_causal_reasoning_in_machine_learning | causality]], and further still when involving [[causal_ai_and_machine_learning | LLMs]] <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

Oscar Cifri presented a critical review of causal inference benchmarks for [[causal_ai_and_machine_learning | LLMs]], highlighting existing gaps <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. A common issue is the scarcity of real-world applications or benchmarks for causality <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. While causality is inherent in fields like medicine, astronomy, and bioinformatics, obtaining true causal benchmarks remains difficult <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

A core problem in [[causal_ai_and_machine_learning | causality]] is the frequent absence of a ground truth causal graph, due to the complexity of real-world systems, and the presence of confounders and noise variables <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. Benchmarking causal models is akin to benchmarking science itself, where it's not feasible to test all implications of a complex model <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This contrasts with traditional machine learning, which often relies on quantifiable metrics like accuracy and F1 scores <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.

## Key Insights and Advancements

### Critical Reviews and New Benchmarks

Alessandro Palmarini's work compared humans, GPT-4, and GPT-4V on abstraction and [[Causal Reasoning in DecisionMaking | reasoning]] tasks, revealing that GPT-4 failed significantly on the ARC benchmark, achieving only around 25% accuracy <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. This benchmark could potentially be modified to serve as a causal benchmark <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

Angelica Romano presented a talk on assessing the strength of causal relationships between real-world events, focusing on benchmarks derived from natural language narratives <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>.

> [!NOTE] CRAB Benchmark
> The Causal Reasoning Assessment Benchmark (CRAB) is a real-world, nicely curated dataset, developed with the help of Amazon Mechanical Turk <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>. It offers a valuable resource for the causal community to move beyond synthetic data for testing models <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. Researchers are encouraged to explore and utilize this benchmark in their work <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>.

### The Impact of Benchmarking

Progress in benchmarking is considered vital for the advancement of the entire [[challenges_and_advancements_in_causal_ai | causal AI]] community <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. Honest assessment through benchmarking allows for a clearer understanding of both traditional and [[causal_ai_and_machine_learning | causal machine learning]]'s true capabilities <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

### Survey Results on LLMs and Causal Models

A survey conducted before and after a workshop on [[Causality Robustness and Fairness in AI Models | causal AI]] showed a shift in participant beliefs regarding [[Causality in Artificial Intelligence | LLMs]]' causal reasoning capabilities <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.

Initially, opinions on whether [[Causality in Artificial Intelligence | LLMs]] could reason causally were almost 50/50 <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. After the workshop, this shifted to approximately two-thirds believing they could, and one-third believing they could not <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

Regarding whether implicit causal world models are part of what [[Causality in Artificial Intelligence | LLMs]] have learned, 75-76% initially said yes <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>. After the workshop, 63% maintained this belief, while 36% disagreed (up from 23% before) <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. This suggests the workshop made participants more skeptical about the full causal capabilities of [[Causality in Artificial Intelligence | LLMs]] <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. This skepticism is viewed positively, as it encourages further research into these questions <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.