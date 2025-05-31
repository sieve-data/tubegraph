---
title: AI model pretraining and finetuning decisions
videoId: 7-3IxVvWoxc
---

From: [[redpointai]] <br/> 

Jonathan Frankle, Chief AI Scientist at Databricks, advises enterprises on strategic decisions regarding [[AI model selection and evaluation for businesses | AI model selection]], training, [[Fine tuning models for better outcomes | fine-tuning]], and prompt engineering <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. His insights stem from working with Databricks' 12,000 customers on AI <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Iterative Journey of AI Model Development

The path to deploying AI systems is not always clear from the outset <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. Frankle emphasizes keeping options open and starting small <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Starting Small: Prompting
The journey typically begins with simple prompting of existing models, such as OpenAI's or Llama models available on Databricks <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This initial step helps to litmus test if AI is suitable for a given use case, as predictability is low <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. It's an experiment, like data science in the literal sense <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### Incorporating Data: Retrieval Augmented Generation (RAG)
If initial prompting shows promise, the next step often involves [[AI models and the product development process | bringing enterprise-specific data to bear]] using hardcore RAG <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Generic models won't know about internal data, so it must be integrated <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### [[Fine tuning models for better outcomes | Fine-tuning]]
If RAG delivers value, [[Finetuning and reinforcement learning techniques for AI | fine-tuning]] becomes a consideration <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. This bakes more specific knowledge into the model, incurring a higher upfront cost but potentially offering better quality in a smaller package, thereby reducing inference costs or improving output quality <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### Continued Pre-training
Beyond fine-tuning, some organizations might consider continued pre-training <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. This requires even more significant upfront investment and is justified by extensive model usage <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

### Full Pre-training from Scratch
Pre-training a model from scratch is a massive undertaking, expensive and labor-intensive, and is generally discouraged unless absolutely necessary <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. However, for those with unique needs, it's an option that Databricks supports <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## Justifying the "Work Your Way Up"

The progression from prompting to full pre-training should be justified by rigorous Return on Investment (ROI) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Each step involves an upfront investment that pays for itself quickly if there's enough usage <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>. This strategic decision-making represents a cost-quality trade-off, allowing companies to either achieve the same quality at a lower inference cost or get a higher quality model for the same cost <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. Once product-market fit is achieved, it becomes a matter of optimizing for quality and cost <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## When Company/Domain-Specific Models Make Sense

There are specific scenarios where investing in dedicated model training, even full pre-training, is logical:

1.  **Language and Domain Gaps:** When general models struggle with specific languages (e.g., Japanese, Korean, Indian languages due to less training data or tokenizer issues) <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
2.  **Unique Task Domains:** For tasks fundamentally different from general language understanding, like protein modeling <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
3.  **Speed and Specificity Requirements:** When a very fast and highly specific model is crucial, such as for code completion for free-tier users where cost is a major constraint <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
4.  **Cost Optimization for High Usage:** For models with very high usage, the upfront cost of pre-training can lead to significant long-term savings or quality improvements <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

## The Role of Data and Evaluation

A common mistake is waiting for perfect data or [[AI model evaluation and benchmarking | perfect evaluation metrics]] before starting AI development <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Frankle advises an agile approach:
*   **Iterate Quickly:** Do just enough data work to interact with a model, build the "crappiest model" possible, create a quick evaluation, and test it against the real world <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Human Feedback:** Connect with human testers, even just one friend at the company, for real-world feedback <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Databricks' team conducts A/B testing of model outputs and RLHF-style pairwise comparisons without revealing the model source <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Simple Evaluations:** Start with simple evaluations, even just five examples with graded responses (e.g., 1-5 scale), which can calibrate an LLM judge <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Dedicated Tools:** Databricks offers a new agent evaluation product to help users create meaningful evaluation sets quickly, aiming for a few dozen examples in an afternoon <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. This tool is a key focus for Frankle, as a measuring stick is essential for any progress <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Insights from Databricks' DBRX Model Development

The development of Databricks' DBRX language model exemplified the end-to-end platform approach <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. They used Spark for data ingestion and ETL, Delta tables for storage, Unity Catalog for tracking data sets, MosaicML tools for model training, and MLflow for experiment tracking <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This integrated use of their own products saved significant time <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

## Future Outlook

Frankle believes the open-source model world is "exceedingly well covered" <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>. Therefore, Databricks' focus shifts to other gaps to ensure customer success <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>:

*   **Evaluation Creation:** Helping customers build their initial measuring sticks <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>.
*   **Navigating Options:** Guiding customers through the complex decisions of RAG versus prompting versus [[Fine tuning models for better outcomes | fine-tuning]], providing many options without overwhelming them <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>.
*   **Data Challenges:** Assisting customers in building AI systems with imperfect or fragmented data <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Compound AI Systems and Agents:** Focusing on connecting different pieces of data and models to solve specific problems <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>.

The field is still learning what works best in different scenarios <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>. The goal is to provide maximum choice with minimal cost, then help customers make the best selection and confidently deploy models into production <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. Even with advancements, AI systems are fundamentally "fuzzy," and achieving "fifth nine" reliability with current technology remains challenging <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>. This understanding helps manage expectations and focus on learning the strengths and weaknesses of the technology <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.