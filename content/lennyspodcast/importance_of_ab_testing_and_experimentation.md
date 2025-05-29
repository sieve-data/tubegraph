---
title: Importance of AB testing and experimentation
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

A/B testing and [[experimentation_and_datadriven_decision_making | experimentation]] are crucial for product development, even for small changes, due to the observed "surprising, unexpected impact" that even minor bug fixes or feature introductions can have <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Ronnie Kohavi, considered a world expert on A/B testing and [[experimentation_and_datadriven_decision_making | experimentation]], advocates for a "test everything" approach, where any code change or new feature must be part of an experiment <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Unexpected Impacts and "Gold Nuggets"

Even seemingly trivial changes can yield significant results.
*   **Bing Ad Title Change**: A simple idea to promote the second line of an ad to the first, making the title larger, was on the backlog for months <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>. It was trivial to implement, taking engineers only a couple of hours <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. When launched as an experiment, it unexpectedly increased revenue by about 12%, which was worth $100 million at the time, without hurting user metrics <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. This was the biggest revenue impact in Bing's history <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
*   **Airbnb New Tab for Search Results**: A small experiment to open a new tab when clicking a search result led to one of the biggest wins in search <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. This concept was even debated heavily before at Microsoft around 2008, with pushback from designers, but proved highly beneficial <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.

While these "gold nuggets" are rare, they highlight the potential for massive returns from small efforts <a class="yt-timestamp" data-t="11:10:00">[01:11:10]</a>. Most gains, however, are made "inch by inch" <a class="yt-timestamp" data-t="11:19:00">[01:11:19]</a>. For example, Bing's relevance team, with hundreds of people, aimed to improve their key metric by 2% annually through small, consistent improvements <a class="yt-timestamp" data-t="12:12:00">[01:12:12]</a>. Similarly, 250 [[experimentation_and_datadriven_decision_making | experiments]] in Airbnb's search relevance team led to a 6% overall revenue improvement through many smaller ideas <a class="yt-timestamp" data-t="12:41:00">[01:12:41]</a>.

## The Reality of Experimentation: High Failure Rates

A humbling reality of [[experimentation_and_datadriven_decision_making | experimentation]] is the high failure rate of ideas.
*   At Microsoft, about two-thirds (66%) of ideas failed <a class="yt-timestamp" data-t="01:13:39">[01:13:39]</a>.
*   At Bing, a more optimized domain, the failure rate was around 85% <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>.
*   At Airbnb search relevance, 92% of [[experimentation_and_datadriven_decision_making | experiments]] failed to improve the target metric <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.
*   Other companies like Booking and Google Ads report similar failure rates of 80-90% <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>.

This high failure rate applies to "big bets" or radical new ideas as well. Even if a team believes strongly in a new design, they should be ready for it to fail 80% of the time <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>, <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>, <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

> "If you go for something big, try it out but be ready to fail eighty percent of the time." <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>

A notable example is Bing's attempt to integrate with social media (Twitter and Facebook), which consumed 100 person-years of effort but ultimately failed after about a year and a half, with all [[experimentation_and_datadriven_decision_making | experiments]] showing negative to flat results <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. This also happened at Netflix and Airbnb with social components <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

## Learning from Failures and Successes

[[experimentation_and_datadriven_decision_making | Experimentation]] acts as an "oracle" that provides data, even if it contradicts strong beliefs about an idea <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

### Documenting Learnings
It's crucial to document and summarize [[experimentation_and_datadriven_decision_making | experimentation]] learnings to build institutional memory <a class="yt-timestamp" data-t="01:17:02">[01:17:02]</a>.
*   Maintain a large internal deck of successes and failures <a class="yt-timestamp" data-t="01:19:35">[01:19:35]</a>.
*   Implement a search capability for past [[experimentation_and_datadriven_decision_making | experiments]] by keywords <a class="yt-timestamp" data-t="01:19:47">[01:19:47]</a>.
*   Hold quarterly meetings to review the most surprising [[experimentation_and_datadriven_decision_making | experiments]], including "surprising losers" <a class="yt-timestamp" data-t="01:27:50">[01:27:50]</a>. A surprising experiment is one where the estimated result and the actual result differ significantly <a class="yt-timestamp" data-t="01:27:50">[01:27:50]</a>.

**Example**: A Microsoft Windows indexer experiment showed improved indexing and relevance in offline tests, but in the live experiment, it dramatically killed battery life by consuming too much CPU <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a>. This unexpected negative outcome provided a critical learning point <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

### Avoiding Large Redesigns
Full product redesigns rarely result in positive outcomes and often require teams to "claw back" what they hurt <a class="yt-timestamp" data-t="01:16:33">[01:16:33]</a>. It's better to:
*   Do redesigns in steps and test incrementally <a class="yt-timestamp" data-t="01:17:05">[01:17:05]</a>.
*   Avoid the "sunk cost fallacy" of launching a bad change because time was already invested <a class="yt-timestamp" data-t="01:17:41">[01:17:41]</a>.
*   Implement changes incrementally, often called "one factor at a time" (OFAT), to learn and adjust <a class="yt-timestamp" data-t="01:18:08">[01:18:08]</a>.

## Addressing Concerns: Innovation vs. Optimization

The concern that [[experimentation_and_datadriven_decision_making | experimentation]] leads only to micro-optimizations and hinders innovation is common. However, it's possible to focus on both incremental changes and high-risk, high-reward ideas <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.

### Overall Evaluation Criterion (OEC)
The Overall Evaluation Criterion (OEC) is crucial for defining what a company is optimizing for <a class="yt-timestamp" data-t="02:28:18">[02:28:18]</a>. It's often misunderstood to be just about revenue, but focusing solely on short-term revenue can hurt the user experience and long-term growth <a class="yt-timestamp" data-t="02:38:38">[02:38:38]</a>.

*   **Balancing Metrics**: The OEC should include countervailing metrics that prevent negative impacts on the user experience. For example, with search ads, revenue can be increased, but it must be balanced with metrics like user churn or time to find a successful result <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. This can be framed as a constraint optimization problem: increasing revenue while staying within a fixed average real estate budget for ads <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **Long-Term Impact**: The OEC should be causally predictive of the lifetime value of the user <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This means considering retention rates, time to achieve a task, or even post-conversion satisfaction (e.g., how happy an Airbnb guest is months after their stay) <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Modeling Costs**: At Amazon, the email team's credit system for sales from recommendations led to spamming because there was no countervailing metric <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. By modeling the cost of user unsubscribes (e.g., lost future value), they found over half their campaigns were negative <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. This led to a new feature allowing users to unsubscribe from specific campaign types, reducing the negative impact <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### Avoiding "Shipping on Flat"
If an experiment shows no significant improvement ("flat" result), it should not be shipped <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. Shipping flat changes introduces more code, increases maintenance overhead, and provides no value <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. Exceptions are legal requirements, but even then, multiple variations should be tested to find the one that hurts the least <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

## When to Start A/B Testing

[[experimentation_and_datadriven_decision_making | Experimentation]] is most effective when there are enough users to make the statistics work out <a class="yt-timestamp" data-t="02:51:16">[02:51:16]</a>.
*   **Tens of thousands of users**: At this stage, you can start running [[experimentation_and_datadriven_decision_making | experiments]] but only detect large effects <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **200,000 users**: This is a "magical" number where you can start testing much more, including focusing on 5-10% beneficial changes, and testing everything to ensure no degradation <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Building the Culture and Platform**: Even if a company is too small to run statistically significant tests, it should start building an [[the_role_of_organizational_culture_in_experimentation_success | experimentation]] culture and integrating systems so that as it scales, it can realize the value <a class="yt-timestamp" data-t="02:51:52">[02:51:52]</a>.

## Building Trust in Experimentation

Trust is paramount for an [[experimentation_and_datadriven_decision_making | experimentation]] platform, which serves as both a safety net (for quick aborts of bad launches) and an oracle (for reliable results) <a class="yt-timestamp" data-t="02:52:03">[02:52:03]</a>.

### Common Pitfalls and Ensuring Validity
*   **Misinterpretation of P-values**: A common mistake is interpreting "1 minus p-value" as the probability that a treatment is better than control (e.g., p=0.02 means 98% probability) <a class="yt-timestamp" data-t="02:53:01">[02:53:01]</a>. This is incorrect <a class="yt-timestamp" data-t="02:59:01">[02:59:01]</a>. P-value assumes the null hypothesis is true. To get the true probability, Bayes' Rule is needed, incorporating the prior probability of success (e.g., historical failure rates like 80-92%) <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. For example, at Airbnb search, with an 8% success rate, a p-value less than 0.05 still means a 26% chance of a false positive <a class="yt-timestamp" data-t="03:04:30">[03:04:30]</a>.
    *   To increase trust, force teams to aim for p-values below 0.01 or replicate [[experimentation_and_datadriven_decision_making | experiments]] and combine results <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   **Sample Ratio Mismatch (SRM)**: This is the most common reason for invalid [[experimentation_and_datadriven_decision_making | experiments]] <a class="yt-timestamp" data-t="02:55:53">[02:55:53]</a>. If an experiment designed for a 50/50 split results in a different proportion (e.g., 50.2% vs. 49.8%), it's a red flag, indicating a problem that needs investigation (e.g., bots, data pipeline issues, skewed traffic sources) <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. At Microsoft, about 8% of [[experimentation_and_datadriven_decision_making | experiments]] suffered from SRM <a class="yt-timestamp" data-t="02:57:14">[02:57:14]</a>.
*   **Twyman's Law**: "If any figure looks interesting or different, it is usually wrong" <a class="yt-timestamp" data-t="03:00:56">[03:00:56]</a>. If an experiment shows a surprisingly large movement (e.g., 10% instead of the usual 1%), hold off on celebrations and investigate; nine out of ten times, there's a flaw <a class="yt-timestamp" data-t="03:01:13">[03:01:13]</a>.

## Experimentation Platforms

Building an [[challenges_and_strategies_in_building_an_experimentation_platform | experimentation platform]] is motivated by the goal of driving the marginal cost of [[experimentation_and_datadriven_decision_making | experiments]] down to zero <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. A good platform enables:
*   **Self-service**: Users can easily set up [[experimentation_and_datadriven_decision_making | experiments]] and define targets and metrics <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Automated Analysis**: Scorecards should be available soon after an experiment finishes, ideally within a day, without waiting a week for a data scientist <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **Metric Management**: A platform helps manage a large number of metrics (e.g., 10,000 at Bing) by breaking them into templates (e.g., UI experiments, revenue experiments) <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Maturity Model**: A framework of six axes can help organizations assess their [[challenges_and_strategies_in_building_an_experimentation_platform | experimentation platform]]'s maturity (crawl, walk, run, fly) and guide next steps <a class="yt-timestamp" data-t="04:11:55">[04:11:55]</a>.
*   **Build vs. Buy**: Today, many good third-party vendors offer [[challenges_and_strategies_in_building_an_experimentation_platform | experimentation platforms]], so companies starting out may consider buying rather than building from scratch <a class="yt-timestamp" data-t="04:06:58">[04:06:58]</a>.

## Speeding Up Experimentation

*   **Automated Scorecards**: Ensure that experiment results are available quickly after completion, ideally within a day, without manual data scientist involvement <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Variance Reduction Techniques**: Methods like capping metrics (e.g., limiting high revenue or nights booked to a maximum value) can reduce metric variance, allowing for statistically significant results with fewer users and thus faster <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
*   **CUPED (Controlled-experiment Using Pre-Experiment Data)**: This technique uses pre-experiment data to adjust the result, leading to unbiased outcomes with lower variance and requiring fewer users <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.

In summary, the importance of A/B testing and [[experimentation_and_datadriven_decision_making | experimentation]] lies in their ability to provide an objective "oracle" for product decisions, reveal surprising impacts, and foster continuous learning and improvement.