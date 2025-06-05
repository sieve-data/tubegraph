---
title: Human reviews of AI outputs
videoId: cZ5ZJy19KMo
---

From: [[aidotengineer]] <br/> 

In applications involving critical decisions, such as healthcare, there is "no room for error" when using AI systems <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While creating a Minimum Viable Product (MVP) with Large Language Models (LLMs) is becoming easier, scaling these products to serve customers presents significant challenges <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. As request volume increases, so do the number of previously unseen edge cases <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## The Need for Human Oversight in Healthcare AI

Anterior, a company serving insurance providers for 50 million American lives, utilizes AI for prior authorization decisions regarding treatment requests <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Their AI processes medical records and guidelines to determine if a treatment should be approved or reviewed by a clinician <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Example of an Edge Case
An example of an AI output might describe a brain MRI showing hyperintensity "consistent with multiple sclerosis" and confirming "prior brain MRI findings suspicious for MS" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. However, this output missed a crucial medical nuance: in a medical context, "suspicious" implies no confirmed diagnosis, but the patient actually had an existing diagnosis <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This makes the AI's answer incorrect <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Mistakes like this, even if rare (e.g., every 1,000 or 10,000 cases), become frequent (e.g., 100 mistakes daily) when processing over 100,000 cases per day <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Errors in US healthcare AI automation can lead to lawsuits <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Implementing Human Reviews
To identify and handle failure cases, performing [[role_of_human_and_automated_evaluators_in_ai_assessment | human reviews]] of AI outputs is essential <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Anterior built an internal clinical team and developed proprietary tooling, called "Scalp," to facilitate efficient reviews <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### The Scalp Review Dashboard
The "Scalp" review dashboard displays all necessary context, such as medical records and guidelines, on the right side without requiring scrolling <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. The left side shows the question being answered and the required context, enabling reviewers to quickly assess a high volume of questions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Reviewers can add critiques, label errors as "Incorrect," and save this information into the system <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Critiques and Ground Truths
Critiques, which explain what is wrong with an AI's output, can be used to generate "ground truths"—descriptions of the correct answer <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. These ground truths are then used in [[evaluating_ai_system_performance | offline evaluations]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Limitations of Human Reviews at Scale
While crucial, [[role_of_human_and_automated_evaluators_in_ai_assessment | human reviews]] face significant [[evaluating_ai_systems_at_scale | scalability]] challenges <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **MVP Stage:** Reviewing 50% of 1,000 daily cases (500 reviews) requires 5 clinicians, with each clinician performing approximately 100 reviews per day <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Scaling Up:** If daily medical decisions increase to 10,000, maintaining a 50% review rate would necessitate 5,000 human reviews daily, requiring 50 clinicians—a number larger than many companies <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Even reducing the review rate to 5% at 100,000 daily decisions still requires 5,000 human reviews and 50 clinicians <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

This demonstrates that relying solely on [[role_of_human_and_automated_evaluators_in_ai_assessment | human reviews]] "doesn't scale" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This leads to two key questions: which cases should be reviewed, and how does the AI perform on unreviewed cases <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>?

## Offline Eval Datasets
[[Evaluating AI system performance | Offline evaluation]] datasets are built from generated ground truths and reside outside the product <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. They can be used to define gold standard datasets, segment performance by enterprise or medical condition, track performance over time, and iterate on AI pipelines <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. However, relying only on [[evaluating_ai_system_performance | offline evals]] can be risky, as new edge cases in medical records (due to high heterogeneity) will continuously appear, and waiting for them to be represented in a downstream dataset means it "could be too late" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Integration with Real-Time Reference-Free Evaluations
The solution to the scalability challenges of [[role_of_human_and_automated_evaluators_in_ai_assessment | human reviews]] and the limitations of [[evaluating_ai_system_performance | offline evals]] is a real-time, reference-free [[evaluating_ai_system_performance | evaluation system]] <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Reference-free means evaluating before the true outcome is known (i.e., before a [[role_of_human_and_automated_evaluators_in_ai_assessment | human review]] has occurred), enabling immediate response to issues <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### Prioritizing Human Reviews
Real-time reference-free evals can provide a "confidence grading" for AI outputs <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This confidence grading can be combined with contextual factors like procedure cost, bias risk, and previous error rates <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This allows for dynamic prioritization of cases, identifying the most relevant ones with the highest probability of error to be reviewed by humans <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### The Virtuous Cycle: Validating the Validator
This creates a "virtuous cycle" where [[role_of_human_and_automated_evaluators_in_ai_assessment | human reviews]] continuously validate and improve the performance of the automated reference-free [[evaluating_ai_system_performance | evaluation system]] <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   Reference-free [[evaluating_ai_system_performance | evals]] surface potential problem cases <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   [[Role of human and automated evaluators in AI assessment | Human review]] determines the actual accuracy <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

This process, often described as "validating the validator," leads to a decrease in unseen edge cases and an improvement in the ability to detect them <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Such a robust [[evaluating_ai_system_performance | system]] is difficult for competitors to replicate, as it requires processing high volumes of real data and extensive data-driven iterations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Impact of an Integrated Evaluation System
Anterior's integrated [[evaluating_ai_system_performance | evaluation system]] has had several significant impacts:
*   **Reduced Staffing Needs:** It eliminated the need to hire an "ever expanding team of expert clinicians" <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. While a competitor hired over 800 nurses for reviews, Anterior reviews tens of thousands of cases with a team of fewer than 10 clinical experts <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Strong Alignment:** The system achieved strong alignment between AI and [[role_of_human_and_automated_evaluators_in_ai_assessment | human reviews]], comparable to the alignment seen between human reviewers themselves <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Rapid Error Response:** It enables quick identification and response to errors, ensuring customer Service Level Agreements (SLAs) are met <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Industry-Leading Performance:** This approach resulted in "provably industry-leading performance" in prior authorization, with an F1 score of nearly 96% in a recent study <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   **Customer Trust:** This high performance fostered customer trust and even "love" for the product <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

## Key Principles for Effective Evaluation
To [[steps_to_create_effective_evaluations_for_ai_applications | build an evaluation system]] that works [[evaluating_ai_systems_at_scale | at scale]], enables real-time performance estimates, and maintains low costs, the following principles are recommended <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>:
1.  **Build a System, Not Just an Audit:** Use review data not just to audit performance, but to "build, audit, and improve your auditing system," which is your [[evaluating_ai_system_performance | evaluation system]] <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
2.  **Evaluate on Live Production Data:** Do not rely solely on [[evaluating_ai_system_performance | offline evals]]. Identify problems immediately for quick response <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
3.  **Empower Best Reviewers:** Prioritize the quality of reviews over quantity and build custom tooling if it helps accelerate the process <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.