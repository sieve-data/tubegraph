---
title: Developing AI agents for productivity
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

Twilio's approach to [[developing_ai_agents_and_agentic_workflows | developing AI agents]] is centered on enhancing productivity rather than replacing human roles <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The goal is to leverage AI to work smarter, not to instill fear about job displacement <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This strategy focuses on turbocharging workflows within a small team, like Twilio's docs team <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Challenge: Pain Points for a Tiny Docs Team

Twilio's small documentation team faced significant challenges with a high volume of Jira tickets <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
*   **Error-prone first drafts** from over 100 product teams <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Time-consuming grooming tasks**, such as style checks, alt text generation, and SEO optimization <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Hallucination risk** if AI models were used without proper controls <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

The team needed leverage to manage the workload without experiencing burnout <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## The Solution: A Fleet of Single-Purpose AI Agents

Instead of [[developing_ai_agents_and_agentic_workflows | building]] one monolithic "megabot," Twilio opted to [[building_effective_ai_agents | build]] six single-purpose [[implementing_ai_agents_in_daily_operations | AI agents]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. These agents operate behind a simple Next.js frontend <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The "sweet spot" for an AI helper involves tasks that are repeatable, high-volume, and low-creativity <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Agent Breakdown

Each agent is designed to tackle a repetitive, well-scoped job, allowing humans to focus on judgment and clarity <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>:

*   **Automated Editor**: Fixes grammar, formatting, and accuracy in documentation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Image Alt Text Generator**: Provides instant accessibility by generating alt text for images <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Jargon Simplifier**: Translates technical developer language into plain English <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **SEO Metadata Generator**: Creates title and description metadata, ensuring character count compliance <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Docs Outline Builder**: Recommends navigation and structure for documentation (coming soon) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Slack Backbot**: Helps triage requests received through help channels <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Architecture and Workflow

The workflow for these [[building_effective_ai_agents | AI agents]] involves a layered approach that ensures accuracy and reduces errors <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>:

1.  **Next.js UI**: A user interface initiates requests <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
2.  **Custom GPT-401 Agent**: The appropriate model is used for each specific job <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This custom GPT incorporates Twilio's style guide and rubric, which are retrieved from an AirTable for easy collaboration <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
3.  **Validation Layer**: Includes Veil linting and CI/CD tests <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
4.  **GitHub PR**: Adds code owner review, making it easier to scrutinize agent-suggested changes <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
5.  **Human Merge**: A human merges the changes only when they are correct, typically after product and engineering reviews <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This ensures multiple human eyes review changes before they are finalized <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

This layered approach significantly reduces hallucinations without slowing down the process <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## The AI Docs Buddy in Action (Demonstration)

The AI Docs Buddy, led by Maria Bermudez, showcases the practical application of these agents <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The platform allows users to access various agents from an overview or release page <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Automated Editor
The automated editor can load an MDX or Markdown file, or plug in a live URL <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. It uses the GPT-401 model, which was chosen after experimentation for its consistent application of the style guide and rubric <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. The output shows a diff of changes and a "changes made" tab that lists original text, revised text, and the specific style guidance applied <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. While powerful, it's noted that it's "not perfect" and may occasionally miss things like missing SEO descriptions <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### SEO Metadata Generator
This agent generates a meta title and meta description for a given page, accounting for character limitations <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Alt Text Generator
Similar to the editor, the alt text generator can process a live URL or multiple selected pages <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. It quickly generates alt text that conforms to the required format for the docs platform <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

### Jargon Simplifier
This tool is useful for simplifying complex text, assisting in writing and reviewing pull requests <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. It provides a diff view and a revised text tab for quick copying and application as a pull request comment or direct file edit <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

The team is also working towards enabling these agents to communicate with each other <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

## Mitigating Risks with Guard Rails

[[challenges_in_ai_agent_development | Building effective AI agents]] requires robust guard rails to ensure quality and mitigate risks <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>:

*   **Hallucinations**: Mitigated using tools like Veil Lint and CI tests, combined with human oversight from various stakeholders <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Bias**: Addressed through data set tests and prompt audits <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Stakeholder Misalignment**: Managed with weekly PR reviews (which can be compressed to days or hours) and Slack feedback loops, particularly with product managers and engineering teams <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. These feedback cycles allow continuous prompt tuning <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## Playbook for Success

Twilio recommends a three-step playbook for other teams looking to [[developing_ai_agents_and_agentic_workflows | develop AI agents]] for productivity <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:

1.  **Identify a single pain point** that is hindering throughput <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Pick a single task** that is repeatable and rule-based <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  **Loop with your users weekly** (at least) through a "ship, measure, and refine" process <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

By stacking these small wins, teams can significantly increase their velocity <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Conclusion

Twilio's experience demonstrates that [[developing_ai_agents_and_agentic_workflows | AI agents]] can be embraced to enable smarter work, addressing common pain points and [[improving_ai_agent_task_execution | improving AI agent task execution]] through focused, single-purpose tools and robust human oversight <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.