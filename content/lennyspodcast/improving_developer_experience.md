---
title: Improving developer experience
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

[[measuring_developer_productivity | Improving developer experience]] (DevEx) is a crucial area of focus for software development teams, aiming to optimize the environment and tools that engineers use to build and deliver software <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. It is distinct from developer productivity but closely related, as a good experience contributes significantly to how much work can be accomplished over time <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

## Defining Developer Experience

Developer experience focuses on "what it's like to write software," aiming for a friction-free, predictable, and certain process <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a> <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. It's about recognizing developers as users of internal tools and systems within the software development process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Relationship with Developer Productivity and DevOps
*   **Developer Productivity** is defined as how much work can be completed over time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It requires a holistic measure, including community effects (software as a team sport) and well-being, as these contribute to sustainability and reduce burnout <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a> <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **DevOps** refers to the capabilities, tools, and processes used to [[improving_user_experience_and_product_quality | improve software development and delivery]] end-to-end, making it faster and more reliable <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a> <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. It encompasses technical, architectural, and cultural practices that enable better work, leading to increased productivity and a better developer experience <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a> <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## Challenges and Importance

While leaders universally desire faster, more productive, and happier engineers <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, a significant challenge lies in clearly defining the problem or goal <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Up to 80% of teams struggle with this, leading to uncertainty even at executive levels <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Without clear definitions (e.g., is "improving developer experience" about inner/outer loop, friction, or culture?), teams can head in "completely different directions" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a> <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

Another challenge is overcoming skepticism regarding the return on investment (ROI) and potential instability when moving faster <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Historical common knowledge, like requiring two-week waits for change approvals for stability, has been disproven <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a> <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. In fact, shipping smaller, more frequent changes leads to *more* stability, not less <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a> <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.

## Frameworks for Measurement and Improvement

### The Dora Framework (Four Keys)

The Dora (DevOps Research and Assessment) research program became known for its four key metrics for software delivery performance <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a> <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. These metrics include two for speed and two for stability:

*   **Speed Metrics:**
    *   **Lead Time for Changes:** How long it takes to get from code committed to code running in production <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   **Deployment Frequency:** How often code is deployed <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   **Stability Metrics:**
    *   **Meantime to Restore (MTTR):** How long it takes to recover if something goes wrong <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
    *   **Change Fail Rate:** The percentage of changes that result in an incident or require human intervention <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

A key finding of Dora research is that **speed and stability move in tandem** <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a> <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. Moving faster (by pushing smaller, more frequent changes) leads to more stable systems, as it reduces the blast radius of errors and makes debugging easier <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a> <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. Conversely, less frequent, larger batch changes lead to more unstable systems and make disentangling bugs difficult <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a> <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

Benchmarks for Elite Performers (as of 2019, consistent over time):
*   **Deployment Frequency:** On demand <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
*   **Lead Time for Changes:** Less than a day <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
*   **Time to Restore:** Less than an hour <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
*   **Change Fail Rate:** Between 0-15% <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

These benchmarks apply across companies of all sizes; large companies often have more complex codebases, while small companies have fewer resources, balancing each other out <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a> <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. Retail is an outlier, performing better due to intense market pressures that selected for high-performing organizations <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a> <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.

The most important aspect of these metrics is knowing your current state and making progress, rather than solely focusing on elite benchmarks <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a> <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. To improve, teams should implement DevOps capabilities, including technical practices (e.g., automated testing, CI/CD, trunk-based development, Version Control System use), architectural practices (e.g., loosely coupled systems, effective cloud utilization), and a positive culture <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a> <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

### The SPACE Framework

SPACE is a framework designed to measure complex, creative work, including [[measuring_developer_productivity | developer productivity]] and [[improving_product_management_skills | incident management]] <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a> <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>. It provides a structure for selecting the right metrics within a given context <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. SPACE stands for five dimensions:

*   **S - Satisfaction and Well-being:** Measures how satisfied and sustainable developers are in their work. This dimension is highly correlated with other productivity aspects and acts as an important signal for potential issues <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a> <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **P - Performance:** Focuses on the outcomes of a process, such as reliability or metrics like Mean Time to Restore (MTTR) and Change Fail Rate from Dora <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a> <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>.
*   **A - Activity:** Refers to counts or numbers of things, easily instrumented and automated (e.g., number of pull requests, check-ins) <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a> <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>.
*   **C - Communication and Collaboration:** Measures how people work and talk together, including meetings, collaboration, or even the searchability of a codebase <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.
*   **E - Efficiency and Flow:** Tracks the flow through a system, such as time taken for a process (e.g., lead time for changes) or number of hops for a ticket <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

To use SPACE correctly, it's recommended to select metrics from at least three dimensions to ensure balance and avoid unintended consequences <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a> <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>. For example, when improving pull requests, balance activity (number of alerts) with efficiency (time to work on coding) and satisfaction (satisfaction with PR process) <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a> <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>. Avoid single, misleading metrics like lines of code <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.

### The Four Box Framework

This framework helps in clearly defining what to measure and test <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>:
1.  **Start with "Words":** Define the hypothesis or relationship you want to test using clear language. For example, "customer satisfaction gets us more money" <a class="yt-timestamp" data-t="00:58:26">[00:58:26]</a> <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>.
2.  **Translate to "Data":** For each "word" box, define the specific data points that will measure it. For customer satisfaction, this could be a CSAT or NPS score <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a> <a class="yt-timestamp" data-t="01:00:16">[01:00:16]</a>.
3.  **Validate:** Share your "words" with stakeholders to ensure alignment on goals before diving into data <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>.
4.  **Analyze and Iterate:** Run correlations or analyses. If the results don't align, investigate whether the data quality is poor, the proxies are bad, or the initial "words" (hypothesis) need revisiting <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a> <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.

This framework is useful for communicating ideas quickly and ensuring clear alignment on measurement goals <a class="yt-timestamp" data-t="01:01:56">[01:01:56]</a>.

## Tactical Advice for Improvement

*   **Define Goals Clearly:** Start by being "super super crisp" on what problem or goal you are trying to solve <a class="yt-timestamp" data-t="00:41:53">[00:41:53]</a> <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>.
*   **Ship Smaller, More Often:** This is a core principle for both speed and stability <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a> <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   **Implement Good Practices:**
    *   **Technical:** Automated testing, CI/CD, trunk-based development, and effective use of Version Control Systems <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.
    *   **Architectural:** Loosely coupled systems and appropriate cloud utilization <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.
*   **Gather Diverse Data:** Combine qualitative data from people (surveys, interviews) with quantitative data from systems <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a> <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. People provide insights systems cannot, such as understanding "heroics" behind speed or code not in version control <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a> <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **Balance Top-down and Bottom-up:** Drive success by pursuing initiatives from both leadership and individual contributors <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.
*   [[improving_communication_in_teams | Improve Communication]]: Ensure good communication throughout the organization, tailoring language to different audiences (e.g., ICs vs. leaders) <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a> <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.
*   **Start Small with Measurement:** If starting from nothing, identify a clear problem, look for any related data/signal, and interview a few developers about their tools, processes, and barriers to productivity <a class="yt-timestamp" data-t="00:54:22">[00:54:22]</a> <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>.

## [[common_pitfalls_in_enhancing_developer_productivity_systems | Common Pitfalls]]

1.  **Lack of Clarity:** Not clearly understanding or defining what is being looked for, leading to scattered efforts <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>.
2.  **Unilateral Approach:** Not pursuing changes with both top-down and bottom-up engagement <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.
3.  **Poor Communication:** Failing to communicate effectively with individual contributors (ICs) and leadership, or using vocabulary that doesn't resonate with them <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a>.

## Impact of [[ai_development_and_model_improvement | AI Development and Model Improvement]]

The rise of [[innovations_in_code_editors_and_ides | AI-enabled tools]] like GitHub Copilot has accelerated the need for better DevEx <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. It has intensified the focus on execution and the ability to create "absolutely novel, incredibly new experiences" at unprecedented speeds <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>.

AI fundamentally shifts how developers work, moving from primarily writing code to spending more time reviewing it <a class="yt-timestamp" data-t="00:51:42">[00:51:42]</a> <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>. This change introduces new considerations for [[measuring_developer_productivity | productivity]]:
*   **Cognitive Load and Friction:** AI changes expected friction and cognitive load <a class="yt-timestamp" data-t="00:53:13">[00:53:13]</a>.
*   **Trust and Over-reliance:** A new dimension like "trust" or "reliability" may need to be added to frameworks like SPACE <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.
*   **Learning and Skill Development:** How AI impacts learning for novices versus experts, and onboarding to new codebases or languages, is an open question <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a> <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.

The goal is not to cut task time in half to lay off engineers, but to free up cognitive space for developers to tackle harder, more novel challenges <a class="yt-timestamp" data-t="00:52:45">[00:52:45]</a> <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

## Noteworthy Examples and Resources

*   **Google:** Known for its systematic, data-informed approach to [[measuring_developer_productivity | developer experience]] and its investments in Telemetry, tooling, and developer experience surveys <a class="yt-timestamp" data-t="00:55:38">[00:55:38]</a>. Notably, when survey data conflicts with advanced instrumentation, surveys are almost always correct <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.
*   **Dora.dev:** The official website for Dora metrics and benchmarks, offering a "quick check" tool to assess a team's performance profile and identify potential constraints <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.
*   **Books:**
    *   *Accelerate* by Nicole Forsgren et al. <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
    *   *How to Measure Anything* by Douglas W. Hubbard <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.
    *   *Good Strategy Bad Strategy* by Richard Rumelt <a class="yt-timestamp" data-t="01:09:11">[01:09:11]</a>.
    *   *Designing Your Life* by Bill Burnett and Dave Evans <a class="yt-timestamp" data-t="01:09:16">[01:09:16]</a>.
    *   *Ender's Game* by Orson Scott Card <a class="yt-timestamp" data-t="01:09:21">[01:09:21]</a>.
*   **Academic Papers:**
    *   The SPACE paper (ACM) <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>.
    *   Paper on using data from people and systems (co-authored with Mick Kirsten, published around 2016-2017) <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.

**Future Work:** Nicole Forsgren is working on a new book covering how to start [[measuring_developer_productivity | measuring developer productivity]] from scratch, the measurement journey (transitioning from subjective data to more objective, scalable system data), and practical examples like interview and survey scripts <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a> <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>. This work aims to be highly accessible, not requiring data science expertise <a class="yt-timestamp" data-t="00:44:22">[00:44:22]</a>.

**Contact Information:** Nicole Forsgren can be reached via Twitter/Bluesky (@NicoleFV) or her website, nicolefv.com <a class="yt-timestamp" data-t="01:15:03">[01:15:03]</a>. She is eager to hear success stories or case studies related to DevEx and measurement journeys <a class="yt-timestamp" data-t="01:15:34">[01:15:34]</a>.