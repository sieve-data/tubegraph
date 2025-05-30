---
title: Pretraining and finetuning AI models
videoId: 7-3IxVvWoxc
---

From: [[redpointai]] <br/> 

Organizations face crucial decisions regarding the deployment of AI models: whether to [[Finetuning AI models for enterprise data | train their own models]], [[Finetuning approaches and considerations in AI | fine-tune existing ones]], or simply use prompt engineering <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The optimal approach depends on the specific use case, data availability, and desired performance.

## The AI Model Development Journey

The journey of adopting AI models for an enterprise is often iterative, starting small and gradually scaling up based on justified return on investment (ROI) <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

The recommended path generally begins with:
1.  **Prompting an existing model** <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This acts as a litmus test to see if AI is suitable for the use case <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
2.  **Retrieval Augmented Generation (RAG)** <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This involves bringing specific enterprise data to bear, as generic models won't have inherent knowledge of internal data <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
3.  **Finetuning** <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. If initial value is demonstrated, finetuning can "bake in" more knowledge, offering better quality in a smaller package and potentially reducing inference costs <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
4.  **Continued Pre-training** <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. This involves further training on domain-specific data.
5.  **Pre-training from scratch** <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This is the most significant undertaking and is "not for the faint of heart" <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

Each step up the chain involves a greater upfront investment, but it can significantly improve the cost-quality trade-off, justifying itself with sufficient model usage <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

## When to Build Custom Models

The decision to [[Finetuning AI models for enterprise data | train or finetune a custom model]] becomes relevant in several scenarios:

*   **Language Specificity**: Off-the-shelf models may not perform well in languages where less training data is available, such as Japanese or Korean, leading companies to build their own models tuned for these languages <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   **Domain Specificity**: For highly specialized tasks, like protein modeling, generic language models are insufficient <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
*   **Performance Requirements**: When a model needs to be extremely fast and specific, such as for code completion used by millions of users, custom development can create a "Lamborghini of models" built for speed and task <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
*   **Cost Optimization**: Pre-training or [[Finetuning approaches and considerations in AI | finetuning]] can lead to a more efficient model for inference, either providing the same quality at a lower cost or higher quality at the same cost <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

## Challenges and Considerations

### Data and Evaluation
A common mistake is waiting for perfect data or perfect evaluations before starting AI development <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. The measure of data quality and evaluation effectiveness comes from the model's performance in real-world scenarios <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. It's recommended to:
*   Start with minimal data preparation to get the model interacting <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   Build the "crappiest model" possible and a quick evaluation <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   Iterate on data, model, and evaluation based on real-world testing <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   Initial evaluations will be proxies for the real world, so direct human testing (even with one friend) is crucial <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   Start with simple evaluations, even just five examples with graded responses, to calibrate LLM judges <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

Databricks, for example, is developing a product to help users create meaningful evaluation sets quickly, aiming for dozens of examples in an afternoon, rather than relying solely on synthetic data generation <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### Cost-Quality Trade-off
[[Scaling AI models and test time compute | Scaling models]] is a game of "incredible investment" <a class="yt-timestamp" data-t="00:36:28">[00:36:28]</a>. While large companies like Meta invest heavily in foundational models, other organizations should focus on existing gaps in the ecosystem to make customers successful <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. This includes [[challenges_and_opportunities_in_ai_model_finetuning | finetuning]], [[the_role_of_reinforcement_and_finetuning_in_ai | RAG]], and developing compound AI systems that connect different pieces of technology <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>.

New [[finetuning_approaches_and_considerations_in_ai | finetuning techniques]] are emerging to address common challenges, such as working with fragmented data where key pieces expected for traditional finetuning might be missing <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>.

### Future of Model Development
The field is in a phase of experimentation with new products and applications <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>. The focus is on providing customers with maximum choice at minimal cost and helping them select the best options and deploy them reliably <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. This approach acknowledges that "it's not AutoML" but aims to simplify the process of navigating many potential model configurations <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.

For a specific application, once product-market fit is achieved, the need to "go back to the drawing board" for fundamental model architecture is not often necessary; the focus shifts to optimizing quality and cost <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.