---
title: Importance of Speed and Stability in Software Development
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Achieving speed and stability in software development is a universal goal for leaders and founders, who consistently express the desire to "move faster," improve engineer productivity, and "get things out the door quicker" <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. Despite this, many are hesitant, questioning the business case, ROI, or fearing that increased speed might lead to instability or a loss of reliability <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>. This concern often stems from outdated beliefs, such as the common knowledge that a two-week wait for change approvals was necessary for stability <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>. However, research indicates this is "not right" <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.

Instead, [[balancing_speed_and_quality_in_product_development | moving faster turns out to be one of the best ways to improve quality and stability]] <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. The core message is to ship smaller things more often, as this approach is "much much safer" <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a> and actually leads to higher quality <a class="yt-timestamp" data-t="18:36:00">[18:36:00]</a>.

## The DORA Framework: Measuring Speed and Stability

The DevOps Research and Assessment (DORA) framework is a research program that provides key metrics for software delivery performance <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>. It measures two aspects of speed and two of stability <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>:

*   **Speed Metrics:**
    *   **Lead Time for Changes:** The time it takes from code being committed to running in production <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.
    *   **Deployment Frequency:** How often code is deployed <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>.
*   **Stability Metrics:**
    *   **Mean Time to Restore (MTTR):** How long it takes to recover if something goes wrong <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a>.
    *   **Change Fail Rate:** The percentage of changes pushed that require human intervention or result in incidents <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.

### The Tandem Movement of Speed and Stability

A significant finding from DORA research is that speed and stability move in tandem <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a> with "very strong significance" <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>. This means:

*   **Moving Faster = More Stable:** When teams move faster, they push smaller changes more often. This results in a smaller "blast radius" for any errors, making them "easier to debug" <a class="yt-timestamp" data-t="15:30:00">[15:30:00]</a> and significantly reducing the mean time to restore and mitigate issues <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>.
*   **Moving Slower = Less Stable:** Conversely, pushing changes less frequently leads to larger batch changes, which have a "very high very large blast radius" <a class="yt-timestamp" data-t="15:58:00">[15:58:00]</a>. When a bug occurs, it becomes much harder to "disentangle this big... ball of mud" <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a> and identify the root cause <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>. Forcing long approval pauses, like the old two-week waiting period, causes this batching up of changes, leading to merge conflicts and integration challenges <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>.

### Elite Performer Benchmarks

While the primary focus should be on knowing your current state and making progress, DORA provides benchmarks for Elite Performers (based on 2019 data, though generally consistent) <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a> <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>:

*   **Deployment Frequency:** On demand <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>.
*   **Lead Time for Changes:** Less than a day <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>.
*   **Time to Restore:** Less than an hour <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>.
*   **Change Fail Rate:** Between 0% and 15% <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>.

These benchmarks apply broadly, as research shows "no statistical significance between small companies and large companies" regarding these metrics, with the notable exception of retail companies performing better due to market pressures <a class="yt-timestamp" data-t="22:58:00">[22:58:00]</a>.

## Achieving Speed and Stability through Capabilities

DevOps is not a toolchain to buy; it is a "set of capabilities" that predict speed and stability <a class="yt-timestamp" data-t="26:24:00">[26:24:00]</a>. These capabilities include:

*   **Technical Capabilities:**
    *   Automated testing <a class="yt-timestamp" data-t="27:01:00">[27:01:00]</a>
    *   CI/CD (Continuous Integration, Continuous Deployment) <a class="yt-timestamp" data-t="27:02:00">[27:02:00]</a>
    *   Trunk-based development <a class="yt-timestamp" data-t="27:10:00">[27:10:00]</a>
    *   Using a Version Control System <a class="yt-timestamp" data-t="27:13:00">[27:13:00]</a>
*   **Architectural Practices:**
    *   Loosely coupled systems <a class="yt-timestamp" data-t="27:23:00">[27:23:00]</a>
    *   Effective cloud utilization (or underlying architectural pieces if not in the cloud) <a class="yt-timestamp" data-t="27:26:00">[27:26:00]</a>
*   **Cultural Capabilities:** Promoting a positive culture that supports these practices <a class="yt-timestamp" data-t="27:44:00">[27:44:00]</a>.

A quick check tool is available on dora.dev to plug in your current metrics and receive insights into potential constraints based on your performance profile and industry <a class="yt-timestamp" data-t="28:07:00">[28:07:00]</a>.

## The Role of [[improving_developer_experience | Developer Experience]] (DX)

[[improving_developer_experience | Developer experience]] (DX) is "very related" and "very tied" to productivity, contributing significantly to it <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. It considers developers as users within the software development process, focusing on "what it is like to write software" <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>. A good DX aims for a "friction free process" and a "predictable and certain experience" <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>, which in turn reduces uncertainty and increases predictability, ultimately contributing to productivity <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.

For example, a fast feedback loop in deployment pipelines directly impacts DX. If a bug occurs "less than a day" after a commit, a developer can fix it while the code's mental model is still fresh <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>. However, if a bug surfaces three months later, the developer has to re-familiarize themselves with old code, leading to significant interruption and cognitive load <a class="yt-timestamp" data-t="22:06:00">[22:06:00]</a>.

## The Impact of [[ais_impact_on_skills_and_product_development | AI]] on Speed and Stability

The current "AI moment" has "poured gas on top of everything" <a class="yt-timestamp" data-t="49:03:00">[49:03:00]</a>, intensifying the focus on execution. It's no longer just about *what* is built, but about "creating absolutely novel incredibly new experiences and doing them at a speed that no one has seen before" <a class="yt-timestamp" data-t="49:25:00">[49:25:00]</a>. The only way to achieve this is through a software pipeline that is "fast and is safe and is stable and is reliable" <a class="yt-timestamp" data-t="49:38:00">[49:38:00]</a>.

[[ais_impact_on_skills_and_product_development | AI-enabled tools]] like GitHub Copilot are already showing impact, with some engineers reporting being "100% more effective and efficient" <a class="yt-timestamp" data-t="50:34:00">[50:34:00]</a>. These tools fundamentally shift workflows, leading to more time spent reviewing code than writing it <a class="yt-timestamp" data-t="51:55:00">[51:55:00]</a>. While AI can accelerate certain tasks, the true benefit lies in freeing up cognitive space for developers to tackle harder, more complex problems <a class="yt-timestamp" data-t="52:50:00">[52:50:00]</a>. This shift also introduces new considerations, such as the need to measure trust and reliance on AI tools <a class="yt-timestamp" data-t="51:29:00">[51:29:00]</a>.

## Getting Started with Improving Speed and Stability

For any company looking to improve developer productivity and experience:

1.  **Define the Problem/Goal:** Be "super super crisp" on "what is your problem or what is your goal" <a class="yt-timestamp" data-t="41:53:00">[41:53:00]</a>. This is often the biggest challenge, even at executive levels, where uncertainty about the exact meaning of "improve developer experience" can lead teams in different directions <a class="yt-timestamp" data-t="42:24:00">[42:24:00]</a>.
2.  **Seek Alignment:** Ensure there's a clear, written-down challenge and understanding of the specific area to improve, whether it's friction in toolchains or culture <a class="yt-timestamp" data-t="42:48:00">[42:48:00]</a>.
3.  **Find Data/Signal:** Look for any existing data or signals related to the problem, even if "loosely defined" <a class="yt-timestamp" data-t="54:53:00">[54:53:00]</a>.
4.  **Engage Developers:** If no data exists, talk to developers and ask them directly about their work tools, processes, and the biggest barriers to their productivity <a class="yt-timestamp" data-t="54:55:00">[54:55:00]</a>. These qualitative insights are crucial complements to system data <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>.

By combining clear objectives with both quantitative and qualitative data, companies can strategically invest in capabilities that lead to faster, more stable, and more reliable software delivery.