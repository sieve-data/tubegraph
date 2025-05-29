---
title: Creating a culture of experimentation in a company
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

A culture of experimentation emphasizes the necessity of testing every code change and feature introduced through experiments. This approach is vital because even minor bug fixes and small changes can lead to surprising, unexpected impacts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

## Why Experiment?

The core rationale for widespread experimentation stems from the humbling reality that most ideas, even seemingly trivial ones, fail to yield positive results <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

*   **High Failure Rate**: Experience across various companies shows high failure rates for ideas:
    *   Around two-thirds (66%) of ideas failed at Microsoft overall <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>, <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   At Bing, a more optimized domain, the failure rate was around 85% <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
    *   At Airbnb, specifically in search relevance, 92% of ideas failed to improve the target metric <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   Other companies like Booking and Google Ads report similar failure rates of 80-90% <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   **Surprising Wins**: While most changes yield incremental gains, or fail, rare "home runs" demonstrate the value of testing.
    *   Moving the second line of ads to the first line on Bing resulted in a 12% revenue increase, worth $100 million at the time, without hurting user metrics <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   At Airbnb, opening search results in a new tab was a significant win, a concept previously proven beneficial at Microsoft (Hotmail, MSN) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Incremental Gains**: While big wins are rare, most success comes from "inch by inch" improvements, where many small gains add up significantly over time <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. For example, Airbnb's search relevance team ran 250 experiments, resulting in a 6% overall revenue improvement through many small ideas <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>, <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Encouraging Big Bets and Innovation

A common concern is that being overly experiment-driven leads only to micro-optimizations, hindering true innovation <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>.

*   **Portfolio Approach**: Companies should maintain a portfolio of experiments, including:
    *   **Incremental Changes**: These move the product steadily in a known successful direction <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
    *   **High-Risk, High-Reward Ideas**: These "big bets" are likely to fail, but if successful, they can be "home runs" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. Allocate some effort to these, being ready for an 80% failure rate <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>, <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.
*   **Rethinking Redesigns**: Large-scale redesigns often fail dramatically. It's often more effective to:
    *   Decompose the redesign into smaller, testable steps <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.
    *   Learn from each small change and adjust direction ("one factor at a time") <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>, <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>. This avoids the "sunk cost fallacy" of shipping bad changes due to prior investment <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.
*   **The Oracle of Experiments**: Experiments serve as an "oracle" providing objective data on whether users truly benefit from changes, regardless of internal beliefs or excitement <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>.

## [[The role of trust in successful experimentation | Building Trust]] in the Experimentation Platform

Trust is paramount for an experimentation platform, as it acts as both a "safety net" (allowing quick abortion of bad launches) and an "oracle" (providing reliable results) <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a>, <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.

*   **[[Building and optimizing an experimentation platform | Trustworthy Platform Design]]**:
    *   Implement checks to ensure experiment correctness. If something is wrong, the platform should halt and flag the issue <a class="yt-timestamp" data-t="00:53:07">[00:53:07]</a>, <a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>.
    *   Avoid statistical naivety: Early implementations of A/B testing tools (e.g., Optimizely) made mistakes by allowing real-time p-value monitoring to stop experiments, which inflates false positive rates <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>, <a class="yt-timestamp" data-t="00:53:40">[00:53:40]</a>.
*   **Common Issues Impacting Trust**:
    *   **Sample Ratio Mismatch (SRM)**: This is the most common reason for invalid experiments, where the number of users in control vs. treatment groups significantly deviates from the designed split (e.g., 50/50) <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>, <a class="yt-timestamp" data-t="00:56:58">[00:56:58]</a>. SRM can be caused by bots or data pipeline issues <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>, <a class="yt-timestamp" data-t="00:58:54">[00:58:54]</a>. Platforms should strongly indicate SRM to prevent misinterpretation of results <a class="yt-timestamp" data-t="00:59:37">[00:59:37]</a>.
    *   **Misinterpreting P-values**: The p-value does **not** represent the probability that a treatment is better than control. It assumes the null hypothesis is true and computes the probability of observing the data <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>, <a class="yt-timestamp" data-t="01:03:07">[01:03:07]</a>. A more useful metric is the "false positive risk," which is often much higher than the perceived 5% (e.g., 26% at Airbnb search due to high idea failure rate) <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>, <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>.
*   **Twyman's Law**: "If any figure that looks interesting or different is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. If an experiment result looks "too good to be true" (e.g., a 10% movement when usual movements are <1%), investigate for flaws before celebrating. Nine out of ten times, a flaw will be found <a class="yt-timestamp" data-t="01:01:38">[01:01:38]</a>.

## Practical Steps for Implementation

### When to Start [[the_importance_of_experimentation_and_longterm_experiments_in_growth | Experimentation]]

For startups, it's generally too early to A/B test if there aren't at least tens of thousands of users, as the statistics won't work out for most metrics <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>. For a retail site trying to detect 5-10% beneficial changes, around 200,000 users are needed for the "magic to start happening" <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>, <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>. Below this, focus on [[Building and maintaining a company culture | building the culture]] and platform for future scaling <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>.

### Build vs. Buy [[building_and_optimizing_an_experimentation_platform | Experimentation Platform]]

The decision to build an internal experimentation platform or buy a third-party solution is not absolute; it's often a mix <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. Today, there are many trustworthy third-party vendors offering good platforms <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>. The goal is to bring the marginal cost of running experiments down to zero through self-service and automation <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>, <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

### Finding a Beachhead for Implementation

To [[Building an Entrepreneurial Culture | shift a company's culture]], start with a team where experimentation is easy to run <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>. This means:

*   **Frequent Launches**: Choose teams that launch often (e.g., weekly, daily), not every few months or years <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>.
*   **Clear Overall Evaluation Criterion (OEC)**: The OEC is what a company is optimizing for. It should be a composite metric that balances business goals (e.g., revenue) with user experience (e.g., not hurting long-term engagement) <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>, <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>.
    *   The OEC should be causally predictive of the user's lifetime value <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>, <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.
    *   A good OEC clearly defines trade-offs (e.g., increase revenue without hurting user experience by more than X) <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.
    *   Avoid ambiguous OECs where different stakeholders disagree on the desired direction of a metric (e.g., is more time on a support site good or bad?) <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>.

### [[Building and maintaining company culture | Institutional Memory]] and Learning

Documenting experiments and their outcomes is crucial for [[Understanding company cultures impact on product development | organizational learning]] <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

*   Maintain a central repository of experiment successes and failures with search capabilities <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>, <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   Regularly hold meetings (e.g., quarterly) to review the most surprising experiments (both winners and "losers") <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. A "surprising" experiment is one where the estimated and actual results differ significantly <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   Learning from "surprising losers" (ideas expected to be positive but turned out negative) can provide deep insights (e.g., Windows indexer improving relevance but killing battery life) <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

## Addressing Resistance and Challenges

*   **Overcoming "We're Different"**: Many groups starting out believe their success rate will be higher than the observed 80-90% failure rates, but they are consistently humbled <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. For example, when Microsoft engineers initially resisted experimentation, they claimed to have "better PMs" <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>. Sharing surprising results from successful experimentation teams (like Bing) can help change minds <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>.
*   **Avoiding "Ship on Flat"**: If an experiment shows a "flat" (non-significant) result, it should generally not be shipped <a class="yt-timestamp" data-t="00:44:28">[00:44:28]</a>. Shipping introduces maintenance overhead and complicates the codebase without value. The only exceptions are legal requirements <a class="yt-timestamp" data-t="00:44:52">[00:44:52]</a>. Even then, test multiple approaches to find the one that hurts the least <a class="yt-timestamp" data-t="00:45:20">[00:45:20]</a>.
*   **[[Innovating within large organizations | Wartime vs. Peacetime Experimentation]]**: In crisis (e.g., COVID-19), the need for experimentation is even greater. If intuition is wrong 66-80% of the time in peacetime, it's unlikely to be suddenly right in wartime <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>, <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>.

## Key Learnings/Takeaways

*   **Test Everything**: Any code change or feature introduction should be part of an experiment <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **Embrace Failure**: Most ideas will fail. This is normal and expected <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.
*   **Balance Bets**: Allocate resources to both incremental improvements and high-risk, high-reward "home run" ideas <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.
*   **Prioritize Trust**: Build a robust, trustworthy experimentation platform that signals issues (like SRM) and provides accurate statistical analysis <a class="yt-timestamp" data-t="00:52:55">[00:52:55]</a>.
*   **Define Your OEC**: Clearly articulate what your company is optimizing for, balancing user and business needs <a class="yt-timestamp" data-t="00:28:25">[00:28:25]</a>.
*   **Cultivate Learning**: Document and share experiment results (both successes and failures) to build institutional memory <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **Speed through Automation**: Automate analysis and reduce variance to get results faster, minimizing the need for constant data scientist intervention <a class="yt-timestamp" data-t="01:12:57">[01:12:57]</a>.
*   **Hierarchy of Evidence**: When evaluating any claim, consider its source. Anecdotes are low-trust; controlled experiments are high-trust <a class="yt-timestamp" data-t="01:20:34">[01:20:34]</a>, <a class="yt-timestamp" data-t="01:20:53">[01:20:53]</a>.