---
title: Role of community structure in disease spread
videoId: gxAaO2rsdIs
---

From: [[3blue1brown]] <br/> 

Simulations modeling epidemic spread highlight the significant [[impact_of_human_behavior_on_epidemic_spread | impact of human behavior]] and community structure on disease transmission <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. These [[mathematical_modeling_of_epidemics | mathematical modeling of epidemics]] explore questions regarding the effect of central locations, inter-community travel, and human actions like isolation and [[effectiveness_of_social_distancing | social distancing]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Modeling Approach

The simulations are based on the [[sir_model_for_epidemic_simulation | SIR model for epidemic simulation]], which categorizes the population into three groups: Susceptible, Infectious, and Recovered (or Removed) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Physical proximity serves as a proxy for close interactions like shaking hands or sneezing <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It is important to note that these are toy models with small populations, which simplifies the complexities of real-world scenarios <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Impact of Central Locations

In models where individuals occasionally visit a central location, such as a grocery store or a school, and then return home, the disease spreads dramatically <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The basic reproductive number (R0) can jump as high as 5.8 with such a shared destination <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. Even when the probability of infection per day is conservatively cut in half (e.g., due to better hygiene), the effect of a central market remains dramatic <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>, <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

If [[effectiveness_of_social_distancing | social distancing]] measures are implemented but people continue to frequent a central location, the peak of the infection curve may be slightly lower than doing nothing <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. However, in terms of the total number of cases, maintaining an active central location largely defeats the positive effects of otherwise [[effectiveness_of_social_distancing | social distancing]] <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>, <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

### Mitigating Central Location Impact
Reducing the frequency of visits to a central spot by a factor of five has a similar effect on overall cases as chopping the probability of infection in half (e.g., through rigorous hand washing and reduced face touching) <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>, <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. This suggests that good hygiene can be as impactful as significantly altering daily routines <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. Combining [[effectiveness_of_social_distancing | social distancing]], restricted central location visits, and lower infection rates proves very effective <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.

## Impact of Inter-Community Travel

Introducing travel between separate communities, where individuals have a probability of visiting another community's center each day, also affects spread <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

Reducing inter-community travel by a factor of four after a certain threshold of cases is reached has a limited effect once communities are already infected <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>, <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>, <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. While earlier intervention is more effective, reducing contact between communities is not a robust standalone solution <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>, <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### Urban Hubs
When simulations are run with larger cities that include concentrated urban hubs, the infection quickly spreads to all urban centers as soon as one is hit <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>, <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. After infecting the centers, it then slowly spreads to the edges of each community <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

## Role of Isolation in Community Settings

The most effective measure to stop an epidemic, even in settings with many communities and transit between them, is to identify and isolate infectious individuals through good testing and quick responsiveness <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

However, even a small percentage of cases slipping through isolation measures can have significant consequences:
*   **20% cases slip through**: The peak number of simultaneous cases is only slightly higher, but there is a very long tail, taking much longer to eliminate the disease and resulting in about twice as many total cases <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **50% cases slip through**: This scenario is only marginally better than doing nothing at all, as a large number of agents continue to spread the disease <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

> [!key takeaways] Disproportionate Impact of Leaky Isolation
> Changes in how many people slip through testing and isolation processes can cause disproportionately large changes to the total number of people infected <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Even with central markets that unchecked lead to large outbreaks, effective identification and [[importance_of_early_testing_and_isolation_in_controlling_an_epidemic | isolation of cases]] can halt the epidemic without the need for [[effectiveness_of_social_distancing | social distancing]] or halting travel to central spots <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>, <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>. Advanced epidemiology includes tactics like contact tracing, which involves identifying and isolating contacts of known cases <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

## Overall Conclusions

While [[effectiveness_of_social_distancing | social distancing]] can save lives, especially when needed, any "cheating" or continued regular meetings at central locations can disproportionately affect the long-term number of cases <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>, <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

> [!caution] Risk of Second Waves
> If nothing is in place to contain cases once people resume normal life, a second wave of infection is likely to occur <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

Living in a world with widespread travel and vibrant urban centers presents an uphill battle against disease spread <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. However, this same connectedness allows for rapid spread of ideas, leading to systems and technologies that can [[importance_of_early_testing_and_isolation_in_controlling_an_epidemic | nip outbreaks in the bud]] <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>. This highlights the "inordinate value of early widespread testing and the ability to isolate cases," along with therapeutics <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.