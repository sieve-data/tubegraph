---
title: Developer productivity measurement
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Understanding and improving [[measuring_engineering_productivity | developer productivity]] is a critical challenge for many organizations, often underestimated by those at executive levels <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Eighty percent of teams struggle with clearly defining their goals, which can lead to months of misdirected effort <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. For example, a vague goal like "improve [[improving_developer_experience | developer experience]]" needs clarification, as it could refer to inner/outer loop processes, toolchain friction, or even culture, each requiring vastly different approaches <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Expert Insight: Nicole Forsgren's Journey

Nicole Forsgren is a leading expert in [[measuring_engineering_productivity | developer productivity]], known for co-authoring the award-winning book *Accelerate* and contributing to the *State of DevOps Report* <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Her career journey began as a software engineer at IBM, where she encountered inefficiencies that inspired her to pursue a PhD in management information systems <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Her academic path focused on using data to demonstrate the link between software development and delivery methods, and outcomes at individual, team, and organizational levels, including ROI and efficiency <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

After academia, she transitioned to industry roles, including leading [[dora_framework_and_metrics_for_software_delivery | Dora]] (DevOps Research and Assessment) which was later acquired by Google <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Currently, she is a partner at Microsoft Research, leading the Developer Experience Lab which focuses on productivity, community, and well-being <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. She also contributes to Microsoft's efforts to improve developer infrastructure <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

### Defining Key Terms
*   **Productivity**: How much can be accomplished over time, emphasizing a holistic measure that includes community effects (software as a team sport) and well-being to ensure sustainability and reduce burnout <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **[[improving_developer_experience | Developer Experience]] (DevEx)**: The ease and predictability of writing software, aiming to reduce friction and uncertainty to contribute to productivity <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Developers are considered users in this context <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **DevOps**: A set of capabilities, tools, processes, and architectural/cultural practices that enable faster and more reliable end-to-end software development and delivery <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. DevOps is not merely a toolchain <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

## The Business Case for Faster Development

While most leaders want their engineering teams to move faster and be more productive, there's often hesitation regarding the investment required or fear of impacting quality and stability <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Historically, practices like two-week change approval waits were believed to ensure stability, but research has shown this to be incorrect <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

The [[dora_framework_and_metrics_for_software_delivery | Dora]] and DevOps research programs demonstrate that implementing good technical and architectural practices (e.g., automated testing, microservices, cloud adoption) allows teams to move faster *and* be more stable <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. This happens by pushing smaller changes more often, which reduces the "blast radius" of errors and makes debugging easier <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. Conversely, infrequent, large batch changes lead to more unstable systems <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

This means: **to move faster and improve quality, ship smaller things more often** <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

## Measuring Success: The [[dora_framework_and_metrics_for_software_delivery | Dora Framework]]

The [[dora_framework_and_metrics_for_software_delivery | Dora framework]] is an extensive research program best known for its "Four Keys" or "Four Metrics" for software delivery performance <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>:

*   **Speed Metrics**:
    *   **Lead Time for Changes**: How long it takes to get code from committed to running in production <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   **Deployment Frequency**: How often code is deployed to production <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   **Stability Metrics**:
    *   **Mean Time to Restore (MTTR)**: How long it takes to restore service if something breaks <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
    *   **Change Fail Rate**: The percentage of changes that result in incidents requiring human intervention <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

These metrics move in tandem; improving speed also improves stability because it encourages smaller, more frequent changes <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. The *State of DevOps Report* publishes benchmarks for low, medium, high, and Elite performers <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

### Elite Performance Benchmarks (2019, generally consistent):
*   **Deployment Frequency**: On demand <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Lead Time for Changes**: Less than one day <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Time to Restore Service**: Less than one hour <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
*   **Change Fail Rate**: Between 0-15% <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

These benchmarks are applicable across companies of all sizes, with no significant statistical difference between small and large companies, except for retail, which tends to perform better due to market pressures <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. What matters most is understanding your current state and making progress, not just hitting an external benchmark <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

To improve these metrics, focus on implementing technical capabilities (e.g., automated testing, CI/CD, trunk-based development, version control), architectural capabilities (e.g., loosely coupled systems, effective cloud usage), and a strong culture <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>. The [dora.dev](https://dora.dev) website offers a "quick check" tool to help identify potential constraints based on your performance profile and industry <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.

## The [[space_framework_for_measuring_complex_creative_work | SPACE Framework]]

The [[space_framework_for_measuring_complex_creative_work | SPACE framework]] is designed to help organizations measure any type of complex creative work, including [[measuring_engineering_productivity | developer productivity]] <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>. It provides a framework to select the right metrics within your specific context and available data <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>. [[dora_framework_and_metrics_for_software_delivery | Dora]] is considered an implementation of [[space_framework_for_measuring_complex_creative_work | SPACE]], focusing on the "outer loop" of development <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

**SPACE** stands for five dimensions you want to measure:
*   **S - Satisfaction and Wellbeing**: How satisfied and healthy are developers? This is highly correlated with other productivity dimensions and acts as an important signal, as declining satisfaction often precedes other problems <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. Measured via surveys periodically <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.
*   **P - Performance**: The outcome of a process, such as reliability, or Dora's MTTR and Change Fail Rate <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **A - Activity**: Counts or numbers of something, easily instrumented and automated (e.g., number of pull requests, check-ins) <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. Avoid relying solely on activity metrics like lines of code <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.
*   **C - Communication and Collaboration**: How people work and talk together (e.g., meetings, system communication, code searchability) <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.
*   **E - Efficiency and Flow**: The flow and time through the system (e.g., time through deployment, number of hops for a ticket) <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

To use [[space_framework_for_measuring_complex_creative_work | SPACE]] effectively, measure at least three dimensions at a time to ensure balance and prevent unintended consequences <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. Qualitative insights (from people, e.g., surveys) and quantitative insights (from systems) are crucial complements <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. Systems alone cannot reveal "heroics" or code not in version control <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a>. Even advanced teams survey their developers at least once a year <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>.

## Common Pitfalls in [[measuring_engineering_productivity | Measurement]] and Improvement

*   **Lack of Clarity**: Not having a clear understanding of the problem or goal <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>.
*   **Unbalanced Approach**: Not pursuing improvements with both top-down and bottom-up engagement <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>. It's essential to get buy-in from individual contributors (ICs) and understand leaders' motivations <a class="yt-timestamp" data-t="00:46:29">[00:46:29]</a>.
*   **Discounting Qualitative Data**: Dismissing developer feedback from surveys because of perceived "lying" or "bad data" <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>. Like system data, human data can have issues, but it provides unique insights <a class="yt-timestamp" data-t="00:36:39">[00:36:39]</a>.

## Evolution of the Field

Over the past decade, the landscape of [[measuring_engineering_productivity | developer productivity]] has changed significantly <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>:
*   **Larger, More Complex Systems**: Almost every company now operates with extensive, intricate systems <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>.
*   **Developer Shortage**: A reported or perceived shortage of developers <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>.
*   **Technology-Driven Companies**: Most companies now understand they are technology-driven, unlike a decade ago where even CTOs might deny being a "tech company" <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>.
*   **[[impact_of_ai_on_developer_productivity | Impact of AI]]**: The rise of AI tools like GitHub Copilot has intensified the focus on developer productivity. It emphasizes that productivity is not just about doing tasks faster, but about freeing up cognitive space for harder, more novel work <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. AI changes the mental model of work, shifting focus from writing code to reviewing it, and introduces new considerations like trust, reliance, and learning <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.

## Tactical Advice for Improvement

### Starting Your Journey
1.  **Define Your Problem/Goal**: Ensure it's clear and written down to avoid confusion <a class="yt-timestamp" data-t="00:54:38">[00:54:38]</a>.
2.  **Seek Data/Signals**: Identify any existing data related to the problem, even if loosely defined <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.
3.  **Engage Developers**: If no data exists, ask a handful of developers how they feel about their tools and processes, and what their biggest productivity barriers are <a class="yt-timestamp" data-t="00:55:29">[00:55:29]</a>.

### The Four Box Framework (for hypothesis testing)
This framework helps clarify what you want to measure and how.
1.  **Draw Four Boxes**: Two on top, two on the bottom, aligned <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.
2.  **Label Sides**: "Words" to the left of the top boxes, "Data" to the left of the bottom boxes <a class="yt-timestamp" data-t="00:58:26">[00:58:26]</a>.
3.  **Define Hypothesis (Words)**: In the top boxes, write your hypothesis. For example, "Customer Satisfaction" -> "Return Customers" <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>. Always start with words, then validate this with stakeholders <a class="yt-timestamp" data-t="00:59:18">[00:59:18]</a>.
4.  **Identify Metrics (Data)**: In the bottom boxes, list the specific data points that will measure the concepts defined in the "words" boxes (e.g., "Customer Satisfaction" -> "CSAT Score, NPS"; "Return Customers" -> "Website returns, referral links") <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>.
5.  **Analyze**: Run correlations or other analyses. If results are unexpected, examine the data quality or the initial hypothesis. This prevents blaming individuals for flawed assumptions or data <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.

### Decision-Making
*   **Define Criteria**: Clearly outline what's important for a decision (e.g., for a job: total compensation, prestige, team, work-life balance) <a class="yt-timestamp" data-t="01:04:42">[01:04:42]</a>.
*   **Weight Criteria**: Assign relative importance to each criterion, adding up to 100% <a class="yt-timestamp" data-t="01:06:37">[01:06:37]</a>.
*   **Score Options**: Give each option a score against each criterion, then multiply by the weight <a class="yt-timestamp" data-t="01:06:49">[01:06:49]</a>.
*   **Be Data-Informed**: Use the numerical results as a guide, but allow for intuition and strategic choices, especially when prioritizing <a class="yt-timestamp" data-t="01:07:14">[01:07:14]</a>. The key to good [[Building Effective Product Teams | strategy]] is knowing what *not* to do, and the key to executing it is actually *not* doing those things <a class="yt-timestamp" data-t="01:07:35">[01:07:35]</a>.

## Recommended Resources
*   **Books**:
    *   *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a>.
    *   *How to Measure Anything* by Douglas W. Hubbard <a class="yt-timestamp" data-t="00:40:03">[00:40:03]</a>.
    *   *Good Strategy Bad Strategy* by Richard Rumelt <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>.
    *   *Designing Your Life* by Bill Burnett and Dave Evans <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>.
    *   *Ender's Game* by Orson Scott Card <a class="yt-timestamp" data-t="01:09:21">[01:09:21]</a>.
*   **Papers**:
    *   The [[space_framework_for_measuring_complex_creative_work | SPACE Framework]] paper (available at ACM) <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.
    *   Paper with Mick Kirsten on using data from people and systems in DevOps context <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.
*   **Websites**:
    *   [dora.dev](https://dora.dev) for reports, quick checks, and deep dives into capabilities <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
*   **Tools**:
    *   DX (getdx.com/lenny) is a platform for [[measuring_engineering_productivity | measuring developer productivity]] designed by researchers behind Dora and SPACE <a class="yt-timestamp" data-t="01:53">[01:53]</a>.
*   **Upcoming Book**: Nicole Forsgren is working on a new book on [[measuring_engineering_productivity | measuring]] and improving developer productivity, covering defining problems, starting measurement from nothing, the measurement journey (subjective vs. objective data), and providing practical examples <a class="yt-timestamp" data-t="00:41:37">[00:41:37]</a>.