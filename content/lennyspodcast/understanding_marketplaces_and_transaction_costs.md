---
title: Understanding Marketplaces and Transaction Costs
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Marketplaces can be likened to a game of "whack-a-mole" where managing them often involves moving attention and inventory around. Changes made within a marketplace environment frequently create both winners and losers [00:00:00]. The challenge lies in recognizing whether the created winners are more beneficial to the business than the created losers [00:51:55].

Ramesh Johari, a professor at Stanford University, conducts research and teaches [[role_of_data_science_in_online_marketplaces | data science]] methods with a specific focus on the design and operation of online marketplaces [01:01:00]. He has advised and worked with major platforms such as Airbnb, Uber, Stripe, Bumble, Stitch Fix, and Upwork [01:13:00].

## What is a Marketplace Business?

Many believe that companies like Airbnb sell rooms or Uber sells rides, but this isn't entirely accurate from the platform's perspective [00:05:54]. The hosts on Airbnb sell listings, and drivers on Uber sell rides [00:06:21]. What Uber and Airbnb actually sell is the removal of friction—specifically, the friction of finding a place to stay or a driver [00:06:32].

In economics, this friction is referred to as "transaction costs" [00:06:44]. Markets don't always function perfectly due to "market failures" caused by these transaction costs [00:06:55]. For example, finding a driver or a temporary place to stay presents frictions that marketplaces aim to eliminate [00:07:09].

Both sides of the marketplace, such as buyers (e.g., ride-seekers, room-bookers) and sellers/providers (e.g., drivers, hosts), are considered customers of the platform. Each side relies on the platform to help remove the friction in their respective objectives, whether it's finding a service or earning money [00:07:41]. The fundamental value proposition of a marketplace is the elimination of these transaction costs [00:08:11].

## The Role of Data and Technology

Unlike ancient physical markets that were fixed in stone, modern online marketplaces, supported by technology, can be constantly architected and re-architected [00:09:01]. This flexibility allows for continuous optimization and improvement of the marketplace's operations [00:09:09].

The [[role_of_data_science_in_online_marketplaces | data science]] of marketplaces primarily addresses three core problems:
1.  **Finding potential matches:** This involves helping users discover available options, such as a traveler finding a room or a host finding a guest [00:09:32].
2.  **Making the match:** This focuses on facilitating the actual transaction or connection, like an employer selecting the right applicant from multiple candidates [00:09:51].
3.  **Learning about matches:** After a match is made, the marketplace gathers data and feedback (e.g., ratings, reviews, passive data like early departures) to learn from the experience [00:10:18]. This learning then feeds back into the process of finding and making better matches in the future, creating a continuous improvement loop [00:10:48].

Every marketplace, regardless of its vertical, deals with these three challenges and relies on algorithms and [[role_of_data_science_in_online_marketplaces | data science]] to help solve them, thereby removing transaction costs [01:11:00].

## Common Pitfalls for Marketplace Founders

A significant [[common_mistakes_in_building_marketplaces | common mistake]] for entrepreneurs is to think too much about being a "marketplace" before actually becoming one [00:12:34]. A marketplace business rarely starts as a fully scaled platform [00:15:09]. Instead, it begins by solving a specific friction point in a non-scaled environment [00:15:22].

For instance, UrbanSitter, a babysitting marketplace, initially addressed the friction of cash payments by enabling credit card transactions [00:13:07]. Once this was established, they leveraged Facebook networks to build trusted introductions, eventually evolving into a platform that helps users find and make babysitting matches [00:13:57]. Similarly, oDesk (now Upwork) started by providing tools to verify remote work, resolving a trust issue before achieving large-scale liquidity [00:15:33].

Founders should not necessarily identify as "marketplace founders" but rather as "founders." Any business, especially in the modern tech-enabled economy, may eventually have the option to evolve into a platform [00:17:08]. Early decisions, particularly regarding [[different_pricing_models_and_when_to_use_them | pricing schemes]] and monetization, can significantly limit future flexibility [00:18:38].

### Disintermediation

A key challenge for marketplaces is "disintermediation," where parties bypass the platform once trust or a relationship is established [00:19:29]. For example, a Thumbtack worker might give a business card to a satisfied customer, eliminating the need for the platform for future interactions [00:19:41]. This can lead to the platform losing revenue from long-term relationships where its value add diminishes over time [00:19:21]. Upwork, after its merger, had to rethink its monetization strategy to address this issue [00:20:03].

Substack offers a positive example of evolving beyond its initial platform. By investing in driving demand to writers, such as through its network, Substack increased its value proposition and created a strong marketplace element, preventing disintermediation [00:20:28]. Conversely, eBay faced significant [[challenges_and_considerations_in_b2b_marketplaces | challenges]] with its seller community when it introduced more granular fees, breaking what sellers perceived as a social contract [00:21:12].

## Identifying a True Marketplace

To determine if a business is truly a marketplace, a key test is whether it has "scaled liquidity" on both sides of its platform [00:23:02]. Scaled liquidity means having a large number of both buyers and sellers [00:23:11].

If a business only has one side scaled (e.g., many buyers but few sellers), it is not yet a marketplace. In this scenario, the focus should be on leveraging the scaled side to attract the other [00:24:09]. Uber, for example, subsidized drivers and then gave out free ride coupons to attract riders in new cities, using the subsidized supply to build demand [00:24:23]. If neither side is scaled, the priority should be on scaling one side first, adopting general startup [[marketplace_growth_strategies | growth strategies]] rather than specific marketplace strategies [00:25:03].

The decision to operate as a marketplace versus a firm (where labor is tightly controlled, like employees) depends on the specific frictions being solved [00:26:56]. For services requiring consistent relationships and curation, such as physical therapy or personal stylists (e.g., Stitch Fix), a firm model might be more appropriate than a pure marketplace [00:27:02].

## Maximizing Data Science Leverage

For a data person in a marketplace, the biggest opportunities for leverage vary depending on the platform's specific structure and needs [00:28:26]. For platforms like Uber or DoorDash, where the platform sets prices, a [[role_of_data_science_in_online_marketplaces | data scientist]] might focus on [[different_pricing_models_and_when_to_use_them | pricing strategies]] that dynamically respond to supply and demand [00:28:51]. In other marketplaces like Airbnb, where hosts set prices, the focus might shift to search and recommendation algorithms, as finding the right match is the primary friction [00:29:16].

A crucial philosophical point for [[role_of_data_science_in_online_marketplaces | data scientists]] is to understand that their goal is to help the business make decisions, not just predict outcomes [00:30:05]. While machine learning models excel at predicting patterns (correlation), effective decision-making requires understanding causation [00:34:11].

For example, predicting who is most likely to be hired (as in oDesk's early days) [00:30:47] or identifying customers with the highest lifetime value (LTV) is about correlation [00:33:00]. However, the real decision is about whether a specific intervention (e.g., sending a promotion) will *cause* a desired outcome (e.g., increased LTV) [00:33:35]. The core takeaway is that a data team's purpose is to help the business make better decisions, explicitly considering the causal impact of actions [00:35:08].

This focus on causation translates into evaluating different ranking algorithms for search/recommendation not just by how well they predict past user choices, but by their impact on core business metrics like bookings or revenue [00:37:10]. For example, comparing two ranking algorithms would involve asking if one leads to more or better matches than the other, using observable outcomes [00:37:40].

## Experimentation and Learning

[[experiments_and_decisionmaking_in_marketplaces | Experimentation]] (A/B testing) is critical for understanding the causal impact of changes [00:39:33]. However, there's a [[challenges_and_considerations_in_b2b_marketplaces | common challenge]] of micro-optimizing and missing larger opportunities if experiments are run too incrementally or for too long [00:39:53].

Companies often incentivize [[role_of_data_science_in_online_marketplaces | data scientists]] based on the number of "wins" (successful experiments), leading to a preference for incremental, low-risk changes that are easier to prove effective [00:42:30]. This also incentivizes running experiments for longer durations to ensure statistically significant results [00:42:48].

A more beneficial approach is to adopt a culture where [[experiments_and_decisionmaking_in_marketplaces | experimentation]] is seen as a means of learning, rather than just winning [00:43:50]. Even if an experiment "fails" (doesn't produce a "win"), if it tests a clear hypothesis about the business, it still provides valuable insights [00:44:07]. For instance, a badging system might reduce overall bookings by over-concentrating attention on badged profiles and diverting it from unbadged ones [00:44:32]. While seemingly a "failure," this teaches the company about how attention and inventory are reallocated [00:44:54].

Airbnb's "Superhost" badge, despite initial experiments showing no direct impact on bookings or revenue, was deemed a success because it improved host satisfaction and retention [00:46:06]. This highlights that some impacts, especially long-term ones like host retention, are hard to measure in short-term experiments [00:48:13]. In such cases, combining experimental data with existing beliefs and understanding of the business ("quantified" rather than purely "data-driven") is essential for decision-making [00:49:11].

This "whack-a-mole" effect in marketplaces means that redirecting attention to one group (e.g., Superhosts) can come at the expense of others, making overall "pie-expanding" wins less obvious in the short term [00:50:00]. Many consequential changes in marketplaces create winners and losers, and management involves deciding whether the benefits to winners outweigh the losses to others [00:51:48].

### The Cost of Learning

Learning, especially through [[experiments_and_decisionmaking_in_marketplaces | experimentation]], is not free; it comes at a cost [00:57:51]. Running holdout groups or A/B tests means intentionally diverting resources or foregoing potential benefits from the "winning" treatment in favor of gaining knowledge [00:58:18]. This cost is often apparent only in hindsight [00:59:39]. However, companies must recognize that paying to learn is a necessary investment to make informed decisions and understand their business better [01:00:10]. The cultural emphasis on "shipping winners" can paradoxically devalue the learning gained from "failed" experiments, reinforcing the idea that time spent on non-winning tests is wasted [01:00:37].

## Designing Effective Rating Systems

Designing effective rating systems in marketplaces is complex and not yet "nailed" by any platform [01:02:31]. A common problem is "rating inflation," where median ratings tend to increase over time due to factors like reciprocity (people don't want to be mean) and norming (a 4-star rating feels low when the average is higher) [01:02:52].

Strategies to mitigate rating inflation include:
*   **Re-norming labels:** Instead of just "poor to excellent," labels like "exceeded expectations" can encourage more nuanced feedback [01:03:51].
*   **Comparative questions:** Asking users to compare their experience to past highly-rated experiences can help elicit more accurate relative feedback [01:04:08].

Another critical consideration is the impact of averaging ratings, especially on new participants [01:04:41]. A default average rating system can be unfair to new sellers or providers; a single negative review can disproportionately harm a new entrant, potentially leading to their exit from the platform [01:05:00]. To address this "distributional fairness," systems can incorporate a "prior belief" about a new participant's quality, which averages their initial ratings with a baseline expectation. This can help buffer the impact of early negative reviews, giving new participants a fairer chance [01:06:01].

The "sound of silence" is an important concept in rating systems, referring to the valuable information contained in the absence of a rating [01:07:47]. Often, not leaving a review is easier than leaving a negative one, providing a subtle signal about dissatisfaction [01:08:23]. Incorporating this passive data, such as by normalizing by including unleft ratings, can provide a more predictive measure of a seller's performance [01:08:03].

## The Impact of AI on Data Science

Large Language Models (LLMs) and generative AI are not likely to automate away large parts of [[role_of_data_science_in_online_marketplaces | data science]] in industry [01:09:12]. While AI tools can make coding, visualization, and dashboard creation faster [01:09:24], their primary impact is a massive expansion of the "frontier of things we could think about" [01:09:50]. This leads to an "astronomical explosion of explanations and ideas" [01:10:00].

This proliferation of ideas puts *more* pressure on humans, not less [01:10:08]. Humans become even more crucial in filtering, funneling, and identifying what truly matters from the vast array of possibilities generated by AI [01:10:13]. This applies to identifying relevant hypotheses in data analysis, choosing which creative variations to test in marketing campaigns, and evaluating the significance of findings [01:10:25]. Therefore, the human element remains central to the productive data science loop [01:11:11].