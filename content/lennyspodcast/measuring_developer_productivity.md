---
title: Measuring Developer Productivity
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Measuring [[Measuring Engineering Productivity and Performance | engineering team productivity and experience]] is a complex challenge, with a significant percentage of teams, even at executive levels, struggling to clearly define their goals and problems <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a> <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a>. Without clear definitions, teams can head in "completely different directions" <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a> <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>.

Dr. Nicole Forsgren, a leading expert in [[Measuring Engineering Productivity and Performance | developer productivity]], has dedicated her career to understanding and improving how software teams build and deliver products <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Her work emphasizes the need for a holistic approach to [[Measuring Engineering Productivity and Performance | measuring engineering productivity and performance]] <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## Key Definitions

Nicole Forsgren distinguishes between several related concepts <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:

*   **Productivity**
    *   Refers to "how much we can get done and how much we can do over time" <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    *   A holistic measure that includes community effect (as software is a team sport) and well-being, which leads to sustainability and reductions in burnout when done correctly <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a> <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Developer Experience (DevEx)**
    *   Contributes significantly to [[Measuring Engineering Productivity and Performance | productivity]] <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
    *   Focuses on "what is it like to write software" – aiming for a friction-free, predictable, and certain experience for developers, who are the "users" in the software development process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a> <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **DevOps**
    *   Refers to the "capabilities and tools and processes that we can use to improve our software development and delivery end to end" <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
    *   Enables faster and more reliable work through technical, architectural, and cultural practices <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## The DORA Framework (Four Keys)

The DORA (DevOps Research and Assessment) framework provides four key metrics for [[Measuring Engineering Productivity and Performance | software delivery performance]] <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. These metrics are composed of two speed metrics and two stability metrics <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### Speed Metrics

1.  **Lead Time for Changes**: The time it takes to get from code committed to code running in production <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. Elite performers achieve this in less than one day <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
2.  **Deployment Frequency**: How often code is deployed <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Elite performers deploy on demand <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

### Stability Metrics

1.  **Mean Time to Restore (MTTR)**: How long it takes to restore service if something happens (e.g., an incident) <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. Elite performers restore service in less than one hour <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
2.  **Change Fail Rate**: The percentage of changes pushed that result in incidents requiring human intervention <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Elite performers have a change fail rate between 0% and 15% <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

### The Relationship Between Speed and Stability

A surprising finding from DORA research is that speed and stability move in tandem <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This means:

*   **Moving faster leads to more stable systems** <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. This is because faster delivery encourages pushing smaller, more frequent changes, which reduces the "blast radius" of errors and makes debugging easier <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a> <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
*   **Less frequent changes lead to less stable systems** <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. Large batch changes, often caused by long approval processes, create complex "balls of mud" that are harder to disentangle and debug when issues arise <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a> <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

This challenges old beliefs, such as the need for two-week change approvals, which actually cause batching and instability <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a> <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. The key message is to [[Balancing Speed and Quality in Product Development | ship smaller things more often]] to improve both speed and quality <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a> <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

### Benchmarks and Application

DORA provides benchmarks for low, medium, high, and elite performers <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. While interesting, the most important aspect is knowing your current state and making progress <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. These benchmarks apply across companies of all sizes, with retail being a slight outlier due to market pressures <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a> <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.

To improve these metrics, focus on [[improving_developer_experience | developer experience]] and implementing good technical and architectural practices <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a> <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. These include:

*   Automated testing <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>
*   CI/CD (Continuous Integration, Continuous Deployment) <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>
*   Trunk-based development <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>
*   Using a Version Control System <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>
*   Loosely coupled systems and effective cloud utilization <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>
*   Positive culture <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>

The dora.dev website offers a "quick check" tool to benchmark your organization and identify potential constraints <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

## The SPACE Framework

The SPACE framework is designed to help organizations choose the right metrics for measuring complex creative work like [[Measuring Engineering Productivity and Performance | developer productivity]] <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a> <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. It advises selecting at least three dimensions to ensure balance <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>. DORA's Four Keys are considered an implementation of SPACE for the "outer loop" of software delivery <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.

SPACE stands for five dimensions:

*   **S - Satisfaction and Well-being**: This dimension includes self-explanatory metrics like job satisfaction and burnout <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>. It's highly correlated with other productivity dimensions and is an important signal: if satisfaction falls, other things break <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a> <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.
*   **P - Performance**: Focuses on the outcomes of a process, such as reliability or the DORA metrics of MTTR and Change Fail Rate <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **A - Activity**: Metrics based on counts or numbers, which are often easy to instrument and automate (e.g., number of pull requests, check-ins) <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. However, relying solely on activity metrics (like lines of code) is a common pitfall <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>.
*   **C - Communication and Collaboration**: Measures how people work and talk together, including meetings, collaboration, searchability of a codebase, and how systems communicate <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.
*   **E - Efficiency and Flow**: Tracks the flow through a system, such as time taken (e.g., time through the deployment pipeline) or the number of hops a ticket takes <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.

To use SPACE, pick at least three dimensions that make sense in your context and aim for a balance or "intention" between them to avoid unintended consequences <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a> <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>. For example, when trying to improve pull request speed, balance it with developer time for coding and developer satisfaction with the review process <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a> <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>.

## Combining Qualitative and Quantitative Data

Effective [[Measuring Engineering Productivity and Performance | measurement]] relies on combining both qualitative data (from people) and quantitative data (from systems) <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a> <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.

*   **Qualitative Data**: Gathered through surveys or interviews, typically conducted periodically (e.g., every few months for satisfaction) <a class="yt-timestamp" data-t="00:35:43">[00:35:43]</a>. This provides insights that system data cannot, such as understanding "heroics" behind fast delivery times or code not being in version control <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a> <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>.
*   **Quantitative Data**: Instrumentable and automatable, pulled from systems frequently (e.g., lead time, deployment frequency) <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>.

Even the most advanced teams with extensive instrumentation still conduct annual developer surveys to gain new insights <a class="yt-timestamp" data-t="00:39:50">[00:39:50]</a>.

## Common Pitfalls and Challenges

Companies often face several pitfalls when rolling out [[Measuring Engineering Productivity and Performance | developer experience]] and [[Measuring Engineering Productivity and Performance | productivity]] systems:

*   **Lack of Clarity**: Not clearly defining what they are looking for or the problem they are trying to solve <a class="yt-timestamp" data-t="00:45:53">[00:45:53]</a>.
*   **Unbalanced Approach**: Failing to pursue initiatives with both top-down and bottom-up buy-in <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>. Good communication throughout the organization is crucial, understanding the vocabulary and motivations of both individual contributors and leaders <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a>.
*   [[Avoiding traditional metrics for product development | Avoiding traditional metrics for product development]]: Over-reliance on simple, easily measurable metrics like lines of code or number of pull requests without considering the full context.

## The Evolution of the Field and AI's Impact

The landscape of [[Measuring Engineering Productivity and Performance | developer productivity]] has evolved significantly:

*   **Increased System Complexity**: Modern companies deal with increasingly large and complex systems compared to a decade ago <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>.
*   **Developer Shortage**: A perceived or reported shortage of developers <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>.
*   **Technology-Driven Companies**: Most companies now recognize they are technology-driven, making [[Measuring Engineering Productivity and Performance | software delivery performance]] a strategic priority <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>.

The rise of [[Role of AI in Developer Productivity | AI in developer productivity]] has "poured gas" on these trends <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a> <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a>. It's no longer just about building features, but about creating novel experiences at unprecedented speeds <a class="yt-timestamp" data-t="00:49:21">[00:49:21]</a>. AI tools fundamentally shift how developers work, moving from writing code to reviewing code <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a> <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>. This frees up cognitive space for harder tasks but also introduces new considerations around trust, reliance, learning, and the impact on novices versus experts <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a> <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>.

## Getting Started with Measurement

To begin improving [[Measuring Engineering Productivity and Performance | developer productivity]]:

1.  **Define the Problem/Goal**: Ensure there is a "clearly defined challenge [or] problem" that is "super, super crisp" <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a> <a class="yt-timestamp" data-t="00:53:40">[00:53:40]</a>.
2.  **Seek Existing Data/Signal**: Look for any existing data or signals related to the problem, even if loosely defined <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.
3.  **Talk to Developers**: If no data exists, talk to a handful of developers and ask them about their work tools, processes, and the biggest barriers to their [[Measuring Engineering Productivity and Performance | productivity]] <a class="yt-timestamp" data-t="01:14:30">[01:14:30]</a>.

## The Four Box Framework for Hypothesis Testing

This framework helps in clearly defining and measuring hypotheses:

1.  **Draw Four Boxes**: Two on top, two on bottom, with arrows between the boxes on each row <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.
2.  **Words on Top**: Write "words" to the left of the top boxes, and "data" to the left of the bottom boxes <a class="yt-timestamp" data-t="00:58:26">[00:58:26]</a>.
3.  **Define Hypothesis (Words)**: Start by clearly stating your hypothesis in words. For example, "customer satisfaction gets us more money" <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>. Place "customer satisfaction" in the first top box and "more money" in the second <a class="yt-timestamp" data-t="00:59:12">[00:59:12]</a>.
4.  **Define Metrics (Data)**: In the bottom boxes, define how you will measure each concept. For "customer satisfaction," it could be a CSAT score or NPS <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>. For "more money," it could be return customers or referral links <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>.
5.  **Test and Iterate**: Run correlations or analyses. If the results are unexpected, you can pinpoint the problem: is the data poor quality, missing, a bad proxy, or is the initial hypothesis (words) incorrect? <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a> This framework encourages clarity and prevents getting "mad at Lenny for his really stupid idea" <a class="yt-timestamp" data-t="01:03:34">[01:03:34]</a>.

## Decision-Making Framework

To make better decisions, both in business and personally:

1.  **Define Objectives and Criteria**: Clearly define your objectives and what criteria are important for the decision <a class="yt-timestamp" data-t="01:04:38">[01:04:38]</a>.
2.  **Weigh Criteria**: Assign a relative weight to each criterion, ensuring they add up to 100% <a class="yt-timestamp" data-t="01:06:37">[01:06:37]</a>.
3.  **Score and Calculate**: Score each option against the weighted criteria and multiply them out <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.
4.  **Data-Informed Choice**: Use the results to inform your decision. The act of identifying and weighing criteria alone can often reveal the answer <a class="yt-timestamp" data-t="01:05:09">[01:05:09]</a> <a class="yt-timestamp" data-t="01:07:15">[01:07:15]</a>.
5.  **Strategic Focus**: Remember that good strategy involves knowing what *not* to do, as you cannot fund or pick everything <a class="yt-timestamp" data-t="01:07:35">[01:07:35]</a>.

## Additional Resources

*   **Book**: *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim <a class="yt-timestamp" data-t="00:59:58">[00:59:58]</a> <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   **Website**: dora.dev for DORA reports and a quick check tool <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a> <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.
*   **Paper**: The SPACE framework paper (available at ACM) <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.
*   **Book**: *How to Measure Anything* by Douglas W. Hubbard <a class="yt-timestamp" data-t="00:40:03">[00:40:03]</a>.

Nicole Forsgren is currently working on a new book that will delve into [[Measuring Engineering Productivity and Performance | measurement]] processes, providing practical guidance for both quick, unofficial measurements and formal, long-term approaches <a class="yt-timestamp" data-t="00:41:32">[00:41:32]</a> <a class="yt-timestamp" data-t="01:15:14">[01:15:14]</a>.

---
*This article draws heavily from the insights of Nicole Forsgren. You can connect with her on Twitter and Bluesky (@NicoleFV) or via her website, nicolefv.com <a class="yt-timestamp" data-t="01:15:03">[01:15:03]</a> <a class="yt-timestamp" data-t="01:15:08">[01:15:08]</a>.*