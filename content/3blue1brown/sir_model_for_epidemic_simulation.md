---
title: SIR model for epidemic simulation
videoId: gxAaO2rsdIs
---

From: [[3blue1brown]] <br/> 

This article explores various simulations that [[mathematical_modeling_of_epidemics | model how an epidemic spreads]] using an [[SIR model for epidemic simulation | SIR model]] to understand the dynamics of disease transmission and the impact of different interventions <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Understanding the SIR Model

Each simulation presented uses an SIR model, which categorizes the population into three groups <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>:
*   **S - Susceptible**: Individuals who are vulnerable to contracting the disease <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **I - Infectious**: Individuals who currently have the disease and can spread it <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **R - Recovered/Removed**: Individuals who have recovered from the infection and are now immune, or those who have died and can no longer spread the disease <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Simulation Mechanics
The model simulates infection based on physical proximity <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. A susceptible person within a certain "infection radius" of an infectious person for a unit of time has a probability of contracting the disease <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This proximity represents real-world interactions like shaking hands, touching surfaces, or sneezing <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. After a period, an infectious person will recover and become unable to spread the disease <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Limitations
These simulations are "toy models" with tiny populations, and they inherently simplify the complexities of real people and larger populations <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The creator emphasizes that direct generalization of these lessons without deeper consideration is not advised, as they are not an epidemiologist <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. However, they serve as a healthy way to engage with scientific and quantitative thinking in a limited fashion <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Basic Simulation Scenarios

### Random Walk
Initially, individuals wander randomly through the simulated city <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. In this default scenario, almost everyone becomes infected relatively quickly <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Impact of Parameters
The spread of the epidemic is highly sensitive to changes in key parameters <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Doubling Infection Radius**: Doubling the infection radius, which represents more interactions or a more socially engaged society, drastically accelerates the spread, leading to a majority of the population being infected simultaneously within a short period <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Halving Infection Probability**: Cutting the probability of infection in half (e.g., through better hygiene like hand washing or cough protection, and less face touching) significantly "spreads out the curve" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This illustrates that changes to hygiene have very large effects on the rate of spreading <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   **Key Takeaway**: The growth of an epidemic is very sensitive to parameters, and small changes in daily habits (e.g., multiplying interactions or halving infection probability) can have huge implications for the pace of spread <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Peak Infection and Mortality
A primary goal in managing an epidemic is to reduce the total number of deaths <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. If the peak of the infection curve is too high, meaning many people are sick at once, healthcare resources can become overwhelmed, which increases the mortality rate for severe diseases <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Adding Complexity to Models

### Central Locations
Introducing a common destination like a central market or a school, where people regularly visit and return from, dramatically accelerates the spread of the disease <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### Separate Communities and Travel
The model can also include multiple separate communities with transit between them, where individuals have a probability of traveling to another community's center daily <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>, <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Actions to Stop Spread

### [[importance_of_early_testing_and_isolation_in_controlling_an_epidemic | Identification and Isolation]]
This is presented as the most effective measure to halt an epidemic <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Effective Isolation**: If all infectious cases are identified and isolated (e.g., through good testing and quick responsiveness), the epidemic is completely halted <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>, <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Leaky Quarantine (Asymptomatic Cases)**: If a percentage of infected individuals (e.g., 20%) are not quarantined because they show no symptoms and are not tested, the epidemic is not halted. The peak number of simultaneous cases may be only slightly higher, but the disease takes much longer to stamp out, resulting in about twice as many total cases <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   In a multi-community setting, a 20% slip-through rate for infectious cases still flattens the curve but results in a much thicker tail and over half the population getting infected <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   If only 50% of infectious cases are isolated, the situation is only marginally better than doing nothing at all, due to the high number of agents still spreading the disease <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   **Key Takeaway**: Small changes in the number of people who slip through testing and isolation can cause disproportionately large changes to the total number of people infected <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Disease Characteristics and Spread
*   Highly lethal diseases that kill their host quickly, or those that show symptoms rapidly, tend to be less dangerous globally because they are easier to identify and contain <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>, <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   The most dangerous viruses are those that lay unnoticed and are spreadable, or worse, remain unnoticed and spreadable in everyone before becoming lethal <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   The SARS outbreak in 2002 was well-contained because most infectious individuals showed symptoms, making them easier to identify and isolate <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Early Treatment**: Antiviral therapeutics that move people out of the infectious category quickly have the same model effect as isolating cases <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### [[impact_of_public_health_measures_on_virus_spread | Social Distancing]]
Social distancing, modeled as a repulsive force between people, significantly reduces interactions <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>, <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Compliance Levels**:
    *   **100% compliance**: The disease quickly disappears <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    *   **Partial compliance (90%, 70%, 50%)**: Social distancing flattens the curve <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. However, even small imperfections (e.g., 10% non-compliance) prolong the spread, resulting in a similar total number of cases as lower compliance rates (e.g., 50%) <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
    *   **Key Takeaway**: Social distancing effectively flattens the curve, but even minor imperfections prolong the spread for a considerable time <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Reducing Travel Between Communities
Cutting the travel rate between communities can have a limited effect once the communities are already infected <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. Its effectiveness is greater the earlier it is implemented <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. In simulations with larger cities acting as urban hubs, infections quickly spread between these centers before slowly spreading to the edges of each community <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

## Quantifying Spread: The Reproductive Number

### Effective Reproductive Number (R)
R is the average number of people an infected person infects while they have the disease <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>, <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

### Basic Reproductive Number (R₀)
R₀ is the value of R in a fully susceptible population, representing the initial spread at the very beginning of an outbreak <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>, <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

### R Values in Simulations
*   **Default simulation**: R peaks around 2.2 <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.
*   **Doubled infection radius**: R can reach as high as 8 <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. This significant jump is expected, as doubling the radius increases the area (and thus potential contacts) by a factor of four <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
*   **Halved infection rate (hygiene)**: R hovers around 1.3 to 1.7 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

### Stages of Disease Spread
*   **Epidemic**: When R is greater than 1, the infection grows exponentially <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Endemic**: When R holds steady around 1 <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
*   **Decline**: When R is less than 1 <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Real-World Comparisons
*   **COVID-19**: R₀ is estimated to be a little above 2 <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
*   **1918 Spanish Flu**: Mean R₀ estimate was also around 2 <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Seasonal Flu**: R is much lower, around 1.3 <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

### R with Central Locations
When a central destination like a market or school is introduced, R₀ can jump as high as 5.8 <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. Even when conservatively cutting the infection probability in half (to account for less intimate interactions at such locations), R₀ is still significantly affected <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

## Combined Interventions

When social distancing is applied but people continue to visit a central location, the peak infection curve is lower than doing nothing, but the total number of cases remains high. The central location actively defeats the benefits of social distancing <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

Comparing the effectiveness of decreasing central location frequency (e.g., by a factor of 5) versus chopping the probability of infection (e.g., by another factor of 2 through hygiene) shows nearly identical results <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>, <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. This highlights the significant impact of hygiene, even if it's "easier said than done" <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

Applying a combination of social distancing, restricting central location visits, and lowering the infection rate all at once is highly effective <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. However, the most desirable outcome is consistently identifying and isolating cases <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. Even in scenarios with central markets, effective isolation can halt the epidemic without requiring people to change their routines <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Real epidemiology employs more sophisticated tactics like contact tracing, which involves isolating not only known cases but also everyone who has been in contact with them <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

## Conclusion

While [[impact_of_public_health_measures_on_virus_spread | social distancing]] saves lives when needed and cheating or continued central meetings disproportionately affect long-term cases <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>, the main takeaway is a deeper appreciation for effective disease control <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. If cases are not contained, a second wave can occur as soon as people return to normal life <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. The value of early widespread testing, the ability to isolate cases, and therapeutics is often underestimated <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. Although global travel and urban centers make fighting disease an uphill battle, the rapid spread of ideas can also lead to systems and technologies that nip outbreaks in the bud <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. There is fundamental optimism in the ability to learn from mistakes <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.