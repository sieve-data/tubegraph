---
title: Benefits and challenges of using AI in workflow
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

AI is increasingly viewed not as a threat, but as an opportunity to [[integrating_ai_into_natural_workflows | integrate AI into natural workflows]] and work smarter <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This perspective highlights how [[applications_of_ai_in_productivity_and_automation | AI agents can turbocharge workflows]] without replacing human roles <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The [[impact_of_ai_on_development_workflow | impact of AI on day-to-day work]] is a significant current trend <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Workflow Pain Points and Challenges

A small documentation team, handling a high volume of Jira tickets, identified several key challenges:
*   **Error-prone first drafts** from numerous product teams <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Time-consuming grooming** tasks like style checks, alt text generation, and SEO optimization <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Hallucination risk** if AI models were used without proper controls <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

These issues pointed to a need for leverage rather than increased workload and burnout <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Leveraging AI for Workflow Augmentation

Instead of building one large AI system, the team developed six single-purpose AI agents <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. These agents are designed to tackle repetitive, high-volume, and low-creativity tasks, allowing humans to focus on judgment and clarity <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This approach exemplifies how [[ai_in_workflow_automation_and_augmentation | AI can automate and augment workflows]] effectively.

### Specific AI Agents and Their Benefits

*   **Automated Editor**: Fixes grammar, formatting, and accuracy in drafts <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. It shows a diff of changes and explains revisions based on style guides and rubrics <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Image Alt Text Generator**: Provides instant accessibility wins by generating accurate alt text for images <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. It can generate alt text for multiple images quickly and conforms to required formats <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Jargon Simplifier**: Translates technical developer language into plain English <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This is useful for writing and reviewing pull requests, providing quick edits <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **SEO Metadata Generator**: Provides title and description metadata while adhering to character limits <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Docs Outline Builder**: Recommends navigation and structure for documentation (coming soon) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Slack Backbot**: Helps triage help channel requests <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

These agents contribute to the [[applications_of_ai_in_productivity_and_automation | applications of AI in productivity and automation]], specifically in the [[automation_of_manual_workflows_with_ai_web_agents | automation of manual workflows with AI web agents]].

## Architecture and Guard Rails: Addressing Challenges

The architecture involves a Next.js UI feeding into a custom GPT-4o agent, with the appropriate model selected for each job <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The custom GPT incorporates a style guide and rubric, retrieved from Airtable for easy collaboration <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

A crucial aspect of this system is the implementation of "guard rails" to mitigate [[challenges_with_current_ai_implementation | challenges with current AI implementation]] and ensure quality <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>:

### Mitigating Hallucinations

*   A **validation layer** includes Veil linting and CI/CD tests <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **GitHub PRs** add codeowner review, making it easier to scrutinize agent suggestions <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Human approval**: A human hits the merge button only when changes are correct, often after product and engineering reviews <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This layered approach significantly reduces hallucinations <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Addressing Bias and Misalignment

*   **Bias**: Addressed through dataset tests and prompt audits <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Stakeholder Misalignment**: Managed through weekly PR reviews and Slack feedback loops with product managers and engineering teams <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. These feedback cycles allow for continuous prompt tuning <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

These strategies highlight the [[challenges_and_innovations_in_ai_engineering | challenges and innovations in AI engineering]] required for practical implementation.

## Playbook for AI Adoption: Navigating Challenges and Opportunities

To successfully adopt AI, a three-step playbook is recommended, offering a pathway to navigate [[challenges_and_opportunities_in_ai_adoption | challenges and opportunities in AI adoption]]:
1.  **Identify a critical pain point** that hinders throughput <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
2.  **Pick a single task** that is repeatable and rule-based, as this is the sweet spot for an AI helper <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a><a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
3.  **Loop with users weekly** (at least) to ship, measure, and refine the AI's performance <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

By stacking these small wins, teams can significantly increase their velocity <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This approach demonstrates how to overcome [[challenges_and_solutions_in_using_ai_for_unstructured_data | challenges and solutions in using AI for unstructured data]] by focusing on specific, well-scoped problems.