---
title: Resolution enhancement techniques RETs
videoId: HxyM2Chu9Vc
---

From: [[asianometry]] <br/> 

[[computational_lithography_advancements | Computational lithography]] plays a crucial role in improving the printability of chip designs, largely through tactics broadly called "Resolution Enhancement Techniques" or RETs <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. These techniques are essentially optical tricks employed to better transfer designs onto the wafer <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

## Historical Context
Up until the late 1990s, the feature sizes printed in a process node were larger than the light wavelengths used <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. This changed with the 180 nanometer node generation, which used the 248 nanometer KrF DUV laser <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. When feature sizes became this small, any deterioration in resolution and image quality could cause patterns to be incorrectly transferred, leading to malfunctions <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

To achieve necessary resolutions with large wavelengths, engineers turned to improving the K1 factor in Rayleigh's equation (Resolution = K1 * wavelength / Numerical Aperture) <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. While raising the Numerical Aperture (NA) is an option, it leads to a thinner depth of focus, which is detrimental for IC development <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Lowering K1, which represents contributions from the manufacturing process, materials, and imaging techniques, became a key strategy <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. This is where [[computational_lithography_advancements | computational lithography]] and RETs help, by lowering K1 significantly over the years <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

## Key RETs
Three major RETs introduced over 25 years ago helped bridge the wavelength-feature size gap at the 180 nanometer node <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>:
*   Phase shifting masks
*   Off-axis illumination
*   [[optical_proximity_correction_opc_techniques | Optical Proximity Correction]] (OPC)

### [[optical_proximity_correction_opc_techniques | Optical Proximity Correction]] (OPC)
[[optical_proximity_correction_opc_techniques | Optical Proximity Corrections]] are modifications made to the chip design layout to compensate for optical distortions <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>. The goal is to deliberately "mis-print" the chip design onto the photomask so that the light passing through it prints correctly on the resist-coated wafer <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

#### Evolution of OPC
1.  **Rules-based OPC**: Introduced in the mid-1990s, these were based on simple geometric rules, such as adding tickmarks (like serifs) at the end of design lines to make them easier to print <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. While simple to check, they were not useful for smaller features lower down on the silicon and were primarily used for the metal layer <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
2.  **Model-based OPC**: As feature sizes continued to shrink, simple rules became insufficient <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. Model-based OPC emerged, using extensive [[computational_lithography_advancements | computational lithography]] simulations to correct the entire layout before it goes to the fab <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. This involves breaking down the chip design into segments, sampling within those segments, simulating the light's journey, and iteratively making corrections <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. Model-based OPC is very accurate but can be slow due to its reliance on intense computation and iteration <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.

### [[inverse_lithography_technology_ilt | Inverse Lithography Technology]] (ILT)
Proposed in 1981 by Professor B.E.A. Saleh, [[inverse_lithography_technology_ilt | Inverse Lithography Technology]] (ILT) is another Resolution Enhancement Technique that aims to improve the resolution of the chip design image transfer <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.

#### Conceptual Difference from OPC
Unlike traditional OPC, which works from the mask to the wafer, ILT conceptually goes the other way: from the wafer to the mask <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. With ILT, the desired pattern on the wafer is known, and the system works backward to determine the best mask design, pixel by pixel, taking into account how light travels through the lithography machine and interacts with the resist <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>. This "inverse" approach is the key differential from traditional model-based OPC <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>.

#### History and Development
*   Professor Saleh initially used a variant of "simulated annealing" for ILT, which involved creating a randomly generated mask and iteratively making random changes ("flipping pixels") to discover a local optimum <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>.
*   Researchers at Berkeley, IBM, and other organizations refined the technique <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
*   In 2003, Luminescent Technologies popularized ILT with their paper "Fast Inverse Lithography Technology" <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.
*   Intel, which had been funding academic research in the field since the 1990s, presented its own version of ILT in 2007, calling it pixelated mask technology <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>.

ILT results in highly unintuitive, "horrific mutation[s]" of the original design, but the print results are superior <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>. ILT masks tend to be more accurate, have greater fidelity to the desired pattern, and offer more room for process error compared to model-based OPC <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.

#### Bottlenecks for ILT
Despite its advantages, ILT faced substantial tradeoffs in the late 2000s and early 2010s <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>:
1.  **Computational Power and Throughput**: Accounting for every pixel requires immense computing power or time, with some designs taking weeks to process <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>.
2.  **Manufacturing Challenges**: ILT generated "curvilinear masks" with complex curves and diagonals, which were difficult to produce using traditional focused electron beam mask writing tools that favored "Manhattan geometry" (shapes made of rectangles) <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. Fracturing these complex shapes into rectangles for manufacturing was challenging <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.

ILT was considered "a bit too early for its time" <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. The advent of 193 nanometer immersion lithography improved resolutions so much that manufacturers didn't widely adopt ILT over OPC <a class="yt-timestamp" data-t="12:45:00">[12:45:00]</a>. Consequently, Luminescent Technologies was split up in 2012 <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>.

#### Changing Times and CuLitho
The situation for ILT has changed <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. Mask writing tools have improved, with new multi-beam tools making it possible to produce complex curvilinear masks in a reasonable time <a class="yt-timestamp" data-t="13:20:00">[13:20:00]</a>. However, the computational challenges remained <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>.

The increasing complexity of leading-edge chips, such as Hopper with 80 billion transistors, has forced fabs to use ILT more frequently <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>. This incentivized efforts to make ILT work faster <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>. TSMC presented simulation results hinting at how GPUs could speed up ILT, leading Nvidia to develop CuLitho <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.

[[computational_lithography_advancements | CuLitho]] is a software library announced by Nvidia in March 2023, claiming a performance leap of up to 40x beyond current lithography <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It's a collection of parallel algorithms invented by Nvidia scientists for accelerated primitive operations of [[optical_proximity_correction_opc_techniques | OPC]] <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. By integrating these GPU-accelerated algorithms into traditional OPC EDA software, CuLitho can speed up the end-to-end computational lithography system by 23-42 times <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

### Source Mask Optimization (SMO)
Another significant RET is Source Mask Optimization (SMO), which involves optimizing both the mask pattern and the illuminating light source behind the mask to achieve the best results <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>.

RETs, especially with advancements like [[computational_lithography_advancements | CuLitho]], are critical for the continued ability to print ever smaller features on chips <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.