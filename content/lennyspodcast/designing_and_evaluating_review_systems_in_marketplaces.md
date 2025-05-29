---
title: Designing and evaluating review systems in marketplaces
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Online marketplaces, such as Airbnb, Uber, and Upwork, fundamentally operate by "taking away" the friction associated with finding and making transactions between parties <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>. This friction includes finding a place to stay, a driver, or someone to hire <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. Both sides of a marketplace – for example, hosts and guests on Airbnb, or drivers and riders on Uber – are considered customers of the platform <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. The value proposition of a marketplace lies in reducing these [[challenges_and_strategies_in_operating_online_marketplaces | transaction costs]] <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.

Data and [[key_performance_indicators_for_marketplaces | data science]] are central to building successful marketplaces <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Marketplaces can be constantly re-architected and re-evaluated with data, unlike ancient markets made of stone <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.

## The Marketplace Data Science Flywheel <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>

The operation of online marketplaces often involves a three-part "data science flywheel":
1.  **Finding Matches**: Helping buyers and sellers find potential partners (e.g., a guest finding a listing, or a host finding a guest) <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
2.  **Making Matches**: Facilitating the actual transaction or connection once potential partners are found (e.g., an employer deciding who to interview and hire from multiple applicants) <a class="yt-timestamp" data-t="09:51:00">[09:51:51]</a>.
3.  **Learning About Matches**: Gathering information and [[customer_feedback_and_product_improvement | feedback]] after a match is made to improve future interactions <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>. This step is where rating and review systems are crucial, as they feed data back into the first two stages, enabling better [[balancing_supply_and_demand_in_marketplaces | matching algorithms]] <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

## Challenges in Designing Review Systems <a class="yt-timestamp" data-t="02:07:00">[02:07:07]</a>

Despite their importance, review systems face several challenges:

*   **Rating Inflation**: A common phenomenon where the median rating on a marketplace tends to increase over time <a class="yt-timestamp" data-t="01:02:52">[01:02:52]</a>. This can be due to:
    *   **Reciprocity**: Users feeling obligated to leave a positive review, especially if they interacted directly with the other party <a class="yt-timestamp" data-t="01:03:20">[01:03:20]</a>.
    *   **Norming**: As overall ratings rise, users adjust their expectations, perceiving a four-star rating, for example, as "screwing this person over," even if it was once considered good <a class="yt-timestamp" data-t="01:03:36">[01:03:36]</a>.
*   **Impact of Averaging**: Defaulting to simply averaging ratings can have significant "distributional consequences" <a class="yt-timestamp" data-t="01:04:57">[01:04:57]</a>. An established entity with many reviews is largely unaffected by a single new review, while a new participant's first negative review can be devastating, potentially causing an 8% immediate hit to expected revenue or even leading to exit from the platform <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.
*   **The "Sound of Silence"**: A significant amount of information is contained in ratings that are *not* left <a class="yt-timestamp" data-t="01:07:47">[01:07:47]</a>. For example, not leaving a review is often easier than leaving a bad one, and this absence of feedback can be predictive of performance <a class="yt-timestamp" data-t="01:08:24">[01:08:24]</a>.

## Strategies for Designing Better Review Systems

*   **Renorming Rating Labels**: Instead of generic "poor to excellent" scales, use labels that require more thought, such as "exceeded expectations" <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.
*   **Contextual Comparisons**: Ask users to compare their experience to past, highly-rated experiences <a class="yt-timestamp" data-t="01:04:06">[01:04:06]</a>. This makes it easier for users to provide more nuanced feedback than simply "dinging" someone with a lower star rating <a class="yt-timestamp" data-t="01:04:26">[01:04:26]</a>.
*   **Mitigating Averaging Impact**: For new participants, consider using a "prior belief" in averaging. This involves averaging their few reviews with a generalized prior belief, potentially pulling up a new user's rating if they received an unlucky negative first review <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. Some platforms delay showing ratings until a few have been accumulated <a class="yt-timestamp" data-t="01:05:42">[01:05:42]</a>.
*   **Double-Blind Reviews**: A system where neither party sees the other's review until both have submitted theirs <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>. While intended to increase honesty and accuracy, a significant impact seen at Airbnb was a substantial increase in review rate due to the incentive to see the other person's feedback <a class="yt-timestamp" data-t="01:07:31">[01:07:31]</a>. This provides more valuable data from the "sound of silence" <a class="yt-timestamp" data-t="01:08:20">[01:08:20]</a>.

## Evaluating Review Systems Through Experimentation <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>

A core function of data scientists in marketplaces is to help the business make decisions that drive value <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

### Prediction vs. Decision-Making <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>

A common pitfall is focusing data science efforts purely on prediction (identifying patterns and correlations) rather than decision-making (understanding causation) <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>. For example, predicting who is most likely to be hired is different from understanding how a ranking algorithm *causes* better matches <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>. The true question is: "How much more are they going to spend on my platform *because* I sent them that promotion?" <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. This shift in thinking from machine learning to causal inference is critical for effectively evaluating system changes, including those to review mechanisms <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>.

### The Role of Experiments <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>

A/B testing is essential for determining if a change truly leads to desired outcomes like more bookings or revenue <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>. However, there are challenges:

*   **Micro-Optimization vs. Big Opportunities**: Companies can become risk-averse, focusing on incremental changes and running experiments for too long, leading to "local minima/maxima" and missing larger opportunities <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.
*   **The "Cost of Learning"**: Understanding that learning is not free is crucial <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>. Running experiments, especially with "control" groups that don't receive the new feature, incurs a cost, like the millions of dollars lost by a real estate platform's unauthorized holdout group <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>. This cost is a necessary investment to learn which changes are truly impactful <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.
*   **Cultural Shift from "Wins" to "Learning"**: If data scientists are judged solely on "wins" (statistically significant positive impacts), they are incentivized to test incremental changes and prolong experiments to demonstrate impact, leading to a culture where "failures" (experiments that don't "win") are seen as wasted time <a class="yt-timestamp" data-t="00:42:30">[00:42:30]</a>. A healthier culture embraces a "hypothesis-driven" approach, where every experiment, even those that "fail," provides valuable learning about the business <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>. For example, a badging system experiment that doesn't increase bookings might still teach how attention is reallocated among participants <a class="yt-timestamp" data-t="00:44:52">[00:44:52]</a>.
*   **[[integrating_customer_feedback_into_product_development | Integrating Past Learning with New Data]]**: Traditional (frequentist) statistical methods used in A/B testing often "throw past learning away" <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. Bayesian A/B testing, however, allows for incorporating prior beliefs (derived from past experiments or business knowledge) with new experiment data to arrive at a conclusion <a class="yt-timestamp" data-t="00:56:25">[00:56:25]</a>. This encourages a culture where contributing information that shapes future analyses is rewarded, even if individual experiments don't yield direct "wins" <a class="yt-timestamp" data-t="00:56:59">[00:56:59]</a>.

The "whack-a-mole" nature of marketplaces means that changes often create [[expansion_strategies_for_marketplaces | winners and losers]] by moving attention and inventory around <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>. Understanding whether the created winners are more important to the business than the losers is a key aspect of [[challenges_and_strategies_in_operating_online_marketplaces | marketplace management]] <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

## Conclusion

Despite their critical role in information gathering and trust-building, rating systems are "understudied" <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>. The shift from simply observing what happened (passive data collection, like booking duration) to actively designing and analyzing feedback systems (like star ratings) and understanding their impact on market dynamics and fairness remains a significant area for advancement <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>. The field of data science, particularly with the [[evals_and_their_importance_in_ai_product_management | advent of AI]], has massively expanded the frontier of hypotheses and ideas, putting more pressure on humans to critically funnel down and interpret insights, ensuring that [[using_qualitative_feedback_for_product_development | product improvements]] are driven by causal understanding rather than mere prediction <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.