---
title: DORA and SPACE frameworks for measuring productivity
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Nicole Forsgren, a leading expert in [[developer_productivity_improvement | developer productivity]], emphasizes the foundational challenge in improving engineering teams: defining the problem or goal clearly <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. She notes that eighty percent of people she works with, even at executive levels, struggle with this, leading to uncertainty after months of effort <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Unclear objectives, such as "improve [[developer_productivity_improvement | developer experience]]" without specifics (e.g., inner/outer loop, friction, culture), can lead teams in disparate directions <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Forsgren's work helps organizations [[measuring_and_improving_engineering_productivity | measure and improve their engineering team's productivity and experience]] <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

## DORA Framework

DORA (DevOps Research and Assessment) is a research program primarily known for its "Four Keys" or "Four Metrics" that measure software delivery performance <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. These metrics include two focused on speed and two on stability <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

### The Four Metrics
*   **Lead Time**: How long it takes to get code from committed to running in production <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **Deployment Frequency**: How often code is deployed <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
*   **Mean Time to Restore (MTTR)**: How long it takes to recover from an incident <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.
*   **Change Fail Rate**: The percentage of changes that result in incidents or require human intervention <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

A significant finding from DORA research is that speed and stability move in tandem <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>, meaning that moving faster typically leads to greater stability <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. This is because faster deployment encourages smaller, more frequent changes, which in turn reduces the "blast radius" of errors and makes debugging easier <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. Conversely, infrequent deployments result in large batch changes, leading to more unstable systems and more complex debugging when issues arise <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

### Elite Performance Benchmarks (2019)
*   **Deployment Frequency**: On demand <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.
*   **Lead Time for Changes**: Less than a day <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **Time to Restore Service**: Less than an hour <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.
*   **Change Fail Rate**: Between zero and fifteen percent <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.

While benchmarks are interesting, Forsgren emphasizes that knowing your current state and making progress is more important than achieving an "elite" status <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. The DORA metrics are universally applicable, showing no statistical significance between small and large companies, except for retail, which tends to perform better due to market pressures <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

DORA is not just about metrics but also about a set of capabilities—technical (e.g., automated testing, CI/CD, trunk-based development, version control), architectural (e.g., loosely coupled systems, cloud utilization), and cultural—that predict speed and stability, which then drive business outcomes <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. The `dora.dev` website provides a quick check tool where users can input their current state and identify potential constraints based on industry benchmarks <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

## SPACE Framework

SPACE is a framework designed to measure complex, creative work, including [[developer_productivity_improvement | developer productivity]] <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. It helps organizations select appropriate metrics within their context and available data <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### The Five Dimensions of SPACE
*   **S - Satisfaction and Well-being**: Measures developer satisfaction, sustainability, and burnout <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. This dimension is highly correlated with other productivity aspects and acts as a strong signal for impending issues <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   **P - Performance**: Focuses on the outcomes of a process, such as system reliability (e.g., DORA's MTTR or change fail rate) <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   **A - Activity**: Relates to counts or numbers of discrete actions (e.g., number of pull requests, check-ins, commits) <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>. These are often easy to instrument <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.
*   **C - Communication and Collaboration**: Encompasses how people work and communicate (e.g., meetings, searchability of codebases, system communication) <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
*   **E - Efficiency and Flow**: Measures the flow through a system or the time taken (e.g., time through a deployment pipeline, number of hops for a ticket) <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

To use SPACE effectively, it's recommended to measure using at least three dimensions simultaneously to ensure balance and prevent unintended consequences <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>. For example, focusing only on "activity" metrics like lines of code or number of commits can be misleading <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. DORA's four metrics can be seen as an implementation of the SPACE framework, primarily covering the "outer loop" aspects of development <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

Data for SPACE can be collected through surveys for subjective measures like satisfaction (periodically) and system instrumentation for quantitative measures like activity or efficiency <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. It's crucial to combine "data from people" and "data from systems" because each provides unique insights; for instance, system data might show fast lead times, but surveys might reveal that it takes "heroics" from developers to achieve that speed <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

## Practical Application and Pitfalls

When implementing a [[developer_productivity_improvement | developer productivity]] system, common pitfalls include:
*   **Lack of Clarity**: Not clearly defining what problem needs to be solved or what goal is being pursued <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.
*   **Unbalanced Approach**: Failing to pursue improvements with both top-down and bottom-up engagement <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. Effective communication with both individual contributors (ICs) and leadership is crucial to drive success <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

The rise of AI has further emphasized the need for better [[developer_productivity_improvement | engineering productivity]] <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. AI-enabled [[tools_and_technologies_for_enhancing_productivity | tools and technologies for enhancing productivity]], like GitHub Copilot, change developer workflows, shifting time from writing code to reviewing it <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. This shift highlights a need to potentially add new dimensions to frameworks like SPACE, such as "trust" or "reliability," as developers learn to rely on AI tools <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>. Forsgren cautions against oversimplifying productivity to just "doing tasks faster," emphasizing that AI should free up cognitive space for engineers to tackle harder problems <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>.

### The Four-Box Framework
Forsgren also uses a "four-box framework" to help clarify hypotheses and measurement strategies <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>:
1.  **Top Left (Words)**: State your initial hypothesis in words (e.g., "Customer satisfaction gets us more money") <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
2.  **Top Right (Words)**: State the expected outcome in words (e.g., "Return customers") <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
3.  **Bottom Left (Data)**: Define how you will measure the first concept (e.g., "Customer satisfaction" via a CSAT score or NPS) <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
4.  **Bottom Right (Data)**: Define how you will measure the outcome (e.g., "Return customers" via website analytics or referral links) <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.

This framework ensures clarity before data analysis, allowing teams to identify issues with data quality or the hypothesis itself, rather than blaming individuals <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.

## Resources and Recommendations

For further learning, Nicole Forsgren recommends:
*   Her book, "Accelerate," which compiles and expands upon the first four years of DORA research <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   The `dora.dev` website for updated reports and the quick check tool <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   The SPACE paper (available at ACM) for its detailed framework and metric examples <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   A paper co-authored with Mick Kirsten on the complementary nature of data from people and systems <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   The book "How to Measure Anything" by Douglas Hubbard, particularly for uncovering intangibles when no data is initially available <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

For organizations looking to improve [[developer_productivity_improvement | developer experience]] and [[developer_productivity_improvement | productivity]], a crucial first step is to ensure that the problem or goal is clearly defined and written down <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. Then, identify any existing data or signals related to that problem <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. If no formal data exists, start by talking to developers about their feelings regarding work tools, processes, and barriers to productivity <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.