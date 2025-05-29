---
title: Improving developer experience
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Improving developer experience is a critical goal for organizations, yet it often presents significant challenges in definition and measurement <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Even at executive levels, teams may spend months on initiatives only to return with uncertainty because the problem or goal wasn't clearly articulated <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. For instance, "improve developer experience" can mean vastly different things, such as addressing inner and outer loop friction, or cultural issues, each requiring a distinct approach <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Defining the Problem and Goal

A primary challenge is clearly defining the problem or goal to be addressed <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Approximately 80% of teams struggle with this initial step <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Without crisp objectives, different parts of an organization can head in conflicting directions <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. It's essential to have a clear, written-down challenge or problem statement <a class="yt-timestamp" data-t="00:54:38">[00:54:38]</a>.

## The Core Concepts

Nicole Forsgren, a leading expert in developer productivity, emphasizes the interconnectedness of developer productivity, developer experience, and DevOps <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>. She has contributed significantly to this field through her book *Accelerate* and the *State of DevOps Report* <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>.

### [[developer_productivity_measurement | Developer Productivity]]

[[developer_productivity_measurement | Developer productivity]] refers to how much work can be accomplished over time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It's crucial to measure this holistically, considering factors like community effects (software as a team sport) and developer well-being <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. When productivity is approached correctly, it leads to sustainability, well-being, and reduced burnout <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Developer Experience

Developer experience is defined by what it's like to write software <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. It focuses on reducing friction and increasing predictability in the software development process, directly contributing to productivity <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Developers are considered users in this context <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### DevOps

DevOps encompasses the capabilities, tools, and processes used to improve end-to-end software development and delivery, making it faster and more reliable <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. It involves technical, architectural, and cultural practices that enable more productive work and better developer experience <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. DevOps is not merely a toolchain but a set of practices that predict speed and stability, ultimately leading to financial benefits <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

## Addressing Common Misconceptions

While most leaders want to move faster and have more productive engineers <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>, there's often resistance due to concerns about return on investment (ROI) or fears of instability from moving too quickly <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. An outdated common belief, for example, was that a two-week wait for change approvals was necessary for stability <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## Measuring Performance: The DORA Framework

The DORA (DevOps Research and Assessment) framework provides key metrics for software delivery performance. It is supported by an entire research program <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

### The Four Key Metrics

DORA's "Four Keys" or "Four Metrics" measure both speed and stability <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>:

1.  **Lead Time for Changes**: How long it takes from code commit to code running in production <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
2.  **Deployment Frequency**: How often code is deployed to production <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
3.  **Mean Time To Restore (MTTR)**: How long it takes to restore service after an incident <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
4.  **Change Fail Rate**: The percentage of changes pushed that result in incidents requiring human intervention <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

### Speed and Stability Move in Tandem

A significant finding from DORA research is that speed and stability move together with strong statistical significance <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This means that moving faster (e.g., by pushing smaller changes more often) actually leads to greater stability <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. Conversely, less frequent deployments result in larger batch changes, higher blast radii, and more unstable systems that are harder to debug <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

> "When you move faster you are more stable, which means you're pushing smaller changes more often. So if you're pushing all the time, it's going to be very, very small changes, which means you have a smaller blast radius, which means when you push, you have an error in production, it's going to be easier to debug." <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>

### Elite Performance Benchmarks

As of 2019, Elite Performers achieve the following benchmarks <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>:

*   **Deployment Frequency**: On-demand deployment (or multiple times a day) <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Lead Time for Changes**: Less than one day <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
*   **Mean Time To Restore**: Less than one hour <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
*   **Change Fail Rate**: Between 0% and 15% <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

> It's more important to know where your organization stands and the progress it's making than to strictly compare to benchmarks <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
>
> These benchmarks apply across companies of all sizes, from startups to Fortune 500s; there's no statistical difference based on company size, except for retail companies which tend to perform better due to market pressure <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.

### Identifying Constraints and Capabilities

DORA research identifies specific capabilities that predict speed and stability. These include:

*   **Technical capabilities**: Automated testing <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>, CI/CD (Continuous Integration/Continuous Deployment) <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>, trunk-based development <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>, and using a version control system <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.
*   **Architectural practices**: Loosely coupled systems and effective cloud usage <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.
*   **Cultural aspects**: Fostering a healthy culture <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

Organizations can use the DORA quick check at [dora.dev](https://dora.dev) to assess their current performance profile and identify potential constraints <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.

## Holistic Measurement: The SPACE Framework

The SPACE framework provides a guide for measuring productivity in complex, creative work, including developer productivity <a class="yt-timestamp" data-t="00:29:35">[00:29:35]</a>. It helps organizations select the right metrics for their specific context <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.

### Five Dimensions of SPACE

SPACE stands for five key dimensions:

*   **S - Satisfaction and Well-being**: Measures aspects like developer satisfaction, sustainability, and burnout <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>. This dimension is highly correlated with other productivity aspects and serves as an important signal for potential issues <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.
*   **P - Performance**: Focuses on outcomes of a process, such as reliability, or DORA metrics like MTTR and Change Fail Rate <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **A - Activity**: Quantifiable counts or numbers, often easy to instrument, like the number of pull requests or check-ins <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
*   **C - Communication and Collaboration**: Measures how people work and talk together, including meetings, collaboration patterns, or even the searchability of a codebase <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.
*   **E - Efficiency and Flow**: Focuses on the flow through a system, such as time taken, or the number of hops a ticket makes <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>.

### Using SPACE for Balanced Measurement

To use SPACE effectively, it's recommended to measure at least three dimensions simultaneously to ensure balance and avoid unintended consequences <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>. This forces a comprehensive view rather than focusing on a single, potentially misleading, metric <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>.

For example, when aiming to improve pull requests, rather than just measuring "number of alerts" (Activity), one should also consider "time to work on coding" (Efficiency & Flow) and "satisfaction with the pull request process" (Satisfaction & Well-being) <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.

### DORA as an Implementation of SPACE

DORA's Four Key Metrics (Lead Time, Deployment Frequency, MTTR, Change Fail Rate) are considered an implementation of the SPACE framework, focusing primarily on performance and efficiency <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.

## Effective Measurement Practices

### Combining Qualitative and Quantitative Data

It is crucial to combine qualitative data (from people) with quantitative data (from systems) <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

*   **Qualitative Data**: Best captured through surveys and interviews (e.g., periodically asking about satisfaction) <a class="yt-timestamp" data-t="00:35:43">[00:35:43]</a>. This type of data can reveal insights systems cannot, such as heroic efforts to achieve fast lead times or mission-critical code not under version control <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a>.
*   **Quantitative Data**: Can be instrumented and pulled from systems continuously (e.g., number of pull requests) <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>.

Even the most advanced teams with extensive instrumentation still survey their developers at least once a year to gain new insights <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>.

### Avoiding Misleading Metrics

Avoid using metrics like "number of lines of code" or "number of commits" as primary indicators of productivity, as they are merely activity metrics and can be misleading <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.

## Tactical Steps for Improvement

*   **Define Clarity**: Start by clearly stating the problem or goal <a class="yt-timestamp" data-t="00:41:53">[00:41:53]</a>.
*   **Find Signals**: Identify any existing data or signals related to the problem <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.
*   **Talk to Developers**: Directly ask developers about their feelings regarding work tools and processes, and their biggest barriers to productivity <a class="yt-timestamp" data-t="01:14:30">[01:14:30]</a>.
*   **Ship Smaller, More Often**: To move faster and improve quality, break down work into smaller changes and deploy them more frequently <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. This approach makes systems safer and easier to debug <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

## Common Pitfalls to Avoid

*   **Lack of Clarity**: Not clearly defining what needs to be improved can lead to misaligned efforts <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>.
*   **Unbalanced Approach**: Neglecting either top-down executive buy-in or bottom-up engagement from individual contributors (ICs) <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.
*   **Poor Communication**: Failing to communicate effectively with both leaders (socializing value points) and ICs (understanding their vocabulary and concerns) <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a>.

## Evolution of the Field: The AI Moment

### Increased Complexity and Pressure

Over the last 10-15 years, systems have become increasingly large and complex, nearly every company is now technology-driven, and there is a reported shortage of developers <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>. This has made improving developer experience a pressing concern for more companies <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>.

### [[impact_of_ai_on_developer_productivity | Impact of AI on Developer Productivity]]

The recent "AI moment" has intensified this pressure <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. With AI tools like GitHub Copilot, the focus shifts from writing code to reviewing code <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>. This frees up cognitive space for developers to tackle harder tasks <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>. However, it also raises questions about trust, reliance (or over-reliance) on AI, and how it impacts learning for both novices and experts <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>. The need for holistic, balanced metrics becomes even more critical to avoid oversimplification <a class="yt-timestamp" data-t="00:53:36">[00:53:36]</a>.

## Frameworks for Strategic Thinking

### The Four Box Framework for Hypothesis Testing

This framework helps clarify and test hypotheses by structuring thinking into words and data:

1.  **Words (Top Left)**: State your initial hypothesis or cause (e.g., "customer satisfaction") <a class="yt-timestamp" data-t="00:58:58">[00:58:58]</a>.
2.  **Words (Top Right)**: State the expected effect or outcome (e.g., "return customers") <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.
3.  **Data (Bottom Left)**: Define how you will measure the cause (e.g., "CSAT score" for customer satisfaction) <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>.
4.  **Data (Bottom Right)**: Define how you will measure the effect (e.g., "returned customers as measured through website data") <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>.

Always start with the "words" (your hypothesis) before moving to "data" <a class="yt-timestamp" data-t="00:59:18">[00:59:18]</a>. This structure makes it clear whether issues lie in the data quality or the underlying hypothesis <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>.

### Personal Decision-Making Spreadsheet

A personal spreadsheet can aid in making complex decisions by:

1.  **Outlining Options**: List all possible choices <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>.
2.  **Identifying Criteria**: Define what's important for the decision (e.g., total compensation, prestige, work-life balance for a job) <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>.
3.  **Weighting Criteria**: Assign a relative importance (percentage) to each criterion, summing to 100% <a class="yt-timestamp" data-t="01:06:34">[01:06:34]</a>.
4.  **Scoring Options**: Score each option against each criterion and multiply by its weight <a class="yt-timestamp" data-t="01:06:48">[01:06:48]</a>.

Often, merely identifying and weighting the criteria reveals the optimal decision <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. This process fosters [[tactics_for_driving_growth_and_simplifying_complex_projects | strategic thinking]] by clarifying priorities and what *not* to do <a class="yt-timestamp" data-t="01:07:35">[01:07:35]</a>.

## Conclusion and Next Steps

To begin improving developer experience, ensure a clear, written problem statement exists <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a>. Then, seek out any existing data or signals related to this problem <a class="yt-timestamp" data-t="01:14:53">[01:14:53]</a>. If formal data is scarce, start by talking to developers to understand their daily experiences, the tools they use, and the biggest barriers to their productivity <a class="yt-timestamp" data-t="01:14:30">[01:14:30]</a>.