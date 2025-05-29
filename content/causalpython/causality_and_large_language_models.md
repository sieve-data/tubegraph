---
title: Causality and Large Language Models
videoId: Y4wMksHyMFg
---

From: [[causalpython]] <br/> 

This article summarizes discussions from AAAI 2024, Part 2, focusing on the intersection of [[Causality and large language models | causality and large language models]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Large Language Models and Causal Inference

Kevin Sha, a PhD student at Columbia University's Causal AI Lab, highlighted a paper that investigated how [[large_language_models_and_causal_reasoning | large language models]] perform when solving causal inference tasks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

*   **Dataset**: The paper introduced a dataset called "seather" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Key Finding**: The primary takeaway was that [[causal_reasoning_in_language_models | LLMs]] are generally "really bad" at solving these tasks <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Future Impact**: Despite current limitations, this work is seen as paving the way for a better understanding of how [[large_language_models_and_causal_reasoning | LLMs]] comprehend the world <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. The creation of such datasets provides valuable benchmarks for future research <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Future Research in Causality and Large Language Models

D Singi, an assistant professor at the Eindhoven University of Technology, Netherlands, indicated that [[causality_and_large_language_models | causality and large language models]] will be a major research focus for the next year or two <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

*   **Workshop Focus**: A workshop titled "Causal Pars Large Language Models" discusses [[causality_and_large_language_models | causality]], noting that while [[large_language_models_and_causality | LLMs]] "talk causality," they are "not exactly causal" <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
*   **Current State**: There has been a recent surge in papers on [[large_language_models_and_causality | LLMs and causality]], which often identify open problems without offering solutions <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.
*   **Call to Action**: Singi emphasizes the need for the community to move beyond identifying problems and actively work towards solving them <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.
*   **Long-Term Goal**: Scaling [[Causality and large language models | causality]] is a long-term objective, potentially by integrating probabilistic circuits, which offer linear inference time <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

### Learning Causality from Correlations

Singi highlighted a recent paper by Amit Sharma from Microsoft that suggests [[large_language_models_and_causal_reasoning | large language models]] can learn [[causality_and_large_language_models | causality]] under certain assumptions <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>. This finding indicates that while correlations of causal facts exist, making specific assumptions can enable [[large_language_models_and_causal_reasoning | LLMs]] to learn [[causality_and_large_language_models | causality]] <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>. This perspective contrasts with findings from the "Causal Paris paper" <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

## Message to the Causal Python Community

D Singi's message to the causal Python community is to continue their excellent work but to focus on scaling models to large models <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. He noted a current lack of benchmarks in the field, suggesting that libraries should be developed with the eventual goal of scaling models to large scales in mind <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.