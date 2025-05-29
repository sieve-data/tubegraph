---
title: Impact of human behavior on epidemic growth
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

While [[understanding_exponential_growth|exponential growth]] is a concept familiar to many, human intuition often struggles to fully grasp its implications <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Numbers that seem small can suddenly become very large, even if the overall trend consistently follows an exponential pattern <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Viruses are a textbook example of [[applications_of_exponential_growth_in_natural_phenomena|exponential growth]] because new cases arise from existing cases <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## How Epidemics Grow

[[understanding_exponential_growth|Exponential growth]] means that the number of cases from one day to the next involves multiplying by a constant factor <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For instance, in data related to COVID-19, the number of cases tended to multiply by approximately 1.15 to 1.25 of the previous day's cases <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

The mechanism behind this growth can be broken down:
*   If `n` is the number of cases on a given day <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   Each infected individual is exposed to, on average, `e` people daily <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Each exposure has a probability `p` of becoming a new infection <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

Therefore, the number of new cases daily is `e` (exposure) multiplied by `p` (probability) multiplied by `n` (existing cases) <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The fact that `n` itself is a factor in its own change causes the rapid acceleration characteristic of [[understanding_exponential_growth|exponential growth]] <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Impact of Human Behavior

For [[exponential_growth_and_decay|exponential growth]] to slow down, either the exposure (`E`) or the probability of infection (`P`) must decrease <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This is where human behavior plays a critical role.

### Reducing Exposure (E)
The amount of exposure (`E`) can decrease when people reduce gathering and traveling <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. [[impact_of_social_distancing_and_hygiene_on_disease_spread|Social distancing]] measures limit the opportunities for infected individuals to come into contact with susceptible people, thus reducing the number of exposures `e` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Reducing Infection Probability (P)
The infection rate (`P`) can go down when people improve their hygiene, such as washing hands more frequently <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. Good hygiene practices reduce the likelihood of transmission during an exposure <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

### The Logistic Curve and Inflection Point
True [[understanding_exponential_growth|exponentials]] rarely exist indefinitely in the real world; every exponential growth phase is the beginning of a logistic curve <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. A logistic curve is initially indistinguishable from an exponential but eventually levels out as it approaches a total population size or saturation point <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

The point where the logistic curve transitions from curving upward to curving downward is called the **inflection point** <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. At this point, the number of new cases each day stops increasing and either stays constant or begins to decrease <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

One metric often followed in [[mathematical_modeling_of_epidemics|epidemic simulations]] is the **growth factor**, defined as the ratio of new cases on one day to new cases on the previous day <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. During the exponential phase, this factor remains consistently above one <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. When the growth factor approaches one, it indicates that the inflection point has been reached <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### Sensitivity to Small Changes
A key [[understanding_exponential_growth|counterintuitive aspect of exponential growth]] is its extreme sensitivity to the constant multiplier <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Even a small reduction in the growth rate due to changes in human behavior can lead to dramatically different outcomes:

*   If the daily growth rate is 15%, a starting point of 21,000 cases could lead to over 100 million cases in 61 days <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   However, if this rate drops to 5% due to less exposure and infection, the projection for the same period drops significantly to around 400,000 cases <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

This highlights that if people are sufficiently worried and take action, there is significantly less to worry about <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Conversely, a lack of concern and action can lead to far more severe outcomes <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.