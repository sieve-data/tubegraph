---
title: Interplay between physics and causal inference
videoId: ubSFglvhBd0
---

From: [[causalpython]] <br/> 

Bernhard Schölkopf, a prominent figure in machine learning and causality, has a deep background in physics and mathematics, which significantly influences his approach to [[causal_inference_concepts_and_applications | causal inference]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. His journey into the field of causality was sparked by a philosophical interest in the topic, coupled with a fascination that it could be rigorously studied using mathematical tools <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. He later realized that many open problems in machine learning are inherently connected to causality, viewing them as intertwined rather than separate <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Physics Perspective in Causal Inference

Schölkopf, along with his co-authors Dominique Janzing and Jonas Peters, who also have physics backgrounds, imbued their book "Elements of Causal Inference" with a perspective close to physics <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a> <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. This approach considers systems on multiple levels of description.

### Modeling Systems on Multiple Levels

In physics, the "gold standard" for modeling a system involves coupled systems of nonlinear partial differential equations <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>. Such models allow for simulation, reasoning about interventions, and understanding different initial conditions <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. Machine learning, by contrast, often operates at the level of statistical dependencies or correlations <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

Schölkopf views structural causal models (SCMs) as an intermediate level of description <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>. SCMs aim to retain the simplicity of machine learning methods—allowing learning from data without a full mechanistic understanding—while still providing enough structure to reason about interventions <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. The ultimate goal is for these causal models to be consistent with the underlying physical reality, as described by more detailed differential equations <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. He is interested in understanding how a physical system described by differential equations can be abstracted into a structural causal model <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.

### Mechanisms vs. Statistical Dependencies

From a physics-inspired viewpoint, [[causal_inference_and_its_applications | causality]] is about understanding mechanisms rather than just statistical dependencies <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. Mechanisms are considered to be a "lower" level that gives rise to statistical dependencies, essentially being physical processes <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. This concept aligns with how other computer scientists, such as Judea Pearl, view causality in terms of mechanisms <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.

The idea of independent mechanisms—where causal systems are realized physically in the world—is also a significant aspect of Schölkopf's work, heavily inspired by physics <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

### Causality in Dynamical Systems

A recent development in [[causality_in_dynamical_systems | causality in dynamical systems]] involves a new formalism based on stochastic differential equations <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. This work, conducted with Lasse Laub, is motivated by several practical considerations:
*   The prevalence of time-series data in many real-world problems, especially biological ones <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.
*   The challenge of systems that do not form a directed acyclic graph (DAG) and may contain loops <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. Unrolling these loops in time raises questions about the optimality of structural causal models <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.

This framework introduces a "kernel deviation from stationarity," aiming to see how much of the causal formalism can be retained in time-dependent settings <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

## Intelligence and Causal Representations

Schölkopf draws a parallel between human and animal intelligence and the need for causal representations in AI <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. He cites Konrad Lorenz's metaphor that "thinking is nothing but acting in an imagined space" <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. Current AI, particularly generative AI, largely relies on statistical representations for pattern recognition <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. However, to move towards truly intelligent systems that can "act in an imagined space," representations must become "interventional" <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This means representations need to include a notion of intervention and action, which inherently moves them towards causality <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

Biological systems offer insights into this, particularly the concept of "efference copies" in the brain—copies of actions our brain produces to affect the outside world <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. Representing both external information and internal actions allows for the development of an internal world model that can simulate actions and their outcomes <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This internal model enables learning "without having to risk your life every time" <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

## Future Directions and Advice

Schölkopf advocates for the [[industrial_applications_of_causal_inference | causal inference]] community to focus on creating compelling applications to convince the broader community of its importance <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>. He particularly emphasizes the intersection of causality and generative modeling, noting that many working on controllable generation are unaware of its connection to causality <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. He encourages researchers, especially young students, to engage with high-performance generative models and integrate them with causal principles <a class="yt-timestamp" data-t="00:32:48">[00:32:48]</a>.

His advice for success in complex fields like causality, physics, or mathematics is twofold:
1.  **Pick a good problem**: Choose an area that is not "beaten to death," where there's still ample room for novel contributions <a class="yt-timestamp" data-t="00:33:49">[00:33:49]</a>.
2.  **Go into depth**: Once a problem is chosen, don't be afraid to delve deeply into it. Even if the initial goal isn't achieved, persistent exploration will likely uncover something intriguing and interesting <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.