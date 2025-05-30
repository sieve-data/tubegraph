---
title: Starting small and building benchmarks
videoId: czyHDP67CMw
---

From: [[redpointai]] <br/> 

When approaching [[building and utilizing large language models | AI projects]], it is recommended to start small and incrementally work your way up <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This iterative process should be justified by a rigorous Return on Investment (ROI), ensuring progress is made on things that matter <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## The Scientific Approach to AI

It is often difficult to predict whether [[building and utilizing large language models | AI]] will be effective for a specific use case <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Therefore, the approach should be that of a scientist:
> "You're a scientist. This is data science in the literal sense. Go run an experiment and try it." <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

The journey can begin by spending a minimal amount, such as 20 cents, on services like OpenAI or Llama on Data Brick, to "litmus test" if [[building and utilizing large language models | AI]] is suitable for a given task <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

To give the experiment the best chance of success:
*   Try it on the best possible model available <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   Prompt the model directly <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   Alternatively, manually pull in a few known helpful documents into the context, rather than immediately implementing Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Observe the results to determine if there is inherent value <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Iterative Benchmarking

As part of [[experimenting and testing AI use cases | testing]] and evaluating AI capabilities, it is crucial to [[ai_evaluations_and_benchmarking | build some benchmarks]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Initial benchmarks may not be perfect, and the process involves:
*   Testing on existing benchmarks <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   Recognizing that those benchmarks may be inadequate <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.
*   Building better ones over time <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Scaling Up

Once initial value is identified, the next steps in scaling up an [[building and utilizing large language models | AI]] solution can include:
1.  **Implementing Hardcore RAG**: This becomes necessary when the model requires access to specific enterprise data, as it will not inherently possess this information <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
2.  **Fine-Tuning**: If significant value is being derived, fine-tuning can bake a lot of the accumulated knowledge into the model. While it may incur more upfront cost, it typically leads to better quality outputs <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.