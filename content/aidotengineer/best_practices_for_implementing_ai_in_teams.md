---
title: Best practices for implementing AI in teams
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

Implementing AI in teams, especially small ones, can significantly turbocharge workflows rather than replacing human roles <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The key is to embrace AI to work smarter, not to instill fear <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Identifying Pain Points for AI Integration

Before implementing AI, it's crucial to identify specific pain points within existing workflows that AI can address <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Common issues include:
*   **Error-prone first drafts:** Receiving initial content that frequently contains errors from various sources <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Time-consuming grooming:** Manual checks for style, accessibility (e.g., alt text), and search engine optimization (SEO) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Hallucination risk:** The potential for AI to generate incorrect or fabricated information if left unchecked <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

The goal is to gain leverage and prevent burnout <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Architecture and Agent Design

Instead of creating one large, monolithic "megabot," a more effective approach is to build multiple single-purpose AI agents <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Each agent should tackle a repetitive, well-scoped job, allowing humans to focus on judgment and clarity <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Core Principles for Task Selection
The "sweet spot" for an AI helper involves tasks that are:
*   Repeatable <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   High volume <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   Low creativity <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>

### Example Agent Types
A documentation team leveraged AI to build agents for specific functions, demonstrating [[developing_ai_agents_for_productivity | developing AI agents for productivity]]:
*   **Automated Editor:** Fixes grammar, formatting, and accuracy <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Image Alt Text Generator:** Provides instant accessibility wins <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Jargon Simplifier:** Translates technical language into plain English <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **SEO Metadata Generator:** Creates title and description metadata while adhering to character limits <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Docs Outline Builder:** Recommends navigation and structure (coming soon) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Slack Backbot:** Helps triage requests from help channels <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Workflow and Architecture
A typical workflow for AI agent requests might include:
1.  **Frontend:** A user interface (e.g., Next.js UI) <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
2.  **Custom GPT Agent:** Utilizing an appropriate model (e.g., GPT-4o) with an integrated style guide and rubric, which can be retrieved from a collaborative source like Airtable <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
3.  **Validation Layer:** Implementing checks like Veil Linting and CI/CD tests <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
4.  **Codeowner Review:** Integrating with version control systems (e.g., GitHub Pull Requests) to facilitate scrutiny of changes suggested by agents <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
5.  **Human Merge:** A human decision point to merge changes only when correct, often after product and engineering reviews <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

This layered approach helps in [[best_practices_for_building_resilient_ai_workflows | building resilient AI workflows]] and significantly reduces hallucinations <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## Guard Rails for Quality Control

To ensure quality and mitigate risks, implement robust guard rails:

*   **Hallucinations:**
    *   Utilize tools like Veil Lint and CI tests <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   Involve human stakeholders for review <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

*   **Bias:**
    *   Conduct data set tests <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   Perform prompt audits <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

*   **Stakeholder Misalignment:**
    *   Conduct weekly (or more frequent) Pull Request reviews <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
    *   Establish Slack feedback loops, especially with product managers and engineering teams <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

These feedback cycles are essential for continuously tuning prompts rather than relying on the model to remain perfect <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## A Three-Step Playbook for Success

For teams looking to adopt AI, here's a recommended playbook that aligns with [[building_successful_ai_projects_with_small_teams | building successful AI projects with small teams]] and [[strategies_for_effective_ai_implementation | strategies for effective AI implementation]]:

1.  **Identify one pain point** that is significantly hindering throughput <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Pick a single task** that is repeatable and rule-based <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  **Loop with your users weekly** at a minimum, following a "ship, measure, and refine" approach <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

Stacking these small wins can significantly boost a team's velocity <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Encouragement from [[leadership_and_organizational_strategies_for_ai_integration | leadership]] is also key to pushing boundaries with AI <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.