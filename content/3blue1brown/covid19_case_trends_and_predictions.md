---
title: COVID19 case trends and predictions
videoId: Kas0tIxDvrg
---

From: [[3blue1brown]] <br/> 

Human intuition often struggles to comprehend [[challenges_in_understanding_model_predictions | exponential growth]] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, leading to surprise when small numbers rapidly become large, even if the underlying trend is consistent <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The recorded cases of COVID-19 provide a practical example to understand this phenomenon <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

## Understanding Exponential Growth

Exponential growth signifies that moving from one day to the next involves multiplying by a constant factor <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. For COVID-19 data, the number of cases each day was approximately 1.15 to 1.25 times the number of cases from the previous day <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

Viruses are a prime example of this type of growth because new cases are generated directly by existing cases <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. If 'n' is the number of cases on a given day, 'e' is the average number of people each infected individual is exposed to daily, and 'p' is the probability of an exposure leading to a new infection, then the number of new cases is `e * p * n` <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. The presence of 'n' as a factor in its own change causes rapid acceleration: as 'n' increases, the growth rate itself increases <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

### Visualizing Exponential Growth

When charting exponential growth, placing the y-axis on a logarithmic scale makes it appear as a straight line <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. On this scale, each fixed step represents multiplication by a certain factor, such as a power of 10 <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Analysis of COVID-19 data showed it took 20 days to go from 100 to 1,000 cases, and 13 days to reach 10,000 from there <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. A linear regression on this logarithmic scale suggested cases multiplied by 10 approximately every 16 days on average <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. The statistical fit for this exponential trend was "really freaking close" <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.

### Counter-Intuitive Implications

A country with 60 cases compared to one with 6,000 might seem to be 100 times better off <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. However, if numbers multiply by 10 every 16 days, the second country is merely about a month behind the first <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

If the trend observed on March 6th continued, it would project:
*   1 million cases in 30 days <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>
*   10 million cases in 47 days <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>
*   100 million cases in 64 days <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>
*   1 billion cases in 81 days <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>

## The Logistic Curve and Inflection Point

Pure [[mathematical_modeling_of_epidemics | exponential growth]] <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a> cannot continue indefinitely; it must eventually slow down <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. This occurs when factors 'E' (exposure) or 'P' (probability of infection) decrease <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. Even in a worst-case scenario where infected individuals randomly encounter the global population, eventually most people they encounter would already be sick, thus limiting new cases <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.

This saturation effect leads to a [[mathematical_modeling_of_epidemics | logistic curve]] <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. This curve is initially indistinguishable from an exponential but eventually levels out as it approaches the total population size <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>. The point where the curve shifts from accelerating upwards to decelerating downwards is called the **inflection point** <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. At this point, the number of new cases per day stops increasing and either remains constant or begins to decrease <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. True exponentials in the real world are always the beginning of a logistic curve <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

### The Growth Factor

The **growth factor** is the ratio between the number of new cases on one day and the new cases from the previous day <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   During the exponential phase, this factor remains consistently above one <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
*   When the growth factor approaches one, it indicates that the inflection point has been reached <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.

A growth factor of one means the total number of cases will likely cap out at about double the current number <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. However, a growth factor even subtly greater than one means the exponential phase is still active, implying orders of magnitude of growth are still possible <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

## Real-World Dynamics and Interventions

While a random shuffling model might suggest saturation when the entire population is infected, real-world scenarios involve people clustered in communities <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>. However, [[epidemic_simulations_and_sir_model | simulations]] <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a> show that even minimal travel between clusters results in similar growth patterns, creating a fractal effect where communities behave like individuals, leading to the same underlying exponential laws <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

Fortunately, population saturation is not the only way to reduce the 'E' and 'P' factors <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.
*   **Reduced Exposure (E)**: This can be achieved when people [[impact_of_social_distancing_and_hygiene_on_disease_spread | stop gathering and traveling]] <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
*   **Reduced Infection Rate (P)**: This can occur when people [[impact_of_social_distancing_and_hygiene_on_disease_spread | wash their hands more]] <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.

### Sensitivity to Growth Rate

A key [[challenges_in_understanding_model_predictions | counter-intuitive aspect]] <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a> of exponential growth is its extreme sensitivity to the constant multiplication factor <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. For example, starting with 21,000 cases and a 15% daily growth rate would lead to over 100 million cases in 61 days <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. However, if this rate drops to 5% due to reduced exposure and infection, the projection for the same period plummets to around 400,000 cases <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. This highlights the profound [[impact_of_human_behavior_on_epidemic_growth | impact of human behavior]] <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>: if people are sufficiently concerned and take action, there is significantly less to worry about; conversely, a lack of concern can lead to substantial problems <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.