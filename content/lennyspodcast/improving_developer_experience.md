---
title: Improving Developer Experience
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Improving developer experience (DevEx) is crucial for enhancing overall [[measuring_developer_productivity|developer productivity]] and achieving business outcomes <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Nicole Forsgren, a leading expert in [[measuring_developer_productivity|developer productivity]] and strategy at Microsoft Research, emphasizes that many companies face challenges in clearly defining their goals related to developer experience <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Defining Key Concepts
Nicole Forsgren distinguishes between several interconnected terms:

*   **Developer Experience (DevEx)**: Focuses on what it's like to write software, aiming for a predictable, certain, and friction-free process for developers, which contributes to [[measuring_developer_productivity|productivity]] <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Developers are seen as the users in the software development process <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **[[measuring_developer_productivity|Developer Productivity]]**: Measures how much work can be accomplished over time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. A holistic approach includes considering community effects (software as a team sport) and developer well-being to ensure sustainability and reduce burnout <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **DevOps**: Refers to the technical, architectural, and cultural practices, capabilities, and tools that enable faster and more reliable software development and delivery end-to-end <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. It's not a tool chain to be bought, but a set of practices <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

## The Importance of Improvement
While most leaders desire faster, more productive, and happier engineers, many question the necessity or ROI of investing in [[measuring_developer_productivity|developer productivity]] initiatives <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. Historically, there was a common misconception that moving faster would compromise stability; however, research proves the opposite <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

Moving faster by pushing smaller changes more often actually leads to more stable systems, as it reduces blast radius and makes debugging easier <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. Conversely, infrequent changes lead to larger, unstable systems that are harder to debug <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

## Frameworks for Measurement and Improvement

### The Dora Framework
The Dora (DevOps Research and Assessment) framework is widely known for its "Four Keys" or "Four Metrics" for software delivery performance <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. These metrics measure both speed and stability:

*   **Speed Metrics:**
    *   **Lead Time for Changes:** Time from code commit to code running in production <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
    *   **Deployment Frequency:** How often code is deployed <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   **Stability Metrics:**
    *   **Mean Time to Restore (MTTR):** Time to recover from an incident <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
    *   **Change Fail Rate:** Percentage of changes that require human intervention <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

**Key Insight:** Speed and stability move in tandem <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. Moving faster (by deploying smaller changes more frequently) results in more stable systems <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

**Elite Performance Benchmarks (2019, consistent over time):**
*   **Deployment Frequency:** On demand <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>
*   **Lead Time for Changes:** Less than a day <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>
*   **Time to Restore:** Less than an hour <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>
*   **Change Fail Rate:** 0-15% <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>

These benchmarks apply broadly across companies of all sizes, with only retail being an outlier due to market pressures <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

To improve these metrics, focus on a set of capabilities including:
*   **Technical Capabilities:** Automated testing, CI/CD (Continuous Integration/Continuous Deployment), trunk-based development, and effective Version Control Systems <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.
*   **Architectural Practices:** Loosely coupled systems and effective cloud usage <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.
*   **Cultural Capabilities** <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

### The SPACE Framework
SPACE provides a framework for selecting the right metrics for complex, creative work like [[measuring_developer_productivity|developer productivity]] <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>. It stands for five dimensions:

*   **S - Satisfaction and Well-being:** Measures sustainability and correlation with other productivity dimensions <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>. When satisfaction drops, other things break <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.
*   **P - Performance:** The outcome of a process, such as reliability or metrics like MTTR and Change Fail Rate from Dora <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **A - Activity:** Any countable metric, easy to instrument, such as number of pull requests or check-ins <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
*   **C - Communication and Collaboration:** How people work and talk together, including meetings, or even system communication and code base searchability <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.
*   **E - Efficiency and Flow:** The flow through the system, time through the system, or number of hops a ticket takes <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

To use SPACE correctly, aim to measure at least three dimensions at a time to ensure balance and avoid unintended consequences <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. Dora's four metrics can be seen as an implementation of SPACE <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.

## Practical Steps for Improvement

### Starting from Nothing
1.  **Define the Problem/Goal:** Be "super, super crisp" on what you are trying to achieve <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>. Many teams struggle with this clarity, leading to misaligned efforts <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a>.
2.  **Seek Data and Signals:** Look for any existing data or signals related to the problem, even if loosely defined <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.
3.  **Gather Data from People:** When starting out, rely more on qualitative data from people (e.g., surveys, interviews) as it's quicker to obtain <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. Don't discount what people say, as they can provide insights systems cannot <a class="yt-timestamp" data-t="00:36:07">[00:36:07]</a>.

### Incorporating Data
*   **Combine Qualitative and Quantitative Data:** Data from people and systems are crucial complements <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>. Surveys provide insights into "heroics" or code not in version control, which system data would miss <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a>.
*   **Periodic Surveys:** For satisfaction metrics, conduct surveys periodically (e.g., once every few months or annually) <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>.

### Common Pitfalls to Avoid
*   **Lack of Clarity:** Not having a clear understanding of the problem or objective <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
*   **One-Sided Approach:** Failing to pursue improvements with both top-down and bottom-up buy-in <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>. Effective communication with both individual contributors and leadership is essential <a class="yt-timestamp" data-t="00:46:22">[00:46:22]</a>.

### Nicole Forsgren's Tools for Clarity
*   **The Four Box Framework:** This framework helps in clarifying hypotheses and measurement:
    1.  Draw four boxes: two on top (for "words") and two on the bottom (for "data") <a class="yt-timestamp" data-t="00:58:07">[00:58:07]</a>.
    2.  Start with "words" at the top: Define the concepts you want to relate (e.g., "customer satisfaction" leads to "return customers") <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>. Validate these concepts with stakeholders <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>.
    3.  Move to "data" at the bottom: Identify the specific metrics that will measure each concept (e.g., "csat score" for customer satisfaction, "website return customers" for return customers) <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.
    4.  Analyze correlations. If results are unexpected, it allows for targeted review: Was the data poor quality? Was the proxy bad? Or was the initial hypothesis flawed? <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>.

*   **Decision-Making Spreadsheet:** For important decisions, personal or business:
    1.  Outline all available options <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>.
    2.  Identify the criteria important to you (e.g., total compensation, prestige, work-life balance) <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>. Often, just identifying criteria clarifies the decision <a class="yt-timestamp" data-t="01:06:16">[01:06:16]</a>.
    3.  Assign a relative weight (adding up to 100%) to each criterion based on its importance <a class="yt-timestamp" data-t="01:06:34">[01:06:34]</a>.
    4.  Score each option against each criterion and multiply by the weight. This provides a data-informed, not necessarily data-driven, choice <a class="yt-timestamp" data-t="01:06:47">[01:06:47]</a>.

## The Evolving Landscape of Developer Experience

The field of [[measuring_developer_productivity|developer productivity]] has seen significant changes due to:
*   **Increased System Complexity:** Companies now operate larger, more complex systems <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>.
*   **Developer Shortage:** A perceived shortage of developers <a class="yt-timestamp" data-t="00:48:11">[00:48:11]</a>.
*   **Technology-Driven Companies:** More companies recognize themselves as technology-driven, prioritizing software development <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>.

### The [[role_of_ai_in_developer_productivity|Role of AI]]
The rise of [[aipowered_software_development|AI]] has "poured gas" on the need for effective developer experience <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a>. It's no longer just about *what* you build, but creating novel experiences at unprecedented speeds <a class="yt-timestamp" data-t="00:49:21">[00:49:21]</a>. This requires a fast, safe, and reliable software pipeline <a class="yt-timestamp" data-t="00:49:38">[00:49:38]</a>.

[[aipowered_software_development|AI]] tools like GitHub Copilot are shifting how developers work:
*   More time is spent **reviewing code** than writing it <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>.
*   Cognitive load and expected friction models are changing <a class="yt-timestamp" data-t="00:53:09">[00:53:09]</a>.
*   New questions arise around trust, reliability, and potential over-reliance on [[aipowered_software_development|AI]] <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>.
*   [[aipowered_software_development|AI]] can free up cognitive space for developers to tackle harder tasks <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>.

The definition of [[measuring_developer_productivity|productivity]] itself is evolving in the [[aipowered_software_development|AI]] era <a class="yt-timestamp" data-t="00:53:29">[00:53:29]</a>.

## Resources

*   **Dora.dev:** The official website for Dora research, providing updated reports and a quick check tool to benchmark your organization's performance and identify potential constraints <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.
*   **Accelerate by Nicole Forsgren:** An award-winning book detailing the initial Dora research and capabilities <a class="yt-timestamp" data-t="00:57:58">[00:57:58]</a>.
*   **The SPACE Paper:** Provides a detailed outline of the SPACE framework with examples of metrics across categories <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.
*   **Paper on Data from People and Systems (with Mick Kirsten):** Discusses the importance of combining qualitative and quantitative data for comprehensive insights <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>.
*   **How to Measure Anything by Douglas Hubbard:** A book that offers methods for measuring intangibles, even when starting with no data <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.
*   **Nicole Forsgren's Upcoming Book:** Will cover starting measurement from nothing, the measurement journey, trade-offs between subjective and objective data, and practical examples like interview and survey scripts <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>.

## Final Tactical Advice
*   **Clarify Your Objectives:** Ensure your team's goals for [[measuring_developer_productivity|developer productivity]] or [[improving_user_activation_and_onboarding_experiences|developer experience]] are clearly written down and understood <a class="yt-timestamp" data-t="01:14:20">[01:14:20]</a>.
*   **Check Existing Data/Efforts:** Identify any current data or ongoing efforts related to these goals <a class="yt-timestamp" data-t="01:14:27">[01:14:27]</a>.
*   **Talk to Developers:** If no clear data exists, speak directly with developers to understand their feelings about work tools, processes, and the biggest barriers to their [[measuring_developer_productivity|productivity]] <a class="yt-timestamp" data-t="01:14:30">[01:14:30]</a>.