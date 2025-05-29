---
title: Lessons from large scale experiments at companies like Amazon Microsoft and Airbnb
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Ronnie Kohavi is widely regarded as a leading expert in A/B testing and experimentation, having held significant roles at major tech companies such as Microsoft (Corporate Vice President, leading their experimentation platform team), Amazon (Director of Data Mining and Personalization), and Airbnb (VP and Technical Fellow of Relevance) <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a> <a class="yt-timestamp" data-t="01:17:34">[01:17:34]</a>. His insights into building and maintaining robust experimentation cultures are drawn from these extensive experiences.

## The "Test Everything" Philosophy

Kohavi is a strong advocate for testing every code change and new feature through experiments <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="02:11:09">[02:11:09]</a>. This approach stems from the observation that even minor bug fixes or small changes can lead to surprising, unexpected impacts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> <a class="yt-timestamp" data-t="02:11:21">[02:11:21]</a>. He asserts that it's impossible to experiment too much, and while some experiments focus on incremental improvements, resources must also be allocated to high-risk, high-reward ideas that are "most likely to fail" but could be "home runs" if successful <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="02:22:03">[02:22:03]</a> <a class="yt-timestamp" data-t="02:22:11">[02:22:11]</a>.

### Surprising Outcomes and Twyman's Law

Experiments often yield unexpected results, highlighting humanity's poor ability to predict outcomes <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a>.
*   **Bing Search Ads:** A seemingly trivial change on Bing, moving the second line of an ad to the first to make the title larger, resulted in a 12% increase in revenue <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a> <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This simple adjustment, implemented in a couple of days, was worth $100 million at the time and didn't negatively impact user metrics <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a> <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Airbnb New Tab:** At [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]], a small experiment to open search results in a new tab was one of the "biggest wins" in search <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a> <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This idea had been explored earlier, even at Microsoft, and consistently showed high benefit <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a> <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Windows Indexer:** An experiment to improve the Windows indexer, which showed offline testing improvements in indexing and relevance, unexpectedly "killed the battery life" of laptops due to increased CPU consumption <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a> <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This revealed an unforeseen factor (battery life) to consider in future designs <a class="yt-timestamp" data-t="01:19:17">[01:19:17]</a>.

These results underscore **Twyman's Law**: "If any figure that looks interesting or different is usually wrong" <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a> <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. When an experiment yields a result that appears "too good to be true," it often indicates a flaw in the experiment <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a>. Kohavi estimates that nine out of ten times this rule is applied, a flaw is found <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

## High Failure Rates and Balancing Bets

The vast majority of ideas fail in experiments:
*   At Microsoft, about two-thirds of ideas failed <a class="yt-timestamp" data-t="01:13:32">[01:13:32]</a> <a class="yt-timestamp" data-t="01:13:43">[01:13:43]</a>.
*   At Bing, a more optimized domain, the failure rate was around 85% <a class="yt-timestamp" data-t="01:13:48">[01:13:48]</a>.
*   At [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] search relevance, 92% of experiments failed to improve the target metric <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.

Even large, strategic initiatives can fail. For instance, Bing's 100-person-year effort to integrate with social media (Twitter and Facebook) ultimately failed to improve search results <a class="yt-timestamp" data-t="02:22:50">[02:22:50]</a>.
[[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] also had a social component that had no impact <a class="yt-timestamp" data-t="02:42:12">[02:42:12]</a>.

> "If you go for something big, try it out but be ready to fail eighty percent of the time." <a class="yt-timestamp" data-t="02:22:36">[02:22:36]</a>

Despite the high failure rate, large bets are necessary to break out of local optima <a class="yt-timestamp" data-t="04:29:57">[04:29:57]</a>. The key is to allocate resources for such endeavors while acknowledging the high probability of failure <a class="yt-timestamp" data-t="04:31:07">[04:31:07]</a>. Most wins, however, are incremental, achieved "inch by inch" <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>.

## The Overall Evaluation Criterion (OEC)

The **Overall Evaluation Criterion (OEC)** is crucial for A/B testing, defining "what you are optimizing for" beyond simple metrics like revenue <a class="yt-timestamp" data-t="02:28:13">[02:28:13]</a>. Focusing solely on short-term gains like revenue can lead to "bad things" that hurt the user experience in the long term <a class="yt-timestamp" data-t="02:28:40">[02:28:40]</a>.

The OEC often involves:
*   **Countervailing Metrics:** These metrics ensure that increasing one desirable outcome (e.g., revenue) doesn't harm another critical one (e.g., user experience). For search engines, this might mean increasing revenue without hurting metrics like user churn or time to find a successful result <a class="yt-timestamp" data-t="02:28:45">[02:28:45]</a> <a class="yt-timestamp" data-t="02:29:11">[02:29:11]</a>.
*   **Constraint Optimization:** Frame the problem as increasing a metric (e.g., revenue) within a given constraint (e.g., average ad real estate) <a class="yt-timestamp" data-t="02:29:41">[02:29:41]</a>.
*   **Long-term Value:** The OEC should be "causally predictive of the lifetime value of the user" <a class="yt-timestamp" data-t="03:20:07">[03:20:07]</a>. For example, at [[leadership_principles_at_amazon | Amazon]]'s email team, simply crediting purchases from emails led to spamming users. The solution involved modeling the cost of spamming (e.g., losing future lifetime value from unsubscribes) to balance short-term revenue with long-term user health <a class="yt-timestamp" data-t="03:32:48">[03:32:48]</a> <a class="yt-timestamp" data-t="03:41:20">[03:41:20]</a>. Similarly, for [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]], conversion rate could be balanced with long-term guest satisfaction (e.g., future ratings of a listing) <a class="yt-timestamp" data-t="03:11:02">[03:11:02]</a>.

When defining an OEC, teams must agree on the direction of key metrics; if half the room thinks "more time on site" is good and half think it's bad, the OEC is flawed <a class="yt-timestamp" data-t="01:09:40">[01:09:40]</a> <a class="yt-timestamp" data-t="01:10:13">[01:10:13]</a>.

## Building Trust in Experimentation

Trust is paramount for an experimentation platform, which serves as both a safety net for bad launches and an oracle for results <a class="yt-timestamp" data-t="05:01:54">[05:01:54]</a> <a class="yt-timestamp" data-t="05:02:03">[05:02:03]</a>.

### Pitfalls to Avoid:
*   **Misinterpreting P-values:** The common interpretation of a p-value (e.g., 1-p-value as probability of success) is incorrect <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>. P-values assume the null hypothesis is true, and the true false positive risk is often much higher than the nominal 5% (e.g., 26% at [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] search) <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>.
*   **Early Stopping:** Stopping an experiment prematurely when the p-value appears statistically significant (e.g., as early Optimizely allowed) "inflates your ... false positive rate materially" <a class="yt-timestamp" data-t="05:31:01">[05:31:01]</a> <a class="yt-timestamp" data-t="05:42:01">[05:42:01]</a>. This led to loss of trust when results didn't materialize over time <a class="yt-timestamp" data-t="05:51:11">[05:51:11]</a>.
*   **Sample Ratio Mismatch (SRM):** This is the most common issue, occurring when the allocation of users to control and treatment groups deviates from the intended ratio (e.g., 50/50) beyond chance <a class="yt-timestamp" data-t="05:55:01">[05:55:01]</a>. SRMs indicate underlying problems (e.g., data pipeline issues, bot traffic) and invalidate results <a class="yt-timestamp" data-t="05:57:01">[05:57:01]</a>. Companies like Microsoft found 8% of experiments suffered from SRM <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>, and early adopters of SRM detection reported similar rates <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>.
*   **Ignoring Warnings:** Teams often ignore warnings about invalid experiments due to a natural bias towards success <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a> <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>.

## Scaling Experimentation and Culture Shift

Starting an experimentation culture requires patience and strategy:
*   **When to Start:** An organization needs "at least tens of thousands of users" for statistics to work <a class="yt-timestamp" data-t="02:53:14">[02:53:14]</a>. For meaningful changes (5-10% beneficial), around 200,000 users are needed <a class="yt-timestamp" data-t="02:53:57">[02:53:57]</a>. Below this, focus on building the culture and platform <a class="yt-timestamp" data-t="02:57:52">[02:57:52]</a>.
*   **Build vs. Buy:** It's often a mix; while older companies had to build platforms from scratch, good third-party solutions exist today <a class="yt-timestamp" data-t="02:59:58">[02:59:58]</a> <a class="yt-timestamp" data-t="03:07:06">[03:07:06]</a>.
*   **Culture Shift:** At Microsoft, the successful large-scale experimentation at Bing helped spread the culture to other groups, including Office, by showing surprising results and through cross-pollination of talent <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a> <a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a> <a class="yt-timestamp" data-t="01:40:48">[01:40:48]</a>.
*   **Start Small and Fast:** Begin with a team that launches frequently (e.g., weekly or daily) and has a clear OEC <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>.
*   **Document Learnings:** Crucially, organizations must document successes and failures and their learnings to build institutional memory <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>. Regularly reviewing "most surprising" experiments (both winners and losers) is key to learning and fostering the "flywheel of experimentation" <a class="yt-timestamp" data-t="01:17:24">[01:17:24]</a> <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.
*   **Iterate vs. Redesign:** Full product redesigns often fail, forcing teams to "claw back what they just hurt" <a class="yt-timestamp" data-t="03:36:33">[03:36:33]</a>. It's better to make incremental changes and test along the way, or if a complete redesign is done, be prepared for failure and avoid the "sunk cost fallacy" <a class="yt-timestamp" data-t="03:40:02">[03:40:02]</a> <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>.

At Microsoft, they were running 20,000-25,000 experiments annually by 2019, starting around 100 new treatments every working day <a class="yt-timestamp" data-t="02:04:02">[02:04:02]</a> <a class="yt-timestamp" data-t="02:14:02">[02:14:02]</a>. This scale is achieved by building a robust platform that makes the "incremental cost of running an experiment approach zero" <a class="yt-timestamp" data-t="02:53:29">[02:53:29]</a>.

## Speeding Up Experiments

To run experiments faster and get quicker results:
*   **Automated Scorecards:** The platform should provide a scorecard "soon after" an experiment finishes, eliminating the need for a data scientist to spend a week analyzing <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>.
*   **Variance Reduction Techniques:** Methods like capping skewed metrics (e.g., booking nights, revenue) or using pre-experiment data (e.g., CUPED technique) can reduce variance, requiring fewer users and leading to faster statistically significant results <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a> <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>.

Ultimately, experimentation provides an "oracle" that gives data, serving as the "arbiter" to determine whether users truly benefit from changes, even when individuals are excited or believe an idea is good <a class="yt-timestamp" data-t="02:42:27">[02:42:27]</a> <a class="yt-timestamp" data-t="02:43:52">[02:43:52]</a>.# Lessons from Large-Scale Experimentation at Tech Giants

Ronnie Kohavi is widely regarded as a leading expert in A/B testing and experimentation, having held significant roles at major tech companies such as Microsoft (Corporate Vice President, leading their experimentation platform team), [[leadership_principles_at_amazon | Amazon]] (Director of Data Mining and Personalization), and [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] (VP and Technical Fellow of Relevance) <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a> <a class="yt-timestamp" data-t="01:17:34">[01:17:34]</a>. His insights into building and maintaining robust experimentation cultures are drawn from these extensive experiences.

## The "Test Everything" Philosophy

Kohavi is a strong advocate for testing every code change and new feature through experiments <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="02:11:09">[02:11:09]</a>. This approach stems from the observation that even minor bug fixes or small changes can lead to surprising, unexpected impacts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> <a class="yt-timestamp" data-t="02:11:21">[02:11:21]</a>. He asserts that it's impossible to experiment too much, and while some experiments focus on incremental improvements, resources must also be allocated to high-risk, high-reward ideas that are "most likely to fail" but could be "home runs" if successful <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="02:22:03">[02:22:03]</a> <a class="yt-timestamp" data-t="02:22:11">[02:22:11]</a>.

### Surprising Outcomes and Twyman's Law

Experiments often yield unexpected results, highlighting humanity's poor ability to predict outcomes <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a>.
*   **Bing Search Ads:** A seemingly trivial change on Bing, moving the second line of an ad to the first to make the title larger, resulted in a 12% increase in revenue <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a> <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This simple adjustment, implemented in a couple of days, was worth $100 million at the time and didn't negatively impact user metrics <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a> <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **[[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] New Tab:** At [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]], a small experiment to open search results in a new tab was one of the "biggest wins" in search <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a> <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This idea had been explored earlier, even at Microsoft, and consistently showed high benefit <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a> <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Windows Indexer:** An experiment to improve the Windows indexer, which showed offline testing improvements in indexing and relevance, unexpectedly "killed the battery life" of laptops due to increased CPU consumption <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a> <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This revealed an unforeseen factor (battery life) to consider in future designs <a class="yt-timestamp" data-t="01:19:17">[01:19:17]</a>.

These results underscore **Twyman's Law**: "If any figure that looks interesting or different is usually wrong" <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a> <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. When an experiment yields a result that appears "too good to be true," it often indicates a flaw in the experiment <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a>. Kohavi estimates that nine out of ten times this rule is applied, a flaw is found <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

## High Failure Rates and Balancing Bets

The vast majority of ideas fail in experiments:
*   At Microsoft, about two-thirds of ideas failed <a class="yt-timestamp" data-t="01:13:32">[01:13:32]</a> <a class="yt-timestamp" data-t="01:13:43">[01:13:43]</a>.
*   At Bing, a more optimized domain, the failure rate was around 85% <a class="yt-timestamp" data-t="01:13:48">[01:13:48]</a>.
*   At [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] search relevance, 92% of experiments failed to improve the target metric <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.

Even large, strategic initiatives can fail. For instance, Bing's 100-person-year effort to integrate with social media (Twitter and Facebook) ultimately failed to improve search results <a class="yt-timestamp" data-t="02:22:50">[02:22:50]</a>. [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] also had a social component that had no impact <a class="yt-timestamp" data-t="02:42:12">[02:42:12]</a>.

> "If you go for something big, try it out but be ready to fail eighty percent of the time." <a class="yt-timestamp" data-t="02:22:36">[02:22:36]</a>

Despite the high failure rate, large bets are necessary to break out of local optima <a class="yt-timestamp" data-t="04:29:57">[04:29:57]</a>. The key is to allocate resources for such endeavors while acknowledging the high probability of failure <a class="yt-timestamp" data-t="04:31:07">[04:31:07]</a>. Most wins, however, are incremental, achieved "inch by inch" <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>.

## The Overall Evaluation Criterion (OEC)

The **Overall Evaluation Criterion (OEC)** is crucial for A/B testing, defining "what you are optimizing for" beyond simple metrics like revenue <a class="yt-timestamp" data-t="02:28:13">[02:28:13]</a>. Focusing solely on short-term gains like revenue can lead to "bad things" that hurt the user experience in the long term <a class="yt-timestamp" data-t="02:28:40">[02:28:40]</a>.

The OEC often involves:
*   **Countervailing Metrics:** These metrics ensure that increasing one desirable outcome (e.g., revenue) doesn't harm another critical one (e.g., user experience). For search engines, this might mean increasing revenue without hurting metrics like user churn or time to find a successful result <a class="yt-timestamp" data-t="02:28:45">[02:28:45]</a> <a class="yt-timestamp" data-t="02:29:11">[02:29:11]</a>.
*   **Constraint Optimization:** Frame the problem as increasing a metric (e.g., revenue) within a given constraint (e.g., average ad real estate) <a class="yt-timestamp" data-t="02:29:41">[02:29:41]</a>.
*   **Long-term Value:** The OEC should be "causally predictive of the lifetime value of the user" <a class="yt-timestamp" data-t="03:20:07">[03:20:07]</a>. For example, at [[leadership_principles_at_amazon | Amazon]]'s email team, simply crediting purchases from emails led to spamming users. The solution involved modeling the cost of spamming (e.g., losing future lifetime value from unsubscribes) to balance short-term revenue with long-term user health <a class="yt-timestamp" data-t="03:32:48">[03:32:48]</a> <a class="yt-timestamp" data-t="03:41:20">[03:41:20]</a>. Similarly, for [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]], conversion rate could be balanced with long-term guest satisfaction (e.g., future ratings of a listing) <a class="yt-timestamp" data-t="03:11:02">[03:11:02]</a>.

When defining an OEC, teams must agree on the direction of key metrics; if half the room thinks "more time on site" is good and half think it's bad, the OEC is flawed <a class="yt-timestamp" data-t="01:09:40">[01:09:40]</a> <a class="yt-timestamp" data-t="01:10:13">[01:10:13]</a>.

## Building Trust in Experimentation

Trust is paramount for an experimentation platform, which serves as both a safety net for bad launches and an oracle for results <a class="yt-timestamp" data-t="05:01:54">[05:01:54]</a> <a class="yt-timestamp" data-t="05:02:03">[05:02:03]</a>.

### Pitfalls to Avoid:
*   **Misinterpreting P-values:** The common interpretation of a p-value (e.g., 1-p-value as probability of success) is incorrect <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>. P-values assume the null hypothesis is true, and the true false positive risk is often much higher than the nominal 5% (e.g., 26% at [[lessons_learned_from_airbnbs_growth_and_culture | Airbnb]] search) <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>.
*   **Early Stopping:** Stopping an experiment prematurely when the p-value appears statistically significant (e.g., as early Optimizely allowed) "inflates your ... false positive rate materially" <a class="yt-timestamp" data-t="05:31:01">[05:31:01]</a> <a class="yt-timestamp" data-t="05:42:01">[05:42:01]</a>. This led to loss of trust when results didn't materialize over time <a class="yt-timestamp" data-t="05:51:11">[05:51:11]</a>.
*   **Sample Ratio Mismatch (SRM):** This is the most common issue, occurring when the allocation of users to control and treatment groups deviates from the intended ratio (e.g., 50/50) beyond chance <a class="yt-timestamp" data-t="05:55:01">[05:55:01]</a>. SRMs indicate underlying problems (e.g., data pipeline issues, bot traffic) and invalidate results <a class="yt-timestamp" data-t="05:57:01">[05:57:01]</a>. Companies like Microsoft found 8% of experiments suffered from SRM <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>, and early adopters of SRM detection reported similar rates <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>.
*   **Ignoring Warnings:** Teams often ignore warnings about invalid experiments due to a natural bias towards success <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a> <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>.

## Scaling Experimentation and Culture Shift

Starting an experimentation culture requires patience and strategy:
*   **When to Start:** An organization needs "at least tens of thousands of users" for statistics to work <a class="yt-timestamp" data-t="02:53:14">[02:53:14]</a>. For meaningful changes (5-10% beneficial), around 200,000 users are needed <a class="yt-timestamp" data-t="02:53:57">[02:53:57]</a>. Below this, focus on building the culture and platform <a class="yt-timestamp" data-t="02:57:52">[02:57:52]</a>.
*   **Build vs. Buy:** It's often a mix; while older companies had to build platforms from scratch, good third-party solutions exist today <a class="yt-timestamp" data-t="02:59:58">[02:59:58]</a> <a class="yt-timestamp" data-t="03:07:06">[03:07:06]</a>.
*   **Culture Shift:** At Microsoft, the successful large-scale experimentation at Bing helped spread the culture to other groups, including Office, by showing surprising results and through cross-pollination of talent <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a> <a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a> <a class="yt-timestamp" data-t="01:40:48">[01:40:48]</a>.
*   **Start Small and Fast:** Begin with a team that launches frequently (e.g., weekly or daily) and has a clear OEC <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>.
*   **Document Learnings:** Crucially, organizations must document successes and failures and their learnings to build institutional memory <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>. Regularly reviewing "most surprising" experiments (both winners and losers) is key to learning and fostering the "flywheel of experimentation" <a class="yt-timestamp" data-t="01:17:24">[01:17:24]</a> <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.
*   **Iterate vs. Redesign:** Full product redesigns often fail, forcing teams to "claw back what they just hurt" <a class="yt-timestamp" data-t="03:36:33">[03:36:33]</a>. It's better to make incremental changes and test along the way, or if a complete redesign is done, be prepared for failure and avoid the "sunk cost fallacy" <a class="yt-timestamp" data-t="03:40:02">[03:40:02]</a> <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>.

At Microsoft, they were running 20,000-25,000 experiments annually by 2019, starting around 100 new treatments every working day <a class="yt-timestamp" data-t="02:04:02">[02:04:02]</a> <a class="yt-timestamp" data-t="02:14:02">[02:14:02]</a>. This scale is achieved by [[building_a_product_at_a_large_company | building a robust platform]] that makes the "incremental cost of running an experiment approach zero" <a class="yt-timestamp" data-t="02:53:29">[02:53:29]</a>.

## Speeding Up Experiments

To run experiments faster and get quicker results:
*   **Automated Scorecards:** The platform should provide a scorecard "soon after" an experiment finishes, eliminating the need for a data scientist to spend a week analyzing <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>.
*   **Variance Reduction Techniques:** Methods like capping skewed metrics (e.g., booking nights, revenue) or using pre-experiment data (e.g., CUPED technique) can reduce variance, requiring fewer users and leading to faster statistically significant results <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a> <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>.

Ultimately, experimentation provides an "oracle" that gives data, serving as the "arbiter" to determine whether users truly benefit from changes, even when individuals are excited or believe an idea is good <a class="yt-timestamp" data-t="02:42:27">[02:42:27]</a> <a class="yt-timestamp" data-t="02:43:52">[02:43:52]</a>.