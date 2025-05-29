---
title: Measuring developer productivity
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Measuring and improving developer productivity and experience is a critical aspect for organizations today, as technology increasingly drives business success <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>. This field has evolved significantly, moving from a niche concern to a strategic priority for many companies <a class="yt-timestamp" data-t="00:48:45">[00:48:45]</a>.

## Defining the Problem and Goals

A significant challenge in enhancing developer productivity is clearly defining the problem or goal <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Many teams, even at executive levels, struggle with this clarity, leading to months of work without a cohesive direction <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. For example, a request to "[[improving_developer_experience | improve developer experience]]" can be ambiguous, encompassing inner/outer loop processes, toolchain friction, or even culture, each requiring vastly different approaches <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Misalignment on definitions means teams head in completely different directions <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Core Concepts

Nicole Forsgren, a leading expert in developer productivity research and strategy, emphasizes the distinct yet related concepts within this domain <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>:

*   **Developer Productivity**
    This refers to how much work can be completed over time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. A holistic measure of productivity includes the "community effect" (as software is a team sport) and well-being, as these contribute to sustainability and reduce burnout <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **[[improving_developer_experience | Developer Experience]] (DevEx)**
    Closely tied to productivity, DevEx focuses on the experience of writing software <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The goal is to make the process friction-free, predictable, and certain, which directly contributes to productivity <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **DevOps**
    DevOps refers to the capabilities, tools, and processes used to improve end-to-end software development and delivery, making it faster and more reliable <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. It's a combination of technical, architectural, and cultural practices that enable better work, leading to higher productivity and a better developer experience <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. DevOps is not a toolchain you buy; it's a set of capabilities and lean management practices <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.

## The Need for Measurement

Most leaders want their engineering teams to move faster, be more productive, and ship quicker <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>. However, there can be resistance or skepticism about the necessity and ROI of such initiatives, often fearing a loss of stability or reliability if speed is prioritized <a class="yt-timestamp" data-t="01:10:57">[01:10:57]</a>. Historically, there was a common misconception that speed meant sacrificing stability, with old practices like two-week waits for change approvals <a class="yt-timestamp" data-t="01:11:19">[01:11:19]</a>.

## The DORA Framework (Four Keys)

The DORA (DevOps Research and Assessment) framework, widely known as the "Four Keys" or "DORA four metrics," provides a quantitative way to measure software delivery performance <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>. It comprises two speed metrics and two stability metrics <a class="yt-timestamp" data-t="01:14:27">[01:14:27]</a>:

1.  **Speed Metrics:**
    *   **Lead Time for Changes:** The time it takes from code commit to code running in production <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a>.
    *   **Deployment Frequency:** How often an organization successfully delivers code to production <a class="yt-timestamp" data-t="01:14:37">[01:14:37]</a>.
2.  **Stability Metrics:**
    *   **Mean Time to Restore (MTTR):** How long it takes to restore service after an incident <a class="yt-timestamp" data-t="01:14:44">[01:14:44]</a>.
    *   **Change Fail Rate:** The percentage of changes to production that result in a degraded service or require remediation <a class="yt-timestamp" data-t="01:14:51">[01:14:51]</a>.

A key finding from DORA research is that **speed and stability move in tandem** <a class="yt-timestamp" data-t="01:15:16">[01:15:16]</a>. Moving faster by pushing smaller changes more often actually leads to more stable systems, as it reduces the blast radius of errors and makes debugging easier <a class="yt-timestamp" data-t="01:15:21">[01:15:21]</a>. Conversely, pushing changes less frequently leads to larger batch changes and more unstable systems <a class="yt-timestamp" data-t="01:15:46">[01:15:46]</a>.

### Elite Performance Benchmarks (2019)

For elite performers, the benchmarks are <a class="yt-timestamp" data-t="01:19:02">[01:19:02]</a>:

*   **Deployment Frequency:** On demand <a class="yt-timestamp" data-t="01:19:33">[01:19:33]</a>.
*   **Lead Time for Changes:** Less than one day <a class="yt-timestamp" data-t="01:19:36">[01:19:36]</a>.
*   **Time to Restore:** Less than one hour <a class="yt-timestamp" data-t="01:19:39">[01:19:39]</a>.
*   **Change Fail Rate:** Between 0-15% <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>.

These benchmarks apply regardless of company size; small and large companies show no statistical significance in their performance categories, with the exception of the retail industry, which often performs better due to market pressures <a class="yt-timestamp" data-t="02:22:56">[02:22:56]</a>.

To improve DORA metrics, organizations should focus on technical capabilities (e.g., automated testing, CI/CD, trunk-based development, version control), architectural practices (e.g., loosely coupled systems, cloud adoption), and fostering a strong culture <a class="yt-timestamp" data-t="02:50:52">[02:50:52]</a>. The dora.dev website provides a "quick check" tool to benchmark performance and identify potential constraints <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

## The SPACE Framework

The SPACE framework is designed to help organizations measure any type of complex creative work, including developer productivity <a class="yt-timestamp" data-t="02:59:22">[02:59:22]</a>. It provides a framework for selecting the right metrics within a specific context and available data <a class="yt-timestamp" data-t="03:00:01">[03:00:01]</a>. SPACE stands for five dimensions <a class="yt-timestamp" data-t="03:00:42">[03:00:42]</a>:

*   **S - Satisfaction and Well-being:** Measures how developers feel about their work, tools, and processes <a class="yt-timestamp" data-t="03:04:53">[03:04:53]</a>. It is highly correlated with other productivity dimensions and can signal problems if it declines <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   **P - Performance:** The outcome of a process, such as reliability or metrics like MTTR and change fail rate from DORA <a class="yt-timestamp" data-t="03:07:22">[03:07:22]</a>.
*   **A - Activity:** Quantity or count of specific actions, often easy to instrument (e.g., number of pull requests, check-ins) <a class="yt-timestamp" data-t="03:11:40">[03:11:40]</a>.
*   **C - Communication and Collaboration:** How people work and talk together, including meetings, or how systems communicate (e.g., code base searchability) <a class="yt-timestamp" data-t="03:14:53">[03:14:53]</a>.
*   **E - Efficiency and Flow:** The flow through the system, such as time taken for a process or the number of hops a ticket takes <a class="yt-timestamp" data-t="03:16:06">[03:16:06]</a>.

To use SPACE correctly, it's recommended to select at least three dimensions to ensure balance and prevent unintended consequences <a class="yt-timestamp" data-t="03:22:24">[03:22:24]</a>. For example, focusing solely on activity metrics like "number of pull requests" can lead to negative outcomes if not balanced with efficiency and satisfaction metrics <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>.

Measurement methods can include both qualitative (e.g., surveys for satisfaction) <a class="yt-timestamp" data-t="03:55:53">[03:55:53]</a> and quantitative (e.g., system data for activity, performance) insights <a class="yt-timestamp" data-t="04:00:56">[04:00:56]</a>. Both are crucial complements, as system data alone cannot capture heroics or hidden processes, while qualitative data reveals the "why" behind the numbers <a class="yt-timestamp" data-t="04:07:59">[04:07:59]</a>.

## Common Pitfalls in [[common_pitfalls_in_enhancing_developer_productivity_systems | Enhancing Developer Productivity Systems]]

*   **Lack of Clear Objectives:** Not clearly defining or understanding what the organization is looking for, leading to scattered efforts <a class="yt-timestamp" data-t="04:53:23">[04:53:23]</a>.
*   **Missing Top-Down and Bottom-Up Approaches:** Failure to pursue initiatives with both leadership buy-in and input from individual contributors (ICs), ensuring good communication throughout <a class="yt-timestamp" data-t="04:58:24">[04:58:24]</a>.
*   **Poor Communication:** Not effectively communicating the purpose and value of productivity initiatives to both developers and leadership <a class="yt-timestamp" data-t="05:15:37">[05:15:37]</a>.

## Evolution of the Field and Impact of AI

The landscape of developer productivity has changed dramatically <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>:
*   **Increasingly Large and Complex Systems:** Modern internet-driven companies necessitate robust technology <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.
*   **Developer Shortage:** A perceived scarcity of developers highlights the importance of efficiency <a class="yt-timestamp" data-t="05:02:17">[05:02:17]</a>.
*   **Technology-Driven Companies:** Most companies now recognize themselves as technology companies <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
*   **AI Moment:** The rise of AI, particularly tools like GitHub Copilot, has poured "gas on top of everything" <a class="yt-timestamp" data-t="05:06:50">[05:06:50]</a>. AI shifts the focus from simply building features to creating novel, new experiences at unprecedented speed <a class="yt-timestamp" data-t="05:07:50">[05:07:50]</a>. It changes the way developers work, often leading to more time spent reviewing code than writing it <a class="yt-timestamp" data-t="05:19:55">[05:19:55]</a>. While AI can make tasks faster, its true value lies in freeing up cognitive space for harder tasks and changing the mental models of development <a class="yt-timestamp" data-t="05:28:50">[05:28:50]</a>.

## Tactical Advice for Getting Started

To begin improving developer productivity, a leader should <a class="yt-timestamp" data-t="05:40:40">[05:40:40]</a>:

1.  **Clearly Define the Problem:** Ensure the challenge or goal is written down and crystal clear <a class="yt-timestamp" data-t="05:41:53">[05:41:53]</a>.
2.  **Seek Data or Signals:** Look for any existing data or signals related to the problem, even if loosely defined <a class="yt-timestamp" data-t="05:49:53">[05:49:53]</a>.
3.  **Talk to Developers:** Engage with a handful of developers to understand how they feel about their work tools and processes, and what the biggest barriers to their productivity are <a class="yt-timestamp" data-t="05:54:38">[05:54:38]</a>.

## The Four-Box Framework

This framework helps clarify hypotheses and measurement strategies <a class="yt-timestamp" data-t="05:57:51">[05:57:51]</a>:

*   Draw four boxes: two on top, two on bottom.
*   Label the left side "Words" and the bottom side "Data" <a class="yt-timestamp" data-t="05:58:26">[05:58:26]</a>.
*   **Top (Words):** Start by articulating your hypothesis or suspected relationship in words. For example, "Customer satisfaction leads to return customers" <a class="yt-timestamp" data-t="05:58:49">[05:58:49]</a>. Validate this with stakeholders <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>.
*   **Bottom (Data):** Define how you will measure each concept from the "Words" boxes. For "customer satisfaction," this could be a CSAT score or NPS; for "return customers," it could be website data <a class="yt-timestamp" data-t="06:07:08">[06:07:08]</a>.
*   **Analysis:** Analyze the correlation between the data points. If the results are unexpected, the framework helps pinpoint where the problem lies: was the data quality poor, was it a bad proxy, or was the initial "words" hypothesis incorrect <a class="yt-timestamp" data-t="06:16:06">[06:16:06]</a>?

This framework prevents blaming individuals and provides a clear structure for evaluating initiatives, ensuring that the "words" (hypothesis) and "data" (measurement) are aligned <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

## [[strategies_for_measuring_product_success | General Advice for Decision Making]]

For effective decision-making, whether in business or personal life <a class="yt-timestamp" data-t="06:28:26">[06:28:26]</a>:

1.  **Define Objectives and Criteria:** Be clear about what you want to achieve and what factors are important <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>.
2.  **Weight Criteria:** Assign relative importance to each criterion, summing to 100% <a class="yt-timestamp" data-t="06:44:40">[06:44:40]</a>.
3.  **Data-Informed Approach:** Use data to score options against criteria, then multiply by weights <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>. This provides a data-informed, rather than purely data-driven, perspective, allowing for human judgment <a class="yt-timestamp" data-t="06:53:50">[06:53:50]</a>.
4.  **Prioritization:** A good strategy means knowing what *not* to do, as funding everything leads to failure <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.

## Resources

*   **Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations** by Nicole Forsgren, Jez Humble, and Gene Kim <a class="yt-timestamp" data-t="02:57:58">[02:57:58]</a>
*   **dora.dev**: Website with DORA reports and quick check tool <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>
*   **SPACE Paper**: Available at ACM, provides framework details and metric examples <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>
*   **"How to Measure Anything"** by Douglas W. Hubbard: A book on uncovering intangibles and starting measurement from nothing <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>
*   **Nicole Forsgren's website**: nicolefe.com for contact information and future updates on her new book <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.
*   **DX.com**: A platform for measuring and [[improving_developer_experience | improving developer productivity]] based on research by Nicole Forsgren and others <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.