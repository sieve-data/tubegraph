---
title: Chip design process and techniques
videoId: ihz2WY-E2C8
---

From: [[asianometry]] <br/> 

Electronic Design Automation (EDA) is a critical software tool for chip designers that enables the creation of many advanced chips today <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Historically, chip design involved painstakingly drawing circuits by hand <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## The Chip Design Process Flow

While names and processes may vary between companies like Apple or Nvidia, a generic chip design flow includes several stages <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>:

### 1. Integrated Circuit Requirements
Product designers and system engineers envision a product and determine the integrated circuit requirements based on customer needs <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. They may not have extensive knowledge of circuit design, but they understand customer demand <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### 2. Logic Design (Circuit Design)
Abstract requirements are translated into circuits with the logic capable of meeting those requirements <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This stage involves defining various circuits:
*   **Logic Circuits (Gates)**: These act as decision boxes, receiving inputs, processing them, and producing an output, such as determining if 'A' equals 'B' or if 'D' is true only if 'E' and 'F' are true <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Memory Circuits**: These circuits are capable of remembering whether a value was true or false, similar to an on/off light switch <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
The outcome of this stage is a "net list," which is a grouping of logic and memory circuits connected by wires <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### 3. Physical Design
After logic design, physical designers undertake the literal physical layout of the logic circuits, memory circuits, and the wiring that connects them on the chip <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This task can be incredibly difficult when dealing with thousands or millions of circuits <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### 4. Verification and Testing
Once the physical design is complete, the chip design undergoes verification and testing for errors before being sent to a foundry like [[role_of_tsmc_and_ibm_in_advancing_chip_technology | TSMC]] or Samsung Foundry <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. EDA software is heavily involved in every stage, including checking newly arrived designs against foundry design rules <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Design Rule Checking (DRC) is crucial, as errors can cost millions of dollars if they proceed to the fabrication stage <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Evolution of Chip Design

### Early Manual Methods
Up until the 1970s, chip designs were primarily done by hand <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. A design drawn on paper would be transferred to a photo mask, often made of ruby lith, which was then used to project patterns onto the substrate material to produce the chip design <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Emergence of Software Tools
As chips grew more complex with increasing numbers of transistors and connections, big companies began developing simple in-house software tools to assist in the design process <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. These early tools focused on automating the placement of blocks and wires on circuit boards <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Routing, a tedious and repetitive task, was a primary target for automation <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Early mainframe programs used simple breadth-first search algorithms, which were slow, leading to the adoption of more advanced algorithms in later versions <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### Transition to the Silicon Realm
When the number of components in integrated circuits surpassed those on circuit boards, EDA software moved to the silicon realm <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This transition helped solve daunting [[challenges_in_semiconductor_manufacturing | challenges in chip making]], such as wiring connections in 3D across multiple layers, including vias (layer-to-layer connections) <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This introduced immense complexity and significant opportunities for errors <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## Challenges and the Role of EDA

Moore's Law, an observation about the pace of the semiconductor industry, suggested an approximate 58% annual rise in the number of transistors that fabs could produce <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. While manufacturing capabilities scaled rapidly, the human ability to design these complex chips did not keep pace <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This created a "productivity gap" between design and manufacturing capabilities <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. For example, a company like AMD might take years to release a 5-nanometer chip, even if [[role_of_tsmc_and_ibm_in_advancing_chip_technology | TSMC]] had the manufacturing capacity <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Better EDA tools are the only practical way for chip design teams to keep up and bridge this gap <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

## Developments in EDA Software and Design Styles

### Commercial Automatic Physical Design Systems
Commercial automatic physical design systems began to emerge in the 1980s, driven by improved computing power and powerful new display technologies <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. Early EDA software literally drew designs on paper <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. The advent of reasonably priced storage tube CRT screens made the industry more accessible to designers <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

### New Approaches to Chip Design
The industry pioneered and adopted new approaches to chip design to leverage EDA's automation powers <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

*   **Programmable Logic Arrays (PLAs)**: Engineers and universities initially advocated for a more space-efficient design style called programmable logic arrays <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. However, EDA software for this style did not scale well, requiring extensive redrawing when components changed, and designers had to manage designs at both high and low levels of abstraction, making it difficult <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

*   **Standard Cell Style**: The semiconductor industry developed a "standard cell" style <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. In this approach, designers select from a library of standardized groups of gates (cells) and define their interconnections <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This allowed the design process to split into separate logical and layout functions, abstracting away low-level details and enabling designers to focus on their specific areas <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Because cells are standardized, EDA software can consistently create electrically and physically correct designs <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Although initially criticized for being less area-efficient (with routing taking up to half the area of some early cells), the standard cell style became the industry standard due to its superior workflow benefits for designers <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Key EDA Industry Players

Over time, software firms in the EDA industry consolidated as tasks became more complex and required integration across various stages of the design cycle <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Their proprietary libraries often became the de facto standard for the entire industry <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

The two leading companies in this space are Cadence and Synopsys, both U.S.-based and publicly traded <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. As of the transcript, Cadence had a $34 billion market capitalization, and Synopsys had $36 billion <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. These companies have grown through a long series of acquisitions and have established alliances with major players like [[role_of_tsmc_and_ibm_in_advancing_chip_technology | TSMC]] and Samsung Foundry to facilitate the transition from design to real-world chip production <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

EDA vendors make it significantly easier for fabless companies to enter the semiconductor world <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Companies may pay millions of dollars for a bundle of software tools <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Beyond tools, these companies own extensive intellectual property (IP), licensing out useful IP blocks for standard chip functions like I/O <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This business model, relying on software subscriptions and IP licensing, results in strong gross margins and cash flows, enabling significant R&D investment to maintain their competitive advantage <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

### Challengers
While Cadence and Synopsys hold a strong position, a few companies are challenging them:
*   Google reportedly developed its own EDA tool to design a recent YouTube chip <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   Chinese alternatives like Empyrean and Celixoff have gained attention, particularly due to the U.S.-China trade war <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   Open-source EDA tools exist for platforms like RISC-V <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
As of now, these efforts remain less developed and lag behind the market leaders <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## Future of EDA

[[emerging_trends_and_challenges_in_chip_design | Exciting new developments]] are on the horizon for EDA-enabled chip design:
*   **Machine Learning**: Programmers are applying machine learning to EDA software, showing promising results <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. For example, machine learning can help EDA tools find optimal wire routes between chip circuits <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a> and simulate photo mask patterns during the lithography phase <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **System-on-Chip (SoC) Designs**: Vendors are experimenting with new techniques to adapt to the industry trend of System-on-Chip (SoC) designs <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

Without EDA software, the cost of creating new chip designs would increase even faster than they already do <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. EDA is a critical part of the industry, essential for the existence of today's advanced chips <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.