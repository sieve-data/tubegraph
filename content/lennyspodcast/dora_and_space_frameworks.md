---
title: Dora and Space Frameworks
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Nicole Forsgren, a recognized expert in developer productivity, emphasizes the significant challenge many organizations face in clearly defining and measuring their goals for improvement. She notes that eighty percent of the teams she works with, including those at executive levels, struggle with this fundamental problem. Teams might spend months tackling something like "improving developer experience" only to return with uncertainty because the initial goal was not specific enough. Clarifying whether "developer experience" refers to inner/outer loop friction, tool chains, or culture is crucial, as misinterpretations can lead teams in "completely different directions" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Measuring and Improving Engineering Productivity

Forsgren, a partner at Microsoft Research leading developer productivity research and strategy, has helped major companies accelerate, enhance product quality, and transform their cultures <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Her work centers on measuring and improving engineering team productivity and experience, utilizing frameworks like DORA and SPACE <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Defining Key Terms

Forsgren clarifies the relationship between developer productivity, developer experience, and DevOps:
*   **Productivity** refers to "how much we can get done and how much we can do over time" <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It requires a holistic measure, considering community effects (as "software is a team sport" <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>) and well-being, which helps reduce burnout <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Developer Experience** (DevEx) contributes significantly to productivity by focusing on the ease of writing software. It aims for a "friction-free process" and increased predictability <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **DevOps** refers to the "capabilities and tools and processes that we can use to improve our software development and delivery end to end so that it's faster and it is more reliable" <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. It encompasses technical, architectural, and cultural practices <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

Forsgren notes that while leaders universally desire faster, more productive, and happier engineers <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, concerns often arise about the return on investment (ROI) or the risk of instability when moving too fast <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Historically, practices like a two-week wait for change approvals were believed to ensure stability, but research has shown this to be incorrect <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

Instead of sacrificing stability for speed, the goal is to implement sound technical practices (like automated testing and CI/CD) and architectural practices (like loosely coupled systems and effective cloud utilization) that enable both speed and stability <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

### The DORA Framework (The Four Keys)

The DORA (DevOps Research and Assessment) research program, primarily known for its "Four Keys" or "four metrics," measures software delivery performance <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>:

*   **Speed Metrics**:
    *   **Lead Time for Changes**: The time it takes from code committed to code running in production <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   **Deployment Frequency**: How often code is deployed <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   **Stability Metrics**:
    *   **Meantime to Restore (MTTR)**: How long it takes to recover from an incident <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
    *   **Change Fail Rate**: The percentage of changes that result in incidents requiring human intervention <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

A key finding of DORA research is that **speed and stability move in tandem** <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Moving faster, by pushing "smaller changes more often," leads to more stable systems because it results in a "smaller blast radius" and easier debugging when errors occur <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. Conversely, pushing changes less frequently leads to larger batch changes, higher blast radii, and more unstable systems that are harder to debug <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

#### Elite Performance Benchmarks (2019 data, generally consistent) <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>:
*   **Deployment Frequency**: On demand <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Lead Time for Changes**: Less than one day <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
*   **Time to Restore Service**: Less than one hour <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
*   **Change Fail Rate**: Between 0% and 15% <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

Forsgren stresses that knowing where you are and making progress is more important than merely comparing to elite benchmarks <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. There is no statistical difference in DORA performance between small and large companies, except for retail, which tends to perform better due to market pressures leading to "natural selection" of high performers <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.

To improve these metrics, organizations should focus on [[building_a_culture_and_platform_for_experimentation | cultural]], architectural, and technical capabilities, such as:
*   Automated testing <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>
*   Continuous Integration and Continuous Deployment (CI/CD) <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>
*   Trunk-based development <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>
*   Using a Version Control System <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>
*   Loosely coupled systems <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>
*   Effective cloud utilization <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>
*   A healthy culture <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>

A "quick check" tool is available at `dora.dev` to help organizations understand their performance profile and identify likely constraints based on industry benchmarks <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>. Forsgren's book, "Accelerate," compiles and expands on the initial DORA research <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.

### The SPACE Framework

The SPACE framework provides a structured approach for selecting metrics to measure complex, creative work like developer productivity or incident management <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>. It offers a "framework to pick the right metrics" rather than prescribing exact ones <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.

SPACE is an acronym for five dimensions:
*   **S - Satisfaction and Well-being**: Measures aspects like job satisfaction and burnout. This dimension is highly correlated with other productivity aspects and serves as an important signal for potential issues <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>.
*   **P - Performance**: Focuses on the outcomes of processes, such as reliability, or DORA metrics like MTTR and Change Fail Rate <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **A - Activity**: Counts of actions or outputs that are easy to instrument, e.g., number of pull requests or check-ins <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. (Avoid using lines of code as a metric <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>).
*   **C - Communication and Collaboration**: Measures how people work and interact, including meetings, collaboration within teams, searchability of a code base, or system communication <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.
*   **E - Efficiency and Flow**: Tracks the flow of work through a system, such as time through a pipeline or the number of hops a ticket takes <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

To use SPACE effectively, one should select metrics from **at least three dimensions** simultaneously to ensure balance and prevent unintended consequences <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>. DORA, for example, is considered an "implementation of SPACE," focusing on the outer loop <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

### Combining Qualitative and Quantitative Data

Forsgren strongly advocates for collecting both qualitative (from people, e.g., surveys or interviews) and quantitative (from systems, e.g., telemetry) data. While system data can be easily instrumented and scaled <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>, qualitative data provides crucial insights that systems cannot, such as whether high speed is achieved through "absolute heroics" or whether significant portions of code are not being version controlled <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a>. Even the most advanced organizations with extensive instrumentation still survey their developers regularly <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>.

## Common Pitfalls and Best Practices

When implementing developer productivity systems, common pitfalls include:
*   **Lack of clear goals**: "Not being clear or not understanding what it is that they're looking for" <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>.
*   **Insufficient buy-in**: Not pursuing improvements with both top-down and bottom-up engagement <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.
*   **Poor communication**: Failing to effectively communicate motivations and value points to both individual contributors (ICs) and leaders <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a>.

Google is cited as a good model for its systematic, data-informed approach, consistently investing in surveys and triangulating data, often finding surveys to be more accurate than instrumentation when disagreements arise <a class="yt-timestamp" data-t="00:55:32">[00:55:32]</a>.

## Impact of AI on Productivity

The rise of AI has significantly amplified the need for improved software development pipelines. Forsgren notes that AI has "poured gas on top of everything" <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a>, making it crucial to build "absolutely novel incredibly new experiences" at unprecedented speeds <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>.

AI tools like GitHub Copilot are fundamentally shifting how developers work, with more time now spent reviewing generated code than writing it <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>. This frees up cognitive space for harder tasks but also changes mental models, expected friction, and reliance on code. Future metrics may need to account for dimensions like "trust or reliability" in AI tools <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.

## Tactical Advice for Improvement

1.  **Define the Problem/Goal Clearly**: Ensure your objective is "super super crisp" <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>. This is the biggest challenge for many teams <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a>.
2.  **Gather Existing Data**: Look for any existing "signal that is related to the problem" <a class="yt-timestamp" data-t="00:54:56">[00:54:56]</a>.
3.  **Talk to Developers**: Ask developers how they feel about their work tools and processes, and what their biggest barriers to productivity are <a class="yt-timestamp" data-t="01:14:30">[01:14:30]</a>.

## The Four-Box Framework

This simple yet powerful [[frameworks_for_life_and_career_planning | framework]] helps define and measure hypotheses, particularly for product managers and leaders. It involves drawing four boxes:

```
+-------+   +-------+
| WORDS |-->| WORDS |
+-------+   +-------+
    |           |
    v           v
+-------+   +-------+
| DATA  |-->| DATA  |
+-------+   +-------+
```

1.  **Start with "Words"**: In the top-left box, define your independent variable (e.g., "Customer Satisfaction"). In the top-right box, define your dependent variable (e.g., "Return Customers"). The arrow implies a suspected causal relationship (e.g., "customer satisfaction gets us more money" <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>).
2.  **Validate with Stakeholders**: Discuss this "word" hypothesis with others to ensure shared understanding and agreement <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>.
3.  **Define "Data"**: In the bottom-left box, list the specific metrics or data points that will measure your independent variable (e.g., "CSAT score," "NPS"). In the bottom-right box, list metrics for your dependent variable (e.g., "returned customers as measured through the website," "referral link usage") <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.
4.  **Analyze and Iterate**: Conduct a correlation analysis between the data points. If the results are unexpected, the framework helps identify where the issue lies: either the data quality/proxies were poor (issues in the "data" boxes) or the initial hypothesis (the "words") was incorrect or not worth testing <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.

The framework ensures clarity and helps avoid "spurious correlations" by forcing a clear articulation of expectations before diving into data analysis <a class="yt-timestamp" data-t="01:02:53">[01:02:53]</a>. Forsgren also applies a similar spreadsheet-based decision-making process for [[career_advice_and_frameworks | career advice and frameworks]] or personal choices, defining criteria, weighting them, and scoring options <a class="yt-timestamp" data-t="01:04:42">[01:04:42]</a>. The key to a good strategy, she notes, is knowing what not to do and then actually not doing it <a class="yt-timestamp" data-t="01:07:35">[01:07:35]</a>.