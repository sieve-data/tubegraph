---
title: Causal AI and machine learning intersection
videoId: ubSFglvhBd0
---

From: [[causalpython]] <br/> 

The [[causality_in_ai | Causal Bandits podcast]] explores the burgeoning intersection of [[causal_inference_and_machine_learning | causality and machine learning]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This field is witnessing a growing community of researchers and practitioners <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, driven by the recognition that many challenging open problems in [[integration_of_causal_thinking_in_machine_learning | machine learning]] are fundamentally connected to [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Bernhard Schölkopf's Journey to Causality

Bernhard Schölkopf, a prominent figure in the field and Director at the Max Planck Institute for Intelligent Systems, initially gravitated towards [[causality_in_ai | causality]] after encountering Judea Pearl's theory of [[causal_inference_and_machine_learning | causal inference]] decades ago <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Although he was working on kernel methods at the time and didn't immediately shift his research <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>, a later collaboration with Dominique Janzing and a persistent student eventually drew him into the field <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. He came to view [[causality_in_ai | causality]] not as a separate discipline, but as a crucial pathway for making progress on fundamental problems in [[causal_inference_and_machine_learning | machine learning and inference]] <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### "Elements of Causal Inference"

Schölkopf co-authored "Elements of Causal Inference" with Dominic Janzing and Jonas Peters <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The motivation for the book was to provide a modern, reasonably compact treatment of the main ideas of [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Upcoming Book: Causal Representation Learning

A new book on [[advancements_in_causal_modeling_and_ai | Causal Representation Learning]] is currently in progress <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This work extends beyond basic [[causality_in_ai | causality]] to explore the integration of causal thinking with modern [[integration_of_causal_thinking_in_machine_learning | machine learning]] techniques, particularly in representation learning and high-dimensional generative models <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

In traditional [[causal_inference_and_machine_learning | machine learning]] with Independent and Identically Distributed (IID) data, statistical dependencies and correlations are sufficient <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. However, in real-world scenarios where conditions or variables change, [[causality_in_ai | causality]] becomes essential <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. The book focuses on scenarios where the entities to be causally modeled are not explicitly given in high-dimensional data (e.g., identifying objects in a scene from pixels) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Learning causal representations involves understanding how data changes under interventions or varying conditions, providing clues for proper data representation <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

This approach contrasts with classical AI, which often assumes symbols are already given <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Learning causal representations is akin to discerning the pieces and moves on a chessboard just by observing gameplay, a problem potentially harder than playing the game itself <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

## Statistical vs. Causal Representations in AI

Current AI and generative AI models heavily rely on statistical representations, identifying patterns and correlations for large-scale pattern recognition <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. While impressive, these systems primarily excel at pattern matching <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. To advance towards more robust and intelligent systems, representations must become "interventional," allowing for actions within an imagined space, a concept central to the [[causality_in_ai | causality]] field <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

## Biological Inspiration for Causal AI

Natural intelligence systems, particularly in the animal kingdom, offer compelling examples of intelligence <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Konrad Lorenz's metaphor that "thinking is nothing but acting in an imagined space" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a> highlights the need for AI representations to include notions of intervention and action <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

Biological systems offer several insights for [[causal_ai_and_its_application_in_different_sciences | Causal AI]]:
*   **Finite Training Data:** Unlike large language models that train on vast datasets, biological systems operate with finite resources, necessitating clever learning strategies <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Modularity and Reuse:** Biological systems learn in a modular fashion, reusing learned modules across different tasks and changing environments (e.g., color consistency across varying light conditions) <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. This modularity might reflect structural similarities in the world itself <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   **Internal World Models:** Having an internal world model allows learning without constantly risking one's life, enabling simulation of actions and their consequences <a class="yt-timestamp" data-t="00:30:56">[00:30:56]</a>. This "simulating the world" ability, while not always perfect, is crucial for complex tasks and credit attribution <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.

## The Role of Physics in Causal Thinking

Physics informs the understanding of [[causality_in_ai | causal systems]] by allowing descriptions at multiple levels <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. While statistical dependencies are one level, differential equations offer a "gold standard" for mechanistic understanding, allowing simulation and reasoning about interventions <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>. Structural causal models (SCMs) sit between these extremes, aiming to preserve the simplicity of [[causal_inference_and_machine_learning | machine learning]] methods while enabling reasoning about interventions <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>.

From a physics perspective, [[causality_in_ai | causality]] is fundamentally about "mechanisms" rather than just statistical dependencies <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. Mechanisms are viewed as underlying physical processes that give rise to statistical dependencies <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. The concept of independent mechanisms, which posits additional assumptions about how causal systems are physically realized, is also heavily inspired by physics <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

Schölkopf's work also includes a new formalism for [[causality_in_ai | causality]] based on stochastic differential equations, motivated by the prevalence of time series data in practice and the challenge of loops in causal graphs <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.

## Future Directions for Causal AI

For the [[causality_in_ai | causality]] community, a key focus should be on developing compelling applications to demonstrate the value of [[causal_ai_in_business_applications | causal AI]] beyond philosophical arguments <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>. There is a strong need to engage with generative modeling, a hot topic in [[causal_inference_and_machine_learning | machine learning]]. Many working on controllable generation are unknowingly grappling with issues related to [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a>. Therefore, the [[causality_in_ai | causality]] community must actively work at the intersection of these fields, leveraging neural networks and other advanced tools in a causally informed manner <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.