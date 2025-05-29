---
title: Technical aspects of Radio Frequency Integrated Circuits RFICs
videoId: cLEfKpsSAEU
---

From: [[asianometry]] <br/> 

If semiconductors are considered "black magic," then Radio Frequency Integrated Circuits, or RFICs, are described as "the darkest of the dark arts" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This article dips into the technical aspects of RFICs, particularly in the context of 5G millimeter-wave (mmWave) deployment <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Fundamentals of Wireless Communication

To understand RFICs, it's helpful to grasp basic wireless concepts:
*   **Wavelength** The distance a wave travels in a single cycle, measured in meters <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Frequency** How many cycles pass through a given point per second, measured in hertz (Hz) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Megahertz (MHz) means a million cycles per second, gigahertz (GHz) a billion, and terahertz (THz) a trillion <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Inverse Relationship** Frequency and wavelength are inversely related; as frequencies rise, wavelengths fall <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Spectrum Allocation** Countries allocate parts of their electromagnetic spectrum for specific uses, such as radar, wireless communication, or Wi-Fi <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Spectrum is fundamentally limited, making efficient use a challenge <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Previous wireless generations (1G through 4G) primarily used frequency bands below 7.125 GHz, which became very crowded <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. 5G, in contrast, opened up new spectrum slices, including the millimeter-wave regions <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Millimeter-wave bands, like those in the 70/80/90 GHz range, have wavelengths between 1-10 millimeters <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## RFIC Functionality: Transmitting a Signal

Modern devices like smartphones and two-way radios are fundamentally radio transceivers, meaning they can both transmit and receive signals <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. The RFIC orchestrates this process.

### Digital to Analog Conversion
When a phone wants to send a message, its processor sends digital data (1s and 0s) to the transceiver <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The RFIC converts these digital bits into a continuous analog signal, known as the "baseband" <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### [[impact_of_frequency_on_5g_performance_and_limitations | Upconversion]]
The baseband signal is low frequency, which would require an impractically large antenna for a phone (rule of thumb: antenna about half the wavelength) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. To address this, the RFIC uses a mixer to combine the baseband signal with a higher frequency signal called the "carrier frequency" <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This process, called "upconversion," transforms the baseband signal into a "passband signal" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

The carrier frequency is chosen by the cell operator based on regulatory allocations and wireless technology standards <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. When the passband signal is created, it also generates "sidebands"—small frequency bands higher and/or lower than the carrier frequency, where the actual data from the baseband is encoded <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The entire range from the lowest to highest sideband is called the bandwidth <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. A higher carrier frequency, like that of mmWave, allows for more bandwidth, translating to greater data capacity <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### [[antenna_design_and_path_loss_in_mmwave_technology | Path Loss]]
When a wave propagates through the air from a mobile device, it can be visualized as an expanding spherical wave, or "isotropic radiator" <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. As this "bubble" expands, its surface area grows, diluting the wave's power density <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This dilution is known as "path loss" and is measured by the Friis Equation <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Path loss contributes significantly to "attenuation," which is the gradual reduction of signal strength <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Other factors like rain, object obstruction, and even the human body can also cause attenuation <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

To ensure the passband signal reaches the cell tower despite path loss and other attenuating factors, its power must be amplified <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

### Power Amplifier
The power amplifier is the most power-hungry and one of the most challenging modules to design within an RFIC <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Designers aim for the highest output power to reach the tower while maintaining good efficiency and linearity <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

*   **Efficiency:** Wireless devices are power-constrained and generate heat, so efficiency is crucial <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. "Drain efficiency" measures this; for example, an amplifier drawing 2 watts and outputting 1 watt has 50% drain efficiency <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Linearity:** This describes the quality of the signal as it passes through the amplifier <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

After amplification, the boosted passband signal is sent to the antennas <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

### [[antenna_design_and_path_loss_in_mmwave_technology | Antennas]]
While high-frequency waves (like mmWave) generally experience 100 times worse path loss than lower frequencies (e.g., 30 GHz vs. 3 GHz) if antennas were identically sized, mmWave's smaller wavelengths allow for smaller antennas <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. These smaller antennas often have a spiral shape and can be packed into arrays within the same area (e.g., 32 antennas) <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. These antenna arrays can generate directional beams aimed precisely at the tower or base station, and vice versa <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

## RFIC Functionality: Receiving a Signal
When the cell tower sends a response, it forms another beam towards the handset <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Inside the handset, the RFIC performs the reverse process: receiving and isolating the transmission, amplifying it, and then using a mixer to extract the analog signal for conversion back into digital data <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

## Challenges for mmWave RFICs

### Line of Sight
A significant challenge for mmWave is its inability to easily penetrate objects like buildings, foliage, or even the human body <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Bricks, trees, and outdoor tinted glass are particularly effective at attenuating mmWave signals <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Even turning away from a base station can drastically reduce performance <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. Therefore, mmWave works best in very busy areas with "line of sight," such as sports arenas, malls, and airports <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

### Densification
Due to these propagation characteristics, mmWave networks require "densification"—installing many small cells much closer together (perhaps 50-100 meters apart), unlike the large macro-cells used for 1G-4G <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This requires extensive infrastructure acquisition, ensuring constant power and back-haul connections, and addressing aesthetic and environmental concerns <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. Telecoms are even considering leveraging reflectors on billboards or glass to bounce mmWave signals, saving costs compared to acquiring new cell sites <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## Conclusion

While mmWave RFICs promise immense bandwidth and super-fast speeds, their deployment has faced technical and economic challenges <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Despite these hurdles, telecoms continue to expand mmWave for fixed wireless access in rural areas and high-density urban locations where it performs best <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. The role of RFICs remains critical as technology evolves towards standalone 5G networks and ongoing improvements from companies like Qualcomm <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.