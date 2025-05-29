---
title: Impact of social distancing and hygiene on disease spread
videoId: gxAaO2rsdIs
---

From: [[3blue1brown]] <br/> 

Simulations can model how an epidemic spreads, building upon interactive articles by Harry Stevens in the Washington Post and Kevin Simler at Melting Asphalt <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. These models explore various scenarios, including the effect of people avoiding each other, occasional visits to central locations like grocery stores or schools, the ability to identify and isolate cases, asymptomatic spread, inter-community travel, and waning public adherence to precautions <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Model Setup

Each simulation represents an [[Epidemic simulations and SIR model | SIR model]], categorizing the population into three groups: susceptible (S), infectious (I), and recovered/removed (R) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

*   **Infection Mechanism**: A susceptible person within a certain "infection radius" of an infectious person has a probability of contracting the disease, representing physical proximity, handshakes, touching surfaces, or respiratory droplets <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Recovery/Removal**: After a period, infectious individuals recover and become immune, or die, thus no longer able to spread the disease. The "R" in SIR can also stand for "removed" to encompass both outcomes <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

It is important to note that these are "toy models" with small populations, simplifying the complexities of real people and larger populations. The author, not being an epidemiologist, advises hesitation in generalizing lessons without deeper consideration <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, engaging with these [[Mathematical modeling of epidemics | quantitative models]] can be a healthy alternative to dwelling on uncertainty <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Baseline Spread and Parameter Sensitivity

Initial simulations show a population meandering randomly, leading to almost everyone getting infected after a relatively short time <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

*   **Impact of Infection Radius**: Doubling the infection radius (representing more interactions or a more socially engaged society) drastically accelerates the spread, leading to the majority of the population being simultaneously infected quickly <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Impact of Infection Probability/Hygiene**: Halving the probability of infection (e.g., through better hand washing, cough protection, and less face touching) significantly "spreads out the curve" of cases over time, illustrating the large [[Impact of human behavior on epidemic growth | effects of hygiene on spreading rates]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

A key takeaway is the high sensitivity of epidemic growth to parameters within human control <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Small changes in daily habits, such as multiplying interactions or halving infection probability, have huge implications for the pace of spread <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The ultimate goal is to reduce total deaths, which involves flattening the infection curve to prevent healthcare resources from being overwhelmed and increasing the mortality rate <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Influence of Central Locations and Community Travel

The presence of a common central destination, such as a market or school, that people regularly visit dramatically accelerates disease spread compared to random wandering <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Simulations also include separate communities with transit between them, where individuals have a probability of traveling to another community's center daily <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

## Effectiveness of Isolation and Testing

The most effective measure is to identify and isolate infectious individuals, achieved through good testing and quick responsiveness <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

*   **Full Isolation**: In simulations, sending infected individuals to a separate location one day after infection completely halts the epidemic <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Leaky Quarantine (Asymptomatic Cases)**: If 20% of infected individuals are not quarantined (e.g., due to no symptoms or lack of testing), the peak number of simultaneous cases is only slightly higher, but the epidemic has a very long tail, taking much longer to stamp out and resulting in about twice as many total cases <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Reduced Isolation Effectiveness**: If only 50% of infectious cases are isolated, the situation is only marginally better than doing nothing at all, as too many agents remain to spread the disease <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

A second key takeaway is that small changes in the proportion of people who slip through testing or isolation can lead to disproportionately large changes in the total number of people infected <a class="yt>timestamp" data-t="00:09:00">[00:09:00]</a>. This highlights why diseases that kill hosts quickly (like highly lethal but easily identifiable ones) are globally less dangerous than those that remain unnoticed and spreadable among some or all infected individuals before becoming lethal <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. The SARS outbreak in 2002 was well-contained because most infectious individuals showed symptoms, making them easier to identify and isolate <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Similarly, early antiviral therapeutics that quickly move people out of the infectious category have the same beneficial effect as isolating cases <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Impact of Social Distancing

[[Impact of human behavior on epidemic growth | Social distancing]] can be modeled as a repulsive force between people, making interactions much rarer <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

*   **Varying Compliance**:
    *   **100% compliance**: The disease quickly disappears <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    *   **Partial compliance (90%, 70%, 50%)**: While widespread social distancing flattens the curve, even 10% of the population not adhering to it (e.g., in the 90% compliance scenario) can prolong the spread for a very long time, leading to a high ultimate number of cases <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. The run with 70% compliance and even 90% compliance resulted in little less than half the population ultimately getting infected, only slightly better than 50% compliance <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

The third key takeaway is that while [[Impact of human behavior on epidemic growth | social distancing]] absolutely works to flatten the curve, even small imperfections in adherence prolong the spread <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Reducing Travel Between Communities

Reducing the rate of travel between separate communities has a limited effect once those communities are already infected. Its effectiveness is greater the earlier it is implemented, but it is not a robust solution on its own <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. In simulations with larger cities, urban centers act as concentrated hubs, quickly spreading infection to all connected centers before it slowly reaches community edges <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

## Quantifying Spread: The Reproductive Number (R)

The effective reproductive number (R) is the average number of people an infected individual infects while they have the disease <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. R-naught (R0) is the basic reproductive number, which is R's value in a fully susceptible population at the very beginning of an outbreak <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

*   **Growth Phases**:
    *   R > 1: Infection grows exponentially (an [[Epidemic simulations and SIR model | epidemic]]) <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
    *   R ≈ 1: Disease is endemic <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
    *   R < 1: Disease is in decline <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

*   **R Values in Simulations**:
    *   Default simulation: R ~2.2 at peak growth <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
    *   Doubled infection radius: R as high as 8 <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
    *   Halved infection probability: R ~1.3 to 1.7 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
    *   With a central location: R0 jumps to 5.8 <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. If infection probability is halved in this scenario (e.g., due to more cautious behavior at the central location), R0 is also halved <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

*   **Real-World Comparisons**:
    *   [[COVID19 case trends and predictions | COVID-19]] R0: A little above 2 <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
    *   1918 Spanish Flu R0: Around 2 <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
    *   Seasonal Flu R0: Around 1.3 <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

Social distancing and travel restrictions cause R to drop quickly <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

## Combined Effects and Key Takeaways

When social distancing is applied but people still visit central locations, the peak of the infection curve is slightly lower than doing nothing, but the central location significantly defeats the overall [[Impact of human behavior on epidemic growth | effects of social distancing]] on the total number of cases <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

Comparing interventions:
*   Reducing central location frequency by a factor of 5.
*   Chopping the probability of infection by another factor of 2 (e.g., super extra cautious hygiene).

These two approaches yield nearly identical results, suggesting that hygiene (e.g., hand washing, not touching face) can be very impactful <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. Combining social distancing, restricting central location visits, and lowering infection rates simultaneously is very effective <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

However, the most desirable case remains the consistent ability to [[Effectiveness of quarantine and isolation | identify and isolate cases]] <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. Even in scenarios with central markets and potential for large outbreaks, effective identification and isolation can halt the epidemic without requiring people to social distance or stop their trips to central spots <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. Real epidemiology involves more sophisticated tactics like [[Importance of early testing and contact tracing | contact tracing]], isolating not only known cases but also their contacts <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

## Conclusion

[[Impact of human behavior on epidemic growth | Social distancing]] saves lives when needed. However, if people relax precautions or continue meeting at central locations, it disproportionately affects the long-term number of cases <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. The uncomfortable truth is that if no measures are in place to contain cases, even few in number, a second wave will occur once people return to normal lives <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.

These simulations highlight the immense value of proper [[Effectiveness of quarantine and isolation | disease control]], including early widespread testing, the ability to isolate cases, and therapeutics <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. "Pandemics that never were"—outbreaks swiftly found and contained—underscore the underestimated value of these preventative measures and the heroes behind them <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. While widespread travel and vibrant urban centers make fighting disease an uphill battle, the rapid spread of ideas allows for systems and technologies that can nip outbreaks in the bud <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.