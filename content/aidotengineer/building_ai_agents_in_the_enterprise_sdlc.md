---
title: Building AI agents in the enterprise SDLC
videoId: UXOLprPvr-0
---

From: [[aidotengineer]] <br/> 

This article details the partnership between Sourcegraph and Booking.com to develop [[AI agents in DevOps | software development agents]] aimed at automating toil and demonstrating measurable ROI within large enterprise codebases <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The collaboration addresses common challenges faced by large companies in [[implementing_ai_in_enterprises | adopting AI]] and proving its impact <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## The Challenge of Large Enterprise Codebases

Booking.com, as one of the world's largest online travel agencies with over 3,000 developers <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, faces significant challenges with its codebase. The company processes over 250 million merge requests and 2.5 million CI jobs annually <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

A core issue stems from its data-driven, experimentation-obsessed culture <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Experiments, often in the form of A/B tests, lead to [[integration_of_ai_agents_into_existing_infrastructure | feature flags]] and dead code accumulating in the codebase over time <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This results in:
*   An [[agentic_enterprise_and_ai_agents | extremely bloated codebase]] <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Increased cycle times and longer debugging periods <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   Developers spending over 90% of their time on "toil" <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   Frustration among developers due to the difficulty of working with the code <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

> "I've seen the best developer minds of my generation destroyed by decade long dead feature flag migrations." <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>

This situation diverts brilliant engineering minds from working on new features and user problems to maintaining [[integration_of_ai_agents_into_existing_infrastructure | legacy craft]] <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Sourcegraph's Contribution

Sourcegraph's mission is to make building software at scale tractable <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Their key products include:
*   **Code Search:** A "Google for your code" that helps developers understand codebases <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Booking.com adopted Code Search over two years ago with great success <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Cody:** An [[Building AI Agents without Frameworks | AI coding assistant]] that is context-aware and tuned for large, messy codebases <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Booking.com began experimenting with Cody a year ago, leveraging its integration with Sourcegraph Search <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

The unifying theme of Sourcegraph's products is to accelerate the developer inner loop, augment human creativity, and automate toil from the outer loop of the software development life cycle <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Booking.com's AI Journey and Measurable Impact

Booking.com's journey with [[building_and_scaling_ai_use_cases_for_enterprises | GenAI innovation]] and [[Building AI agents in the enterprise SDLC | AI agents]] involved a rapid evolution over a year <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>:

### Early Stages (January)
*   Initial rollout of Cody to all 3,000 developers <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Challenges included a single LLM choice, token limits, and a lack of perceived value from some users <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   Partnership with Sourcegraph enabled the removal of guardrails, allowing multiple LLMs per developer, which was crucial as LLMs demonstrated expertise in different code contexts (e.g., legacy vs. new service development) <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Evolution and Training (July)
*   [[Building and Improving AI Agents | Developer training]] became critical, transforming initial skeptics into "daily users" <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Shifted from "hours saved" (a statistically irrelevant metric based on limited research) to more robust metrics <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Defining KPIs and Impact (October-November)
*   **New KPIs defined in October** <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>:
    *   **Lead Time for Change:**
        *   *Short-term:* Time to review Merge Requests (MRs). Daily Cody users ship 30%+ more MRs, and their MRs are lighter (less code) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **Quality:**
        *   *Mid-term:* Predicting and eliminating vulnerabilities in the codebase <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
        *   *Long-term:* Increasing test coverage, especially for legacy code during re-platforming efforts <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
    *   **Codebase Insights:**
        *   *Mid-term:* Tracking unused code, lingering feature flags, and non-performant code <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
    *   **Modernization:**
        *   *Long-term:* Reducing the time to re-platform the codebase from years to months <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **November Findings:** Traces showed developers using Cody daily were 30%+ faster <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   An API layer was created for Cody, enabling [[integration_of_ai_coding_agents_with_thirdparty_tools | integration with existing tools]] like Slack and Jira, extracting its utility beyond the IDE <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

## Specific AI Agent Use Cases

The shift from coding assistants to [[building_and_improving_ai_agents | AI agents]] arose from engineers' desire to compose LLM calls into longer chain automations <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. A joint hackathon was crucial in building initial agents <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### 1. GraphQL Schema Agent
*   **Problem:** Booking.com's GraphQL API schema is over a million tokens long, making it impossible to fit into current LLM context windows, leading to hallucinations if naively integrated <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Solution:** An agent that searches the large schema, identifies relevant nodes, and agentically reasons which parent nodes to pull in. This process generates coherent and accurate responses <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

### 2. Automated Code Migration Agent
*   **Problem:** Migrating legacy functions, some with over 10,000 lines of code, for re-platforming efforts was a massive, time-consuming task <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. Developers spent months just understanding the problem size <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Solution:**
    *   Leveraged Code Search and structured meta-prompts <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
    *   Employed a "divide and conquer" approach for smaller code bits <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
    *   **Crucial:** Pairing with experts significantly accelerated the process. During a two-day hackathon, they were able to precisely define the problem size and identify call sites, which had previously taken months <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. This highlights that lack of knowledge in working with LLMs was a major impediment <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

### 3. Customizable AI Code Review Agent
*   **Problem:** While many off-the-shelf AI code review tools exist, they often lack the customization needed for enterprise-specific rules, guidelines, and a long tail of organizational requirements <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Solution:** An interface for productizing the process of building a review agent tailored to a specific team or organization <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
    *   Users define rules in a simple flat file format <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   The agent consumes these rules and selectively applies relevant ones to modified files in a Pull Request <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
    *   It posts precise, targeted comments, optimizing for precision over recall to avoid noise <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

## The Future: Self-Healing Services and Declarative Coding

The goal is to move towards self-healing services <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This involves:
*   Anticipating CI pipeline errors and shifting them left to the IDE <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.
*   Presenting errors with immediate fixes <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.
*   Leveraging developer-created prompt libraries to automate questions to the server and extract knowledge from the codebase <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

This approach has the potential to solve the "mythical man-month" problem, where successful software becomes a victim of its own success due to accruing technical debt and losing code cohesion with more contributors <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
With declarative coding, senior engineers and architects can define constraints and rules that must hold throughout the codebase <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. These rules can then be enforced automatically at code review time and within the editor, regardless of whether the code is written by a human or AI <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. This also helps with compliance rules and other non-feature-related developer toil <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

## Key Takeaway: Education is Paramount

The most important factor in the success of [[Building AI agents in the enterprise SDLC | AI agent]] adoption and demonstrating value has been **education** <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. By educating developers and providing hands-on workshops and hackathons, they become passionate daily users, leading to the observed 30%+ increase in speed <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.