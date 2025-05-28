---
title: Impact of derivatives on global financial markets
videoId: A5w-dEgIU1M
---

From: [[veritasium]] <br/> 

Derivatives, financial instruments whose value is derived from an underlying asset, have profoundly transformed the global financial landscape and everyone's approach to risk <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The sheer scale and utility of derivatives are often unknown to most people <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. At its core, the equation that spawned four multi-trillion dollar industries comes from physics, from discovering atoms, understanding heat transfer, and even strategies to beat casinos <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## [[history_and_origins_of_options_and_derivatives | History and Origins of Options and Derivatives]]

The earliest known options contracts were bought around 600 BC by the Greek philosopher Thales of Miletus <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Anticipating a large olive crop, Thales paid olive press owners a small fee to secure the right to rent their presses at a predetermined price in the summer <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. When the bumper harvest arrived, press rental prices skyrocketed, and Thales profited by renting the presses at a higher rate than his pre-agreed price <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This transaction represents the first known "call option" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Types of Options
*   **Call Option**: Gives the holder the right, but not the obligation, to buy an asset at a set price (the strike price) by a later date <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This is useful when expecting the asset's price to go up <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Put Option**: Gives the holder the right, but not the obligation, to sell an asset at the strike price by a later date <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This is useful when expecting the asset's price to go down <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Advantages of Options
Options offer several advantages:
1.  **Limited Downside**: They limit potential losses to the premium paid for the option, unlike direct stock ownership where losses can be much larger <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
2.  **Leverage**: A small investment in an option can control a much larger value of the underlying asset, potentially leading to much higher percentage returns on investment <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. For example, a $10 option leading to a $20 profit represents a 200% return <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
3.  **Hedging**: Options can be used as a hedge to protect against losses or reduce risk in an investment portfolio <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. The original motivation for options was to reduce risk, acting like insurance <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

## Early Mathematical Approaches to Option Pricing

### Louis Bachelier and the Random Walk
In 1900, Louis Bachelier, a mathematics student who worked at the Paris Stock Exchange (the Bourse), became fascinated by options <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Despite centuries of options trading, no one had found a reliable way to price them <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Bachelier believed there had to be a mathematical solution and proposed it as his PhD topic to Henri Poincaré <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

Bachelier realized that while individual market factors (weather, politics, etc.) are impossible to predict, the overall movement of stock prices over the long term follows a random walk <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. He proposed that the expected future price of a stock is described by a normal distribution, centered on the current price and spreading out over time <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

This concept connected to established scientific principles:
*   **Radiation of Probabilities**: Bachelier's discovery was the exact equation Joseph Fourier had found in 1822 to describe how heat radiates <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Brownian Motion**: Five years after Bachelier, Albert Einstein independently used the mathematics of the random walk to explain Brownian motion, the random movement of particles observed by Robert Brown in 1827 <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. Einstein's work provided definitive evidence for the existence of atoms and molecules <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

Bachelier's key insight for pricing options was that the fair price should make the expected return for both buyers and sellers equal <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. Despite his groundbreaking work, it went largely unnoticed by both the physics and finance communities at the time <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

## Ed Thorpe and Dynamic Hedging
In the 1950s, physicist Ed Thorpe, famous for inventing card counting in blackjack, applied his skills to the stock market, pioneering a type of hedging <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. Thorpe's hedge fund achieved an unprecedented 20% annual return for 20 years <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.

Thorpe's method involved **dynamic hedging**, where a seller of an option could adjust their stock holdings to offset the risk from price fluctuations <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. This technique allows for the synthetic manufacturing of options, eliminating the need to take the opposite side of a trade directly <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. Thorpe also developed a more accurate option pricing model than Bachelier's, accounting for the general drift (increase or decrease) in stock prices over time <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. He kept this model quiet for his own investors <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

## [[Significance of the BlackScholesMerton equation in finance | Significance of the Black-Scholes-Merton Equation in Finance]]

The landscape changed dramatically in 1973 when Fischer Black and Myron Scholes (and independently, Robert Merton) published their option pricing equation <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Their approach assumed that a risk-free portfolio of options and stocks (similar to Thorpe's delta hedging) in an efficient market should only yield the risk-free rate, like that of US treasury bonds <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. They used an improved version of Bachelier's random walk model, incorporating a general trend or drift <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.

The resulting equation, the most famous in finance, provided an explicit formula to calculate the price of any contract related to an asset <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. This meant that for the first time, traders had a direct number they could plug in to use for trading <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

## Impact on Global Financial Markets

The publication of the Black-Scholes-Merton equation coincided with the founding of the Chicago Board Options Exchange in 1973 <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. Its rapid adoption by Wall Street as the benchmark for trading options led to an explosion in the exchange-traded options market, which is now a multi-trillion dollar industry <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>. This growth is compared to Moore's Law, doubling roughly every five years <a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>.

Beyond options, the Black-Scholes-Merton idea has fueled the growth of other multi-trillion dollar industries, including:
*   Credit default swaps market <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>
*   OTC (Over-The-Counter) derivatives market <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>
*   Securitized debt market <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>

### Risk Management and Leverage
The equation opened new ways to hedge against various risks <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. Large companies, governments, and even individual investors now use options to manage specific risks, such as an airline hedging against rising oil prices <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

Options also provide significant leverage, as seen in the GameStop phenomenon <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. Small investments in options can influence the equivalent of much larger amounts of stock, amplifying price movements and leading to rapid gains or losses <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

### Scale and Stability
The global derivatives market is estimated to be on the order of several hundred trillion dollars, multiples of the underlying securities they are based on <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. This is because derivatives allow the creation of many different versions of an underlying asset, catering to diverse risk-reward preferences <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.

Regarding market stability, derivatives have a dual impact <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>:
*   **Normal Times**: They are a significant source of liquidity and thus contribute to market stability <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.
*   **Abnormal Times**: During periods of market stress, these securities can all move in one direction (typically down), exacerbating market crashes and dislocations <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.

In 1997, Myron Scholes and Robert Merton were awarded the Nobel Prize in economics for their contributions, with Fischer Black acknowledged posthumously <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.

## [[Contributions of mathematicians and scientists to investment strategies | Contributions of Mathematicians and Scientists to Investment Strategies]]

The [[role_of_mathematics_and_physics_in_financial_markets | role of mathematics and physics in financial markets]] has been pivotal <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Many of the best to beat the stock market were not veteran traders but physicists, scientists, and mathematicians <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Jim Simons and Renaissance Technologies
A prime example is Jim Simons, a mathematics professor who founded the Medallion Investment Fund in 1988 <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. For 30 years, the Medallion fund consistently delivered returns significantly higher than the market average, averaging 66% per year <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This made Simons the richest mathematician of all time <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

Simons' strategy at Renaissance Technologies, founded in 1978, was to use machine learning to find patterns in the stock market <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>. Having previously worked on breaking Russian codes by extracting patterns from data during the Cold War, Simons applied a similar approach to finance <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>. He intentionally hired top scientists, astronomers, and mathematicians with PhDs who had little to no prior knowledge of finance <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.

The Medallion fund, utilizing strategies like Hidden Markov models pioneered by Leonard Baum, became the highest-returning investment fund ever <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>. Its success led some, like Bradford Cornell of UCLA, to suggest that the Efficient Market Hypothesis itself might be wrong, indicating that market predictability exists if one possesses the right models, training, resources, and computational power <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.

## Conclusion

The profound impact of derivatives on global financial markets stems from the foundational work of mathematicians and physicists who modeled market dynamics <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. By providing new insights into risk and accurately pricing complex financial instruments, they have helped eliminate market inefficiencies and opened up entirely new markets <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>. While the pursuit of patterns can lead to significant profits, ironically, fully understanding and exploiting all market patterns could ultimately lead to a perfectly efficient market where all price movements are truly random <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>.