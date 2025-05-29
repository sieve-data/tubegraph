---
title: Common Mistakes in Building Marketplaces
videoId: BVzTfsUMaK8
---

From: [[lennyspodcast]] <br/> 

Building and managing a marketplace can be compared to a game of "whack-a-mole," where addressing one issue may cause another to emerge elsewhere in the system <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This dynamic arises because effective marketplace management involves strategically moving attention and inventory, and many significant changes create both winners and losers <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The challenge lies in recognizing whether the winners created are more important to the business than the losers <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Ramesh Johari, a professor at Stanford University, researches and teaches data science methods with a specific focus on the design and operation of online marketplaces <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. He has advised and worked with major platforms including Airbnb, Uber, Stripe, Bumble, Stitch Fix, and Upwork <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

## What a Marketplace *Really* Sells: Overcoming Friction

A common misconception is that platforms like Airbnb sell rooms or Uber sells rides <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. While individuals on the platform sell these services (e.g., hosts on Airbnb, drivers on Uber), the platform itself sells the elimination of friction <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This friction, known as [[understanding_marketplaces_and_transaction_costs | transaction costs]] in economics, is the difficulty in finding a place to stay or a driver <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. The marketplace's value proposition is taking this friction away <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

A fundamental misunderstanding that can lead to being "wildly off" is forgetting that a marketplace's core value proposition is removing [[understanding_marketplaces_and_transaction_costs | transaction costs]] <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Both sides of the marketplace (e.g., guests and hosts on Airbnb, riders and drivers on Uber) are customers of the platform, as both depend on it to reduce friction <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## Common Flaws in Starting a Marketplace

Many founders attempt to start a marketplace business in areas where such opportunities don't exist, leading to recurring failures <a class="yt-timestamp" data-t="01:11:23">[01:11:23]</a>.

### Premature Marketplace Thinking

The biggest mistake is thinking too much about building a "marketplace" *before* the business is actually a marketplace <a class="yt-timestamp" data-t="01:12:39">[01:12:39]</a>. A marketplace, at scale, removes the friction of two sides finding each other <a class="yt-timestamp" data-t="01:15:13">[01:15:13]</a>. When starting, without that scale, a founder must define their value proposition in a world without liquidity on both sides <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>.

*   **Example: UrbanSitter**
    *   UrbanSitter, a babysitting marketplace, initially addressed the friction of needing cash to pay babysitters by enabling credit card payments <a class="yt-timestamp" data-t="01:13:48">[01:13:48]</a>.
    *   Only after gaining some liquidity did they focus on solving problems like helping users find potential matches and making those matches <a class="yt-timestamp" data-t="01:16:10">[01:16:10]</a>.
    *   Their monetization model later shifted from credit card payment processing to charging for finding and contacting sitters <a class="yt-timestamp" data-t="01:14:39">[01:14:39]</a>.

*   **Example: oDesk (now Upwork)**
    *   oDesk's initial value proposition was resolving trust issues in remote work by providing tools for workers to verify hours and tasks <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>. This allowed for payment guarantees on both sides <a class="yt-timestamp" data-t="01:16:04">[01:16:04]</a>.
    *   At this early stage, liquidity wasn't the primary goal; it was solving a specific problem faced by remote workers and employers <a class="yt-timestamp" data-t="01:16:22">[01:16:22]</a>.

### Lack of Scaled Liquidity

A key test for whether a business is a marketplace is having "scaled liquidity" on both sides—meaning a lot of buyers and a lot of sellers <a class="yt-timestamp" data-t="01:23:08">[01:23:08]</a>. If a business doesn't have both, it is not yet a marketplace, even if it aims to be <a class="yt-timestamp" data-t="01:23:36">[01:23:36]</a>.

*   If only one side is scaled, the focus should be on leveraging that strength to attract the other side (e.g., Uber subsidizing drivers to attract riders) <a class="yt-timestamp" data-t="01:24:13">[01:24:13]</a>.
*   If neither side is scaled, founders should prioritize scaling one side first, focusing on general startup [[marketplace_growth_strategies | growth strategies]] rather than marketplace-specific ones <a class="yt-timestamp" data-t="01:25:05">[01:25:05]</a>.

### Rigid Early Commitments and Disintermediation

Early choices, such as a particular pricing scheme, can tie a company's hands later, especially as the platform matures <a class="yt-timestamp" data-t="01:18:38">[01:18:38]</a>.

*   For instance, platforms that take a constant fraction of transactions may face [[challenges_and_considerations_in_b2b_marketplaces | disintermediation]] when long-term relationships develop and the platform's added value decreases over time <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>.
*   [[challenges_and_considerations_in_b2b_marketplaces | Disintermediation]] occurs when parties bypass the platform once initial trust and connection are established (e.g., a service provider giving a client their business card directly) <a class="yt-timestamp" data-t="01:19:47">[01:19:47]</a>.

### The "Marketplace Founder" Fallacy

Founders should not think of themselves primarily as "marketplace founders" but simply as "founders" <a class="yt-timestamp" data-t="01:17:03">[01:17:03]</a>. In the modern tech-enabled economy, virtually any business has the option to become a platform or marketplace over time <a class="yt-timestamp" data-t="01:17:23">[01:17:23]</a>. This mindset shift prevents over-committing to a marketplace model too early and allows for broader strategic thinking <a class="yt-timestamp" data-t="01:18:05">[01:18:05]</a>.

## The Role of Data and Avoiding Experimentation Pitfalls

Data science is central to building successful marketplaces, encompassing finding matches, making matches, and learning from matches <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>.

### Prediction vs. Decision-Making

A common mistake is using machine learning models primarily for prediction (finding correlations in past data) rather than for decision-making (understanding causation) <a class="yt-timestamp" data-t="01:31:12">[01:31:12]</a>.

*   The goal of a data scientist should be to help the business make decisions that increase net value, which requires understanding *why* certain outcomes occur (causation), not just predicting them <a class="yt-timestamp" data-t="01:33:05">[01:33:05]</a>.
*   For example, a marketing manager might send promotions to customers predicted to have the highest lifetime value (LTV). However, the critical question is how much more they will spend *because* of the promotion (differential LTV), not just their absolute LTV <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

### Micro-Optimization vs. Big Opportunities

Over-reliance on [[experiments_and_decisionmaking_in_marketplaces | experimentation]] can lead to micro-optimization and missing out on larger opportunities <a class="yt-timestamp" data-t="01:39:51">[01:39:51]</a>. This often stems from:

*   **Risk Aversion in Design:** Teams tend to design and test incremental changes rather than big, risky ones <a class="yt-timestamp" data-t="01:41:52">[01:41:52]</a>.
*   **Running Experiments Too Long:** Experiments are often run longer than necessary <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>.
*   **Incentives for "Wins":** When data scientists are judged by "wins" (statistically significant positive impacts), it disincentivizes exploring riskier, potentially transformative ideas that might "fail" but offer valuable learning <a class="yt-timestamp" data-t="01:43:52">[01:43:52]</a>.

#### Shifting Culture Towards Learning

Instead of focusing on "winners and losers," experimentation should be "hypothesis-driven," emphasizing what is learned about the business <a class="yt-timestamp" data-t="01:43:50">[01:43:50]</a>.

*   A cultural shift is needed where leaders expect data scientists to articulate what they are learning, not just deliver statistically rigorous results <a class="yt-timestamp" data-t="01:54:27">[01:54:27]</a>.
*   Bayesian A/B testing can help by incorporating past learnings (prior beliefs) into future experiment analyses, rewarding teams for contributing information even if an experiment doesn't immediately "win" <a class="yt-timestamp" data-t="01:56:25">[01:56:25]</a>. This creates an "information positive externality" for the business <a class="yt-timestamp" data-t="01:57:15">[01:57:15]</a>.

### The Cost of Learning

Learning from experiments is not free; there is a cost associated with allocating resources to various options, even if some prove to be "losers" <a class="yt-timestamp" data-t="01:57:51">[01:57:51]</a>. If a "losing" option is tested, the resources allocated to it represent a missed opportunity from the "winning" option <a class="yt-timestamp" data-t="01:59:37">[01:59:37]</a>. Culturally, businesses need to recognize that paying to learn is essential <a class="yt-timestamp" data-t="01:59:59">[01:59:59]</a>.

### Rating Systems and Fairness

When designing rating systems, common mistakes include:

*   **Ignoring Rating Inflation:** Over time, median ratings tend to inflate due to reciprocity (people don't want to be mean) and norming (a lower rating might be perceived as worse over time) <a class="yt-timestamp" data-t="02:02:50">[02:02:50]</a>. Renorming the meaning of labels (e.g., using "exceeded expectations" for top ratings) can help <a class="yt-timestamp" data-t="02:03:51">[02:03:51]</a>.
*   **Blind Averaging:** Simply averaging ratings can have significant distributional consequences, especially for new entrants <a class="yt-timestamp" data-t="02:04:41">[02:04:41]</a>. A single negative review can disproportionately harm a new provider compared to an established one with many reviews <a class="yt-timestamp" data-t="02:05:05">[02:05:05]</a>. Incorporating a prior belief (e.g., using Bayesian methods) can help mitigate this by pulling new ratings towards a reasonable average, giving new providers a fairer chance <a class="yt-timestamp" data-t="02:06:01">[02:06:01]</a>.

## Conclusion

Successfully building and scaling a marketplace requires understanding its core function (removing friction), thoughtful long-term planning, a data-driven approach that prioritizes learning and causation over mere prediction, and a cultural embrace of experimentation that acknowledges the cost of learning while fostering innovation <a class="yt-timestamp" data-t="01:23:51">[01:23:51]</a>. It also involves careful consideration of how internal incentives and external systems like ratings impact the marketplace's overall health and fairness <a class="yt-timestamp" data-t="01:42:04">[01:42:04]</a>.