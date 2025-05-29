---
title: Experiments and DecisionMaking in Marketplaces
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Marketplaces are dynamic, often compared to a game of "whac-a-mole," where addressing an issue on one side can create challenges on the other [00:00:00]. Many changes introduced in marketplaces, especially those that are highly consequential, create both winners and losers [00:00:47]. The ability to adapt to these changes hinges on recognizing whether the created winners are more important to the business than the losers [00:00:50].

## The Role of Data in Marketplace Management

Ramesh Johari, a professor at Stanford University, researches and teaches [[role_of_data_science_in_online_marketplaces | data science]] methods and practices with a focus on online marketplaces [00:01:05]. He has advised major marketplaces like Airbnb, Uber, Stripe, Bumble, Stitch Fix, and Upwork [00:01:14].

From an economic perspective, marketplaces sell the "taking away of friction" or [[understanding_marketplaces_and_transaction_costs | transaction costs]] [00:06:35]. For example, Uber doesn't sell rides; it removes the friction of finding a driver [00:06:04]. Both sides of a marketplace—buyers and sellers, hosts and guests, drivers and riders—are customers of the platform, as they all depend on it to reduce friction [00:07:52].

Modern technology allows marketplaces to constantly re-architect their operations, making [[role_of_data_science_in_online_marketplaces | data science]] central to their success [00:09:07]. Data science addresses three core problems in marketplaces, forming a "flywheel" of continuous improvement:
1.  **Finding potential matches:** This involves helping users find what they're looking for, such as an Airbnb listing or a driver [00:09:31].
2.  **Making the match:** This focuses on assisting users in selecting the best option from available matches, like triaging job applicants on a freelancing platform [00:09:51].
3.  **Learning about matches:** This involves collecting feedback, both active (e.g., [[key_performance_indicators_for_marketplaces | ratings]] and reviews) and passive (e.g., early booking cancellations), to improve future matching and user experience [00:10:18].

## Redefining the Marketplace Founder

A common pitfall for entrepreneurs is thinking too much about being a "Marketplace founder" before they truly are one [00:12:34]. A true marketplace, in Ramesh Johari's view, requires "scaled liquidity" on both sides of the platform [00:23:08]. If a business lacks this, it's not yet a marketplace [00:23:36].

Instead, founders should focus on their core value proposition in a world where they don't yet have two-sided scale [00:15:24]. For example, UrbanSitter initially focused on solving the friction of credit card payments for babysitters before evolving into a full marketplace [00:13:48]. Odesk (now Upwork) initially provided tools to verify remote work, addressing a trust issue, before becoming a large freelancing platform [00:15:47].

> "A Marketplace business never starts as a Marketplace business because what we think of as a Marketplace business is something which at scale is removing the friction of the two sides finding each other" <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>

Ramesh Johari argues that "every founder is a Marketplace founder" [00:17:05]. The decision to build a platform or marketplace is often a choice made after initial growth, as seen with Open AI and its plugins [00:17:29]. Early commitments, particularly to pricing models, can limit future options and lead to [[common_mistakes_in_building_marketplaces | disintermediation]] if the platform's value proposition changes over time [00:18:21].

If a business only has one side scaled (e.g., many buyers but few sellers), the focus should be on leveraging that strength to attract the other side, igniting the [[marketplace_growth_strategies | flywheel of growth]] [00:24:13]. This might involve subsidizing one side, as Uber did with free ride coupons to attract riders in new cities [00:24:41]. If neither side is scaled, the priority should be on scaling one side first, leveraging general startup [[expansion_strategies_for_marketplaces | growth strategies]] rather than specific marketplace ones [00:25:00]. This might even mean opting for a "firm" model with employed labor rather than a market model, where it better addresses the specific friction, as seen in healthcare platforms or Stitch Fix [00:26:53].

## Leveraging Data Scientists for Better Decisions

The greatest leverage for data scientists in marketplaces lies in helping the business make better [[decision_making_in_product_management | decisions]] [00:29:54].

### Prediction vs. Causation
A common misconception is that predictive models (machine learning) directly lead to good decisions [00:32:14]. Predicting what *will* happen (e.g., who is most likely to be hired) is different from understanding the causal impact of an intervention (e.g., how much more revenue a customer will generate *because* of a promotion) [00:33:05]. Prediction is about correlation; decision-making requires understanding causation [00:34:23].

> "The first and most important thing that I feel very strongly about and what would I get a data scientist to do is no matter who they are... get them to be thinking in the back of their mind always that their goal is to help the business make decisions and that the distinction between causation and correlation matters a lot" <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>

In areas like search, recommendation, and matching algorithms, data scientists should evaluate different algorithms not just by how well they predict past user choices, but by their ability to lead to more or better matches in the future, measured by core business metrics like bookings and revenue [00:36:42].

### The Role of Experimentation
Experimentation, particularly A/B testing, is crucial for establishing causal relationships [00:40:37]. However, there are common [[common_mistakes_in_building_marketplaces | challenges]]:
*   **Micro-optimization:** A focus on quick wins can lead to incremental changes and miss larger opportunities [00:39:53].
*   **Risk Aversion:** Companies often test incremental changes and run experiments for too long due to incentives that reward "wins" [00:41:52].
*   **"Winners and Losers" Mindset:** Framing experiments in terms of wins and losses discourages exploring risky but potentially insightful hypotheses [00:43:31]. A better approach is to prioritize "learning" as a win, even if an experiment "fails" to produce a positive immediate metric [00:45:05].

> "Many of the changes that are most consequential create winners and losers and rolling with those changes is about recognizing whether the winners you've created are more important to your business view than the losers you've created in the process" <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>

For example, implementing a "superhost" badge might reallocate attention to badged hosts at the expense of unbadged ones, potentially leading to flat or even decreased overall bookings in the short run [00:50:08]. The true value might be in long-term host retention, which is harder to measure in short experiments [00:48:26].

### Learning is Not Free
Running experiments incurs a cost, as resources are allocated to different options (treatment and control groups) [00:59:58]. A holdout group in a marketing campaign, for instance, might reveal the value of the team's efforts but at a direct cost of lost revenue [00:58:52]. This cost of learning is often overlooked due to the "winners and losers" mentality, which implies that time spent on "failing" experiments is wasted [01:00:30].

### Designing Effective Rating Systems
Rating systems are fundamental to marketplaces, but they face challenges like "rating inflation" due to reciprocity and norming effects [01:02:50]. To counter this, marketplaces can:
*   **Renorming:** Change rating labels (e.g., "exceeded expectations" instead of just "excellent") or ask users to compare an experience to past highly-rated ones [01:03:51]. This makes it easier for users to provide more honest feedback [01:04:20].
*   **Address Averaging Issues:** Simple averaging of [[key_performance_indicators_for_marketplaces | ratings]] can disproportionately harm new participants, as a single negative early review can severely impact their prospects [01:05:05]. This creates "distributional fairness" challenges [01:05:50].
*   **Use Prior Beliefs:** Implement Bayesian A/B testing, which incorporates past data or prior beliefs into the analysis of new experiments [00:56:06]. This can help mitigate the impact of early negative reviews on new sellers, providing a "prior belief" that pulls up their average rating [01:06:01].

Additionally, there's significant information in "the sound of silence"—the lack of a review [01:07:47]. Platforms can leverage this, for example, by incentivizing reviews (like Airbnb's double-blind review system that increased review rates) to gather more data [01:07:20].

## The Impact of AI on Data Science

AI, particularly large language models (LLMs) and generative AI, is expanding the frontier of hypotheses and ideas that data scientists can explore [01:09:50]. While AI can automate basic tasks like coding and visualization, it ultimately places *more* pressure on humans to be in the loop [01:10:08]. Humans become even more critical in funneling down the astronomical explosion of ideas generated by AI and identifying what truly matters [01:10:18]. This requires increased "data literacy" among all individuals interacting with these tools [01:22:38].

---
### Additional Resources
*   "How to Lie with Statistics" by Darrell Huff <a class="yt-timestamp" data-t="01:11:42">[01:11:42]</a>
*   Works by David Freedman (statistician) <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>
*   "4,000 Weeks" by Oliver Burkman <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>
*   Movie: "The Alpinist" <a class="yt-timestamp" data-t="01:13:58">[01:13:58]</a>
*   TV Show: "Only Murders in the Building" <a class="yt-timestamp" data-t="01:14:26">[01:14:26]</a>
*   Research on "effective percent positive" in ratings by Steve Tadelis et al. <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>