---
title: Simulated Annealing for Optimization
videoId: SmyPTnlqhlk
---

From: [[fireship]] <br/> 

Simulated annealing is an algorithm used in optimization to find the best solution among many good ones, particularly for problems where a simple approach like a "Hill Climb algorithm" would get stuck in "local Peaks" rather than finding the true optimum <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Origin and Concept
The term "annealing" originates from metallurgy, where metals are repeatedly heated and cooled to remove defects <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This same principle is applied in the algorithm <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## How it Works
The algorithm operates in two phases:
1.  **Exploration (High Temperature)**: Initially, a high "temperature" allows the algorithm to explore freely, accepting potentially worse solutions to escape local optima <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This is analogous to imagining a mountain range with many peaks and valleys, where a simple climb would only find the nearest peak <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
2.  **Exploitation (Lower Temperature)**: As time progresses, the "temperature" is gradually lowered <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This reduction in temperature decreases the probability of accepting a worse solution, causing the algorithm to settle into better solutions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

The core of this algorithm involves a trade-off between "exploration" and "exploitation" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## Practical Applications
For instance, in a large-scale system like an Amazon warehouse, there might be numerous ways to organize inventory, with some being more efficient than others. Simulated annealing can help find the most efficient organization <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Analogy for Learning to Code
The concept of simulated annealing can also be used as an analogy for how beginners learn to code <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Initially, one explores various technologies and frameworks ("high temperature" exploration), and eventually, they find a specific area to specialize in ("lower temperature" exploitation) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This process of [[problemsolving_and_coding_practice | problemsolving and coding practice]] helps in finding a specific niche.