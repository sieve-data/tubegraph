---
title: Challenges of maintaining large codebases
videoId: UXOLprPvr-0
---

From: [[aidotengineer]] <br/> 

Maintaining large and complex codebases presents significant challenges for organizations, impacting developer productivity, efficiency, and the overall quality of software development <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Causes of Codebase Bloat

At companies like Booking.com, a major contributor to codebase bloat is their obsession with experimentation and being data-driven <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a> <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. As new features are brought to users, experiments and feature flags are added to the codebase <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. Often, these experiment flags or dead code persist in the codebase for decades, leading to an "extremely bloated" state <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a> <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

## Impact on Development

The consequences of a bloated codebase are substantial:
*   **Increased Cycle Times** As the codebase grows, software development cycle times become longer <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a> <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   **High Toil Percentage** Developers may spend over 90% of their time on "toil"—debugging and working on the code base rather than on innovative features <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a> <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
*   **Decreased Developer Satisfaction** Surveys reveal that it becomes increasingly difficult for developers to perform their work <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a> <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
*   **Misallocation of Talent** Brilliant engineers may be "destroyed by decade-long dead feature flag migrations," instead of focusing on new features and user problems <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a> <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a> <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
*   **Erosion of Standards** Over time, as more contributors are added to the codebase, there is a loss of cohesion, vision, and the maintenance of established coding standards <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a> <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

This phenomenon, described as successful software becoming "a victim of its own success," is due to the accumulation of technical debt as businesses prioritize new features and bug fixes to remain competitive <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a> <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

## Solutions and Impact Measurement

Companies like Sourcegraph aim to make building software at scale "tractable" <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. Solutions include:
*   **Code Search Tools** Tools like Sourcegraph's Code Search help developers navigate and understand large, messy codebases <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a> <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.
*   **[[large_language_models_in_code_generation | AI Coding Assistants]]** [[large_language_models_in_code_generation | AI coding assistants]] like Cody, which are context-aware and tuned for large codebases, can accelerate the developer inner loop and augment human creativity <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a> <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a> <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.
*   **[[impact_of_ai_coding_agents_on_software_engineering | Software Development Agents]]** The primary focus is on [[impact_of_ai_coding_agents_on_software_engineering | agents]] that automate "toil" out of the software development lifecycle <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a> <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a> <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. These [[impact_of_ai_coding_agents_on_software_engineering | agents]] aim to automate large-scale refactoring and code migrations <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a> <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. Examples of such [[impact_of_ai_coding_agents_on_software_engineering | agents]] include:
    *   **GraphQL Query Generation** An agent that searches massive GraphQL schemas (over a million tokens) to find relevant nodes and generate coherent queries, overcoming context window limitations and hallucinations common with naive [[building_and_scaling_large_language_models | LLM]] usage <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a> <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
    *   **Automated Code Migration** [[impact_of_ai_coding_agents_on_software_engineering | Agents]] designed to handle legacy functions with over 10,000 lines of code, speeding up replatforming efforts by dividing the codebase into smaller, conquerable bits <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a> <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a> <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a> <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. This drastically reduces the time needed to understand problem scope from months to days <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a> <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
    *   **AI-Powered Code Review** Customizable [[impact_of_ai_coding_agents_on_software_engineering | agents]] that consume organization-specific rules and guidelines (defined in a simple flat file format) to selectively post comments during code review, ensuring precision and reducing noise <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a> <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a> <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

Organizations are measuring the impact of these solutions using KPIs like:
*   **Lead Time for Change** <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>
*   **Code Quality** (e.g., reducing vulnerabilities, increasing test coverage, especially for legacy code) <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a> <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.
*   **Codebase Insights** (e.g., tracking unused code, lingering feature flags, and non-performant code) <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a> <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

The ultimate goal for Booking.com is to reduce the time to replatform their codebase from years to months <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a> <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

## The Future of Codebase Maintenance

The potential for self-healing services and the ability to declare service rules are emerging as key areas <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a> <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a> <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. By anticipating CI pipeline errors and shifting checks left into the IDE, developers can receive immediate fixes <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a> <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Declarative coding allows senior engineers and architects to define and enforce constraints and rules throughout the codebase, both at review time and within the editor, for code written by humans or [[impact_of_ai_coding_agents_on_software_engineering | AI]] <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a> <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. This addresses the long-standing problem of maintaining standards and cohesion in large, evolving software projects <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a> <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

A crucial factor in successful adoption and achieving positive impacts is **education** <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. By educating developers through workshops and hackathons, companies can transform them into daily users who are passionate about the tools and contribute to measurable improvements in speed <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a> <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.