---
title: Design and operation of online marketplaces
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Ramesh Johari, a professor at Stanford University, conducts research and teaches [[role_of_data_science_in_successful_marketplaces | data science]] methods and practices with a focus on the design and operation of online marketplaces. He has advised companies such as Airbnb, Uber, Stripe, Bumble, Stitch Fix, and Upwork [01:03:00].

## What is a Marketplace Business?

A marketplace business does not sell rooms or rides directly; rather, it sells the removal of friction in finding these services [06:11:11]. This friction, known in economics as transaction costs, prevents markets from working efficiently [06:44:45]. For instance, Uber removes the friction of finding a driver, and Airbnb removes the friction of finding a place to stay [06:37:05].

Both sides of a marketplace are considered customers of the platform [07:52:43]. Drivers on Uber, for example, are customers because they rely on the platform to earn money by taking people places, just as riders rely on Uber to find transportation [07:59:03]. The core value proposition of a marketplace is fundamentally about taking away these transaction costs [08:11:00].

## The Role of Data Science in Marketplaces

[[role_of_data_science_in_successful_marketplaces | Data science]] is central to building successful marketplaces [01:33:43]. Unlike ancient markets built of stone, modern technology allows marketplaces to be constantly architected and rearchitected through the use of data [09:01:21]. This constant change and reallocation of attention and inventory is what makes marketplace management akin to a game of "whack-a-mole" [00:00:00].

The fundamental problems that [[role_of_data_science_in_successful_marketplaces | data science]] helps solve in marketplaces include [09:25:29]:
1.  **Finding Matches** <a class="yt-timestamp" data-t="09:31:01">[09:31:01]</a>: Connecting buyers and sellers (e.g., finding hosts for travelers or travelers for listings) <a class="yt-timestamp" data-t="09:39:10">[09:39:10]</a>.
2.  **Making Matches** <a class="yt-timestamp" data-t="09:50:48">[09:50:48]</a>: Helping users choose the best option from multiple possibilities (e.g., triaging applicants for a job) <a class="yt-timestamp" data-t="10:14:09">[10:14:09]</a>.
3.  **Learning about Matches** <a class="yt-timestamp" data-t="10:16:11">[10:16:11]</a>: Collecting feedback (e.g., ratings, reviews, passive data) to improve future matching and search capabilities [10:28:13].

These three areas form a data science flywheel, where learning from past matches informs future finding and making of matches [11:00:30].

## [[challenges_in_starting_and_scaling_marketplace_businesses | Challenges in Starting and Scaling Marketplace Businesses]]

A common flaw for founders is thinking too much about being a marketplace before they actually are one [12:32:05]. A true marketplace requires "scaled liquidity" on both the buyer and seller sides of the platform [23:08:24]. If a platform only has one side scaled, it's not yet a marketplace; it's a business that has successfully attracted one side [23:33:04].

Initial value propositions should focus on solving specific frictions for one side, not on being a full-fledged marketplace [15:15:39].

### Examples of Early-Stage Strategies:

*   **Urban Sitter (Babysitting Marketplace)**: Initially focused on addressing the friction of cash payments for babysitters by accepting credit card payments [13:47:49]. Once liquidity was established, they leveraged Facebook networks for trusted introductions and shifted monetization to finding potential babysitters rather than just payment processing [13:57:04].
*   **oDesk (Upwork)**: Began by providing tools for remote workers to verify their hours and tasks, which built trust and enabled guarantees for both workers and employers [15:49:57]. This addressed a trust issue in remote work before scaling as a full marketplace [16:17:19].

The advice is that a marketplace business never starts as a marketplace business [15:06:04]. Founders should focus on their value proposition in a world without scaled liquidity on both sides [15:27:03]. Many of the problems faced by marketplace startups are the same as any other startup, such as growth [16:46:17]. The decision to become a platform is often a choice made after initial growth [17:29:05].

### The "Every Founder is a Marketplace Founder" Concept

Every entrepreneur's business endeavor today could potentially be disrupted by online transactions [17:10:04]. Therefore, virtually any founder is a "marketplace founder" in a sense, as building a platform can become a choice they make after they grow [17:25:27]. For example, Open AI, which started as an AI research company, is now functioning as a marketplace due to its plugin ecosystem [17:36:00].

Founders must be careful not to "overcommit their future" with early choices [18:20:00]. Monetization models chosen early on, like a constant fraction of transactions, can lead to disintermediation later when relationships mature and the platform's value add diminishes [18:41:00]. For instance, if a long-term relationship between a worker and employer on a platform like oDesk no longer requires active intermediation, but the platform still charges a percentage, it creates an incentive for them to take the relationship off-platform [19:01:00]. This is what Ramesh calls "disintermediation" [19:29:32].

> "You have to recognize when you run marketplaces that many of the changes that are most consequential create winners and losers and rolling with those changes is about recognizing whether the winners you've created are more important to your business than the losers you've created in the process." <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>

### [[unit_economics_in_marketplaces | Unit Economics in Marketplaces]]

Founders should consider the [[unit_economics_in_marketplaces | unit economics]] of their business model [25:52:03]. The best resolution for frictions might not be a marketplace, but rather a tightly controlled labor force, as seen in companies like Stitch Fix with their stylists, or healthcare platforms [26:56:04]. This distinction between a "market" and a "firm" is a long-standing concept in economics [26:27:04].

## Leveraging Data Science for Marketplace Efficiency

For data scientists in marketplaces, the biggest leverage comes from helping the business make *decisions* based on causation, rather than merely making *predictions* based on correlation [33:31:00].

*   **Prediction vs. Causation**: Machine learning models are great at predicting outcomes by finding patterns and correlations in past data [30:05:06]. However, effective decision-making requires understanding causation – how a specific action will *change* an outcome [33:17:22]. For example, a marketing manager should not just send promotions to the highest lifetime value (LTV) customers based on prediction, but rather to customers where the promotion will *increase* their LTV, which is a differential effect [32:51:39].

This emphasis shifts the focus from simply predicting who will be hired to understanding which ranking algorithm will lead to more or better matches in the future [37:52:43].

## Experimentation and Learning

### The Role of Experiments

[[role_of_data_science_in_successful_marketplaces | Data science]] is crucial for experimentation, particularly in [[marketplace_growth_strategy | marketplace growth strategy]] [39:10:03]. Experiments are essential to determine the causal impact of changes [39:33:43].

### Avoiding Micro-Optimization

There's a challenge with experimentation: focusing too much on individual experiments can lead to micro-optimization or "local minima/maxima," potentially missing larger opportunities [39:48:46].

Ramesh believes companies often make two mistakes in experimentation [41:15:00]:
1.  **Testing Incremental Changes**: What people decide to test tends to be incremental by design [42:01:03].
2.  **Running Experiments for Too Long**: Experiments are often run longer than necessary [42:09:27].

These issues are often tied to organizational incentives [42:24:00]. If data scientists are judged by "wins" per quarter, they are incentivized to pursue incremental changes that are easier to show positive results for, and to run experiments longer to ensure those wins are statistically significant [42:30:00].

### Shifting to a Learning Culture

> "Experimentation is always very hypothesis driven. It's about what are you learning, and that's really an important distinction because what it means is if I go with something big, risky and it quote unquote fails meaning that doesn't win, I nevertheless if I was being rigorous about what hypothesis that's testing about my business I'm potentially learning a lot." <a class="yt-timestamp" data-t="00:43:49">[00:43:49]</a>

A cultural shift is needed to prioritize learning over merely accumulating "wins" [45:05:05]. Leaders should expect data scientists to articulate what they are learning about the business, its flows, funnels, and user preferences, not just deliver narrowly defined statistically rigorous results [54:28:09]. This means defining experiments with clear hypotheses about business flows, rather than just win/loss metrics [55:02:00].

One technical approach to support this culture is **Bayesian AB testing** [56:42:00]. Traditional (frequentist) statistical methods used in AB testing typically ignore past learnings. Bayesian methods allow incorporating "prior beliefs" based on past experiments, meaning even a "failed" experiment can be valuable by updating that prior belief, generating an "information positive externality" for future analyses [56:59:00].

### The Cost of Learning

Learning is not free; it comes at a cost [57:51:00]. For example, a marketing manager deliberately holding out a segment of users from new innovations to measure the impact of their team's efforts incurs a direct financial cost (e.g., millions of dollars in lost revenue) [58:31:00]. However, this "cost" generates invaluable knowledge about the effectiveness of their strategies [59:03:00].

The "Sound of Silence" in ratings is another example of valuable information often missed – the lack of a response can be as informative as a negative one [01:07:47].

## Designing Rating Systems

Designing effective rating systems for marketplaces is challenging, and no one has "nailed it" yet [01:02:31]. Key considerations include:

*   **Rating Inflation**: Over time, median ratings tend to inflate due to factors like reciprocity (users wanting to be nice) and norming (where a 4-star rating might be perceived as negative when the average is 4.8) [01:02:54].
*   **Renorming**: To combat inflation, platforms can renorm the meaning of labels (e.g., "exceeded expectations" instead of just "excellent") or ask users to compare new experiences to highly rated past experiences [01:03:51]. This makes it easier for users to provide more nuanced feedback without feeling like they are "dinging" someone [01:04:23].
*   **Averaging and Distributional Fairness**: Simply averaging ratings can be problematic [01:04:41]. For established entities with many reviews, a new negative review has little impact [01:05:11]. However, for new entrants, an early negative review can be devastating, significantly impacting their ability to get work and potentially leading to early exit from the platform [01:05:16].
*   **Using Priors for Fairness**: Bayesian concepts can be applied here. By averaging a new entrant's rating with a "prior belief" about average quality, a platform can smooth out the impact of initial negative reviews, giving new participants a fairer chance to succeed [01:06:01].

Rating systems are "understudied" despite being one of the biggest changes from traditional markets, as they allow platforms to learn from matches and understand who wins and loses in the market [01:06:38].

## [[impact_of_ai_on_data_science_and_marketplaces | Impact of AI on Data Science and Marketplaces]]

While AI and Large Language Models (LLMs) can automate parts of [[role_of_data_science_in_successful_marketplaces | data science]] (e.g., coding, visualizations, dashboards), their primary impact is on expanding the frontier of ideas and hypotheses that can be explored [01:09:09].

This explosion of possibilities puts *more* pressure on humans, not less [01:10:05]. Humans become even more critical in funneling down explanations, ideas, and experiment designs to identify what truly matters [01:10:13]. The need for data literacy among those interacting with these tools and each other becomes paramount [01:22:36].