---
title: Impact of human behavior on epidemic spread
videoId: gxAaO2rsdIs
---

From: [[3blue1brown]] <br/> 

This article explores various simulations modeling the spread of an epidemic, drawing insights from interactive articles by Harry Stevens (Washington Post) and Kevin Simler (Melting Asphalt) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The simulations aim to answer questions about the effectiveness of different human behaviors and interventions, such as social distancing, isolation, and travel restrictions, on disease transmission <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## How the Models Work: The [[sir_model_for_epidemic_simulation | SIR Model]]

Each simulation is based on an [[sir_model_for_epidemic_simulation | SIR model]], which categorizes a population into three groups:
*   **S**usceptible: Individuals who can contract the disease <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **I**nfectious: Individuals who currently have the disease and can spread it <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **R**ecovered: Individuals who have recovered and are immune, or have died, thus no longer able to spread the disease (sometimes referred to as "Removed") <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

The models use physical proximity as a proxy for disease transmission, where a susceptible person within a certain infection radius of an infectious person has a probability of contracting the disease per unit of time <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. After a certain period, infectious people recover or are removed from the infectious pool <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

It's important to note that these are "toy models" with tiny populations, simplifying the complexities of real-world epidemiology <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Initial Observations on Spread Parameters

In baseline simulations where individuals wander randomly, the infection spreads quickly, infecting almost everyone <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Impact of Infection Radius
Doubling the infection radius (representing more interactions or a more socially engaged society) drastically accelerates the spread, leading to a simultaneous infection of the majority of the population in a short time <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This means a four-fold increase in the number of people within the infection radius <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.

### Impact of Infection Probability (Hygiene)
Halving the probability of infection (e.g., through better hand washing, cough protection, and less face touching) significantly "spreads out the curve," illustrating the large effect of hygiene changes on the rate of spread <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

> "The first of several key takeaways here that I'd like you to tuck away in your mind is just how sensitive this growth can be to each parameter in our control." <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>

Small changes in daily habits, such as multiplying interactions or halving infection probability, have huge implications for the pace of spread <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The goal is to reduce the total number of deaths, which can be increased if the peak of the infection curve is too high, overwhelming healthcare resources <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## The [[role_of_community_structure_in_disease_spread | Role of Community Structure]]

### Central Locations
Introducing a central location (like a grocery store or school) that people regularly visit and return from dramatically increases the spread <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Even when accounting for less intimate interactions at such locations by halving the infection probability, the effect of a central market remains dramatic <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

### Separate Communities with Transit
Modeling separate communities with transit between them (e.g., a 2% daily chance of travel to another community's center) shows how infection can spread between regions <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. In larger cities, urban centers act as concentrated hubs, and infection quickly hits all centers before slowly spreading to the edges of each community <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

## Actions to Stop Spread

### [[importance_of_early_testing_and_isolation_in_controlling_an_epidemic | Identifying and Isolating Cases]]
The most effective action is to identify and isolate infectious individuals through good testing and quick responsiveness <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. This can halt an epidemic entirely <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

#### Imperfections in Isolation
If a percentage of infected individuals are not quarantined (e.g., 20% due to asymptomatic cases), the peak number of simultaneous cases may only be slightly higher, but there is a very low, long tail, resulting in about twice as many total cases and taking much longer to stamp out <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

In multi-community settings, a 20% slip-through rate for infectious cases still flattens the curve, but results in a much thicker tail and over half the population getting infected <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. If only 50% of infectious cases are isolated, the situation is only marginally better than doing nothing at all, as many agents continue to spread the disease <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

> "A second key takeaway here is that changes in how many people slip through the tests can cause disproportionately large changes to the total number of people infected." <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>

#### Lethality and Transmissibility
Paradoxically, highly lethal diseases can be less globally dangerous if they kill their hosts quickly or cause severe symptoms that lead to rapid isolation, preventing widespread transmission (e.g., SARS in 2002) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>, <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>, <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. The most dangerous viruses are those that spread unnoticed (asymptomatically) before becoming lethal <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

#### Early Treatment
Early antiviral therapeutics that quickly move people out of the infectious category have the same beneficial effect on the model as isolating cases <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

### [[effectiveness_of_social_distancing | Social Distancing]]
Introducing a "social distance factor" (a repulsive force between individuals) can significantly impact spread <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

#### Participation Rates
*   **100% participation**: The disease quickly disappears <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>, <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Partial participation (90%, 70%, 50%)**: While [[effectiveness_of_social_distancing | social distancing]] definitely flattens the curve, even a small percentage of the population not adhering (e.g., 10%) can prolong the spread significantly, leading to a similar ultimate number of cases as lower participation rates, just over a longer period <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>, <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

> "Social distancing absolutely works to flatten the curve, but even small imperfections prolong the spread for a while." <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>

#### Impact with Central Locations
If [[effectiveness_of_social_distancing | social distancing]] is implemented but people continue to visit central locations, the effect of social distancing is largely defeated in terms of the total number of cases, though the peak might be slightly lower <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. Reducing frequency of visits to central spots by a factor of 5 has a similar effect on the epidemic curve as cutting the probability of infection (through hygiene) by a factor of 2 <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>, <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. This highlights the substantial impact of improved hygiene.

### Limiting Travel Between Communities
Reducing travel rates between communities (e.g., by a factor of 4) can have varied results; in some runs, it makes no difference, while in others, some communities remain unscathed <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>, <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. This intervention is most effective when implemented early, but has limited effect once communities are already widely infected, and is not a robust solution on its own <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

## Quantifying Spread: The Reproductive Number (R)

The **effective reproductive number (R)** is the average number of people one infected person infects while they have the disease <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. **R-naught (R₀)**, the basic reproductive number, is the value of R in a fully susceptible population at the very beginning of an outbreak <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

*   **Default simulation**: R is around 2.2 at its peak before falling as the population becomes saturated <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.
*   **Doubled infection radius**: R can be as high as 8 <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **Halved infection probability**: R hovers around 1.3 to 1.7 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

An infection is considered an epidemic when R is greater than 1, meaning it is growing [[exponential_growth_and_decay | exponentially]] <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. When R holds steady around 1, a disease is endemic <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. Less than 1 means it's on the decline <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

For comparison:
*   [[covid19_pandemic_analysis | COVID-19]]: R-naught estimated a little above 2 <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
*   1918 Spanish Flu: Mean R-naught estimate around 2 <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   Seasonal Flu: Around 1.3 <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

In simulations with central locations, R0 can jump as high as 5.8, highlighting the amplifying effect of such gathering spots <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

## Conclusion and Key Takeaways

Combining interventions like [[effectiveness_of_social_distancing | social distancing]], restricted travel to central locations, and lower infection rates (hygiene) is very effective <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

However, the most desirable outcome is achieved through consistent [[importance_of_early_testing_and_isolation_in_controlling_an_epidemic | identification and isolation of cases]] <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. Real-world epidemiology adds sophistication with tactics like contact tracing, which involves isolating not only known cases but also everyone who has been in contact with them <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

While [[effectiveness_of_social_distancing | social distancing]] saves lives when needed, the uncomfortable truth is that if interventions are lifted while the disease still exists without mechanisms to contain cases, second waves will occur <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>, <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

A deeper appreciation emerges for the value of early widespread testing, the ability to isolate cases, and therapeutics <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. Living in a connected world with widespread travel and urban centers presents an uphill battle against disease spread, but the rapid spread of ideas also allows for the development of systems and technologies to nip outbreaks in the bud <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.