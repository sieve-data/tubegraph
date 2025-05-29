---
title: Challenges in developing EUV systems
videoId: 8_OOta7Y6Ik
---

From: [[asianometry]] <br/> 

The development of Extreme Ultraviolet (EUV) lithography systems has been a long and winding road spanning multiple decades, ultimately leading to ASML's successful shipment of the first high-volume EUV system in 2019 <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This marked a significant shift in the semiconductor lithography industry towards Europe, particularly at the expense of Japan, which had previously led the industry <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. [[japans_failed_euv_development_journey | Japan's failed EUV development journey]] illustrates the incredible challenge of producing commercial-ready [[euv_lithography_technology_and_its_challenges | EUV systems]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Early Perceptions and Misjudgments
[[euv_lithography_technology_and_its_challenges | EUV was invented in Japan]] in 1986 by Dr. Hiro Kinoshita, who successfully printed a circuit pattern using EUV light <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. However, at the time, EUV was just one of several potential next-generation lithography candidates <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Other options included Electron Beam direct write lithography, proximity x-ray, ion beam projection, Electron Beam projection, and 157 nanometers fluorine <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The Japanese lithography industry, like others, studied all these options but did not initially prefer EUV, seemingly leaning towards proximity x-ray <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. As late as 1997, Sematech evaluated EUV in fourth place, with x-ray in first <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Intel's interest and the founding of EUV LLC in the US, a consortium to fund EUV R&D, caught the Japanese by surprise <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Due to American restrictions on foreign participation, Japanese lithography makers Nikon and Canon could not directly join EUV LLC, forcing them to pursue their own path <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Japan's Development Strategy and Organizational Challenges
Japan's Ministry of International Trade and Industry (MITI) began its own [[euv_lithography_technology_and_its_challenges | EUV lithography]] program in 1998 <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The plan had three phases:
1.  **Phase 1 (1998-2001)**: Develop basic technologies for the exposure tool, mask, and resist, managed by ASET (Association of Super Advanced Electronic Technologies) <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
2.  **Phase 2 (2001-2003)**: Turn ASET's raw technology into a working prototype with partial financial support from the Japanese semiconductor industry <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
3.  **Phase 3 (until 2006)**: Commercialize the prototype, involving companies like Selete, Nikon, and Canon <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

This [[japans_failed_euv_development_journey | Japanese EUV effort]] rapidly expanded beyond the management capacity of a single research institution <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. By 2005, there were four research consortia:
*   ASET: Handled resist contamination control and multi-layer mirror masks <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   EUVA (Extreme Ultraviolet Lithography System Development Association): Handled the exposure tool's light source and some optics <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   Leading Project: Managed inter-university collaboration on light sources <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   Mirai: Handled mask defect control detection subsystems <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

This "complicated setup" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a> contrasted sharply with the American EUV project, which had a single entity, EUV LLC, overseeing early commercialization <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

## [[technical_and_engineering_aspects_of_high_na_euv | Technical and Engineering Aspects]]
While [[the_evolution_of_euv_lithography | EUV lithography machines]] shared a philosophical heritage with predecessors, the actual [[technical_and_engineering_aspects_of_high_na_euv | engineering required brand new, substantial work]] <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Resources were limited <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Exposure Tool Challenges
ASET focused its limited resources on optics manufacturing, including adding mirror reflective multi-layers and cleaning them, as well as metrology <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This meant they couldn't work on the exposure tool's light source, an essential piece, which was reassigned to the EUVA <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

EUVA researched two possible approaches to producing EUV light:
1.  **Laser-produced plasma (LPP)**: Firing a laser at a material to turn it into plasma, which emits EUV light. This was the approach ASML eventually chose <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
2.  **Discharge-produced plasma (DPP)**: Creating a material cloud and firing high-powered sparks between electrodes to create light-emitting plasma <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

The DPP approach, used in Nikon's EUV-1, was said to be more [[advancements_in_euv_power_efficiency | power efficient]], physically smaller, and supposedly cleaner than LPP <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. However, it struggled to output sufficient power <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. The EUV-1's light source power topped out at about 100 Watts, far short of the eventual goal of 250 Watts for high-volume production <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. This low power output meant longer exposure times and slower throughput <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. ASML also tried DPP but halted work in 2013, as sufficient power levels were not reached until their laser double shot method <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

### Photoresist Challenges
The major challenge with [[euv_and_duv_technologies_in_semiconductor_manufacturing | EUV photoresist]] was the high absorbability of EUV light by traditional resist materials <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. EUV light could only penetrate about 700 angstroms, far short of the 4,000 angstrom depth traditionally used <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This required developing new "thin layer imaging" (TLI) technologies <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Mask Challenges
ASET needed new subsystems for producing mirror mask blanks, adding patterns, and cleaning surfaces <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. A critical difficulty was consistently producing defect-free photo masks due to the "incredible tolerances involved" <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. The threshold for a defect was a deviance of just a few nanometers <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. Furthermore, traditional DUV light could not penetrate deep enough into the blank's mirror layer for inspection, requiring EUV light itself (actinic light) for inspection <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

### Contamination Issues
Nikon's EUV-1 struggled significantly with contamination control <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>. EUV light continually hitting the mirror's surface created carbon contamination, deteriorating the mirror's reflectiveness <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>. While introducing pure oxygen and using UV dry cleaning helped with carbon, the team then struggled with a mysterious contamination from a silicon carbon compound called cyloxane <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. In 2011, Nikon researchers were still trying to overcome these widespread contamination issues <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

## [[economic_impact_and_cost_considerations_of_euv_technology | Economic Impact and Cost Considerations]]
Japan's ambitious schedule for EUV development, aiming for high-volume [[euv_lithography_technology_and_its_challenges | EUV lithography]] by 2010 for the 45-nanometer process node <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>, was difficult to meet. Nikon's EUV-1 was completed and installed in January 2008 <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>, about 1.5 years behind ASML's Alpha demo tool delivered in 2006 <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

The delay of the EUV-1 pushed the high-volume ship schedule back to the 32-nanometer node, and even discussion of 28 and 22 nanometer nodes, requiring even more EUV machine power <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

The [[economic_impact_and_cost_considerations_of_euv_technology | global financial crisis]] severely impacted companies like Canon, with profits shrinking over 60% <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. Lithography R&D expenses were high (over $600 million annually in 2008), leading Canon to cut back and eventually halt its [[the_evolution_of_euv_lithography | EUV development]] <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

By 2011, it was clear that ASML had pulled ahead with a lead of 18 months to two years <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. The financial crisis also caused Nikon to cut R&D budgets in 2009 <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. A major blow came in July 2012 when Intel, Nikon's second-biggest customer, announced an investment of up to $4 billion into ASML <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. This signaled Intel's decision to move forward with ASML alone, leading Nikon to quietly cease its EUV efforts, as it was not economically viable without a cornerstone customer like Intel <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.

The total cost of Japan's EUV effort from 1999 to 2012 is estimated to be between $5 to $10 billion <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>. For context, the VLSI project that remade Japan's semiconductor industry in the late 1970s cost about $150 million <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>, highlighting the exponential jump in development costs. It is estimated that building an independent EUV machine today would require at least $5 to $10 billion, direct guidance from European and American EUV makers, and 10 to 15 years <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.