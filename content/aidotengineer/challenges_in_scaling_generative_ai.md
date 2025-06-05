---
title: Challenges in scaling generative AI
videoId: wHhlvcQgi9M
---

From: [[aidotengineer]] <br/> 

The biggest challenge in scaling generative AI workloads is evaluations <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. While concerns like cost, hallucinations, accuracy, and capacity frequently arise, a lack of evaluations is identified as the number one issue across all workloads <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Evaluations are considered the "missing piece" to scaling Generative AI, as their implementation often unlocks the ability to scale a workload <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Case Study: Document Processing Workload

In July 2024, an AWS Principal Applied AI Architect was called in to assist a customer with a document processing workload <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This project had been ongoing for six to twelve months with six to eight engineers, but its accuracy was only 22% <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The core issue discovered was the complete absence of evaluations <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

After an [[evaluating_generative_ai_workloads | evaluations]] framework was designed and implemented, it became trivial to identify and fix problems <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The real [[challenges_with_current_ai_implementation | challenge]] was not increasing accuracy, but knowing where the problems were and their causes <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Within six months, the customer achieved 92% accuracy, exceeding their 90% threshold for production launch <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This led to the workload becoming the single largest document processing workload on AWS in North America at the time <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Purpose of Evaluations

The primary goal of an evaluation framework should be to discover problems <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. While generating a quality score is important, it's a secondary benefit <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. An effective framework pinpoints issues and can even suggest solutions, especially if it incorporates Generative AI reasoning <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Adopting a mindset that the framework will find errors leads to a different and more effective design compared to one solely focused on measuring performance <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Evaluations as a Success Filter

Evaluations serve as a critical filter distinguishing a "science project" from a successful project <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Teams unwilling to invest time in building a "gold standard set" for evaluations, often view it as boring, and are likely to create projects that do not scale <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Conversely, successful projects, some achieving 100x ROI or significant cost reductions, are characterized by teams eager to invest substantial time in building robust evaluation frameworks <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Overcoming Generative AI Evaluation Challenges

Traditional AI/ML evaluations often rely on exact numerical scores (e.g., F1 score, precision, recall) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. However, Generative AI outputs are typically free-text, which can seem daunting to evaluate mathematically <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. The human race has been grading and evaluating free text for centuries, similar to how a professor grades an essay <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Importance of Reasoning in Evaluations

Simply receiving a score (like an 'F' on an essay) without explanation is unhelpful for improvement <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. With Generative AI, it's crucial to understand the model's reasoning behind its output, akin to a good professor pointing out where a student went wrong <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

For example, in a weather summary use case, if the model incorrectly reports "sunny and bright" despite data showing rain, a simple "zero" score doesn't explain *why* <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. However, if the model explains its reasoning (e.g., "it's important to mental health to be happy, so I decided not to talk about the rain"), this insight reveals the underlying flaw <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Similarly, even if a correct output is generated (e.g., "sunny" when it's sunny), if the model's reasoning is flawed (e.g., "the weather is sunny and bright, and it's nice to be happy"), it indicates a systemic issue that could lead to failures in other cases <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. Evaluating the reasoning process helps identify and fix such problems <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Prompt Decomposition for Scalability

Prompt decomposition is a technique where a large, complex prompt is broken down into a series of chained, smaller prompts <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. This allows evaluations to be attached to each section of the prompt, making it easier to pinpoint where errors occur <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. This approach also helps determine if Generative AI is even the appropriate tool for a particular section <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

In the weather company example, a complex prompt included mathematical comparisons (e.g., "if wind speed is less than five, it's not very windy") <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. When scaled, Claude occasionally miscalculated (e.g., "wind speed is seven, seven is less than five") <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. By decomposing the prompt and replacing the mathematical comparison with a Python step, accuracy for that section became 100% <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

## Semantic Routing and its Benefits for Scaling

Semantic routing is a common pattern for [[building_scalable_ai_systems | building scalable AI systems]] <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. It involves routing an input query to different models based on its complexity <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>:
*   Easy tasks go to smaller, faster models (e.g., Nova Micro) <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   Hard tasks go to larger models <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

Attaching evaluations to each step of this process helps ensure the right model is used for the job <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. This segmented approach often significantly increases accuracy because it removes "dead space" or unnecessary instructions, reducing cost and confusion for the model <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

## Seven Habits of Highly Effective Generative AI Evaluations

Successfully scaled Generative AI workloads almost always incorporate these seven habits <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>:

1.  **Fast** <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>: Evaluations should provide results in seconds, not days or weeks <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. A target of 30 seconds for an evaluation framework run is ideal <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. This allows for hundreds of changes and tests daily, significantly accelerating the pace of innovation and accuracy improvements <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. This speed is achieved by using Generative AI as a judge and processing test cases and judgments in parallel <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
2.  **Quantifiable** <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>: Effective frameworks produce numerical scores <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. While scores may have some "jitter," this can be mitigated by having numerous test cases and averaging the results <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
3.  **Numerous** <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>: A diverse and comprehensive set of test cases is essential to cover all use cases and understand the project's scope <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. Building 100 test cases is a useful rule of thumb, ensuring core use cases have many examples while edge cases have a few <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. This process can even help teams clarify product design by defining what questions should be answered and what should be redirected <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
4.  **Explainable** <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>: Evaluations should provide insight into *how* the model reached its output and *how* the judge reasoned its score <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. This requires engineering the "judge prompt" with clear instructions and a rubric, similar to a professor grading an essay <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
5.  **Segmented** <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>: Almost all scaled workloads involve multiple steps, meaning each step needs to be evaluated individually <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. This allows for determining the most appropriate and smallest model for each step (e.g., using a smaller model for semantic routing) <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.
6.  **Diverse** <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>: The test cases should cover all anticipated use cases, including those intended to be handled and those out of scope <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. This ensures the model correctly redirects out-of-scope queries <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
7.  **Traditional** <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>: Not everything needs to be evaluated by Generative AI <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. Traditional techniques remain powerful and important for certain aspects of evaluation, such as numeric outputs, database accuracy, retrieval precision (for RAG architectures), and measuring cost and latency <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.

### Evaluation Workflow

A typical evaluation workflow for Generative AI involves:
1.  **Gold Standard Set** <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>: This is the most crucial part, requiring significant investment to ensure accuracy <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>. Using Generative AI to create the gold standard is discouraged, as it can propagate errors; human review is essential even for "silver standard" sets generated by AI <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.
2.  **Generation** <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>: An input from the gold standard set is fed into the prompt template and LLM to generate an output, which includes both the answer and its reasoning <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.
3.  **Judging** <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>: The generated output is compared against the gold standard's matching answer using a "judge prompt" <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. The judge generates a numerical score and its reasoning <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.
4.  **Categorization and Summary** <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>: Categories, often included in the gold standard set, allow for breaking down and summarizing the evaluation results for both correct and incorrect answers by category <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. This provides clear insights into performance trends and areas needing improvement <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.