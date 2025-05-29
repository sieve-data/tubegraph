---
title: Approaches for studying intelligence in biological systems
videoId: ubSFglvhBd0
---

From: [[causalpython]] <br/> 

Studying intelligence often involves looking at natural intelligence, particularly in the animal kingdom, as these are the most compelling current examples of realized intelligence <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Thinking as Acting in an Imagined Space
Conrad Lorenz, a pioneer in the study of animal behavior (ethology), offered a significant metaphor: thinking is "nothing but acting in an imagined space" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This concept suggests that intelligence involves the ability to perform actions within an internal, simulated environment. For artificial intelligence (AI) to move towards this capability, its representations must become interventional, allowing for actions within the representation <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. These representations need to incorporate notions of intervention and action, enabling an AI to simulate the world and its own actions within it <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

## Biological Constraints and Learning Strategies
A key characteristic of biological systems is their finite training data and computational resources, unlike large machine learning models that can train on vast datasets like the entire internet <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. This constraint forces biological systems to learn more cleverly and efficiently <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

Due to limited resources, biological systems tend to:
*   **Reuse learned modules**: Once a module or task is learned, it is often reused across multiple contexts (e.g., color consistency mechanisms for recognizing apples, pears, and people under varying light conditions) <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Learn in a modular fashion**: This contrasts with modern AI, which often scales up system size without being forced to develop modularity <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Exhibit structural similarities**: The modules learned by biological systems might structurally correspond to modules in the physical world, even if the system doesn't understand the underlying physics (e.g., retinal gain control adapting to varying brightness) <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## The Role of Causality and Internal Models
While [[symbolic_and_neural_approaches_in_ai | correlational learning]] is powerful and accounts for much of what biological brains do (especially for fast reactions) <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>, [[causal_ai_and_its_application_in_different_sciences | causal models]] are crucial for learning efficiently with finite data <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

Internal world models allow systems to learn without constantly risking their lives <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. This enables:
*   **Simulated interventions**: Imagining the outcome of an action (e.g., how an object would look if moved) before performing it in the real world <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This aligns with physicist Heinrich Hertz's idea that an internal model's evolution of an object should match the real-world evolution of that object <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Counterfactual reasoning and credit attribution**: Analyzing past events to identify causal factors (e.g., determining what caused sickness after eating) <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.
*   **Cultural learning**: The ability to explain principles and show examples (e.g., teaching children how to hunt) suggests the use of underlying models <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.

However, not all tasks require explicit causal reasoning. Many tasks, like brushing teeth, become automatic and no longer require an internal model for simulation once learned <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>. The balance between correlational and causal reasoning is a deep question in intelligence <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

## Philosophical and Empirical Perspectives
Donald Hoffman's evolutionary simulations suggest that perceiving reality in a biased way, favoring fitness outcomes, might be a more successful evolutionary strategy than an unbiased perception of reality <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This could explain why human simulation abilities are good in some cases but fail in others, as explicit simulations are resource-intensive <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

## Biological Mechanisms and Physics
From a physics perspective, understanding causal systems can be approached at multiple levels. While statistical dependencies are one level, differential equations represent the gold standard, allowing for simulation and reasoning about interventions and initial conditions <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. [[comparison_of_dynamical_systems_with_computational_models_in_cognitive_science | Structural causal models]] can be seen as an intermediate level, simplifying aspects of machine learning while retaining the ability to understand interventions, and are ideally consistent with underlying physical reality <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>.

The concept of "mechanisms" is central to understanding causality. Mechanisms are considered a lower level than statistical dependencies, representing the underlying physical processes that give rise to observed correlations <a class="yt-timestamp" data-t="00:25:19">[00:25:19]</a>. This view, shared by some computer scientists like Judea Pearl, emphasizes that causal systems are physically realized <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>. Research into "independent mechanisms" aims to capture how causal systems are physically realized in the world <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.