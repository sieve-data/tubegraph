---
title: AI in workflow automation
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

AI is becoming a transformative tool that enables teams to work smarter rather than replacing human roles <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. By leveraging [[role_of_ai_agents_in_workflow_automation | AI agents]], teams can significantly enhance and [[role_of_ai_agents_in_workflow_automation | turbocharge workflows]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Addressing Workflow Pain Points

A common challenge in documentation teams, for example, is managing a high volume of tasks, often leading to burnout <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Key pain points include:
*   Error-prone first drafts from numerous product teams <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   Time-consuming grooming tasks such as style checks, alt text generation, and SEO optimization <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   The risk of AI "hallucinations" if not properly managed <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

To address these, the strategy involves building specialized, single-purpose [[developing_ai_agents_and_agentic_workflows | agents]] rather than a single large, monolithic bot <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## AI Agent Architecture and Workflow

Six single-purpose [[developing_ai_agents_and_agentic_workflows | agents]] were built, operating behind a simple Next.js frontend <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Each [[AI agents | agent]] focuses on a repetitive, well-scoped job, allowing humans to concentrate on judgment and clarity <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The ideal tasks for [[AI agents | AI]] assistance are repeatable, high-volume, and low-creativity <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Specific Agents Developed
*   **Automated Editor:** Fixes grammar, formatting, and accuracy <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Image Alt Text Generator:** Provides instant accessibility wins <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Jargon Simplifier:** Translates technical developer language into plain English <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **SEO Metadata Generator:** Creates title and description metadata while adhering to character limits <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Docs Outline Builder:** Recommends navigation and structure (coming soon) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Slack Backbot:** Helps triage help channel requests <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Behind the Request Flow
Every request follows a structured flow <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:
1.  **Next.js UI:** Serves as the user interface <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
2.  **Custom GPT-4o Agent:** Utilizes an appropriate model for the specific job. This [[developing_ai_agents_and_agentic_workflows | custom GPT]] incorporates a baked-in style guide and rubric, retrieved from an AirTable for collaborative editing <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
3.  **Validation Layer:** Includes Veil linting and CI/CD tests <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
4.  **GitHub Pull Request (PR):** Adds codeowner review, making it easier to scrutinize [[AI agents | agent]] suggestions <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
5.  **Human Review and Merge:** A human merges changes only when they are correct, often after product and engineering reviews <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This multi-layered approach significantly reduces hallucinations <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

### Agent Demonstrations
During a demonstration, the capabilities of several [[AI agents | agents]] were showcased:
*   The **Automated Editor** allows users to input an MDX file or a live URL, and it generates a diff of changes along with explanations, linking revisions to specific style guide and rubric items <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   The **SEO Metadata Generator** creates meta titles and descriptions, accounting for character limitations <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   The **Alt Text Generator** quickly processes multiple images from selected pages or a live URL to generate compliant alt text <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   The **Jargon Simplifier** takes prepared text, simplifies it, and provides a diff, allowing for quick copy-pasting into pull request comments or direct file edits <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

While there's ongoing work to enable [[agent_continuations_for_ai_workflows | agents]] to communicate with each other, the current setup provides significant benefits <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

## Guard Rails for Quality and Resilience

To ensure quality and mitigate risks, [[best_practices_for_building_resilient_ai_workflows | guard rails]] are crucial <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>:
*   **Hallucinations:** Mitigated through tools like Veil Lint and CI tests, combined with human stakeholder review <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Bias:** Addressed through data set tests and prompt audits <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Stakeholder Misalignment:** Managed through weekly PR reviews (sometimes compressed to daily or hourly) and Slack feedback loops with product managers and engineering teams <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

These feedback cycles enable continuous prompt tuning, preventing over-reliance on the model's magical perfection <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## Playbook for Implementing AI

A recommended three-step playbook for other teams to implement [[AI in enterprise and startups | AI]] <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:
1.  **Identify a pain point:** Pinpoint a single area that significantly hinders throughput <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Pick a task:** Choose a single task that is repeatable and rule-based <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
3.  **Loop with users:** Engage with users weekly, at a minimum, to ship, measure, and refine solutions <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

By stacking these small wins, a team's velocity can significantly increase <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.