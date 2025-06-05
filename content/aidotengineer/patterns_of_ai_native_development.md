---
title: Patterns of AI Native Development
videoId: 9u6xvcNJaxc
---

From: [[aidotengineer]] <br/> 

This article explores the four emerging patterns of [[ai_native_companies | AI native]] development, detailing how AI has transformed the software development workflow since the rise of generative AI <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Technology has evolved from simple Large Language Models (LLMs) to Retrieval Augmented Generation (RAG), code indexing, advanced functions, and even teams of agents <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Similar to the cloud-native explosion, AI is ushering in a new way of working <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

The integration of AI changes our tasks: some are replaced, others are enhanced, and new ones emerge <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The core of this shift is the developer, moving into different areas of expertise <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Speaker Background
The speaker is an independent industry advisor known for work in DevOps and DevSecOps, focusing on automation, which aligns well with generative AI integration in software engineering <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. They also contribute to the [[ai_native_companies | AI native]] dev community by curating content <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Four Patterns of AI Native Development

### 1. From Producer to Manager
Traditionally, developers produce code. With AI agents producing code, the developer's role shifts to managing these agents <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

*   **Shift in Workload**
    *   Less time spent coding <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   Increased time and cognitive load in reviewing AI-generated code <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. The "thinking work" now occurs during the review phase <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Reducing Cognitive Load in Review**
    *   New review methods are emerging beyond clunky diff views or verbose chat views <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   **Summarized Reviews:** Reviews can be stripped down to what matters, allowing for quick "yes/no" decisions <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   **Step-by-Step Review:** For multiple files, breaking down the review into a structured flow helps manage complexity <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   **Visual Reviews:** Reviewing changes through diagrams rather than just text makes it easier to spot errors and impacts <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   **Moldable Development Environments:** Future IDEs are expected to adapt to specific code review needs and domains, moving away from endless text streams <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Automating Commits and Agent Management**
    *   **Auto-Commit:** The concept of auto-committing AI-generated code, with developers reviewing only if they don't like it, shifts the responsibility <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This relies on heuristics to accept low-risk or low-impact changes <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   **Checkpoints for Longer-Running Agents:** For extended agent operations, checkpoints allow developers to jump in at specific points and regenerate code, avoiding full re-reviews of the entire thought process <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   **Setting Constraints:** Developers, acting as managers, can set rules for AI, such as locking files or defining permissions for agents, establishing guardrails for their actions <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   **Cost Monitoring:** As agents run for longer durations, monitoring the cost of their operations becomes important <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### 2. From Implementation to Intent
The focus shifts from directly implementing code to specifying the desired outcome or intent to AI agents <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

*   **Specification-Driven Development**
    *   **Simple Markdown Specifications:** Early forms involved adding markdown files as simplified specification files to prompts, reducing repetitive re-writing in prompts <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. This helps build shared functional or technical specifications <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   **AI-Generated Plans:** AI can assist in building step-by-step plans from desired outcomes, moving towards intent-based coding rather than just chat or text completion <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   **Specification-Centric Workflows:** Entire workflows can become specification-centric, where functional, technical, and security requirements are paramount, and the underlying code is less visible <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
    *   **Program Manager Role:** Developers increasingly manage the process of defining intent, akin to a program manager <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

### 3. From Delivery to Discovery
With robust pipelines handling delivery, the emphasis shifts to discovering new ideas and problems to solve <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

*   **Accelerated Prototyping and Design**
    *   AI enables faster design and creation of prototypes, allowing for quicker exploration of "how it needs to be" <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
    *   **Multiple Iterations:** AI can generate multiple versions or iterations of a design, allowing developers to choose the best one and suggesting ideas they might not have considered <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    *   **Design-to-Code Loop:** The iterative process of designing, coding, redesigning, and modifying code is refined to facilitate discovery and exploration <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
    *   **Customer Involvement:** The concept of "vibe coding" (rapid prototyping) can extend to customers, allowing them to design their desired interfaces on top of a product, similar to A/B testing on steroids <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This addresses friction points in achieving the "perfect product" <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### 4. From Data to Knowledge
Whatever is learned throughout the development process, including content produced, is transformed into reusable knowledge <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

*   **Capturing and Leveraging Knowledge**
    *   **Learning from Production Issues:** Insights gained from production issues can be fed back into code and development practices <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
    *   **Incident Response:** Lessons from incidents, such as what failed or new guidelines, can be codified as knowledge <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
    *   **Onboarding and Retention:** Turning code into lessons reduces onboarding time for new team members and helps retain knowledge when someone leaves <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
    *   **Feature Memory:** AI can track the history of features, including discarded attempts, creating a "feature memory" to prevent re-doing work and track decisions that are often lost in tickets or diagrams <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
    *   **In-Flow Knowledge Capture:** As developers chat and code, agents can proactively suggest saving important information as knowledge, creating a beneficial loop for both human and AI learning <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    *   **Knowledge Application:** This captured knowledge can then be used to answer questions and improve the coding of solutions <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

## Summary of Patterns and Roles
The four patterns of [[ai_native_companies | AI native]] development represent a shift in the developer's role <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>:

*   **From Producer to Manager:** Moving towards operations, overseeing AI-generated code.
*   **From Implementation to Intent:** Shifting towards QA and architecture, defining what needs to be built.
*   **From Delivery to Discovery:** Embracing a product owner mindset, exploring and finding new ideas.
*   **From Data to Knowledge:** Acting more like a data engineer, capturing and leveraging insights.

These shifts highlight that AI's impact extends far beyond merely helping with faster typing <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>; it enables developers to perform tasks traditionally associated with senior roles <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

## Resources
To explore the landscape of [[tool_usage_and_development_in_ai_frameworks | AI native development tools]], you can visit ainativedev.io, which curates over 300 tools <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. A newsletter also focuses on the intersection of coding, software engineering, and AI <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.