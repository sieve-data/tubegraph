---
title: Role of trust pvalue and Twymans Law in experiments
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Rani Kohavi, widely recognized as an expert in [[importance_of_ab_testing_and_experimentation | A/B testing and experimentation]], emphasizes that while the speed of running experiments is important, trust in the experimentation process is paramount <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a> <a class="yt-timestamp" data-t="01:12:28">[01:12:28]</a>. This trust is built on the reliability of the platform and the accurate interpretation of results.

## Importance of Trust in Experimentation
The experimentation platform serves two primary purposes:
1.  **Safety Net** If a deployed feature is problematic, the platform should enable quick abortion of the experiment <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>.
2.  **Oracle** At the end of an experiment (e.g., two weeks), the platform should accurately report the impact on key metrics, along with other debugging and guardrail metrics <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>.

Trust in these functions is crucial for an organization to adopt an experiment-driven culture <a class="yt-timestamp" data-t="00:52:59">[00:52:59]</a>. Trust, however, is easily lost <a class="yt-timestamp" data-t="00:52:43">[00:52:43]</a>. Early implementations of experimentation platforms, such as Optimizely, made statistical errors by allowing users to stop experiments when p-values became statistically significant in real-time, leading to inflated false positive rates (e.g., 30% instead of the aimed 5%) <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. This erosion of trust prompted a famous post titled "Optimizely almost got me fired" <a class="yt-timestamp" data-t="00:54:28">[00:54:28]</a>. This highlights the importance of [[building_trust_as_a_product_leader | building trust as a product leader]] in the experimentation platform.

## Understanding P-Value
A common misconception about p-values is interpreting `1 - p-value` as the probability that a treatment is better than the control (e.g., a p-value of 0.02 means a 98% probability of the treatment being better) <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>. This interpretation is incorrect <a class="yt-timestamp" data-t="01:02:59">[01:02:59]</a>.

The p-value is a conditional probability, assuming the null hypothesis is true. It computes the probability of observing the data given that there is no true difference between the control and treatment groups <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. To determine the probability that the hypothesis (e.g., treatment is better) is true given the data, Bayes' Rule must be applied, which requires an additional "prior probability" of the hypothesis being successful <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.

Considering historical data on [[challenges_and_success_rates_in_experimentation | experimentation success rates]] (e.g., 8% success rate in Airbnb search <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a>), the actual "false positive risk" can be much higher than the perceived 5% <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>. For example, at an 8% success rate, a statistically significant result (p-value < 0.05) still has a 26% chance of being a false positive <a class="yt-timestamp" data-t="01:04:35">[01:04:35]</a>. To mitigate this, teams are often advised to require p-values below 0.01 and replicate experiments, especially for high-impact changes, to achieve a much lower false positive rate <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>.

## Twyman's Law
Twyman's Law states: "if any figure that looks interesting or different is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. This principle advises caution when encountering unusually large or surprising results from an experiment <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>. For instance, if typical experiment movements are under one percent and a result shows a 10% movement, it warrants immediate investigation before celebration <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>.

In practice, nine out of ten times, applying Twyman's Law leads to the discovery of a flaw in the experiment <a class="yt-timestamp" data-t="01:01:38">[01:01:38]</a>. An example of a legitimate, but initially surprising, breakthrough was a trivial change to Bing's ad display (moving the second line to the first) that increased revenue by 12% <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This result was thoroughly replicated and double-checked due to its surprising nature <a class="yt-timestamp" data-t="01:01:47">[01:01:47]</a>.

## Signs of Invalid Experiments
A critical step in maintaining trust is identifying and addressing invalid experiments. The most common issue is a **Sample Ratio Mismatch (SRM)** <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>.

### Sample Ratio Mismatch (SRM)
SRM occurs when the actual distribution of users to control and treatment groups deviates significantly from the intended allocation (e.g., a 50/50 split resulting in 50.2% vs. 49.8% for a large experiment) <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. Such deviations are highly improbable by chance and indicate a problem with the experiment's setup <a class="yt-timestamp" data-t="00:56:44">[00:56:44]</a>.

Even at Microsoft, after years of running experiments, about 8% of experiments suffered from SRM <a class="yt-timestamp" data-t="00:57:20">[00:57:20]</a>. Other companies report similar rates, ranging from 6% to 10% <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.

Common causes of SRM include:
*   **Bots**: Bots interacting differently with control and treatment versions due to website changes <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>.
*   **Data Pipeline Issues**: Errors in how data is collected or processed <a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>.
*   **Skewed Traffic**: External campaigns or entry points to the site unintentionally skewing traffic to certain groups <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>.

To ensure trust, experimentation platforms have implemented strict measures against SRM:
*   Initially, banners were displayed warning of SRM, but users often ignored them <a class="yt-timestamp" data-t="00:59:29">[00:59:29]</a>.
*   Later, scorecards were blanked out, requiring a user click to expose results, to force acknowledgement of the issue <a class="yt-timestamp" data-t="00:59:37">[00:59:37]</a>.
*   Ultimately, every number in the scorecard was highlighted with a red line so that even screenshots would indicate an SRM <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a>.
*   This approach reinforces the need to investigate and understand why results might be invalid, combating the natural bias to see success <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>. This is part of [[managing_failure_and_rebuilding_trust | managing failure and rebuilding trust]] in the experimentation process.

Adhering to these principles of trust, proper statistical interpretation, and skepticism towards extreme results is crucial for effective and reliable [[importance_of_ab_testing_and_experimentation | experimentation]].