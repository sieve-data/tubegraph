---
title: Electronic Design Automation EDA software
videoId: ihz2WY-E2C8
---

From: [[asianometry]] <br/> 

Electronic Design Automation (EDA) is a critical software tool used by [[chip_design_process and techniques | chip designers]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Without this unheralded software, many of today's most advanced chips could not be made <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The [[role_of_eda_in_the_semiconductor_industry | role of EDA in the semiconductor industry]] is paramount, as it helps solve daunting challenges in [[engineering_and_manufacturing_of_silicon_wafers | chip making]] <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## The Chip Design Process and EDA's Role

To understand how EDA software assists the [[chip_design_process and techniques | chip designer]], it's essential to know the [[chip_design_process and techniques | chip design process]] flow <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. While the process and names may vary between companies like Apple or Nvidia, a generic flow includes several key stages:

### 1. Product Design and System Engineering
Product designers and system engineers envision a product and determine a set of integrated circuit requirements based on customer needs <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### 2. Logic Design (Circuit Design)
Chip requirements then move to logic design, also known as circuit design <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Here, abstract requirements are translated into circuits with the logic capable of meeting those requirements <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. A chip contains many circuits that perform different functions <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:
*   **Logic circuits (gates):** Act as decision boxes, receiving inputs, processing them, and producing an output <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. A single logic circuit is simple, but in groups, they can perform complex tasks <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Memory circuits:** Capable of remembering whether a value was true or false, similar to an on/off light switch <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Once logic designers complete their work, they produce groupings of logic and memory circuits connected by wires, referred to as a "net list" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### 3. Physical Design
After logic design, the design is handed to physical designers <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Their work involves the literal physical layout of logic circuits, memory circuits, and the wiring between them on the chip <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This becomes extremely difficult with thousands or millions of circuits <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### 4. Verification and Testing
Finally, the [[chip_design_process and techniques | chip design]] is verified and tested for errors before being sent to a foundry like TSMC or Samsung Foundry <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

EDA software is heavily involved in every one of these stages <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Foundries like TSMC or Samsung also use EDA software to check newly arrived designs for compatibility with their design rules <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This "design rule checking" (DRC) is crucial, as an error here could cost millions of dollars if it slips into the fabrication stage <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Evolution of EDA Software

In the early stages of [[chip_design_process and techniques | chip design]], up until the 1970s, designs were done by hand <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Designers would draw on paper, and this paper design would then be transferred to a photo mask made of "ruby lith" <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The photo mask was used to produce chip patterns by projecting light through it onto the substrate <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

As chips grew more complex with increasing transistors and connections, simple software tools were developed in-house by large companies to assist in the design process <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. These tools evolved into the EDA software used today <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The first software programs automated the placement of a small number of blocks and wires on a circuit board, not a chip <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This "routing" task was tedious and constantly repeated as board components moved <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. These early mainframe programs used simple breadth-first search algorithms, which were slow and quickly moved to other algorithms in later versions <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

As the number of components in integrated circuits surpassed those on circuit boards, EDA software moved into the silicon realm <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Chips are built in layers, requiring wiring connections in 3D, including layer-to-layer connections called vias <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This adds immense complexity and opportunities for errors <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### Moore's Law and the Productivity Gap
Moore's Law, an observation about the semiconductor industry's pace, dictates an ever-increasing number of transistors on chips <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>, <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Historically, this translates to roughly a 58% annual rise in transistor counts that fabs are capable of manufacturing <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>, <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

However, being able to fabricate many transistors is different from designing them <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Design speed is limited because human knowledge and skills cannot scale as fast as tools and capital <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This creates a "productivity gap" between design and manufacturing capabilities <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. For example, AMD might take years to release a 5-nanometer chip even if TSMC has the capacity ready <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Better EDA tools are the only practical way for [[chip_design_process and techniques | chip design]] teams to keep up and close this gap <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Advancements in EDA and Chip Design Styles
Commercial automatic physical design systems emerged in the 1980s, fueled by improved computing power and new display technologies like reasonably priced storage-tube CRT screens <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>, <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>, <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

The industry also adopted new approaches to [[chip_design_process and techniques | chip design]] that enhanced EDA automation <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Programmable Logic Arrays (PLAs):** Initially advocated by engineers and universities for their space-efficient design style <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>, <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. However, EDA software for PLAs did not scale well, requiring extensive redrawing when components changed, and designers had to handle both high and low levels of abstraction simultaneously <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Standard Cell Style:** Developed by the semiconductor industry, this approach allows designers to choose from a library of standardized groups of gates, called "cells," and decide how they are wired together <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This standardized approach abstracted away lower-level details, enabling the design process to split into separate logical and layout functions <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Because cells are standardized, EDA software can consistently create electrically and physically correct designs <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Although initially criticized for being less area-efficient (some early standard cells had half their area taken by routing), its superior workflow with EDA made it the industry standard <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

## Major EDA Companies and Market Presence

An EDA industry emerged to service various parts of the [[chip_design_process and techniques | chip design process]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Over time, these software firms consolidated as tasks became harder and required integration across different design cycle stages <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Their proprietary libraries often became the de facto standard for the entire industry <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

The two [[major_eda_companies_and_their_market_presence | leading companies]] in this space are Cadence and Synopsys <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>, both based in the United States and publicly traded <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Cadence has a market capitalization of $34 billion, and Synopsys $36 billion <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>, <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. These companies are the result of long series of acquisitions and have established alliances with major players like TSMC and Samsung Foundry to ease the transition of chips from design to the real world <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>, <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

Fabless entrants seeking to enter the semiconductor world typically need to acquire bundles of software tools from these EDA vendors, often costing millions of dollars <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Beyond EDA tools, these companies also own substantial intellectual property (IP) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. They generate revenue by licensing useful IP blocks for standard chip functions, like IO <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This business model, combining software subscriptions and IP licensing, results in very good gross margins and strong cash flows, enabling significant R&D investment to further extend their advantages <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>, <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

While Cadence and Synopsys maintain strong positions, a few challengers exist <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>:
*   Google reportedly developed its own EDA tool for a recent YouTube chip <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   Chinese alternatives like Empyrean and Celixoff have gained attention due to the US-China trade war <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   Open-source EDA tools are emerging for initiatives like RISC-V <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

However, as of now, these efforts remain undeveloped and lag behind the market leaders <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## Emerging Trends and Challenges in Chip Design

Exciting new developments are on the horizon for EDA-enabled [[chip_design_process and techniques | chip design]] <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Programmers are applying machine learning to EDA software, showing promising results <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>:
*   Machine learning can help EDA tools find optimal routes for wires between chip circuits <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   It can simulate the patterns a photo mask design will project during the lithography phase <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

Outside of machine learning, vendors continue to experiment with new [[emerging_trends_and_challenges_in_chip_design | techniques]] to adapt to the industry trend of Systems-on-Chip (SoC) designs <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>, <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

Without EDA software, the cost of creating new [[chip_design_process and techniques | chip designs]] would soar even faster than they already do <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. EDA is a critical part of the semiconductor industry, and today's advanced chips would not exist without it <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.