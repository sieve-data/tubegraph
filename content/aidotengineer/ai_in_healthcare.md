---
title: AI in healthcare
videoId: cZ5ZJy19KMo
---

From: [[aidotengineer]] <br/> 

[[AI in healthcare]] applications, particularly in areas like prior authorization decisions, require robust evaluation systems to ensure accuracy and build trust <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Christopher Ljy, an AI engineer and former medical doctor, highlights that in healthcare, there is "no room for error" when building systems that support mission-critical decisions <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Challenges of Scaling [[AI in healthcare]]

While it is relatively easy to create a Minimum Viable Product (MVP) powered by Large Language Models (LLMs), scaling these products to serve customers at scale presents numerous challenges <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. As request volume increases, so does the number of unforeseen edge cases <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Example: Prior Authorization Decisions
Anterior, a company serving insurance providers covering 50 million American lives, focuses on supporting prior authorization decisions for medical treatments <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. They receive medical records and guidelines to determine if a treatment request should be approved or reviewed by a clinician <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

Consider an example question: "Has a patient had a previous brain MRI suspicious for multiple sclerosis (MS)?" This helps determine if the patient should receive a cervical spine MRI <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. An AI might respond:

> "The medical record shows a brain MRI from [date] that demonstrates hyperintensity in the infratentorial, DRX theortical, and per ventricular white matter, which is noted to be consistent with multiple sclerosis, and this confirms prior brain M findings suspicious for MS." <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

On the surface, this seems reasonable <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. However, it misses a key medical nuance: in a medical context, "suspicious" implies no confirmed diagnosis <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. If the patient already has a confirmed diagnosis, the AI's answer is incorrect because it uses "suspicious" when it should be "confirmed" <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

Mistakes like this might occur in 1 out of 1,000 or 10,000 cases <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. But if processing over 100,000 cases daily, this leads to a significant number of errors <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Making such mistakes in healthcare can lead to organizations being sued for inappropriate [[AI in workflow automation | AI automation]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Identifying and Handling Failure Cases

### Human Reviews
A first step to identify and handle failure cases is performing human reviews of [[AI in workflow automation | AI outputs]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Anterior has built an internal clinical team and specialized tooling called "Scalp" to facilitate this process <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The Scalp review dashboard displays all necessary context (medical record, guidelines) alongside the AI's answer and the question, allowing reviewers to quickly assess and critique responses <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Reviewers can label incorrect answers and provide critiques, which are then used to generate "ground truths" (correct answers) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

However, human reviews do not scale effectively <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>:
*   **MVP phase (1,000 decisions/day)**: Reviewing 50% (500 cases) requires 5 clinicians (at 100 reviews/day per clinician) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **Scaling (10,000 decisions/day)**: Maintaining a 50% review rate would require 5,000 human reviews daily, needing 50 clinicians—which is larger than most entire companies <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Even reviewing a smaller subset like 5% at 100,000 decisions/day still leads to 5,000 reviews and 50 clinicians <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

The challenge becomes: which cases should be reviewed, and how is the system performing on cases that are not reviewed? <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

### Offline Evaluation Datasets
Ground truths from human reviews can be used to build offline evaluation datasets <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. These datasets live outside the product and can be used for continuous evaluations and scoring <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. They are helpful for:
*   Defining gold standard datasets <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   Segmenting performance by enterprise, medical type, complex cases, or ambiguous outcomes <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   Iterating [[AI in workflow automation | AI pipelines]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

However, relying solely on offline evaluations is risky <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The input space of medical records is vast and heterogeneous, meaning new edge cases will continuously appear at scale <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Waiting for new edge cases to be represented in these datasets, which are built downstream of customer interaction, can be too late <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Real-time Reference-Free Evaluation Systems

The solution to these scaling problems is a real-time, reference-free evaluation system <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. "Reference-free" (or "label-free") means evaluating before knowing the true outcome (i.e., before a human review) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. This enables real-time response to issues <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### LLM as Judge
A core component of this system is using an LLM as a judge <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
1.  Inputs go into the primary LLM pipeline, which generates outputs <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
2.  These outputs are then fed into another LLM (the "judge"), along with a scoring system <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
3.  The scoring system can evaluate various aspects: helpfulness, conciseness, brand tone, or confidence in correctness (especially for binary or multi-class classifications) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

At Anterior, their generated output is either "approval" or "escalation for review" (a binary output) <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. They use a reference-free evaluation (which can include an LLM as judge or other methods like confidence estimation using logic-based methods) to provide a "confidence grading" <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This grading ranges from high confidence (correct) to low confidence (actively wrong) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. This score is then converted into a predicted correct output <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Applications of Reference-Free Evals
Reference-free evals provide two key pieces of information:
1.  **Estimated Performance**: They predict the estimated performance on *all* cases in real-time, not just those undergoing human review <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This allows for immediate response and feedback to customers <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
2.  **Dynamic Prioritization**: They can combine confidence grading with contextual factors (e.g., cost of procedure, risk of bias, previous error rates) to dynamically prioritize cases for human review <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This identifies the most relevant cases with the highest probability of error <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

This creates a virtuous cycle where human reviews validate and improve performance, while dynamic prioritization feeds cases back into the system <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. The reference-free evals surface potential issues, and human review determines accuracy, in a process known as "validating the validator" <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Over time, the number of unseen edge cases decreases, and the ability to detect them improves, creating a system that is difficult to replicate <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Integrating into the Pipeline
Once confident in the system's performance, the reference-free evaluation can be incorporated directly into the AI pipeline <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>:
*   If the reference-free eval indicates high confidence, the output can be directly returned to the customer <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   If confidence is low, a "further action" can be taken <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This might involve sending it to:
    *   Another LLM pipeline with more expensive models <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
    *   An internal on-call clinician for review <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
    *   The customer's review dashboard for their team to review <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

This mechanism ensures customer trust in the AI's outputs <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

## Impact at Anterior

Implementing this evaluation system has had significant impacts for Anterior:
*   **Reduced Hiring**: They have not needed to hire an ever-expanding team of expert clinicians like competitors (e.g., one competitor hired over 800 nurses) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Anterior reviews tens of thousands of cases with a review team of less than 10 clinical experts <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **High Alignment**: Achieved strong alignment between [[AI in workflow automation | AI and human reviews]], comparable to human-to-human reviewer alignment <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Quick Error Response**: They can quickly identify and respond to errors, ensuring they meet customer Service Level Agreements (SLAs) and maintain confidence in results <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Industry-Leading Performance**: Achieved provably industry-leading performance in prior authorization with an F1 score of nearly 96% in a recent study <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   **Customer Trust and Love**: This has led to gaining customer trust and even "love" for their product, with nurses expressing gratitude for its continued use <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

### Principles for Building a System: [[AI implementation and best practices]]
Anterior recommends the following principles for building such a system:
1.  **Build a System**: Think big; use review data not just to audit performance but to build, audit, and improve the entire evaluation system <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
2.  **Evaluate on Live Production Data**: Don't rely solely on offline evaluations. Identify problems immediately for quick response <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
3.  **Empower Best Reviewers**: Prioritize review quality over quantity and build custom tooling to accelerate the process <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

This approach enables real-time performance estimates, accurate responses, scalability, low cost, and is powered by a small, focused team of experts <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. It allows companies to scale from MVP while maintaining customer trust <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.