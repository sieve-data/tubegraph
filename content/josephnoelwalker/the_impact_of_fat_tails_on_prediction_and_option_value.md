---
title: The impact of fat tails on prediction and option value
videoId: bn1YGi9u-pM
---

From: [[josephnoelwalker]] <br/> 

The concept of "fat tails" in [[understanding_fat_tails_in_probability_distributions | probability distributions]] has significant implications for both financial predictions and the valuation of options. A core disagreement between traditional forecasting methods, such as "super forecasting," and an understanding rooted in the nature of extreme events lies in the distinction between binary and continuous payoffs [00:00:06].

## Binary vs. Continuous Payoffs in Options Trading

In options trading, a naive person might assume that an out-of-the-money binary option would increase in value if the probability distribution's tail fattens [00:00:37]. However, the opposite is true: they go *down* in value when the tail fattens [00:00:47]. This is because a binary option represents a probability [00:00:49].

Consider a Gaussian curve:
*   Fattening the tail means that the probabilities of being above or below a certain sigma (e.g., plus or minus one standard deviation, which normally encompasses about 68% for a Gaussian curve [00:00:56]) actually drop [00:01:17].
*   This occurs because the variance of the distribution becomes more explained by rare events, causing the "body" of the distribution to go up while the "shoulders" narrow [00:01:22]. This implies more "ordinary" events because the deviations that do occur are much more pronounced [00:01:31].

From an options trader's perspective, this means that making a bet using binary options or anything that "clips your upside" is the wrong strategy [00:01:42]. Experienced option traders understand this, whereas rookies or individuals from other fields (like economics) often express their bets using such binary structures [00:01:52]. There is a crucial difference between a bet that pays a fixed $1 and one that pays "a lot" due to full randomness [00:02:06]. For instance, one might be bullish on the market's probability of going up, but short on the expectation (the payoff) [00:02:24]. These concepts do not translate well outside of option trading [00:02:34].

## The Nature of Events in Fat-Tailed Distributions

A significant problem with forecasting, particularly within [[limitations_of_traditional_forecasting_methods | traditional forecasting methods]], is the tendency to sub-select events that are forecastable but ultimately inconsequential [00:02:47]. Such questions are often very small and restricted [00:02:55].

Furthermore, in distributions with fat tails, there is no such thing as a "standard event" [00:03:00]. For example, a "war" can mean an event that kills two people or one that kills 600,000 [00:03:09]. As [[Mandelbrots influence on understanding extreme events | Benoit Mandelbrot]] frequently repeated, "there is no such thing as a standard deviation in extremistan" [00:03:17]. One cannot simply judge an event by saying "there's a pandemic or no pandemic" because the *size* of the event is itself a random variable [00:03:32].

### Scale-Free Distributions
In [[understanding_fat_tails_in_probability_distributions | scale-free distributions]] (like a Pareto distribution), the ratio between outcomes remains constant [00:03:46]. For example, the ratio of 10 million people to 5 million people is approximately the same as 20 million to 10 million [00:03:54]. The consequence is that there is no "standard event" or "typical event" [00:04:10].

This differs from a Gaussian distribution, where the expected deviation above a certain sigma (e.g., 3 Sigma) is only slightly more than that sigma, and it shrinks as you consider higher deviations [00:04:29]. For instance, life expectancy at birth might be 80 years, but at 100 years, it's only two additional years [00:04:51]. In contrast, in "extremistan" (fat-tailed domains), the scale remains the same [00:05:05]. An "expected company" with sales higher than $10 million might be $15 million, and one higher than $100 million might be $150 million [00:05:20]. The numbers don't shrink; in fact, proportionally they stay the same, but in absolute terms, they can "explode" [00:05:58]. This explosion signifies the absence of a standard large deviation [00:06:04].

This idea, which posits "no characteristic scale," provides a simple framework to understand events like the 1987 market crash [00:06:30]. This perspective was foundational to works like *The Black Swan*, which was dedicated to [[Mandelbrots influence on understanding extreme events | Mandelbrot]] based on this characteristic scale idea [00:06:51].

## Implications for Forecasting

The absence of a characteristic scale makes forecasting problematic, as it is "sterile" [00:07:05]. What comes "above" (e.g., higher than $10 million or $100 million) has distinct meaning [00:07:23].

A paper was written arguing against point forecasts for fat-tailed variables [00:08:00]. For example, one might be good at forecasting the growth rate (R) of a disease like COVID, but this cannot be directly translated into how many people will be killed (WT) [00:12:24]. If the relationship is exponential (WT = W0 * e^(RT)), a small error in R can lead to a Pareto distribution for WT [00:13:00]. This implies that there can be an infinite expectation for WT with a finite explanation in R [00:13:12].

This also relates to the [[limitations_of_traditional_forecasting_methods | VAR-Sear dilemma]]:
*   **Value-at-Risk (VAR)** states that "within 95% confidence, you won't lose more than a million" [00:13:37].
*   **Conditional Expectation (Sear)** highlights that the remaining 5% is where the significant action lies, as conditional on losing more than a million, one might lose 200 million [00:13:56].

The exponential transformation applies to VAR as well: while probability itself is bounded between zero and one (and can be fat-tailed), the transformation of that probability outside of a Gaussian framework can be "explosive" due to its concave/convex nature [00:14:09].

## The Payoff Function and Real-World Value

A crucial distinction in the world of [[probability_and_prediction_in_finance_and_economics | finance and economics]] is that one is paid in "dollars and cents," not just frequency [00:10:57]. People who are good at forecasting in banks are rarely rich [00:15:34]. The true test of a forecasting method is whether it enables one to make money [00:18:06].

The central problem with traditional forecasting is that it often isolates forecasting from the payoff function [00:18:21]. For example, when predicting volatility, an option trader might consistently overestimate volatility by 30% but still make money, because the "bet against volatility" (selling options) is nonlinear, and volatility comes in lumps [00:17:01].

### Probability as a Kernel
A deeper understanding of probability reveals that probability is not a product but a "kernel"—something that adds up to one and cannot be isolated [00:19:40]. A probability density function (P(X)) by itself has no standalone meaning [00:20:45]. It only gains meaning when integrated with some function G(X), which represents the payoff [00:20:51]. Whether G(X) is an indicator function (for binary outcomes) or a continuous, convex, or concave function fundamentally changes the implications [00:20:51]. Option traders, therefore, discuss the value of the option (the payoff) rather than just raw probabilities [00:21:50].