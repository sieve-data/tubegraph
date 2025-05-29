---
title: Deployment strategies of 5G in the United States
videoId: cLEfKpsSAEU
---

From: [[asianometry]] <br/> 

5G marks a significant transition in wireless technology, promising immense bandwidth and super-fast speeds, particularly through Millimeter-Wave (mmWave) technology <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. However, a few years into its rollout, significant technical and economic [[Challenges of MillimeterWave 5G deployment | challenges]] remain <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Foundations of 5G

The philosophical foundations for 5G aimed for broad capabilities beyond just handling more data traffic, which is addressed by the Enhanced Mobile Broadband section of the standard <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. Creators also envisioned 5G enabling:
*   **Ultra Reliable Low Latency Networking (URLLC)**: For critical data requiring quick and reliable delivery, such as self-driving car communication or wirelessly controlled robot arms, aiming for signal delivery in under 10 milliseconds <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   **Massive Machine Type Communications**: For numerous low-cost machines transmitting data infrequently over long periods, like sensors, actuators, and vending machines <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.

These varied goals led to 5G being designed with greater flexibility in the frequency bands it can utilize, opening up new spectrum slices <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

## Millimeter Wave (mmWave) Technology

In 2011, Zhouyue Pi and Farooq Khan from Samsung Electronics advocated for exploring mmWave regions for 5G, specifically pointing to bands in the 70/80/90 gigahertz range <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. These are called millimeter wave bands because their wavelengths are in the 1-10 millimeter range <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. The FCC opened these bands for new economic development in 2003, having previously been used for military radars, satellite communications, or cellular back-haul (point-to-point connections) <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. Early consumer uses included automotive radar (77 GHz) and the WiGig WiFi standard (60 GHz) <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. By 2014, research demonstrated the technical feasibility of bringing mmWave to consumer wireless applications <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. Ultimately, 5G gained support for bands in the 24.25 to 52.6 gigahertz range, in addition to traditional sub-7 gigahertz bands <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

Higher carrier frequencies like mmWave provide more bandwidth, allowing for greater data capacity <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. However, [[Impact of frequency on 5G performance and limitations | mmWave]] signals face significant [[Impact of frequency on 5G performance and limitations | path loss]] (dilution of wave's power density as it travels) and attenuation <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. This requires amplification by a power amplifier, the most power-hungry and challenging module in an RFIC <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

### Challenges of mmWave Propagation
One of the primary [[Challenges of MillimeterWave 5G deployment | challenges of MillimeterWave 5G deployment]] is its inability to easily penetrate objects such as buildings, foliage, and even the human body <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>. Bricks, trees, and outdoor tinted glass are particularly effective at attenuating mmWave signals <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. Facing away from a base station can also drastically reduce performance <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. This means mmWave works best in extremely busy areas with "line of sight," such as sports arenas, malls, and airports <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.

To counteract these propagation issues, smaller mmWave antennas can be arranged in arrays (sometimes as many as 32) to generate directional beams aimed at the tower or base station, and vice versa <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>.

## Deployment Strategies

Given the propagation characteristics, mmWave requires significant network [[Challenges of MillimeterWave 5G deployment | densification]] <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>. Unlike 1G-4G's large macro-cells with several kilometers of range, mmWave deployments need many small cells, potentially as close as 50-100 meters apart <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>. Acquiring these sites is challenging, requiring 24/7 power, back-haul connections, aesthetic inconspicuousness, and environmental permitting <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. Telecoms have even considered using reflectors integrated into billboards or glass to bounce signals and save on site acquisition costs <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.

There are two main ways to deploy 5G, both using the 5G New Radio standard, which supports low, mid, and high (mmWave) bands <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>:
1.  **Standalone (SA) 5G**: A completely new 5G network with 5G base stations, a 5G core network, and 5G New Radio consumer devices <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>.
2.  **Non-Standalone (NSA) 5G**: A stepping stone between 4G LTE and Standalone 5G, where a 5G New Radio connects to a 4G LTE core network. This offers some speed improvements and LTE fallback, but benefits are often not great, especially at lower bands <a class="yt-timestamp" data-t="16:23:00">[16:23:00]</a>.

## 5G Deployment in the United States

The major American telecoms, Verizon and AT&T, were early adopters of mmWave 5G <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>. This made sense for them because their legacy 3G and 4G networks already occupied the low and mid-band 5G frequencies, making the high mmWave bands greenfield territory <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.

In 2018, Verizon began deploying Non-Standalone 5G for both mobile and fixed wireless access (internet broadband via wireless connection) <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>. While fixed wireless access showed promise, the mobile service rollout encountered difficulties <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>. Customer willingness to pay a premium for faster rates was low, and confusing branding of "5G" further complicated adoption <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>.

The release of the US version of the iPhone 12 with 5G mmWave support in late 2020 was a significant hope for broader adoption <a class="yt-timestamp" data-t="17:57:00">[17:57:00]</a>. However, expectations were not met. Analysts predicted mmWave would carry about 5% of mobile traffic in 2021 <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>, and Verizon projected 50% of urban traffic would eventually be on mmWave <a class="yt-timestamp" data-t="18:17:00">[18:17:00]</a>. Yet, OpenSignal reported that in 2021, only about 2.9% of mobile traffic in US urban areas was consumed on mmWave 5G <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>. A study in San Diego revealed that even slight movement would cause phones to fall back to 4G LTE after connection, casting doubt on the return on investment for covering large cities with mmWave <a class="yt-timestamp" data-t="18:35:00">[18:35:00]</a>. While Verizon and Qualcomm argued that shifting data traffic to mmWave would alleviate pressure on existing 3G and 4G networks, Wall Street remained unconvinced <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.

### Strategic Adjustments

Facing market dissatisfaction and the rise of T-Mobile's low and mid-band 5G deployments, Verizon and AT&T adjusted their strategies <a class="yt-timestamp" data-t="19:10:00">[19:10:00]</a>. In February 2021, both companies heavily invested in licenses for 5G mid-band spectrum in the "C-band" (3.7 gigahertz), with Verizon spending over $45 billion alone <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>. Since then, their focus has shifted to expanding mid-band offerings, including their Standalone 5G networks <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>. Device support for mmWave has also been inconsistent, with only US iPhones supporting it and iPads recently dropping support entirely <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>.

## Conclusion

While telecoms continue to expand mmWave, it is primarily for fixed wireless access in rural areas and high-density urban locations like airports and sports stadiums, where it works best <a class="yt-timestamp" data-t="20:14:00">[20:14:00]</a>. A "killer app" for mmWave with broad consumer appeal has yet to emerge, and many "Internet of Things" and Industry 4.0 initiatives that 5G was expected to enable have not materialized <a class="yt-timestamp" data-t="20:30:00">[20:30:00]</a>. Due to deployments not meeting expectations, the FCC is exploring more creative solutions for utilizing the largely unused mmWave spectrum <a class="yt-timestamp" data-t="20:43:00">[20:43:00]</a>. Outside of the US, few countries have significantly adopted mmWave, with Japan being a notable exception due to its network setup for the 2020 Tokyo Olympics <a class="yt-timestamp" data-t="20:55:00">[20:55:00]</a>.

Technology continues to evolve, with telecoms moving towards Standalone 5G and ongoing improvements by companies like Qualcomm <a class="yt-timestamp" data-t="21:07:00">[21:07:00]</a>. However, whether mmWave will fully benefit from this progression remains to be seen <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a>.