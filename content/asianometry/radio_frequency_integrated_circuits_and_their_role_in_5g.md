---
title: Radio Frequency Integrated Circuits and their role in 5G
videoId: cLEfKpsSAEU
---

From: [[asianometry]] <br/> 

[[standards_and_strategic_evolution_of_5G_networks | 5G]] represents a significant transition in wireless technology <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. A key promise of this transition was immense bandwidth and super-fast speeds, primarily delivered through [[millimeterwave_5g_challenges_and_prospects | Millimeter-Wave (mmWave)]] technology <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, the rollout of [[millimeterwave_5g_challenges_and_prospects | 5G mmWave]] has faced [[technical_and_economic_obstacles_in_mmwave_deployment | difficult technical and economic challenges]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

Radio Frequency Integrated Circuits (RFICs) are complex components in this ecosystem <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This article explores RFICs and their integration into [[millimeterwave_5g_challenges_and_prospects | 5G mmWave deployment]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Fundamentals of Wireless Communication

A wave's `wavelength` is the distance it travels in a single cycle, measured in meters <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. `Frequency` is the number of cycles passing a given point, measured in hertz <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   A megahertz signifies a million cycles per second <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   A gigahertz signifies a billion cycles per second <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   A terahertz signifies a trillion cycles per second <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

Frequency and wavelength are inversely related: as frequencies increase, wavelengths decrease <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For example, gamma rays have high frequencies and wavelengths measured in picometers <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Countries allocate specific parts of the electromagnetic spectrum for various uses, such as radar, wireless communication, or WiFi <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The spectrum is inherently limited, posing a challenge for optimal utilization <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### The Evolution from 4G to 5G

The previous wireless generation, 4G, saw global telecoms converge on the LTE standard due to its superior data downlink speeds <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. LTE had to accommodate diverse frequency slices, ranging from 450 megahertz to 3.6 gigahertz <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, which complicated the development of a universal "world phone" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. A larger concern was the capacity constraints due to reliance on small frequency slices <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

1G through 4G systems consistently utilized frequency bands below 7.125 gigahertz <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Over time, these bands became very crowded <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Typically, a cell operator in a specific area only had about 200 megahertz of spectrum available, which proved insufficient <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## 5G Objectives and Spectrum Expansion

Engineers conceptualized [[standards_and_strategic_evolution_of_5G_networks | 5G]] to address these limitations <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Beyond handling more data traffic, primarily mobile video, known as Enhanced Mobile Broadband (eMBB) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, [[standards_and_strategic_evolution_of_5G_networks | 5G]] was designed to enable other communication types:
*   **Ultra Reliable Low Latency Networking (URLLC)**: For critical data requiring rapid and reliable delivery, such as self-driving cars avoiding collisions or wirelessly controlled robot arms, with signal delivery needed in under 10 milliseconds <a class="yt-timestamp" data-t="00:02:52">[00:03:11]</a>.
*   **Massive Machine Type Communications (mMTC)**: For numerous low-cost machines that transmit data infrequently over long periods, like sensors, actuators, and vending machines <a class="yt-timestamp" data-t="00:03:18">[00:03:28]</a>.

These varied objectives necessitated a more flexible [[standards_and_strategic_evolution_of_5G_networks | 5G standard]], particularly regarding its usable frequency bands <a class="yt-timestamp" data-t="00:03:46">[00:03:50]</a>. Significantly, [[standards_and_strategic_evolution_of_5G_networks | 5G]] opened up a completely new slice of the spectrum <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### [[millimeterwave_5g_challenges_and_prospects | Millimeter Wave]]

In 2011, Zhouyue Pi and Farooq Khan from Samsung Electronics authored an influential article in IEEE Communications magazine <a class="yt-timestamp" data-t="00:04:02">[00:04:07]</a>. They suggested exploring the largely uncharted [[millimeterwave_5g_challenges_and_prospects | mmWave]] regions, specifically pointing to bands in the 70/80/90 gigahertz range <a class="yt-timestamp" data-t="00:04:21">[00:04:26]</a>. These are termed [[millimeterwave_5g_challenges_and_prospects | millimeter wave]] bands because their wavelengths fall within the 1-10 millimeter range <a class="yt-timestamp" data-t="00:04:32">[00:04:37]</a>.

The FCC initially opened these bands for new economic development in 2003 <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Prior to that, the spectrum was primarily used for military radars, satellite communications, or cellular back-haul <a class="yt-timestamp" data-t="00:04:43">[00:04:46]</a>. These were typically point-to-point connections where large fixed antennas fired narrow [[millimeterwave_5g_challenges_and_prospects | mmWave]] beams at other fixed antennas several kilometers away <a class="yt-timestamp" data-t="00:04:50">[00:04:55]</a>. Such systems were susceptible to strong winds misaligning the beams, explaining why [[millimeterwave_5g_challenges_and_prospects | mmWave]] wasn't extensively used for consumer wireless <a class="yt-timestamp" data-t="00:05:01">[00:05:05]</a>.

Early consumer applications following the FCC decision included:
*   **Automotive radar**: The 77 gigahertz spectrum band was opened to aid advanced driver assistance systems in identifying dangerous situations <a class="yt-timestamp" data-t="00:05:12">[00:05:21]</a>.
*   **WiGig WiFi standard**: This standard, formed in 2009, uses a 60 gigahertz band, though its adoption has been limited <a class="yt-timestamp" data-t="00:05:28">[00:05:31]</a>.

After Samsung's paper, the concept gained momentum <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Research published in 2014 by NYU and UT Austin demonstrated the technical feasibility of bringing [[millimeterwave_5g_challenges_and_prospects | mmWave]] to consumer wireless applications <a class="yt-timestamp" data-t="00:05:45">[00:05:50]</a>. As a result, [[standards_and_strategic_evolution_of_5G_networks | 5G]] gained support for a set of bands ranging from 24.25 to 52.6 gigahertz, in addition to more traditional sub-7 gigahertz bands <a class="yt-timestamp" data-t="00:05:53">[00:06:04]</a>.

## How RFICs Work

RFICs (Radio Frequency Integrated Circuits) are found in devices ranging from iPhones to two-way radios <a class="yt-timestamp" data-t="00:06:08">[00:06:17]</a>. These devices function as `transceivers`, combining both transmitter and receiver capabilities <a class="yt-timestamp" data-t="00:06:17">[00:06:21]</a>.

The process of sending a message from a phone through an RFIC involves several steps:
1.  **Digital to Analog Conversion**: The phone's processor sends digital data (bits) to the transceiver <a class="yt-timestamp" data-t="00:06:36">[00:06:40]</a>. The RFIC converts these digital bits into a continuous analog signal, known as the `baseband` <a class="yt-timestamp" data-t="00:06:47">[00:06:54]</a>.

### Upconversion

The `baseband` signal is low frequency, which would require an impractically large antenna for a phone, as antennas are optimally about half the wavelength <a class="yt-timestamp" data-t="00:07:03">[00:07:15]</a>. To address this, the RFIC utilizes a `mixer` to combine the baseband signal with a higher frequency signal called the `carrier frequency` <a class="yt-timestamp" data-t="00:07:21">[00:07:32]</a>.

This process, known as `upconversion`, transforms the baseband signal into a `passband signal` <a class="yt-timestamp" data-t="00:07:32">[00:07:35]</a>. The cell operator selects the carrier frequency based on regulatory allocations and wireless technology standards <a class="yt-timestamp" data-t="00:07:41">[00:07:45]</a>. When the passband signal is created, `sidebands` of frequencies higher and/or lower than the carrier frequency are also generated, containing the actual data from the baseband <a class="yt-timestamp" data-t="00:07:50">[00:08:00]</a>. The `bandwidth` encompasses the entire range of frequencies from the lowest to the highest sideband <a class="yt-timestamp" data-t="00:08:04">[00:08:08]</a>. The size of these sidebands is a percentage of the carrier frequency <a class="yt-timestamp" data-t="00:08:10">[00:08:15]</a>; thus, a higher carrier frequency, like that of [[millimeterwave_5g_challenges_and_prospects | mmWave]], yields greater bandwidth and more data capacity <a class="yt-timestamp" data-t="00:08:15">[00:08:21]</a>.

### Path Loss

Once the passband signal is prepared, it needs to reach the cell tower, often kilometers away <a class="yt-timestamp" data-t="00:08:28">[00:08:37]</a>. As a wave propagates outwards from the phone, it expands like a spherical bubble, a behavior formally known as an `isotropic radiator` <a class="yt-timestamp" data-t="00:08:44">[00:09:04]</a>.

The power used to output this signal is spread across the bubble's expanding surface area, diluting the wave's power density <a class="yt-timestamp" data-t="00:09:25">[00:09:31]</a>. This dilution is called `path loss`, quantified by the Friis Equation <a class="yt-timestamp" data-t="00:09:37">[00:09:43]</a>. Path loss contributes significantly to `attenuation`, the gradual reduction of signal strength <a class="yt-timestamp" data-t="00:09:43">[00:09:51]</a>. Other factors like rain and object obstruction also cause attenuation <a class="yt-timestamp" data-t="00:09:51">[00:09:55]</a>. To ensure the passband signal reaches the tower, its power must be amplified <a class="yt-timestamp" data-t="00:10:02">[00:10:09]</a>.

### Power Amplifier

The `power amplifier` is the most power-hungry and challenging module to design within an RFIC <a class="yt-timestamp" data-t="00:10:15">[00:10:20]</a>. Designers must achieve high output power to reach the tower while maintaining good efficiency and linearity <a class="yt-timestamp" data-t="00:10:24">[00:10:28]</a>.

*   **Efficiency**: Wireless devices operate in power-constrained environments and generate heat <a class="yt-timestamp" data-t="00:10:33">[00:10:36]</a>. `Drain efficiency` measures this, for example, 50% efficiency means 2 watts drawn from the battery yield 1 watt output <a class="yt-timestamp" data-t="00:10:42">[00:10:46]</a>.
*   **Linearity**: Describes the quality of the signal as it passes through the amplifier <a class="yt-timestamp" data-t="00:10:52">[00:10:56]</a>.

After amplification, the boosted passband signal is sent to the antennas <a class="yt-timestamp" data-t="00:11:03">[00:11:05]</a>.

### Antennas for mmWave

While the Friis equation indicates that path loss is proportional to the wavelength squared, suggesting high-frequency waves travel less effectively, this is only true for identically sized antennas <a class="yt-timestamp" data-t="00:11:18">[00:11:28]</a>. With [[millimeterwave_5g_challenges_and_prospects | mmWave]], the smaller wavelengths allow for smaller antennas <a class="yt-timestamp" data-t="00:11:44">[00:11:50]</a>.

These smaller antennas, often with a gnarly spiral shape <a class="yt-timestamp" data-t="00:11:50">[00:11:57]</a>, can be packed into arrays (sometimes as many as 32) within the same area <a class="yt-timestamp" data-t="00:11:57">[00:12:01]</a>. These antenna arrays can generate directional beams aimed at the tower or base station <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. When the tower sends a response, it also forms a beam towards the handset <a class="yt-timestamp" data-t="00:12:18">[00:12:22]</a>.

Inside the handset, the process is reversed: the transmission is received, isolated, amplified, and then a mixer pulls out the analog signal for conversion back into digital <a class="yt-timestamp" data-t="00:12:25">[00:12:39]</a>.

## [[millimeterwave_5g_challenges_and_prospects | Millimeter Wave Challenges]]

One of the significant [[millimeterwave_5g_challenges_and_prospects | challenges with mmWave]] is its inability to easily penetrate objects <a class="yt-timestamp" data-t="00:12:39">[00:12:43]</a>. Buildings, foliage, and even the human body can attenuate the signal <a class="yt-timestamp" data-t="00:12:47">[00:12:50]</a>. Bricks, trees, and outdoor tinted glass are particularly effective at attenuating [[millimeterwave_5g_challenges_and_prospects | mmWave signals]] <a class="yt-timestamp" data-t="00:12:50">[00:12:55]</a>, with AT&T flagging the latter as a major issue <a class="yt-timestamp" data-t="00:12:55">[00:13:01]</a>. Heavy rainfall, however, does not appear to be a significant factor for people within 200 meters of a base station <a class="yt-timestamp" data-t="00:13:01">[00:13:05]</a>.

Even simply facing away from a base station can hurt performance <a class="yt-timestamp" data-t="00:13:10">[00:13:13]</a>. A 2022 experiment in Boston found that turning one's back to a [[millimeterwave_5g_challenges_and_prospects | mmWave]] base station caused a drastic drop in both downlink and uplink metrics, despite initial performance being 10 times better for downlink and 3 times better for uplink compared to LTE <a class="yt-timestamp" data-t="00:13:13">[00:13:27]</a>.

Therefore, [[millimeterwave_5g_challenges_and_prospects | mmWave]] generally performs best in busy areas with "line of sight," such as sports arenas, malls, and airports <a class="yt-timestamp" data-t="00:13:31">[00:13:39]</a>. While there have been **[[MillimeterWave 5G challenges and prospects | 5G conspiracy theories]]**, little credible scientific evidence suggests that [[millimeterwave_5g_challenges_and_prospects | mmWave]] rollouts cause damaging health issues <a class="yt-timestamp" data-t="00:13:40">[00:13:52]</a>.

### Densification

The characteristics of [[millimeterwave_5g_challenges_and_prospects | mmWave]] necessitate `densification` for telecoms <a class="yt-timestamp" data-t="00:14:13">[00:14:16]</a>. Unlike 1G through 4G, which used large macro-cells with ranges of several kilometers, [[millimeterwave_5g_challenges_and_prospects | mmWave]] requires the installation of many small cells, potentially as close as 50-100 meters apart <a class="yt-timestamp" data-t="00:14:16">[00:14:26]</a>.

This `densification` presents [[technical_and_economic_obstacles_in_mmwave_deployment | significant challenges]]:
*   **Site Acquisition**: Obtaining numerous 5G sites is a time-consuming task <a class="yt-timestamp" data-t="00:14:32">[00:14:35]</a>.
*   **Infrastructure Requirements**: Sites need 24/7 power for emergency services and a back-haul connection to the larger network <a class="yt-timestamp" data-t="00:14:35">[00:14:46]</a>.
*   **Aesthetics and Permitting**: Cells must be aesthetically inconspicuous, and environmental permitting is required <a class="yt-timestamp" data-t="00:14:46">[00:14:56]</a>.

Telecoms are considering innovative solutions, such as leveraging `reflectors` integrated into billboards or exterior glass to bounce [[millimeterwave_5g_challenges_and_prospects | mmWave signals]] off buildings, as a cost-saving alternative to acquiring new cell sites <a class="yt-timestamp" data-t="00:14:56">[00:15:10]</a>.

## [[technical_and_economic_obstacles_in_mmwave_deployment | 5G Deployment Complexities]]

The transition from LTE to [[standards_and_strategic_evolution_of_5G_networks | 5G]] has been complex <a class="yt-timestamp" data-t="00:15:16">[00:15:21]</a>. The definition of [[standards_and_strategic_evolution_of_5G_networks | 5G]] applies to any device using the [[standards_and_strategic_evolution_of_5G_networks | 5G New Radio standard]] <a class="yt-timestamp" data-t="00:15:21">[00:15:27]</a>. The [[standards_and_strategic_evolution_of_5G_networks | 5G New Radio standard]] supports three sets of [[5g_spectrum_and_its_frequency_bands | 5G bands]]: low, mid, and high bands <a class="yt-timestamp" data-t="00:15:27">[00:15:33]</a>.

*   **Low and Mid Bands**: Between 410 megahertz and 7.1 gigahertz, these offer good coverage but weaker capacity, similar to 4G LTE <a class="yt-timestamp" data-t="00:15:33">[00:15:44]</a>.
*   **High Band ([[millimeterwave_5g_challenges_and_prospects | mmWave]])**: This is where the most capacity and data rates are promised <a class="yt-timestamp" data-t="00:15:48">[00:15:52]</a>. However, its deployment is the most challenging due to propagation and densification issues <a class="yt-timestamp" data-t="00:15:52">[00:15:56]</a>.

Telecoms have two primary deployment strategies to transition without abandoning their existing LTE networks <a class="yt-timestamp" data-t="00:16:00">[00:16:05]</a>:
*   **Standalone (SA)**: Building a true [[standards_and_strategic_evolution_of_5G_networks | 5G network]] with [[standards_and_strategic_evolution_of_5G_networks | 5G base stations]] connected to a [[standards_and_strategic_evolution_of_5G_networks | 5G core network]] and [[standards_and_strategic_evolution_of_5G_networks | 5G New Radio consumer devices]], representing a completely new infrastructure <a class="yt-timestamp" data-t="00:16:09">[00:16:23]</a>.
*   **Non-standalone (NSA)**: An interim step where [[standards_and_strategic_evolution_of_5G_networks | 5G New Radio]] connects to a 4G LTE core <a class="yt-timestamp" data-t="00:16:23">[00:16:35]</a>. This offers some speed improvements and LTE fallback but provides less significant enhancement, especially at lower bands <a class="yt-timestamp" data-t="00:16:35">[00:16:40]</a>.

### United States Deployment and Pullback

American telecoms like Verizon and AT&T were early adopters of [[millimeterwave_5g_challenges_and_prospects | mmWave 5G]] <a class="yt-timestamp" data-t="00:16:44">[00:16:51]</a>. For them, existing 3G and 4G networks occupied the low and mid-band [[5g_spectrum_and_its_frequency_bands | 5G frequencies]], making high-band [[5g_spectrum_and_its_frequency_bands | spectrum]] a greenfield opportunity <a class="yt-timestamp" data-t="00:16:51">[00:17:05]</a>.

In 2018, Verizon began deploying Non-Standalone [[standards_and_strategic_evolution_of_5G_networks | 5G]] for mobile and fixed wireless access, which delivers internet broadband wirelessly <a class="yt-timestamp" data-t="00:17:05">[00:17:11]</a>. While fixed wireless access has worked well as a niche service <a class="yt-timestamp" data-t="00:17:17">[00:17:20]</a>, the mobile service rollout of [[millimeterwave_5g_challenges_and_prospects | mmWave]] faced challenges <a class="yt-timestamp" data-t="00:17:26">[00:17:29]</a>. Customers were generally unwilling to pay a significant premium for faster rates, and confusing [[standards_and_strategic_evolution_of_5G_networks | 5G]] branding contributed to a lack of clear understanding about network connectivity <a class="yt-timestamp" data-t="00:17:29">[00:17:49]</a>.

Despite Apple's release of the [[millimeterwave_5g_challenges_and_prospects | 5G mmWave]]-supported iPhone 12 in the US in late 2020 <a class="yt-timestamp" data-t="00:17:57">[00:18:03]</a>, the situation did not significantly change <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. Analysts expected [[millimeterwave_5g_challenges_and_prospects | mmWave]] to carry 5% of mobile traffic in 2021 <a class="yt-timestamp" data-t="00:18:12">[00:18:17]</a>. However, OpenSignal reported that only 2.9% of mobile traffic in US urban areas was consumed on [[millimeterwave_5g_challenges_and_prospects | mmWave 5G]] in 2021 <a class="yt-timestamp" data-t="00:18:22">[00:18:28]</a>.

A study by EJL Wireless Research in San Diego indicated that slight movement would cause phones to fall back to 4G LTE <a class="yt-timestamp" data-t="00:18:35">[00:18:47]</a>, raising skepticism about the return on investment for covering large cities <a class="yt-timestamp" data-t="00:18:47">[00:18:54]</a>. While Verizon and Qualcomm argued that shifting data traffic to [[millimeterwave_5g_challenges_and_prospects | mmWave]] would alleviate pressure on 3G and 4G networks, Wall Street remained unconvinced <a class="yt-timestamp" data-t="00:18:54">[00:19:10]</a>.

Consequently, Verizon and AT&T have adjusted their strategy. In February 2021, they acquired licenses for [[5g_spectrum_and_its_frequency_bands | 5G mid-band spectrum]] in the "C-band" (3.7 gigahertz), with Verizon alone spending over $45 billion <a class="yt-timestamp" data-t="00:19:20">[00:19:30]</a>. Since then, both companies have concentrated on expanding their mid-band offerings, including their Standalone [[standards_and_strategic_evolution_of_5G_networks | 5G network]] <a class="yt-timestamp" data-t="00:19:38">[00:19:42]</a>. Device support for [[millimeterwave_5g_challenges_and_prospects | mmWave]] remains limited, with only US iPhones supporting it and iPads recently dropping support entirely <a class="yt-timestamp" data-t="00:19:48">[00:19:57]</a>.

## Conclusion

Telecoms continue to expand [[millimeterwave_5g_challenges_and_prospects | mmWave]] primarily for fixed wireless access in rural areas and high-density urban areas like airports and sports stadiums, where its capabilities are best utilized <a class="yt-timestamp" data-t="00:20:14">[00:20:24]</a>. However, a widespread, compelling killer application for [[millimeterwave_5g_challenges_and_prospects | mmWave]] has not yet emerged <a class="yt-timestamp" data-t="00:20:30">[00:20:36]</a>. Many of the "internet of things" and Industry 4.0 initiatives that [[standards_and_strategic_evolution_of_5G_networks | 5G]] was expected to facilitate have not materialized <a class="yt-timestamp" data-t="00:20:36">[00:20:43]</a>.

[[technical_and_economic_obstacles_in_mmwave_deployment | Deployments]] in the United States have not met expectations, leading the FCC to explore more creative solutions for utilizing the largely unused [[millimeterwave_5g_challenges_and_prospects | mmWave spectrum]] <a class="yt-timestamp" data-t="00:20:43">[00:20:55]</a>. Outside the US, the rest of the world has not extensively adopted [[millimeterwave_5g_challenges_and_prospects | mmWave]], with Japan being a notable exception due to its network setup for the 2020 Tokyo Olympics <a class="yt-timestamp" data-t="00:20:55">[00:21:07]</a>.

While technology continues to evolve and telecoms move towards Standalone [[standards_and_strategic_evolution_of_5G_networks | 5G]] with ongoing improvements from companies like Qualcomm <a class="yt-timestamp" data-t="00:21:07">[00:21:15]</a>, the future benefits for [[millimeterwave_5g_challenges_and_prospects | mmWave]] from this progression remain to be seen <a class="yt-timestamp" data-t="00:21:15">[00:21:17]</a>.