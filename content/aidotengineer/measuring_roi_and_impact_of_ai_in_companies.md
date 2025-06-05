---
title: Measuring ROI and impact of AI in companies
videoId: UXOLprPvr-0
---

From: [[aidotengineer]] <br/> 

Many large companies face the challenge of proving the return on investment (ROI) and measurable impact of their AI adoption initiatives <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Often, initial AI purchases are driven by "fomo" (fear of missing out) or executive mandates, leading to questions from finance departments about tangible benefits <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Booking.com, a major online travel agency with over 3,000 developers and a highly data-driven culture, has been at the forefront of addressing this challenge by systematically [[importance_of_evaluation_and_metrics_in_ai_systems | measuring the impact of AI solutions]] on its software development processes <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## The Challenge: A Bloated Codebase

Booking.com's core mission is to make experiencing the world easier, while its developer experience team aims to clear paths for developers to do their best work <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The company's success is rooted in extensive experimentation, primarily through A/B tests <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Over decades, this approach led to a massive, bloated codebase riddled with persistent feature flags and dead code, resulting in increased cycle times and developers spending over 90% of their time on "toil" rather than innovative features <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This environment highlighted the need to unlock developers' minds from legacy craft to focus on new features and user problems <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Sourcegraph, a partner in this endeavor, aims to make building software at scale tractable, accelerating the developer inner loop, augmenting human creativity, and automating "BS" from the outer loop <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Their tools include Code Search (a "Google for your code"), large-scale refactoring tools, and Cody, an AI coding assistant <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## Evolving AI Adoption and Metrics

Booking.com's journey with AI began with adopting Sourcegraph's Code Search over two years ago, which significantly improved the ability to navigate their large codebase <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. About a year later, in January, they started experimenting with Cody, leveraging its context-awareness derived from Code Search <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

Initially, all 3,000 developers were given access to Cody, but usage varied, with some stopping due to perceived lack of value <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Early limitations included relying on a single LLM and token limits <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Working with Sourcegraph, Booking.com removed guardrails, enabling multiple LLMs per developer, recognizing that different LLMs had "expertise" better suited for tasks like excavating bloated codebases versus developing new services <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### The Shift to Robust KPIs

The initial metric of "hours saved" proved statistically irrelevant and was considered "semi-BS" <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. By October, Booking.com had defined new, measurable KPIs (Key Performance Indicators) and metrics that could demonstrate results within a year <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>:

*   **Lead Time for Change**:
    *   **Short-term metric**: Time to review Merge Requests (MRs) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **Observed Impact**: Developers using Cody daily (12+ days a month) shipped 30%+ more MRs, and their MRs were "lighter" with less code <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>, <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Quality**:
    *   **Mid-term metrics**: Predicting new vulnerabilities based on historical data and increasing test coverage, especially for legacy code during re-platforming <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Codebase Insights**:
    *   **Long-term metrics**: Tracking unused code, lingering feature flags, and non-performant code <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
    *   **Ultimate Goal**: Reducing the time to re-platform their codebase from years to months <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

## Automating Toil with AI Agents

A crucial part of Booking.com's success lies in building AI agents to automate toil in the software development lifecycle <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Developers started customizing prompts and building longer chain automations, leading to the creation of these agents <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

Key agents developed through joint hackathons with Sourcegraph include:

*   **GraphQL Query Generator**: This agent addresses the challenge of a massive GraphQL API (over a million tokens long) that doesn't fit into standard LLM context windows <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. It intelligently searches the schema, identifies relevant nodes, walks up the schema tree to pull in parent nodes, and then generates coherent GraphQL queries, avoiding the "garbage" output of naive approaches <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Automated Code Migration**: Aimed at accelerating re-platforming efforts, this agent tackles legacy functions with over 10,000 lines of code <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. By leveraging Code Search, structured meta-prompts, and dividing the codebase into smaller, conquerable bits, it allows developers to quickly define and understand the scope of migration problems <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. A problem that previously took months for developers to size could be defined within two days using this agent <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Tailored Code Review Agent**: Recognizing that off-the-shelf AI code review tools lack the customization needed for specific organizational rules and guidelines, Sourcegraph built an interface to productize the process of building a team- and organization-tailored review agent <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This agent consumes rules defined in a simple flat file, applies relevant ones to modified files in a PR, and selectively posts precise comments to avoid noise <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

## The Future: Self-Healing Services and Declarative Coding

Looking forward, the vision is to create self-healing services where errors are anticipated and fixed directly within the IDE, effectively "shifting left" current CI pipeline errors <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. This involves using the context of the codebase and developer-created prompts to automate questions to the server, extracting knowledge and implementing fixes <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.

This approach leverages "declarative coding" to address the perennial problem of software becoming a "victim of its own success," where accumulating technical debt from feature requests and bug reports leads to a loss of code cohesion and standards <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. With declarative coding, senior engineers, architects, and leaders can define constraints and rules that are automatically enforced throughout the codebase at review time and within the editor, for code written by humans or AI <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. This includes compliance rules and other non-feature-facing requirements that often consume significant developer time <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## The Importance of Education

A critical factor in Booking.com's success has been comprehensive developer education <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. Many developers initially stopped using Cody due to a "pure lack of knowledge" on how to effectively work with LLMs and craft appropriate prompts <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Through workshops and hackathons, Booking.com educated developers, showing them the value and enabling them to experiment with the tools. This hands-on approach transformed initial skeptics into "daily users," helping to defend the observed 30%+ increase in development speed <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. For any company embarking on AI adoption, "education" is the primary takeaway <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.