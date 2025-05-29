---
title: Measuring Engineering Productivity and Performance
videoId: Z9ftpRhRiJE
---

From: [[lennyspodcast]] <br/> 

Measuring engineering productivity and performance has become an increasingly critical aspect of product development, particularly in a market that prioritizes efficiency and output <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. The shift from a "zero interest rate era" to a more constrained market has led to a greater focus on how effectively engineering teams contribute to business goals <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Evolution of Engineering Roles and Accountability

Historically, engineers have sometimes been "coddled," sheltered from direct accountability for product outcomes <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This approach was partly driven by an emphasis on retention, where losing team members was a major issue for middle management <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. However, this "coddling" can be detrimental to engineers' growth and the organization's efficiency <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

There is a growing trend towards treating engineers as peers and placing them in senior leadership roles, holding them accountable for solving real problems <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This means a direct focus on:
*   **Leading the team deeply** <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>
*   **Figuring out the right allocation and sizing of engineering teams** <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
*   **Giving engineers hard problems and holding them accountable** <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This enables them to grow and assume senior roles <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

## Approaches to Measuring Productivity

The most common and challenging questions for engineering leaders are "How do I know if my engineers are moving as quickly as they can?" and "How do we help them move faster?" <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>

### 1. Benchmarking

A straightforward, mechanical approach involves benchmarking spending on R&D and engineering against industry data, often provided by venture capital funds <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>. While this can provide a defensible answer to boards regarding spending, it doesn't offer insights into improving organizational effectiveness <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.

### 2. Qualitative Insights

*   **Talk to Engineers**: Engineers often know if their teams are effective and can identify reasons for inefficiency <a class="yt-timestamp" data-t="00:50:28">[00:50:28]</a>. Leaders can use these "crumbs" to diagnose contributing causes <a class="yt-timestamp" data-t="00:50:40">[00:50:40]</a>.
*   **Align Engineering to Business and Product Goals**: Engineering evaluation should be wholly accountable to product goals, rather than focusing solely on internal engineering metrics <a class="yt-timestamp" data-t="00:51:27">[00:51:27]</a>.
*   **Show the Roadmap of Valuable Work**: Clearly demonstrating the meaningful, impactful contributions over a period (e.g., six months) can build trust and space from stakeholders <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>. If this list is difficult to populate, it signals a legitimate concern <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>.

### 3. Quantitative Metrics (DORA Metrics)

One of the most influential frameworks in software engineering leadership is the [[DORA Metrics|DORA metrics]] from the book *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>. These four key metrics are:
1.  **Lead Time**: Time from code committed to code running in production <a class="yt-timestamp" data-t="00:53:09">[00:53:09]</a>.
2.  **Deployment Frequency**: How often an organization successfully releases to production <a class="yt-timestamp" data-t="00:53:09">[00:53:09]</a>.
3.  **Mean Time To Restore (MTTR)**: Time it takes to restore service after an incident <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>.
4.  **Change Failure Rate**: Percentage of changes to production that result in degraded service and require remediation <a class="yt-timestamp" data-t="00:53:14">[00:53:14]</a>.

These metrics are excellent for **diagnosis** (e.g., "our deployments are slow, why?"), but they don't directly indicate if a company is "good" or "bad" <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>. They tell you where to invest in improvement, not whether to fire engineers <a class="yt-timestamp" data-t="00:53:43">[00:53:43]</a>.

### Overcoming Measurement Paralysis

Engineers, being experts, can often identify flaws and inaccuracies in any proposed measurement, leading to the measurement of nothing <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>. It's crucial to:
*   **Get Comfortable with Imperfection**: Measure something, even if it's not perfect <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>.
*   **Educate Stakeholders**: Use imperfect metrics as an opportunity to educate those consuming them about the nuances and limitations of the data <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>. This helps them develop a more sophisticated understanding of engineering efforts <a class="yt-timestamp" data-t="00:55:27">[00:55:27]</a>.

## Systems Thinking for Performance Analysis

[[Systems Thinking|Systems thinking]] involves conceptualizing operations in terms of "stocks" (things that accumulate) and "flows" (movement between stocks) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This approach can be applied to analyze various processes, including:

*   **Incident Management**: At Stripe, initial efforts focused heavily on analyzing incidents, but without prioritizing improvements, the system became stuck in endless measurement <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. The key is to move from analysis to action <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Hiring Pipeline**: A hiring pipeline can be modeled with stocks (e.g., potential candidates, sourced candidates, candidates in different interview stages) and flows (e.g., conversion rates between stages) <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. By mapping this model against real data from applicant tracking systems, organizations can identify bottlenecks, such as:
    *   Hiring managers not extending offers due to lack of confidence <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   Offers extended but not accepted <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
    *   Insufficient candidates entering the pipeline <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

This allows for systematic problem-solving, rather than making broad changes based on assumptions <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

## Collaborative Performance Evaluation

To address misaligned incentives and improve [[Engineering and Product Management Collaboration|engineering and product management collaboration]], some companies implement a shared performance evaluation model. For example, the Engineering Manager (EM) and Product Manager (PM) in a pair might receive the same performance rating <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>. This fosters a shared understanding of success and encourages balanced decision-making, rather than focusing solely on functional constraints <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. This model can even be extended to include business leadership, creating a "trifecta" <a class="yt-timestamp" data-t="00:45:06">[00:45:06]</a>.