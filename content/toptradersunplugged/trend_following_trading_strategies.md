---
title: Trend following trading strategies
videoId: 3GuNVdlgJ-Q
---

From: [[toptradersunplugged]] <br/> 

## Introduction

[[trend_following_strategies | Trend following]] involves learning from the experiences, successes, and failures of leading hedge fund managers in the world, enabling individuals to enhance their manager due diligence or investment career [00:00:10]. All discussions regarding investment performance pertain to the past, and past performance offers no guarantee or inference about future performance [00:00:35]. Furthermore, all investment strategies carry a significant risk of financial loss, and it is crucial to understand the specific risks from the investment manager before making any decisions [00:00:43].

## Evaluating [[trend_following_strategies | Trend Following Strategies]]

Understanding the strategy and ensuring a consistent track record are paramount for investors [00:03:04]. While it's easy to state, this consistency can be complex to verify, especially in the systematic world where the strategy isn't explicitly known [00:03:21]. Despite acknowledging the bias, investors are always influenced by track records, even from a brief glance at metrics like Sharpe and Sortino ratios [00:03:38]. The most crucial aspect of a track record is not merely the past, but a combination of understanding the strategy and observing its past performance align with expectations [00:04:00]. As the strategy performs "out of sample," it should deliver expected results within reasonable bounds [00:04:20].

For example, if a [[trend_following_strategies | trend following]] strategy is perceived as long volatility, problems arise when volatility increases or equity declines, leading to difficult explanations [00:04:33].

### Challenges and Performance

The perception that [[trend_following_strategies | trend following]] has underperformed in recent years due to excessive money chasing the strategy post-2008 is a common query [00:05:00]. The performance of [[trend_following_strategies | trend following]] systems, like any portfolio system, depends on correlation and diversification across markets [00:05:31].

From 2008 until late 2013, correlations across futures markets significantly increased and remained high, unlike the lower correlations observed in the prior 20 years [00:06:00]. While divergent events like quantitative easing or the nuclear meltdown in Japan did occur, high correlation means low diversification [00:06:27]. This lack of diversification, coupled with low volatility, meant that even with some trends, the risk was high, leading to a difficult period for [[trend_following_strategies | trend following]] [00:06:46]. Although some profits were made, there wasn't enough diversification to support performance consistent with historical patterns [00:07:15].

Price range compression, visible in the difference between highs and lows over rolling periods, also contributed to smaller trends and reduced opportunities for [[trend_following_strategies | trend followers]] in recent years [00:07:29]. Both high correlation and price compression combined to create a challenging environment [00:08:28].

Historically, [[trend_following_strategies | trend following]] is long divergence [00:19:24]. If inflation causes divergence, the strategy benefits [00:19:29]. It is designed to adapt to spectacular market moves [00:19:52]. It does not matter whether there is deflation or inflation; as long as divergence is created, it is favorable for [[trend_following_strategies | trend followers]] [00:20:11].

Data from 1720 to 2013 shows that average returns for a [[trend_following_strategies | trend following]] system varied with inflation [00:20:40]:
*   Low inflation to deflationary environments: ~10.4% [00:20:51].
*   5% to 10% inflation: ~10.1% [00:20:57].
*   High inflation: ~15% [00:21:02].
This suggests that extreme environments, both very high and possibly extremely low inflation/deflation, tend to create divergence and opportunities [00:21:05].

## Components of a [[trend_following_strategies | Trend Following]] System

A framework for [[trend_following_strategies | trend following]] is built around one core formula [00:10:59].

### Four Key Questions of [[trend_following_strategies | Trend Following]]
1.  When to enter [00:11:29].
2.  How large a position to take on [00:11:33].
3.  How to get out of a position [00:11:35].
4.  How much risk to allocate to any particular position [00:11:38].

### Five Key Building Blocks
1.  Data processing [00:11:51].
2.  Signal generation [00:11:53].
3.  Position sizing [00:11:53].
4.  Market allocation [00:11:56].
5.  Execution [00:11:56].

The most important of these is **position sizing** [00:12:02]. A single formula for position sizing is a function of several variables:
*   Nominal position amount = Sizing function * Risk loading * Capital allocated to that market / (Total adjusted dollar risk * Dollar risk of a position) [00:12:18].
    *   **Sizing function**: Indicates conviction strength; for example, if moving average models suggest a strong trend, the sizing function weights based on those rules [00:12:22].
    *   **Risk loading**: A simple loading of risk across markets allowing for levering positions up and down [00:13:20].
    *   **Capital allocated**: The dollar amount invested in the position [00:13:36].
    *   **Dollar risk of that one contract**: Multiplies the capital allocated [00:13:41].
    *   **Total adjusted dollar risk**: Divides to adjust for volatility across different futures contracts (e.g., Lean Hogs vs. Oil), reducing capital allocation for more volatile assets to maintain the same risk exposure [00:13:46].

### Signal Generation
Signal generation, whether through moving averages or breakout channels, is left open as part of the sizing function [00:14:20]. For instance, a moving average system would use moving averages to create the sizing function, which could involve a basket of averages [00:14:47]. This aspect highlights the "art" in [[trend_following_strategies | trend following]] [00:15:08].

### Importance of Exit Rules
The exit from a trade is a very important part of the entire process, distinct from the entry decision [00:16:19]. Trading systems with agnostic entry rules (e.g., random coin flip) still demonstrate performance from getting out of positions, emphasizing the significance of exit decisions [00:16:43].

The concept of "Trend leakage" examines how often a [[trend_following_strategies | trend following]] system's position is positively correlated with a future trend position [00:17:26]. Trend leakage exists and is time-varying; sometimes trends leak into market prices, but often, performance is driven by effectively exiting positions when trends disappear [00:17:38]. Therefore, exits largely determine the performance environment [00:18:26].

## Risk Management in [[trend_following_strategies | Trend Following]]

Risk management is considered the greatest asset of the CTA industry [00:24:08]. A sophisticated understanding and effective system for allocating risk over time represent the major value added by professional management [00:24:17].

For example, perfect foresight of a market's price one year from now (e.g., oil) would still carry huge risk if the position is held without management, as market movements could wipe out capital [00:24:56]. However, by applying risk management, the Sharpe ratio of such an approach dramatically improves over time, and drawdowns are reduced [00:25:29]. Thus, risk management is the primary value added by any [[trend_following_strategies | trend following]] system [00:25:58].

Understanding how a manager changes their risk and what causes them to allocate more or less risk to a position is crucial [00:26:59]. Real dangers arise from dynamic leveraging or accelerating positions [00:27:11]. It's important to know if risk allocation is conditional and whether leverage is a function of past P&L [00:27:28].

### Hidden and Unhidden Risks
*   **Unhidden risks** are those that manifest in price, such as price risk [00:28:35].
*   **Hidden risks** are those that do not show up in price until they occur, inflating Sharpe ratios [00:28:45].
    *   **Liquidity risk**: Does not show up until it arrives and is hard to measure beforehand [00:28:49].
    *   **Credit risk**: Difficult to estimate credit quality and appears in shocks [00:29:00].
    *   **Leverage**: While it can be transparent, risk can be embedded through dynamic leveraging where losing bets are doubled, creating cyclicality that may not show up on slower frequencies [00:29:28]. Most [[trend_following_strategies | trend following]] systems avoid this [00:30:02].

Option strategies, for instance, apply dynamic leveraging (Delta of a call option increases with P&L), which can lead to increased leverage and suffering during market downturns, unlike a [[trend_following_strategies | trend following]] strategy that avoids such dynamic leveraging [00:31:31].

## Drawdowns in [[trend_following_strategies | Trend Following]]

[[trend_following_strategies | Trend followers]] typically experience more frequent but shorter drawdowns compared to equity strategies [00:32:46]. This is because [[trend_following_strategies | trend following]] is systematically exposed only to price risk, without the hidden risks that create huge, rare drawdowns [00:33:33].

However, the past few years have seen many managers, even those with decades of experience, face larger and longer drawdowns than previously observed [00:34:01]. Research suggests that [[trend_following_strategies | trend following]] performance tends to be depressed after a crisis, as markets need time to restabilize and readjust [00:35:32]. The recent prolonged period of difficulty for [[trend_following_strategies | trend following]] strategies might be attributed to the severity and ongoing fallout of the crisis [00:36:21]. With correlations now decreasing and market issues being sorted, the strategy appears to be bouncing back [00:37:07].

A key challenge is educating investors to navigate the emotional rollercoaster of drawdowns and avoid redeeming or reducing investments at the worst possible time [00:38:13]. Investors often "[[trend_following_strategies | trend follow]] [[trend_following_strategies | trend following]]" by buying high and selling low [00:38:30]. Since [[trend_following_strategies | trend following]] tends to be mean-reverting over the long run, investors should "buy low and sell high" [00:39:51]. For example, when equity markets are at historic highs, some investors reallocate to CTAs, profiting from this counter-intuitive move [00:40:31].

One advantage of [[trend_following_strategies | trend following]] is its use of futures, which ensures a controlled amount of capital at risk and limits on price moves for some markets [00:41:52]. [[trend_following_strategies | Trend following]] managers have a strong history of understanding their exact notional risk exposure, which is not always as transparent in traditional investments [00:42:26]. Operational risks (like MF Global events) and hidden risks (which do not apply to [[trend_following_strategies | trend following]]) are the primary concerns [00:42:52]. Futures markets proved robust during the financial crisis, with many swap dealers going bankrupt while futures markets remained open [00:43:12].

## Benchmarking and Style Analysis

Detecting if a manager's system has stopped working comes back to benchmarking and understanding their style [00:43:50]. When a manager's delivered performance deviates from their stated expectations, it raises questions [00:44:08]. Noise in performance, such as one manager being up 10% while another is only up 2%, highlights that every system is designed to capture divergence, and each divergence is different [00:44:21]. Investors should inquire about the reasons for performance differences, whether it was due to a single position or general risk allocation, and if the manager has explanations that might reassure them in different scenarios [00:44:53].

Benchmarking in the industry is challenging, often compared to comparing a fruit salad to an apple, given the wide return dispersion among different strategies [00:46:10]. Although managers may have high correlations, their differences in performance are significant [00:46:44].

A framework for style analysis can be created, similar to the Fama-French three-factor model [00:47:30]. This involves constructing a pure "Divergent risk-taking strategy" as a basic benchmark [00:47:45]. This Bayesian system uses the best estimate of an uptrend to determine position, with simple trailing stops for exit [00:47:56].

Additional "tweak" factors can then be added:
*   **Size factor**: Represents the difference between a market-capacity-weighted index and an equally weighted index, indicating the value added by including smaller markets [00:48:49]. In 2013, a negative size factor meant bigger markets outperformed smaller ones [00:50:22].
*   **Equity bias**: Measures the impact of adding cash equities or having long-minus-short biases [00:49:07].
*   **Trading speed**: The difference between slow and fast trading approaches [00:49:23].

These factors allow for the analysis of individual managers, determining how they fit into this structure and what their loadings are for each factor [00:49:38].

## The [[trend_following_strategies | Trend Following]] Industry: Challenges and Future

The biggest challenge for the [[trend_following_strategies | trend following]] industry is overcoming past performance struggles and consistently delivering by capturing divergent market opportunities, thereby re-entering the mainstream hedge fund strategies of interest [00:50:57]. Other key challenges include adapting to a new market environment with more players, different capital flows (retail vs. institutional), increased competition, and new threats like High-Frequency Trading (HFT) [00:51:21].

Regulation, particularly in Europe (like AIFMD), poses a significant challenge for smaller managers by limiting investor access for sub-threshold managers [00:59:03]. This suggests that regulations may stifle innovation from smaller, newer firms in the hedge fund industry [01:00:06]. While regulation is beneficial, it ultimately increases costs for investors and creates barriers to entry [01:00:36].

Looking ahead, the worst may be over for the [[trend_following_strategies | trend following]] space, but it remains a bumpy ride [01:03:09]. The strategy and industry are expected to continue delivering value over time by sticking to their principles [01:03:18].

## Qualities of a Good [[trend_following_strategies | Trend Following]] Manager

A successful [[trend_following_strategies | trend following]] manager needs to be able to communicate effectively [00:55:22]. This means clearly defining their identity, articulating their value proposition, detailing what they will deliver to investors, and explaining how they will appropriately handle risk [00:55:27]. This clear and structured communication is fundamental [00:55:41]. Building a CTA from small to large also requires significant hard work [00:56:37].

Additionally, understanding the "why" behind a manager's actions is important, as it often differentiates one manager from another and helps communicate their unique value proposition [00:56:57].

Investors should push for more transparency in how different strategies are constructed [00:53:36]. They should also ask more questions about back-testing to ensure managers are not simply data-fitting to past results [00:53:47]. A closer look at interday leverage application is also important, as it can vary greatly between managers and impact risk [00:54:01].