---
title: Case study of AI application in documentation
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

Elmer Thomas, Principal Developer Educator at Twilio, presents a case study on how their small documentation team leverages AI to enhance workflows rather than replace human workers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The approach aims to embrace AI to "work smarter" <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Initial Pain Points in Documentation <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

The tiny documentation team faced a significant influx of Jira tickets, leading to three primary challenges:
1.  **Error-prone first drafts** from over 100 product teams <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  **Time-consuming grooming tasks**, such as style checks, alt text generation, and SEO optimization <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  **Hallucination risk** if AI was left unchecked <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The team sought "leverage, not burnout" to address these issues <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## AI Agent Architecture and Implementation Strategy <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>

Instead of a single "megabot," Twilio's docs team built six single-purpose AI agents operating behind a simple Next.js frontend <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This strategy falls under [[strategies_for_effective_ai_implementation | strategies for effective AI implementation]] and [[ai_in_workflow_automation | AI in workflow automation]].

### Specific AI Agents Built <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
Each agent is designed to tackle a repetitive, well-scoped job, allowing humans to focus on judgment and clarity <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Automated Editor:** Fixes grammar, formatting, and accuracy <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Image Alt Text Generator:** Provides instant accessibility wins <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Jargon Simplifier:** Translates developer terminology into plain English <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **SEO Metadata Generator:** Creates title and description metadata while adhering to character limits <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Docs Outline Builder (Coming Soon):** Recommends navigation and structure <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Slack Backbot:** Helps triage help channel requests <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Sweet Spot for AI Tasks <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
The rule of thumb for selecting tasks for an AI helper is to pick those that are:
*   Repeatable <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   High volume <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   Low creativity <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>

### Technical Flow and Guardrails <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
The process for each request incorporates several layers of oversight:
1.  **Next.js UI:** Front-end interface <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
2.  **Custom GPT-4o Agent:** Utilizes the appropriate model for the job <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The custom GPT includes Twilio's style guide and rubric, retrieved from an AirTable for easy collaboration <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
3.  **Validation Layer:** Includes Veil linting and CI/CD tests <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
4.  **GitHub Pull Request (PR):** Adds codeowner review, making it easier to scrutinize agent-suggested changes <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
5.  **Human Merge:** A human only merges the changes when they are correct, typically after product and engineering reviews <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This layered approach significantly reduces hallucinations <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## Live Demo Overview <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
Maria Bermudez, Lead Developer of the AI Docs Buddy, demonstrated the agents <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The system can autogenerate overview and release pages using Copilot <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Automated Editor <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>
This agent allows users to load an MDX or Markdown file, or plug in a live URL <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. It uses the GPT-4o model, chosen for its consistency in applying Twilio's style guide and rubric <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. The output shows a diff of changes and a detailed list of explanations, including original text, revised text, and the specific style guide/rubric items addressed <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. It's acknowledged that it's "not perfect," sometimes missing things like SEO descriptions <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### SEO Metadata Generator <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
This agent generates a meta title (which can be toggled off if not desired) and a meta description, accounting for character limitations <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Image Alt Text Generator <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
Similar to the editor, this agent can take a live URL or allow users to select multiple pages to generate alt text for all images. It produces alt text quickly and conforms to the required format of Twilio's docs platform <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

### Jargon Simplifier <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>
Useful for both writing and reviewing pull requests, this agent simplifies complex text <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. It provides a diff-like editor and a revised text tab for quick copying and application as a pull request comment or direct file edit <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

The team is currently working on enabling agents to communicate with each other <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

## Guardrails and Risk Mitigation <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>
Effective [[strategies_for_effective_ai_implementation | AI implementation]] requires robust guardrails to ensure quality, addressing risks such as:
*   **Hallucinations:** Mitigated using tools like Veil Lint and CI tests, combined with multiple human stakeholders reviewing <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Bias:** Addressed through dataset tests and prompt audits <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Stakeholder Misalignment:** Managed through weekly PR reviews (sometimes compressed to days or hours) and Slack feedback loops, especially with product managers and engineering teams <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. These feedback cycles allow for continuous prompt tuning <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## Playbook for AI Implementation <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>
Twilio shares a three-step playbook for teams looking to implement AI:
1.  **Identify one pain** that significantly impacts throughput <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Pick a single task** that is repeatable and rule-based <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
3.  **Loop with your users weekly**, at minimum <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

The process should be "Ship, measure, and refine" <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Stacking these small wins can significantly boost a team's velocity <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This serves as a [[case_studies_and_practical_examples_of_ai_implementation | practical example of AI implementation]] and outlines [[steps_to_create_effective_evaluations_for_ai_applications | steps to create effective evaluations for AI applications]].