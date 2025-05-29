---
title: Applications and challenges of causality in generative modeling
videoId: ubSFglvhBd0
---

From: [[causalpython]] <br/> 

Bernhard Schölkopf, a distinguished professor and director at the Max Planck Institute for Intelligent Systems, highlights the critical role of [[causality_and_causal_models | causality]] in advancing [[generative_ai_and_causal_models | generative AI]] and [[machine_learning_and_causality | machine learning]], particularly for [[future_directions_for_causal_ai_and_generative_models | controllable generation]] and robust learning in dynamic environments <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. He emphasizes that many working on controllable generation don't realize its connection to [[causality_and_causal_models | causality]] <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>. Schölkopf's journey into [[causality_and_causal_models | causality]] began with a fascination for its philosophical aspects and the discovery that it could be studied with mathematical tools <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. He co-authored "Elements of Causal Inference," aiming for a modern, compact mathematical treatment of key causal ideas <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## The Need for Causality in Generative Models

Traditional [[machine_learning_and_causality | machine learning]] and [[generative_ai_and_causal_models | generative AI]] often rely on statistical representations and pattern recognition <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This approach is effective in Independent and Identically Distributed (IID) settings, where correlation statistics are sufficient <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. However, real-world scenarios frequently involve changing distributions or variables, which inherently relate to [[causality_and_causal_models | causality]] <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### Limitations of Correlational Learning
While [[large_language_models_and_causality | large language models]] demonstrate the power of correlational learning with vast datasets <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>, biological systems operate with finite training data and computational resources <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. For learning multiple tasks across changing conditions (e.g., an apple appearing the same despite changing light spectra), biological systems employ clever, modular learning strategies <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. This modularity, potentially aligning with the modular structure of the world, hints at the importance of [[causality_and_causal_models | causal]] representations <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Causality for Interventional Representations

Schölkopf draws inspiration from Konrad Lorenz's metaphor: "thinking is nothing but acting in an imagined space" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. For AI to move beyond statistical pattern recognition towards intelligent systems that can "act in an imagined space," its representations must incorporate notions of intervention and action <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This requires finding representations that permit actions and representing actions within the same space, similar to how biological systems use "efference copies" of actions to simulate their effects on the world <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### The Commutative Diagram of Intervention
A key concept is the consistency between imagining an intervention and performing it in the real world <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Schölkopf illustrates this with the example of moving an object:
> "I take an object I look at the object if I then move the object and look at it again I should get the same result as if I first looked closed my eyes and just imagined performing the intervention in my brain" <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>

This "commutative diagram" captures the consistency required for robust internal models <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.

### Internal World Models for Safe Learning
Having an internal world model allows for learning without constant risk to life <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This is crucial for complex tasks, such as understanding food preparation to avoid sickness or diagnosing the cause of an illness <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. While some tasks become automatic through correlational learning (e.g., brushing teeth), the ability to simulate interventions (e.g., brushing around a sensitive tooth) highlights the benefit of internal [[causality_and_causal_models | causal]] models <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

## Future Directions and Advice for the Causality Community

Schölkopf provides clear advice for the [[causality_and_ai_challenges_and_opportunities | causality and AI Challenges and Opportunities]] community:

*   **Develop Compelling Applications**: To convince the broader [[causality_and_machine_learning | machine learning]] community, it's essential to demonstrate the practical value of [[causality_and_causal_models | causal]] models through compelling applications <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   **Embrace Generative Modeling**: The [[causality_and_ai_challenges_and_opportunities | causality and AI Challenges and Opportunities]] community should actively work at the [[intersection_of_causal_ai_and_generative_ai | intersection of causal AI and generative AI]] <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. This includes understanding and training high-performance [[generative_ai_and_causal_models | generative models]] and integrating [[causality_in_large_language_models | causality in large language models]] in interesting ways <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
*   **Go Deep into Problems**: When choosing a research area, select problems that are not yet "beaten to death" <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>. Once chosen, delve deep, as persistent effort will reveal intriguing insights, even if the initial problem isn't solved directly <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.

The goal is to bridge the gap between low-level physical descriptions (like differential equations) and high-level statistical models, using structural [[causality_and_causal_models | causal models]] as an intermediate, interpretable layer <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>. This requires understanding how to abstract physical systems into [[causality_and_causal_models | causal]] ones and thinking about "mechanisms" rather than just statistical dependencies <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. Recent work on stochastic differential equations for [[causality_and_causal_models | causality]] addresses challenges like time-series data and causal loops <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.