---
title: Significance of the BlackScholesMerton equation in finance
videoId: A5w-dEgIU1M
---

From: [[veritasium]] <br/> 

The Black-Scholes-Merton (BSM) equation is a singular mathematical formula that has profoundly transformed the financial landscape, giving rise to multiple multi-trillion dollar industries and fundamentally altering approaches to risk management <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Its core principles are rooted in [[role_of_mathematics_and_physics_in_financial_markets | physics]] and mathematics, drawing parallels from the discovery of atoms, heat transfer, and even strategies to beat casino games <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Historical Foundations: From Ancient Greece to Random Walks

The concept of [[history_and_origins_of_options_and_derivatives | options]] dates back to around 600 BC, with the Greek philosopher Thales of Miletus executing what is considered the first known call option <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Anticipating a bumper olive crop, Thales paid a small fee to secure the right to rent olive presses at a specified price in the summer <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. When his prediction proved correct and rental prices skyrocketed, he profited by renting the presses at a higher rate after paying the pre-agreed price <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Understanding Options
An option grants the holder the right, but not the obligation, to buy (a call option) or sell (a put option) an asset at a predetermined price (the strike price) by a future date <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Options offer several advantages:
*   **Limited Downside** Options limit potential losses to the premium paid <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Leverage** A small investment in an option can control a much larger value of the underlying asset, leading to magnified returns <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Hedging** Options can be used as insurance against adverse price movements, reducing risk <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### Bachelier's Pioneering Work
Despite their long history, a reliable method for pricing options remained elusive for centuries <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. In 1900, mathematics professor Louis Bachelier, studying at the Paris Stock Exchange (the Bourse), proposed a mathematical solution for option pricing as his PhD topic <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

Bachelier theorized that stock prices follow a "random walk," meaning that at any given moment, the price is equally likely to move up or down <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This concept aligns with the Efficient Market Hypothesis, which posits that asset prices reflect all available information, making it impossible to consistently profit from predicting future movements <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

Using a Galton board analogy, Bachelier demonstrated that while the path of an individual stock price is unpredictable, the collective behavior of many stock prices over time forms a predictable pattern: a normal distribution centered around the current price, spreading out over time <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. He realized this mathematical description was identical to the equation describing how heat radiates, a discovery first made by Joseph Fourier in 1822, leading Bachelier to term his finding "the radiation of probabilities" <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

> [!quote] Expected Return of an Option <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>
> Bachelier calculated the expected return of an option by multiplying the potential profit or loss by the probability of each outcome. He argued that the "fair price" of an option is what makes the expected return for both buyers and sellers equal, ensuring both parties stand to gain or lose the same amount <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

Unbeknownst to Bachelier, his work on the random walk predated Albert Einstein's 1905 explanation of Brownian motion, which described the random movement of microscopic particles as definitive evidence for the existence of atoms and molecules <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>, <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

## The Advent of Modern Option Pricing

Despite Bachelier's breakthroughs, his work went largely unnoticed by both physicists and traders <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. The missing piece was a way to consistently make significant profits.

### Ed Thorpe and Dynamic Hedging
In the 1950s, physicist Ed Thorpe, after inventing card counting to beat blackjack, applied similar principles to the stock market <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. He pioneered "dynamic hedging," a technique to protect against losses by continuously adjusting a portfolio to offset option risk with balancing stock transactions <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. This method allowed a seller to profit with minimal risk from fluctuating stock prices <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.

Thorpe also developed his own, more accurate option pricing model that accounted for a general upward or downward trend (drift) in stock prices, an improvement over Bachelier's purely random walk assumption <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. He used this model to identify undervalued or overvalued options, leading to a 20% annual return for 20 years, a record at the time <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

### The Black-Scholes-Merton Formula
In 1973, Fischer Black and Myron Scholes, with independent contributions from Robert Merton, published the equation that would revolutionize finance <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Building on Thorpe's concept of delta hedging, their model assumed that if a risk-free portfolio of options and stocks could be constructed, it should yield no more than the risk-free rate (e.g., US Treasury bonds) in an efficient market <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.

The Black-Scholes-Merton model refined Bachelier's stock price dynamics by incorporating both a random component and a general trend (drift) <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. The resulting partial differential equation yielded an explicit formula for the price of an option, allowing traders to plug in parameters and obtain a precise value <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

## Transformative Impact on Global Finance

The Black-Scholes-Merton equation's publication coincided with the founding of the Chicago Board Options Exchange in 1973 <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Its immediate adoption by Wall Street as the benchmark for option trading marked one of the fastest integrations of an academic idea into industry <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.

### Growth of Derivatives Markets
The equation fueled an explosion in the exchange-traded [[impact_of_derivatives_on_global_financial_markets | options]] market, which has since grown into a multi-trillion dollar industry, doubling in volume roughly every five years <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. Its influence extended to other massive markets, including:
*   Credit default swaps <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>
*   Over-the-counter (OTC) [[impact_of_derivatives_on_global_financial_markets | derivatives]] <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>
*   Securitized debt <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>

A [[impact_of_derivatives_on_global_financial_markets | derivative]] is a financial security whose value is derived from another underlying asset <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. The global [[impact_of_derivatives_on_global_financial_markets | derivatives]] market is estimated to be several hundred trillion dollars, vastly exceeding the value of the underlying securities <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. This seemingly counterintuitive phenomenon arises because [[impact_of_derivatives_on_global_financial_markets | options]] and [[impact_of_derivatives_on_global_financial_markets | derivatives]] allow a single underlying asset to be "turned into 5, 10, 20, 50 things," creating numerous versions tailored to different risk-reward preferences <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>.

### Risk Management and Leverage
The BSM equation revolutionized risk management, allowing large companies, governments, and individual investors to accurately and efficiently hedge against specific risks <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. For example, an airline can use an [[impact_of_derivatives_on_global_financial_markets | option]] to offset the risk of rising oil prices by buying a contract that pays off if oil increases, compensating for higher fuel costs <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.

Conversely, [[impact_of_derivatives_on_global_financial_markets | derivatives]] can also provide significant leverage, as seen in the GameStop phenomenon <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. Retail investors on Reddit's r/wallstreetbets utilized [[impact_of_derivatives_on_global_financial_markets | options]] alongside stock purchases to rapidly drive up GameStop's price, causing substantial losses for hedge funds that had bet against the company <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

### Market Stability and Instability
During normal periods, [[impact_of_derivatives_on_global_financial_markets | derivatives]] markets significantly contribute to liquidity and overall market stability <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>. However, during times of market stress, these securities can all move downward simultaneously, exacerbating market dislocations and potentially leading to severe crashes <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

## The Enduring Legacy

In 1997, Robert Merton and Myron Scholes were awarded the Nobel Prize in Economics for their groundbreaking work, with Fischer Black recognized posthumously for his contributions <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.

The widespread availability of the Black-Scholes-Merton formula shifted the focus for hedge funds from simply pricing [[impact_of_derivatives_on_global_financial_markets | options]] to identifying other market inefficiencies <a class="yt-timestamp" data-t="00:26:59">[00:26:59]</a>. This paved the way for [[contributions_of_mathematicians_and_scientists_to_investment_strategies | mathematicians]] and [[contributions_of_mathematicians_and_scientists_to_investment_strategies | physicists]] like Jim Simons.

### Jim Simons and Quantitative Trading
Jim Simons, a distinguished [[contributions_of_mathematicians_and_scientists_to_investment_strategies | mathematician]] known for his work on Riemann geometry and Chern-Simons theory, founded Renaissance Technologies in 1978 <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>. His strategy involved using machine learning and extracting patterns from vast amounts of financial data, similar to his Cold War work in code-breaking <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>. Simons purposefully hired top [[contributions_of_mathematicians_and_scientists_to_investment_strategies | scientists]] (physicists, astronomers, mathematicians, statisticians) with no prior finance experience, valuing their analytical skills <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.

Renaissance's Medallion Fund, utilizing strategies like Hidden Markov models, became the highest-returning investment fund of all time, averaging 66% per year over 30 years <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>. This unprecedented success led some to question the Efficient Market Hypothesis itself, suggesting that predictabilities *do* exist in the stock market for those with the right models, training, and computational power <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>.

The [[contributions_of_mathematicians_and_scientists_to_investment_strategies | contributions of mathematicians and physicists]] have been instrumental in modeling market dynamics, providing new insights into risk, and creating entirely new markets <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>. By accurately pricing [[impact_of_derivatives_on_global_financial_markets | derivatives]], they have helped eliminate market inefficiencies <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>. Paradoxically, the more patterns we discover in the market, the more we can eliminate them, moving closer to a truly efficient market where price movements are purely random <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>.