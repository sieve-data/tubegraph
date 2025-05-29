---
title: Emerging trends and challenges in chip design
videoId: ihz2WY-E2C8
---

From: [[asianometry]] <br/> 

Chip design, once a manual and painstaking process, has evolved significantly due to increasing complexity and the demand for rapid innovation. The shift from hand-drawn circuits to sophisticated software tools has been a critical development in addressing modern design [[challenges_in_the_semiconductor_industry | challenges]].

## Evolution of Chip Design Practices

In the past, chip designs were created by hand, with designers drawing intricate diagrams on paper <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These paper designs were then transferred to photo masks, typically made of a material called ruby lith, which were used to project patterns onto the substrate during fabrication <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. However, as chips became more complex with millions of transistors and connections, this manual approach became unsustainable <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## The Role of Electronic Design Automation (EDA)

The development of Electronic Design Automation (EDA) software revolutionized chip design <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. These tools automate many aspects of the [[chip_design_process_and_techniques | chip design process]], which would otherwise be extremely difficult and error-prone <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. EDA software is integral at every stage, from initial design to final verification, even used by foundries like TSMC and Samsung to ensure compatibility with their design rules <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Errors in design rule checking can cost millions of dollars if they slip into fabrication <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Challenges in Modern Chip Design

Despite advancements, several [[challenges_in_the_semiconductor_industry | challenges]] persist in chip design:

*   **Increasing Complexity**
    *   Chips are built in multiple layers, requiring connections (vias) in 3D, which adds astounding amounts of complexity and opportunities for errors <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Productivity Gap**
    *   [[impact_of_generational_shifts_in_the_semiconductor_industry | Moore's Law]] dictates an approximate 58% annual rise in the number of transistors fabs can produce <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
    *   However, human knowledge and skills cannot scale as fast as tools and capital, creating a productivity gap between design and manufacturing capabilities <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Better EDA tools are the only practical way to close this gap <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Design Methodologies**
    *   Early EDA software for [[early_challenges_and_developments_in_fpga_technology | programmable logic arrays]] did not scale well, requiring extensive redrawing when components changed and forcing designers to handle both high and low levels of abstraction simultaneously <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

## Emerging Trends and Solutions

### Standard Cell Design Style

The semiconductor industry adopted a "standard cell" design style, where designers choose from a library of standardized groups of gates (cells) and define their interconnections <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This approach:
*   Allows the design process to split into separate logical and physical layout functions <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   Abstracts away low-level details, enabling designers to focus on their specific areas <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   Enables EDA software to consistently create electrically and physically correct designs due to standardized cells <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. While initially criticized for being less area-efficient, its workflow benefits made it an industry standard <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### The EDA Industry Landscape

The EDA industry emerged to service various parts of the [[chip_design_process_and_techniques | chip design process]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Over time, these software firms consolidated as tasks became harder and required integration across various design stages <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

*   **Leading Companies**: Cadence (approx. $34 billion market cap) and Synopsys (approx. $36 billion market cap) are the two dominant players, both based in the United States <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. They have developed proprietary libraries that have become de facto industry standards <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Strategic Alliances**: These companies have alliances with major foundries like TSMC and Samsung Foundry, simplifying the transition of chip designs to the real world for fabless entrants <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Business Model**: EDA vendors charge millions of dollars for bundles of software tools <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. They also license out useful IP blocks for standard chip functions, generating strong cash flows and gross margins <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

### Competitors and Future Developments

While Cadence and Synopsys hold strong positions, challengers are emerging:
*   **Internal Tools**: Google developed its own EDA tool for a YouTube chip <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Chinese Alternatives**: Companies like Empyrean and Celixoff have gained attention, partly due to the U.S.-China trade war <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Open-Source EDA**: Open-source tools, for architectures like Risk 5, are also being developed <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Machine Learning (ML)**: Programmers are applying machine learning to EDA software, showing promising results <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. ML can optimize wire routing between circuits and simulate photo mask patterns during lithography <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Systems-on-Chip (SoC)**: Vendors are experimenting with new techniques to adapt to the industry trend of Systems-on-Chip (SoC) designs <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

Without EDA software, the cost of creating new chip designs would soar even faster than they currently are <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>, highlighting their critical role in the semiconductor industry and the existence of today's advanced chips <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.