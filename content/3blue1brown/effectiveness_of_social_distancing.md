---
title: Effectiveness of social distancing
videoId: gxAaO2rsdIs
---

From: [[3blue1brown]] <br/> 

Simulations model how an epidemic spreads, building upon existing interactive articles from the Washington Post and Melting Asphalt <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. These models explore various scenarios, including the impact of people staying away from each other, occasional visits to central locations, and the effectiveness of identifying and isolating cases <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## How the Models Work: The [[sir_model_for_epidemic_simulation | SIR Model]]

Each simulation is based on an [[sir_model_for_epidemic_simulation | SIR model]], which categorizes a population into three groups:
*   **Susceptible (S)**: Those who can get the disease <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Infectious (I)**: Those currently carrying and spreading the disease <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Recovered (R)**: Those who have recovered and are immune, or who have died, and can no longer spread the disease <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The 'R' can also generically stand for "removed" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

In these simulations, physical proximity is a stand-in for interactions that spread disease, such as shaking hands or touching surfaces <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Susceptible individuals within a certain infection radius of an infectious person have a probability of contracting the disease per unit of time <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. After a period, infectious individuals recover or are removed <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

> [!CAUTION] Toy Models
> These are toy models with small populations, which inherently simplify the complexities of real people and larger populations. The creator, not an epidemiologist, advises caution when generalizing these lessons without deeper consideration <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, engaging with these models can be a healthy way to explore [[mathematical_modeling_of_epidemics | quantitative aspects of epidemics]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Initial Spread Dynamics

In a basic scenario where individuals wander randomly, the infection spreads quickly, leading to almost everyone getting infected <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

Modifying parameters significantly alters the spread:
*   **Doubling the infection radius**: This rapidly increases the number of simultaneous infections, as it represents more interactions or a more socially engaged society <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The effective reproductive number (R) can jump from around 2.2 to as high as 8 <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **Halving the infection probability**: This simulates improved hygiene (e.g., better hand washing, cough protection, less face touching) <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. It significantly spreads out the infection curve, illustrating the large [[impact_of_human_behavior_on_epidemic_spread | effect of hygiene]] on the rate of spread <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. R hovers around 1.3 to 1.7 in this scenario <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

The **sensitivity of growth to controllable parameters** is a key takeaway; even small changes in daily habits can have huge implications for the pace of spread <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. A high peak in the infection curve can overwhelm healthcare resources, increasing the mortality rate <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Introducing Social Distancing

Social distancing is modeled as a repulsive force between individuals, causing them to glow yellow when they are too close to neighbors <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. This makes interactions much rarer <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

Simulations show the [[impact_of_public_health_measures_on_virus_spread | effects of social distancing]] at different population adherence levels:
*   **100% adherence**: The disease quickly goes away entirely <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Partial adherence (90%, 70%, 50%)**: In all cases, social distancing flattens the curve <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. However, even with 90% adherence, a small percentage of people not participating can keep the "fire slowly burning for a long time," leading to a significant number of total cases (about half the population infected for 70% and 90% adherence) <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

> [!NOTE] Key Takeaway
> [[impact_of_public_health_measures_on_virus_spread | Social distancing]] absolutely works to flatten the curve, but even small imperfections can prolong the spread for a significant period <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Social Distancing with Central Locations

Introducing a central location, like a market or school, that people regularly visit dramatically increases the basic reproductive number (R0) to as high as 5.8, even when the probability of infection per day is cut in half <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. This highlights the [[role_of_community_structure_in_disease_spread | impact of common gathering spots]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

When social distancing is implemented but people continue to visit the central location, the peak of the infection curve is only slightly lower than doing nothing <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. Keeping the central location active largely defeats the positive effects of otherwise social distancing <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

Comparing strategies:
*   Decreasing the frequency of visits to the central spot (e.g., by a factor of 5) <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
*   Chopping the probability of infection (e.g., by a factor of 2, through improved hygiene) <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

Surprisingly, these two different approaches produce nearly identical results in the simulations, indicating that enhanced hygiene can be as effective as drastically altering daily routines <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. A combination of social distancing, restricted central location visits, and lower infection rates is very effective <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

## Broader Implications and Takeaways

While [[impact_of_public_health_measures_on_virus_spread | social distancing]] is crucial and saves lives when needed, the uncomfortable truth is that without measures to contain cases, a second wave can occur once people return to normal life <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. The most effective strategy is the consistent [[importance_of_early_testing_and_isolation_in_controlling_an_epidemic | identification and isolation of cases]] <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, even in scenarios with central gathering spots <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. This can include contact tracing <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

The most dangerous viruses are those that spread unnoticed due to asymptomatic carriers or a delay in symptoms <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. In contrast, diseases that cause immediate, obvious symptoms (like SARS in 2002) are easier to identify and contain <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Early treatment with antivirals, by quickly moving people out of the infectious category, has a similar effect to isolating cases <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

The ultimate takeaway from these simulations is a deeper appreciation for effective disease control, especially the value of early widespread testing, the ability to isolate cases, and therapeutics <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. Despite the challenges posed by global travel and urban centers, human connectivity also allows for the rapid spread of ideas and technologies to contain outbreaks <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.