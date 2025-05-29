---
title: COVID19 pandemic analysis
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

Human intuition often struggles to recognize the implications of exponential growth, even when data consistently follows such a trend <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Small numbers can quickly become large, causing surprise <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The recorded cases of COVID-19, also known as the coronavirus, serve as a real-world example to explore the nature, implications, and eventual end of exponential growth <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Understanding Exponential Growth

Exponential growth signifies that moving from one day to the next involves multiplying by a constant factor <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. In the early stages of the COVID-19 data, the number of cases each day tended to be 1.15 to 1.25 times the number of cases from the previous day <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### How Viruses Grow Exponentially

Viruses are a classic example of this growth pattern because existing cases directly cause new cases <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. If 'n' is the number of cases on a given day, 'e' is the average number of people each infected individual is exposed to daily, and 'p' is the probability of an exposure leading to a new infection, then the number of new cases is calculated as `e * p * n` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The presence of 'n' as a factor in its own change accelerates the growth rate significantly <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This means that to get the next day's growth, you essentially multiply by a constant greater than one <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Visualizing Growth

To better visualize exponential growth, a logarithmic scale on the y-axis can be used <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. On this scale, where each step represents multiplication by a certain factor (e.g., a power of 10), exponential growth appears as a straight line <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

Analysis of early COVID-19 data showed it took 20 days to increase from 100 to 1,000 cases, and then 13 days to go from 1,000 to 10,000 cases <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. A linear regression on this logarithmic scale indicated that cases multiplied by 10 approximately every 16 days on average <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The statistical fit of this exponential model to the data was extremely close <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### The "Month Behind" Analogy

When comparing countries, seeing one with 6,000 cases and another with 60 might suggest the latter is significantly better off <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. However, in an exponential growth scenario where numbers multiply by 10 every 16 days, the country with 60 cases is merely about a month behind the one with 6,000 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

If the early trend continued, a projection from March 6th would suggest reaching one million cases in 30 days, 10 million in 47 days, 100 million in 64 days, and one billion in 81 days <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Limits to Exponential Growth: The [[logistic_growth_and_inflection_point | Logistic Curve]]

True exponential growth cannot continue indefinitely <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It must eventually slow down <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. The reason for this expected slowdown is that either the exposure rate ('E') or the probability of infection ('P') must decrease <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. For example, if every infected person exposed a random subset of the world's population, eventually many people they encounter would already be sick, thus unable to become new cases <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This means the probability of an exposure leading to a new infection ('p') would need to account for the proportion of the population already infected <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### The [[sir_model_for_epidemic_simulation | SIR Model]] and [[logistic_growth_and_inflection_point | Logistic Curve]]

In a random shuffling model, including a factor like "1 minus the proportion of people in the world who are already infected" into the probability 'p' leads to what is known as a [[sir_model_for_epidemic_simulation | SIR model]] and results in a [[logistic_growth_and_inflection_point | logistic curve]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. A [[logistic_growth_and_inflection_point | logistic curve]] is initially indistinguishable from an exponential curve but eventually levels out as it approaches the total population size <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. In reality, every exponential growth pattern is merely the beginning of a [[logistic_growth_and_inflection_point | logistic curve]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### The [[logistic_growth_and_inflection_point | Inflection Point]] and Growth Factor

The [[logistic_growth_and_inflection_point | inflection point]] on a [[logistic_growth_and_inflection_point | logistic curve]] is where the curve shifts from curving upward to curving downward <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. At this point, the number of new cases daily stops increasing and may remain constant before starting to decrease <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

The **growth factor** in epidemics is defined as the ratio between the number of new cases on one day and the number of new cases the previous day <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. While in the exponential phase, this factor remains consistently above one <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. When the growth factor approaches one, it signals that the [[logistic_growth_and_inflection_point | inflection point]] has been reached <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

This leads to a counterintuitive reality: a growth factor of one, where the number of new cases is roughly stable, could mean the total number of cases will max out at about twice the current level <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. However, a growth factor even slightly larger than one, which might seem subtle, indicates that the epidemic is still in its exponential phase, implying orders of magnitude of growth are still possible <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## [[Impact of human behavior on epidemic spread | Factors Influencing Epidemic Spread]]

While the worst-case saturation point for an epidemic is the total population, real-world viral spread is not characterized by random shuffling of infected individuals across the globe <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. People are clustered in local communities <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Even with minimal travel between such clusters, simulations show that the overall growth pattern remains similar, manifesting as a fractal pattern where communities themselves act like individuals, leading to the same underlying exponential-inducing laws <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### [[impact of public health measures on virus spread | Public Health Measures]] and Sensitivity

Fortunately, factors beyond population saturation can reduce 'E' (exposure) and 'P' (probability of infection) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. For instance, [[effectiveness of social distancing | exposure can decrease when people stop gathering and traveling]], and the infection rate can fall when people improve hygiene, such as washing hands more <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

Exponential growth is highly sensitive to small changes in its constant multiplier <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. For example, if the growth rate is 15% and there are 21,000 cases, it would lead to over 100 million cases in 61 days <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. However, if that rate drops to 5% due to reduced exposure and infection, the projection for 61 days would decrease drastically to around 400,000 cases <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This demonstrates that if the public is sufficiently concerned and takes [[impact of public health measures on virus spread | preventative measures]], the overall risk is significantly reduced <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Conversely, a lack of concern is cause for worry <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.