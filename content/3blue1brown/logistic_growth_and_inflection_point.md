---
title: logistic growth and inflection point
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

## Logistic Growth Explained

While [[exponential_growth | exponential growth]] is a familiar concept, human intuition often struggles to recognize its implications fully <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. In reality, true [[exponential_growth | exponentials]] essentially never exist in the real world; instead, every [[exponential_growth | exponential growth]] phase is actually the start of a logistic curve <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>, <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.

A logistic curve describes growth that is initially [[exponential_growth | exponential]] but ultimately levels out <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. For instance, in [[mathematical_modeling_of_epidemics | epidemic models]], if the probability of an exposure leading to a new infection accounts for the proportion of people already infected, the growth curve shifts from [[exponential_growth | exponential]] to logistic <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>, <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>, <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. This means that as a population approaches its total size, the growth rate naturally slows down <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

### Why Exponential Growth Slows Down
[[Exponential growth and decay | Exponential growth]] in phenomena like viral spread occurs because new cases are directly proportional to existing cases <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>, <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>, <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. This involves multiplying by a constant factor each day <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>, <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>, <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. This continues as long as two factors (E, the average number of people an infected individual is exposed to, and P, the probability of exposure leading to new infection) remain constant or above a certain threshold <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

Growth eventually slows down when:
*   **Saturation:** A significant portion of the population becomes infected, meaning new exposures are likely to be to people who are already sick <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>, <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **Reduced Exposure (E):** People stop gathering and traveling, decreasing the opportunities for spread <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
*   **Reduced Infection Rate (P):** Measures like increased handwashing reduce the probability of transmission upon exposure <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.

## Inflection Point

The **inflection point** is a critical moment on a logistic curve where the rate of growth begins to slow <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. Specifically, it's the point where the curve transitions from curving upward to curving downward <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

At the inflection point:
*   The number of new cases each day (represented by the slope of the curve) stops increasing <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
*   The daily new cases remain roughly constant for a period before starting to decrease <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

### Growth Factor and Inflection
The **growth factor** is a metric often followed in [[mathematical_modeling_of_epidemics | epidemics]], defined as the ratio between the number of new cases on one day and the number of new cases the previous day <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>, <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>, <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

*   During the [[exponential_growth | exponential]] phase, this factor consistently stays above one <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
*   When the growth factor approaches one, it signals that the inflection point has been reached <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>, <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

A growth factor of one at the inflection point implies that the total number of cases will roughly max out at about double the current total <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>, <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>, <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>. In contrast, a growth factor even slightly greater than one, though it may seem subtle, indicates that the system is still in the [[exponential_growth | exponential]] phase, with orders of magnitude of growth potentially still ahead <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>, <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>, <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.