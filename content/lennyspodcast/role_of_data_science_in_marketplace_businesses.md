---
title: Role of data science in marketplace businesses
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Online marketplaces are complex systems that, at scale, primarily sell the removal of friction or "transaction costs" between buyers and sellers <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>. For example, Airbnb doesn't sell rooms; it eliminates the friction of finding a place to stay. Similarly, Uber doesn't sell rides, but rather the friction of finding a driver <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. Both sides of the marketplace are considered customers of the platform, as both depend on the platform to facilitate transactions <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.

Ramesh Johari, a professor at Stanford University, specializes in the design and [[challenges_and_strategies_in_operating_online_marketplaces | operation of online marketplaces]], having advised major players like Airbnb, Uber, Stripe, Bumble, Stitch Fix, and Upwork <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. He describes marketplaces as a "game of whack-a-mole," where changes often create winners and losers due to the reallocation of attention and inventory <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Why Data is Central to Marketplaces

Unlike ancient markets made of stone, modern technology allows for constant re-architecture of online marketplaces <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. This flexibility is largely thanks to the strategic use of data and algorithms <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>. Data science is crucial for managing attention and inventory across the marketplace <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

## The Three Core Problems Data Science Addresses

Every online marketplace, regardless of its vertical, grapples with three fundamental problems that data science helps solve <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>:

1.  **Finding Potential Matches** <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>:
    *   This involves connecting buyers with sellers (e.g., finding a host for a traveler, or a job for a freelancer) <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
    *   Core components include search and recommendation systems <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.

2.  **Making the Match** <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>:
    *   Once potential matches are found, data science assists in the decision-making process (e.g., helping an employer choose which applicant to hire from multiple options) <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.
    *   This involves ranking and triaging algorithms <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

3.  **Learning About Matches** <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>:
    *   After a match is made, the platform gathers feedback to improve future interactions <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>.
    *   This includes [[key_performance_indicators_for_marketplaces | rating systems]] and feedback mechanisms (both active, like star ratings, and passive, like early departures) <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.
    *   This continuous learning loop allows the marketplace to refine its matching and finding algorithms <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>.

## Distinguishing Prediction from Decision-Making

A crucial aspect of [[building_effective_data_teams | effective data science]] in marketplaces is understanding the difference between prediction and decision-making <a class="yt-timestamp" data-t="30:02:00">[30:02:00]</a>. While machine learning models are excellent at predicting outcomes based on past data (correlation) <a class="yt-timestamp" data-t="31:00:00">[31:00:00]</a>, the goal for a business is to make decisions that drive desired future outcomes (causation) <a class="yt-timestamp" data-t="33:33:00">[33:33:00]</a>.

For example, a model might predict which customer has the highest lifetime value (LTV) <a class="yt-timestamp" data-t="32:33:00">[32:33:00]</a>. However, the more important question for a marketing manager is: "How much *more* will they spend on my platform *because* I sent them this promotion?" <a class="yt-timestamp" data-t="33:05:00">[33:05:00]</a> This requires understanding differential impact, not just absolute value <a class="yt-timestamp" data-t="33:11:00">[33:11:00]</a>.

> "Prediction is inherently about correlation, but when we ask people to make decisions, we're asking them to think about causation." <a class="yt-timestamp" data-t="34:30:00">[34:30:00]</a>

## The Role of Experimentation

To move from prediction to causation, [[role_of_data_and_experimentation_in_growth | experimentation (A/B testing)]] is vital <a class="yt-timestamp" data-t="39:33:00">[39:33:00]</a>. When evaluating a new ranking algorithm, for instance, the question should be whether it leads to more bookings or better matches, not just if it better recreates past user choices <a class="yt-timestamp" data-t="36:46:00">[36:46:00]</a>.

### Challenges in Experimentation

*   **Micro-optimization vs. Big Opportunities:** A common concern is that excessive reliance on experiments can lead to incremental improvements and "local maxima," missing out on larger, transformative opportunities <a class="yt-timestamp" data-t="39:53:00">[39:53:00]</a>.
*   **Organizational Incentives:** Companies often incentivize data scientists based on "wins" (successful experiments), which can push teams towards safer, more incremental tests that are run longer to ensure statistical significance <a class="yt-timestamp" data-t="42:24:00">[42:24:00]</a>.
*   **"Learning is Costly":** It's often counter-intuitive to pay to learn, as evidenced by holding out groups from new features or promotions. However, this cost is necessary to understand the true impact of changes <a class="yt-timestamp" data-t="59:52:00">[59:52:00]</a>. If experiments are viewed only as "wins" or "losses," the valuable lessons from "failed" experiments are often discarded <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>.

### Shifting the Culture

To address these challenges, a cultural shift is needed:

*   **From "Wins" to "Learning":** Experiments should be viewed as opportunities for learning about the business, not just about achieving a positive metric outcome <a class="yt-timestamp" data-t="43:49:00">[43:49:00]</a>. Even a "failed" experiment can provide crucial insights into how the marketplace operates <a class="yt-timestamp" data-t="44:03:00">[44:04:00]</a>.
*   **Embrace Hypothesis-Driven Testing:** Experiment documentation should articulate the hypotheses being tested, focusing on what will be learned about business flows, funnels, or user preferences <a class="yt-timestamp" data-t="55:02:00">[55:02:00]</a>.
*   **Quantified, Not Just Data-Driven:** Acknowledge that not everything can be perfectly measured. Combine experiment results with existing beliefs and understanding of the business to make decisions, especially for long-term impacts that are hard to capture in short-term tests <a class="yt-timestamp" data-t="48:51:00">[48:51:00]</a>.
*   **Bayesian A/B Testing:** Incorporate past knowledge and previous experiment results into a "prior belief" that informs the analysis of new experiments <a class="yt-timestamp" data-t="56:25:00">[56:25:00]</a>. This rewards data scientists for contributing information that shapes future analyses, fostering a positive information externality across the business <a class="yt-timestamp" data-t="56:53:00">[56:53:00]</a>.

## Designing Effective Rating Systems

Rating systems are fundamental to the "learning about matches" phase of a marketplace's lifecycle <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>. However, they present unique challenges:

*   **Rating Inflation:** Over time, median ratings tend to inflate due to factors like reciprocity and norming (e.g., a four-star rating feeling like a "ding" when five stars is the norm) <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>.
*   **Renorming:** Instead of generic star ratings, consider systems that ask users to compare an experience to expectations (e.g., "exceeded expectations") or to past experiences they rated highly. This makes it easier for users to provide more nuanced feedback without feeling like they are penalizing someone <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>.
*   **Averaging Pitfalls:** Simply averaging ratings can have significant distributional consequences. New sellers with a few early negative reviews can be severely disadvantaged, potentially leading to early exit from the platform <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a>.
*   **Prior Beliefs in Ratings:** Using a prior belief can help mitigate the impact of early negative reviews for new participants, pulling their average rating up slightly and giving them a fairer chance to succeed <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>.
*   **"Sound of Silence":** The absence of a review often carries valuable information (e.g., it's easier to not leave a review than to leave a negative one). Incorporating this passive data can lead to more predictive indicators of seller performance <a class="yt-timestamp" data-t="01:07:47">[01:07:47]</a>. Double-blind review systems can also encourage higher review rates by allowing users to see the other party's review only after submitting their own <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>.

## [[Impacts of AI on data science and marketplace operations | AI's Impact on Data Science]]

The rise of LLMs and generative AI is expanding the frontier of ideas and hypotheses available to data scientists astronomically <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. While AI can automate tasks like coding and visualization, it places *more* pressure on humans, not less <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>. Humans become even more critical in funneling down the explosion of possibilities to identify what truly matters for the business <a class="yt-timestamp" data-t="01:10:18">[01:10:18]</a>. This means data literacy is increasingly vital for anyone interacting with these tools and each other <a class="yt-timestamp" data-t="01:22:38">[01:22:38]</a>.