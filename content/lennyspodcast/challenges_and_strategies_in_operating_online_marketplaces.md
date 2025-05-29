---
title: Challenges and strategies in operating online marketplaces
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Operating online marketplaces often feels like a "game of whack-a-mole" where addressing one issue can lead to unintended consequences elsewhere in the system <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This dynamic arises because marketplace management fundamentally involves moving attention and inventory around, and many significant changes create both winners and losers <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Recognizing whether the created winners are more important to the business than the losers is key to navigating these changes <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Ramesh Johari, a professor at Stanford University, specializes in the design and operation of online marketplaces, offering insights based on his work with companies like Airbnb, Uber, Stripe, and Upwork <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## What a Marketplace Business Truly Sells

Contrary to popular belief, a marketplace like Airbnb doesn't sell rooms, and Uber doesn't sell rides <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Instead, they sell the *removal of friction* – known in economics as transaction costs <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Their core value proposition is to eliminate the difficulty of finding a place to stay or a driver <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. This means both sides of the marketplace (e.g., hosts and guests on Airbnb, drivers and riders on Uber) are the platform's customers, as both depend on the platform to remove these frictions <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

## The Pivotal Role of Data Science

The ability to architect and re-architect a marketplace, unlike ancient markets made of stone, means platforms can be constantly redesigned <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Data science is central to this flexibility <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### The Marketplace Data Science Flywheel
Effective marketplace operation revolves around three core problems, forming a continuous flywheel <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>:

1.  **Finding Matches**: Helping users find suitable partners on the other side of the market (e.g., guests finding listings, hosts finding guests) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
2.  **Making Matches**: Assisting users in choosing from multiple potential partners (e.g., employers triaging job applicants) <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
3.  **Learning About Matches**: Collecting feedback and data from completed transactions to improve future matching processes <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This includes active data collection like ratings and passive data like booking completion rates <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

Every step in this flywheel relies on algorithms and data science to remove transaction frictions <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

### Beyond Prediction: Focusing on Causation and Decisions
A key challenge for data scientists in marketplaces is shifting focus from merely *predicting* outcomes to *making better decisions* that drive value <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. For example, predicting a customer's lifetime value (LTV) is different from understanding how a promotion will *increase* their LTV <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>. Prediction relies on correlation, while effective decision-making requires understanding causation <a class="yt-timestamp" data-t="00:34:11">[00:34:11]</a>. Data scientists should always aim to help the business make decisions by understanding the causal impact of different actions <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>. This means evaluating algorithms not by how well they predict past choices, but by their ability to generate more or better matches in the future, measured by core business metrics like bookings and revenue <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.

## Common Pitfalls for Marketplace Founders

Many founders attempt to create marketplaces where they are not yet viable, leading to recurring failures <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

### Don't Start as a Marketplace
The biggest failure mode is thinking too much about being a marketplace before actually having a marketplace <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. A true marketplace has "scaled liquidity" on both sides – a lot of buyers and a lot of sellers <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. If only one side is scaled, the focus should be on leveraging that strength to attract the other side, not on acting as a full marketplace yet <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>. If neither side has scale, the focus should be on building one side first, and the business should operate as a standard startup, solving a specific pain point that doesn't necessarily require two-sided liquidity <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

For example, Urban Sitter, a babysitting marketplace, initially addressed the friction of cash payments by allowing credit card payments <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. Only after gaining liquidity and trust through Facebook networks did they shift to monetization based on finding potential sitters <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. Similarly, oDesk (now Upwork) began by providing tools to verify remote work, resolving a trust issue, before focusing on broader liquidity <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

### The Risk of Early Commitments (Monetization, Disintermediation)
Early decisions can inadvertently tie a marketplace's hands later on <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. For instance, oDesk's initial model of taking a constant fraction of transaction dollars led to disintermediation over time, as long-term relationships between workers and employers no longer required the platform's initial value proposition <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This highlights the importance of evolving monetization strategies to prevent users from bypassing the platform once trust and relationships are established offline <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

Conversely, Substack's strategy of investing heavily in driving demand to writers demonstrates a positive [[Expansion strategies for marketplaces|expansion strategy]], strengthening their social contract and value proposition <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.

### Every Founder is a Marketplace Founder
The rise of online transactions means virtually any business can eventually become a marketplace <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. Founders should recognize this potential and avoid over-committing their future by adopting rigid business models too early <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. The choice to become a platform is often made as a business scales, not at its inception <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

## [[Challenges and Strategies in EarlyStage Startup Growth|Experimentation]] and Learning in Marketplaces

Experimentation is crucial for making informed decisions, but challenges exist in its application.

### Avoiding Micro-Optimization
While being "experiment-driven" is valuable, solely focusing on experiments can lead to micro-optimization and missed larger opportunities <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>. Businesses often become risk-averse, testing only incremental changes and running experiments for too long <a class="yt-timestamp" data-t="00:41:52">[00:41:52]</a>. This is often driven by incentives that reward "wins" in experiments, making data scientists less willing to pursue riskier, potentially transformative ideas that might "fail" in the short term <a class="yt-timestamp" data-t="00:42:41">[00:42:41]</a>.

Instead, experimentation should be hypothesis-driven, focusing on *learning* rather than just "wins" or "losses" <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>. A "failed" experiment can still provide valuable insights into business dynamics, such as how attention and inventory are reallocated (e.g., the impact of "badges" like Superhost on non-badged listings) <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>. Fostering a culture where learning is valued as a win, even if the direct metric doesn't improve, is crucial <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>.

### The Cost of Learning
Learning through experimentation is not free; it comes at a cost <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>. For example, a marketing manager who uses a "holdout group" to measure the effectiveness of ad spend implicitly pays for the learning by not exposing that group to optimizations <a class="yt-timestamp" data-t="00:58:39">[00:58:39]</a>. This "cost to learn" is often culturally difficult to accept, as "wasted" samples on non-winning treatments can be perceived as failures rather than valuable data points <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. Businesses need to acknowledge and account for this cost, understanding that making informed decisions requires an investment in knowledge acquisition <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.

## [[Designing and evaluating review systems in marketplaces|Designing Effective Review Systems]]

Review and rating systems are vital for marketplaces but present complex challenges.

### Addressing Rating Inflation
A common issue is "rating inflation," where the median rating on marketplaces tends to increase over time <a class="yt-timestamp" data-t="01:02:52">[01:02:52]</a>. This can be due to reciprocity (users leaving positive reviews to receive them) or norming (what was once a good rating becomes perceived as average or poor) <a class="yt-timestamp" data-t="01:03:20">[01:03:20]</a>. Renorming the meaning of labels, such as asking if an experience "exceeded expectations" rather than just giving stars, can help elicit more honest feedback <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.

### Averaging and Distributional Fairness
Averaging ratings, while seemingly intuitive, can have significant "distributional consequences," especially for new participants <a class="yt-timestamp" data-t="01:04:41">[01:04:41]</a>. An established seller with thousands of reviews is largely unaffected by a single new review, but a new seller receiving one negative review can be "completely screwed," potentially leading to their early exit from the platform <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. To address this, platforms can use a "prior belief" system, where a new seller's rating is averaged with a general marketplace belief, pulling up a single negative rating that might have been due to unluckiness <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>.

Furthermore, there is valuable information in "the sound of silence"—ratings that are *not* left <a class="yt-timestamp" data-t="01:07:47">[01:07:47]</a>. Incorporating these non-responses into metrics can provide a more predictive understanding of seller performance <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>.

## The Future: AI's Impact on Data Science in Marketplaces

The advent of Large Language Models (LLMs) and generative AI will not automate out the human element of data science, but rather amplify its importance <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. AI massively expands the frontier of possible ideas and explanations, placing more pressure on humans to funnel down options and identify what truly matters <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. This necessitates increased data literacy among individuals interacting with these tools and each other <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>.