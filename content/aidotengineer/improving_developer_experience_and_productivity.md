---
title: Improving developer experience and productivity
videoId: UXOLprPvr-0
---

From: [[aidotengineer]] <br/> 

## Introduction
The partnership between Sourcegraph, a company building developer tools for large codebases, and Booking.com, a leading online travel agency, aims to [[agentic_editors_in_software_development | build software development agents]] to automate toil within Booking.com's operations <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. A key focus of this collaboration is demonstrating the real Return on Investment (ROI) and impact of these AI tools, addressing a common challenge many companies face when adopting AI <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## The Challenge at Booking.com
Booking.com's team is dedicated to clearing the path for their developers to do their best work <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The company operates at a vast scale, serving 1.5 million room nights and employing over 3,000 developers <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Technically, they handle over 250 million merge requests and 2.5 million CI jobs annually <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

Booking.com's culture is deeply data-driven, with an obsession for experimentation, primarily through A/B tests <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This dedication to experimentation has led to a significant problem: as new features are pushed, old experiment flags and dead code accumulate, making the codebase "extremely bloated" over decades <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This bloat results in increased cycle times <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a> and developers spending over 90% of their time on toil, such as debugging and maintenance <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This represents a significant [[challenges_in_software_maintenance_and_bug_fixing | challenge in software maintenance and bug fixing]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The aim is to free up brilliant developer minds from mundane tasks to focus on creating new features and solving user problems <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Sourcegraph's Solutions
Sourcegraph's mission is to make building software at scale tractable <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Their products include:
*   **Code Search**: Described as a "Google for your code," it allows developers to quickly find and understand code <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Large-scale Refactoring and Code Migration Tools** <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Cody**: An AI coding assistant that is context-aware and tuned for large, messy codebases <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **AI Agents**: Tools built to automate toil out of the software development lifecycle <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

The unifying theme of Sourcegraph's tools is to accelerate the developer inner loop, augment human creativity, and automate as much "BS" out of the outer loop as possible <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Booking.com's Journey with AI
Booking.com began using Sourcegraph Search over two years ago with great success, improving the ability to navigate their bloated codebase <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

In January of the previous year, Booking.com started experimenting with Cody, which leveraged Sourcegraph Search for context <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Initially, all 3,000 developers were given access <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Early feedback showed some developers didn't see value, which intrigued the team <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Key Milestones and Learnings:
*   **Early Challenges**: Limited by a single LLM choice and token limits <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Partnership and Flexibility**: Sourcegraph enabled Booking.com to remove guardrails and offer multiple LLMs per developer, recognizing that LLMs have different areas of expertise for tasks like excavating old code versus developing new features <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. This demonstrates an [[integration_of_ai_into_development_environments_and_editors | integration of AI into development environments and editors]].
*   **Training and Adoption**: By July, training developers became crucial. Those who received training started using Cody daily, becoming "daily users" <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This highlights the importance of [[developing_and_using_software_automation_tools | developing and using software automation tools]] effectively.
*   **Measuring Impact**:
    *   Initial metric, "time saved," was found to be statistically irrelevant and based on limited research <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
    *   By October, new, statistically relevant KPIs were defined <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
    *   By November, traces showed daily Cody users were **30% faster** <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
    *   An API layer was created for Cody, allowing integration with tools like Slack and Jira, extending its use beyond the IDE <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. This showcases the [[impact_of_ai_on_development_workflow | impact of AI on development workflow]].

## Defined KPIs for Measuring AI Impact
Booking.com established four key performance indicators to measure AI impact within a year:
1.  **Lead Time for Change** <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>
    *   **Short Term (Metrics observed)**: Developers using Cody daily shipped 30% more Merge Requests (MRs) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. These MRs also contained less code, though the implications are still being analyzed <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
2.  **Quality** <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>
    *   **Mid-Term (Aspirations)**: Predicting new vulnerabilities or identifying lingering ones by providing codebase context <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Increasing test coverage, especially for legacy code during re-platforming <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
3.  **Codebase Insights** <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>
    *   **Mid-Term (Aspirations)**: Tracking unused parts of the codebase, lingering feature flags, and non-performant code <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
4.  **Modernize (Re-platforming Time)** <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>
    *   **Long-Term Goal**: Reduce the time to re-platform their codebase from years to months <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## AI Agents in Action
As developers started using AI coding assistants, they also began experimenting with the underlying APIs, leading to a desire to build longer chain automations, or "agents" <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

A joint hackathon between Sourcegraph and Booking.com yielded significant breakthroughs:

1.  **GraphQL Agent**:
    *   This agent generates GraphQL queries for Booking.com's massive GraphQL API, which is over a million tokens long and doesn't fit into a single LLM context window <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
    *   The system uses Sourcegraph Search to find relevant nodes within the schema and then [[agentic_editors_in_software_development | agentically]] figures out which ones are relevant, pulling in necessary parent nodes <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
    *   This approach significantly reduced hallucinations and led to far better results compared to naive implementations <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

2.  **Automated Code Migration Agent**:
    *   This agent targets legacy functions with over 10,000 lines of code to accelerate re-platforming efforts <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
    *   It leverages Sourcegraph Search, structured meta-prompts, and the concept of dividing the codebase into smaller, conquerable bits <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
    *   Pairing with experts to provide knowledge on effective LLM prompting was crucial <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
    *   A problem that previously took developers months to understand and size was defined and started to yield "low-hanging fruits" within two days during the hackathon <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

3.  **AI Code Review Agent**:
    *   While many startups offer AI code review, Booking.com found that enterprise code review is highly specific to the organization, with a long tail of internal rules and guidelines <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. Off-the-shelf tools often lack sufficient customizability <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
    *   The built interface allows organizations to define a set of rules for their code in a simple flat file format <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   The agent consumes these rules, applies relevant ones to modified files in a Pull Request (PR), and selectively posts highly precise comments tuned to those rules <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.

## The Future of AI in Software Development
The goal is to move towards self-healing services by declaring rules for a service and shifting error anticipation and fixes left into the IDE <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. This envisions [[future_of_ai_in_improving_user_experience_and_integrations | AI integration]] that provides errors and fixes directly within the development environment <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

This approach has the potential to solve a long-standing problem in software development: the inevitable accumulation of technical debt as successful software grows <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. With declarative coding, senior engineers and architects can define constraints and rules that must hold across the codebase <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. These rules can then be enforced during code review and directly within the editor, whether the code is written by humans or AI <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. This can also apply to compliance rules and other non-feature-adding tasks <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## The Importance of Education
The most important lesson from this year-long collaboration is the power of **education** <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. By educating developers and providing hands-on workshops and hackathons, teams became passionate about AI tools and transformed into daily users <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This direct experience led to the validated 30%+ increase in development speed <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. This demonstrates the critical role of [[turning_development_experiences_into_organized_knowledge | turning development experiences into organized knowledge]] through training.