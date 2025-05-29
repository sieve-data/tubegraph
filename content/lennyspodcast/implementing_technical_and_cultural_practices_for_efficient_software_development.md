---
title: Implementing technical and cultural practices for efficient software development
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

Nicole Forsgren, a recognized expert in [[developer_productivity_improvement | developer productivity]], emphasizes that defining the core problem or goal is often the biggest challenge for organizations seeking to improve their software development processes. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> Even at executive levels, teams may spend months on initiatives like [[understanding_and_improving_developer_experience | improving developer experience]] only to return with uncertainty due to a lack of clarity on what that means (e.g., inner/outer loop, friction, or [[understanding_company_cultures_impact_on_product_development | culture]]). <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> Different interpretations can lead teams in completely different directions. <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>

Forsgren is the author of the book "Accelerate" and a co-author of the "State of DevOps Report." <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> She is currently a partner at Microsoft Research, leading developer productivity research and strategy, and has assisted major companies in achieving faster delivery, improved product quality, and cultural transformation. <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>

## Understanding Key Terms: Productivity, Experience, and DevOps
Nicole Forsgren clarifies the distinctions between related concepts:
*   **Productivity** refers to how much can be accomplished over time, emphasizing a holistic measure that includes community effects and well-being. <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a> When done correctly, it promotes sustainability and reduces burnout. <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>
*   **[[understanding_and_improving_developer_experience | Developer experience]] (DevEx)** contributes to productivity by focusing on what it's like to write software, aiming for a friction-free, predictable, and certain process. <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>
*   **DevOps** encompasses the capabilities, tools, and processes used to improve end-to-end software development and delivery, making it faster and more reliable. <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a> DevOps is a set of technical, architectural, and cultural practices that enable better work, leading to increased productivity and an improved developer experience. <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>

While leaders universally desire faster development, higher productivity, and happier engineers, there's often hesitation regarding the investment required or concerns about potential instability from increased speed. <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> Historically, it was common belief that a two-week wait for change approvals was necessary for stability, a notion that has since been disproven. <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>

## Measuring Performance with the DORA Framework
The DORA (DevOps Research and Assessment) framework, particularly known for its "Four Keys" or "Four Metrics," measures software delivery performance. <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>

### The Four Keys
1.  **Lead Time for Changes**: How long it takes to get from code committed to code running in production. <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>
2.  **Deployment Frequency**: How often code is deployed. <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>
3.  **Mean Time to Restore (MTTR)**: How long it takes to restore service if something goes wrong. <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>
4.  **Change Fail Rate**: The percentage of changes pushed that require human intervention due to incidents. <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>

### Speed and Stability Move Together
A significant finding from DORA research is that speed and stability move in tandem. <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>
*   When teams move faster, they are more stable because they push smaller, more frequent changes, resulting in a smaller "blast radius" for errors and easier debugging. <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>
*   Conversely, pushing changes less frequently leads to larger batch changes, higher blast radii, and more unstable systems that are harder to disentangle and fix when bugs occur. <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a> Forcing long pauses for change approvals causes batching, leading to merge conflicts and significant challenges in pushing code to production. <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>

[!INFO] **Key Takeaway**: To [[balancing_speed_and_quality_in_software_development | move faster and improve quality]], teams should ship smaller things and deploy more often. <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a> This approach is much safer. <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>

### Benchmarks
DORA provides benchmarks for low, medium, high, and Elite performers. While absolute precision isn't crucial, knowing your general category and making progress is vital. <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>

**Elite Performance Benchmarks (as of 2019, remain consistent):**
*   **Deployment Frequency**: On demand (multiple times a day). <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>
*   **Lead Time for Changes**: Less than one day. <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>
*   **Time to Restore Service**: Less than one hour. <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>
*   **Change Fail Rate**: Between 0% and 15%. <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>

These benchmarks apply broadly across companies of all sizes, with no significant statistical difference between small and large organizations, except for retail, which tends to perform better due to market pressures. <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>

## The SPACE Framework for Comprehensive Measurement
The SPACE framework helps measure productivity for complex, creative work, including developer productivity and incident management. <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a> It provides a framework to select appropriate metrics within a given context and available data. <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>

SPACE stands for five dimensions:
*   **S - Satisfaction and Well-being**: Includes sustainability, burnout, and overall job satisfaction. This dimension is highly correlated with other productivity metrics and serves as an important signal for potential issues. <a class="yt-timestamp" data-t="00:30:47">[00:30:47]</a>
*   **P - Performance**: Outcomes of a process, such as reliability (e.g., MTTR, change fail rate from DORA). <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>
*   **A - Activity**: Counts or numbers of actions, easy to instrument (e.g., number of pull requests, check-ins). <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>
*   **C - Communication and Collaboration**: How people work and talk together (meetings, searchability of codebase, system communication). <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>
*   **E - Efficiency and Flow**: Flow through the system (e.g., time through system, number of hops a ticket takes). <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>

### Using SPACE Effectively
To use SPACE correctly, aim to measure at least three dimensions simultaneously to ensure balance. <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a> DORA's Four Keys, for example, are an implementation of SPACE focusing on the outer loop. <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a> Avoid relying solely on activity metrics like "number of lines of code" or "number of commits," as these can be misleading and do not provide a balanced view. <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>

[Comment]: I need to remember to link to "Understanding work for product development" and "Building a product-oriented engineering culture" where possible, specifically when talking about "culture" and "work."

Surveys are crucial for capturing satisfaction metrics periodically, as people can provide insights systems cannot (e.g., heroic efforts to achieve speed, or code not in version control). <a class="yt-timestamp" data-t="00:35:43">[00:35:43]</a> Data from people and systems are important complements for a holistic understanding. <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>

## [[developer_productivity_improvement | Improving Developer Productivity]] and Experience: Technical and Cultural Practices
Beyond just metrics, DORA research identifies specific capabilities that predict speed and stability, which in turn lead to business value. <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>

### Technical Capabilities
*   Automated testing <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>
*   CI/CD (Continuous Integration, Continuous Deployment) <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>
*   Trunk-based development <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>
*   Using a Version Control System <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>

### Architectural Practices
*   Loosely coupled systems <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>
*   Effective use of cloud technologies (or underlying architectural pieces that enable good cloud practices) <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>

### Cultural Practices
*   Fostering a healthy [[understanding_company_cultures_impact_on_product_development | culture]] that supports high performance. <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>

Organizations can use the quick check tool at dora.dev to plug in their current performance and identify probable constraints based on their industry and profile. <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>

### The Importance of Balanced Metrics
When improving specific areas, like continuous integration or [[understanding_company_cultures_impact_on_product_development | culture]], it's crucial to select balanced metrics that are in tension to avoid unintended consequences. For example, when improving pull request processes, consider:
*   Efficiency/flow (e.g., time to work on coding, code review time). <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>
*   Satisfaction with the process and reviewer selection. <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>
This ensures protecting developer time while also optimizing review processes. <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>

## Common Pitfalls in Implementation
Companies often face challenges when implementing developer productivity systems:
1.  **Lack of Clarity**: Not having a clear understanding or written definition of what they are trying to achieve, leading to scattered efforts. <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>
2.  **Unbalanced Approach**: Failing to pursue improvements with both top-down and bottom-up structures, and lacking consistent communication. <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a> It's important to get individual contributors (ICs) bought in, understand their vocabulary, and communicate effectively with leaders by tying initiatives to their motivations and strategic priorities. <a class="yt-timestamp" data-t="00:46:29">[00:46:29]</a>

## The Impact of AI on Software Development
Over the last decade, companies have become increasingly technology-driven, facing larger, more complex systems and a perceived shortage of developers. <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a> This has pushed the need for better software development practices. <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>

The recent [[ais_impact_on_software_development | AI moment]] has poured "gas on top of everything." <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a> It's no longer just about building features, but about creating novel, new experiences at unprecedented speeds. <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a> This necessitates a fast, safe, stable, and reliable software pipeline. <a class="yt-timestamp" data-t="00:49:38">[00:49:38]</a>

AI tools like GitHub Copilot are already impacting engineering productivity. Developers using these tools fundamentally shift their work, spending more time reviewing code than writing it. <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a> While tasks might be completed faster, the true benefit lies in freeing up cognitive space for developers to tackle harder problems. <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a> AI also changes mental models, expected friction, cognitive load, and reliance on code, raising questions about trust, learning, and how to measure productivity for novices versus experts. <a class="yt-timestamp" data-t="00:53:06">[00:53:06]</a>

[!NOTE] **The future of software development beyond traditional coding**: The future isn't about laying off engineers due to AI; it's about enabling engineers to do more complex, novel work faster. <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>

## Decision-Making with the Four-Box Framework
This framework helps clarify and test hypotheses, making decision-making more structured:
1.  **Top Row (Words)**: Draw two boxes. In the first, write your initial concept (e.g., "customer satisfaction"). In the second, write the expected outcome (e.g., "return customers"). Connect them with an arrow to form a sentence (e.g., "Customer satisfaction leads to return customers"). <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>
2.  **Bottom Row (Data)**: Below each "word" box, draw a corresponding "data" box. In these, define how you will measure each concept (e.g., customer satisfaction by "CSAT score," return customers by "website returns"). <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>

Always start with "words" to gain alignment from stakeholders before moving to data. If the data analysis (e.g., correlations) doesn't support the hypothesis, the framework helps pinpoint whether the issue lies with poor data quality, missing data, bad proxies, or if the initial "words" (the hypothesis) were flawed. <a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>

## General Advice for Leaders and Teams
*   **Be Clear on Goals**: Clearly define the problem or goal you are trying to solve. <a class="yt-timestamp" data-t="00:41:53">[00:41:53]</a>
*   **Start Simple**: Begin by finding existing data or signals related to your problem. <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>
*   **Talk to Developers**: If no data exists, interview developers about their feelings on work tools, processes, and biggest productivity barriers. <a class="yt-timestamp" data-t="01:14:29">[01:14:29]</a>
*   **Balance Data Sources**: Initially, you might rely more on data from people (interviews, surveys), transitioning to more scalable system data over time. Always triangulate qualitative and quantitative data. <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>
*   **Don't Let Perfect Be the Enemy of Good**: Start measuring even with imperfect data and iterate. <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>
*   **Communicate Clearly**: Make your work accessible and easy to understand for your key audiences. Adapt your language to resonate with their roles and priorities. <a class="yt-timestamp" data-t="00:56:54">[00:56:54]</a> For researchers, this means bringing the "far near" (communicating ambitious research simply); for tactical implementers, it means bringing the "near far" (aligning short-term actions with long-term vision). <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>
*   **Decision-Making**: Clearly define criteria for decisions, assign relative weights to each, and then evaluate options. Sometimes, the mere act of defining criteria reveals the answer. <a class="yt-timestamp" data-t="01:04:42">[01:04:42]</a>

## Recommended Resources
*   **DORA.dev**: Website for the DORA research program, including the quick check tool and deep dives into capabilities. <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>
*   **"Accelerate" by Nicole Forsgren, Jez Humble, and Gene Kim**: Covers the initial four years of DORA research and its applications. <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>
*   **SPACE Paper**: Outlines the framework and provides examples of metrics for each category. <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>
*   **Paper on Data from People and Systems**: Discusses how qualitative and quantitative data complement each other in a DevOps context. <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>
*   **"How to Measure Anything" by Douglas W. Hubbard**: Useful for thinking about uncovering intangibles and making hunches with limited data. <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>
*   **Nicole Forsgren's Website**: nicolefv.com for contact information and updates on her upcoming book. <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>