---
title: Importance of early testing and isolation in controlling an epidemic
videoId: gxAaO2rsdIs
---

From: [[3blue1brown]] <br/> 

Simulations modeling how an [[mathematical_modeling_of_epidemics | epidemic]] spreads highlight the critical role of early detection and isolation in containment efforts <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. These simulations, drawing inspiration from interactive articles by Harry Stevens and Kevin Simler, explore various scenarios of disease transmission <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## The SIR Model Framework
The simulations are based on an [[sir_model_for_epidemic_simulation | SIR model for epidemic simulation]] <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This model categorizes a population into three groups:
*   **S**usceptible: Individuals who can contract the disease <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **I**nfectious: Individuals who have the disease and can spread it <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **R**ecovered: Individuals who have recovered from the infection and are immune, or have been removed (e.g., by death) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

In these models, susceptible individuals have a probability of contracting the disease if they are within a certain infection radius of an infectious person <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This physical proximity represents various forms of contact that facilitate spread <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. After a period, infectious individuals recover or are removed, ceasing to spread the disease <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

It's important to note that these are "toy models" with small populations and simplified complexities, not directly generalizable without deeper consideration <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. However, they allow for quantitative experimentation <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Direct Impact of Identification and Isolation
The most effective action in stopping an [[mathematical_modeling_of_epidemics | epidemic]] is to identify and isolate infectious individuals, such as through good testing and quick responsiveness <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

In simulations where infectious people are sent to a separate location one day after infection, the [[mathematical_modeling_of_epidemics | epidemic]] is totally halted <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This represents any real-world isolation method <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

### The Effect of Imperfect Isolation (Leaky Quarantine)
The effectiveness of isolation is significantly reduced if some cases slip through the process <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. For example, if 20% of infected individuals are not quarantined (e.g., due to asymptomatic presentation), the peak number of simultaneous cases is only slightly higher, but the epidemic develops a very low, long tail, taking much longer to stamp out and resulting in about twice as many total cases <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

In a setting with multiple [[role_of_community_structure_in_disease_spread | communities]] and transit between them, perfect isolation is still very effective <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. However, if 20% of infectious cases slip through, the "leaky quarantining" effort flattens the curve but results in a much thicker tail and over half the population getting infected <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. If only 50% of infectious cases are isolated, the situation is only barely better than doing nothing at all, as many agents are still out spreading the disease <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

> A key takeaway is that changes in how many people slip through tests can cause disproportionately large changes to the total number of people infected <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Stealthy Diseases and Treatment
The most dangerous viruses are those that can lay unnoticed and spreadable among a population, or remain unnoticed and spreadable in everyone before becoming lethal <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Highly lethal diseases, paradoxically, can be less dangerous globally because their severe symptoms make them easier to identify and isolate <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. The SARS outbreak in 2002 was well-contained largely because most infectious individuals showed symptoms, aiding identification and isolation <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

Similarly, early treatment with antiviral therapeutics that quickly move people out of the infectious category has the same beneficial effect on the model as isolating those cases <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

## Isolation vs. Other Measures
While [[effectiveness_of_social_distancing | social distancing]] definitely helps flatten the curve, small imperfections can prolong the spread <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. Similarly, reducing travel between [[role_of_community_structure_in_disease_spread | communities]] has a limited effect once communities are already infected <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

The simulations consistently show that the most desirable outcome is achieved when cases can be consistently identified and isolated <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. Even in scenarios with a central market that significantly accelerates spread (where R0 can jump as high as 5.8 <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>), effective isolation still halts the [[mathematical_modeling_of_epidemics | epidemic]] without requiring people to completely change their routines or stop visiting central locations <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. This contrasts with [[effectiveness_of_social_distancing | social distancing]], where continuing to visit a central location can "really defeat the effects of otherwise social distancing" <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

## Conclusion
The simulations underscore a profound appreciation for effective disease control <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. The "inordinate value of early widespread testing and the ability to isolate cases," along with therapeutics, cannot be underestimated <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. While [[effectiveness_of_social_distancing | social distancing]] is crucial when needed, it is a temporary measure <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. If cases are not contained, lifting such measures can lead to a second wave <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

Effective containment prevents "pandemics that never were," where novel pathogens are swiftly found and contained before spreading widely <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. Despite the challenges of global travel and urban centers in fighting disease spread, the rapid spread of ideas can lead to systems and technologies that "nip these outbreaks in the bud" <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.