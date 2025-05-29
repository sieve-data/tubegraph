---
title: Challenges and advancements in photomask manufacturing
videoId: HxyM2Chu9Vc
---

From: [[asianometry]] <br/> 

Photomasks are a crucial component in [[Challenges in Semiconductor Lithography | lithography]], serving as the medium through which a chip design is transferred onto a resist-coated wafer <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Powerful light waves are projected through or off the mask to transfer the design at high volume <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Evolution of Mask Design

### Optical Proximity Correction (OPC)
[[Advancements in semiconductor technology | Advancements]] in computational lithography, particularly through techniques like Optical Proximity Correction (OPC), have significantly enhanced the printability of chip designs <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a> <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. OPC involves making modifications to the chip design layout on the quartz photomask to compensate for optical distortions <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. The goal is to "mis-print" the design on the mask so that, after light passes through it, it prints correctly on the wafer <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

Early OPC methods, introduced in the mid-1990s, were "rules-based" and relied on simple geometric rules, such as adding tickmarks (like serifs) to design lines to make them easier to print <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a> <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a> <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. These were useful for higher layers of the IC, like the metal interconnects, where feature sizes were larger <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

As feature sizes continued to shrink, "model-based OPC" emerged <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a> <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This approach uses extensive computational lithography simulations to correct the entire layout before it goes to the fab <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The process involves breaking down the chip design into segments, sampling within those segments, simulating the light's journey, and iteratively making corrections to the mask design <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a> <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. While very accurate, model-based OPC can be slow due to its computational intensity and iterative nature <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Inverse Lithography Technology (ILT)
Proposed in 1981 by Professor B.E.A. Saleh, Inverse Lithography Technology (ILT) is another Resolution Enhancement Technique aimed at improving the resolution of chip design image transfer <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a> <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a> <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Unlike OPC, which starts with a design and modifies the mask, ILT conceptually works backward from the desired pattern on the wafer to design the optimal mask <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a> <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. ILT constructs the mask from scratch, pixel by pixel, based on the desired wafer pattern and the known behavior of light in the lithography machine <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a> <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This "inverse" approach is a key differentiator <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

Early ILT methods used techniques like "simulated annealing" to optimize mask designs by iteratively changing pixels and keeping what works <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a> <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. Luminescent Technologies popularized ILT in 2003, and Intel also developed its own version, which they called "pixelated mask technology" <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a> <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a> <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a> <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

Masks generated with ILT are highly accurate, offer greater fidelity to the desired pattern, and provide more room for process error compared to model-based OPC <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. However, the resulting ILT mask patterns can appear unintuitive or like "horrific mutations" of the original design <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

## [[Challenges in Semiconductor Lithography | Challenges]] in Photomask Manufacturing

### Computational Power and Throughput
Both model-based OPC and ILT present significant [[Challenges in Semiconductor Lithography | challenges]] related to computational power and throughput.
*   Model-based OPC runtimes became longer as chip designs grew more complicated, interfering with development cycles <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   ILT, by accounting for every pixel, requires a lot of computing power or time, with some designs taking weeks to process <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a> <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a> <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

The increasing complexity of modern chips, such as Nvidia's Hopper with 80 billion transistors, translates to trillions of polygons on a single chip, further exacerbating these computational demands <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a> <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a> <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a> <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

### Mask Writing and Curvilinear Masks
Photomasks are "written" using focused electron beams, a process that is slow but precise <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
Most masks traditionally use "Manhattan geometry," composed of many rectangles <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. However, masks generated with ILT tend to have "curvilinear" or free-form shapes with complicated curves and diagonals <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a> <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Producing these curvilinear masks with traditional technologies was challenging, requiring "fracturing" complex shapes into rectangles <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a> <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

These manufacturing and computational [[Challenges in Semiconductor Lithography | challenges]] were significant hurdles for ILT's widespread adoption in the late 2000s and early 2010s, leading companies like Luminescent Technologies to struggle and eventually be acquired <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a> <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a> <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

## [[Advancements in semiconductor technology | Advancements]] and the Future of Mask Manufacturing

### Improved Mask Writing Tools
Over time, mask writing tools have improved <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. New multi-beam tools, such as those from Austria-based IMS, now make it possible to produce the complex shapes of curvilinear masks in a reasonable time <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a> <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### CuLitho: Accelerating Computational Lithography
The increasing demands of leading-edge chips have incentivized fabs to use ILT more frequently and to seek ways to make it faster <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a> <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. Nvidia, in collaboration with TSMC, developed CuLitho, a new software library announced in March 2023 <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a> <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

CuLitho is a collection of parallel algorithms invented by Nvidia scientists for accelerated primitive operations of OPC <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. It leverages GPUs to process these algorithms significantly faster—sometimes hundreds of times faster—than CPUs <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a> <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Nvidia claims CuLitho can deliver a performance leap of up to 40x beyond current lithography <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This speedup in component processes leads to an overall 23-42 times faster end-to-end computational lithography system <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a> <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Essentially, CuLitho is GPU-optimized software designed to quickly run computational lithography processes <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

This [[Technological advances in lithography tools by ASML | technological advancement]] addresses the critical computational [[Challenges in Semiconductor Lithography | challenges]] of mask design, particularly for ILT, allowing fabs to generate proper masks without excessive processing times <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a> <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### Source Mask Optimization (SMO)
Beyond OPC and ILT, other functionalities like Source Mask Optimization (SMO) are part of the broader field of computational lithography <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. SMO involves optimizing both the mask pattern and the illuminating light source behind the mask to achieve the best results <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

Computational lithography and [[Advancements in semiconductor technology | advancements]] in mask manufacturing directly impact the ability to print ever-smaller features on chips, contributing to the development of faster computers using computers <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a> <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a> <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.