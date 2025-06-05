---
title: Ensuring AI accuracy and reducing errors
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

AI can be embraced to work smarter, not to replace human jobs, by turbocharging workflows and ensuring accuracy <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. A key focus for small teams leveraging AI is to build systems that maintain accuracy and reduce errors rather than increasing workload <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[challenges_with_current_ai_implementation | Challenges with Current AI Implementation]]

Even with a small team, managing a high volume of tasks can lead to significant pain points related to accuracy and quality <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
*   **Error-prone first drafts** from numerous product teams <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Time-consuming grooming** tasks like style checks, alt text generation, and SEO optimization <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Hallucination risk** if AI models are left unchecked <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## AI Agent Architecture for Accuracy

To achieve leverage without burnout, a team developed six single-purpose AI agents behind a Next.js frontend, designed to tackle repetitive, well-scoped jobs so humans can focus on judgment and clarity <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The "sweet spot" for an AI helper is tasks that are repeatable, high-volume, and low-creativity <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

The architecture emphasizes accuracy and error reduction through a layered approach <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:
*   **Next.js UI** feeds requests into custom AI agents <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Custom GPT-401 Agents** are used, with the appropriate model selected for the specific job <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. These agents have a baked-in style guide and rubric, retrieved from an AirTable for easy collaboration <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Validation Layer** includes Veil Linting and CI/CD tests <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **GitHub PRs** add codeowner review, making it easier to scrutinize agent suggestions <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Human Oversight** ensures a human hits the merge button only when changes are right, often with product and engineering reviews <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This layered approach significantly reduces hallucinations <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## Specific Agent Examples and Accuracy

Several agents contribute to quality and accuracy:
*   **Automated Editor**: Fixes grammar, formatting, and accuracy, applying a style guide and rubric <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. It shows diffs of changes and provides explanations of original text, revised text, and the specific style guide/rubric item applied <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. While powerful, it's noted as "not perfect" (e.g., occasionally missing SEO descriptions) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **SEO Metadata Generator**: Provides metatitle and meta description while accounting for character limitations <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Image Alt Text Generator**: Generates alt text that conforms to required formats <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Jargon Simplifier**: Turns technical "dev" language into plain English, helpful for writing and reviewing pull requests <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Guard Rails for Quality

Tools alone do not guarantee quality; guard rails are essential to mitigate risks <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>:
*   **Hallucinations**: Mitigated using tools like Veil Lint and CI tests, combined with human stakeholder reviews <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Bias**: Tackled through data set tests and prompt audits <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Stakeholder Misalignment**: Addressed via weekly (or more frequent) PR reviews and Slack feedback loops with product managers and engineering teams <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   [[continuous_improvement_in_ai_systems | Continuous Improvement]]: These feedback cycles allow for continuous tuning of prompts, rather than relying on the model to magically stay perfect <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## [[best_practices_for_building_ai_systems | Best Practices for Building AI Systems]]

A three-step playbook for ensuring AI accuracy and improving team velocity <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:
1.  **Identify one pain point** that significantly impacts throughput <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Pick a single task** that is repeatable and rule-based <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
3.  **Loop with users weekly** (at least): ship, measure, and refine <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    *   Stacking these "wins" can significantly boost a team's velocity <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.