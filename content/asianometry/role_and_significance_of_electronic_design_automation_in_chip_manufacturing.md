---
title: Role and significance of electronic design automation in chip manufacturing
videoId: ihz2WY-E2C8
---

From: [[asianometry]] <br/> 

Electronic Design Automation (EDA) is a critical software tool for chip designers, without which many advanced chips could not be made today <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Previously, chip design was done by hand, with intricate diagrams and drawings covering tables and walls <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. However, modern chip designs are too complex for manual drawing <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## The Chip Design Process Flow
Understanding the [[process_of_chip_design_flow_from_requirements_to_physical_design | chip design process flow]] is essential to grasp how EDA software assists designers <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Although names and specific steps may vary between companies like Apple or Nvidia, a generic flow includes several key stages:

### 1. Integrated Circuit Requirements
The process begins with product designers and system engineers envisioning a product and defining its integrated circuit requirements based on customer needs <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### 2. Logic Design (Circuit Design)
Next, the chip's requirements move to logic design, also known as circuit design <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Designers translate abstract requirements into circuits with logic capable of meeting those needs <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. A chip contains many circuits that perform different functions, including:
*   **Logic Circuits (Gates)**: These act as decision boxes, receiving inputs and producing an output (e.g., "A equal to B," or "D is true only if E and F are also true") <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. While simple individually, groups of logic circuits can achieve complex tasks <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Memory Circuits**: Capable of remembering a true or false value, similar to an on/off light switch <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Upon completion, the logic designers create groupings of logic and memory circuits connected by wires, referred to as a "net list" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### 3. Physical Design
The design is then handed to physical designers, who work on the literal physical layout of the logic circuits, memory circuits, and their interconnecting wires on the chip <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This becomes extremely difficult with thousands or millions of circuits <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### 4. Verification and Testing
After physical design, the chip design undergoes verification and testing for errors before being sent to a foundry like TSMC or Samsung Foundry <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. EDA software is heavily involved in every stage, including checking newly arrived designs for compatibility with design rules <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Such design rule checking (DRC) is crucial, as errors can cost millions of dollars if they slip into the fabrication stage <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## [[history_of_chip_design_and_evolution_of_electronic_design_automation | History of Chip Design and Evolution of Electronic Design Automation]]
Before the 1970s, chip designs were done by hand, drawn on paper, and then transferred to a photo mask (made of ruby lith) to produce patterns on the substrate <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. As chips grew more complex with increasing transistors and connections, big companies began developing simple in-house software tools to assist in the design process <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. These tools eventually evolved into today's EDA software <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Early software programs automated the placement of a small number of blocks and wires on circuit boards, not chips <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Routing was an early focus due to its tedious and repetitive nature <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. These early mainframe programs used simple breadth-first search algorithms, which were slow and quickly moved to other algorithms in later versions <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

As the number of components in integrated circuits surpassed those on circuit boards, EDA software moved into the silicon realm <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This transition helped solve daunting challenges in chipmaking, especially with chips being built in layers, requiring 3D wiring and consideration for layer-to-layer connections called vias, adding astounding complexity <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### The Productivity Gap
Moore's Law, an observation about the pace of the semiconductor industry, suggests a historical 58% annual rise in the number of transistors fabs can produce <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. However, designing these transistors cannot scale as fast as manufacturing capabilities, as human knowledge and skills have limits <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This creates a "productivity gap" between design and manufacturing capabilities <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. For example, AMD might take years to release a [[7nanometer_chip_production_and_technological_significance | five nanometer chip]], even if TSMC had immediate capacity <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Better EDA tools are the only practical way for chip design teams to keep up and close this gap <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Commercialization and Design Styles
Commercial automatic physical design systems began emerging in the 1980s, driven by improved computing power and powerful new display technologies like reasonably priced storage tube class CRT screens <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. The first EDA software initially just drew things on paper like a printer <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

The industry also adopted new approaches to chip design, unlocking more of EDA's automation power <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Programmable Logic Arrays (PLA)**: Engineers and universities advocated for this more space-efficient design style <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. However, EDA software for PLAs did not scale well, requiring significant redrawing with component changes and forcing designers to handle designs at both high and low levels of abstraction <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Standard Cell Style**: The semiconductor industry developed this style, where designers choose from a library of standardized groups of gates, called cells, and determine their wiring <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This allowed the design process to split into separate logical and layout functions, abstracting away low-level details <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Because cells are standardized, EDA software can consistently create electrically and physically correct designs <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Although initially criticized for being less area-efficient (some early standard cells had half their area taken by routing), its superior workflow with EDA made it the industry standard <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## [[major_companies_and_players_in_the_electronic_design_automation_industry | Major Companies and Players in the Electronic Design Automation Industry]]
An EDA industry emerged to service various parts of the chip design process <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Over time, these software firms consolidated as tasks became harder and required integration across various stages of the design cycle <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Their proprietary libraries became de facto industry standards <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

The two leading companies in this space are:
*   **Cadence**: Based in the United States, with a market capitalization of $34 billion <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Synopsys**: Also based in the United States, with a market capitalization of $36 billion <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

These companies are the result of a long series of acquisitions and have long-standing alliances with major players like TSMC and Samsung Foundry to ease the transition from design to fabrication <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Fabless companies entering the semiconductor world almost certainly need to acquire software bundles from these EDA vendors, often costing millions of dollars <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

Beyond EDA tools, these companies own significant intellectual property (IP), licensing out useful IP blocks for standard chip functions like I/O <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This business model, combining software subscriptions and IP licensing, yields strong cash flows and high gross margins, allowing them to invest heavily in R&D and maintain their advantages <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Their market positions are considered "rock solid" <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Challengers to Incumbents
While Cadence and Synopsys dominate, a few companies are challenging them:
*   **Google**: Reportedly made its own EDA tool to design a recent YouTube chip <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Chinese Alternatives**: Companies like Empyrean and Celixoff have gained attention due to the U.S.-China trade war <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Open Source EDA Tools**: Efforts exist for platforms like RISC-V <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

As of now, these alternative efforts remain undeveloped and lag behind the market leaders <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## [[emerging_trends_and_future_developments_in_electronic_design_automation | Emerging Trends and Future Developments in Electronic Design Automation]]
Exciting new developments are on the horizon for EDA. Programmers are applying machine learning to EDA software with promising results <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. For instance, machine learning can help:
*   Find optimal routes for wires between chip circuits <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   Simulate how photo mask designs will project during the lithography phase <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

Beyond machine learning, vendors are experimenting with new techniques to adapt to the industry trend of Systems on Chip (SoC) designs <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

## Conclusion
Without EDA software, the cost of creating new chip designs would soar even faster than they already do <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. EDA is a critical part of the semiconductor industry, and today's advanced chips would not exist without it <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.