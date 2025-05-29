---
title: Technological advancements in semiconductor manufacturing
videoId: YJrOuBkYCMQ
---

From: [[asianometry]] <br/> 
The semiconductor industry encompasses a wide range of technologies, from the cutting-edge to the more established "trailing-edge" processes. While much attention is often given to the most advanced engineering feats, such as [[Impact of EUV technology on semiconductor fabrication | extreme ultraviolet lithography]], the majority of chips in circulation are produced using older, less "sexy" methods <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, understanding the distinctions and challenges associated with these different technological tiers is crucial for comprehending the current state of the global chip supply chain <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Semiconductor Process Nodes

Semiconductor manufacturing processes are categorized into different "nodes," which broadly refer to the feature size of the transistors on a chip.

### Trailing Edge Nodes
Trailing edge process nodes are the workhorses of the semiconductor industry, underpinning a vast array of devices <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. These are not the "sexy three-nanometer monsters" but rather "unheralded workhorses" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

*   **Definition:** The definition of a trailing node can vary, but TSMC classifies any process at 16 nanometers (nm) or older as a trailing node <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. In 2021, these nodes accounted for approximately 50% of semiconductor revenue <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Subdivisions:**
    *   **Mature Nodes:** Generally considered to be in the 40 to 450 nanometer range <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   **Legacy Nodes:** Anything older than 450 nanometers <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Common Use:** Most microcontrollers, such as the ATSAMD21, are made with 110 or 180 nanometer processes <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. These chips, like the ATSAMD21, are small 48 MHz ARM chips with 256 KB of flash and 32 KB of SRAM, selling for about $3-4 per unit <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. They are deployed in automation, metering, and industrial manufacturing <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Leading Edge Nodes
These are the most advanced and complex process nodes, constantly pushing the boundaries of transistor density and performance <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Companies like AMD and Apple historically aimed to utilize these fastest, "sexiest" leading-edge nodes, moving on as the industry progressed <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Key Technological Shifts and Advancements

### Planar Gates vs. FinFET Gates
A significant technological transition occurred around the 28-22 nanometer generation gap <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **28nm Node:** This node is notable as it is likely the most advanced still utilizing a planar gate structure <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Beyond 28nm:** Moving to newer nodes requires dealing with more complex FinFET gates, rampant multi-patterning concerns, and potentially [[Impact of EUV technology on semiconductor fabrication | EUV]] <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. These advancements contribute to increased complexity, less reliable products, lower yields, and higher costs per gate <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. As a result, 28nm often represents the "bottom of the cost curve" on a per 100 million gate basis, with newer nodes becoming more expensive per gate <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Wafer Size Evolution
Another significant shift in manufacturing technology involves wafer size.
*   **Current Standard:** The current industry standard for wafers is 300 millimeters <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Older Standard:** Over 200 fabs still produce 200-millimeter wafers, which are smaller and older <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Upgrade Benefits:** Upgrading from 200mm to 300mm wafers can yield over two times as many dies, thanks to the laws of numbers <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. While this requires a substantial facility overhaul (larger floor layout, new automation systems, and managing wafer supply concerns), it can double output without building an entirely new fab <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

### Design Tools and Methodologies
Advancements in design tools also play a role in optimizing semiconductor manufacturing.
*   **Open Source EDA & PDKs:** Initiatives like open-source EDA (Electronic Design Automation) software and PDKs (Process Design Kits) aim to reduce the cost of hardware development <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Facilitating Die Shrinks:** New tools can make it easier for designers to adapt designs for or perform a "die shrink" onto another node <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. An example is the open-source 130 nanometer PDK released by Google and SkyWater Technologies, which could encourage long-delayed die shrinks, leading to faster and better chips for consumers <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

## Impact of Technological Advancements

The rapid pace of technological advancements, particularly at the leading edge, has had several [[Impact of generational shifts in the semiconductor industry | impacts]] on the industry:

*   **Commoditization of Older Nodes:** Initially, new fabs produce leading-edge chips with high margins, recouping investment <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. However, as the industry moves on (often within a year or two), the prices of older fab's chips collapse and become commoditized <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Slowing Upscaling Trend:** It has become increasingly difficult to move to the very next node, as customers must balance the benefits against the higher costs and complexities <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Chips That Don't Scale Well:** Certain types of chips, such as analog, mixed-signal, radio frequency (RF), and MEMS (Micro-Electro-Mechanical Systems) chips (found in devices like accelerometers), do not scale up well to newer nodes <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Demand for these chips, often produced on trailing-edge nodes, is very high <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **Reliability Over Bleeding Edge:** Industries like automotive prioritize reliability and effectiveness across challenging conditions, making them significant consumers of trailing-edge chips (about 40% of market demand) <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. They often do not require the absolute fastest chips if it means dealing with the trade-offs of newer, more complex nodes <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## Industry Response and Future Outlook

Despite the focus on leading-edge advancements, the industry is increasingly recognizing the importance of trailing-edge capacity due to persistent shortages <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Increased Investment:** While most semiconductor industry investments in new fabs have historically focused on leading-edge technology, there's a growing commitment to older nodes <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   TSMC is building new trailing-edge fabs in Japan and Kaohsiung operating in the 28-22 nanometer range, partly financed by price increases on older nodes <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   Samsung, traditionally focused on the latest technology, is investing more in trailing-edge semiconductor capacity <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
    *   [[Chinas semiconductor manufacturing efforts | China]] is also significantly expanding its trailing-edge capacity with up to a dozen new fabs, including SMIC spending over $9 billion to add wafer capacity in Shanghai and Shenzhen <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
    *   India's Vedanta has partnered with Foxconn to build a trailing-edge fab (65-28 nm) with government support <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   The U.S. CHIPS Act has appropriated $2 billion specifically for "mature technology nodes" <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Patience Required:** Addressing supply constraints for trailing-edge semiconductors will take time, at least one to two years, meaning shortages may continue until at least 2023 <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. However, signs of growth slowing in trailing-edge nodes and increased fab construction suggest a potential easing of demand if there's a cyclical downturn in the macro economy <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.