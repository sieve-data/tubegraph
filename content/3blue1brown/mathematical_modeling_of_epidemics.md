---
title: mathematical modeling of epidemics
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

Mathematical modeling, particularly concerning [[exponential_growth | exponential growth]], helps understand and predict the spread of epidemics <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. While the phrase [[exponential_growth | "exponential growth"]] is familiar, human intuition often struggles to fully grasp its implications <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Small initial numbers can quickly become surprisingly large, even if the overall trend remains consistently exponential <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Understanding Exponential Growth in Epidemics

[[exponential_growth | Exponential growth]] means that the number of cases from one day to the next involves multiplication by a constant factor <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Viruses are a textbook example of this growth pattern because existing cases directly lead to new ones <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For instance, in the COVID-19 data at the time of recording, the number of cases tended to be about 1.15 to 1.25 times the number from the previous day <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

The core of this growth can be expressed mathematically:
If `n` is the number of cases on a given day, `e` is the average number of people each infected individual is exposed to daily, and `p` is the probability of an exposure leading to a new infection, then the number of new cases is `e × p × n` <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The crucial aspect is that `n` (the number of existing cases) is a factor in its own change, meaning the rate of growth itself increases as `n` gets larger <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This effectively means multiplying the total by a constant greater than one each day <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Visualizing Exponential Growth
[[exponential_growth | Exponential growth]] can be counterintuitive when looking at linear graphs. However, on a logarithmic scale for the y-axis, [[exponential_growth | exponential growth]] appears as a straight line <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This scale represents each fixed distance step as a multiplication by a certain factor, often a power of 10 <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For example, COVID-19 data showed an approximate multiplication by 10 every 16 days on average <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Statistical analysis confirms that this exponential fit is "really freaking close" to real-world epidemic data <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

Consider two countries, one with 6,000 cases and another with 60 cases <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. While it seems the second is 100 times better, if numbers multiply by 10 every 16 days, the second country is only about a month behind the first <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Limitations of Exponential Growth: The Logistic Curve

[[exponential_growth | Exponential growth]] cannot continue indefinitely <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It must slow down at some point <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. This slowdown occurs because the number of exposures (`e`) or the probability of infection (`p`) must eventually decrease <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Even in a worst-case scenario where individuals are exposed to random subsets of the population, eventually, many of those exposed would already be sick, preventing new cases <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

This phenomenon is captured by the [[SIR model for epidemic simulation | SIR model]] and results in a [[logistic_growth_and_inflection_point | logistic curve]] <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. A [[logistic_growth_and_inflection_point | logistic curve]] is nearly indistinguishable from an exponential at the beginning but eventually levels out as it approaches the total population size <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. True exponentials rarely exist in the real world; they are almost always the start of a [[logistic_growth_and_inflection_point | logistic curve]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### The Inflection Point and Growth Factor

The [[logistic_growth_and_inflection_point | inflection point]] is where the [[logistic_growth_and_inflection_point | logistic curve]] transitions from curving upward to curving downward <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. At this point, the number of new cases per day (represented by the curve's slope) stops increasing and then begins to decrease <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A key metric in epidemic modeling is the **growth factor**, defined as the ratio between the number of new cases on one day and the number of new cases the previous day <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

*   During the [[exponential_growth | exponential]] phase, this factor remains consistently above one <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   When the growth factor approaches one, it signals that the inflection point has been reached <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

This can be counterintuitive: a growth factor of one, meaning the number of new cases is stable, suggests the epidemic is at its [[logistic_growth_and_inflection_point | inflection point]] and the total cases will max out at roughly double the current number <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. However, a growth factor even slightly greater than one, while seemingly subtle, indicates the epidemic is still in its [[exponential_growth | exponential]] phase, implying orders of magnitude of growth potentially still ahead <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Factors Slowing Epidemic Growth

While reaching saturation of the population is one way growth slows, it's not the only way <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. Human interventions can also reduce the `E` (exposure) or `P` (infection probability) factors <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>:
*   **Reduced Exposure (E):** People stopping large gatherings and travel <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Reduced Infection Rate (P):** Practices like increased handwashing <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

### Role of Community Structure

The [[role_of_community_structure_in_disease_spread | assumption that individuals are randomly shuffled around the world's population]] is an oversimplification <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. People are clustered in local communities <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. However, simulations show that even with limited travel between clusters, the overall growth pattern remains similar, exhibiting a fractal pattern where communities themselves function like individuals, subject to the same [[exponential_growth | exponential-inducing laws]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### Sensitivity to Small Changes and Human Behavior

A crucial and optimistic counterintuitive fact about [[exponential_growth | exponential growth]] is its extreme sensitivity to the constant growth factor <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   If the growth rate is 15% (meaning total cases multiply by 1.15 daily), 21,000 cases could become over 100 million in 61 days <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   However, if through changes in exposure and infection, that rate drops to 5%, the projection for the same period drops dramatically to around 400,000 <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

This illustrates the profound [[impact_of_human_behavior_on_epidemic_spread | impact of human behavior]]: if people are sufficiently worried and act accordingly, the severity of an epidemic can be significantly mitigated <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Conversely, a lack of concern can lead to rapid and widespread escalation <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.