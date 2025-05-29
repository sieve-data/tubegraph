---
title: Space framework for measuring complex creative work
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 
The [[Space framework for measuring complex creative work]] is a method for measuring complex creative work, such as [[developer_productivity_measurement | developer productivity]] <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a> <a class="yt-timestamp" data-t="29:35:00">[29:35:00]</a>. It provides a framework for choosing appropriate metrics for complex work <a class="yt-timestamp" data-t="30:06:00">[30:06:00]</a>.

It was developed to help individuals and organizations choose the right metrics when trying to measure or improve something <a class="yt-timestamp" data-t="33:09:00">[33:09:00]</a>. This framework was created after observing that people often struggled with selecting appropriate metrics, frequently choosing only activity metrics like lines of code or number of commits, which are insufficient for a holistic view <a class="yt-timestamp" data-t="33:52:00">[33:52:00]</a>.

## The Five Dimensions of SPACE
The SPACE framework is named after its five dimensions, each representing an aspect to measure <a class="yt-timestamp" data-t="30:45:00">[30:45:00]</a>:

*   **S: Satisfaction and Well-being** <a class="yt-timestamp" data-t="30:52:00">[30:52:00]</a>
    *   This dimension focuses on how people feel about their work and environment <a class="yt-timestamp" data-t="30:53:00">[30:53:00]</a>.
    *   It is highly correlated with other dimensions of [[measuring_engineering_productivity | productivity]] and indicates sustainability and reductions in burnout when managed correctly <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a> <a class="yt-timestamp" data-t="31:02:00">[31:02:00]</a>.
    *   A decline in satisfaction and well-being can signal that other aspects are starting to break <a class="yt-timestamp" data-t="31:16:00">[31:16:00]</a>.
    *   Measurement typically involves asking people through surveys <a class="yt-timestamp" data-t="35:43:00">[35:43:00]</a> <a class="yt-timestamp" data-t="39:49:00">[39:49:00]</a>.

*   **P: Performance** <a class="yt-timestamp" data-t="31:22:00">[31:22:00]</a>
    *   Measures the outcome of a process <a class="yt-timestamp" data-t="31:24:00">[31:24:00]</a>.
    *   Examples include reliability, or metrics like mean time to restore (MTTR) and change fail rate, which are also part of the [[Dora framework and metrics for software delivery]] <a class="yt-timestamp" data-t="31:26:00">[31:26:00]</a>.

*   **A: Activity** <a class="yt-timestamp" data-t="31:39:00">[31:39:00]</a>
    *   Refers to counts or numbers of something, easily instrumented and automated <a class="yt-timestamp" data-t="31:40:00">[31:40:00]</a>.
    *   Examples include the number of pull requests or check-ins <a class="yt-timestamp" data-t="31:46:00">[31:46:00]</a>.
    *   However, relying solely on activity metrics like lines of code or number of commits is a common pitfall <a class="yt-timestamp" data-t="33:54:00">[33:54:00]</a>.

*   **C: Communication and Collaboration** <a class="yt-timestamp" data-t="31:53:00">[31:53:00]</a>
    *   Encompasses how people work and talk together, including meetings or the searchability of a code base <a class="yt-timestamp" data-t="31:55:00">[31:55:00]</a>.
    *   It can also apply to how systems communicate with each other <a class="yt-timestamp" data-t="32:01:00">[32:01:00]</a>.

*   **E: Efficiency and Flow** <a class="yt-timestamp" data-t="32:07:00">[32:07:00]</a>
    *   Measures the flow of work through a system, such as time taken for a process <a class="yt-timestamp" data-t="32:09:00">[32:09:00]</a>.
    *   Examples include the number of hops a ticket takes to reach the right person <a class="yt-timestamp" data-t="32:15:00">[32:15:00]</a>.

### How to Use SPACE
To use the SPACE framework effectively, it is recommended to use at least three dimensions at a time <a class="yt-timestamp" data-t="32:23:00">[32:23:00]</a>. This helps to achieve balance and ensures that unintended negative consequences are avoided, preventing the system from being thrown out of whack <a class="yt-timestamp" data-t="32:27:00">[32:27:00]</a> <a class="yt-timestamp" data-t="34:16:00">[34:16:00]</a>.

For example, when attempting to improve pull requests, merely increasing alerts (an activity metric) could lead to alert fatigue <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>. By adding dimensions like efficiency and flow (e.g., time to work on coding) and satisfaction (e.g., satisfaction with the pull request process), a more balanced approach is achieved that protects developers' time while also improving the process <a class="yt-timestamp" data-t="35:05:00">[35:05:00]</a>.

## Relationship with Dora
The [[Dora framework and metrics for software delivery]] (Deployment Frequency, Lead Time for Changes, Time to Restore Service, and Change Fail Rate) is an implementation of the SPACE framework <a class="yt-timestamp" data-t="32:29:00">[32:29:00]</a>. While Dora provides specific metrics, SPACE offers a broader framework for thinking about and selecting any complex measurement <a class="yt-timestamp" data-t="33:00:00">[33:00:00]</a>.

## Resources
For further information on the SPACE framework, you can refer to the SPACE paper at ACM <a class="yt-timestamp" data-t="38:31:00">[38:31:00]</a>. The paper outlines the framework and provides examples of metrics for each category <a class="yt-timestamp" data-t="38:45:00">[38:45:00]</a>. Additionally, Nicole Forsgren's book "Accelerate" compiles and expands on the research, including the underlying capabilities that predict speed and stability <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a>. The website dora.dev also provides a quick check tool for benchmarking performance and identifying potential constraints <a class="yt-timestamp" data-t="28:02:00">[28:02:00]</a>.