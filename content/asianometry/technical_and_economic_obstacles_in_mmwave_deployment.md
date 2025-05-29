---
title: Technical and economic obstacles in mmWave deployment
videoId: cLEfKpsSAEU
---

From: [[asianometry]] <br/> 

[[standards_and_strategic_evolution_of_5G_networks | 5G]] marked a significant wireless technology transition, with [[millimeterwave_5g_challenges_and_prospects | Millimeter-Wave]] (mmWave) promising immense bandwidth and super-fast speeds <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, a few years into the [[standards_and_strategic_evolution_of_5G_networks | 5G]] rollout, difficult technical and economic [[challenges_in_the_semiconductor_industry | challenges]] remain for this fascinating technology <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. [[radio_frequency_integrated_circuits_and_their_role_in_5G | Radio Frequency Integrated Circuits]] (RFICs) are central to mmWave deployment <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Background: The Need for Millimeter Wave

Previous wireless generations, from 1G through 4G, primarily utilized frequency bands below 7.125 gigahertz <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. These "neighborhoods" became very crowded, with cell operators typically having only about 200 megahertz of spectrum <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This limited capacity prompted engineers to explore new approaches for [[standards_and_strategic_evolution_of_5G_networks | 5G]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

In 2011, Zhouyue Pi and Farooq Khan from Samsung Electronics suggested entering the largely unexplored mmWave regions, pointing to bands in the 70/80/90 gigahertz range <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. These are called millimeter wave bands because their wavelengths are in the 1-10 millimeter range <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The FCC opened these bands in 2003 for new economic development; previously, they were used for military radars, satellite communications, or cellular back-haul (point-to-point connections with fixed antennas) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

After Samsung's paper, research in 2014 from NYU and UT Austin demonstrated the technical feasibility of bringing mmWave to consumer wireless applications <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Consequently, [[standards_and_strategic_evolution_of_5G_networks | 5G]] gained support for a set of mmWave bands in the 24.25 to 52.6 gigahertz range <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Higher carrier frequencies, like those of mmWave, allow for greater bandwidth, meaning more data capacity <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## Technical Obstacles in mmWave Deployment

### Path Loss and Attenuation
A significant obstacle for mmWave is "path loss," the dilution of a wave's power density as it travels outwards and its surface area expands <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This phenomenon, along with other factors like rain and object obstruction, leads to "attenuation" or the gradual reduction of signal strength <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. High-frequency waves generally travel less effectively than lower-frequency ones; a shift from 3 gigahertz to 30 gigahertz spectrum can result in path loss that is 100 times worse <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

While smaller mmWave antennas can be used due to shorter wavelengths, allowing for arrays that generate directional beams to counteract path loss <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>, significant power amplification is still required for the signal to reach cell towers <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

### RFIC Design: Power Amplifier Challenges
The power amplifier within an [[radio_frequency_integrated_circuits_and_their_role_in_5G | RFIC]] is the most power-hungry and difficult module to design <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Designers must achieve high output power to reach the tower while maintaining good efficiency (to conserve battery and manage heat) and linearity (signal quality) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

### Line of Sight Limitations
One of the most widely recognized issues with mmWave is its inability to easily penetrate certain objects <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>:
*   **Buildings** <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>
*   **Foliage** <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>
*   **Human body** <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>
*   **Bricks, trees, and outdoor tinted glass** are particularly effective at attenuating mmWave signals <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   Even facing away from the base station can drastically hurt performance <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

While heavy rainfall does not appear to be a significant factor <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>, the general rule of thumb is that mmWave works best in "line of sight" situations within extremely busy areas like sports arenas, malls, and airports <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Densification Requirements
Due to line-of-sight and propagation issues, mmWave deployment requires a "densification" strategy <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Instead of large macro-cells with ranges of several kilometers (common in 1G-4G), telecoms need to install many small cells, perhaps as little as 50-100 meters apart <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

This presents several [[economic_challenges_in_the_mems_industry | economic challenges]]:
*   **Site Acquisition:** Acquiring numerous 5G sites is challenging and time-consuming <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **Infrastructure:** Sites must have 24/7 power for emergency services and a back-haul connection to the larger network <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   **Aesthetics and Permitting:** Sites must be aesthetically inconspicuous, and environmental permitting adds complexity <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Telecoms have even considered leveraging reflectors on billboards or glass to bounce mmWave signals to save money <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## Deployment and Economic Obstacles

The transition from LTE to [[standards_and_strategic_evolution_of_5G_networks | 5G]] has been highly complicated <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. While the [[standards_and_strategic_evolution_of_5G_networks | 5G]] New Radio standard supports low, mid, and high bands (mmWave) <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>, deploying mmWave (high band) is the most difficult due to its propagation and densification [[challenges_in_the_semiconductor_industry | challenges]] <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Telecoms have two deployment options:
*   **Standalone (SA):** A completely new [[standards_and_strategic_evolution_of_5G_networks | 5G]] network with [[standards_and_strategic_evolution_of_5G_networks | 5G]] base stations and a [[standards_and_strategic_evolution_of_5G_networks | 5G]] core network <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Non-Standalone (NSA):** A middle ground where [[standards_and_strategic_evolution_of_5G_networks | 5G]] New Radio connects to a 4G LTE core <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. This offers some speed improvements but is not as significant, especially at lower bands <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

### US Rollout Experiences
In the United States, Verizon and AT&T were early adopters of mmWave [[standards_and_strategic_evolution_of_5G_networks | 5G]] because their low and mid-band frequencies were already occupied by legacy 3G and 4G networks <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. Verizon began deploying Non-Standalone [[standards_and_strategic_evolution_of_5G_networks | 5G]] in 2018 for both mobile and fixed wireless access <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. While fixed wireless access showed promise, the mobile service part of the mmWave rollout faced significant hurdles <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

### Market Response and Strategic Shift
Several factors contributed to the limited success of mmWave for mobile services:
*   **Customer Apathy:** Most customers were unwilling to pay a large premium for faster rates, especially as the smartphone ecosystem matured <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
*   **Confusing Branding:** The super-confusing branding of what constituted "5G" did not help, leading to customer confusion about their connection type <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Low Traffic:** Analysts had expected mmWave to carry 5% of mobile traffic in 2021, and Verizon predicted 50% of urban traffic would be on mmWave over time <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. However, in 2021, only about 2.9% of mobile traffic in US urban areas was consumed on mmWave [[standards_and_strategic_evolution_of_5G_networks | 5G]] <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Connection Stability:** Studies showed that slight movements could cause phones to fall back onto 4G LTE after connecting to mmWave <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

Despite arguments from Verizon and Qualcomm that shifting any data traffic to mmWave would alleviate pressure on existing 3G and 4G networks <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>, Wall Street was not satisfied, especially as T-Mobile focused on low and mid-band [[standards_and_strategic_evolution_of_5G_networks | 5G]] deployments <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This led Verizon and AT&T to adjust their strategies, investing heavily in 5G mid-band spectrum (e.g., C-band 3.7 gigahertz) in February 2021 <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Since then, they have focused on expanding their mid-band offerings, including their standalone [[standards_and_strategic_evolution_of_5G_networks | 5G]] networks <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

### Limited Device Support
Device support for mmWave has also been inconsistent. A few years into the rollout, only US iPhones support mmWave, and iPads have recently dropped support for it entirely <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

### Lack of Killer Applications
Many of the "internet of things" and "Industry 4.0" initiatives that [[standards_and_strategic_evolution_of_5G_networks | 5G]] was supposedly to be good for have not emerged, leading to a question of whether there is a "super-compelling, super-broad killer app" for mmWave <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. Consequently, the mmWave spectrum remains largely unused, and the FCC is exploring more creative solutions for its utilization <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.

### Global Adoption
Outside of the United States, most of the world has not widely adopted mmWave, with Japan being a notable exception due to its network setup for the 2020 Tokyo Olympics <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.

## Conclusion

While telecoms continue to expand mmWave for fixed wireless access in rural areas and high-density urban areas like airports and sports stadiums, where it works best <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>, its broader deployment for mobile services has faced significant hurdles. Technology continues to evolve, and telecoms are moving towards Standalone [[standards_and_strategic_evolution_of_5G_networks | 5G]] with ongoing improvements from companies like Qualcomm <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. However, whether mmWave will benefit significantly from this progression remains to be seen <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.