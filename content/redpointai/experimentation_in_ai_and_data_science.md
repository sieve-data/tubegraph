---
title: Experimentation in AI and data science
videoId: czyHDP67CMw
---

From: [[redpointai]] <br/> 

[[starting_small_in_ai_projects | Starting small]] and working iteratively is crucial when approaching AI projects <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Any progression in complexity should be justified by rigorous Return on Investment (ROI), ensuring that efforts contribute to meaningful objectives <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Iterative Testing and Benchmarking

A key part of the [[lean_startup_principles_applied_to_ai | experimental process]] involves building benchmarks and testing against them <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It's common to find initial benchmarks are inadequate, necessitating the creation of better ones <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### Litmus Testing with Minimal Investment

The journey often begins with a minimal financial outlay, such as spending 20 cents on platforms like OpenAI or Llama on Databricks <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This initial investment serves as a litmus test to determine if AI is suitable for a given task <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. There is currently limited predictability regarding an AI model's effectiveness for a specific use case <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### The Scientific Approach

Approaching AI implementation should be seen as a scientific endeavor, akin to data science <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The recommendation is to conduct experiments to find out what works <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

To give an experiment the best chance of success:
*   Try it on the best possible model available <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   Start by simply prompting the model <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Initially, manually provide relevant documents directly into the context, rather than immediately implementing complex Retrieval Augmented Generation (RAG) systems <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Observe the results to determine if the approach yields a valuable outcome <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Scaling Up and Advanced Techniques

Once initial value is demonstrated, the next step is to progressively increase complexity <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Retrieval Augmented Generation (RAG)

If manual context provision proves effective, the next step might be implementing "hardcore RAG" <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This becomes necessary when the model requires access to specific [[enterprise_use_of_ai_and_model_specialization | internal enterprise data]] that it would not inherently know <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Fine-tuning

If significant value is derived from the AI application, fine-tuning the model can be considered <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Fine-tuning allows specific knowledge to be baked into the model, potentially leading to better quality outputs <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. While fine-tuning incurs a higher upfront cost, it can yield improved performance in the long run <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This iterative and experimental approach is part of the [[creative_process_and_experimentation_with_ai | creative process and experimentation with AI]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.