---
title: Challenges in integrating photonics with silicon technology
videoId: 29aTqLvRia8
---

From: [[asianometry]] <br/> 

[[overview_of_silicon_photonics | Silicon photonics]] aims to combine the principles of photonics (the transmission and manipulation of light) with the established processes of silicon manufacturing <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The ultimate goal is to create a monolithic silicon chip where all components are made from a single material system, capable of transmitting and manipulating light <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Core Technical Challenges

Integrating photonics onto silicon faces two significant technical hurdles:

*   **Silicon's Inability to Emit Light**
    Silicon, in its crystalline form, possesses an "indirect band gap" <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. This property prevents it from naturally emitting light and means it cannot "lase" <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. While researchers have modified silicon to create efficient room-temperature silicon-based LEDs by implanting boron <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>, commercial silicon-based lasers are not yet available <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. A silicon-based laser is considered the "holy grail" for [[future_prospects_and_innovations_in_the_field_of_silicon_photonics | silicon photonics]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Lack of Pockels Effect in Silicon**
    Silicon's crystal structure does not exhibit the Pockels effect, which allows an electric field to control the speed of light through an object by changing its refractive index <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Without this effect, it is difficult to convert continuous laser light into a digital signal using electrical fields, hindering the creation of an effective modulator <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

These two issues make it challenging to produce a fully integrated photonics device out of pure silicon using standard CMOS manufacturing methods <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Workarounds and Advancements

Early optics researchers focused on other materials like gallium arsenide and indium phosphide for light emission <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. For [[overview_of_silicon_photonics | silicon photonics]], workarounds have been developed:

*   **External Lasers**: Using a laser positioned outside the chip itself, which also helps prevent the chip from overheating <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Hybrid Integration**: Bonding a pre-made laser from a different material, such as indium phosphide, onto the silicon chip <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Most commercial [[current_applications_and_market_potential_of_silicon_photonics | silicon photonics]] providers currently utilize one of these two methods <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Modulator Breakthroughs**:
    *   In 2004, Intel announced the first silicon-based high-speed optical modulator with bandwidth over 1 gigahertz, utilizing a Mach-Zehnder interferometer (MZI) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   In 2012, Intel further announced a fully integrated CMOS [[overview_of_silicon_photonics | silicon photonics]] transceiver with four channels, each at 25 gigabit per second, fabricated with a 90-nanometer process and using a more compact ring modulator <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## Manufacturing and Market Challenges

### Specialty Node Manufacturing

[[overview_of_silicon_photonics | Silicon photonics]] products typically use Silicon-on-Insulator (SOI) wafers, which include special layers (often silicon dioxide) that help confine light <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. This requires a slightly different fabrication process, placing it a few years behind the leading-edge processes <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This makes it a "specialty node," offering opportunities for foundries not competing at the most advanced nanometer scales <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Limited Market Volume and Commercialization

Despite advancements, [[overview_of_silicon_photonics | silicon photonics]] remains a technology "in search of a commercial market big and valuable enough to fulfill its potential" <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

*   **Current Market Size**: The largest market for [[overview_of_silicon_photonics | silicon photonics]] in the short term is transceivers for data centers <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. However, this market is relatively small in terms of wafer volume. Projections for 50-75 million transceiver units sold annually over the next few years translate to only about 40,000 to 60,000 200mm SOI wafers for the entire industry per year <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. This is less than a month's production for a typical mega-fab <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Size Disparity with Traditional CMOS**: While traditional transistors have feature sizes of only a few nanometers, photonic components cannot be made smaller than the wavelengths of the light they carry, typically topping out at about one micrometer <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. At the 7-nanometer node, one square micrometer can house over 100 transistors, indicating a very high opportunity cost for integrating photonic components on a chip <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. This pushes the industry towards packaging solutions that pair photonic and traditional chiplets together rather than fully integrated monolithic silicon photonics devices <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Comparison to MEMS**: Similar to the MEMS (Micro-Electro-Mechanical Systems) industry, where individual dies sell for cents and most of the value is in packaging, [[overview_of_silicon_photonics | silicon photonics]] risks stifled innovation and difficulty in commercialization if it doesn't find sufficiently large and valuable markets <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

## Industry Landscape

*   **GlobalFoundries**: Considered a market leader in [[overview_of_silicon_photonics | silicon photonics]], having acquired relevant IP from IBM's microelectronics division in 2014 <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
*   **Intel**: A long-time R&D pioneer in [[overview_of_silicon_photonics | silicon photonics]], with early breakthroughs in modulators and transceivers <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **TSMC**: Has not offered much in the [[overview_of_silicon_photonics | silicon photonics]] space directly <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. Their strategy seems to focus on building integration schemes that allow [[overview_of_silicon_photonics | silicon photonics]] chiplets to work seamlessly with traditional semiconductors <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>, likely due to the low volume of the current market <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

While [[overview_of_silicon_photonics | silicon photonics]] is a futuristic technology aiming to revolutionize data transmission by replacing electrical signals with light <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, its biggest [[challenges_in_the_semiconductor_industry | challenge]] is finding a large enough commercial market to fulfill its potential <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.