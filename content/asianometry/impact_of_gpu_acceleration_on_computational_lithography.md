---
title: Impact of GPU acceleration on computational lithography
videoId: HxyM2Chu9Vc
---

From: [[asianometry]] <br/> 
## Impact of GPU Acceleration on Computational Lithography

In March 2023, Nvidia unveiled a new software library known as [[computational_lithography_and_culitho | CuLitho]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Nvidia asserts that this [[computational_lithography_and_culitho | computational lithography]] library can deliver a performance increase of up to 40 times beyond existing lithography processes <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The announcement garnered positive feedback from industry leaders such as ASML and TSMC <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Understanding CuLitho

[[computational_lithography_and_culitho | CuLitho]] was introduced by Dr. Vivek K. Singh during an Nvidia session titled "Accelerating Computational Lithography: Enabling our Electronic Future" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Dr. Singh describes [[computational_lithography_and_culitho | CuLitho]] as:
> CuLitho is a collection of parallel algorithms invented by Nvidia scientists for accelerated primitive operations of OPC <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

These algorithms have shown performance accelerations, sometimes by hundreds of times, through the use of GPUs <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Integrated into traditional Optical Proximity Correction (OPC) Electronic Design Automation (EDA) software, GPUs can process these algorithms significantly faster than CPUs due to their parallel processing capabilities <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This acceleration of component processes results in an overall end-to-end [[computational_lithography_and_culitho | computational lithography]] system that is 23 to 42 times faster <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Essentially, [[computational_lithography_and_culitho | CuLitho]] is GPU-optimized software designed to expedite [[computational_lithography_and_culitho | computational lithography]] processes <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### The Role of Computational Lithography

[[computational_lithography_and_culitho | Computational lithography]] is crucial for achieving the necessary resolutions in semiconductor manufacturing <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. It plays a significant role in lowering the K1 factor in Rayleigh's equation (Resolution = K1 * wavelength / Numerical Aperture), which is vital as feature sizes continue to shrink below light wavelengths <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. By simulating the lithography process, [[computational_lithography_and_culitho | computational lithography]] enables the use of Resolution Enhancement Techniques (RETs) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

One prominent RET is Optical Proximity Correction (OPC), which involves modifying the chip design layout on the photomask to compensate for optical distortions and ensure correct printing on the wafer <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. As feature sizes became smaller, simple "rules-based" OPC evolved into "model-based OPC" <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Model-based OPC uses extensive [[computational_lithography_and_culitho | computational lithography]] simulations to correct the entire layout <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. However, its reliance on intense computation and iterative processes can make it very slow <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Inverse Lithography Technology (ILT) and Computational Bottlenecks

A more advanced RET is [[inverse_lithography_technology_and_its_applications | Inverse Lithography Technology]] (ILT), first proposed in 1981 <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Unlike traditional OPC, ILT works conceptually backward from the desired pattern on the wafer to design the optimal mask pixel by pixel <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. ILT produces more accurate masks with greater fidelity to the desired pattern and offers more room for process error compared to model-based OPC <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

Despite its advantages, ILT faces significant [[challenges_in_semiconductor_lithography | challenges]] due to its computational intensity <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. Accounting for every pixel in a chip design requires substantial computing power or time, with some designs potentially taking weeks to process, which is unacceptable in modern development cycles <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Additionally, ILT often generates curvilinear masks (complicated curves and diagonals) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>, which were challenging to manufacture with traditional mask writing technologies <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

In the late 2000s and early 2010s, manufacturability, computation, and competition were "game-breaking issues" for ILT <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, making it "a bit too early for its time" <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

### The Rise of GPU Acceleration

Times have changed, and mask writing tools have improved, with new multi-beam tools enabling the production of complex curvilinear masks in a reasonable timeframe <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. However, the computational [[challenges_in_semiconductor_lithography | challenges]] remained <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. Modern leading-edge chips, like Nvidia's Hopper with 80 billion transistors, require trillions of polygons, making the computational demands for generating proper masks increasingly daunting <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

These increasing demands have compelled fabs to adopt ILT more frequently, which in turn incentivized them to find ways to accelerate ILT processes <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. TSMC presented intriguing simulation results hinting at how GPUs could speed up ILT <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. Nvidia took up this challenge, leading to the development of [[computational_lithography_and_culitho | CuLitho]] <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

GPU acceleration, through [[computational_lithography_and_culitho | CuLitho]], has a direct [[impact_of_industry_collaboration_and_research_on_lithography | impact]] on the ability to print ever smaller features <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This enables faster and more efficient [[computational_lithography_and_culitho | computational lithography]] processes, facilitating the production of increasingly complex chips <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.