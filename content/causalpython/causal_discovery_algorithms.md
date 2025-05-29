---
title: Causal discovery algorithms
videoId: sljBU_HFnFs
---

From: [[causalpython]] <br/> 

[[Causal Discovery Algorithms and Techniques | Causal discovery algorithms]] aim to uncover causal relationships from data. Researchers are working towards developing practical algorithms that can be applied in real-world scenarios <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Adaptive Causal Discovery

A key area of research involves adapting [[Causal Discovery Algorithms and Techniques | causal discovery algorithms]] to data as it arrives over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Instead of requiring a fully specified dataset from the beginning, these algorithms can learn and update as new data streams in <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

This adaptive approach can also be applied when the underlying data-generating process is dynamical, meaning the causal relationships change over time <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. A compression-based strategy can be used to separate these different types of structures <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Challenges

Developing such general and adaptive algorithms presents several challenges:
*   **Distinguishing differences** It is difficult to differentiate between structures, especially when data is just starting to arrive <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Dynamical networks** In worst-case scenarios, if new data points consistently come from a different dynamical network, it becomes very challenging to distinguish them practically <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Impact on results** Poor distinction early on can negatively affect later results <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Real-World Impact

The hope for this work is to apply these adaptive [[Causal Discovery Algorithms and Techniques | causal discovery algorithms]] to practical problems, such as those in the [[applications_of_causal_discovery_in_biology | healthcare domain]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For instance, in disease diagnosis, where initial data might be scarce, algorithms could adapt their knowledge as more information becomes available, rather than always starting from scratch <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Computational Requirements

For score-based [[Causal Discovery Algorithms and Techniques | causal discovery]], the worst-case computational requirements still involve exponential scaling with the number of nodes <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

However, in practice, the greedy nature of the search can alleviate some of this cost <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. By building or discovering networks in a greedy fashion, and assuming the chosen score aligns with data assumptions, the approach can work well <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This greedy approach has enabled scaling to around 500 variables in sparse networks in earlier algorithms <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Assumptions

The work typically relies on functional assumptions such as nonlinear functions with additive Gaussian noise <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This is considered less restrictive than assuming linearity <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.