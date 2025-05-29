---
title: Challenges and success rates in experimentation
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Experimentation is critical for product development, yet it comes with significant challenges and often surprising success rates. Organizations are frequently "humbled by how bad we are at predicting the outcome of experiments" <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## The Unpredictable Nature of Experimentation

Even minor changes can have unexpected and significant impacts, making it crucial to [[importance_of_ab_testing_and_experimentation | test everything]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Small bug fixes or code changes "can sometimes have surprising unexpected impact" <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

### Surprising Wins
Seemingly trivial changes can yield massive returns:
-   **Bing Ad Title Change**: Moving the second line of an ad to the first, making the title larger, was a "simple idea" that "increased Revenue by about 12 percent" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This change was "worth a hundred million dollars" at the time and "didn't hurt the user metric" <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. It was "the biggest Revenue impact of Bing in all its history" <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
-   **New Tab for Search Results**: At Microsoft (predating Airbnb), opening search results in a new tab was a "highly surprising result" that was "highly beneficial" <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This same change was a "biggest win in search" when later implemented at Airbnb <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Such "gold nuggets" or "small efforts huge gain" results are "very rare" <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Most improvements are "inch by inch" <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>, accumulating over time.

### High Failure Rates
A significant challenge in experimentation is the high rate of failure for new ideas and features:
-   **Microsoft**: Approximately "66 two-thirds of ideas fail" <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.
-   **Bing**: As the domain became more optimized, the failure rate increased to "around 85 percent" <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.
-   **Airbnb Search Relevance**: Out of 250 experiments during a specific tenure, "92 percent failed to improve the metric that we were trying to move" <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. Only "eight percent of our ideas actually were successful" <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>.
-   **Industry Average**: Other companies like Booking.com and Google Ads report failure rates "around 80 to 90 percent" <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>.

> [!WARNING] The speaker notes that these percentages refer to *experiments*, not necessarily unique ideas. An idea might be iterated on multiple times due to bugs or pivots, with initial implementations failing <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. Approximately "10 percent of experiments tend to be aborted on the first date" usually due to "implementation issue or something we haven't thought about" <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

## Balancing Incremental Gains and Big Bets

While most successes are incremental, it's vital to "allocate sometimes to these high risk High reward ideas" <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. These "most likely to fail" ideas can be "a home run" if successful <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.

> [!WARNING] It's crucial to "be ready to fail eighty percent of the time" with radical new ideas or designs <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.

A prime example of a big bet that failed was Bing's attempt to "integrate with social" platforms like Twitter and Facebook, spending "a hundred percent years on this idea" <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>. All experiments were "negative to flat," and the feature was eventually aborted <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. Similarly, Netflix and Airbnb also saw social features fail in experimentation <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

### Avoiding Redesigns and Sunk Cost Fallacy
Full product redesigns "dramatically failed" very often <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>. The recommended approach is to "do it in steps and test on the way and adjust" <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>. This prevents falling into the "sunk cost fallacy" where teams might feel compelled to launch a bad product due to prior investment <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.

Shipping "flat" results (no positive impact) is also not recommended, as it introduces "more code" and "maintenance overhead" <a class="yt-timestamp" data-t="00:44:52">[00:44:52]</a>. Only ship flat or negative results if it's a legal requirement, and even then, test multiple options to "ship the one that hurts the least" <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.

## Defining Success: The Overall Evaluation Criterion (OEC)

A key concept for effective experimentation is the Overall Evaluation Criterion (OEC), which defines "what are you optimizing for" <a class="yt-timestamp" data-t="00:28:25">[00:28:25]</a>. Simply optimizing for revenue is often "the wrong question" as it can lead to "a lot of bad things that will improve Revenue" at the expense of user experience <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.

The OEC should include "countervailing metrics" to balance short-term gains with long-term health. For example, in search, while adding more ads increases revenue, it can also increase user churn or time to find a successful result <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>. The goal is "long-term growth and revenue" tied to the "lifetime value of the user" <a class="yt-timestamp" data-t="00:32:28">[00:32:28]</a>.

> [!EXAMPLE] **Amazon Email Team**: The email team was initially credited for any purchase resulting from an email, leading to excessive spamming <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. By modeling the "cost of spamming the users" (e.g., value lost from unsubscribes), it was discovered that "more than half the campaigns that were being sent were negative" when considering long-term value <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>. This led to a new feature allowing users to unsubscribe from specific campaign types, reducing the negative impact <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a>.

To understand long-term metrics, organizations can run "long term experiments for the goal of learning something" <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a> or "build models that use some of our background knowledge or use some you know data science to look historical" <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.

## Ensuring Trust in Experimentation

The [[role_of_trust_pvalue_and_twymans_law_in_experiments | experimentation platform]] acts as a "safety net" for quick abortion of bad launches and an "oracle" for accurate results <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a>. Trust in the platform is paramount and "easy to lose" <a class="yt-timestamp" data-t="00:52:40">[00:52:40]</a>.

### Common Pitfalls and How to Avoid Them
1.  **Misinterpretation of P-values**: A common mistake is interpreting `1 - p-value` as the probability that treatment is better than control, which is "wrong" <a class="yt-timestamp" data-t="01:02:59">[01:02:59]</a>. For example, at Airbnb search, where the success rate was only 8%, a statistically significant result (p-value < 0.05) actually had a "26 percent chance that this is a false positive result" <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>. To combat this, results with p-values between 0.01 and 0.05 should be replicated <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>.
2.  **Optimizing on Real-Time P-values**: Early implementations by companies like Optimzely were "statistically naive" by allowing users to stop an experiment when the p-value became statistically significant in real-time. This "inflates your what's called type one error or the false positive rate materially" to potentially 30% <a class="yt-timestamp" data-t="00:53:48">[00:53:48]</a>.
3.  **Sample Ratio Mismatch (SRM)**: If an experiment designed to send 50% of users to control and 50% to treatment deviates significantly (e.g., 50.2% vs. 49.8%), it's a "red flag" <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>. At Microsoft, "around eight percent of experiments... suffered from the sample ratio mismatch" <a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>. Common causes include bots disproportionately hitting control/treatment groups or issues with the data pipeline <a class="yt-timestamp" data-t="00:58:41">[00:58:41]</a>.
    > [!NOTE] To ensure teams address SRMs, Microsoft's platform eventually highlighted every number in the scorecard with a red line if an SRM was detected, even in screenshots <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a>.
4.  **[[role_of_trust_pvalue_and_twymans_law_in_experiments | Twyman's Law]]**: This law states that "if any figure that looks interesting or different is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. If an experiment shows an unusually large positive (or negative) movement (e.g., 10% when normal is 1%), "hold the celebratory there" and "investigate" <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>. In 9 out of 10 cases, a flaw is found <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

### Institutional Memory and Learning
It's vital to document and summarize learnings from experiments to build "institutional memory" <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>. Regular "quarterly meeting of the most surprising experiments" (both winners and losers) helps <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. A "surprising experiment is one where the estimated resolve beforehand and the actual result differ by a lot" <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## Building an Experimentation Culture and Platform

For organizations embarking on experimentation, there are key considerations:

### When to Start A/B Testing
Unless a company has "at least tens of thousands of users, the math the statistics just don't work out" for most metrics <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>. To detect beneficial changes of 5% or more, a retail site would need "something like 200,000 users" <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

> [!TIP] Start building the culture and platform when you have "tens of thousands of users" to detect large effects, and expect "magic" to happen when you reach "200,000 users" <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.

### Shifting Culture
To shift a company's culture towards experimentation, start with a "beachhead" team that launches frequently (e.g., weekly or multiple times a day) and has a clear OEC <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>. Bing's success at Microsoft demonstrated the value, and cross-pollination of personnel helped spread the data-driven mindset <a class="yt-timestamp" data-t="01:08:22">[01:08:22]</a>.

> [!EXAMPLE] **Microsoft Office**: Initially, Office released every three years and had a "complete denial" that their ideas could fail <a class="yt-timestamp" data-t="00:40:31">[00:40:31]</a>. With executive support, Office eventually started running experiments and "realized that many of their ideas were failing" <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>.

### The Role of a Platform
A robust [[building_a_culture_and_platform_for_experimentation | experimentation platform]] aims to bring the "marginal cost of experiments down to zero" <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>, enabling self-service and automated analysis. When the platform is good, "when the experiment finishes you should have a scorecard soon after" <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>, ideally within a day, rather than waiting a week for an analyst <a class="yt-timestamp" data-t="01:12:53">[01:12:53]</a>.

In its early days, platforms were built internally (e.g., Amazon, Microsoft), but today, "enough vendors that provide good experimentation platforms that are trustworthy" are available <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>.

### Speeding Up Experiments
To run experiments faster and get quicker results:
-   **Automated Scorecards**: Ensure the platform provides immediate scorecards post-experiment to eliminate delays from manual analysis <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.
-   **Variance Reduction Techniques**: Methods like "capping metrics" (e.g., limiting max revenue credit for an order, or capping nights booked) or Cupid, which uses pre-experiment data to adjust results, can "reduce the variance of metrics so that you need less users" and "get statistically significant results faster" <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.

## Key Learnings

Experimentation provides an "Oracle that gives you the data" <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>, helping to determine if users are truly benefiting. While there's a natural bias towards expecting success, the "humbling reality" is that "most ideas fail" <a class="yt-timestamp" data-t="00:37:53">[00:37:53]</a>. Organizations that embrace this reality and invest in trustworthy experimentation platforms and cultures are better positioned for long-term success.