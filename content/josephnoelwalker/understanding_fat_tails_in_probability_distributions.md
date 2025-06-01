---
title: Understanding fat tails in probability distributions
videoId: cP5tQGWagKc
---

From: [[josephnoelwalker]] <br/> 

Nassim Nicholas Taleb's work, particularly "The Black Swan," introduces the concept of the platonic fold and the statistical consequences of fat tails, which significantly influence fields ranging from finance to social science <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a> <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Fat Tails vs. Thin Tails

A key distinction in [[probability_and_prediction_in_finance_and_economics | probability and prediction]] is between "thin-tailed" and "fat-tailed" (or "thick-tailed") probability distributions <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

*   **Thin-tailed distributions** (e.g., Gaussian or normal distribution) assume that extreme deviations are highly improbable and have a limited impact on the overall distribution <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. In such environments, large deviations can "destroy the assumption" of using that distribution <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Fat-tailed distributions** (or "large deviation models" / [[nassim_talebs_theories_on_extremistan | Extremistan models]]) acknowledge that extreme events are more probable and carry significant consequences <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. In these environments, even "quiet periods" are statistically consistent, as are large deviations; nothing can truly surprise a fat-tailed model because it accounts for extremes <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Identifying Fat Tails

One must assume they are in an [[nassim_talebs_theories_on_extremistan | Extremistan model]] unless there are compelling, robust reasons to rule it out <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a> <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

Reasons to rule out fat tails (i.e., confirm a thin-tailed process):
*   **Physical or Biological Limitations**: Processes with inherent boundaries, like human height, are thin-tailed. A person cannot be five kilometers tall because biological limitations require a mother, and there's no unlimited energy <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a> <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a> <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. A Gaussian distribution, for instance, assumes a bounded variance, which is equivalent to bounding energy <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Knowledge of the Generating Process**: If one possesses deep understanding of the underlying physical or biological generator of a phenomenon, they might rule out extreme deviations <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Processes typically exhibiting fat tails:
*   **Multiplicative Phenomena**: Processes like contagions, pandemics, or wealth accumulation tend to be multiplicative, leading to fat-tailed distributions <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a> <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>.
*   **Unbounded Movements**: Phenomena like prices, where there are no physical limitations on how high they can go, are fat-tailed <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a> <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a> <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **No Characteristic Scale**: In an [[nassim_talebs_theories_on_extremistan | Extremistan]] environment, there's no "typical event" or "standard deviation" <a class="yt-timestamp" data-t="00:52:20">[00:52:20]</a> <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>. The ratio of events (e.g., a 10 million-person event vs. a 5 million-person event) remains constant, unlike Gaussian distributions where deviations shrink further from the mean <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a> <a class="yt-timestamp" data-t="00:53:33">[00:53:33]</a>. This concept, central to [[mandelbrots_influence_on_understanding_extreme_events | Mandelbrot's influence]], indicates that standard deviation doesn't have meaning in [[nassim_talebs_theories_on_extremistan | Extremistan]] <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a> <a class="yt-timestamp" data-t="00:55:12">[00:55:12]</a>.

### Power Laws and Log-Normal Distributions

*   **Power Laws**: These distributions, where extreme events are common, appear widely in nature and society <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Taleb is skeptical of "cute theories" that try to assign fixed tail exponents (e.g., 3 for financial markets, 1.5 for company size), noting that such observations are very noisy and can be influenced by technology <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a> <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a> <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Log-Normal Distributions**: These arise from multiplicative processes <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>. If a Gaussian distribution is exponentiated, it results in a log-normal distribution, which can also be fat-tailed, especially at high variance <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a> <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a> <a class="yt-timestamp" data-t="00:36:15">[00:36:15]</a>. If a thin-tailed but slightly fatter-tailed distribution (like exponential or gamma) is exponentiated, it yields a power law (Pareto distribution) <a class="yt-timestamp" data-t="00:38:06">[00:38:06]</a> <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>.

## Implications in Finance

[[the_impact_of_fat_tails_on_prediction_and_option_value | Fat tails]] are crucial for understanding financial markets.
*   **Options Pricing**: Taleb realized before 1987 that volatility should not be flat across strike prices for options <a class="yt-timestamp" data-t="00:30:32">[00:30:32]</a> <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. He observed large deviations frequently, particularly after the Plaza Accord's 10-sigma move in 1985 <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. This led to the understanding that "tail options" (out-of-the-money options that pay off big during extreme events) should be priced higher than conventional models like Black-Scholes would suggest <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a> <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Winner-Take-All Effects**: Finance exhibits "winner-take-all effects," which are incompatible with a Gaussian representation <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>.
*   **Tail Hedging**: Despite the evident benefits, the [[the_impact_of_fat_tails_on_prediction_and_option_value | tail hedging]] strategy (buying tail options) is not fully priced into markets <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This is attributed to:
    *   **Blinding Theories**: People are blinded by academic theories like Modern Portfolio Theory <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
    *   **Incentives**: Institutional frameworks incentivize making money frequently, which often means selling volatility, rather than buying it for long-term tail protection <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a> <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a> <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. Markets may price convexity in some way, but they don't know how to price it correctly <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Venture Capital**: While power laws describe startup success, Venture Capitalists (VCs) often concentrate their bets rather than diversify <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a> <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. Taleb argues this isn't about optimizing for true success, but rather a "greater fool" compensation scheme: VCs make money by hyping ideas and cashing in as new investors are brought in, not by waiting for real cash flow <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a> <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a> <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. Their skill lies in packaging, not predicting market success <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## Critiques of Conventional Statistical Methods

Taleb argues that many conventional statistical methods and interpretations are flawed, especially in the presence of fat tails.

### Behavioral Economics and Rationality

Initially more sympathetic to behavioral economics, Taleb later found its practitioners often misunderstood probability structures and dynamics <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. He views "rationality" as survival, not adherence to theoretical constructs <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.

Many supposed "biases" identified in [[debates_in_behavioral_economics | behavioral economics]] are, in fact, rational strategies under different assumptions or in the real world:
*   **Equity Premium Puzzle**: The "puzzle" that people prefer bonds to stocks (despite historical stock performance) is not irrational when considering tail risks that thin-tailed analyses miss <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a> <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.
*   **"One-over-N" Rule**: Spreading investments evenly among many choices (the "one-over-N" rule) is optimal under fat tails, contrary to claims that people should reduce their choices <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.
*   **Probability Matching**: Allocating resources proportional to probabilities (e.g., 40% to a 40% chance, 60% to a 60% chance) is optimal for long-term growth (e.g., via Kelly Criterion), even if it doesn't maximize expected single-instance payoffs <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a> <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a> <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.
*   **Refusing a Bet**: Refusing a bet with a 55% win probability can be rational if viewed dynamically, as repeatedly taking such bets might lead to ruin (an "uncle point") <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a> <a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a>.
*   **Mental Accounting**: Seemingly irrational practices like treating money won from a casino differently are often rational for survival ("playing with the house money") <a class="yt-timestamp" data-t="02:00:25">[02:00:25]</a> <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.

[!NOTE]
Danny Kahneman, co-founder of [[debates_in_behavioral_economics | behavioral economics]], publicly acknowledged that his prospect theory, while correct for certain loss functions, doesn't necessarily apply to [[the_impact_of_fat_tails_on_prediction_and_option_value | fat-tailed]] environments, effectively conceding to Taleb's argument <a class="yt-timestamp" data-t="00:40:11">[00:40:11]</a> <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.

### Forecasting and Binary Payoffs

Taleb's core disagreement with "superforecasting" lies in the distinction between [[binary_versus_continuous_payoffs_in_options_trading | binary versus continuous payoffs]] <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a>.
*   **Binary Payoffs**: Forecasting projects often focus on binary outcomes (yes/no) or clipped payoffs, like "will there be a war?" <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a> <a class="yt-timestamp" data-t="00:52:04">[00:52:04]</a>. However, in fat-tailed domains, the *size* of the event (e.g., how many people die in a war) is a random variable, making a binary forecast meaningless <a class="yt-timestamp" data-t="00:52:09">[00:52:09]</a> <a class="yt-timestamp" data-t="00:52:35">[00:52:35]</a>.
*   **Consequentiality**: Superforecasting often selects events that are inconsequential or very small and restricted <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.
*   **Misleading Metrics**: In [[the_impact_of_fat_tails_on_prediction_and_option_value | fat-tailed]] environments, metrics like R-scores (which track binary probabilities) can be misleading <a class="yt-timestamp" data-t="01:03:27">[01:03:27]</a>. For example, a high accuracy rate in predicting daily market movements is meaningless if the infrequent large movements cause massive losses <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>.
*   **No Rich Forecasters**: Taleb notes that people who are good at forecasting in traditional institutions are rarely rich, implying that their predictions don't translate to financial success in fat-tailed environments <a class="yt-timestamp" data-t="01:04:40">[01:04:40]</a> <a class="yt-timestamp" data-t="01:06:43">[01:06:43]</a>.

### The Shadow Mean

In fat-tailed distributions, the empirically observed mean (sample mean) can be a severely biased underestimate of the true population mean (the "shadow mean") <a class="yt-timestamp" data-t="01:23:51">[01:23:51]</a> <a class="yt-timestamp" data-t="01:25:36">[01:25:36]</a>. This occurs because most observations will be below the true mean, and extreme events, which heavily influence the mean, are rare and may not appear in a limited sample <a class="yt-timestamp" data-t="01:25:32">[01:25:32]</a> <a class="yt-timestamp" data-t="01:27:02">[01:27:02]</a>. For instance, the observed mean of an industry like biotech, which is heavy-tailed, will underestimate its true mean <a class="yt-timestamp" data-t="01:26:14">[01:26:14]</a>.

### Correlation

Taleb states that "correlation isn't correlation" <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   **Misunderstanding**: Many social scientists and even practitioners use correlation without fully understanding its meaning or limitations <a class="yt-timestamp" data-t="01:44:22">[01:44:22]</a>.
*   **Non-linearity**: For decision-making, the predictive power of correlation is highly nonlinear; low correlations are effectively noise <a class="yt-timestamp" data-t="01:46:09">[01:46:09]</a>. A 0.5 correlation is not halfway between zero and one <a class="yt-timestamp" data-t="01:46:16">[01:46:16]</a>.
*   **Sub-additivity**: Correlation is sub-additive in absolute terms, meaning subsampling a dataset won't accurately represent the correlation of the whole <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>.
*   **Dilution by Error**: Even a "good" R-squared value (e.g., 0.5) is diluted significantly by model error, making it less useful for individual cases <a class="yt-timestamp" data-t="01:49:15">[01:49:15]</a>.
*   **Fat-tailed Issues**: One cannot simply regress a fat-tailed variable (like income) against a thin-tailed one (like IQ) because they have fundamentally different designs <a class="yt-timestamp" data-t="01:49:45">[01:49:45]</a>.

### Mean Absolute Deviation (MAD) vs. Standard Deviation (SD)

Taleb prefers Mean Absolute Deviation (MAD) over Standard Deviation (SD) as a measure of dispersion <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a> <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a>.
*   **Physical Intuition**: MAD (the average of absolute deviations from the mean) has a more direct physical intuition than SD (the square root of the average of squared deviations) <a class="yt-timestamp" data-t="01:59:05">[01:59:05]</a>.
*   **Efficiency for Gaussian**: SD became traditional because it was found to be more "efficient" than MAD *in the Gaussian case* <a class="yt-timestamp" data-t="01:58:37">[01:58:37]</a>.
*   **Indicator of Fatness**: The ratio of standard deviation to mean deviation is the best indicator of a distribution's "fatness" <a class="yt-timestamp" data-t="02:00:37">[02:00:37]</a>. For a Gaussian, SD is about 25% higher than MAD; for fat-tailed distributions (e.g., with an alpha below two, like the Cauchy distribution), the SD can be infinite while the MAD is finite <a class="yt-timestamp" data-t="02:00:47">[02:00:47]</a>.

## Real-World Examples of Fat Tails

### Pandemics

Pandemics are [[the_impact_of_fat_tails_on_prediction_and_option_value | fat-tailed]] events, driven by multiplicative processes <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a> <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>. The number of people killed in pandemics follows a distribution with a tail exponent of approximately 0.5 <a class="yt-timestamp" data-t="00:57:38">[00:57:38]</a> <a class="yt-timestamp" data-t="00:57:40">[00:57:40]</a>. This means:
*   **Unpredictable Scale**: It's foolish to give a single-point forecast for deaths, as 95% of observations will be below the mean <a class="yt-timestamp" data-t="00:58:15">[00:58:15]</a> <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>.
*   **Exponential Growth**: A small error in the growth rate (R) of a contagion can lead to an enormous error in the total number of people affected, as the total grows exponentially (WT = W0 * e^(RT)) <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a> <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This can result in an infinite expectation for the total number of cases, even with a finite expectation for the growth rate <a class="yt-timestamp" data-t="01:02:12">[01:02:12]</a>.
*   **Precautionary Principle**: For multiplicative risks like pandemics, precautions must be taken to "kill it in the egg" by cutting off the distribution of paths and reducing connectivity (e.g., border controls, testing, quarantines) <a class="yt-timestamp" data-t="01:39:57">[01:39:57]</a> <a class="yt-timestamp" data-t="01:40:30">[01:40:30]</a>.

### Warfare

Warfare also exhibits [[the_impact_of_fat_tails_on_prediction_and_option_value | fat-tailed]] properties <a class="yt-timestamp" data-t="01:27:11">[01:27:11]</a>.
*   **Shadow Mean of Deaths**: The historical data on war deaths visibly underestimates the true mean because extreme events are so rare they haven't all occurred in the observed sample <a class="yt-timestamp" data-t="01:27:20">[01:27:20]</a>. The true process for war deaths is likely three times deadlier than what has been observed <a class="yt-timestamp" data-t="01:27:23">[01:27:23]</a>.
*   **Inter-arrival Time**: The waiting time for wars of a certain magnitude (e.g., over 10 million deaths) is exponentially distributed and memoryless <a class="yt-timestamp" data-t="01:28:27">[01:28:27]</a> <a class="yt-timestamp" data-t="01:29:02">[01:29:02]</a>. This means that even if a war hasn't happened in 100 years, the expectation for the next one remains the same <a class="yt-timestamp" data-t="01:29:17">[01:29:17]</a>. Therefore, 80 years without a World War II-scale conflict provides no statistical evidence that violence is declining <a class="yt-timestamp" data-t="01:36:44">[01:36:44]</a> <a class="yt-timestamp" data-t="01:37:44">[01:37:44]</a>.
*   **Changing Scale, Not Fatness**: The *fatness* (alpha) of war distributions remains consistent over time, but the *scale* (the absolute number of deaths) can change, particularly with the development of more destructive technologies and globalization <a class="yt-timestamp" data-t="01:32:10">[01:32:10]</a> <a class="yt-timestamp" data-t="01:32:16">[01:32:16]</a> <a class="yt-timestamp" data-t="01:30:05">[01:30:05]</a>.
*   **Exaggeration of Death Counts**: Historically, both conquerors (for intimidation) and victims (due to glorification of victimhood in religions like Christianity and Shia Islam) had incentives to exaggerate death counts <a class="yt-timestamp" data-t="01:33:14">[01:33:14]</a> <a class="yt-timestamp" data-t="01:33:54">[01:33:54]</a> <a class="yt-timestamp" data-t="01:34:20">[01:34:20]</a>.

## Conclusion

Understanding [[the_impact_of_fat_tails_on_prediction_and_option_value | fat tails]] is crucial for making informed decisions in a world dominated by extremes. Conventional statistical methods, often designed for thin-tailed distributions, can provide misleading results and lead to flawed policies when applied to complex, unbounded systems <a class="yt-timestamp" data-t="01:42:16">[01:42:16]</a>. True rationality, in Taleb's view, lies in survival and adapting to the dynamic, fat-tailed nature of reality <a class="yt-timestamp" data-t="01:15:17">[01:15:17]</a>.