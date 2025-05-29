---
title: Understanding exponential growth
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

The phrase [[exponential_growth_and_decay | exponential growth]] is familiar to most people, yet human intuition often struggles to grasp its true implications <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Small initial numbers can lead to surprising large outcomes, even when the overall trend is perfectly consistent with [[exponential_growth_and_decay | exponential]] patterns <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Defining Exponential Growth

[[exponential_growth_and_decay | Exponential growth]] means that moving from one day to the next involves multiplying by a constant factor <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. For example, in data for recorded COVID-19 cases, the number of cases each day tended to be a multiple of about 1.15 to 1.25 of the previous day's cases <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Viruses are a [[applications_of_exponential_growth_in_natural_phenomena | textbook example]] of this growth type because new cases are caused by existing ones <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### The Mechanism of Growth
If 'n' is the number of cases on a given day, 'e' is the average number of people each infected individual exposes, and 'p' is the probability of an exposure leading to a new infection, then the number of new cases is `e * p * n` <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The fact that 'n' (the current number of cases) is a factor in its own change is what causes rapid acceleration <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. As 'n' grows, the rate of growth itself increases <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This is equivalent to multiplying the total cases by a constant greater than 1 each day <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Visualizing Exponential Growth

To better visualize [[exponential_growth and decay | exponential growth]], a logarithmic scale for the y-axis can be used <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. On this scale, each fixed distance step represents multiplication by a certain factor (e.g., a power of 10) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. When plotted on a logarithmic scale, [[exponential_growth_and_decay | exponential growth]] appears as a straight line <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

Using data, a linear regression can determine the best fit line. For instance, if cases multiply by 10 every 16 days on average, this indicates a strong [[exponential_growth_and_decay | exponential]] fit <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Counterintuitive Implications

One counterintuitive aspect of [[exponential_growth_and_decay | exponential growth]] is how different initial states can quickly converge. A country with 60 cases versus one with 6,000 might seem vastly different, but if numbers multiply by 10 every 16 days, the second country is only about a month behind the first <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

If an [[exponential_growth_and_decay | exponential trend]] continues, numbers can escalate rapidly:
*   From 10,000 cases to 1 million in 30 days <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   To 10 million in 47 days <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   To 100 million in 64 days <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   To 1 billion in 81 days <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## The Limits of Exponential Growth: The Logistic Curve

[[True exponentials | True exponentials]] essentially never exist in the real world <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>; every observed instance is the start of a logistic curve <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

A logistic curve initially mimics [[exponential_growth_and_decay | exponential growth]] but eventually levels out as it approaches a total population size <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This leveling occurs because factors like 'e' (exposure) or 'p' (infection probability) must decrease <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. For example, if a large proportion of the population is already infected, the probability of exposure leading to a *new* infection decreases <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Inflection Point
The point where a logistic curve transitions from curving upward to curving downward is called the [[inflection point]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. At this point, the number of new cases each day stops increasing and remains roughly constant before starting to decrease <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## The Growth Factor

The growth factor is the ratio between the number of new cases on one day and the number of new cases the previous day <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   During the [[exponential_growth_and_decay | exponential part]] of a curve, this factor consistently stays above one <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   When the growth factor approaches one, it signals that the [[inflection point]] has been reached <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

A subtle difference in the growth factor can have vastly different implications:
*   A growth factor of one might mean the total number of cases will max out at about twice the current total <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   A growth factor slightly greater than one, however, means the system is still in the [[exponential_growth_and_decay | exponential part]], implying orders of magnitude of growth are still possible <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## Halting Exponential Growth

While an idealized model might suggest saturation at the total population, real-world factors like people clustering in local communities and less random shuffling of individuals modify the spread <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. However, even with slight travel between clusters, the growth follows similar [[applications_of_exponential_growth_in_natural_phenomena | exponential-inducing laws]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

Fortunately, the two key factors contributing to growth ('E' for exposure and 'P' for infection probability) can be reduced <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>:
*   Exposure can decrease when people stop gathering and traveling <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Infection rates can go down with practices like increased hand washing <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

[[exponential_growth_and_decay | Exponential growth]] is highly sensitive to the constant multiplier <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. For instance, a 15% daily growth rate could lead to over 100 million cases in 61 days from 21,000 <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. But if that rate drops to 5%, the projection for the same period falls drastically to around 400,000 cases <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This highlights that proactive measures can significantly mitigate potential outcomes <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.