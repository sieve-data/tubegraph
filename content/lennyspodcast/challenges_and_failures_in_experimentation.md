---
title: Challenges and failures in experimentation
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Ronnie Kohavi, a world expert in A/B testing and experimentation, emphasizes that the journey of [[the_importance_of_experimentation_and_longterm_experiments_in_growth | experimentation]] is fraught with challenges and unexpected outcomes. Despite the common desire for quick wins, the reality often involves a high rate of failure and the need for persistent learning from both successes and setbacks <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>.

## The Humbling Reality of A/B Testing

Kohavi is a strong advocate for "test everything," meaning any code change or new feature should be part of an experiment <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This is because even small bug fixes or minor changes can have surprising and unexpected impacts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

However, the majority of experiments do not yield positive results:
*   At Microsoft, about two-thirds (66%) of ideas failed <a class="yt-timestamp" data-t="01:13:34">[01:13:34]</a>.
*   At Bing, a more optimized domain, the failure rate was around 85% <a class="yt-timestamp" data-t="01:13:48">[01:13:48]</a>.
*   At Airbnb, specifically in search relevance under Kohavi's tenure, 92% of experiments failed to improve the target metric <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>, <a class="yt-timestamp" data-t="01:13:08">[01:13:08]</a>.
*   Other companies like Booking.com and Google Ads report similar failure rates of 80% to 90% <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>.

This high failure rate is "very humbling" <a class="yt-timestamp" data-t="01:15:17">[01:15:17]</a>, and new groups often mistakenly believe their success rate will be much higher <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>.

## Unexpected Impacts and [[lessons_from_failures_and_the_importance_of_persistence | Learning from Failures]]

While most ideas fail, some produce highly surprising and valuable results, whether positive or negative.

### Surprising Wins
*   **Bing Ad Title Change**: A seemingly trivial change on Bing that moved the second line of an ad to the first, making the title larger, increased revenue by about 12% <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This change was worth $100 million at the time and didn't hurt user metrics <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Airbnb New Tab**: A small experiment at Airbnb to open search results in a new tab instead of directly navigating to the listing led to one of the biggest wins in search <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This concept had previously yielded highly beneficial results at Microsoft in 2008 for Hotmail and MSN <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

These "gold nuggets" are rare, with most gains being "inch by inch" improvements <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>. For example, Bing's relevance team aimed to improve their overall evaluation criterion by 2% annually through many small gains <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.

### Surprising Losses and Learning
It's crucial to learn from failures and unexpected negative results. A surprising experiment is one where the estimated result and the actual result differ significantly <a class="yt-timestamp" data-t="01:17:40">[01:17:40]</a>.
*   **Windows Indexer**: An improvement to the Windows indexer showed better indexing offline, but in an experiment, it significantly killed battery life by consuming more CPU on laptops <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a>. This unexpected negative outcome led to incorporating battery life as a critical factor in future designs <a class="yt-timestamp" data-t="01:19:17">[01:19:17]</a>.
*   **Bing Social Integration**: A major investment in integrating social feeds (Twitter, Facebook) into Bing search results, involving 100 person-years of effort, failed completely <a class="yt-timestamp" data-t="01:22:50">[01:22:50]</a>, <a class="yt-timestamp" data-t="01:23:08">[01:23:08]</a>. All experiments showed negative to flat results, leading to its eventual abortion after about a year and a half <a class="yt-timestamp" data-t="01:23:17">[01:23:17]</a>. Similar social features also failed at Netflix and Airbnb <a class="yt-timestamp" data-t="01:24:06">[01:24:06]</a>.
*   **Amazon Email Campaigns**: Initially, Amazon's email team credited revenue whenever a user purchased something after coming from an email, leading to excessive spamming as the team ramped up email volume to claim more money <a class="yt-timestamp" data-t="01:33:31">[01:33:31]</a>, <a class="yt-timestamp" data-t="01:34:01">[01:34:01]</a>. By modeling the "cost of spamming" (e.g., value lost from unsubscribes), it was discovered that over half the campaigns were negative in terms of long-term value <a class="yt-timestamp" data-t="01:35:07">[01:35:07]</a>. This led to a new feature allowing users to unsubscribe from specific campaign types, preserving overall lifetime value <a class="yt-timestamp" data-t="01:35:57">[01:35:57]</a>.

To retain [[challenges_and_insights_in_product_management | institutional memory]] of these learnings, organizations should:
*   Document successes and failures in a shared repository <a class="yt-timestamp" data-t="01:19:35">[01:19:35]</a>.
*   Enable searching of past experiments by keywords <a class="yt-timestamp" data-t="01:19:52">[01:19:52]</a>.
*   Hold regular meetings (e.g., quarterly) to discuss the most surprising experiments (both wins and losses) <a class="yt-timestamp" data-t="01:20:33">[01:20:33]</a>.

## Avoiding Common Pitfalls

### Big Redesigns Often Fail
Full product redesigns rarely result in positive outcomes <a class="yt-timestamp" data-t="01:36:33">[01:36:33]</a>. Kohavi has published examples of large redesigns that "dramatically failed" <a class="yt-timestamp" data-t="01:36:59">[01:36:59]</a>. The recommended approach is to implement redesigns incrementally, testing each step to learn and adjust, rather than launching 17 new changes at once, most of which are likely to fail <a class="yt-timestamp" data-t="01:37:05">[01:37:05]</a>.
*   **Sunk Cost Fallacy**: A significant [[challenges_and_pitfalls_in_product_management | pitfall]] is the "sunk cost fallacy" where teams insist on launching a feature after investing much time and resources, even if experiments show it's negative <a class="yt-timestamp" data-t="01:37:41">[01:37:41]</a>.
*   **"No Ship on Flat"**: If an experiment shows no significant positive impact (flat results), it should generally not be shipped due to maintenance overhead and complicating the codebase <a class="yt-timestamp" data-t="01:44:30">[01:44:30]</a>. Exceptions exist for legal requirements, but even then, teams should experiment to find the option that "hurts the least" <a class="yt-timestamp" data-t="01:45:17">[01:45:17]</a>.

While large bets or radical redesigns are sometimes necessary to break out of a local maximum, be prepared for failure. Kohavi advises allocating resources to high-risk, high-reward ideas, but accepting that "most will fail eighty percent of the time" <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>, <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.

### The [[the_role_of_trust_in_successful_experimentation | Importance of Trust]] and Valid Results
A key challenge is ensuring the trustworthiness of experiment results. An experimentation platform serves as a safety net (allowing quick aborts of bad launches) and an oracle (providing reliable results) <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a>. Trust is easily lost but hard to build <a class="yt-timestamp" data-t="00:52:39">[00:52:39]</a>.

#### Sample Ratio Mismatch (SRM)
The most common sign of an invalid experiment is a Sample Ratio Mismatch (SRM) <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. If an experiment is designed to send 50% of users to control and 50% to treatment, any significant deviation from this split (e.g., 50.2% vs. 49.8% in a million-user experiment) is a red flag <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>, <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>.
*   SRM can occur in about 8% of experiments even in mature platforms like Microsoft's <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a>.
*   Common causes include bots hitting control/treatment differently <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>, data pipeline issues, or interactions with other campaigns <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>.
*   If SRM is detected, results cannot be trusted <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a>. Initially, warnings were ignored, leading platforms to blank out scorecards or highlight all numbers with a red line to prevent misinterpretation <a class="yt-timestamp" data-t="00:59:32">[00:59:32]</a>.

#### [[challenges_and_insights_in_product_management | Twyman's Law]]
"If any figure that looks interesting or different is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. If an experiment shows a surprisingly large movement (e.g., 10% when normal is 1%), it should be investigated before celebrating, as 9 out of 10 times, a flaw is found <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>, <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

#### Misunderstanding P-values
A common misinterpretation of a p-value is that `1 - p-value` represents the probability that the treatment is better than control <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>, which is incorrect <a class="yt-timestamp" data-t="01:02:59">[01:02:59]</a>. A p-value is a conditional probability, assuming the null hypothesis is true <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. To get the true probability of a successful hypothesis, Bayes' Rule is needed, incorporating prior probabilities (historical failure rates) <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.
*   For example, at Airbnb search, with an 8% success rate of ideas, a statistically significant result (p-value < 0.05) has a 26% chance of being a false positive, not 5% <a class="yt-timestamp" data-t="01:04:35">[01:04:35]</a>.
*   This highlights the need to lower the p-value threshold (e.g., below 0.01) and consider replication for high-stakes experiments to achieve a much lower false positive rate <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>.

## Organizational Resistance and Cultural Shift

### Initial Resistance
When Kohavi first proposed [[building_and_optimizing_an_experimentation_platform | building an experimentation platform]] at Microsoft, the classical response was "we have better PMs here," denying that 50% of their ideas could fail <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>, <a class="yt-timestamp" data-t="01:40:51">[01:40:51]</a>. Bing's success in implementing experimentation at scale helped demonstrate the value to other groups, including Office, which eventually adopted it <a class="yt-timestamp" data-t="01:40:45">[01:40:45]</a>.

### [[creating_a_culture_of_experimentation_in_a_company | Shifting Culture]]
To overcome resistance and foster an experiment-driven culture:
1.  **Find a Beachhead**: Start with a team where experimentation is easy to run, i.e., they launch frequently (e.g., weekly or multiple times a day) <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>.
2.  **Define a Clear Overall Evaluation Criterion (OEC)**: Clearly define what the team is optimizing for <a class="yt-timestamp" data-t="01:09:01">[01:09:01]</a>. This can be challenging; for instance, on Microsoft.com, "time on site" was a problematic OEC because half the team saw it as positive (engagement) and the other half as negative (failure to quickly find information on a support site) <a class="yt-timestamp" data-t="01:09:55">[01:09:55]</a>. The OEC should be causally predictive of the long-term lifetime value of the user <a class="yt-timestamp" data-t="01:32:07">[01:32:07]</a>.
3.  **Invest in a Platform**: [[building_and_optimizing_an_experimentation_platform | Building a robust experimentation platform]] drives the marginal cost of running experiments towards zero, enabling self-service and reducing reliance on manual data analysis <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>. At Bing, users could define 10,000 metrics for their scorecard, necessitating templates for different experiment types <a class="yt-timestamp" data-t="01:10:58">[01:10:58]</a>. A mature platform reduces the need for many data scientists to interpret results <a class="yt-timestamp" data-t="01:11:29">[01:11:29]</a>.

While there are many [[challenges_and_insights_in_product_management | challenges]] and failures inherent in experimentation, embracing this reality and focusing on building trust and learning from every result is key to successful long-term growth.