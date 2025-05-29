---
title: Developer productivity improvement
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

[[measuring_and_improving_engineering_productivity | Measuring and improving engineering productivity]] is a significant challenge for many organizations, with 80% of teams and executives struggling to clearly define their goals in this area [00:00:06]. Ambiguous objectives, such as "improve [[understanding_and_improving_developer_experience | developer experience]]" without specifying if it refers to inner/outer loop, friction, or culture, can lead teams in different directions [00:00:18].

## Understanding Key Concepts

Nicole Forsgren, a leading expert in [[understanding_and_improving_developer_experience | developer experience]] and productivity, defines these terms as follows:

*   **Productivity** is how much work can be accomplished over time [00:08:22]. A holistic measure of productivity considers community effects (as software is a team sport) and well-being, leading to sustainability and reduced burnout when done correctly [00:08:37].
*   **[[understanding_and_improving_developer_experience | Developer Experience (DevEx)]]** refers to the experience of writing software, focusing on whether the process is friction-free, predictable, and certain [00:09:10]. DevEx contributes significantly to overall productivity [00:08:53].
*   **DevOps** describes the capabilities, [[tools_and_technologies_for_enhancing_productivity | tools and technologies for enhancing productivity]], and processes that enhance software development and delivery end-to-end, making it faster and more reliable [00:09:41]. It encompasses technical, architectural, and cultural practices [00:09:53].

Leaders universally desire faster movement, greater engineer productivity, quicker product releases, and happier engineers [01:10:07]. The challenge often lies in demonstrating the business case and ROI, or addressing concerns about instability when moving too quickly [01:10:49]. Historical misconceptions, like the belief that a two-week wait for change approvals ensures stability, have been disproven [01:11:13]. In reality, implementing good technical and architectural practices allows for faster movement while simultaneously increasing stability [01:12:31].

## Frameworks for Measurement and Improvement

### The DORA Framework

The DORA (DevOps Research and Assessment) framework is an extensive research program, best known for its "Four Keys" or "Four Metrics" for software delivery performance [01:14:03]:

*   **Speed Metrics:**
    *   **Lead Time for Changes:** Time from code commit to code running in production [01:14:31].
    *   **Deployment Frequency:** How often code is deployed [01:14:38].
*   **Stability Metrics:**
    *   **Mean Time to Restore (MTTR):** How long it takes to recover from an incident [01:14:44].
    *   **Change Fail Rate:** The percentage of changes requiring human intervention [01:14:51].

A key finding from DORA research is that **speed and stability move in tandem** [01:15:04]. Moving faster by pushing smaller, more frequent changes leads to more stable systems, smaller blast radii for errors, and easier debugging [01:15:21]. Conversely, less frequent, larger batch changes lead to more unstable systems and longer debugging times [01:15:46].

#### DORA Benchmarks (Elite Performance - 2019 data)
*   **Deployment Frequency:** On demand (multiple times a day) [01:19:33].
*   **Lead Time for Changes:** Less than one day [01:19:36].
*   **Time to Restore Service:** Less than one hour [01:19:39].
*   **Change Fail Rate:** Between 0-15% [01:19:41].

These benchmarks apply across companies of all sizes; studies show no statistical significance between small and large companies, except for retail (which performs better due to market pressure) [01:22:58]. The most important aspect is knowing your current state and making continuous progress, rather than solely focusing on elite benchmarks [01:17:20].

To improve DORA metrics, organizations should focus on [[implementing_technical_and_cultural_practices_for_efficient_software_development | technical and cultural practices for efficient software development]], such as:
*   Automated testing [01:27:01]
*   CI/CD (Continuous Integration/Continuous Deployment) [01:27:02]
*   Trunk-based development [01:27:10]
*   Using a Version Control System [01:27:13]
*   Loosely coupled architectural systems [01:27:23]
*   Effective use of cloud technologies [01:27:26]
*   Fostering a positive culture [01:27:44]

For a quick check on your organization's DORA performance and potential constraints, visit [dora.dev](http://dora.dev/) [01:28:07]. The book "Accelerate" by Nicole Forsgren further compiles and expands on DORA research [01:25:58].

### The SPACE Framework

The SPACE framework provides a balanced way to measure complex, creative work, including [[measuring_and_improving_engineering_productivity | developer productivity]] [01:30:03]. It's a framework to help select the right metrics, not a prescriptive list like DORA [01:30:06]. SPACE emphasizes using at least three dimensions to ensure balance and avoid unintended consequences [01:32:24].

The five dimensions of SPACE are:

*   **S - Satisfaction and Well-being:** Measures how developers feel about their work, which is highly correlated with other productivity dimensions and acts as an important signal for potential breakdowns [01:30:51]. This can be measured through periodic surveys [01:35:43].
*   **P - Performance:** The outcome of a process, such as reliability, MTTR, or change fail rate (as seen in Dora) [01:31:22].
*   **A - Activity:** Countable metrics that are easy to instrument, like the number of pull requests or check-ins [01:31:40].
*   **C - Communication and Collaboration:** How people work and communicate, including meetings, collaboration patterns, or code base searchability [01:31:53].
*   **E - Efficiency and Flow:** The flow of work through a system, such as time spent in various stages or the number of hops a ticket takes [01:32:06].

DORA can be considered an implementation of SPACE, focusing on the outer loop of software delivery [01:32:31]. The SPACE paper outlines this framework with examples of metrics for each category and is available via ACM [01:38:32].

## Data-Informed Approach

It's crucial to combine qualitative data (from people) and quantitative data (from systems) [01:36:58].
*   **Qualitative data**, often gathered through surveys or interviews, provides insights into human factors like "heroics" required to meet deadlines or code not being committed to version control, which system data alone cannot reveal [01:37:22].
*   **Quantitative data**, pulled from systems, offers scalable and engineered insights [01:43:48].

Even the most advanced teams with extensive instrumentation still conduct annual developer surveys to gain new insights [01:39:51].

## The Four-Box Framework for Hypothesis Testing

To clearly define and measure hypotheses, use the four-box framework:

1.  **Start with "Words":** Define your hypothesis or assumption in two boxes, e.g., "Customer Satisfaction" -> "Return Customers" [00:58:26].
2.  **Validate with Stakeholders:** Ask others if they agree with this relationship [00:59:22].
3.  **Define "Data":** In the two boxes below, outline how you will measure each "word" with actual data points, e.g., "Customer Satisfaction" measured by a CSAT score, and "Return Customers" by website return data [00:59:36].
4.  **Analyze and Iterate:** Run correlations. If results diverge, examine if the data is poor quality, if there are missing data points, or if the initial "words" (hypothesis) were flawed [01:00:54].

This framework helps ensure clarity, facilitates communication, and identifies where issues lie (data quality vs. hypothesis validity) [01:01:56].

## Impact of AI on Productivity

The rise of AI has intensified the focus on [[measuring_and_improving_engineering_productivity | developer productivity]], emphasizing the ability to create novel experiences at unprecedented speeds [01:49:05]. AI tools like GitHub Copilot are fundamentally shifting how developers work:
*   Developers spend more time reviewing code than writing it [01:51:55].
*   Cognitive load and expectations of friction are changing [01:53:13].
*   Questions arise about reliance/over-reliance on AI, its impact on learning, and how it affects novices versus experts [01:53:17].

The goal with AI is not merely to cut task time in half, but to free up cognitive space, enabling developers to tackle harder, more complex problems [01:52:45]. A holistic, balanced approach to metrics is essential to avoid oversimplification [01:53:41].

## Common Pitfalls and Advice for Improvement

### Pitfalls to Avoid
1.  **Lack of Clarity:** Not being clear or understanding what you're looking for, leading to scattered efforts [01:55:57].
2.  **Unbalanced Approach:** Not pursuing improvement with both top-down (leadership buy-in) and bottom-up (IC engagement) strategies [01:46:10].
3.  **Poor Communication:** Failing to communicate clearly to all stakeholders, including individual contributors (ICs) and leaders [01:46:22].

### General Advice
*   **Be Crisp on Your Problem/Goal:** Clearly define what you are trying to achieve [01:54:51]. This is a bigger challenge than most realize [01:42:05].
*   **Start with Existing Data/Signal:** Look for any data, however loosely defined, that relates to the problem [01:54:53].
*   **Talk to Developers:** If no data exists, ask a handful of developers how they feel about their work, tools, processes, and the biggest barriers to their productivity [01:54:56].
*   **Communicate Strategically:** Tailor your communication to your audience (e.g., leaders versus individual contributors) and their motivations [01:56:56]. Explain the "why" and connect improvements to business value [01:46:43].
*   **Prioritize and Decide:** Use a decision-making framework (like a weighted criteria spreadsheet) to clearly define criteria, assign weights, and make informed choices about what to fund and what not to do [01:04:40].

## Recommended Resources

*   **DORA Website:** [dora.dev](http://dora.dev/) - Provides updated reports, a quick check tool for benchmarks, and deep dives into capabilities [01:19:18].
*   **Book: *Accelerate*** by Nicole Forsgren, Jez Humble, and Gene Kim - Details the DORA research findings and practices [01:25:58].
*   **Paper: The SPACE Framework:** Available at ACM, it outlines the framework and provides metric examples [01:38:32].
*   **Paper on Human and System Data:** A paper co-authored with Mick Kirsten from 2016/2017 discusses the complementary importance of data from people and data from systems [01:36:58].
*   **Book: *How to Measure Anything*** by Douglas Hubbard - Discusses how to measure intangibles, especially when starting with no data [00:40:03].
*   **Book: *Good Strategy Bad Strategy*** by Richard Rumelt - Explores effective strategy development [01:11:10].
*   **Book: *Designing Your Life*** by Bill Burnett and Dave Evans - A practical guide to life design [01:16:16].

Nicole Forsgren is also working on a new book that will provide guidance on how to measure developer productivity from scratch, the measurement journey, and the trade-offs between subjective and objective data [01:41:37]. Interested individuals can sign up for notifications on her website, [nicolefv.com](http://nicolefv.com/) [01:44:50]. She also encourages sharing success stories or questions regarding measurement [01:45:01].