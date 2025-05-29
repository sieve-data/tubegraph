---
title: Design and operation of online marketplaces
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Marketplaces often operate like a "game of whack-a-mole," where addressing an issue on one side can create a new problem on the other [00:00:00]. This dynamic highlights that a significant aspect of [[marketplace_management_and_friction_reduction | marketplace management]] involves redirecting attention and inventory [00:00:43]. Many impactful changes within a marketplace create both winners and losers, and successful management means recognizing if the created winners are more valuable to the business than the losers [00:51:50].

Ramesh Johari, a professor at Stanford University, researches and teaches data science methods with a focus on online marketplace design and operation [01:04:00]. He has advised major marketplaces such as Airbnb, Uber, Stripe, Bumble, Stitch Fix, and Upwork [01:16:00].

## The Core Value Proposition of Marketplaces

Contrary to common perception, online marketplaces like Airbnb or Uber do not primarily sell rooms or rides directly [00:06:00]. Instead, the hosts on Airbnb sell listings, and drivers on Uber sell rides [00:06:21]. What the platforms themselves sell is the elimination of friction, which economists refer to as "transaction costs" [00:06:35]. This friction includes challenges like finding a place to stay or securing a driver [00:07:12].

A critical distinction is that both sides of the marketplace – both buyers and sellers – are customers of the platform [00:07:41]. Both depend on the platform to remove friction from their interactions [00:07:56]. The idea that marketplaces generate revenue by reducing transaction costs is a fundamental, yet often misunderstood, concept for entrepreneurs [00:08:11].

## The Role of Data and Algorithms

Online marketplaces are fundamentally different from ancient markets like the Roman Forum because modern technology allows for constant architectural and re-architectural changes, driven by data and algorithms [00:09:05]. This forms the basis of the [[role_of_data_and_algorithms_in_building_successful_marketplaces | role of data and algorithms in building successful marketplaces]].

According to Johari, the [[role_of_data_and_algorithms_in_building_successful_marketplaces | data science of marketplaces]] revolves around three core problems [00:11:02]:
1.  **Finding Matches:** Identifying potential partners (e.g., a traveler finding available listings, or a host finding potential guests) [00:09:29].
2.  **Making Matches:** Assisting users in selecting the best option from available matches (e.g., an employer choosing from job applicants) [00:09:51].
3.  **Learning About Matches:** Collecting feedback and data from completed transactions to improve future matching [00:10:18]. This includes active feedback (like star ratings) and passive data collection (like early departures) [00:10:43]. This feedback loop continuously enhances the processes of finding and making future matches [00:10:48].

## Founding a Marketplace Business

A common pitfall for new founders is thinking too much about being a marketplace *before* they actually achieve marketplace scale [00:12:39]. A marketplace business rarely starts as one in the traditional sense, as it initially lacks the "scaled liquidity" – a significant number of both buyers and sellers [00:15:09].

The advice is to first focus on a specific, non-marketplace problem or friction point [00:16:22].
*   **UrbanSitter Example:** Initially, UrbanSitter addressed the friction of babysitters needing cash by enabling credit card payments. Only after gaining liquidity from this initial value proposition did they pivot to solving the broader friction of finding and connecting with sitters [00:13:07].
*   **Odesk Example:** Odesk (now Upwork) began by solving trust issues in remote work by providing tools to verify work hours and activities, thereby enabling guarantees for both workers and employers [00:15:35].

Johari suggests that "every founder is a Marketplace founder" [00:17:08]. Any business endeavor in the modern, tech-enabled economy has the potential to evolve into a platform where transactions occur online. This evolution is a choice made after initial growth, as seen with companies like Open AI (with plugins) or Substack (investing in driving demand for writers) [00:17:31].

Early commitments, such as specific pricing schemes, can hinder a marketplace's future. For example, Upwork (formerly Odesk) faced disintermediation (parties taking their relationship off-platform) because their constant percentage fee became less justifiable as long-term trust developed between workers and employers [00:18:21].

### Assessing Marketplace Readiness

To determine if a business is truly a marketplace, Johari proposes a "smell test" of "scaled liquidity" [00:23:08]. This means having a large number of buyers and sellers [00:23:27].
*   If neither side is scaled, the focus should be on scaling one side first, not on being a marketplace [00:25:03].
*   If one side is scaled, the business then faces the choice of leveraging that scaled side to attract the other [00:24:09]. Uber, for example, subsidized drivers with free rides to attract riders in new cities, fostering a flywheel of growth [00:24:23].

The decision between operating as a marketplace or a "firm" (where labor is tightly controlled, like employees) depends on the specific friction being addressed [00:26:27]. For services requiring high trust or curation, like healthcare or personalized styling (e.g., Stitch Fix), a firm model might be more effective [00:27:02].

## Experimentation and Data in Marketplaces

The biggest leverage for a data person in a marketplace is to help the business make decisions that focus on *causation*, rather than merely *prediction* [00:33:31]. While machine learning models are good at predicting outcomes by identifying correlations in past data, effective [[experimentation_and_decisionmaking_in_marketplaces | decision-making]] requires understanding *why* an action will lead to a particular outcome [00:34:11].

*   **Example:** A marketing manager might predict which customers have the highest lifetime value (LTV) and send them promotions. However, the true question for [[experimentation_and_decisionmaking_in_marketplaces | decision-making]] is how much *more* a customer will spend *because* they received a promotion – a differential, causal question, not an absolute predictive one [00:33:05].

In marketplace settings, data scientists should focus on:
*   **Search and Recommendation:** Evaluating ranking algorithms not just by how well they recreate past choices, but by whether they lead to more or better matches and ultimately increase core metrics like bookings and revenue [00:36:04].
*   **Hiring:** Assessing algorithms by the quality of future matches made, based on ratings and re-hires, rather than just predicting who *would have been* hired [00:37:31].

### The Culture of Experimentation

While [[experimentation_and_decisionmaking_in_marketplaces | experimentation is crucial for driving growth]], relying too heavily on immediate "wins" can lead to micro-optimization and miss larger opportunities [00:39:53]. Johari suggests that companies often become risk-averse, testing only incremental changes and running experiments for too long [00:41:52]. This is often due to incentives where data scientists are judged by the number of "wins" [00:42:30].

A healthier [[experimentation_and_decisionmaking_in_marketplaces | experimentation culture]] emphasizes learning over just winning [00:45:05]. Even a "failed" experiment can provide valuable insights into business dynamics (e.g., how a badging feature reallocates attention, as seen with Airbnb's Superhost program [00:46:06]). This perspective requires changing the language from "winners and losers" to "what was learned" [00:43:50].

Moreover, "learning isn't free" [00:57:51]. Running experiments, especially holdout groups, incurs a cost, but this cost provides valuable insights into the true impact of changes [00:58:19].

## Rating Systems

Designing effective rating systems is an ongoing challenge, with no single perfect model [01:02:31].
*   **Rating Inflation:** A common problem where median ratings inflate over time due to factors like reciprocity and norming (where a 4-star rating might feel "mean" compared to the high average) [01:02:50].
*   **Renorming:** Addressing inflation can involve renorming labels (e.g., "exceeded expectations" for top rating) or asking users to compare experiences to past highly-rated ones [01:03:51].
*   **Averaging Pitfalls:** Simply averaging ratings can disproportionately affect new users. A single negative review can severely impact a new profile with few ratings, making it difficult to gain traction [01:04:41].
*   **Prior Beliefs:** Using "prior beliefs" in a Bayesian approach can help. This involves incorporating broader marketplace knowledge or a default "average" rating for new entrants, pulling their initial rating up slightly to give them a fairer chance [01:05:58].
*   **"Sound of Silence":** There's significant information in ratings that *aren't* left. For instance, a lack of review might indicate a negative experience (as it's easier to leave no review than a bad one), and platforms can leverage this passive data [01:07:47].

## AI's Impact on Data Science

AI, especially large language models (LLMs) and generative AI, is massively expanding the frontier of possible hypotheses and ideas for data analysis and experimentation [01:09:50]. This explosion of possibilities means that humans become *more* important, not less, in the data science loop [01:10:08]. The human role shifts to funneling down the myriad of AI-generated explanations and ideas, prioritizing what truly matters for the business [01:10:18].