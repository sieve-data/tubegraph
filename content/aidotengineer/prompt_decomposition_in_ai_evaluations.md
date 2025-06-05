---
title: Prompt decomposition in AI evaluations
videoId: wHhlvcQgi9M
---

From: [[aidotengineer]] <br/> 

Prompt decomposition is a technique where a large, complex prompt is broken down into a series of smaller, chained prompts <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. While not exclusive to evaluations, this method is frequently applied within their context <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Why Use Prompt Decomposition?
The primary challenge with evaluating large, complex prompts is that an evaluation can typically only be attached to the entire prompt, providing an overall score without pinpointing specific issues <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>, <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This makes it difficult to understand where errors originate within a complex sequence of instructions <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

By breaking down a prompt:
*   **Pinpoint Errors**: You can attach an evaluation to each section of the prompt, allowing you to identify which specific part is performing well and which is not, thus directing where to focus improvement efforts <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>, <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Optimize Tool Selection**: It helps determine if generative AI is even the most appropriate tool for a particular part of the prompt <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
*   **Improve Accuracy**: By removing "dead space" or "dead tokens" (unnecessary instructions for a given sub-task), evaluations often show a significant increase in accuracy <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>, <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. This also reduces cost and opportunities for the model to get confused <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>, <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

## Practical Example: Weather Summary Workload
Consider a meteorology company that used a single, large prompt to create summaries of local weather based on sensor data <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>, <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. This prompt contained various instructions, including a conditional logic to determine windiness (e.g., if wind speed is less than 5, it's not very windy; if more than 5, it's windy) <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>, <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

While this worked well in a proof-of-concept (POC) stage, during scaling, the generative AI model (Claude) incorrectly processed the mathematical comparison about 2-3% of the time, leading to errors like "the wind speed is seven, seven is less than five, so it's not windy" <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

The solution involved a series of prompt decompositions <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. For the mathematical comparison, instead of relying on the generative AI, a Python script was integrated into the chaining steps <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. Python is "perfectly accurate" for such comparisons, whereas generative AI is not needed <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. This change improved the accuracy of that specific step to 100% <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

## Segmented Evaluations
[[evaluating_and_optimizing_ai_agents_and_workflows | Evaluations]] within a prompt decomposition framework are described as "segmented" <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. This means that each individual step in a multi-step workload is evaluated separately <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. This is particularly useful because:
*   **Model Selection**: It allows for evaluation of which model is most appropriate for each specific step <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>, <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. For instance, a smaller, faster model like Nova Micro might be suitable for simpler tasks like semantic routing that only require a numeric output <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>, <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>.
*   **Cost Efficiency**: By proving which minimal model is effective for each step, costs can be optimized <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

### Semantic Routing
[[evaluating_and_optimizing_ai_agents_and_workflows | Semantic routing]] is a common pattern that exemplifies prompt decomposition <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. In this pattern, an incoming query or input is first routed based on the type of task it represents <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. An easy task might be directed to a small model, while a difficult task goes to a larger model <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>, <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Attaching evaluations to each step in this process allows for precise measurement of accuracy and efficiency <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.