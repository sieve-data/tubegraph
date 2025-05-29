---
title: Challenges in developing commercial EUV systems
videoId: 8_OOta7Y6Ik
---

From: [[asianometry]] <br/> 

The development of commercial-ready Extreme Ultraviolet (EUV) lithography systems presented an "incredible challenge" to the semiconductor industry, stretching over multiple decades <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This monumental task required brand new, substantial engineering work and significant resources <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The total cost of Japan's EUV effort from 1999 to 2012 is estimated to be between $5 to $10 billion, an "exponential jump" compared to previous lithography projects like the VLSI project which cost around $150 million <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.

## Technical Hurdles

The development of EUV systems involved overcoming significant [[engineering_challenges_of_the_euv_light_source | engineering challenges across its three core parts]]: the exposure tool, the mask, and the photoresist <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Exposure Tool Challenges
The exposure tool, containing the EUV light source and optical system, faced numerous [[innovations_in_optical_systems_for_high_na_euv | challenges in optical systems]] and other subsystems <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>:
*   **Light Source Power:** A major hurdle was achieving sufficient power output from the light source. The Nikon EUV-1's light source topped out at about 100 Watts, far short of the intermediate goal of 110-180 Watts and the high-volume production goal of 250 Watts <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a> <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. Less power meant longer wafer exposure times, slowing down throughput <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **Light Source Technology:** Two main approaches for producing EUV light were researched:
    *   **Laser-produced plasma (LPP):** Firing a laser at a material to turn it into plasma that emits EUV light <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This was the approach eventually chosen by [[asml_and_highvolume_euv_systems | ASML]] <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   **Discharge-produced plasma (DPP):** Creating a material cloud and firing high-powered sparks between electrodes to create light-emitting plasma <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. While considered more power-efficient, physically smaller, and cleaner, DPP struggled to output sufficient power <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. Japan's Nikon used a DPP contraption, but it struggled with contamination and power output <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. [[asml_and_highvolume_euv_systems | ASML]] also experimented with DPP but halted work on it in 2013, eventually pioneering a laser double-shot method for sufficient power levels <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
*   **Optics Manufacturing and Metrology:** Developing the work of adding reflective multi-layers to mirrors and cleaning them was a significant challenge, as was measuring mirror performance during exposure steps <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Mechanical Alignment:** Aligning the wafer and mask within tolerances of half a nanometer was a vital, though less "sexy," subsystem challenge <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Mask Challenges
The mask, containing the chip design, posed several [[challenges_in_manufacturing_euv_lithography_machines | challenges]] <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>:
*   **Defect-Free Production:** Consistently producing defect-free photomasks was immensely difficult due to the "incredible tolerances involved" <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. The goal was to reduce defects from an ambitious 0.1-1 per square centimeter to eventually 0.003 defects per square centimeter <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. A defect threshold on the mask blank was a deviance of just a few nanometers <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Defect Detection (Actinic Light):** Traditional DUV light could not penetrate deep enough to detect defects in the blank's mirror layer <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This necessitated the use of EUV light itself for inspection, known as "actinic light" <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Contamination:** EUV light continually hitting the mirror's surface created carbon contamination, slowly deteriorating reflectivity <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>. While oxygen and UV dry cleaning helped, a mysterious contamination from a silicon carbon compound (cyloxane) emerged as a persistent problem as late as 2011 <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.

### Photoresist Challenges
[[Challenges in EUV Photoresist and Metrology | EUV photoresist]] development faced a major challenge related to EUV light's high absorbability <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>:
*   **Thin Layer Imaging (TLI):** EUV light could only travel about 700 angstroms deep into traditional resist materials, falling short of the customary 4,000 angstrom depth for existing patterns <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This required the development of new "thin layer imaging" (TLI) technologies <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

## Organizational and Economic Difficulties

Beyond the technical issues, the [[historical_context_and_industry_efforts_in_euv_advancement | development of EUV lithography]] was also impacted by organizational and economic factors.

### Complex Organization (Japan)
Japan's EUV effort rapidly expanded beyond the management capacity of a single research institution <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. By 2005, four separate research consortia were focusing on different parts of the EUV machine (ASET, EUVA, Leading Project, Mirai), creating a "complicated setup" <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a> <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. In contrast, the American EUV project had a single entity, EUV LLC, overseeing early commercialization <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

### Financial Constraints and Market Volatility
*   **Global Financial Crisis:** The 2008 global financial crisis heavily affected companies like Canon, with profits shrinking over 60 percent, leading to delayed plans and probable cuts in lithography R&D expenses (which were north of $600 million a year in 2008) <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. Nikon also cut R&D budgets during the 2009 crisis <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
*   **Market Decline:** 2010 was a difficult year, with market sales for lithography machines in the chip and LCD industries falling by half year-over-year <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

### Competition and Customer Loss
[[asml_and_the_commercialization_of_euv_lithography | ASML]] continually pulled ahead of Japanese competitors, establishing a lead of 18 months to two years by 2011 <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. In 2012, Intel's decision to invest up to $4 billion in [[asml_and_the_commercialization_of_euv_lithography | ASML]] for a 15% stake was a critical blow <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. As Intel was Nikon's second-biggest customer, the market realized this meant Intel was moving forward with [[asml_and_the_commercialization_of_euv_lithography | ASML]] alone <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. Without Intel as a cornerstone customer, Nikon likely decided that spending hundreds of millions of dollars annually on EUV R&D and capital expenditures was no longer viable, and their EUV efforts quietly tailed off <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.

Ultimately, the failure of Japan's EUV efforts was attributed to "economics and competition, not technology," despite substantial progress and the fact that problems faced by Nikon's EUV-1 were "not deal breakers" <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a> <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.