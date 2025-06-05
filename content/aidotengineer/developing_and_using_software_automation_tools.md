---
title: Developing and using software automation tools
videoId: UXOLprPvr-0
---

From: [[aidotengineer]] <br/> 

Biang, CTO and co-founder of Sourcegraph, and Bruno Pasos, Head of Product for developer experience at booking.com, discuss their partnership in building software development agents to automate toil within booking.com, aiming for measurable ROI and [[impact_of_ai_on_development_workflow | impact]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

A common challenge for large companies adopting AI is measuring its ROI and impact, a question booking.com is proactively addressing <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Booking.com's Context and Challenges

Booking.com aims to make travel easier for everyone, and internally, to clear paths for its developers to do their best work <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. As one of the largest online travel agencies, it serves approximately 1.5 million room nights and employs over 3,000 developers <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. The company handles over 250 merge requests and 2.5 million CI jobs annually <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

Booking.com is extremely data-driven, with its success rooted in experimentation and being obsessed with data <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This approach, primarily through A/B tests, leads to a significant accumulation of experiment flags and dead code within the codebase over decades <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This bloat increases cycle times, resulting in developers spending over 90% of their time on "toil" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Developer surveys confirm the increasing difficulty of working with the codebase <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Sourcegraph's Solutions

Sourcegraph's mission is to make building software at scale tractable <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Its products include:
*   **Code Search** – Described as "Google for your code," it allows human developers to find and understand code <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Large-scale refactoring and code migration tools** <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Cody** – An AI coding assistant, context-aware and tuned for large, messy codebases <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Agents** – Tools built to [[automation_of_manual_workflows_with_ai_web_agents | automate toil]] out of the software development life cycle <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

The unifying theme across Sourcegraph's products is to accelerate the developer inner loop, augment human creativity, and automate as much "BS" out of the outer loop as possible <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Partnership and Evolution of AI Adoption

Booking.com began using Sourcegraph Search over two years ago, finding it highly successful for navigating their large codebase <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Around a year ago, they started experimenting with Cody, leveraging its integration with Sourcegraph Search for context <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. The next step is building agents using both Cody and Sourcegraph Search <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Timeline of AI Tool Adoption and Measurement

The journey of adopting AI tools at booking.com has been rapid:
*   **January (Last Year)**: Cody was made available to all 3,000 developers <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Initial challenges included limited LLM choices and token limits <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Partnering with Sourcegraph, they removed guardrails, enabling multiple LLMs per developer, which was crucial as different LLMs showed expertise in different code contexts (e.g., excavating old code vs. developing new features) <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **July**: [[improving_developer_experience_and_productivity | Developer training]] on Cody began. This was "incredibly important" as developers who initially saw no value, after training, became daily users <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **January-October**: The initial metric for success, "hours saved," was found to be statistically irrelevant and based on limited research <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This led to brainstorming for more statistically relevant metrics <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **October**: New KPIs were defined to measure the [[ai_tools_for_business_efficiency | impact of GenAI]] within a one-year timeframe <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **November**: Traces showed developers using Cody daily (12+ days a month) were 30% faster <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. An API layer was created in front of Cody, allowing for creative integrations with tools like Slack and Jira, extracting functionality beyond the IDE <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

### Key Performance Indicators (KPIs) for AI Adoption

Booking.com defined four core KPIs for measuring GenAI impact over a year:
1.  **Lead time for change** <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>:
    *   **Short-term**: Time to review Merge Requests (MRs). Daily Cody users ship 30% more MRs than non-users, and their MRs contain less code <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
2.  **Quality** <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>:
    *   **Mid-term**: Reduce vulnerabilities by providing LLMs with past vulnerability context from the codebase to predict new ones <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   **Mid-term**: Increase test coverage, especially for legacy code, to ensure new platforms pass existing tests <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
3.  **Codebase insights** <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>:
    *   **Mid-term**: Track unused code parts, lingering feature flags, and non-performant code <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
4.  **Modernization** <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>:
    *   **Long-term**: Reduce the time to re-platform their codebase from years to months <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Building and Utilizing Software Agents

Engineers using Cody began to experiment with the underlying APIs, leading to a desire to compose calls into longer chain automations, now called "agents" <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Initial [[challenges_and_considerations_in_tool_creation_and_execution | pitfalls]] included managing expectations about LLM capabilities <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. A joint hackathon was held to build these agents <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Examples of AI Agents Developed

1.  **GraphQL Query Generator** <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>:
    *   Booking.com has a massive GraphQL API schema (over a million tokens) that doesn't fit into standard LLM context windows <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
    *   The agent uses Sourcegraph Search to find relevant nodes within the schema and then agentically walks up the tree to pull in relevant parent nodes <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
    *   This process allows the LLM to reason about which parts of the schema to use, generating coherent responses where naive approaches would result in "garbage" due to hallucinations <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
2.  **Automated Code Migration Agent** <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>:
    *   Targets legacy functions with over 10,000 lines of code to accelerate re-platforming efforts <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Combines Sourcegraph Search, structured meta-prompts, and the concept of dividing the code into smaller, manageable bits <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
    *   In-person pairing with experts was crucial, as developers often lacked knowledge on how to effectively use LLMs and craft prompts <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
    *   Developers spent months trying to understand the scope of the problem, but within two days of a hackathon, the agent could define and understand call sites, identifying low-hanging fruits <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
3.  **Code Review Agent** <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>:
    *   Addresses the universal practice of code review in enterprises <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
    *   Unlike generic AI code review tools, this agent is highly customizable to an organization's specific rules and guidelines <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
    *   Users define rules in a simple flat file format, which the agent consumes <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   The agent applies relevant rules to modified files in a PR and selectively posts comments, optimizing for precision to avoid noise <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

## Future Vision: Self-Healing Services and Declarative Coding

The goal is to develop self-healing services by shifting error detection left into the IDE, providing instant fixes based on service rules and prompts <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. This leverages developer-created prompt libraries to automate inquiries to the server and extract knowledge from the codebase <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

This approach has the potential to address a long-standing problem in software development: successful software becomes a victim of its own success due to accumulated technical debt and loss of cohesion <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. With declarative coding, senior engineers and architects can define constraints and rules that are automatically enforced throughout the codebase, both during code review and within the editor, for code written by humans or AI <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. This can also enforce compliance rules that don't directly feed new features to end-users <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## The Importance of Education

A key takeaway from this past year of partnership is the critical role of education <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Hand-holding entire business units, showing them the value of the tools, and enabling them to experiment through workshops and hackathons (even within two days) transforms them into passionate daily users <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. This education is vital to achieve the 30% plus increase in speed <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.