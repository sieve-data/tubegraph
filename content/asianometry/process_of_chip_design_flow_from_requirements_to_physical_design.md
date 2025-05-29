---
title: Process of chip design flow from requirements to physical design
videoId: ihz2WY-E2C8
---

From: [[asianometry]] <br/> 

The process of designing modern integrated circuits (ICs) has evolved significantly from the days of manual drawing to sophisticated automated systems. Today, [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | electronic design automation (EDA)]] software is a critical tool for chip designers, without which many advanced chips could not be made <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Generic Chip Design Process Flow

While specific names and steps might differ between companies like Apple or Nvidia, a generic chip design flow can be outlined as follows <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:

### 1. Product Requirements
The process begins with product designers and system engineers envisioning a product at a high level <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. They translate customer needs into a set of integrated circuit requirements <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### 2. Logic Design (Circuit Design)
Next, the chip's requirements are handed over to logic designers, also known as circuit designers <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. These individuals translate the abstract requirements into specific circuits capable of meeting them <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Chips contain many circuits that perform different functions <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Two common types include:
*   **Logic Circuits (Gates)**: These act like "decision boxes," receiving inputs, processing them, and producing an output (e.g., "is A equal to B," or "D is true only if E and F are also true") <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Memory Circuits**: These circuits are capable of "remembering" whether a value was true or false, similar to a light switch being on or off <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Once logic designers complete their work, they produce groupings of logic and memory circuits connected by wires, referred to as a "net list" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### 3. Physical Design
The net list is then handed to physical designers <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Their task involves the literal physical layout of the logic circuits, memory circuits, and the wiring between them on the chip <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This becomes very complex when dealing with thousands or millions of circuits <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### 4. Verification and Foundry Compatibility
After physical design, the chip design is verified and tested for errors <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. It is then sent to a foundry like TSMC or Samsung Foundry <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Foundries also use [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | EDA]] software to check newly arrived designs for compatibility with their design rules <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Design rule checking is crucial, as an error at this stage could cost millions of dollars if it proceeds to fabrication <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Historical Context and Evolution

In the early stages of [[history_of_chip_design_and_evolution_of_electronic_design_automation | chip design]], up to the 1970s, designs were done by hand <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Designers would draw on paper, and these designs would be transferred to a photo mask made of ruby lith <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. The photo mask was then used to project patterns onto a substrate <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

As chips grew more complex, simple software tools were developed in-house by large companies to assist in the design process <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. These tools evolved into the [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | EDA]] software used today <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Initial programs automated the placement of blocks and wires on circuit boards before moving to the "silicon realm" as integrated circuits surpassed circuit board complexity <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This shift introduced challenges like wiring connections in 3D with "vias" (layer-to-layer connections), adding immense complexity and opportunities for errors <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## The Role of EDA in Bridging the Productivity Gap

[[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | EDA]] tools became indispensable due to Moore's Law, which set the pace for the semiconductor industry to produce chips with exponentially increasing transistor counts <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. While fabs can manufacture a vast number of transistors, designing them at the same pace is challenging, as human knowledge and skills cannot scale as quickly as tools and capital <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

This creates a "productivity gap" between design and manufacturing capabilities <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. For example, a company like AMD might need years to design a 5-nanometer chip, even if TSMC had immediate capacity <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Better [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | EDA]] tools are the only practical way for chip design teams to keep up and close this gap <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

## Evolution of Design Approaches with EDA

Commercial automatic physical design systems emerged in the 1980s, driven by improved computing power and new display technologies like CRT screens <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

The industry also adopted new chip design approaches that amplified [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | EDA]]'s automation capabilities <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>:
*   **Programmable Logic Arrays (PLAs)**: Initially, engineers advocated for this space-efficient design style <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. However, [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | EDA]] software for PLAs did not scale well, requiring extensive redrawing when components changed, and designers had to manage the design at both high and low levels of abstraction <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Standard Cell Style**: The semiconductor industry developed this style where designers choose from a library of standardized groups of gates, called "cells," and decide how they are wired together <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This approach allowed the design process to split into separate logical and physical (layout) functions, abstracting away low-level details <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Because cells are standardized, [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | EDA]] software can consistently create electrically and physically correct designs <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Although initially criticized for being less area-efficient, the standard cell style became the industry standard due to its superior workflow with [[role_and_significance_of_electronic_design_automation  | EDA]] <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

In conclusion, the structured chip design flow, from initial product requirements to final physical layout and verification, is heavily reliant on advanced [[role_and_significance_of_electronic_design_automation_in_chip_manufacturing | electronic design automation]] software. These tools are indispensable for managing the ever-increasing complexity of modern chips and for bridging the productivity gap between design capabilities and manufacturing advancements <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.