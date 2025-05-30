---
title: Risk Management in Trading
videoId: 6myigI5buI4
---

From: [[toptradersunplugged]] <br/> 

The Systematic Investor podcast series frequently explores the world of rules-based investing, with a special focus on strategies like trend following. A recurring and critical theme in these discussions is [[risk_management_in_trading | risk management]], particularly as it applies to systematic trading systems <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Esteemed trend following and systematic trading legend, Perry Kaufman, shares his insights on this vital aspect of successful investing <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Core Philosophy of System Design and Risk

Perry Kaufman emphasizes a philosophical approach to system development that prioritizes flexibility over precision. His guiding principle, "loose pants fits everyone," suggests that trading systems should not be overly specific or constrained <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. The market is highly unpredictable in the short term, necessitating systems that can hold positions through various market conditions <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

Instead of fine-tuning a system to reduce risk, Kaufman argues that traders must first come to grips with the amount of [[understanding_and_managing_trading_risks | risk]] they are willing to accept and manage that [[risk_management_strategies | risk]] differently <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. He states that attempting to fine-tune a system to reduce [[risk_management_in_trading | risk]] "really doesn't work" because [[risk_management_in_trading | risk]] will inevitably appear elsewhere, likening it to a game where pushing down [[risk_management_in_trading | risk]] in one place causes it to pop up in another <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. The objective, therefore, is to understand the true [[risk_management_in_trading | risk]] and manage the portfolio to prevent being wiped out <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

## Measuring and Managing Volatility

A key component of [[risk_management_techniques_in_trading | risk management]] is measuring [[risk_management_in_trading | risk]] effectively. Kaufman highlights the importance of measuring [[risk_management_in_trading | risk]] based on the *system's* daily returns or Net Asset Values (NAVs), rather than the underlying volatility of individual markets <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

Moritz Siebert's contribution, "volatility stabilization" (or volatility targeting), is a significant improvement in this area <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This approach involves targeting a specific acceptable volatility for the portfolio (e.g., 12% annualized, a common industry standard) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. If the portfolio's volatility goes above the target, positions are cut; if it falls below, leverage is increased <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The surprising outcome of this method is that most of the improvement comes from *raising* volatility to the target when it drops, preventing a significant reduction in expected returns <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

Moritz further elaborates that while traders cannot control returns, they can control [[risk_management_in_trading | risk]] by sizing positions in relation to what they are willing to accept <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Different traders define and manage [[risk_management_in_trading | risk]] in profoundly different ways, some equating it directly to volatility, others using value-at-risk, or basing position sizing on average true range <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

## Position Sizing and Market Selection

Position sizing is identified as the critical first step in [[risk_management_in_trading | risk control]] <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>. For futures traders, a "volatility parity" approach ensures that every trade carries the same [[risk_management_in_trading | risk]] <a class="yt-timestamp" data-t="01:07:23">[01:07:23]</a>.

Kaufman advocates for selecting markets based on their historical performance under the system's rules, focusing on *return* rather than a risk-adjusted metric like the Sharpe ratio <a class="yt-timestamp" data-t="02:21:30">[02:21:30]</a>. He believes that "the more restrictions you put on performance the worse the future results will be" <a class="yt-timestamp" data-t="02:19:07">[02:19:07]</a>. His process involves:
*   **Ranking Returns**: Ranking the returns of each stock or futures market over a relatively short period (e.g., 60 days) <a class="yt-timestamp" data-t="02:57:58">[02:57:58]</a>.
*   **Persistence**: Believing that markets performing best on his system will continue to do so, like Amazon or Tesla <a class="yt-timestamp" data-t="01:58:50">[01:58:50]</a>.
*   **Dynamic Selection**: Re-ranking daily and replacing markets if they fall significantly in rank (e.g., four positions) <a class="yt-timestamp" data-t="02:28:20">[02:28:20]</a>.
*   **Market Universe**: Limiting exposure to a specific number of top-performing markets (e.g., 20-22 for futures) <a class="yt-timestamp" data-t="03:39:58">[03:39:58]</a>.
*   **Sector Diversification**: Reducing total exposure if diversification across sectors is limited, for instance, trading less if only one sector qualifies <a class="yt-timestamp" data-t="03:40:02">[03:40:02]</a>.

Kaufman also uses an "efficiency ratio" to select markets that are more trending (higher ratio) or noisy (lower ratio), indicating suitability for trend following or mean reversion strategies, respectively <a class="yt-timestamp" data-t="04:16:46">[04:16:46]</a>. He explains that newer, emerging markets tend to be more trending due to less noise from diverse participants <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

## Profit Targets, Stop Losses, and Extreme Risk Exits

For **short-term trading**, profit targets can be effective, often taken in multiple parts to reduce [[risk_management_in_trading | risk]] as profits accumulate <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

However, for **long-term trend following**, both profit targets and strict stop losses are generally discouraged <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>. Trend following success hinges on capturing "fat tail" events—long, continuous moves <a class="yt-timestamp" data-t="04:07:07">[04:07:07]</a>. Taking profits or stopping out prematurely can eliminate the possibility of capturing these significant moves. While re-entry rules can be developed, they complicate the system and typically lead to inferior long-term results compared to simply staying with the position <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

Perry Kaufman has implemented an **extreme [[risk_management_in_systematic_trading | risk management]] exit** in his systems, especially for smaller, potentially highly correlated portfolios. This involves bailing out completely if the portfolio's volatility (e.g., 32% annualized for stocks) is too high *and* the market is net down for a specific number of days (e.g., three days) <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. This acts as an emergency measure to protect against scenarios where market correlations converge (e.g., during a crisis), and money is withdrawn across all asset classes simultaneously <a class="yt-timestamp" data-t="01:23:31">[01:23:31]</a>.

## Diversification and Long-Term Outlook

While Perry Kaufman prefers to focus on the top-performing markets in his portfolio, limiting "over-diversification" beyond 10-20 good markets, Moritz advocates for broader diversification <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. Moritz argues that even if the additional diversification benefit mathematically declines after a certain number of markets, it is never zero as long as markets are not perfectly correlated <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>. He sees this as a "free snack" that should be exploited to increase the sample size of the system and capture potential future "rockstar performance" from any market <a class="yt-timestamp" data-t="01:19:14">[01:19:14]</a>.

Kaufman acknowledges that long-term trends persist due to economic factors and central bank policies, which drive interest rate trends that can take months or years to unfold <a class="yt-timestamp" data-t="01:53:43">[01:53:43]</a>. However, he notes that increased market noise means it takes longer for trend following systems to identify trend changes, resulting in entering and exiting trends later and potentially extracting a smaller portion of the overall move <a class="yt-timestamp" data-t="01:55:23">[01:55:23]</a>. Despite this, he firmly believes that trends will continue to exist <a class="yt-timestamp" data-t="01:55:56">[01:55:56]</a>.

Ultimately, both experts emphasize that [[risk_management_in_investment_firms | risk management]] is a personal choice. Traders must find a [[risk_management_in_trading_strategies | risk management strategy]] and position sizing approach that they are comfortable with and can stick to over the long term, as consistency and patience are crucial for systematic investing success <a class="yt-timestamp" data-t="01:15:11">[01:15:11]</a>.