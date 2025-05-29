---
title: Computational lithography advancements
videoId: HxyM2Chu9Vc
---

From: [[asianometry]] <br/> 

In March 2023, Nvidia announced a new software library called "CuLitho" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Nvidia claims this computational lithography library can "deliver a performance leap of up to 40x beyond current lithography" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This breakthrough has garnered positive feedback from major industry players like [[development_and_history_of_asml_lithography_technology | ASML]] and TSMC <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Introducing CuLitho

Dr. Vivek K. Singh of Nvidia presented a session titled "Accelerating Computational Lithography: Enabling our Electronic Future" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Dr. Singh describes CuLitho as:
> CuLitho is a collection of parallel algorithms invented by Nvidia scientists for accelerated primitive operations of OPC <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

These algorithms, optimized using GPUs, have seen performance accelerations sometimes reaching hundreds of times faster than traditional methods <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. By integrating these GPU-accelerated algorithms into existing Optical Proximity Correction (OPC) Electronic Design Automation (EDA) software, CuLitho provides an overall end-to-end computational lithography system that is 23 to 42 times faster <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Essentially, CuLitho is GPU-optimized software designed to speed up computational lithography processes <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Lithography Fundamentals

Lithography is the process of transferring a chip design from a photomask onto a resist-coated wafer <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Since its inception, optical lithography has been employed, using powerful light waves to project designs at high volume <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

A critical challenge emerged in the late 1990s with the 180 nanometer process node, which used a 248 nanometer KrF DUV laser <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. For the first time, feature sizes being printed were smaller than the light wavelengths used <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This situation is problematic because any deterioration in resolution or image quality can lead to incorrect pattern transfer, causing errors in the chip <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Improving K1

To achieve the necessary resolutions with relatively large light wavelengths, engineers refer to Rayleigh's holy equation:
> Resolution = K1 * wavelength / Numerical Aperture or NA <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>

There are two primary options: raising Numerical Aperture (NA) or lowering K1 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Raising NA** involves collecting more light, as seen in immersion lithography and [[extreme_ultraviolet_lithography_and_its_challenges | High-NA EUV]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. However, this reduces the "depth of focus," the vertical distance where image quality remains acceptable <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. A thinner depth of focus can lead to blurring within the resist layer, necessitating thinner resist layers which can compromise subsequent etch processes <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. While pursued, raising NA has limits <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Lowering K1** is the other option <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. K1 represents contributions from the manufacturing process, including the resist, materials, and imaging techniques <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is where [[role_of_technology_and_innovation_in_lithography | computational lithography]] plays a crucial role, helping to significantly lower K1 over the years and pushing closer to its physical limit <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## The Rise of Computational Lithography

[[technological_advancements_in_semiconductor_manufacturing | Computational lithography]] began to take shape in the early 1970s with efforts to quantify the natural principles behind lithography, which was previously considered an artisan technique <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. Pioneers like IBM's Dr. Rick Dill developed computer models to simulate how resist-coated wafers react to light <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

By the early 1990s, with sufficient computing power, computational lithography became practical for real-world applications <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This allowed for the improvement of chip design printability through "Resolution Enhancement Techniques" (RETs) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Resolution Enhancement Techniques (RETs) and Optical Proximity Correction (OPC)

RETs are optical modifications applied to better transfer designs to the wafer <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Three significant RETs introduced over 25 years ago, crucial for the 180 nanometer node, were: Phase shifting masks, Off-axis illumination, and Optical Proximity Correction (OPC) <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

**Optical Proximity Correction (OPC)** involves making modifications to the chip design layout on the photomask to compensate for optical distortions <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. The idea is to deliberately "mis-print" the design on the photomask so that the light passing through it prints correctly on the wafer <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

*   **Rules-based OPC**: Introduced in the mid-1990s, these were simple geometric rules, like adding "tickmarks" (serifs) to design lines to make them easier to print <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Due to their simplicity, they were primarily used for higher layers of the IC, such as the metal layer <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Model-based OPC**: As feature sizes shrank, simple rules became insufficient <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Model-based OPC emerged, using extensive computational lithography simulations to correct the entire layout before fabrication <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This involves breaking down the chip design into segments, sampling within them, simulating the light's journey, and iteratively making corrections <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. While accurate, its reliance on intense computation makes it very slow, leading to long runtimes that can interfere with development cycles <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## [[inverse_lithography_technology_ilt | Inverse Lithography Technology (ILT)]]

In 1981, Professor B.E.A. Saleh proposed the concepts that would eventually become [[inverse_lithography_technology_ilt | Inverse Lithography Technology (ILT)]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Like OPC, ILT is an RET aimed at improving chip design image transfer <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

The key difference lies in the approach:
*   **OPC** starts with a design and makes slight changes to the mask based on simulations of light flowing from mask to wafer <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **ILT** conceptually works backward from the desired pattern on the wafer to design the optimal mask from scratch, pixel by pixel <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

Professor Saleh initially used a variant of "simulated annealing," an optimization technique where a randomly generated mask is iteratively improved by "flipping pixels" (making random changes and keeping what works) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Luminescent Technologies, a startup, gave ILT its current name in 2003 and heavily promoted it <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Intel also developed its own version, which it called "pixelated mask technology" <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. ILT results in highly unintuitive, often mutated mask designs, but they yield superior fidelity and greater process error tolerance <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

## Bottlenecks and Evolution

Despite its superior results, ILT faced substantial trade-offs:
1.  **Computational Power and Throughput**: Accounting for every pixel meant immense computing power or time was needed, with some designs taking weeks to process <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
2.  **Mask Manufacturing Challenges**: Traditional electron beam mask writing, slow but precise, was ill-suited for the complex, curvilinear masks generated by ILT <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. These "curvilinear masks" required challenging "fracturing" into rectangles for production <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

These issues proved "game-breaking" for early adopters like Luminescent Technologies in the late 2000s and early 2010s <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. The advent of 193 nanometer immersion lithography, which significantly improved resolutions, further reduced the immediate need for ILT over OPC <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Consequently, ILT adoption was limited, primarily reserved for special situations <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>, and Luminescent was eventually split up <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

## Changing Times and CuLitho's Impact

[[technological_advancements_in_semiconductor_manufacturing | Technological advancements]] eventually caught up. New multi-beam mask writing tools from companies like IMS made it feasible to produce complex curvilinear masks in a reasonable timeframe <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

However, the computational challenges remained, especially with the increasing complexity of leading-edge chips, such as Nvidia's Hopper, which contains 80 billion transistors <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This escalating demand has forced fabs to increase their use of ILT, creating an incentive to accelerate its processes <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

TSMC demonstrated intriguing simulation results suggesting that GPUs could significantly speed up ILT <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. Nvidia took on this challenge, leading to the development of CuLitho <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

## Conclusion

[[role_of_technology_and_innovation_in_lithography | Computational lithography]] techniques directly enable the printing of ever-smaller features on chips <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. Beyond OPC and ILT, the field encompasses other functionalities like Source Mask Optimization, which optimizes both the mask pattern and the illuminating light source for the best results <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. The recursive nature of using computers to facilitate the creation of even faster computers highlights the innovative cycle within the semiconductor industry <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The future impact and benefits of software libraries like CuLitho are keenly anticipated <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.