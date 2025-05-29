---
title: Computational Lithography and CuLitho
videoId: HxyM2Chu9Vc
---

From: [[asianometry]] <br/> 

In March 2023, Nvidia announced a new software library called "CuLitho" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Nvidia claims this computational lithography library can deliver a performance leap of up to 40x beyond current lithography methods <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The announcement garnered positive feedback from both ASML and TSMC <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Introducing CuLitho

During an Nvidia session titled "Accelerating Computational Lithography: Enabling our Electronic Future," Dr. Vivek K. Singh described CuLitho as "a collection of parallel algorithms invented by Nvidia scientists for accelerated primitive operations of OPC" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. These algorithms are integrated into traditional OPC EDA software <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. By leveraging GPUs' parallelism, CuLitho can process these algorithms significantly faster than CPUs, sometimes hundreds of times faster <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This acceleration of component processes leads to an overall faster end-to-end [[impact_of_gpu_acceleration_on_computational_lithography | computational lithography]] system, achieving a 23-42 times speedup, which is the source of the headline performance claim <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Essentially, CuLitho is GPU-optimized software designed to quickly run [[impact_of_gpu_acceleration_on_computational_lithography | computational lithography]] processes <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## What is Lithography?

Lithography is the process of transferring a chip design from a photomask onto a resist-coated wafer <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Since its inception, optical lithography has been used, which involves a multimillion-dollar camera projecting powerful light waves through or off a mask to transfer a design at high volume <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

Until the late 1990s, feature sizes printed in a process node were larger than the light wavelengths used <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This changed with the 180 nanometer node, which used the 248 nanometer KrF DUV laser <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. When feature sizes become this small, any deterioration in resolution or image quality can lead to incorrect pattern transfer and functional issues <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Improving K1

To achieve necessary resolutions with large wavelengths, the Rayleigh's equation for resolution is considered:
> Resolution = K1 * wavelength / Numerical Aperture (NA) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>

Options include raising NA or lowering K1 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Raising NA means collecting more light, a concept behind immersion lithography and High-NA [[euv_lithography_technology_and_its_challenges | EUV]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. However, increasing NA reduces the depth of focus (the vertical distance where image quality is acceptable), which is detrimental for IC development <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. A thinner depth of focus requires a thinner resist layer, potentially compromising subsequent etch processes <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. While raising NA is pursued, it has limitations <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

Therefore, the alternative is to lower K1 <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. K1 represents contributions from the manufacturing process, such as the resist, materials, and imaging techniques <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is where [[impact_of_gpu_acceleration_on_computational_lithography | computational lithography]] plays a crucial role, helping to significantly lower K1 over the years, pushing closer to its physical limit <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## Computational Lithography

In the early 1970s, efforts began to quantify the natural principles of lithography, which was previously considered an artisan technique <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. [[impact_of_industry_collaboration_and_research_on_lithography | Dr. Rick Dill of IBM]] and others developed computer models to simulate how a resist-coated wafer reacts to light <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. By the early 1990s, [[impact_of_gpu_acceleration_on_computational_lithography | computational lithography]] became useful for real-world applications, allowing for simulations of the light's journey through the optics system and photomask to predict the pattern on the wafer <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

This knowledge is leveraged to improve the printability of chip designs through tactics broadly known as Resolution Enhancement Techniques (RETs) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### RETs & OPCs

RETs are "optical tricks" used to better transfer designs to the wafer <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Three major RETs introduced over 25 years ago, including Phase shifting masks, Off-axis illumination, and Optical Proximity Correction (OPC), helped bridge the wavelength-feature size gap at the 180 nanometer node <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

**Optical Proximity Corrections (OPC)** involve modifying the chip design layout to compensate for optical distortions <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This means purposefully mis-printing the chip design onto the photomask so that the light passing through it prints correctly on the resist-coated wafer <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

Early OPCs, introduced in the mid-1990s, were "rules-based," relying on simple geometric rules like adding tickmarks (serifs) to design lines to make them easier to print <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. These simple rules were useful for higher layers like the metal interconnects <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### From Rules to Models

As feature sizes continued to shrink, "model-based OPC" emerged <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This advanced OPC type uses extensive [[impact_of_gpu_acceleration_on_computational_lithography | computational lithography]] simulations to correct the entire design layout before it goes to the fab <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The process involves breaking down the chip design into segments, sampling within them, simulating the light's journey, and iteratively correcting the mask design <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. While highly accurate, model-based OPC is computationally intensive and slow, leading to long runtimes that interfere with development cycles <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## [[inverse_lithography_technology_and_its_applications | Inverse Lithography Technology (ILT)]]

In 1981, Professor B.E.A. Saleh proposed the concepts that would become [[inverse_lithography_technology_and_its_applications | Inverse Lithography Technology (ILT)]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Like OPC, ILT is a Resolution Enhancement Technique aimed at improving chip design image transfer <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

Unlike traditional OPC, which flows from mask to wafer, ILT conceptually works backward from the desired pattern on the wafer to generate the best mask design from scratch, pixel by pixel <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Professor Saleh initially used a variant of "simulated annealing," a statistical optimization technique, to achieve this <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Researchers at Berkeley, [[impact_of_industry_collaboration_and_research_on_lithography | IBM]], and other organizations refined the technique <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. In 2003, Luminescent Technologies popularized ILT with their paper "Fast Inverse Lithography Technology" <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. [[impact_of_industry_collaboration_and_research_on_lithography | Intel]] also funded academic research in the field since the 1990s and presented its own "pixelated mask technology" version in 2007 <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

ILT produces highly accurate masks with greater fidelity and process error margin compared to model-based OPC <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. However, ILT results are often counter-intuitive, appearing as "horrific mutations" of the original design <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

### Bottlenecks

Despite its superior results, ILT faced significant [[challenges_in_semiconductor_lithography | challenges]] and tradeoffs:
*   **Computational Power**: Accounting for every pixel requires immense computing power or time; some designs could take weeks to process <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **Mask Manufacturing**: ILT-generated masks often have complex, curvilinear shapes, unlike the Manhattan geometry (rectangles) of traditional masks <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Producing these "curvilinear masks" with traditional electron beam tools was challenging, as it required fracturing complex shapes into rectangles <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

These manufacturing and computational issues prevented widespread adoption of ILT in the late 2000s and early 2010s <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. For instance, Luminescent's push for ILT at the 45 nanometer and 32 nanometer nodes was superseded by the improvements in 193 nanometer immersion lithography, which reduced the need for ILT over OPC <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. While some EDA vendors incorporated ILT, it was primarily reserved for special situations <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Luminescent itself was split up in 2012, with parts acquired by KLA and Synopsys <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

## Changing Times

Over time, advancements have addressed some of these [[challenges_in_semiconductor_lithography | challenges]] <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. Mask writing tools improved, with new multi-beam tools from companies like Austria-based IMS making it possible to produce complex curvilinear masks in a reasonable time <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

However, the computational [[challenges_in_semiconductor_lithography | challenges]] remained, especially with the increasing complexity of leading-edge chips <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. Modern chips like Hopper GPUs can have 80 billion transistors, translating to trillions of polygons <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This demand has pushed fabs to use ILT more frequently, incentivizing efforts to accelerate it <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. Dr. Singh noted how [[impact_of_industry_collaboration_and_research_on_lithography | TSMC presented intriguing simulation results hinting at GPUs' ability to speed up ILT]] <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. Nvidia accepted the challenge, leading to the development of CuLitho <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

## Conclusion

[[impact_of_gpu_acceleration_on_computational_lithography | Computational lithography]] techniques like CuLitho directly impact the ability to print ever-smaller features on chips <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. The field encompasses many other functionalities, such as Source Mask Optimization, which optimizes both the mask pattern and the illuminating light source for optimal results <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. The symbiotic relationship where computers are used to create chips for faster computers highlights the self-referential nature of this technological advancement <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.