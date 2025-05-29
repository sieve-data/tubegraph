---
title: Understanding and improving developer experience
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

[[developer_productivity_improvement | Developer experience]] (DX) is a critical area of focus for organizations aiming to improve software development and delivery. It is closely related to [[developer_productivity_improvement | developer productivity]] and DevOps practices, with successful implementation leading to faster delivery, higher quality, and increased developer well-being <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Defining Developer Experience

[[developer_productivity_improvement | Productivity]] is fundamentally about how much work can be completed over time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It necessitates a holistic approach that incorporates elements like community effect, as software development is a team effort, and well-being, which leads to sustainability and reduced burnout <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

[[improving_user_experience_through_customer_feedback | Developer experience]] is closely tied to [[developer_productivity_improvement | productivity]] and contributes to it <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Thinking of developers as users within the software development process, [[improving_user_experience_through_customer_feedback | developer experience]] focuses on the ease and predictability of writing software, aiming to reduce friction and uncertainty <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

DevOps, in Nicole Forsgren's view, refers to the technical, architectural, and cultural practices used to enhance end-to-end software development and delivery, making it faster and more reliable <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. These practices enable greater [[developer_productivity_improvement | productivity]] and a better [[improving_user_experience_through_customer_feedback | developer experience]] <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## The Challenge of Defining Goals

A significant challenge, even at executive levels, is clearly defining the problem or goal <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Teams might spend months working on vague directives like "improve [[improving_user_experience_through_customer_feedback | developer experience]]" without a clear understanding of what that entails—whether it's about inner/outer loops, toolchain friction, or culture. This lack of clarity can lead teams in completely different directions <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Measuring Developer Experience and Productivity

### The DORA Framework (DevOps Research and Assessment)

The DORA research program is best known for its four key metrics, also known as the "Four Keys," which measure software delivery performance <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>:

*   **Speed Metrics:**
    *   **Lead Time:** Time from code commit to code running in production <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   **Deployment Frequency:** How often code is deployed <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   **Stability Metrics:**
    *   **Mean Time To Restore (MTTR):** Time to recover from an incident <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
    *   **Change Fail Rate:** Percentage of changes that result in incidents requiring human intervention <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

A key finding from DORA research is that speed and stability move in tandem <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Moving faster (e.g., by pushing smaller changes more often) leads to more stable systems, as it reduces the blast radius of errors and makes debugging easier <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. Conversely, less frequent deployments lead to larger batch changes and more unstable systems <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. This debunks old beliefs, such as the necessity of a two-week wait for change approvals, which actually cause batching and instability <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

#### DORA Benchmarks (2019 data, generally consistent):

*   **Elite Performance:**
    *   Deployment Frequency: On demand (multiple times a day) <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.
    *   Lead Time for Changes: Less than one day <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
    *   Time to Restore: Less than one hour <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.
    *   Change Fail Rate: Between 0-15% <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
*   **High Performance:** Lead Time for Changes is between a day and a week <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

These benchmarks are broadly applicable across company sizes, with no significant statistical difference between small and large companies, except for retail, which tends to be better due to market pressures <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. The most important aspect is knowing your current state and making progress, rather than solely aiming for elite status <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

More information and a quick check tool are available at [dora.dev](http://dora.dev/) <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### The SPACE Framework

The SPACE framework provides a structured approach to measuring complex, creative work, including [[improving_user_experience_through_customer_feedback | developer productivity]] <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. It outlines five dimensions for measurement:

*   **S - Satisfaction and Wellbeing:** Measures aspects like job satisfaction and sustainability <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. This dimension is highly correlated with other [[developer_productivity_improvement | productivity]] dimensions and acts as an early signal for potential issues <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.
*   **P - Performance:** Focuses on the outcomes of a process, such as reliability, or Dora metrics like MTTR and Change Fail Rate <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **A - Activity:** Involves counting measurable actions, like the number of pull requests or check-ins <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. These are often easy to instrument and automate <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.
*   **C - Communication and Collaboration:** Assesses how people interact and work together (e.g., meetings, collaboration) or how systems communicate (e.g., code base searchability) <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.
*   **E - Efficiency and Flow:** Measures the time taken to move through a system, such as time for feature delivery or the number of hops a ticket takes <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

To use SPACE effectively, it's recommended to measure at least three dimensions simultaneously to ensure balance and prevent unintended consequences <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>. The DORA metrics are considered an implementation of the SPACE framework <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.

When measuring, it's crucial to combine both qualitative (from people) and quantitative (from systems) data <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>. Surveys are valuable for capturing developer satisfaction and understanding insights not available from system data, such as whether achieving speed requires "heroics" or if critical code isn't even in version control <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a>.

### The Four Box Framework

This framework helps clarify hypotheses and measurement strategies <a class="yt-timestamp" data-t="00:57:48">[00:57:48]</a>:

1.  **Top Left Box (Words):** State your initial hypothesis or what you want to measure (e.g., "Customer satisfaction").
2.  **Top Right Box (Words):** State the expected outcome (e.g., "Return customers"). Draw an arrow connecting the two word boxes <a class="yt-timestamp" data-t="00:58:23">[00:58:23]</a>.
3.  **Bottom Left Box (Data):** Define how you will measure the first concept (e.g., "CSAT score" or "NPS") <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>.
4.  **Bottom Right Box (Data):** Define how you will measure the outcome (e.g., "Returned customers as measured through website" or "Referral links") <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>. Draw an arrow connecting the two data boxes <a class="yt-timestamp" data-t="00:58:42">[00:58:42]</a>.

Always start with the "words" boxes to ensure clarity and agreement on the problem or goal <a class="yt-timestamp" data-t="00:59:18">[00:59:18]</a>. If data analysis doesn't support the hypothesis, this framework helps pinpoint whether the issue lies in the data quality, the chosen metrics (proxies), or the initial hypothesis itself <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>.

## Improving Developer Experience

### Key Practices for Improvement

*   **Technical Capabilities:** Implement practices such as automated testing, continuous integration/continuous deployment (CI/CD), trunk-based development, and effective use of Version Control Systems <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>.
*   **Architectural Practices:** Utilize loosely coupled systems and leverage cloud computing effectively (or underlying architectural pieces if not fully in the cloud) <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.
*   **Cultural Practices:** Foster a supportive culture that enables faster, more reliable software delivery <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

These practices, when combined, lead to improved speed and stability, ultimately contributing to business value through faster feature creation <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.

### Common Pitfalls to Avoid

*   **Lack of Clarity on Goals:** Not having a clear understanding of what "improvement" means can lead to scattered efforts <a class="yt-timestamp" data-t="00:45:57">[00:45:57]</a>.
*   **Lack of Top-Down and Bottom-Up Approach:** Success requires both leadership buy-in and engagement from individual contributors <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.
*   **Poor Communication:** Not communicating effectively with both engineers (using their vocabulary) and leaders (aligning with their motivations and priorities) <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a>. Leaders need to understand the business case and ROI for investing in DX <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### The Impact of AI on Software Development

[[ais_impact_on_software_development | AI's impact on software development]] is a significant "AI moment" that is accelerating discussions around [[developer_productivity_improvement | developer productivity]] <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. It emphasizes that execution, rather than just ideas, is paramount, and it requires creating novel experiences at unprecedented speeds <a class="yt-timestamp" data-t="00:49:13">[00:49:13]</a>. This necessitates a fast, safe, stable, and reliable software pipeline <a class="yt-timestamp" data-t="00:49:38">[00:49:38]</a>.

AI tools like GitHub Copilot fundamentally shift how developers work, moving from primarily writing code to spending more time reviewing it <a class="yt-timestamp" data-t="00:51:42">[00:51:42]</a>. While AI can make certain tasks (like building an HTTP server) 50% faster, the true benefit is in freeing up cognitive space for engineers to tackle more complex problems <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>. This shift impacts mental models, friction, cognitive load, and raises questions about reliance, learning, and how to measure [[developer_productivity_improvement | productivity]] in a new context <a class="yt-timestamp" data-t="00:53:06">[00:53:06]</a>.

## Getting Started: Tactical Advice

1.  **Define the Problem Clearly:** Start by asking: "What is your problem or what is your goal?" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Ensure it's written down and crystal clear to avoid confusion and misaligned efforts <a class="yt-timestamp" data-t="00:41:53">[00:41:53]</a>.
2.  **Find Related Data or Signal:** Look for any existing data, even loosely defined, that relates to the identified problem <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.
3.  **Talk to Developers:** If no data exists, directly ask developers how they feel about their work, tools, processes, and the biggest barriers to their [[developer_productivity_improvement | productivity]] <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. This can be done through interviews or surveys <a class="yt-timestamp" data-t="00:35:43">[00:35:43]</a>.
4.  **Embrace Incremental Measurement:** When starting from nothing, rely more on data from people initially, then gradually transition to more scalable system data as instrumentation is built out <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>. Don't let the perfect be the enemy of the good <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>.

## Resources

*   **Book:** *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim. This book compiles and expands on the initial DORA research <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
*   **Website:** [dora.dev](http://dora.dev/) for DORA reports, quick checks, and deep dives into capabilities <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.
*   **Research Paper:** The SPACE paper (available at ACM) provides details on the framework and examples of metrics <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.
*   **Book:** *How to Measure Anything* by Douglas W. Hubbard, useful for understanding how to measure intangibles when starting with no data <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.
*   **DX Platform:** DX is a platform designed by researchers behind DORA and SPACE, including Nicole Forsgren, to measure and improve [[developer_productivity_improvement | developer productivity]] by combining qualitative and quantitative insights <a class="yt-timestamp" data-t="01:13:58">[01:13:58]</a>.

Nicole Forsgren is currently working on a new book that will delve into defining problems, starting measurement from scratch, the measurement journey (subjective vs. objective data), and providing practical examples like interview and survey scripts <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>.

## The Future of Engineering

Over the past 10-15 years, companies have become increasingly technology-driven, realizing the necessity of improving their tech capabilities <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>. This, combined with increasingly large and complex systems and a perceived shortage of developers, has put pressure on organizations to prioritize [[developer_productivity_improvement | developer productivity]] and experience <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>. The advent of AI has intensified this, making the ability to execute quickly and safely paramount <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. The discussion has shifted to how to create absolutely novel, new experiences at unprecedented speeds, which hinges on having a fast, safe, stable, and reliable software pipeline <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>. This aligns with [[the_future_of_engineering_and_code_development | the future of engineering and code development]].