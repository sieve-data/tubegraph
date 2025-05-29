---
title: Optical proximity correction OPC techniques
videoId: HxyM2Chu9Vc
---

From: [[asianometry]] <br/> 

In March 2023, Nvidia announced a new software library called "CuLitho" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Nvidia claims this [[computational_lithography_advancements | computational lithography]] library can "deliver a performance leap of up to 40x beyond current lithography" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The technology has garnered positive remarks from both [[asml_lithography_machine_operation_and_precision | ASML]] and [[tsmcs_technological_advancements | TSMC]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. CuLitho is described as a collection of parallel algorithms invented by Nvidia scientists for accelerated primitive operations of OPC <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. These GPU-accelerated algorithms are integrated into traditional OPC EDA software, leading to a 23-42 times faster end-to-end [[computational_lithography_advancements | computational lithography]] system <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Lithography Fundamentals

Lithography involves transferring a chip design from a photomask onto a resist-coated wafer <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Since its inception, optical lithography has been used, acting like a multimillion-dollar camera projecting light waves through or off the mask to transfer a design <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

Until the late 1990s, the feature sizes printed were larger than the light wavelengths used <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This changed with the 180 nanometer node, which used a 248 nanometer KrF DUV laser <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. When feature sizes become this small, any deterioration in resolution or image quality can lead to incorrect pattern transfer and functional issues <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Improving K1 Factor for Resolution

To achieve necessary resolutions with large wavelengths, the industry refers to Rayleigh's equation: Resolution = K1 * wavelength / Numerical Aperture (NA) <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Options include raising NA or lowering K1 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

Raising NA means collecting more light, as seen in immersion lithography and [[innovations_in_optical_systems_for_high_na_euv | High-NA EUV]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. However, it also leads to a thinner depth of focus, which is undesirable for IC development as it can cause image blur at certain resist depths, potentially compromising the subsequent etch process <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. While raising NA is pursued, it has limitations <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

Therefore, lowering K1 becomes crucial <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. K1 represents the contribution from the manufacturing process, including the resist, materials, and imaging techniques <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is where [[computational_lithography_advancements | computational lithography]] plays a vital role, significantly helping to lower K1 over the years <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## The Rise of Computational Lithography

Beginning in the early 1970s, efforts were made to quantify the natural principles behind lithography, previously seen as an artisan technique <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. IBM's Dr. Rick Dill and others developed computer models to simulate how a resist-coated wafer reacts to light <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. By the early 1990s, [[computational_lithography_advancements | computational lithography]] became useful for real-world applications, leveraging simulations of light passing through the optical system, photomask, and onto the wafer <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This knowledge is used to improve the printability of chip designs through tactics broadly called [[resolution_enhancement_techniques_rets | Resolution Enhancement Techniques]] (RETs) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Resolution Enhancement Techniques (RETs) and OPC

[[resolution_enhancement_techniques_rets | RETs]] are optical strategies used to better transfer designs to the wafer, involving the entire optical system <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Three major [[resolution_enhancement_techniques_rets | RETs]] introduced over 25 years ago, including Phase Shifting Masks, Off-Axis Illumination, and Optical Proximity Correction (OPC), helped bridge the wavelength-feature size gap at the 180 nanometer node <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Optical Proximity Correction (OPC)

OPC involves modifications made to the chip design layout to compensate for optical distortions <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. The core idea is to intentionally "mis-print" the chip design onto the quartz photomask so that after light passes through, it prints correctly on the resist-coated wafer <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

#### Rules-Based OPC

The first OPCs, introduced in the mid-1990s, were based on simple geometric rules <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. An example is adding "tickmarks" at the end of design lines, similar to serifs in fonts, to make the design line easier to print <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. These "rules-based" OPCs were simple to check during the "Design Rule Checking" stage <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a> but were not effective for smaller features further down the silicon, thus primarily used for higher-up layers like the metal interconnect <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

#### Model-Based OPC

As feature sizes continued to shrink, simple rules became insufficient <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. A new type, "model-based OPC," emerged <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This approach uses extensive [[computational_lithography_advancements | computational lithography]] simulations to correct the entire layout before it goes to the fab <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

After a design is finalized (e.g., in a GDSII file), it's run through OPC semiconductor design software <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Since simulating the entire chip design simultaneously is impossible, the program breaks down design polygons into segments and samples points within them <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. It then simulates the light's journey through these sampled mask segments and the resist's reaction <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. The program iteratively makes corrections to optimize the mask design <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

Model-based OPC is highly accurate but can be very slow due to its reliance on intense computation and iteration <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Because it only samples certain areas, physical verification is still needed after OPC <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. These long runtimes grew longer as chip designs became more complex, interfering with development cycles <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## Inverse Lithography Technology (ILT)

In 1981, Professor B.E.A. Saleh proposed the concepts that would become Inverse Lithography Technology (ILT) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Like OPC, ILT is a [[resolution_enhancement_techniques_rets | Resolution Enhancement Technique]] aimed at improving chip design image transfer resolution <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### ILT Approach vs. OPC

Traditional OPC flows from the mask to the wafer, making slight changes to an initial design <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. ILT, conceptually, goes the other way: from the wafer to the mask <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. It starts with the desired pattern on the wafer and works backward to determine the best mask design, pixel by pixel, taking into account how light interacts with the lithography machine and resist <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. This "inverse" approach is the key differentiator <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

### Development and Characteristics of ILT

Professor Saleh first used a variant of "simulated annealing," a statistical optimization technique, creating a randomly generated mask and iteratively making random changes ("flipping pixels") to discover a local optimum <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Researchers refined the technique, and in 2003, Luminescent Technologies popularized ILT with their paper "Fast Inverse Lithography Technology" <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Intel also funded academic research and presented its own version in 2007, calling it "pixelated mask technology" <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

ILT results in masks with highly unintuitive, often curvilinear shapes, unlike the Manhattan geometry (rectangles) of most traditional masks <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Despite their odd appearance, these masks tend to be more accurate, have greater fidelity to the desired pattern, and offer more room for process error compared to model-based OPC <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Bottlenecks and Changing Times for ILT

ILT faces substantial tradeoffs, primarily computational power and throughput <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. Accounting for every pixel provides an optimal solution but requires immense computing power or time, with some designs taking weeks to process <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

Another challenge is manufacturing the masks themselves <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Photomasks are written using focused electron beams, a slow but precise process <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Producing complex curvilinear masks generated by ILT traditionally meant "fracturing" the shapes into rectangles, which was difficult <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

These manufacturing and computational issues, along with competition from 193 nanometer immersion lithography (which improved resolutions significantly), made ILT "too early for its time" in the late 2000s and early 2010s <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. While some EDA vendors adopted ILT, it was reserved for special situations <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Luminescent was eventually split up in 2012 <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

However, times have changed <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. Mask writing tools have improved, with new multi-beam tools from companies like IMS making it possible to produce complex curvilinear masks in a reasonable time <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. The computational challenges remained, but the increasing complexity of leading-edge chips, such as Hopper with 80 billion transistors, has forced fabs to use ILT more <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This incentivized finding ways to make ILT faster <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. [[tsmcs_technological_advancements | TSMC]] presented intriguing simulation results hinting at GPU acceleration for ILT, leading Nvidia to develop CuLitho to turn these simulations into reality <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

Techniques like [[computational_lithography_advancements | computational lithography]], including OPC and ILT, directly impact the ability to print ever smaller features <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. The field is extensive, with other functionalities like Source Mask Optimization, which optimizes both the mask pattern and the illuminating light source for the best results <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.