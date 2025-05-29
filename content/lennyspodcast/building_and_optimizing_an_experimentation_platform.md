---
title: Building and optimizing an experimentation platform
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Ronny Kohavi, recognized as a leading expert in [[the_importance_of_ab_testing_in_software_development | A/B testing]] and experimentation, emphasizes the critical role of a robust experimentation platform in driving growth and making data-driven decisions [01:17:10](<a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>. A well-built platform acts as both a safety net for deployments and an oracle for understanding user behavior [00:52:03](<a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.

## The Value of an Experimentation Platform

The primary motivation for building an experimentation platform is to reduce the marginal cost of running experiments to near zero [01:10:32](<a class="yt-timestamp" data-t="01:10:32">[01:10:32]</a>. Once the platform is established, the incremental cost of running an experiment should approach zero [00:25:40](<a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>. This allows for pervasive experimentation, where nearly every code change or feature introduction is tested [00:21:08](<a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

Kohavi is a strong advocate for "test everything" [00:00:02](<a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, [00:21:08](<a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. Even small bug fixes or minor changes can have surprising, unexpected impacts [00:00:13](<a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, [00:21:21](<a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. He believes it's not possible to experiment too much [00:21:30](<a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.

## Key Aspects of a Trustworthy Platform

A trustworthy experimentation platform is essential for [[the_role_of_trust_in_successful_experimentation | building a culture of trust]] in the results [00:52:55](<a class="yt-timestamp" data-t="00:52:55">[00:52:55]</a>. This trust enables the platform to serve two main purposes:
1.  **Safety Net**: Allowing for quick abortion of bad launches [00:52:10](<a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.
2.  **Oracle**: Providing clear results on key metrics and debugging information after an experiment [00:52:10](<a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.

### Ensuring Trustworthiness

*   **Checks and Balances**: Implementing checks to ensure experiment correctness is crucial [00:53:07](<a class="yt-timestamp" data-t="00:53:07">[00:53:07]</a>. If something is wrong, the platform should flag it, indicating untrustworthy results [00:53:12](<a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>.
*   **Avoiding Statistical Naiveté**: Early implementations, such as Optimizely's, sometimes led to inflated error rates by allowing real-time p-value monitoring and stopping experiments based on early statistical significance [00:53:31](<a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. This can lead to a 30% error rate where a 5% false positive rate is expected [00:54:02](<a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.
*   **Sample Ratio Mismatch (SRM) Detection**: This is the most common issue observed [00:55:53](<a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. If user allocation to control and treatment groups deviates significantly from the design (e.g., 50/50), it's a red flag [00:56:11](<a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>.
    *   Microsoft saw about 8% of experiments suffer from SRMs [00:57:24](<a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>.
    *   Common causes include bots interacting differently with changes or issues in the data pipeline [00:58:41](<a class="yt-timestamp" data-t="00:58:41">[00:58:41]</a>.
    *   Platforms should prevent users from easily ignoring SRM warnings to maintain trust [00:59:29](<a class="yt-timestamp" data-t="00:59:29">[00:59:29]</a>.

### Defining the Overall Evaluation Criterion (OEC)

A critical aspect of any experimentation platform is clearly defining what it is optimizing for through an [[the_importance_of_experimentation_and_longterm_experiments_in_growth | Overall Evaluation Criterion (OEC)]] [02:28:13](<a class="yt-timestamp" data-t="02:28:13">[02:28:13]</a>.
*   The OEC should be causally predictive of the long-term lifetime value of the user [03:20:07](<a class="yt-timestamp" data-t="03:20:07">[03:20:07]</a>.
*   It should include countervailing metrics to prevent short-term gains at the expense of user experience or long-term health [02:28:45](<a class="yt-timestamp" data-t="02:28:45">[02:28:45]</a>, [02:29:29](<a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>. For example, increasing revenue shouldn't come at the cost of increased user churn or time to successful task completion [02:29:16](<a class="yt-timestamp" data-t="02:29:16">[02:29:16]</a>.
*   Some OECs can incorporate user satisfaction metrics, even if they have a time delay, by building predictive models based on historical data [03:14:00](<a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>, [03:31:19](<a class="yt-timestamp" data-t="03:31:19">[03:31:19]</a>.

## Scaling and Maturity of the Platform

A mature platform enables self-service for setting up and running experiments, defining targets, and selecting relevant metrics [01:10:39](<a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a>.
*   The number of available metrics in a scorecard can grow very large (e.g., 10,000 at Bing) [01:10:49](<a class="yt-timestamp" data-t="01:10:49">[01:10:49]</a>. Platforms can use templates (e.g., for UI or revenue experiments) to manage this complexity [01:11:05](<a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>.
*   Automation is key to reducing the need for data scientists to interpret results [01:11:46](<a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.
*   A "crawl, walk, run, fly" framework with six axes can help organizations assess their experimentation maturity and guide future development [01:11:53](<a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>.

### Speeding up Experimentation

While trust is paramount, platform optimization can also increase speed:
*   **Fast Scorecard Generation**: Results should be available soon after an experiment finishes, ideally within a day, without waiting a week for a data scientist [01:12:44](<a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>.
*   **Variance Reduction Techniques**: Methods like capping skewed metrics (e.g., revenue, nights booked) or using CUPED (Controlled-experiment Using Pre-Experiment Data) can reduce variance, requiring fewer users and yielding faster statistically significant results [01:13:04](<a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.

## Build vs. Buy

For companies starting out, the decision of whether to build or buy an experimentation platform is crucial [01:06:46](<a class="yt-timestamp" data-t="01:06:46">[01:06:46]</a>.
*   Historically, companies like Amazon and Microsoft had to build their own platforms because no commercial solutions existed [01:07:22](<a class="yt-timestamp" data-t="01:07:22">[01:07:22]</a>.
*   Today, many trustworthy third-party vendors offer good experimentation platforms [01:07:34](<a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>.
*   The decision is often not binary but involves a combination of building and buying [01:07:06](<a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>.

## Fostering a Culture of Experimentation

To successfully implement and scale an experimentation platform, a [[creating_a_culture_of_experimentation_in_a_company | culture of experimentation]] is vital.
*   Start by finding a team that launches frequently (e.g., weekly or daily) and where the OEC is clearly defined [01:08:40](<a class="yt-timestamp" data-t="01:08:40">[01:08:40]</a>.
*   Share surprising results from early experiments to build internal buy-in [01:08:15](<a class="yt-timestamp" data-t="01:08:15">[01:08:15]</a>.
*   Leverage cross-pollination, where individuals experienced with experimentation move to other teams and advocate for its adoption [01:08:23](<a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a>.
*   Expect that most ideas will fail (e.g., 66% at Microsoft, 85% at Bing, 92% at Airbnb search) [01:13:32](<a class="yt-timestamp" data-t="01:13:32">[01:13:32]</a>, [01:14:02](<a class="yt-timestamp" data-t="01:14:02">[01:14:02]</a>, [01:14:06](<a class="yt-timestamp" data-t="01:14:06">[01:14:06]</a>, [01:14:19](<a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>. This humble reality needs to be internalized by organizations [00:00:41](<a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, [01:15:17](<a class="yt-timestamp" data-t="01:15:17">[01:15:17]</a>.

![[challenges_and_failures_in_experimentation#Surprising Results & Twyman's Law]]

# When to Start A/B Testing

Companies should start considering A/B testing when they have at least tens of thousands of users [02:26:53](<a class="yt-timestamp" data-t="02:26:53">[02:26:53]</a>. For retail sites aiming to detect 5% beneficial changes, around 200,000 users are needed for the statistics to work effectively [02:27:21](<a class="yt-timestamp" data-t="02:27:21">[02:27:21]</a>. Below this threshold, companies can still begin building the culture and integrating the platform so they are ready to scale when user numbers increase [02:27:52](<a class="yt-timestamp" data-t="02:27:52">[02:27:52]</a>.