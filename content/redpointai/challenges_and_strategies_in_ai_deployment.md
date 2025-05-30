---
title: Challenges and strategies in AI deployment
videoId: 7-3IxVvWoxc
---

From: [[redpointai]] <br/> 
Jonathan Frankle, Chief AI Scientist at Databricks, focuses on helping enterprises navigate the complexities of AI adoption and deployment <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. His work involves guiding companies on when to train their own models, fine-tune existing ones, or simply use prompt engineering <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Core Guidance for AI Model Deployment

Frankle advises organizations to keep their options open when embarking on their AI journey, as the ultimate destination (e.g., prompting vs. pre-training) is not always obvious at the outset <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Databricks aims to provide comprehensive tools so no one has to compromise on their AI development path <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

The recommended approach is to:
1.  **Start small** and work your way up <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
2.  **Run experiments** to test if AI is suitable for a given task, even by manually pulling in documents and prompting a model <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
3.  **Justify scaling efforts with rigorous ROI** <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Data and Evaluation Challenges

A common mistake is believing that AI can only be implemented once data or evaluations are perfect <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Instead, the usefulness of an AI system dictates the quality of the data, and the real-world performance validates the evaluation <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

Key advice for data and evaluation:
*   **Be agile**: Do just enough data work to interact with the model, build a quick evaluation, test it, and then iterate to refine the model, data, or even reassess expectations from AI <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Human input is crucial**: Any evaluation is a proxy for the real world <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. Having even one person not involved in the project act as a human tester for the process is more valuable than synthetic benchmarks <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Databricks teams perform A/B testing with human feedback, like RLHF (Reinforcement Learning from Human Feedback), for model outputs <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Start simple with evaluations**: Begin by writing five examples, even without precise right/wrong answers, and assign quality scores (e.g., 1-5) <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This can calibrate an LLM (Large Language Model) judge <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
*   **Utilize tools**: Databricks has released an agent evaluation product designed to help users create meaningful evaluation datasets of a few dozen examples in an afternoon, by leveraging automated tools while valuing human time <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

## Scenarios for Custom Model Development and Deployment

While large, generic models are powerful, there are specific scenarios where developing domain- or company-specific models, or engaging in continued pre-training, makes sense <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>:

1.  **Model performance for specific languages**: Generic models may not be well-tuned for languages like Japanese or Korean due to less available training data <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. Companies in these regions often need to build their own models <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
2.  **Different task domains**: For tasks fundamentally different from typical language models, such as protein modeling, specialized models are necessary <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
3.  **Need for speed and specificity**: Some applications require extremely fast and highly specific models, like code completion tools that need to serve all users, including free tiers, efficiently <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
4.  **Cost optimization**: While pre-training models is expensive upfront, for high-usage models, it can lead to a better cost-quality trade-off <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. This means either achieving the same quality at a lower inference cost or obtaining a better quality model for the same cost <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. The upfront investment pays for itself quickly with sufficient usage <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.

### The Cost-Quality Trade-off Journey

The journey from simple prompting to fine-tuning, continued pre-training, and full pre-training represents increasing upfront investment for improved cost-quality trade-offs <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. Organizations progress along this path as usage justifies the investment <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. Once product-market fit is achieved, the focus shifts to optimizing quality and cost <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## Product-Market Fit in AI and Navigating Fuzziness

Product-market fit in AI tends to occur in two patterns <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>:
1.  **Scenarios where precision isn't paramount**: Applications where there are many "right" answers, such as brainstorming, creative applications, marketing, or surfacing information (e.g., Glean), do not require perfect accuracy <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
2.  **Scenarios with human checks**: Use cases where the AI's output is relatively costly for a human to produce but quick for a human to check <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. Code copilots are a prime example, as checking suggested code is faster than writing it from scratch <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. Similarly, customer support is a good fit <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.

AI's "fuzziness" is both a superpower and a challenge <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. While chaining models and creative uses can push towards higher quality, achieving "perfection" (e.g., five nines of quality) with current technology is difficult <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.

### The Long Journey of AI Maturation

Frankle emphasizes that the current state of AI is analogous to early software engineering <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. It took decades to learn how to build structured programs, manage vulnerabilities, and handle massive code bases <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>. Even if AI technology were to freeze today, enormous creativity and advancements would still occur as we learn to better use these tools <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>.

A significant challenge in high-stakes areas like healthcare and autonomous vehicles is the lack of human intuition about when AI systems will fail, unlike with human errors <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. This unpredictability makes it harder for society to make peace with AI mistakes <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. Holding AI to rigorous standards, however, might lead to reassessing and improving human performance standards as well <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.

## Databricks' Role in AI Deployment

Databricks focuses on providing an end-to-end platform that integrates all necessary tools for AI development and deployment, from data ingestion to evaluation <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. This includes using Spark for data ingestion, Delta tables for storage, Unity Catalog for tracking, MosaicML tools for training, and MLflow for experiment tracking <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

Key aspects of their strategy include:
*   **Integrated platform**: Ensuring all tools work well together under one roof to avoid issues with data transiting between different places <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.
*   **Customer-centric development**: Working hand-in-hand with customers to understand their challenges and refine product offerings <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
*   **Addressing the "last mile"**: Focusing on how to make raw AI materials useful to customers by connecting diverse data to AI system building processes, including through compound AI systems and agents <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.
*   **Providing choice without overwhelm**: Helping customers measure and choose from many options, including different fine-tuning techniques (like "soft" fine-tuning for fragmented data) <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.
*   **Partnerships and Acquisitions**: Databricks partners with many startups that build phenomenal point solutions (e.g., data annotation, eval creation) <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. Acquisitions, like Lilac, happen when a tool is so valuable (e.g., used internally for DBRX) that integrating the team makes sense for customers <a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>.

## Current Gaps and Future Focus in AI Deployment

Frankle identifies several gaps in the current AI landscape that Databricks is focused on:
*   **Measurement**: Still learning how to best help customers build methods to measure their AI products effectively <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
*   **Navigation of approaches**: Understanding what combination of RAG (Retrieval Augmented Generation), prompting, and fine-tuning works best for different use cases <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a>.
*   **Data challenges**: Helping customers with messy or incomplete data sets (e.g., many inputs but few outputs) to build effective AI systems <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Production comfort**: Ensuring customers feel comfortable deploying and running AI systems in production environments <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

Frankle believes the open-source model world is "exceedingly well covered" <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>, allowing Databricks to focus on these "last mile" challenges to make AI useful for its 12,000 customers <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

## Policy and Responsible AI Deployment

Frankle stresses that AI experts have a responsibility to participate in policy discussions to ensure systems are used responsibly <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. Key policy questions include:
*   **When to allow/disallow systems**: It is acceptable to say that certain AI systems are not reliable enough for specific contexts <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>.
*   **Setting standards**: Rigorous standards for AI systems, particularly in high-stakes areas like law enforcement, medicine, and autonomous vehicles, where mistakes can have severe consequences <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>.
*   **Scientific honesty**: Being transparent about what is known and unknown about AI capabilities, and not over-promising future advancements, helps build public trust <a class="yt-timestamp" data-t="00:57:46">[00:57:46]</a>.

## Underexplored Areas

While AI applications are being explored everywhere, Frankle is personally excited about robotics and embodied systems, viewing them as powerful tools for interacting with the physical world, similar to how information systems interact with the digital world <a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>.