---
title: Serverless architecture and its impact on costs
videoId: 1gLHnRDiIms
---

From: [[redpointai]] <br/> 

Pine Cone, a vector database, redesigned its solution to a serverless architecture due to rapid scaling and overwhelming demand <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>. This shift was a necessity as the company "literally couldn't handle the load" with their previous setup <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.

## Cost Efficiency for Customers

The serverless architecture is "maybe two orders of Mag more efficient" <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a> than their previous solution. This improvement has significantly impacted customer costs:

*   For users with millions of vectors, the monthly cost can be less than $100 <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Pine Cone excels at managing "hundreds of millions [or] billions scale" <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a> embeddings, especially for SaaS providers. These companies often need to handle up to 10 billion embeddings across thousands of partitions [[enterprise_ai_deployment_models|cost effectively]] <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   The multi-tenant serverless workload allows for costs as low as "a dollar a year" or even "50 cents a year" per paying user <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This focus on unit economics is crucial for companies building products <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   Customers often miscalculate costs, estimating tens of thousands of dollars per month when the actual cost might be hundreds <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>. Incorrect cost estimations can prevent companies from even starting a project <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>. This highlights the importance of [[cost_efficiency_and_accessibility_in_ai|cost transparency]] and accurate projections.

## Business Impact and Challenges

The transition to a serverless model was "very painful" for Pine Cone as a company <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>. While workloads grew faster, revenue was impacted because the product became significantly cheaper <a class="yt-timestamp" data-t="00:37:50">[00:37:50]</a>.

*   This could mean leaving "more than half of our revenue on the table" <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>.
*   For some extreme cases (e.g., Pharma, storage-heavy workloads), cost reductions could be 70%, 80%, or even 90% <a class="yt-timestamp" data-t="00:38:54">[00:38:54]</a>. Some customers who paid $100,000 now pay $2,000 a year <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>.
*   Despite the financial impact, the company believes it was the "right thing for the customer" and for those building solutions on their platform <a class="yt-timestamp" data-t="00:39:28">[00:39:28]</a>. The long-term vision is for Pine Cone to fit "snugly into that cost structure for like tens of thousands of or hundreds of thousands of different workloads" <a class="yt-timestamp" data-t="00:40:28">[00:40:28]</a>.
*   Advice to founders undergoing similar transitions is to move and "take the hit as soon as possible" <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>. This aligns with [[lean_startup_principles_applied_to_ai|Lean Startup principles]] of iterating quickly.

## Future of AI Infrastructure and Cost

The current reliance on GPUs for making models bigger is deemed unsustainable from an economic perspective <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. Operating a 100 billion parameter model for every API call is not feasible financially or environmentally ("you're going to go bankrupt right and you're going to make the planet hotter") <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.

*   There needs to be a significant shift in hardware, possibly involving more CPU workloads, specialized servers, or distributed infrastructure optimized for training or serving <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.
*   The speaker is bullish that models can achieve similar or better results at a fraction of the cost by "doing things right" with smaller models and efficient architectures <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>.
*   The use of larger context windows by model companies is seen as a pricing strategy to make users pay more per token <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>. This approach is criticized for being slow, expensive, and not always helpful <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.
*   Instead of stuffing all data into a context window, leveraging a vector database can reduce token usage significantly (e.g., sending 3,000 tokens instead of 100,000), resulting in 10% of the cost without performance loss <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>. This demonstrates [[cost_efficiency_and_accessibility_in_ai|cost optimization]] in AI.