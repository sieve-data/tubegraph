---
title: Causality in large language models
videoId: zFeAtV7AN0A
---

From: [[causalpython]] <br/> 

A recent live stream provided a summary and insights from a workshop focused on the intersection of [[causality_and_large_language_models | causality in large language models]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The event was described as a "tightly knit community" with around 100 attendees interested in the same topics <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It featured nine speakers and over 100 participants, with organizers including Alex, Dendra, Mate, Lean, Amit, and Christian <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Workshop Highlights and Key Insights

The workshop aimed to explore how [[large_language_models_and_causality | large language models]] (LLMs) intersect with causal analysis, attracting participants from both academia and industry, as well as varied backgrounds like computer science, economics, and philosophy <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Leveraging LLMs in Causal Processes
Emre Kiciman from Microsoft Research presented his paper "A New Frontier at the Intersection of [[causality_and_large_language_models | Causal and LLMs]]" <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. His talk focused on how LLMs can be helpful in the causal process, rather than whether they are formally causal themselves <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This perspective was particularly eye-opening for many attendees, especially those from academia <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. His paper was noted as one of the first to address the intersection of [[causality_and_large_language_models | causality and LLMs]] <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### The Question of Causal Models in LLMs
Judea Pearl's talk was a highlight for many <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. He posed the question: "Does [[large_language_models_and_causal_reasoning | Large Language Models]] have a causal model of the world?" and cheekily suggested, "if we can't or if they don't, who cares?" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. He argued that behavioral tests like generalizability or recovery from local perturbations could suffice, even without a complete causal model <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

Pearl also presented his "seven plus one pillars of causal inference," with the "plus one" being the emergence of meta-science and "tricky prompting" <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This concept suggests that LLMs, even if not truly causal, can provide interesting insights, exemplified by a recent paper where fine-tuned LLMs predicted experiment outcomes better than humans <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This aligns with the "causal parrots" idea, where models may talk causality but aren't inherently causal <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

### LLMs and Causal Discovery
Two contributed talks by Kai Henrik Kors and Anik Vashishta focused on [[causal_reasoning_in_language_models | causal discovery]] using [[large_language_models_and_causality | large language models]] <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. The prevalence of such talks indicates a simultaneous realization among researchers about the potential of LLMs for learning from and contributing to causal discovery, particularly regarding computational efficiency and financial cost when querying models like GPT-4 for pairwise relationships <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### Benchmarking [[Causal Reasoning in Language Models]]
Oscar Kuncoro presented a critical review of [[systematic_evaluation_of_language_models_in_causality | causal inference benchmarks for large language models]] <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Benchmarking LLMs for causality is a complex challenge, as there's often no agreement on benchmark definitions <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. A significant problem in causality, in general, is the lack of real-world applications for testing, despite causality being inherent in fields like medicine and bioinformatics <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. The difficulty in obtaining a "ground truth causal graph" due to complexity and unknown confounders further complicates benchmarking <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

### Symbolic Reasoning and Learning Shortcuts
Humean Brooks from UCLA discussed "Symbolic Reasoning for [[large_language_models_and_causality | Large Language Models]]" <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. He explored whether LLMs can perform logical reasoning and showed that while they might perform well on simple logic benchmarks, their performance drops significantly with slight modifications <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. A "mind-blowing" theorem was presented: there exist Transformer parameters that can compute the ground truth reasoning function <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. However, paradoxically, if these ideal weights are used as a starting point and the model is fine-tuned on empirical data, it will unlearn the correct solution and instead learn a shortcut <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. This highlights the ongoing focus on "shortcut learning" in machine learning <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

### Abstraction and Reasoning Tasks
Alessandro Palmarini shared work comparing humans, GPT-4, and GPT-4V on abstraction and reasoning tasks <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. Results indicated that GPT-4 struggled with abstraction and reasoning tasks, achieving only about 25% accuracy on the Arc Benchmark, performing worse than humans even after extensive prompting <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. This benchmark could potentially be modified for [[systematic_evaluation_of_language_models_in_causality | causal evaluation]] <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

### Learning Causal Strategies from Passive Data
Andrew Lampinen from Google DeepMind presented on "Learning Active Causal Strategies from Passive Data" <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. He clarified that while LLMs are trained on "passive" data, this data often describes outcomes of experiments with procedures, making it "interventional" in nature <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. His work showed that a language model can learn to generalize causal strategies from such passive, interventional data under certain conditions <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. Adding explanations or allowing interaction with the environment can significantly enhance performance <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>. However, current training regimes and datasets might not be sufficient for this <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>. This research opens new avenues for a [[unique_integration_of_causality_with_deep_learning_and_language_models | unique integration of causality with deep learning and language models]] <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>.

### Benchmarks from Real-World Narratives
Angelica Romano's talk addressed "Assessing the Strength of Causal Relationships between Real-World Events" using benchmarks from natural language narratives <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>. This work, including the Causal Reasoning Assessment Benchmark (CRAB), provides real-world, curated data, which is crucial given the current reliance on synthetic data in the causal community <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

## Participant Survey Results

A survey conducted before and after the workshop revealed interesting shifts in participants' beliefs about [[causality_and_large_language_models | causality in large language models]]:

1.  **"Do you believe that LLMs can reason causally?"**
    *   Before: Almost 50/50 <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>
    *   After: Approximately 2/3 believed they *cannot* vs. 1/3 who believed they *can* <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. This indicates a shift towards more skepticism regarding LLMs' causal reasoning capabilities <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

2.  **"Are implicit causal World models part of what LLMs have learned?"**
    *   Before: 75-76% said Yes <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>
    *   After: 63% said Yes, and 36% said No (up from 23% before) <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.

The increased skepticism is viewed positively, as it encourages further research into these questions <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. There is a perceived paradox where a majority believe LLMs have learned implicit causal models, yet a growing number doubt their ability to reason causally. This aligns with the "causal parrots" idea: LLMs may have an inherent notion of causality but don't necessarily "know" what causality is or spit out causal facts <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.

## Future Plans

The organizers are considering a follow-up [[workshop_on_large_language_models_and_causality | workshop on large language models and causality]] at a major conference <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. There's also an open question regarding the potential of using models like Mamba for [[causal_reasoning_in_language_models | causal inference]], as most discussions have focused on Transformer-based models like the GPT family <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.