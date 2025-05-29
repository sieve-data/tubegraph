---
title: Challenges of MillimeterWave 5G deployment
videoId: cLEfKpsSAEU
---

From: [[asianometry]] <br/> 

Millimeter-Wave (mmWave) technology promised immense bandwidth and super-fast speeds as part of the 5G wireless transition <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, a few years into its rollout, significant technical and economic challenges persist <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Millimeter Wave Fundamentals

Millimeter wave bands are characterized by wavelengths in the 1-10 millimeter range <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The FCC opened these bands for new economic development in 2003 <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Historically, this spectrum was primarily used for military radars, satellite communications, or cellular back-haul <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. These applications involved point-to-point connections where large fixed antennas fired narrow mmWave beams at other fixed antennas several kilometers away <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Beam tolerances for these systems were so precise that strong winds could misalign them <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, illustrating why mmWave was not widely used for consumer wireless <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

The move to 5G embraced a new slice of the spectrum, supporting bands from 24.25 to 52.6 gigahertz <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. This higher [[impact_of_frequency_on_5g_performance_and_limitations | carrier frequency]] allows for more bandwidth and thus more data capacity <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## Key Technical Challenges

### [[antenna_design_and_path_loss_in_mmwave_technology | Path Loss and Attenuation]]

One of the primary challenges for mmWave is "path loss" <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. As a wireless signal propagates outwards from a device, its power density is diluted because it spreads across an expanding "surface area," similar to a spherical wave <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This dilution leads to "attenuation," a gradual reduction of signal strength <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

The Friis Equation indicates that path loss is proportional to the wavelength squared <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This implies that higher frequency waves, like mmWave, travel less effectively than lower frequency ones <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. For example, moving from a 3 gigahertz to a 30 gigahertz spectrum can result in path loss that is 100 times worse, requiring immense power to send a signal if antennas were identically sized <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

### Antenna Design for Mitigation

To counteract severe path loss, mmWave technology leverages smaller antennas due to its smaller wavelengths <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. These antennas, often with a gnarly spiral shape, can be packed into arrays (sometimes as many as 32) within the same space <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. These antenna arrays can generate directional beams aimed precisely at a tower or base station, and vice versa, to improve signal strength <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Line of Sight Limitations

A well-known issue with mmWave is its inability to easily penetrate certain objects <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Buildings, foliage, and even the human body can significantly attenuate signals <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. Bricks, trees, and outdoor tinted glass are particularly effective at blocking mmWave signals, with AT&T flagging the latter as a major concern during trials <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

Even simply facing away from a base station can hurt performance <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. A 2022 experiment in Boston found that turning one's back to a mmWave base station caused a drastic drop in both downlink and uplink performance compared to facing it <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

As a general rule, mmWave works best in extremely busy areas with a clear "line of sight," such as sports arenas, malls, and airports <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Densification Requirements

Given the limited range and penetration capabilities, mmWave deployment necessitates "densification" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Unlike 1G through 4G networks that used large macro-cells with ranges of several kilometers, mmWave requires the installation of many small cells in dense amounts, sometimes as close as 50-100 meters apart <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

Acquiring these numerous 5G sites is a challenging and time-consuming task <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. These sites need 24/7 power for emergency services, a back-haul connection to the larger network, and must be aesthetically inconspicuous <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. Environmental permitting adds another layer of complexity <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Telecoms have explored leveraging reflectors integrated into billboards or exterior glass to bounce mmWave signals, which could save costs compared to acquiring new cell sites <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## Deployment and Market Challenges

### [[deployment_strategies_of_5g_in_the_united_states | Deployment Strategies]]

The transition from LTE to 5G has been complex <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. The 5G New Radio standard supports low, mid, and high bands <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. While low and mid bands (410 megahertz to 7.1 gigahertz) offer good coverage, their capacity is weaker, similar to 4G LTE <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. The high band, where mmWave spectrum resides, promises the most capacity and data rates but requires the most work due to propagation and densification challenges <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.

Telecoms use two primary deployment methods:
*   **Standalone (SA)**: A true 5G network with 5G base stations, a 5G core network, and 5G New Radio consumer devices <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Non-standalone (NSA)**: A stepping stone where 5G New Radio connects to a 4G LTE core <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. This offers some speed improvements and LTE fallback but with less significant gains, especially at lower bands <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

### United States Market Reception

In the United States, major telecoms like Verizon and AT&T initially prioritized mmWave 5G <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This strategy made sense for them because their existing 3G and 4G networks occupied the low and mid-band frequencies, leaving high bands as "green field territory" <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

Verizon began deploying Non-Standalone mmWave 5G for mobile and fixed wireless access in 2018 <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. While fixed wireless access has worked well, the mobile service rollout faced difficulties <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. The mature smartphone ecosystem meant customers were not highly willing to pay a premium for faster rates <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. Additionally, confusing branding surrounding what constituted "5G" did not help <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

Despite Apple's iPhone 12 supporting mmWave in the US in late 2020 <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>, this did not significantly change the landscape <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. In 2021, analysts had expected mmWave to carry about 5% of mobile traffic, with Verizon hoping for 50% of urban traffic over time <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. However, OpenSignal reported that only about 2.9% of mobile traffic in US urban areas was consumed on mmWave 5G <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

A study in San Diego revealed a key reason: even slight movement could cause a phone to fall back to 4G LTE after connecting to mmWave <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. This raised skepticism about the return on investment for covering large cities <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

Facing Wall Street's displeasure and T-Mobile's successful low and mid-band 5G deployments <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>, Verizon and AT&T shifted their strategy. In February 2021, they bought licenses for 5G mid-band spectrum in the "C-band" (3.7 gigahertz), with Verizon alone spending over $45 billion <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. Since then, they have focused on expanding their mid-band offerings, including their standalone 5G network <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Device support for mmWave has also remained inconsistent, with only US iPhones supporting it and iPads recently dropping support entirely <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

## Conclusion

While telecoms continue to expand mmWave, it is primarily for fixed wireless access in rural areas and high-density urban locations like airports and sports stadiums, where it performs best <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. The promised "internet of things" and "industry 4.0" initiatives that 5G was expected to enable have not yet widely emerged <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

In the United States, mmWave deployments have not met expectations, leading the FCC to explore more creative solutions for its largely unused spectrum <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. Outside the US, adoption of mmWave has been limited, with Japan being a notable exception due to its network setup for the 2020 Tokyo Olympics <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. As technology evolves and telecoms move towards Standalone 5G with continued improvements from companies like Qualcomm, it remains to be seen if mmWave will benefit from this progression <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.