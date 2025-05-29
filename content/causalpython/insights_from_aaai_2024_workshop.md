---
title: Insights from AAAI 2024 workshop
videoId: zFeAtV7AN0A
---

From: [[causalpython]] <br/> 

This article summarizes the key discussions, presentations, and community insights from the post-AAAI 2024 livestream, focusing on the intersection of [[causality_in_ai | causality in AI]] and Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.

## Workshop Overview
The [[workshop_on_large_language_models_and_causality_at_aaai_2024 | workshop]] was described as "really amazing" and "one of the better parts of the conference" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. It fostered a tightly knit community of around 100 people interested in the same topics <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The organizers included Alex, Dendra, Mate, Lean, Amit, and Christian, whose contributions were vital <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
The event featured nine speakers and over 100 participants <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Key Presentations and Insights

### LLMs in Causal Modeling
Emre Kiciman from Microsoft Research presented a paper co-authored with Amit Sharma, titled "A New Frontier at the [[intersection_of_causality_and_ai_technologies | Intersection of Causal and LLMs]]" <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. His talk explored how LLMs can be beneficial in the causal modeling process, focusing on leveraging these models for causal discovery rather than debating their inherent causal nature <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This perspective was particularly insightful for academic attendees often focused on formal aspects <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The paper was recognized as one of the first to address this intersection <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Judea Pearl's Perspective
Judea Pearl's talk was a highlight for many, noted for its profound insights and fresh perspective <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
One key question he posed was: "Does large language models have a causal model of the world?" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. His cheeky answer was, "If we can't or if they don't, who cares?" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, suggesting that behavioral tests (like generalizability or recovery from local perturbations) could be sufficient <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

Pearl also introduced his "Seven Plus One Pillars of Causal Inference," with the "+1" pillar being the emergence of metascience and "tricky prompting" <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This concept suggests that even if models aren't causal, they might offer interesting insights, as demonstrated by a recent paper showing LLMs fine-tuned on scientific data predicting experiment outcomes better than humans <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### Causal Discovery and LLMs
The workshop featured two contributed talks on LLMs and causal discovery by Kai Henrik Kors and Anik Vashishta <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. The fact that multiple researchers were simultaneously exploring this idea highlights a significant [[trend_in_causal_ai_focusing_on_practical_challenges | trend]] in the field <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. These talks explored what LLMs know, what can be learned from them, and the computational and financial efficiency of using them for causal discovery <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. The discussion touched upon various approaches, including constraint-based causal discovery <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

### Benchmarking Causal Inference
Oscar Olmo presented a critical review of causal inference benchmarks for LLMs <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Benchmarking, especially for [[causality_in_ai | causality in AI]], is a challenging and often underappreciated topic <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. The problem lies in the lack of agreement on benchmark definitions, intensified by the complexity of integrating causality and LLMs <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. The difficulty in obtaining real-world causal benchmarks, due to the unknown ground truth causal graph and the presence of confounders, was emphasized <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### Symbolic Reasoning for LLMs
Guy Van den Broeck from UCLA discussed symbolic reasoning for LLMs <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. He addressed whether LLMs can perform logical reasoning and follow deduction rules <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. A key insight was a theorem proposing the existence of Transformer parameters that can compute the ground truth reasoning function <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. However, paradoxically, if these optimally set weights are fine-tuned on empirical data, the model tends to unlearn the correct solution and learn a shortcut instead <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. This highlights the ongoing focus on shortcut learning in [[symbolic_and_neural_approaches_in_ai | machine learning]] <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

### Abstraction and Reasoning Tasks
Alessandro Palmarini presented work comparing humans, GPT-4, and GPT-4V on abstraction and reasoning tasks <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. The results showed that GPT-4 struggled with abstraction and reasoning tasks, achieving only about 25% accuracy on the ARC Benchmark, which is worse than humans <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>. Even extensive prompting did not significantly improve results <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.

### Learning Causal Strategies from Passive Data
Andrew Lampinen discussed learning active causal strategies from passive data <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. He highlighted that LLMs, when trained on data describing experimental outcomes and procedures, are essentially trained on "interventional" passive data <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. His work shows that language models can generalize causal strategies from such data under certain conditions, and performance can be enhanced by adding explanations or allowing interaction with the environment <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. Key insights include the possibility of generalization in simple cases and the current limitations of existing training regimes and datasets <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.

### Benchmarks from Natural Language Narratives
Angelica Romano presented on assessing the strength of causal relationships between real-world events, focusing on benchmarks from natural language narratives <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. Her work introduced a real-world, nicely curated dataset called CRAB (Causal Reasoning Assessment Benchmark) <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>. This benchmark is crucial for the [[causality_in_ai | causal AI]] community, as much work currently relies on synthetic data <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.

## Open Stage and Community Feedback
The workshop concluded with an Open Stage, allowing participants to share their ideas <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. Comments included:
*   Perhaps it's too early to definitively say if LLMs can reason causally, as current probing methods might be inadequate <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.
*   LLMs are fundamentally "just playing guess the next word," which questions their ability to build causal models <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>.

## Workshop Survey Results
A survey conducted before and after the workshop revealed interesting shifts in participants' beliefs:

| Question                                                       | Before Workshop | After Workshop |
| :------------------------------------------------------------- | :-------------- | :------------- |
| Do you believe that LLMs can reason causally?                  | ~50% Yes        | ~33% Yes <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a><a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a> |
| Are implicit causal world models part of what LLMs have learned? | 75-76% Yes      | 63% Yes <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a><a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a> |

> [!NOTE] Interpretation of Survey Results
> The workshop made participants more skeptical about the causal reasoning capabilities of LLMs <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. Despite a decrease in belief that LLMs can reason causally, a majority still believe that implicit causal models are learned by LLMs. This paradox aligns with the "causal parrot" concept: LLMs may talk causality but are not truly causal, possessing an inherent notion without understanding <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

## Future Plans and Announcements

### Follow-up Workshop
The organizers are planning a follow-up [[workshop_on_large_language_models_and_causality_at_aaai_2024 | workshop]] at a major conference <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. This will be announced in the coming months <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>. The question of using Mamba models for causal inference remains an open question for future exploration <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.

### Causal Bandits Podcast
A new episode of the Causal Bandits podcast with Stephen Senn, a statistician and experimenter involved in drug trials, will be released <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

### Causal Bandits Extra Episodes
Over the next few weeks, "Causal Bandits Extra" episodes will be released, featuring researchers and participants from AAAI discussing their [[causality_in_ai | causality]] work <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>. Guests include Andrew Lampinen (Google DeepMind), Scott Miller (UCLA, working with Judea Pearl on counterfactual reasoning), and Emily McMillan (Meta) <a class="yt-timestamp" data-t="00:32:34">[00:32:34]</a>.

### Book Translation
A book on [[advancements_in_causal_modeling_and_ai | causal inference]] has been translated into Spanish, titled "Inferencia Curio Causal en Python," and will be released on April 25 in Spain and Latin America <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

### Book Giveaway
A book giveaway is being held, offering three print books and three ebooks <a class="yt-timestamp" data-t="00:35:14">[00:35:14]</a>. Participants can enter by filling out a survey with the same questions asked of workshop attendees <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>. The deadline to participate is Friday, March 15, 2024 <a class="yt-timestamp" data-t="00:35:33">[00:35:33]</a>.