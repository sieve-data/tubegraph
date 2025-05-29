---
title: Optical Proximity Correction and Resolution Enhancement Techniques
videoId: HxyM2Chu9Vc
---

From: [[asianometry]] <br/> 

[[Computational photography techniques | Computational lithography]] is a critical field that directly impacts the ability to print ever-smaller features on chips <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. Its techniques help lower the K1 factor in Rayleigh's equation, which is crucial for achieving necessary resolutions when feature sizes are smaller than light wavelengths <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>, <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This became a challenge starting with the 180 nanometer node generation, which used the 248 nanometer KrF DUV laser <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Resolution Enhancement Techniques (RETs)

[[Computational photography techniques | Computational lithography]] involves creating computer models to simulate how light interacts with a resist-coated wafer after passing through an optics system and a photomask <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>, <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. This knowledge is leveraged to improve the printability of chip designs through strategies broadly known as Resolution Enhancement Techniques, or RETs <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>, <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

RETs are essentially optical modifications applied to better transfer designs to the wafer <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. These are not minor adjustments but involve the entire optical system <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

Three significant RETs introduced over 25 years ago, at the 180 nanometer node, helped bridge the gap between wavelength and feature size:
*   Phase shifting masks <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>
*   Off-axis illumination <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>
*   Optical Proximity Correction (OPC) <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>

## Optical Proximity Correction (OPC)

Optical Proximity Correction (OPC) involves making modifications to the chip design layout to compensate for optical distortions <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. The goal is to intentionally mis-print the chip design onto the quartz photomask so that, after light passes through it, the pattern prints correctly on the resist-coated wafer <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Rules-Based OPC

The earliest OPCs, introduced in the mid-1990s, were based on simple geometric rules <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. An example is adding "tickmarks" at the end of design lines, similar to serifs in fonts, to make the line easier to print <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>, <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. These simple rules streamlined checks during the "Design Rule Checking" stage <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. However, their simplicity limited their usefulness for lower layers of the silicon, so they were primarily used for the metal layer (interconnects) higher up in the integrated circuit <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Model-Based OPC

As feature sizes continued to shrink, simple rules became insufficient <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This led to the development of "model-based OPC," which utilizes extensive [[computational_photography_techniques | computational lithography]] simulations to correct the entire layout before it goes to the fabrication plant <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

The process involves:
1.  Taking the GDSII file (the finished chip design) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>, <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
2.  Running it through OPC semiconductor design software <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
3.  Since simulating the entire chip design at once is impossible, the program breaks down the design's polygons into segments and takes samples within those segments <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
4.  It then simulates the light's journey through the sampled mask segments and how the resist reacts <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
5.  The program iteratively makes corrections to optimize the mask design <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

While model-based OPC is highly accurate, its reliance on intense computation and iteration can make it very slow <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Additionally, because it only samples certain areas, physical verification is still needed after OPC <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. These long runtimes became a bottleneck as chip designs grew more complex, interfering with development cycles <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## Inverse Lithography Technology (ILT)

Inverse Lithography Technology (ILT) is another Resolution Enhancement Technique, first proposed by Professor B.E.A. Saleh in 1981 <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>, <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Its goal is also to improve the resolution of the chip design image transfer <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### Approach

Unlike traditional OPC, which starts with a design and simulates changes from mask to wafer, ILT conceptually works backward, from the wafer to the mask <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>, <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. The user specifies the desired pattern on the wafer, and ILT determines the best mask design to achieve that pattern, considering how light travels through the lithography machine and interacts with the resist <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. ILT then creates the entire mask from scratch, pixel by pixel <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This "inverse" approach is the key difference from model-based OPC <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

### Development and Characteristics

Professor Saleh initially used a variant of "simulated annealing," an optimization technique <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This involved creating a randomly generated mask, making random pixel changes ("flipping pixels"), and keeping what worked <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>, <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. Researchers at Berkeley, IBM, and other organizations refined the technique <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

In 2003, Luminescent Technologies popularized ILT with their paper "Fast Inverse Lithography Technology" <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>, <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Intel also developed its own version, which it called pixelated mask technology, after funding academic research in the field since the 1990s <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>, <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>, <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. ILT results in mask patterns that are often counter-intuitive and complex, sometimes described as "horrific mutations" of the original design, but they yield superior outcomes <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>, <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Tradeoffs and Challenges

While ILT tends to produce more accurate masks with greater fidelity and more process error room compared to model-based OPC, it comes with significant tradeoffs <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>, <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>, <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

1.  **Computational Power and Throughput**: Accounting for every pixel provides an optimal solution but demands immense computing power or time, with some designs taking weeks to process <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>, <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
2.  **Mask Manufacturing**: Traditional photomasks use "Manhattan geometry" (shapes made of rectangles) <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. ILT-generated masks often have curvilinear shapes (complicated curves and diagonals) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Producing these curvilinear masks with traditional technologies required "fracturing" complex shapes into rectangles, which was challenging <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

These issues of manufacturability, computation, and competition were "game-breaking" for early ILT proponents like Luminescent in the late 2000s and early 2010s <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. ILT was considered ahead of its time <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The advent of 193 nanometer immersion lithography improved resolutions to an extent that manufacturers did not widely adopt ILT over OPC at the 45nm and 32nm nodes <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>, <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>, <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. While some EDA vendors adopted ILT for special situations, it wasn't broadly used <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Luminescent was eventually split up and acquired in 2012 <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

### Recent Advancements

Over time, mask writing tools have improved, with new multi-beam tools enabling the production of complex curvilinear masks in a reasonable time <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>, <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. However, the computational challenges remained <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. Modern leading-edge chips, like Nvidia's Hopper with 80 billion transistors, require processing trillions of polygons, making the demands on [[computational_photography_techniques | computational lithography]] immense <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>, <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>, <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

These increasing demands have compelled fabs to use ILT more frequently, incentivizing efforts to speed it up <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>, <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. TSMC presented simulation results hinting that GPUs could accelerate ILT <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>, <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Nvidia took on this challenge, resulting in CuLitho, a GPU-optimized software library designed to accelerate [[computational_photography_techniques | computational lithography]] processes, including OPC <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. Nvidia claims CuLitho can deliver a performance leap of up to 40x beyond current lithography methods <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Other Related Techniques

Beyond OPC and ILT, the field of [[computational_photography_techniques | computational lithography]] includes other functionalities, such as Source Mask Optimization (SMO). SMO involves optimizing both the mask pattern and the illuminating light source behind the mask to achieve the best printing results <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>, <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. The continuous development in [[computational_photography_techniques | computational lithography]] allows for the creation of chips that, in turn, enable faster computers <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.