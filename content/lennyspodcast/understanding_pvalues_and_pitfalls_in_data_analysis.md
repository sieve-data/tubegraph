---
title: Understanding pvalues and pitfalls in data analysis
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Effective data analysis, particularly within the realm of A/B testing and experimentation, relies on a deep understanding of statistical concepts like p-values and an awareness of common pitfalls. Experts advocate for a culture of testing everything, recognizing that even minor changes can yield surprising, unexpected impacts <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a> <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Understanding P-values

A p-value is a statistical measure frequently used in A/B testing to determine the significance of an experimental result. However, its interpretation is often misunderstood <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>.

### Common Misinterpretations of P-values

A significant misconception is that a p-value of, for example, 0.02 means there's a 98% probability that the treatment is better than the control <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a> <a class="yt-timestamp" data-t="01:02:59">[01:02:59]</a>. This interpretation is incorrect <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.

A p-value is a conditional probability. It assumes the null hypothesis is true (i.e., there is no difference between the control and treatment groups) and computes the probability that the observed data would occur under that assumption <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a> <a class="yt-timestamp" data-t="01:03:26">[01:03:26]</a>. To determine the probability that the hypothesis is true given the data, Bayes' Rule must be applied, which requires knowing the prior probability of the hypothesis being successful <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a> <a class="yt-timestamp" data-t="01:03:48">[01:03:48]</a>.

### False Positive Risk

The "false positive risk" is the true probability that a statistically significant result is, in fact, a false positive <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>. This risk tends to be much higher than the common 5% (p-value < 0.05) often assumed <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>.

For instance, in environments like Airbnb's search team, where the success rate of ideas is very low (only 8% of experiments were successful at moving key metrics) <a class="yt-timestamp" data-t="01:13:10">[01:13:10]</a>, a statistically significant result with a p-value less than 0.05 could have a 26% chance of being a false positive <a class="yt-timestamp" data-t="01:04:40">[01:04:40]</a> <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>. To increase confidence and reduce false positives, teams might be required to achieve a p-value below 0.01 or perform replications for high-stakes experiments <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a> <a class="yt-timestamp" data-t="01:05:18">[01:05:18]</a>.

## Common Pitfalls in Data Analysis and Experimentation

### The Importance of [[common_pitfalls_in_pm_career_growth | Trust]]

Trust is paramount in an experimentation culture <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a> <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>. An experimentation platform serves as both a safety net—allowing quick abortion of bad launches—and an oracle, providing reliable results for key metrics <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a> <a class="yt-timestamp" data-t="00:52:21">[00:52:21]</a>. Losing trust in the platform, such as due to inflated error rates, can undermine the entire data-driven approach <a class="yt-timestamp" data-t="00:55:16">[00:55:16]</a> <a class="yt-timestamp" data-t="00:55:20">[00:55:20]</a>.

### Sample Ratio Mismatch (SRM)

A common issue that invalidates experiment results is a sample ratio mismatch <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. This occurs when the observed user distribution across control and treatment groups deviates significantly from the designed ratio (e.g., a 50/50 split showing 50.2/49.8 when it shouldn't by chance) <a class="yt-timestamp" data-t="00:55:58">[00:55:58]</a> <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>. It's a critical red flag indicating something is wrong with the experiment <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>.

*   **Prevalence:** About 8% of experiments at Microsoft suffered from SRM, a surprisingly high number <a class="yt-timestamp" data-t="00:57:12">[00:57:12]</a> <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>. Other third-party companies report similar rates of 6-10% <a class="yt-timestamp" data-t="00:58:10">[00:58:10]</a> <a class="yt-timestamp" data-t="00:58:20">[00:58:20]</a>.
*   **Causes:** Common causes include bots interacting differently with variations, or issues within the data pipeline (e.g., skewed traffic removal) <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a> <a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>.
*   **Addressing SRM:** When an SRM is detected, the experiment results should not be trusted <a class="yt-timestamp" data-t="00:57:40">[00:57:40]</a>. Platforms can enforce this by blanking out scorecards or highlighting numbers with a red line to prevent misinterpretation <a class="yt-timestamp" data-t="00:59:37">[00:59:37]</a> <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>.

### Twyman's Law

Twyman's Law states: "If any figure looks interesting or different, it is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a> <a class="yt-timestamp" data-t="01:00:58">[01:00:58]</a>. If an experiment yields a result that is "too good to be true" (e.g., a 10% movement when typical is under 1%) <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>, it's highly probable that something is wrong with the result <a class="yt-timestamp" data-t="01:01:36">[01:01:36]</a>. In practice, nine out of ten times this law is invoked, a flaw is found <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

### Lack of a Clear Overall Evaluation Criterion (OEC)

A significant pitfall is not clearly defining what you are optimizing for, known as the "Overall Evaluation Criterion" (OEC) <a class="yt-timestamp" data-t="02:28:18">[02:28:18]</a> <a class="yt-timestamp" data-t="02:28:25">[02:28:25]</a>. Simply optimizing for short-term revenue can lead to detrimental outcomes for the user experience and long-term value <a class="yt-timestamp" data-t="02:28:40">[02:28:40]</a> <a class="yt-timestamp" data-t="02:29:11">[02:29:11]</a>.

*   **Balancing Metrics:** An effective OEC incorporates countervailing metrics, such as user experience metrics (e.g., time to successful click, session success rate) alongside revenue, or framing it as a constraint optimization problem (e.g., maximizing revenue within a fixed ad real estate budget) <a class="yt-timestamp" data-t="02:28:45">[02:28:45]</a> <a class="yt-timestamp" data-t="02:29:41">[02:29:41]</a>.
*   **Long-Term Value:** The OEC should be causally predictive of the user's lifetime value <a class="yt-timestamp" data-t="03:07:07">[03:07:07]</a> <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. This requires incorporating metrics like retention rates or user satisfaction (e.g., post-stay ratings for Airbnb) <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a> <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.
*   **Modeling Long-Term Impact:** Long-term effects can be understood through dedicated long-term experiments or by building models using historical data, such as modeling the cost of user churn (e.g., Amazon's email team accounting for unsubscribe value) <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a> <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

### Shipping on Flat or Negative Results

A common mistake is shipping features that show flat or negative results in an experiment, often due to the sunk cost fallacy or a desire not to demotivate the team <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a> <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. Shipping a project with no value unnecessarily complicates the code base and increases maintenance costs <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a> <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. Unless there's a legal or similar requirement, features showing flat or negative impact should not be launched <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a> <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

### Big Redesigns vs. Iterative Changes

Large-scale product redesigns frequently fail <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a> <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. Instead of launching a comprehensive overhaul, it's often more effective to implement redesigns in smaller, incremental steps, testing along the way and adjusting based on results <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a> <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. This "one factor at a time" (OFAT) approach allows for learning and prevents months of wasted effort on features that negatively impact key metrics <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a> <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.

### Not Learning from Failures

Many companies run numerous experiments but fail to summarize and learn from the results, particularly the surprising ones (both successes and failures) <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a> <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. This leads to a loss of institutional memory <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. Documenting these learnings, holding quarterly meetings to discuss the most interesting experiments, and enabling searchable experiment history are crucial for an organization to learn and adapt <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a> <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a> <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

### Too Small to A/B Test

Not every domain is suitable for A/B testing, and a company needs a sufficient number of users for the statistics to work out <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a> <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. For most metrics, at least tens of thousands of users are needed <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. To detect meaningful changes (e.g., 5-10% beneficial changes for a startup), around 200,000 users might be required <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a> <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a> <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. Below this threshold, companies should focus on building an experimentation culture and platform in preparation for scale <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

## Strategies for Better Experimentation

### Test Everything

Adopting a "test everything" philosophy means that any code change or new feature should be introduced within an experiment <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a> <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. This is critical because even small bug fixes or changes can have unexpected and surprising impacts <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a> <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

### Balancing Incremental and Big Bets

While many wins come from small, inch-by-inch improvements, organizations should allocate some effort to high-risk, high-reward ideas <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a> <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a> <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. It's crucial to understand and accept that most of these big bets are likely to fail (around 80% of the time), but a successful one can be a "home run" <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a> <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a> <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

### Building a Robust Platform

Investing in an experimentation platform is key to bringing the marginal cost of running experiments close to zero <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a> <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. A mature platform should offer self-service capabilities for setting up experiments, defining targets and metrics, and analyzing results quickly without extensive manual analyst involvement <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a> <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a> <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.

### Speeding Up Experiments

To obtain results faster, several techniques can be employed:

*   **Post-Experiment Analysis Automation:** The platform should provide a scorecard soon after the experiment finishes, ideally within a day, to avoid waiting weeks for data scientists <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a> <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   **Variance Reduction:** Techniques like capping skewed metrics (e.g., limiting very high revenue or nights booked values) can reduce the variance and allow for statistically significant results with fewer users <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a> <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.
*   **CUPED Method:** This method uses pre-experiment data to adjust results, lowering variance and requiring fewer users to detect effects <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a> <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

## Conclusion

Understanding p-values accurately, recognizing common pitfalls like sample ratio mismatches and the risks of big redesigns, and committing to a culture of continuous learning through experimentation are crucial for making informed, data-driven decisions and fostering long-term product growth <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a> <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. The shift from anecdotal decision-making to a reliance on controlled experiments provides an "oracle" that reveals whether users truly benefit from product changes <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a> <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.