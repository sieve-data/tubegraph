---
title: Logistic curves and inflection points
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

The phrase [[exponential growth and decay | exponential growth]] is familiar to most people, but human intuition often struggles to fully grasp its implications <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While small numbers may initially seem insignificant, they can become surprisingly large, even if the overall trend perfectly follows an [[exponential growth and decay | exponential]] pattern <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Understanding Exponential Growth

[[exponential growth and decay | Exponential growth]] means that going from one day to the next involves multiplying by some constant <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For instance, in data related to cases of COVID-19, the number of cases each day tended to be a multiple of approximately 1.15 to 1.25 of the previous day's cases <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Viruses serve as a textbook example of this kind of growth because new cases are directly caused by existing cases <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

If `N` is the number of cases on a given day, `E` is the average number of people each infected individual is exposed to, and `P` is the probability of an exposure becoming a new infection, then the number of new cases is `E * P * N` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The fact that `N` itself is a factor in its own change causes rapid growth <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>; as `N` increases, the rate of growth also increases <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This means that adding new cases to get the next day's growth is equivalent to multiplying by a constant greater than one <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

On a logarithmic scale for the y-axis, where each fixed distance step corresponds to multiplying by a certain factor (e.g., a power of 10), [[exponential growth and decay | exponential growth]] appears as a straight line <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. For example, if numbers multiply by 10 every 16 days, a country with 60 cases might seem to be doing much better than one with 6000, but in an [[exponential growth and decay | exponential]] scenario, the former is simply about a month behind the latter <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Transition from Exponential to Logistic Growth

While an [[exponential growth and decay | exponential trend]] might initially seem to continue indefinitely, it must eventually slow down <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. [[exponential growth and decay | Exponential growth]] only persists if the factors `E` (exposure) or `P` (probability of infection) remain constant <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. It is inevitable that these factors will eventually decrease <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

Even in a model where infected individuals are exposed to a random subset of the world's population, eventually, most people they encounter would already be sick, preventing new cases <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. In such a scenario, the probability `P` of an exposure leading to a new infection would need to include a factor accounting for the likelihood that the exposed person is already infected <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. For a random shuffling model, this might involve a factor like "1 minus the proportion of people in the world who are already infected" <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

Including this factor and solving for how `N` grows yields what is known as a **logistic curve** <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Characteristics of a Logistic Curve
A logistic curve is essentially indistinguishable from an [[exponential growth and decay | exponential]] at its beginning <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. However, it ultimately levels out once it approaches the total population size <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. "True exponentials essentially never exist in the real world; every one of them is the start of a logistic curve" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## The Inflection Point

The **inflection point** of a logistic curve is where the curve transitions from curving upward to curving downward <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. At this point, the number of new cases each day, represented by the [[Tangent lines and slopes | slope]] of the curve, stops increasing and remains roughly constant before starting to decrease <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Growth Factor as an Indicator
The growth factor, defined as the ratio between the number of new cases on one day and the number of new cases the previous day, is often tracked with epidemics <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

While on the [[exponential growth and decay | exponential]] part of the curve, this growth factor consistently stays above one <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. However, as soon as the growth factor approaches one, it signals that the inflection point has been reached <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

Even though a growth factor of one (indicating the inflection point) and a factor slightly greater than one (still in the [[exponential growth and decay | exponential]] phase) might seem subtly different in terms of daily totals <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, their implications are vast <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. If the growth factor is one, the total number of cases might max out at about double the current number <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. But if it's still bigger than one, even slightly, it means orders of magnitude of growth could still lie ahead <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Influencing the Curve

Saturating the entire population is not the sole cause for the factors `E` (amount of exposure) and `P` (infection rate) to decrease <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. Human actions can directly influence these factors:
*   Exposure (`E`) can decrease when people reduce gatherings and travel <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Infection rate (`P`) can decrease with improved hygiene, such as more frequent hand washing <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

[[exponential growth and decay | Exponential growth]] is highly sensitive to the constant multiplier <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. For example, a 15% daily growth rate could lead to over 100 million cases in 61 days from 21,000 <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. However, if that rate drops to 5% due to reduced exposure and infection, the projection significantly lowers to around 400,000 cases <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This highlights that collective action can dramatically alter the trajectory of a logistic curve <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.