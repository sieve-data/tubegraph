---
title: exponential growth
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

The phrase [[exponential_growth_and_decay | exponential growth]] is familiar to most people, yet human [[intuition_behind_the_growth_of_exponential_functions | intuition]] often struggles to fully grasp its implications <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It can lead to surprise when numbers, initially small, suddenly become very large, even if the overall trend follows an [[exponential_growth_and_decay | exponential]] pattern consistently <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

A prominent example of [[exponential_growth_and_decay | exponential growth]] is the data for recorded cases of COVID-19, or coronavirus <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Defining Exponential Growth

[[exponential_growth_and_decay | Exponential growth]] means that as a quantity progresses from one period (e.g., day) to the next, it involves multiplying by some constant factor <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. In the context of COVID-19 case data, the number of cases each day tended to be a multiple of approximately 1.15 to 1.25 of the cases from the previous day <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

Viruses are a classic example of this type of growth because new cases are directly caused by existing cases <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. If 'n' represents the number of cases on a given day, 'e' is the average number of people each infected individual exposes daily, and 'p' is the probability of an exposure leading to a new infection, then the number of new cases is calculated as `e * p * n` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The crucial aspect is that 'n' (the current number of cases) is a factor in its own rate of change, causing rapid acceleration: as 'n' increases, the growth rate itself increases <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This mechanism results in the total number of cases being multiplied by a constant greater than one each day <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Visualizing Exponential Growth

Visualizing [[exponential_growth_and_decay | exponential growth]] can be easier on a logarithmic scale <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. On this scale, each step of a fixed distance represents multiplication by a certain factor (e.g., a power of 10) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. When plotted on a logarithmic scale, [[exponential_growth_and_decay | exponential growth]] appears as a straight line <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

For instance, COVID-19 data showed it took 20 days to increase from 100 to 1,000 cases, and 13 days to go from 1,000 to 10,000 cases <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. A linear regression analysis of this data suggests that the number of cases tended to multiply by 10 every 16 days on average <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The statistical fit of this [[exponential_growth_and_decay | exponential]] model was described as "really freaking close" <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Counterintuitive Implications
One counterintuitive aspect of [[exponential_growth_and_decay | exponential growth]] is how relative numbers can be misleading <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. If numbers multiply by 10 every 16 days, a country with 60 cases, compared to one with 6,000 cases, is not necessarily "fine" despite having 100 times fewer cases <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Instead, it might simply be about a month behind the first country in its progression <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

If the trend observed on March 6th were to continue, the number of cases would reach one million in 30 days, 10 million in 47 days, 100 million in 64 days, and one billion in 81 days <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## When Exponential Growth Ends: The Logistic Curve

A truly [[exponential_growth_and_decay | exponential]] line cannot continue indefinitely <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It must eventually slow down <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. The reason to expect [[exponential_growth_and_decay | exponential growth]] in the first place is that new cases are proportional to existing cases <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This means multiplying by a constant every day <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This multiplication only ceases if either the exposure rate ('E') or the probability of infection ('P') decreases <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

It is inevitable that this will happen <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. In a theoretical model where every infected person randomly exposes others globally, eventually most exposed people would already be sick, thus unable to become new cases <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This means the probability of an exposure becoming a new infection would need to account for the proportion of the population already infected (e.g., `1 - proportion already infected`) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

Including such a factor leads to what is known as a [[logistic_growth_and_inflection_point | logistic curve]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. A [[logistic_growth_and_inflection_point | logistic curve]] is virtually indistinguishable from an [[exponential_growth_and_decay | exponential]] at the beginning but ultimately levels out as it approaches the total population size <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. True [[exponential_growth_and_decay | exponentials]] rarely exist in the real world; every apparent [[exponential_growth_and_decay | exponential]] is typically the initial phase of a [[logistic_growth_and_inflection_point | logistic curve]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### The Inflection Point
The point where a [[logistic_growth_and_inflection_point | logistic curve]] transitions from curving upward to curving downward is called the [[logistic_growth_and_inflection_point | inflection point]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. At this point, the number of new cases each day (represented by the slope of the curve) stops increasing and either remains roughly constant or begins to decrease <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Growth Factor
In epidemics, a key metric is the growth factor, defined as the ratio between the number of new cases on one day and the number of new cases on the previous day <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. On the [[exponential_growth_and_decay | exponential]] part of the curve, this factor consistently stays above one <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. When the growth factor approaches one, it signals that the [[logistic_growth_and_inflection_point | inflection point]] has been reached <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

This can be another source of counterintuitive understanding <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. A situation where new cases are about 15% more than the previous day might not *feel* drastically different from a situation where new cases are about the same <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. However, a growth factor of one suggests reaching the [[logistic_growth_and_inflection_point | inflection point]] of a [[logistic_growth_and_inflection_point | logistic curve]], implying the total number of cases will roughly double from that point <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Conversely, a growth factor slightly greater than one, though subtle, indicates that the system is still in the [[exponential_growth_and_decay | exponential]] phase, with orders of magnitude of growth potentially still ahead <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Factors Influencing Growth
While the worst-case scenario involves saturation of the total population, real-world situations are more complex than a random shuffling model <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. People are clustered in local communities <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Even with some travel between clusters, the growth pattern can still be similar, resembling a fractal pattern where communities themselves act like individuals, leading to the same underlying [[exponential_growth_and_decay | exponential-inducing]] laws <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

Fortunately, several factors can cause the exposure rate and infection probability to decrease:
*   People stopping gathering and traveling reduces exposure <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   Improved hygiene, like hand washing, can lower the infection rate <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

Another counterintuitive aspect of [[exponential_growth_and_decay | exponential growth]], this time more optimistically, is its sensitivity to the constant growth factor <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. For example, starting with 21,000 cases and a 15% daily growth rate would lead to over 100 million cases in 61 days <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. However, if that rate drops to 5% due to less exposure and infection, the projection doesn't just decrease by a factor of three; it dramatically drops to around 400,000 cases <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This highlights that if people are sufficiently concerned and take action, there is significantly less to worry about; conversely, a lack of concern can be a cause for worry <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.