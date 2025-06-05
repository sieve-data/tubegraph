---
title: Building singlepurpose AI agents
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

Elmer Thomas, Principal Developer Educator at Twilio, presented at the AI Engineer World's Fair on how their small documentation team leverages [[building_and_improving_ai_agents | AI agents]] to enhance workflows rather than replace staff <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The talk, titled "The Robots Are Coming for Your Job, and That's Okay," aims to demonstrate why AI should be embraced for smarter work <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Identifying Pain Points in Documentation Workflows

The Twilio docs team faced significant challenges with a high volume of Jira tickets <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Three main issues were identified <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>:
1.  **Error-prone first drafts**: Over 100 product teams submitted drafts, often leading to errors <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  **Time-consuming grooming**: Tasks like style checks, alt text generation, and SEO optimization were time sinks <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  **Hallucination risk**: Allowing large language models (LLMs) to operate unchecked posed a risk of generating incorrect information <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

To combat burnout and improve efficiency, the team sought leverage <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Architecture: Six Single-Purpose AI Agents

Instead of developing one large, monolithic bot, Twilio built six [[different_architectures_for_ai_agents | single-purpose AI agents]] accessible via a Next.js frontend <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Each agent is designed to tackle a specific, repetitive, and well-scoped job, allowing human team members to focus on judgment and clarity <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The rule of thumb for selecting tasks for [[components_of_ai_agents | AI helpers]] is to pick those that are repeatable, high-volume, and low-creativity <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

The agents developed include:
*   **Automated Editor**: Fixes grammar, formatting, and accuracy in documentation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Image Alt Text Generator**: Provides instant accessibility by generating alt text for images <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Jargon Simplifier**: Translates technical developer language into plain English <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **SEO Metadata Generator**: Creates title and description metadata, ensuring character count compliance <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Docs Outline Builder**: Recommends navigation and document structure (coming soon) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Slack Backbot**: Assists in triaging help channel requests <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Agent Workflow and Human Oversight
The general workflow for each request involves a Next.js UI feeding into a custom GPT-4o agent <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The appropriate model is chosen for each specific job <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

Key aspects of the architecture include:
*   **Custom GPT**: Incorporates Twilio's style guide and rubric, which are retrieved from an Airtable for easy collaboration <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Validation Layer**: Includes Veil linting and CI/CD tests <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **GitHub PRs**: Codeowner reviews are integrated, making it easier to scrutinize agent-suggested changes <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Human Approval**: A human only merges changes when they are correct, often after product and engineering reviews <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

This layered approach significantly reduces hallucinations without slowing down the process <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Live Agent Walkthrough
Maria Bermudez, a lead developer of the AI Docs Buddy, demonstrated the agents <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

*   **Automated Editor**: Allows users to load MDX files or plug in a live URL <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. It uses the GPT-4o model for consistent application of the style guide and rubric <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. The tool shows a diff of changes and provides a detailed explanation of original text, revised text, and the specific style guide/rubric items that triggered the changes <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **SEO Metadata Generator**: Can generate metatitles and meta descriptions, accounting for character limitations <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Alt Text Generator**: Offers the option to plug in a live URL or process multiple pages simultaneously, quickly generating alt text in the required format <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Jargon Simplifier**: Helps simplify complex technical text, useful for writing and reviewing pull requests <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. It provides a diff and a revised text tab for easy copying and application of edits <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

The team is currently working on enabling agents to communicate with each other <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

## Guard Rails: Mitigating Risks in AI Development
To ensure quality and mitigate risks, Twilio implemented several guard rails <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>:

*   **Hallucinations**: Mitigated using Veil Lint and CI tests, combined with multiple human stakeholders' reviews <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Bias**: Addressed through dataset tests and prompt audits <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Stakeholder Misalignment**: Prevented via weekly (or more frequent) PR reviews and Slack feedback loops with product managers and engineering teams <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

These feedback cycles enable continuous prompt tuning, rather than relying on the model to remain perfect <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## Playbook for Building AI Agents
The Twilio team suggests a three-step playbook for other teams to adopt when [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]] <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:
1.  **Identify one pain point** that significantly impacts throughput <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Pick a single task** that is repeatable and rule-based <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
3.  **Loop with users weekly** (at least): Ship, measure, and refine <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

By stacking small wins, teams can significantly increase their velocity <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.