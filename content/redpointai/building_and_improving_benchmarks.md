---
title: Building and improving benchmarks
videoId: czyHDP67CMw
---

From: [[redpointai]] <br/> 

When evaluating AI applications, it's recommended to start small and gradually increase complexity, always justifying progress with a rigorous return on investment (ROI) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The core question is whether the AI is making progress on what truly matters to the user <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## The Iterative Process of Benchmarking

A crucial step in this process is to [[ai_model_evaluation_and_benchmarking | build some benchmarks]] and test against them <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It's common to discover that initial benchmarks are insufficient, necessitating the creation of better ones <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This iterative approach is vital for effective [[ai_evaluation_and_benchmarking | AI evaluation]].

## Starting Your AI Experiment

The journey can begin with minimal investment, perhaps spending as little as 20 cents on platforms like OpenAI or Llama on Databricks, to litmus test whether AI is suitable for a specific task <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. There is currently a lack of predictability regarding AI's effectiveness for particular use cases <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

It's advised to approach this like a scientist engaging in data science: run an experiment <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. To maximize the chance of success, set up the experiment carefully <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> and utilize the best available model <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

Initial testing can be as simple as:
*   Prompting the model <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Manually providing a few relevant documents into the context, without relying on Retrieval-Augmented Generation (RAG), to observe the outcome <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

The goal is to determine if there's any value or "there there" before scaling up <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Advanced Steps: RAG and Fine-Tuning

If initial tests show promise, the next step might involve implementing more sophisticated RAG techniques to integrate proprietary data, as models do not inherently possess knowledge of internal enterprise information <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

Further down the line, if significant value is being generated, [[fine_tuning_models_for_better_outcomes | fine-tuning]] models becomes a consideration <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. While fine-tuning incurs a greater upfront cost, it can embed learned patterns directly into the model, leading to improved quality outcomes <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.