---
title: ARMs business model and licensing strategy
videoId: Y8guMe665RE
---

From: [[acquiredfm]] <br/> 

[[ARMs business model and licensing strategy|ARM Holdings]] is a company that develops the instruction set architecture (ISA) and designs for central processing units (CPUs) that underpin electronic devices globally, from phones to cars <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Established over 30 years ago out of Cambridge, ARM was publicly traded, taken private by SoftBank in 2016, and went public again in 2023, now valued at approximately $150 billion <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Core Business Model: Licensing and Royalties
ARM's fundamental business model revolves around licensing and royalties <a class="yt-timestamp" data-t="00:39:42">[00:39:42]</a>.
1.  **Upfront Licensing Fee**: Customers pay an upfront fee for the right to use ARM's designs or architecture. This fee is considered a proxy for research and development (R&D) that companies would otherwise spend developing their own CPU <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>. In the early days, when companies were not shipping high volumes, licensing revenue was the majority of ARM's income <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.
2.  **Production Royalties**: ARM receives a royalty payment for each chip shipped by its partners that incorporates ARM's technology <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. This represents a "shared success model" where ARM benefits as its customers scale their production <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. As volumes increased, royalties became a significant component of ARM's revenue <a class="yt-timestamp" data-t="00:40:14">[00:40:14]</a>.

This model was innovative in the early 1990s, diverging from the vertically integrated approach of other processor developers like x86, 68000, and AMD 29000 <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

## Types of Licenses

ARM offers two primary types of licenses:

### 1. Core/Implementation License
ARM designs and builds its own CPUs (referred to as cores or implementations), which it then licenses to companies <a class="yt-timestamp" data-t="02:15:27">[02:15:27]</a>. Examples of companies that license ARM's pre-designed cores include Samsung, MediaTek, Tesla, Qualcomm, and [[AWS business strategy | Amazon]] <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

### 2. Instruction Set Architecture (ISA) / Architectural License
Under an architectural license, ARM licenses its instruction set architecture (ISA), allowing partners to develop their *own* CPU designs based on the ARM ISA <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Apple, for instance, develops its A-series and M-series chips based on the ARM ISA <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.

A critical aspect of these architectural licenses is that licensees are *not* allowed to add custom instructions that break software compatibility with the ARM ISA <a class="yt-timestamp" data-t="04:33:10">[04:33:10]</a>. This adherence to a consistent ISA ensures that software written for ARM can run across various ARM-based chips, regardless of the specific implementation <a class="yt-timestamp" data-t="04:31:50">[04:31:50]</a>. While common in earlier days, these architectural licenses are becoming less frequent as the complexity and return on investment (ROI) for developing custom implementations decrease <a class="yt-timestamp" data-t="04:13:10">[04:13:10]</a>.

## Strategic Evolution: Subsystems
ARM's business model has evolved to offer more integrated solutions called "subsystems" <a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>. Beyond individual CPUs, ARM also develops GPUs, NPUs (for AI), and complex interconnects like Coherent Mesh Networks (CMN) needed to build sophisticated System-on-Chips (SoCs) <a class="yt-timestamp" data-t="01:10:37">[01:10:37]</a>.

Subsystems essentially bundle these disparate "Lego blocks" of IP (e.g., 128 CPUs, CMN, memory interfaces) and stitch them together <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. ARM verifies that these integrated designs will functionally work and meet specific performance characteristics, such as frequency output <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>. This "virtual chipset" approach offers significant benefits:
*   **Faster Time to Market**: Saves customers 3 to 9 months of engineering time, enabling quicker product launches <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>.
*   **Reduced Complexity**: Customers don't need to spend resources on integrating basic IP, allowing them to focus on proprietary value-add components like camera ISPs for phones or accelerators for cloud services <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a>.

## Competitive Advantages
ARM's business model provides several key advantages in the semiconductor industry:

### 1. Open Model and Optionality
Unlike x86 architecture, which is primarily built by two companies (Intel in-house and [[TSMCs business strategies and comparison with Apple | AMD]] at [[TSMCs business strategies and comparison with Apple | TSMC]]), ARM's open model allows its designs to be built at *any* fab by *any* chip company <a class="yt-timestamp" data-t="00:50:26">[00:50:26]</a>. This provides significant optionality and flexibility for customers, who can choose from multiple chip vendors or even design their own custom SoCs based on ARM <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>. Hyperscalers like Microsoft, Google, and [[AWS business strategy | AWS]] leverage this to build custom chips with specific memory, storage, and interconnects for extreme efficiency <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.

### 2. Low-Margin Foundation
ARM originated with a business model that was not focused on high per-unit margins, unlike its x86 competitors <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>. This foundational difference made it easier for ARM to gain widespread adoption, as it offered an affordable and efficient alternative, especially for new markets.

### 3. Software Compatibility Flywheel
ARM's strict adherence to a consistent ISA, prohibiting customers from adding custom instructions that break compatibility, has fostered a massive software ecosystem <a class="yt-timestamp" data-t="04:33:10">[04:33:10]</a>. This ensures that applications can run seamlessly across all ARM-based devices, which is a "superpower" and a key reason for ARM's enduring dominance, especially in [[ARMs role in mobile and smartphone markets | mobile and smartphone markets]] <a class="yt-timestamp" data-t="04:33:10">[04:33:10]</a>. The sheer volume of software written for ARM makes it incredibly difficult for alternative architectures to gain traction <a class="yt-timestamp" data-t="04:48:51">[04:48:51]</a>.

## Financial Outlook
In the last quarter, ARM reported $939 million in revenue, indicating a run rate of approximately $4 billion annually <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. The market is highly bullish on ARM, reflected in its $150 billion valuation <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. This optimism is driven by several factors:
*   **Ubiquitous Presence**: ARM chips are found in billions of devices globally, from cars and appliances to game consoles <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. In FY2024, an estimated 29 billion ARM chips were shipped, equating to four ARM-based chips for every human on Earth in the last 12 months <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.
*   **Market Tailwinds**: The growth in connected devices and the increasing demand for compute in every aspect of life provides a significant tailwind <a class="yt-timestamp" data-t="00:55:14">[00:55:14]</a>.
*   **[[ARMs adoption in data centers and AI applications | AI Revolution]]**: The rise of artificial intelligence (AI) is a massive opportunity for ARM. AI requires unprecedented compute capacity and capability, both for training (often in [[ARMs adoption in data centers and AI applications | data centers]]) and for inference (running applications on edge devices like cars, wearables, and smartphones) <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>. ARM's power efficiency and adaptability make it ideal for these diverse AI workloads, especially at the "edge" where high-power GPUs are impractical <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.