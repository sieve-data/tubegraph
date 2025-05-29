---
title: Dora and Space frameworks for developer performance
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Nicole Forsgren, a renowned expert in developer productivity, emphasizes that a significant challenge for many teams, even at executive levels, is clearly defining their problems or goals [00:00:00]. Teams may spend months working on [[improving_developer_experience | developer experience]], only to find that the initial directive was too vague (e.g., whether it refers to inner/outer loop, friction, or culture) [00:00:11]. This lack of clarity can lead teams in "completely different directions" [00:00:31].

Forsgren's work, including the award-winning book *Accelerate* and the annual *State of DevOps Report*, focuses on [[measuring_developer_productivity | measuring developer productivity]] and experience, implementing frameworks like DORA and SPACE, and helping companies move faster, improve quality, and transform cultures [00:01:00].

## The DORA Framework

DORA (DevOps Research and Assessment) is a comprehensive research program, widely recognized for its "Four Keys" or "DORA Four" metrics [00:14:03]. These metrics measure software delivery performance and consist of two speed metrics and two stability metrics [00:14:21]:

*   **Speed Metrics**
    *   **Lead Time for Changes**: How long it takes to get code from committed to running in production [00:14:31].
    *   **Deployment Frequency**: How often code is deployed [00:14:35].
*   **Stability Metrics**
    *   **Mean Time to Restore (MTTR)**: How long it takes to recover if something goes wrong [00:14:40].
    *   **Change Fail Rate**: The percentage of changes pushed that result in incidents or require human intervention [00:14:51].

A crucial finding from DORA research is that speed and stability move in tandem [00:15:01]. This means that when you move faster, you are actually *more stable* [00:15:16]. The reason for this counter-intuitive result is that faster deployment encourages smaller, more frequent changes, which inherently have a smaller "blast radius." If an error occurs, it's easier to debug, restore, and mitigate [00:15:25]. Conversely, less frequent deployments lead to larger batch changes, making systems more unstable and errors harder to disentangle [00:15:46]. This insight directly challenges older IT change management processes, like ITIL/ITSM, which often enforced two-week waiting periods for approvals, inadvertently causing larger, riskier batches of changes [00:16:25].

### DORA Benchmarks (Elite Performance - 2019 data)

While the most important aspect is knowing your own progress, these benchmarks provide a target [00:17:20]:

*   **Deployment Frequency**: On demand [00:19:33].
*   **Lead Time for Changes**: Less than a day [00:19:36].
*   **Time to Restore**: Less than an hour [00:19:40].
*   **Change Fail Rate**: Between 0% and 15% [00:19:41].

These benchmarks apply broadly, with no statistical significance found between small and large companies, except for retail, which performed better due to market pressures (the "retail apocalypse" forced top-tier performance) [00:22:56].

To achieve these metrics, DORA emphasizes improving a set of **capabilities** [00:26:17]. These are not just toolchains, but:

*   **Technical Capabilities**: Such as automated testing, CI/CD (Continuous Integration/Continuous Deployment), trunk-based development, and effective use of Version Control Systems [00:26:58].
*   **Architectural Practices**: Like having a loosely coupled system and proper cloud utilization [00:27:21].
*   **Cultural Capabilities**: Fostering a good team culture [00:27:44].

The DORA website ([dora.dev](http://dora.dev)) offers a "quick check" tool where organizations can plug in their current performance to see where they stand and identify probable constraints based on industry data [00:28:07].

## The SPACE Framework

SPACE is a framework designed to measure complex, creative work, including [[measuring_developer_productivity | developer productivity]] [00:29:30]. Unlike DORA, which provides specific metrics, SPACE offers a framework to *select* the right metrics within a given context, using available data [00:30:03].

SPACE stands for five dimensions of productivity:

*   **S - Satisfaction and Well-being**: This includes aspects like sustainability and burnout. It's highly correlated with other productivity dimensions and can be an early signal of problems [00:30:47].
*   **P - Performance**: The outcome of a process, such as system reliability, MTTR, or change fail rate (like DORA's stability metrics) [00:31:22].
*   **A - Activity**: Any count or number of something, often easy to instrument (e.g., number of pull requests, check-ins) [00:31:38].
*   **C - Communication and Collaboration**: How people work and talk together (meetings, collaboration) or how systems communicate (codebase searchability) [00:31:53].
*   **E - Efficiency and Flow**: The time taken for flow through a system (e.g., time through deployment pipeline, number of hops for a ticket) [00:32:06].

To use SPACE effectively, you should select at least **three dimensions** to ensure balance and avoid unintended consequences [00:32:23]. DORA's Four Keys, for instance, are an implementation of SPACE, primarily focusing on the "outer loop" aspects [00:32:30].

A key takeaway for measuring developer productivity is to combine **qualitative insights** (data from people via surveys and interviews) and **quantitative insights** (data from systems) [00:41:00]. Qualitative data can reveal "heroics" or code not even in systems, which quantitative data would miss [00:37:22]. Even the most advanced teams with extensive instrumentation still survey their developers periodically to gain insights not available from system data [00:39:34].

## Practical Application and Pitfalls

### Common Pitfalls
When rolling out [[improving_developer_experience | developer experience]] or [[measuring_developer_productivity | developer productivity]] initiatives, [[common_pitfalls_in_enhancing_developer_productivity_systems | common pitfalls]] include:

*   **Lack of Clarity**: Not being clear on the problem or goal, leading to scattered efforts [00:45:57].
*   **Unbalanced Approach**: Failing to pursue initiatives with both top-down (leadership buy-in) and bottom-up (IC engagement) strategies [00:46:10].
*   **Poor Communication**: Not using the right vocabulary or value points to communicate effectively with different stakeholders, especially executive teams who need to see the ROI [00:46:22].

### Evolution of the Field and AI's Impact
The landscape of developer productivity has changed significantly. Companies now deal with increasingly large and complex systems, face perceived developer shortages, and are more acutely aware of their technology-driven nature [00:47:58]. The recent "AI moment" has "poured gas on top of everything" [00:49:03]. It's no longer just about building things, but creating "absolutely novel, incredibly new experiences" at unprecedented speed [00:49:25]. This necessitates a fast, safe, stable, and reliable software pipeline [00:49:38].

AI's impact on engineering productivity is profound. Developers using AI-enabled tools like GitHub Copilot fundamentally shift their workflow, spending more time reviewing code than writing it [00:51:50]. This changes mental models, expected friction, cognitive load, and reliance on code [00:53:09]. While AI can make certain tasks faster, its true value lies in freeing up cognitive space for developers to tackle harder problems and create new, complex features [00:52:50]. It's crucial to resist the oversimplification of AI's role (e.g., using it to justify layoffs) and instead focus on holistic, balanced metrics to understand its true impact on productivity, learning, and well-being [00:53:35].

## Other Useful Frameworks and Advice

### The Four Box Framework
This framework helps to clarify hypotheses and measurement [00:57:48]:
1.  Draw four boxes: two on top (aligned), two on bottom (aligned).
2.  Left of the top boxes, write "Words"; left of the bottom boxes, write "Data" [00:58:23].
3.  Draw an arrow between the two top boxes and between the two bottom boxes [00:58:34].
4.  **Top Boxes (Words)**: Start with a hypothesis (e.g., "Customer satisfaction leads to return customers"). Write the concepts in the boxes [00:59:03]. Validate this with stakeholders [00:59:22].
5.  **Bottom Boxes (Data)**: Define how you will measure each concept from the "Words" boxes. These are your data points or proxies (e.g., "Customer satisfaction" measured by CSAT/NPS score, "Return customers" by website tracking or referral links) [00:59:36].
6.  Run correlations/analysis [01:00:59]. If the results don't support the hypothesis, evaluate the "Data" boxes (poor data quality, missing data, bad proxies) or go back to the "Words" boxes (the hypothesis itself may be flawed) [01:01:07]. This framework provides a structured way to identify where the problem lies, rather than blaming individuals [01:01:32].

### Decision-Making Spreadsheet
For making decisions, both personal and professional, Forsgren recommends a spreadsheet approach [01:04:54]:
1.  **Define Objectives and Criteria**: Clearly state what you are trying to achieve and identify all relevant criteria (e.g., for a job: total compensation, team, work-life balance) [01:05:38].
2.  **Weight Criteria**: Assign a relative weight (adding up to 100%) to each criterion based on its importance [01:06:37].
3.  **Score Options**: Rate each option against each criterion.
4.  **Calculate and Choose**: Multiply scores by weights to get a total score. This provides a data-informed decision, though personal judgment can still be applied (data-informed, not data-driven) [01:07:08]. The act of simply identifying and weighing criteria can often reveal the right decision [01:06:01].

### Tactical Advice for This Week
*   **Clarify Goals**: If working on developer productivity, ensure your problem or goal is clearly written down and understood [01:14:20].
*   **Find Data**: Identify any existing data or signals related to that problem [01:14:53].
*   **Talk to Developers**: If no data exists, directly ask developers about their work tools, processes, and biggest barriers to productivity [01:14:29].