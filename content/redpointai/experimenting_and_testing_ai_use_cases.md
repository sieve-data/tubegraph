---
title: Experimenting and testing AI use cases
videoId: czyHDP67CMw
---

From: [[redpointai]] <br/> 

When approaching [[exploration_and_experimentation_in_ai | AI exploration and experimentation]], it is recommended to "always start small and work your way up" <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Any progression should be justified by [[evaluating_ai_through_rigorous_roi_testing | rigorous ROI]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, ensuring progress on important objectives <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Initial Experimentation and Litmus Testing
The journey into AI begins with minimal investment, such as "spending 20 cents on Open AI or on Llama on Databrick" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a> to perform a [[exploration_and_experimentation_in_ai | litmus test]] on AI's suitability for a particular task <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. It is currently difficult to predict whether AI will be effective for a specific use case <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The process should be approached scientifically, treating it as "data science in the literal sense" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. One should "go run an experiment and try it" <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, giving oneself the best chance of success <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This involves using the "best possible model you can get your hands on" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, either by direct prompting or by manually supplying a few known-helpful documents into the context, to observe outcomes <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Iterative Development and Refinement
After initial experimentation, one should assess if there is potential for further development <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This progression may lead to more advanced techniques:

*   **Benchmarking**
    *   "Build some benchmarks" and test the AI against them <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
    *   Be prepared to "realize your benchmarks suck and build better ones" <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

*   **Retrieval-Augmented Generation (RAG)**
    *   If initial tests show promise, it might be time for "hardcore RAG" <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
    *   This is crucial because the model "is not going to just have telepathy and know about my internal enterprise data" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, requiring data to be brought to bear <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

*   **Fine-tuning**
    *   If the AI is already providing value, fine-tuning can be considered <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   Fine-tuning allows "baking a lot of this into the model" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
    *   While it incurs "a little more upfront cost" <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>, it generally leads to "better quality" <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.