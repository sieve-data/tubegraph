---
title: Dora framework and metrics for software delivery
videoId: dP8NmcEkxJI
---

From: [[lennyspodcast]] <br/> 

The [[metrics_and_measuring_product_success|Dora (DevOps Research and Assessment) framework]] is a comprehensive research program focused on understanding and improving software development and delivery performance <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. While it encompasses an entire research program, it is primarily known for its "Four Keys" or "Four Metrics" that measure software delivery performance <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## The Four Key Metrics <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>

The [[metrics_and_measuring_product_success|Dora framework]] identifies four core metrics, split into two categories: speed and stability <a class="yt-timestamp" data-t="01:14:27">[01:14:27]</a>.

### Speed Metrics
*   **Lead Time for Changes:** This measures the time it takes to get from code committed to code running in production <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a>. This includes the entire deployment pipeline, from committing code to its first public endpoint ("ring zero") <a class="yt-timestamp" data-t="02:09:53">[02:09:53]</a>.
*   **Deployment Frequency:** This indicates how often an organization successfully deploys code to production <a class="yt-timestamp" data-t="01:14:38">[01:14:38]</a>.

### Stability Metrics
*   **Mean Time To Restore (MTTR):** This metric tracks how long it takes to restore service if something goes wrong <a class="yt-timestamp" data-t="01:14:44">[01:14:44]</a>.
*   **Change Fail Rate:** For every change pushed, this measures the rough percentage of incidents or issues that require human intervention <a class="yt-timestamp" data-t="01:14:51">[01:14:51]</a>.

### Key Finding: Speed and Stability Move in Tandem <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>
A significant finding from [[developer_productivity_measurement|Dora's research]] is that speed and stability move together with strong statistical significance <a class="yt-timestamp" data-t="01:15:08">[01:15:08]</a>.
*   **Moving Faster = More Stable Systems:** When teams move faster, they push smaller changes more often, leading to a smaller "blast radius" for issues. This makes debugging easier and reduces mean time to restore and mitigate problems <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>.
*   **Moving Slower = More Unstable Systems:** Conversely, pushing changes less frequently results in very large batch changes, which have a high "blast radius" and make it much harder to disentangle and fix bugs <a class="yt-timestamp" data-t="01:15:46">[01:15:46]</a>. This finding refutes the older common knowledge from ITIL and ITSM that required a two-week wait for change approvals to ensure stability, which actually caused batching up of changes and increased challenges <a class="yt-timestamp" data-t="01:16:20">[01:16:20]</a>.
*   **Core Message:** To move faster and improve quality, teams should "ship smaller things" and deploy more often <a class="yt-timestamp" data-t="01:18:12">[01:18:12]</a>. This approach is much safer <a class="yt-timestamp" data-t="01:18:28">[01:18:28]</a>.

## Elite Performance Benchmarks <a class="yt-timestamp" data-t="01:19:30">[01:19:30]</a>

As of 2019 (and remaining fairly consistent), elite performance benchmarks are:
*   **Deployment Frequency:** Deploy on demand <a class="yt-timestamp" data-t="01:19:33">[01:19:33]</a>.
*   **Lead Time for Changes:** Less than a day <a class="yt-timestamp" data-t="01:19:38">[01:19:38]</a>.
*   **Time to Restore:** Less than an hour <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a>.
*   **Change Fail Rate:** Between 0% and 15% <a class="yt-timestamp" data-t="01:19:43">[01:19:43]</a>.

> "Precision isn't really super important here [for these metrics]. Like, I don't... it doesn't really matter if your lead time is... if it's less than a day, it's less than a day, right? Like, that's fine from a business perspective." <a class="yt-timestamp" data-t="01:59:55">[01:59:55]</a>

There is no statistical significance in these benchmarks between small and large companies, with the exception of retail, which tended to perform better due to market pressures (the "retail apocalypse") forcing top performance or failure <a class="yt-timestamp" data-t="02:29:14">[02:29:14]</a>.

## Implementing and Improving with Dora

Instead of merely comparing to benchmarks, the most important aspect is knowing where an organization is and making progress <a class="yt-timestamp" data-t="01:17:20">[01:17:20]</a>.

The [[scaled_agile_framework_safe_and_its_challenges|Dora research program]] identifies a set of capabilities that predict speed and stability, which then lead to financial benefits (ROI and efficiency) <a class="yt-timestamp" data-t="02:59:57">[02:59:57]</a>:
*   **Technical Capabilities:** Such as automated testing, Continuous Integration/Continuous Delivery (CI/CD), trunk-based development, and effective use of Version Control Systems <a class="yt-timestamp" data-t="02:59:57">[02:59:57]</a>.
*   **Architectural Capabilities:** Including the use of loosely coupled systems and effective cloud adoption <a class="yt-timestamp" data-t="02:59:57">[02:59:57]</a>.
*   **Cultural Capabilities:** Fostering a healthy and productive team culture <a class="yt-timestamp" data-t="02:59:57">[02:59:57]</a>.
*   **Lean Management Practices:** Efficient workflows and continuous improvement <a class="yt-timestamp" data-t="02:59:57">[02:59:57]</a>.

### Getting Started
*   **Define the Problem/Goal:** Be extremely clear on what problem you are trying to solve or what goal you are trying to achieve <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This is often the biggest challenge, even at executive levels <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.
*   **Use the Dora Quick Check:** The dora.dev website provides a "quick check" tool where organizations can input their current metrics to see where they stand in the benchmarks and identify their probable constraints or areas of struggle <a class="yt-timestamp" data-t="02:56:59">[02:56:59]</a>. This tool is free and does not collect personal information <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   **Focus on Specific Capabilities:** Once constraints are identified (e.g., culture or continuous integration), focus on improving the relevant technical, architectural, or cultural practices <a class="yt-timestamp" data-t="02:52:52">[02:52:52]</a>.

## Relationship with [[space_framework_for_measuring_complex_creative_work|SPACE Framework]]

While [[metrics_and_measuring_product_success|Dora]] provides specific metrics for software delivery performance, the [[space_framework_for_measuring_complex_creative_work|SPACE framework]] offers a broader approach to measuring any type of complex creative work, including [[developer_productivity_measurement|developer productivity]] <a class="yt-timestamp" data-t="02:59:30">[02:59:30]</a>. [[metrics_and_measuring_product_success|Dora]] is effectively an implementation of [[space_framework_for_measuring_complex_creative_work|SPACE]], primarily focusing on the "outer loop" of software delivery <a class="yt-timestamp" data-t="03:29:29">[03:29:29]</a>.

## Resources
*   **dora.dev:** Website containing continued reports and deep dives into capabilities <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>.
*   **"Accelerate" book:** Written by Nicole Forsgren, it compiles and expands on the first four years of [[metrics_and_measuring_product_success|Dora's research]] <a class="yt-timestamp" data-t="02:57:57">[02:57:57]</a>.
*   **[[space_framework_for_measuring_complex_creative_work|SPACE paper]]:** Outlines the framework for measuring [[developer_productivity_measurement|developer productivity]] and provides examples of metrics for each dimension <a class="yt-timestamp" data-t="03:38:32">[03:38:32]</a>.
*   **"How to Measure Anything" by Hubbard:** A useful book for thinking about measuring intangible aspects and starting measurement from nothing <a class="yt-timestamp" data-t="04:03:04">[04:03:04]</a>.