---
title: Evaluating AI systems at scale
videoId: cZ5ZJy19KMo
---

From: [[aidotengineer]] <br/> 

Building an evaluation system that operates effectively at scale is crucial, especially for mission-critical decisions like those in healthcare, where errors are unacceptable <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article, based on learnings from Anterior, which serves insurance providers covering 50 million American lives, explores how real-time, reference-free evaluations can foster customer trust and enable effective [[evaluating_ai_agents_and_assistance | evaluation of AI agents]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## [[challenges_in_scaling_ai_products | Challenges in Scaling AI Products]]

While creating a Minimum Viable Product (MVP) powered by Large Language Models (LLMs) is becoming increasingly straightforward <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, transitioning from MVP to serving customers at scale introduces significant [[challenges_in_ai_agent_evaluation | problems]] that are not apparent until high volumes are reached <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. As request volume grows, so does the number of unforeseen edge cases <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Example: Medical Prior Authorization
At Anterior, the core product supports prior authorization decisions for treatment requests, determining if a treatment should be approved or reviewed by a clinician <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The AI processes medical records and guidelines to answer specific questions, such as whether a patient had a previous brain MRI suspicious for Multiple Sclerosis (MS) to decide on a cervical spine MRI <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

An AI output might state a brain MRI confirmed prior findings suspicious for MS <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. However, this output could miss key medical nuance. In a medical context, "suspicious" implies no confirmed diagnosis. If the patient *already* has a confirmed diagnosis, stating it's "suspicious" is incorrect <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Such mistakes might occur once every thousand or ten thousand cases <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. When processing over 100,000 cases daily, this translates to a significant number of errors that must be identified <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Mistakes of this nature are unacceptable in healthcare, as organizations face lawsuits for inappropriate AI automation <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Human Reviews and Their Limitations
A primary [[strategies_for_ai_evaluation_and_troubleshooting | strategy]] to identify and handle failure cases is performing human reviews of AI outputs <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Anterior built an internal clinical team and specialized tooling, "Scalp," to facilitate these reviews <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This dashboard provides reviewers with all necessary context (medical record, guideline) alongside the question and AI answer, enabling quick and effective reviews <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Reviewers can critique incorrect answers, label them, and save them <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. These critiques can then be used to generate "ground truths," which are descriptions of the correct answers, useful for offline evaluations <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

However, human reviews do not scale effectively <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   Reviewing 50% of 1,000 daily cases requires 5 clinicians <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   Scaling to 10,000 daily cases at the same 50% review rate would require 50 clinicians, which is often larger than an entire company <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   Even reducing the review rate to 5% at 100,000 daily cases still requires 50 clinicians <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

This leads to two key questions: Which cases should be reviewed, and how is performance measured for cases not reviewed by humans <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>?

## Offline Eval Data Sets
Offline evaluation datasets are built from generated ground truths and live outside the product <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. They are helpful for defining gold standard datasets, segmenting performance by enterprise or medical type, plotting performance over time, and iterating AI pipelines <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

However, relying solely on offline evals is risky <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The input space for medical records is vast and heterogeneous, meaning new edge cases will constantly emerge at scale <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Waiting for new edge cases to appear in a manually built dataset, downstream of customer interaction, means it could be too late to respond to issues <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Solution: Real-time Reference-Free Evaluation System
The solution to the scalability challenges of human reviews and the limitations of offline evals is a real-time, reference-free evaluation system <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

**Reference-free** (or **label-free**) means evaluating an AI output *before* the true outcome is known or a human review has occurred <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This enables real-time response to issues as they arise <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### LLM as Judge
A great starting point for reference-free evaluation is using an LLM as a judge <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The process involves:
1.  Inputs go into the LLM pipeline being evaluated, producing outputs <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
2.  These outputs are fed into an "LLM as judge" along with a scoring system <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
3.  The scoring system can assess various factors like helpfulness, conciseness, tone, or confidence in correctness <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. For binary or multi-class classifications, it can assess confidence levels <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

At Anterior, with a binary output (approval or escalation for review), the reference-free eval system (which can include an LLM as judge or logic-based methods) provides a "confidence grading" – how confident the system is that the LLM output is correct <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This confidence grading can range from high confidence to low confidence, indicating potential errors <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. A threshold is then used to predict the correct output <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Utilizing Reference-Free Eval Information
The confidence grading and predicted correct outputs from reference-free evals can be used in several ways:

1.  **Estimated Performance Prediction**: Real-time estimated performance across *all* cases, not just those reviewed by humans, can be predicted <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This allows for immediate response and feedback to customers <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
2.  **System Alignment**: By comparing outputs from human reviews and reference-free evals on cases that have both, the alignment and trustworthiness of the automated system can be computed <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
3.  **Dynamic Prioritization for Human Review**: Confidence grading can be combined with contextual factors (e.g., cost of procedure, risk of bias, previous error rates) to dynamically prioritize cases for human review <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This ensures that the most relevant cases with the highest probability of error are reviewed by experts <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

This creates a virtuous cycle: reference-free evals surface potential issues, human reviews determine accuracy, and this process continuously validates and improves the evaluation system itself <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Over time, the number of unseen edge cases diminishes, and the ability to detect them improves, building a robust, difficult-to-replicate system <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Incorporating Evals into the AI Pipeline
Once confidence in the system's performance is high, the evaluation system can be integrated directly into the AI pipeline <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>:
*   Inputs pass through the primary LLM pipeline, generating outputs <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   These outputs are then fed into the reference-free evaluation system <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   Based on the eval output, the system can either confidently return the result directly to the customer or trigger a further action <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   Further actions might include sending the case to another LLM pipeline (perhaps with more expensive models), escalating it to an internal clinician for review, or surfacing it in the customer's review dashboard for their team to review <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

This powerful mechanism ensures customer trust in the delivered outputs <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

## Impact at Anterior
Implementing this system provided significant benefits for Anterior:
*   **Reduced need for large review teams**: They did not need to hire an ever-expanding team of clinicians. While a competitor hired over 800 nurses for reviews, Anterior reviews tens of thousands of cases with a team of less than 10 clinical experts <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This is a clear example of [[leveraging_ai_tools_for_efficiency_and_scalability | leveraging AI tools for efficiency and scalability]].
*   **Strong AI-human alignment**: After multiple iterations, strong alignment was achieved between AI and human reviews, comparable to alignment between human reviewers themselves <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Quick error identification and response**: The system enables rapid identification and correction of errors, ensuring timely responses and meeting customer Service Level Agreements (SLAs) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Industry-leading performance**: Anterior achieved provably industry-leading performance in prior authorization, with an F1 score of nearly 96% in a recent study <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   **Enhanced customer trust and love**: This performance led to customer trust and even "love" for their product <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Key Principles for Building an Eval System
Based on their experience, Anterior recommends the following [[steps_to_create_effective_evaluations_for_ai_applications | principles]] for building an effective evaluation system:
1.  **Build a System, Not Just Audit**: Think big. Use review data not just to audit performance, but to build, audit, and improve the auditing (evaluation) system itself <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
2.  [[evaluating_ai_agents_methods_and_metrics | Evaluate]] **on Live Production Data**: Do not solely rely on offline evaluations. Identify problems immediately to enable quick responses <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
3.  **Empower Best Reviewers**: Prioritize the quality of human reviews over quantity. Build custom tooling if it accelerates the process <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

This approach results in an evaluation system that provides real-time performance estimates, ensures accuracy, scales to meet demand while maintaining low costs, and is powered by a small, focused team of experts <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. It enables the transition from MVP to serving customers and maintaining their trust at scale <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.