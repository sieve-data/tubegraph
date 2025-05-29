---
title: Building a culture and platform for experimentation
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Experimentation, particularly A/B testing, is seen by many as essential for modern product development and growth <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>. Ronnie Kohavi, a world expert in A/B testing, emphasizes the importance of systematically testing changes to ensure product success and drive innovation <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.

## The Power of Experimentation

Every code change or feature introduction should be part of an experiment <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. Even small bug fixes or minor changes can have unexpected and surprising impacts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It's not possible to experiment too much <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.

### Surprising Wins
Experimentation often reveals unexpected opportunities:
*   **Bing's Ad Title Change** A seemingly minor change to display ad titles on Bing – promoting the second line of an ad to the first – led to a 12% increase in revenue <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This simple idea, trivial to implement, was worth $100 million at the time and didn't hurt user metrics <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Airbnb's New Tab for Search Results** Opening search results in a new tab was a significant win for Airbnb's search team <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This concept, initially debated and met with pushback from designers in earlier contexts like Microsoft's MSN, repeatedly proved highly beneficial <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>, <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>, <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

While "gold nuggets" – small efforts yielding huge gains – are rare <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>, most improvements come "inch by inch" <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. For example, Bing's relevance team aimed to improve their key metric by 2% annually, achieving this through many small, incremental changes <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

### The Reality of Failure
A key aspect of experimentation is accepting a high failure rate:
*   At Microsoft, about two-thirds (66%) of ideas failed <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   At Bing, a more optimized domain, the failure rate was around 85% <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   At Airbnb, 92% of experiments failed to improve the target metric in search relevance <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>, <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   Industry-wide, other companies like Booking.com and Google Ads report failure rates of 80-90% <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   About 10% of experiments are aborted on the first day due to implementation bugs, not necessarily bad ideas <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

New teams often believe they will be different, but most are humbled by these high failure rates <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Building a Culture of Experimentation

[[creating_a_strong_product_culture | Creating a strong product culture]] that is experiment-driven requires addressing several key areas:

### Defining the Overall Evaluation Criterion (OEC)
The OEC is the single most important metric or combination of metrics a company is optimizing for <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. It's often misunderstood as simply optimizing for revenue <a class="yt-timestamp" data-t="00:28:32">[00:28:32]</a>.
*   **Balancing Metrics**: The OEC must include a "countervailing metric" to prevent short-term gains from hurting long-term user experience <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>, <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. For search engines, simply displaying more ads increases revenue but hurts user experience <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
*   **Constraint Optimization**: A useful approach is to phrase the OEC as a constraint optimization problem. For example, increase revenue within a fixed amount of ad real estate <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>.
*   **Long-Term Value**: The OEC should be causally predictive of the user's lifetime value <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. This encourages thinking about retention rates or the time it takes users to achieve a task <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>.
    *   For hotels, conversion rate isn't enough; customer satisfaction months after their stay should be considered part of the OEC <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>.
    *   At Amazon, crediting the email team solely on purchases led to spamming <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>. Modeling the cost of unsubscribes revealed that over half of campaigns were negative when considering long-term value <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>, <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>. This led to a new feature allowing users to unsubscribe from specific campaign types, preserving overall email engagement <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>.

### Iterative Development vs. Big Redesigns
Large-scale redesigns often fail dramatically <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>. It's better to:
*   **Decompose Redesigns**: Break down a redesign into smaller, testable steps, adjusting along the way <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>. This "one factor at a time" (OFAT) approach allows teams to learn and incorporate only the successful components <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.
*   **Manage Expectations for Big Bets**: When allocating resources to high-risk, high-reward ideas or complete redesigns, teams must be ready to fail 80% of the time <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>, <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>. This prevents the sunk cost fallacy, where significant investment leads to launching a bad product <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.

### Addressing Resistance and Fostering Adoption
When facing resistance to experimentation:
*   **Find a Beachhead**: Start with a team that launches frequently (e.g., weekly or daily) and has a clear OEC <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>.
*   **Share Successes (and Failures)**: Once early adopter teams show success, share these surprising results across the company <a class="yt-timestamp" data-t="01:08:15">[01:08:15]</a>.
*   **Cross-Pollination**: As people from experiment-driven teams move to other groups, they help spread the culture <a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a>.
*   **Humble the Organization**: Early, smaller experiments can effectively show skeptical groups that their intuition is often wrong <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>. At Microsoft, initial resistance ("we have better PMs here") was overcome after Bing demonstrated the value of experimentation at scale <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>.

### Institutional Memory and Learning
[[building_and_maintaining_company_culture_to_enhance_team_collaboration | Building and maintaining company culture to enhance team collaboration]] around experimentation involves effective knowledge management:
*   **Document Learnings**: Summarize and document experiment successes and failures to retain institutional memory <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>, <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   **Searchable Experiment History**: Implement a system to search past experiments by keywords to prevent re-running known failures or rediscovering past successes <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. Microsoft ran 20,000-25,000 experiments annually, making searchability crucial <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.
*   **Regular Review Meetings**: Hold quarterly meetings to discuss the most surprising experiments (both winners and losers) to foster learning and engagement <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>, <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.

## Building a Trustworthy Experimentation Platform

A robust experimentation platform is crucial, acting as both a "safety net" for bad launches and an "oracle" for reliable results <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a>.

### Trust as the Foundation
[[building_trust_as_a_product_leader | Building trust as a product leader]] is paramount in experimentation. The platform must be trustworthy, or its results will be questioned <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>.
*   **Preventing False Positives**: Early platforms like Optimizely sometimes provided statistically naive results, leading to inflated false positive rates (e.g., 30% instead of the expected 5%) <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. This eroded user trust, as reported successes didn't materialize <a class="yt-timestamp" data-t="00:54:09">[00:54:09]</a>.
*   **Twyman's Law**: "If any figure looks interesting or different, it is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. If an experiment shows an unusually large positive impact, it's critical to investigate for flaws before celebrating <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>. Nine out of ten times, a flaw is found <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.
*   **P-Value Misinterpretation**: The most common misinterpretation of a p-value (e.g., 0.02) is that it represents the probability that the treatment is better than control (e.g., 98%). This is incorrect <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>. The true "false positive risk" (the probability that a positive result is false) is often much higher, especially in domains with high idea failure rates (e.g., 26% at Airbnb search) <a class="yt-timestamp" data-t="01:04:10">[01:04:10]</a>.

### Identifying Invalid Results
*   **Sample Ratio Mismatch (SRM)**: A common issue where the actual user distribution between control and treatment groups deviates significantly from the designed split (e.g., 50/50) <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. This is a major red flag, indicating something is wrong with the experiment <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>.
    *   At Microsoft, about 8% of experiments suffered from SRM <a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>.
    *   Common causes include bots interacting differently with new versions or issues in the data pipeline <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>.
    *   Platforms should proactively flag and even hide invalid results to force investigation <a class="yt-timestamp" data-t="00:59:32">[00:59:32]</a>.

### Speeding Up Experiments
Once a trustworthy platform is in place, focus on speed:
*   **Automated Scorecards**: Results should be available shortly after an experiment finishes, eliminating waiting for data scientists to analyze <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>.
*   **Variance Reduction Techniques**:
    *   **Capping Metrics**: For skewed metrics like revenue, capping extreme values (e.g., purchases over $1,000) can reduce variance and allow faster statistically significant results <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.
    *   **CUPED (Controlled-experiment Using Pre-Experiment Data)**: This technique uses pre-experiment data to adjust results, lowering variance without biasing the outcome <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>.

## When to Start Experimenting
*   Start considering A/B testing when you have at least tens of thousands of users <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.
*   For statistically significant results on common metrics, especially detecting 5-10% beneficial changes, around 200,000 users are typically needed <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   Below 200,000 users, focus on [[building_a_startup_culture | building the culture]] and the platform infrastructure so that as you scale, you can fully leverage experimentation <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.

### Build vs. Buy
*   For early-stage companies, it's often more efficient to use existing third-party experimentation platforms rather than building one from scratch, as many good vendors now exist <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>.
*   The goal is to drive the incremental cost of running an experiment close to zero through self-service tools and automation <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>.