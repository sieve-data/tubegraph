---
title: MillimeterWave 5G challenges and prospects
videoId: cLEfKpsSAEU
---

From: [[asianometry]] <br/> 

Fifth-generation (5G) cellular technology represents a significant transition in wireless communication. A key component of this transition, promising immense bandwidth and super-fast speeds, is [[5g_spectrum_and_its_frequency_bands | Millimeter-Wave]] (mmWave) [00:00:02], [00:00:06]. While a fascinating technology, its rollout has encountered [[technical_and_economic_obstacles_in_mmwave_deployment | difficult technical and economic challenges]] [00:00:12], [00:00:16].

## Fundamentals

A wave's frequency and wavelength are inversely related; as frequencies rise, wavelengths fall [00:01:07]. Millimeter wave bands are so named because their wavelengths are in the 1-10 millimeter range [00:04:32]. A megahertz signifies a million cycles per second, a gigahertz a billion, and a terahertz a trillion [00:01:00].

Countries allocate parts of their electromagnetic spectrum for specific uses, such as radar or wireless communication [00:01:25]. Spectrum is fundamentally limited, making its efficient use a key challenge [00:01:29]. Previous wireless generations (1G through 4G) primarily utilized frequency bands below 7.125 gigahertz [00:02:09]. These "neighborhoods" became increasingly crowded, with cell operators typically having only about 200 megahertz of spectrum, which proved insufficient for growing demands [00:02:15], [00:02:21].

## The Rise of Millimeter Wave in 5G

In 2011, Zhouyue Pi and Farooq Khan of Samsung Electronics published an influential article suggesting the exploration of largely unused mmWave regions for future wireless communication [00:04:02], [00:04:21]. They identified several mmWave bands in the 70/80/90 gigahertz range as potential candidates [00:04:26].

Prior to this, the FCC had opened these bands in 2003 for new economic development [00:04:37]. Before 2003, mmWave spectrum was primarily used for military radars, satellite communications, or cellular back-haul (point-to-point connections with fixed antennas) [00:04:43], [00:04:50]. These point-to-point connections were sensitive to strong winds, which could misalign beams, making them impractical for general consumer wireless use [00:05:01], [00:05:05].

Some of the first consumer applications of mmWave after the FCC's decision included:
*   **Automotive radar:** The 77 gigahertz band was opened to assist advanced driver assistance systems (ADAS) in identifying dangerous situations [00:05:12], [00:05:16], [00:05:21].
*   **WiGig WiFi standard:** Uses a 60 gigahertz band, though its adoption has been limited [00:05:28], [00:05:31].

After Samsung's paper, the concept gained traction. By 2014, research from NYU and UT Austin demonstrated the technical feasibility of bringing mmWave to consumer wireless applications [00:05:39], [00:05:45]. Ultimately, [[standards_and_strategic_evolution_of_5G_networks | 5G gained support]] for a new set of high-band frequencies ranging from 24.25 to 52.6 gigahertz, in addition to more traditional sub-7 gigahertz bands [00:05:53], [00:06:04].

The philosophical goals for the 5G standard were broad, intending to handle more mobile video traffic (Enhanced Mobile Broadband) [00:02:37], [00:02:42], enable ultra-reliable low-latency networking (URLLC) for critical data like self-driving cars or wirelessly controlled robots [00:02:52], [00:02:57], and support Massive Machine Type Communications for low-cost, infrequent data transmissions from sensors or vending machines [00:03:18], [00:03:23], [00:03:28]. To achieve these diverse requirements, 5G was designed to be highly flexible, particularly in its supported frequency bands [00:03:46], [00:03:50].

A key advantage of higher carrier frequencies like mmWave is increased bandwidth [00:08:15]. For example, 10% of 25 gigahertz offers significantly more data capacity than 10% of 7 gigahertz [00:08:21].

## Technical Considerations: RFICs and Antennas

[[radio_frequency_integrated_circuits_and_their_role_in_5G | Radio Frequency Integrated Circuits (RFICs)]] are central to wireless communication, acting as transceivers (combined transmitters and receivers) [00:00:20], [00:06:08], [00:06:21]. When a phone transmits, the RFIC converts digital data (bits) into a continuous analog "baseband" signal [00:06:40], [00:06:47], [00:06:54].

### Upconversion
Since baseband signals are low frequency and would require impractically large antennas for a phone (an antenna should be about half the wavelength) [00:07:03], [00:07:08], the RFIC employs a mixer to "upconvert" the baseband signal [00:07:21]. This involves mixing it with a higher "carrier frequency" to create a "passband signal" [00:07:27], [00:07:32], [00:07:35]. The actual data from the baseband is encoded in small bands of frequencies higher and/or lower than the carrier frequency, known as "sidebands" [00:07:50], [00:07:54], [00:08:00]. The entire frequency range from the lowest to highest sideband is the bandwidth [00:08:04].

### Path Loss and Power Amplifiers
As a wave travels outward from a mobile device, its power density dilutes, a phenomenon called "path loss" [00:08:44], [00:08:49], [00:08:59], [00:09:31]. Path loss contributes to "attenuation," which is the gradual reduction of signal strength [00:09:43], [00:09:46]. To ensure the passband signal reaches the cell tower, its power must be amplified by a power amplifier [00:10:06], [00:10:09].

The power amplifier is the most power-hungry and challenging module to design within the RFIC [00:10:15], [00:10:20]. Designers must achieve high output power to reach the tower while maintaining efficiency (e.g., drain efficiency) and linearity (signal quality) [00:10:24], [00:10:28], [00:10:33], [00:10:42], [00:10:52], [00:10:56]. After amplification, the signal is transferred to the antennas [00:11:03].

### Antennas for mmWave
While higher frequency waves like mmWave typically suffer greater path loss (proportional to wavelength squared), mmWave's smaller wavelengths allow for smaller antennas [00:11:22], [00:11:28], [00:11:34], [00:11:44], [00:11:50]. This enables the integration of multiple antennas into arrays, sometimes as many as 32, within the same space [00:11:57], [00:12:01]. These antenna arrays can generate directional beams, known as beamforming, that are precisely aimed at the tower or base station, and vice versa [00:12:05].

## Challenges and Deployment

### Line of Sight Issues
A significant challenge for mmWave is its poor penetration capabilities [00:12:39]. The signal struggles to pass through objects such as buildings, foliage, and even the human body [00:12:43], [00:12:47], [00:12:50]. Bricks, trees, and outdoor tinted glass are particularly effective at attenuating mmWave signals [00:12:50], [00:12:55]. Even facing away from a base station can drastically reduce performance [00:13:10], [00:13:13], [00:13:24], [00:13:27]. However, heavy rainfall does not appear to be a major factor [00:13:01].

Due to these limitations, mmWave works best in "line of sight" environments, such as sports arenas, malls, and airports [00:13:31], [00:13:35].

*   **5G Conspiracy Theories:** Despite some rhetoric, there is little credible scientific evidence that mmWave rollouts cause damaging health issues [00:13:40], [00:13:44], [00:13:48]. The waves primarily affect skin without penetrating deeply, and the Sun's UV rays are considered far more energetic and potentially damaging [00:13:55], [00:14:01], [00:14:06].

### Densification
The limited range and penetration of mmWave signals necessitate a "densification" of network infrastructure [00:14:13]. Unlike 1G-4G networks that used large macro-cells with ranges of several kilometers, mmWave requires many small cells to be installed in dense urban areas, perhaps as close as 50-100 meters apart [00:14:16], [00:14:21], [00:14:26].

Acquiring numerous 5G sites presents significant challenges for telecoms [00:14:32]. These sites require:
*   24/7 power availability for emergency services [00:14:35], [00:14:41].
*   Back-haul connections to the larger network [00:14:43].
*   Aesthetically inconspicuous designs, to avoid visual clutter [00:14:46], [00:14:51].
*   Navigating environmental permitting processes [00:14:54].

Telecoms have even considered innovative solutions like leveraging reflectors integrated into billboards or exterior glass to bounce mmWave signals, potentially saving money compared to acquiring new cell sites [00:14:56], [00:15:00], [00:15:10].

### Deployment Strategies
The transition from LTE to 5G has been complex [00:15:16]. The 5G New Radio standard supports three types of bands: low, mid, and high [00:15:21], [00:15:27].
*   **Low and Mid-bands:** Ranging between 410 megahertz and 7.1 gigahertz, these offer good coverage but weaker capacity, similar to 4G LTE [00:15:33], [00:15:40], [00:15:44].
*   **High-band:** This is the mmWave spectrum, promising the most capacity and data rates, but also posing the greatest deployment challenges due to propagation and densification issues [00:15:48], [00:15:52], [00:15:56].

Telecoms can deploy 5G using two main approaches:
*   **Standalone (SA) 5G:** Involves building an entirely new 5G network with 5G base stations connected to a 5G core network and supporting 5G New Radio devices [00:16:09], [00:16:16]. This is considered "true 5G" [00:21:10].
*   **Non-Standalone (NSA) 5G:** A transitional step where 5G New Radio connects to an existing 4G LTE core [00:16:23], [00:16:28]. While offering somewhat faster speeds and LTE fallback, the improvement is not always significant, particularly at lower bands [00:16:35], [00:16:40].

## United States Experience

In the United States, Verizon and AT&T were early adopters of mmWave 5G [00:16:44]. For them, the high bands presented "green field territory" as their low and mid-band frequencies were already occupied by legacy 3G and 4G networks [00:16:51], [00:16:57], [00:17:05].

In 2018, Verizon began deploying Non-Standalone 5G for both mobile and fixed wireless access services (internet broadband via wireless connection) [00:17:05], [00:17:11]. While fixed wireless access has seen some success, the mobile service part of the mmWave rollout faced challenges [00:17:17], [00:17:20], [00:17:26]. The mature smartphone market meant customers were generally unwilling to pay a significant premium for faster rates [00:17:29], [00:17:35]. Confusing branding around what constituted "5G" also hindered adoption [00:17:41], [00:17:45].

Even with Apple's release of the iPhone 12 with mmWave support in the US in late 2020, expectations were not met [00:17:57], [00:18:03]. Analysts projected mmWave to carry 5% of mobile traffic in 2021, with Verizon hoping for 50% of urban traffic [00:18:12], [00:18:17]. However, OpenSignal reported only 2.9% of US urban mobile traffic on mmWave 5G in 2021 [00:18:22], [00:18:28]. A study in San Diego revealed that slight movement could cause phones to fall back to 4G LTE after connection, raising skepticism about covering large cities with mmWave [00:18:35], [00:18:41], [00:18:47].

While Verizon and Qualcomm argued that shifting data traffic to mmWave would alleviate pressure on existing 3G/4G networks, Wall Street remained unconvinced, especially as T-Mobile gained ground with low and mid-band 5G deployments [00:18:54], [00:18:59], [00:19:04], [00:19:10], [00:19:12], [00:19:20].

As a result, Verizon and AT&T adjusted their strategies. In February 2021, they invested heavily in mid-band 5G spectrum (C-band, 3.7 gigahertz), with Verizon spending over $45 billion [00:19:26], [00:19:30], [00:19:38]. They have since focused on expanding their mid-band offerings, including standalone 5G networks [00:19:38], [00:19:42]. Device support for mmWave has also been inconsistent; only US iPhones support it, and iPads recently dropped support entirely [00:19:48], [00:19:53], [00:19:57].

## Future Prospects

Telecoms continue to expand mmWave, but primarily for fixed wireless access in rural areas and in high-density urban locations like airports and sports stadiums, where its line-of-sight characteristics are best suited [00:20:14], [00:20:19], [00:20:24].

A "killer app" for mmWave — a broadly compelling use case — has yet to emerge [00:20:30]. Many anticipated applications for the "internet of things" and Industry 4.0 that 5G was expected to facilitate have not materialized [00:20:36]. In the United States, deployments have fallen short of expectations, leading the FCC to explore more creative solutions for utilizing the largely unused mmWave spectrum [00:20:43], [00:20:48].

Globally, mmWave adoption has been limited, with Japan being a notable exception, having set up a network ahead of the 2020 Tokyo Olympics [00:20:55], [00:21:00]. While wireless technology continues to evolve, with telecoms moving towards Standalone 5G bolstered by ongoing improvements from companies like Qualcomm, it remains to be seen if mmWave will significantly benefit from this progression [00:21:07], [00:21:12], [00:21:15].