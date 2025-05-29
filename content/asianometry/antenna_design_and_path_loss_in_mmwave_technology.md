---
title: Antenna design and path loss in mmWave technology
videoId: cLEfKpsSAEU
---

From: [[asianometry]] <br/> 

[[challenges_of_millimeterwave_5g_deployment | Millimeter-Wave]] (mmWave) technology, a key part of the 5G wireless transition, promises immense bandwidth and super-fast speeds <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, its deployment faces significant technical and economic [[challenges_of_millimeterwave_5g_deployment | challenges]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Understanding the physics of wave propagation, specifically path loss, and innovations in antenna design are crucial to grasp how mmWave functions and its limitations.

## Radio Frequency Basics
Wireless communication relies on waves traveling through open space <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. The distance a wave travels in a single cycle is its wavelength, measured in meters <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The number of cycles passing a given point is the frequency, measured in hertz <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Frequency and wavelength are inversely related: as frequencies rise, wavelengths fall <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

Previous wireless generations (1G through 4G) primarily used frequency bands below 7.125 gigahertz <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. These bands have become very crowded, with typical cell operators having limited spectrum (around 200 megahertz) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. 5G was designed to be more flexible in its frequency band usage, opening up new parts of the spectrum, including mmWave <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Millimeter Wave Frequencies
[[impact_of_frequency_on_5g_performance_and_limitations | Millimeter Wave]] bands are typically in the 70/80/90 gigahertz range <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, with wavelengths in the 1-10 millimeter range <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The FCC opened these bands for new economic development in 2003 <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Before 5G, these frequencies were primarily used for military radars, satellite communications, or cellular back-haul (point-to-point connections with fixed antennas) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Signal Processing in [[technical_aspects_of_radio_frequency_integrated_circuits_rfics | RFICs]]
A phone's [[technical_aspects_of_radio_frequency_integrated_circuits_rfics | Radio Frequency Integrated Circuit]] (RFIC) acts as a transceiver, handling both transmission and reception <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

### Upconversion
When a phone sends data, the processor converts digital bits into a continuous analog signal called the "baseband" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This baseband signal is low frequency, which would require an impractically large antenna for a phone <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. To overcome this, the RFIC uses a mixer to combine the baseband signal with a higher frequency "carrier frequency" <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This process, called "upconversion," transforms the baseband into a "passband signal" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. The actual data is encoded in "sidebands" — a band of frequencies higher and/or lower than the carrier frequency <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

A higher carrier frequency, like those used in mmWave, allows for more bandwidth because the size of the sidebands is a percentage of the carrier frequency <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. For example, 10% of 25 gigahertz provides significantly more data capacity than 10% of 7 gigahertz <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## Path Loss and Attenuation
As a wireless signal propagates outwards from a device, it spreads out, like an expanding spherical bubble <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This expansion dilutes the wave's power density <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This dilution is known as "path loss" and is measured using the Friis Equation <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. Path loss leads to "attenuation," which is the gradual reduction of signal strength <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Other factors like rain and physical obstructions also contribute to attenuation <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

A critical point for mmWave is that path loss is proportional to the wavelength squared <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This means high-frequency waves, with their shorter wavelengths, generally experience much worse path loss than lower-frequency ones <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. Moving from 3 gigahertz to 30 gigahertz, for instance, can make path loss 100 times worse, requiring immense power to send a signal if using identically sized antennas <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

To compensate for path loss, the passband signal must be amplified by a power amplifier, the most power-hungry and challenging module to design in an RFIC <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Antenna Design for mmWave
The inverse relationship between frequency and wavelength is exploited in mmWave antenna design. Since mmWave has smaller wavelengths, antennas can also be made much smaller <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. This allows for stuffing whole arrays of antennas (sometimes as many as 32) into the same area <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

These antenna arrays can generate "directional beams" aimed precisely at the cell tower or base station, and vice versa <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This beamforming capability helps counteract the high path loss of mmWave frequencies by concentrating the signal's energy in a specific direction, rather than allowing it to spread out isotropically.

## Line of Sight [[challenges_of_millimeterwave_5g_deployment | Challenges]]
One of the most significant challenges for mmWave is its inability to easily penetrate certain objects <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Buildings, foliage, and even the human body can severely attenuate mmWave signals <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. Bricks, trees, and outdoor tinted glass are particularly effective at blocking these signals <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

Even just facing away from a base station can drastically reduce performance <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. An experiment in Boston found that while mmWave offered significantly better downlink and uplink speeds compared to LTE when facing the base station, turning one's back resulted in a drastic drop in both metrics <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

Due to these propagation characteristics, mmWave works best in extremely busy areas with a clear "line of sight," such as sports arenas, malls, and airports <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

## Densification and [[deployment_strategies_of_5g_in_the_united_states | Deployment]]
The limitations of mmWave signal penetration necessitate a strategy called "densification" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Unlike 4G, which used large macro-cells with ranges of several kilometers, mmWave requires installing many small cells, potentially as close as 50-100 meters apart <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. This mass deployment is challenging due to site acquisition, power availability, back-haul connections, aesthetic considerations, and environmental permitting <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

Telecoms have even considered leveraging reflectors integrated into billboards or exterior glass to bounce mmWave signals off buildings, as a cost-saving measure compared to acquiring more cell sites <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

Despite the technical feasibility demonstrated in research <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, real-world [[deployment_strategies_of_5g_in_the_united_states | deployments]] in the United States have not met initial expectations <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a> <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. Studies indicated that slight movements could cause phones to fall back to 4G LTE, casting doubt on the return on investment for large-scale urban coverage <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. Currently, mmWave is primarily expanding for fixed wireless access in rural areas and high-density urban areas like airports and sports stadiums <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. Outside the U.S., [[deployment_strategies_of_5g_in_the_united_states | Japan]] is a significant exception in its adoption of mmWave <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.