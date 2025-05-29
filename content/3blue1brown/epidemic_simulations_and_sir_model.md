---
title: Epidemic simulations and SIR model
videoId: gxAaO2rsdIs
---

From: [[3blue1brown]] <br/> 

Simulations can model how an epidemic spreads, providing insights into various factors influencing disease transmission <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Notable interactive articles on this topic include one by Harry Stevens in the Washington Post and another by Kevin Simler at Melting Asphalt <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. These simulations explore questions such as the effect of occasional visits to central locations, the impact of isolating cases, the role of asymptomatic carriers, the influence of travel between communities, and the consequences of people tiring of prevention measures <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## The SIR Model

Each simulation typically represents an [[mathematical_modeling_of_epidemics | SIR model]] <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. In this model, the population is divided into three categories:
*   **Susceptible (S)**: Individuals who can contract the disease <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Infectious (I)**: Individuals who currently have and can spread the disease <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Recovered (R)**: Individuals who have recovered from the infection and are immune, or have died (sometimes referred to as "Removed" for a generic term) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

In these models, a susceptible person within a certain "infection radius" of an infectious person has a probability of contracting the disease, representing physical proximity and interactions like shaking hands or sneezing <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. After a period, an infectious person either recovers or dies, ceasing to spread the disease <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Model Limitations and Purpose

These simulations are "toy models" with tiny populations, simplifying the complexities of real people and larger populations <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The creator emphasizes that they are not an epidemiologist and advises hesitation in generalizing lessons without deeper consideration <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Nevertheless, these models are valuable for engaging scientific curiosity, experimenting with quantitative concepts, and providing an alternative to dwelling on headlines and uncertainty <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Basic Simulation Examples

Initially, individuals in the simulation wander randomly, and infection follows the SIR model rules <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

*   **Default Run**: After a short time, most individuals become infected <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Doubling Infection Radius**: Doubling the infection radius (representing more interactions or a more socially engaged society) drastically accelerates the spread, leading to a majority of the population being infected simultaneously within a short period <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Halving Infection Probability**: Cutting the probability of infection in half (representing better hand washing, cough protection, or less face touching) significantly spreads out the infection curve, highlighting the large effect of hygiene changes on spread rate <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

> [!NOTE] Key Takeaway 1
> The growth of an epidemic is highly sensitive to small changes in parameters <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Small adjustments to daily habits, like reducing interactions or cutting infection probability, can have huge implications for the pace of spread <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

The ultimate goal in managing an epidemic is to reduce the total number of deaths <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. If the peak of the infection curve is too high, healthcare resources become overwhelmed, which increases the mortality rate <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Introducing Complexity

### [[Role of central locations in spreading disease | Central Locations]]

Most people do not wander randomly; they often visit common destinations like grocery stores or schools <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Introducing a central spot that people regularly visit significantly accelerates the spread of the disease <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### Multiple Communities and Travel

Another feature that can be included is separate communities with transit between them, where individuals have a probability of traveling to another community's center <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

## Actions to Stop the Spread

### Identification and Isolation/Quarantine

By far, the most effective action is to identify and isolate infectious individuals through good testing and quick responsiveness <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Perfect Isolation**: This totally halts the epidemic <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Leaky Quarantine (20% slip through)**: If 20% of infected individuals are not quarantined (e.g., due to no symptoms), the peak number of simultaneous cases is only slightly higher, but a very long tail of cases results in about twice as many total infections <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Leaky Quarantine (50% isolated)**: If only 50% of infectious people are quarantined, the situation is only marginally better than doing nothing, as many agents continue to spread the disease <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

> [!NOTE] Key Takeaway 2
> Changes in how many infected people slip through tests can cause disproportionately large changes to the total number of people infected <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

The most lethal diseases can be less dangerous globally if they kill their host quickly or show obvious symptoms, making isolation easier <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. For example, the SARS outbreak in 2002 was well-contained because most infectious individuals showed symptoms <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Conversely, the most dangerous viruses are those that spread unnoticed (asymptomatic carriers) before becoming lethal <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Early treatment with antivirals has a similar effect to isolation, moving people out of the infectious category quickly <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### [[Impact of social distancing and hygiene on disease spread | Social Distancing]]

[[Impact of social distancing and hygiene on disease spread | Social distancing]] involves people actively trying to avoid each other, represented by a repulsive force between individuals <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Even with imperfections, where individuals occasionally get close enough to infect, the interactions become much rarer <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

Simulations show:
*   **100% Social Distancing**: The disease quickly disappears <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Partial Social Distancing (90%, 70%, 50%)**: All levels flatten the curve. However, even with 90% compliance, the ultimate number of cases can be nearly as high as with 50% compliance, as a small percentage of non-compliant individuals can prolong the spread for a long time <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

> [!NOTE] Key Takeaway 3
> [[Impact of social distancing and hygiene on disease spread | Social distancing]] is effective in flattening the curve, but even small imperfections can significantly prolong the spread <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Travel Restrictions

Reducing contact between communities by cutting travel rates (e.g., from 2% to 0.5% chance of travel per day) has a limited effect once the communities are already infected <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. Its effectiveness is greater if implemented earlier, but it is not a robust solution on its own <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. In larger cities with concentrated urban hubs, infection can spread very quickly between these centers before slowly reaching the edges of each community <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

## Quantifying Spread: Reproductive Numbers (R & R₀)

The spread of a disease can be quantified using reproductive numbers:
*   **Effective Reproductive Number (R)**: The average number of people one infected person infects while they have the disease <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   **Basic Reproductive Number (R₀)**: The value of R in a fully susceptible population, typically at the very beginning of an outbreak <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

In the simulations, R is estimated by tracking current infectious individuals and averaging their total projected infections <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   **Default simulation**: R peaks around 2.2 <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   **Doubled infection radius**: R can reach as high as 8, due to approximately four times as many people being within the infection radius <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **Halved infection rate**: R hovers around 1.3 to 1.7 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

When R is greater than 1, the infection grows exponentially (an epidemic) <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. When R is around 1, the disease is endemic, and less than 1 means it is on the decline <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
For comparison, R₀ for [[COVID19 case trends and predictions | COVID-19]] is estimated to be slightly above 2, similar to the 1918 Spanish flu pandemic, while the seasonal flu is around 1.3 <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. [[Impact of social distancing and hygiene on disease spread | Social distancing]] and travel restrictions cause R to drop quickly <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

Introducing a [[Role of central locations in spreading disease | shared central location]] can cause R₀ to jump as high as 5.8 <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. Even with a halved probability of infection to account for less intense contact in such locations, the effect of a central market remains dramatic <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. Social distancing while maintaining central location visits still allows the central location to largely defeat the effects of otherwise social distancing <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Combined Strategies and Insights

Reducing the frequency of visits to a central spot (e.g., by a factor of 5) can have a similar effect on the infection curve as greatly increasing hygiene (cutting infection probability by a factor of 2) <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. This suggests that hygiene changes, though potentially harder to implement, can be highly effective <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. A combination of social distancing, restricted central location visits, and lower infection rates (hygiene) is highly effective <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

Despite the effectiveness of other measures, the most desirable outcome is consistently identifying and isolating cases <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. Even with [[Role of central locations in spreading disease | central locations]], effective isolation halts the epidemic without requiring other behavioral changes <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Real epidemiology also uses tactics like contact tracing to identify and isolate contacts of known cases <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

While [[Impact of social distancing and hygiene on disease spread | social distancing]] saves lives when needed, a key uncomfortable truth is that if nothing is in place to contain cases once people return to normal lives, a second wave can occur <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. The simulations highlight the immense value of early, widespread testing, the ability to isolate cases, and therapeutics <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. These efforts often go unappreciated because they prevent pandemics from materializing <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

Living in a connected world with widespread travel and urban centers makes fighting disease spread an uphill battle, but it also allows for rapid spread of ideas, leading to systems and technologies that can nip outbreaks in the bud <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.