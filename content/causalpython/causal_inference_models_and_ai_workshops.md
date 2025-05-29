---
title: Causal inference models and AI workshops
videoId: zFeAtV7AN0A
---

From: [[causalpython]] <br/> 

This article summarizes key insights and discussions from a post-Triple AI live stream, focusing on the intersection of causality and Large Language Models (LLMs). The event served as a workshop, bringing together a "tightly knit community" of around 100 people interested in the same topics, featuring "amazing invited talks" and contributed papers [01:23:00].

## Workshop Overview
The workshop was organized by Alex and Dendra, along with Lean, Amit, and Christian, whose "excellent work" made the event possible [03:01:00]. The event featured nine speakers and over 100 participants [03:51:00]. The organizers emphasized the event's story, which led to its creation, and presented a brief history of the sub-area at the intersection of causality and large language models [04:17:00].

## Key Presentations and Discussions

### LLMs as Aids in Causal Processes
Amra Kiman from Microsoft Research discussed how LLMs can be helpful in causal processes, rather than focusing on whether they are formally causal [04:41:00]. His talk, based on a paper co-authored with Amit Sharma titled "A New Frontier at the Intersection of Causal and LLMs," explored leveraging these models within a [[causal_inference_and_its_applications | causal modeling]] and [[causal_inference_and_its_applications | causal discovery]] process [04:47:00]. This perspective was particularly "eye-opening" for many participants, especially academics often focused on more formal aspects [05:45:00]. The audience included individuals from diverse backgrounds, including computer science, economics, and philosophy [06:03:00].

### Judea Pearl on LLMs and Causal Models
A highlight for many was Judea Pearl's talk, which provided "so many insights" and stunned attendees with the "quality of his thinking" [07:25:00]. Pearl posed the question: "Does large language models have a causal model of the world?" and cheekily replied, "who cares?" [08:06:00]. He suggested that [[benchmarking_causal_reasoning_in_ai | behavioral tests]] like generalizability or recovery from local perturbations could suffice, even without a complete causal model [08:25:00].

Pearl also introduced his "Seven Plus One Pillars of [[causal_inference_and_its_applications | causal inference]]", with the "+1" pillar being the emergence of "meta-science" and "tricky prompting" [08:49:00]. The concept of "meta-science" suggests that LLMs, even if not truly causal, might provide "interesting insights" [09:41:00]. Recent research indicates that LLMs fine-tuned on scientific data can predict experiment outcomes better than humans, potentially exemplifying this meta-science idea [09:52:00].

### Causal Discovery and LLMs
Two contributed talks focused on [[causal_inference_and_its_applications | causal discovery]] using LLMs: one by Kai Henrik Kors and another by Anik Vashishta (who also works with Amit Sharma) [10:46:00]. The presence of multiple talks on this topic suggests a simultaneous realization among researchers about the potential for LLMs to assist in [[causal_inference_and_its_applications | causal discovery]] [11:00:00]. Discussions included the computational and financial efficiency of querying LLMs for causal information, noting that even small network queries can incur significant costs [11:35:00]. The talks also touched upon different approaches, such as constraint-based [[causal_inference_and_its_applications | causal discovery]] and measuring uncertainty [12:10:00].

### Benchmarking Causal Inference
Oscar CIO presented a critical review of [[benchmarking_causal_reasoning_in_ai | causal inference benchmarks]] for LLMs [12:41:00]. The discussion highlighted the general difficulty of benchmarking, especially when incorporating causality and LLMs [13:05:00]. A significant challenge in causality is the lack of real-world applications for benchmarks, despite its inherent presence in fields like medicine, astronomy, and bioinformatics [13:56:00]. The question of benchmarking [[causal_inference_and_its_applications | causal models]] was equated to benchmarking science itself, noting that not all implications of complex models can be tested [14:57:00].

### Symbolic Reasoning and "Unlearning"
Guy Van Den Broeck from UCLA presented on symbolic reasoning for LLMs [17:02:00]. He questioned whether LLMs can perform logical reasoning and whether they follow rules of logical deduction [17:18:00]. While LLMs perform well on simple logic benchmarks, their performance significantly drops when benchmarks are slightly modified [17:50:00]. A "mind-blowing" theorem from his paper demonstrated that Transformer parameters can exist to compute the ground truth reasoning function [18:12:00]. However, if these models, starting with exact solutions, are fine-tuned on empirical data, they "unlearn the correct solution and will learn a shortcut" [19:00:00]. This phenomenon of shortcut learning is a major focus in machine learning [19:27:00].

### Abstraction and Reasoning in LLMs
Alessandro Palmarini presented work comparing human, GPT-4, and GPT-4V performance on abstraction and reasoning tasks, co-authored by Melanie Mitchell [20:11:00]. The results showed that GPT-4 failed significantly on abstraction and reasoning tasks within the ARC benchmark, achieving only around 25% accuracy [20:37:00]. Fine-tuning through prompting did not substantially improve results [21:02:00]. This work could serve as a valuable [[benchmarking_causal_reasoning_in_ai | benchmark]] for future research [21:11:00].

### Learning Causal Strategies from Passive Data
Andrew Lampinen discussed learning active causal strategies from passive data [21:38:00]. He highlighted that LLMs, though trained on passive data, process "outcomes of experiments with procedures described," making the data "interventional" [22:12:00]. Lampinen showed that language models can learn to generalize causal strategies from passive data describing interventional strategies [22:32:00]. Performance can be significantly enhanced by adding explanations or allowing models to interact with the environment at certain points [22:47:00]. Key insights from his paper include the possibility of generalization in simple cases and the current limitations of existing training regimes and datasets [23:11:00]. This work is conceptually related to Google DeepMind's research on agents learning causal models by learning optimal/suboptimal policies in diverse environments [23:42:00].

### Real-World Causal Relationships and Benchmarking
Angelica Romano presented on assessing the strength of causal relationships between real-world events, specifically a [[benchmarking_causal_reasoning_in_ai | benchmark]] derived from natural language narratives [24:15:00]. The "Causal Reasoning Assessment Benchmark" (CRAB) uses "real-world data," curated with the help of Mechanical Turk [24:42:00]. This clean and curated benchmark is important for the [[causal_inference_and_its_applications | causal community]], which often relies on synthetic data [25:12:00].

## Open Stage and Participant Feedback
The workshop concluded with an Open Stage, allowing participants to share their ideas and thoughts [25:59:00]. Comments included skepticism about whether it's "too early to say if those models can reason causally" and the observation that LLMs are "just playing you, just guess the next word," questioning their ability to build a [[causal_inference_and_its_applications | causal model]] [26:26:00].

## Workshop Survey Results

Participants were surveyed before and after the workshop about their beliefs regarding LLMs and causality.

**Question 1: Do you believe that LLMs can reason causally?**
*   Before workshop: Approximately 50/50 [27:16:00]
*   After workshop: Two-thirds believed yes, one-third believed no [27:21:00]

**Question 2: Are implicit causal World models part of what LLMs have learned?**
*   Before workshop: 75-76% said yes [27:46:00]
*   After workshop: 63% maintained this belief, while 36% said no (up from 23% before) [27:51:00].

> [!NOTE] The results suggest the workshop made participants "more skeptical" about LLM capabilities [28:08:00]. The organizers noted a "paradox" where a majority believe LLMs implicitly learn causal models, but a growing skepticism exists about their ability to reason causally [28:50:00]. This skepticism is considered "good" as it drives further research [28:18:00].

## Future Outlook

The organizers are considering hosting a follow-up workshop at a major conference, with announcements expected in a couple of months [29:50:00]. A question was raised regarding the possibility of using Mamba models for [[causal_inference_and_its_applications | causal inference]], which remains an open question as most discussions focused on GPT or Transformer-based models [30:10:00].