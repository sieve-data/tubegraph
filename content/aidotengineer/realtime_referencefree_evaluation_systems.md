---
title: Realtime referencefree evaluation systems
videoId: cZ5ZJy19KMo
---

From: [[aidotengineer]] <br/> 

Developing an evaluation system that operates at scale is crucial for supporting mission-critical decisions, especially in fields like healthcare where there is no room for error <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Companies like Anterior, which serve insurance providers covering 50 million American lives, have had to develop such systems to ensure customer trust <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Challenges of AI at Scale

While creating an MVP (Minimum Viable Product) powered by Large Language Models (LLMs) is becoming increasingly easy, scaling it to serve customers introduces significant challenges <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. As request volume grows, so does the number of unforeseen edge cases <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### The Problem of Medical Nuance
In the medical industry, an AI system assisting with prior authorization decisions must handle complex nuances <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For instance, an AI might incorrectly interpret "suspicious for MS" as a confirmed diagnosis when the patient already has an existing diagnosis, rendering the AI's answer wrong <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Mistakes like this, even if rare (e.g., every 1,000 or 10,000 cases), accumulate to a large number of errors when processing over 100,000 cases daily <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Errors in US healthcare AI automation can lead to lawsuits <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Limitations of Human Reviews
Human reviews of AI outputs are a key method for identifying and handling failure cases <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. At Anterior, an internal clinical team uses a review dashboard called "Scalp" to efficiently review medical records, guidelines, and AI-generated answers <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Reviewers can critique incorrect answers, label them, and save them, which can then be used to generate ground truths for [[evaluations_and_finetuning_in_ai_development | offline evaluations]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

However, human reviews do not scale <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>:
*   Reviewing 50% of 1,000 daily decisions requires 5 clinicians <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   Maintaining this 50% review rate for 10,000 daily decisions would require 50 clinicians, which is impractical for many companies <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Even reviewing a smaller subset, like 5% of 100,000 daily decisions, still requires 50 clinicians <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

This leads to two critical questions: Which cases should be reviewed, and how is the AI performing on cases that are not reviewed <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>?

### Limitations of Offline Eval Datasets
Offline eval datasets, built from human-generated ground truths, can be useful for defining gold standards, segmenting data, and tracking performance over time <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. They help in iterating AI pipelines <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

However, relying solely on offline [[evaluating_ai_system_performance | evaluations]] is risky <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The input space for medical records is vast and highly heterogeneous <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. New edge cases constantly emerge at scale, and waiting for them to appear in offline datasets means it might be "too late" to identify and respond <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Realtime Reference-Free Evaluation Systems

The solution to these scaling and response challenges is [[realtime_ai_fraud_defense_and_response | Realtime AI fraud defense and response]] evaluation systems <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. "Reference-free," also known as "label-free," means that [[evaluating_ai_system_performance | evaluation]] occurs before the true outcome is known or a human review has been performed <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This enables the system to be real-time, allowing immediate response to issues <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### How it Works: LLM as Judge
A key starting point for [[monitoring_tracing_and_evaluation_in_rag_systems | monitoring tracing and evaluation in RAG systems]] and similar systems is using an LLM as a judge <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
1.  **Input and AI Output:** Inputs go into the main LLM pipeline, generating an output <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
2.  **LLM as Judge:** This output is fed into another LLM, acting as a judge, along with a scoring system <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
3.  **Scoring Criteria:** The scoring system can assess various [[metrics_for_evaluating_RAG_systems | metrics for evaluating RAG systems]] and other AI outputs, such as helpfulness, conciseness, tone, or confidence in correctness <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. For binary or multiclass classification outputs, confidence levels can be assigned <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
4.  **Confidence Grading:** At Anterior, this process yields a "confidence grading" for the AI's output, ranging from high confidence (correct) to low confidence (wrong) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This can also incorporate other methods like confidence estimation using logic-based approaches <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
5.  **Predicted Correct Output:** The confidence score can then be converted into a predicted correct output using a threshold <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Applications of Realtime Eval Information
This dual information — confidence grading and predicted output — can be used in several ways:
1.  **Estimated Performance:** Predict the estimated performance across all cases in real time, not just those reviewed by humans <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This allows for immediate response and feedback to customers <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
2.  **System Alignment:** Compare reference-free eval outputs with human reviews to compute the alignment and determine the system's trustworthiness <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
3.  **Dynamic Prioritization for Human Review:** Combine confidence grading with contextual factors (e.g., cost of procedure, risk of bias, previous error rates) to dynamically prioritize cases for human review <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This identifies the most relevant cases with the highest probability of error <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

### The Virtuous Cycle: Validating the Validator
This creates a "virtuous cycle" where human reviews validate and improve the system's performance, and dynamically prioritized cases feed back into the process <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Realtime reference-free evals surface potential problem cases, and human reviews confirm accuracy <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This process, known as "validating the validator," continually reduces unseen edge cases and improves error detection <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Incorporating into the Pipeline
Once confidence in the system's performance is high, the reference-free eval can be directly integrated into the AI pipeline <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>:
*   Inputs go through the original AI pipeline, generating outputs <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   These outputs are passed to the reference-free evals <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   Depending on the eval's output, the system can either confidently return the response to the customer or take further action <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   Further actions might include sending it to another LLM pipeline with more expensive models, assigning it to an internal on-call clinician for review, or surfacing it in the customer's own review dashboard <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

This powerful mechanism ensures customer trust in the AI's outputs <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

## Impact and Benefits
At Anterior, the implementation of [[realtime_ai_fraud_defense_and_response | realtime AI fraud defense and response]] has yielded significant benefits:
*   **Reduced Staffing Needs:** Avoids the need to hire an ever-expanding team of expert clinicians. Anterior reviews tens of thousands of cases with a team of less than 10 clinical experts, unlike competitors who might hire hundreds of nurses <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   **Strong AI-Human Alignment:** Achieved very strong alignment between AI and human reviews, comparable to the alignment observed between human reviewers themselves <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Quick Error Response:** Enables rapid identification and response to errors, ensuring customer SLAs (Service Level Agreements) are met <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Industry-Leading Performance:** Resulted in provably industry-leading performance in prior authorization, with an F1 score of nearly 96% in a recent study <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   **Enhanced Customer Trust and Love:** Led to deep customer trust and satisfaction, exemplified by a nurse expressing relief at being able to continue using the AI <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Principles for Building an Evaluation System
Christopher Ljy recommends the following principles for building an [[effective_evaluation_frameworks | effective evaluation framework]]:
1.  **Build a System:** Think big. Use review data not just to audit performance, but to build, audit, and improve the auditing and [[evaluating_ai_system_performance | evaluation system]] itself <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
2.  **Evaluate on Live Production Data:** Do not rely solely on [[evaluations_and_finetuning_in_ai_development | offline evaluations]]. Identify problems immediately to respond quickly <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
3.  **Empower Best Reviewers:** Prioritize the quality of reviews over quantity. Build custom tooling if it helps to move faster <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

This approach creates an evaluation system that provides real-time performance estimates, enables quick and accurate responses, scales to meet demand at low cost, and is powered by a small, focused team of experts <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. It supports the transition from MVP to serving customers and maintaining their trust at scale <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.