---
title: Role of EDA in the semiconductor industry
videoId: ihz2WY-E2C8
---

From: [[asianometry]] <br/> 

[[electronic_design_automation_eda_software | Electronic Design Automation]] (EDA) software is a critical tool for chip designers <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Historically, chip designs were drawn by hand on paper, a painstaking process involving intricate diagrams and drawings <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This manual approach was common into the 1970s, where paper designs were then transferred to photo masks for chip production <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Today, no one draws circuits by hand anymore <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Without [[electronic_design_automation_eda_software | EDA software]], many of the most advanced chips currently produced would not be possible <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## The Chip Design Process Flow

Designing a custom chip, as done by companies like Apple or Nvidia, follows a generic process flow <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>:

1.  **Product Conception and Requirements**
    *   Product designers and system engineers envision a product at a high level <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   They define a set of integrated circuit requirements based on customer needs <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

2.  **Logic Design (Circuit Design)**
    *   Chip requirements are translated into circuits with the logic capable of meeting those requirements <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
    *   This involves designing:
        *   **Logic Circuits (Gates)**: Act like decision boxes, receiving inputs and producing an output <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
        *   **Memory Circuits**: Capable of remembering a true or false value <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   The outcome is a "net list," which is a grouping of logic and memory circuits connected by wires <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

3.  **Physical Design**
    *   The design is handed over to physical designers, who are responsible for the literal physical layout of logic circuits, memory circuits, and their wiring on the chip <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This becomes extremely difficult with thousands or millions of circuits <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

4.  **Verification and Testing**
    *   After physical design, the chip design is verified and tested for errors before being sent to a foundry like [[TSMC]] or [[Samsung Foundry]] <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   [[electronic_design_automation_eda_software | EDA software]] is heavily involved in every one of these stages <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Foundries also use [[electronic_design_automation_eda_software | EDA software]] to check new designs for compatibility with their design rules <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Errors at this stage can cost millions of dollars if they proceed to fabrication <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Evolution and Impact of EDA

As chips became increasingly complex with more transistors and connections, simple software tools were developed in-house by large companies to aid in design <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. These tools evolved into the [[electronic_design_automation_eda_software | EDA software]] used today <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Initial Automation
Early [[electronic_design_automation_eda_software | EDA software]] programs automated the placement of blocks and wires on circuit boards <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This "routing" task was tedious and required constant repetition as board components moved <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. As integrated circuit components exceeded those on circuit boards, [[electronic_design_automation_eda_software | EDA software]] transitioned to the silicon realm <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Addressing [[Challenges in the Semiconductor Industry | Challenges]]
Bringing [[electronic_design_automation_eda_software | EDA software]] to silicon helps solve daunting [[challenges in semiconductor manufacturing | challenges in chip making]] <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. A chip is built in layers, requiring wire connections in 3D, including layer-to-layer connections called vias <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This adds astounding complexity and creates huge opportunities for errors <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

[[electronic_design_automation_eda_software | EDA software]] helps bridge the productivity gap between design and manufacturing capabilities, which arises from [[Moore's Law]] <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. While fabs are capable of manufacturing ever-increasing numbers of transistors, human knowledge and skills in design cannot scale as quickly as tools and capital <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Better [[electronic_design_automation_eda_software | EDA software]] tools are the only practical way for chip design teams to keep up <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Design Style Shift
Commercial automatic physical design systems emerged in the 1980s, driven by improved computing power and new display technologies like CRT screens <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. The industry also adopted new approaches to chip design:

*   **Programmable Logic Arrays (PLAs)**: An early space-efficient design style <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. However, [[electronic_design_automation_eda_software | EDA software]] for PLAs did not scale well, requiring extensive redrawing when components changed, and forcing designers to handle design at both high and low levels of abstraction <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Standard Cell Style**: Developed by the semiconductor industry, this style allows designers to choose from a library of standardized groups of gates (cells) and decide how they are wired together <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This approach:
    *   Split the design process into separate logical and layout functions <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
    *   Abstracted away low-level details, allowing designers to focus on their specific areas <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   Enabled [[electronic_design_automation_eda_software | EDA software]] to consistently create electrically and physically correct designs due to standardization <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   Despite being less area-efficient initially, its workflow benefits with [[electronic_design_automation_eda_software | EDA software]] made it the industry standard <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

## Key Players in the EDA Industry

An [[electronic_design_automation_eda_software | EDA]] industry sprouted to service various parts of the chip design process <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Over time, these software firms consolidated as tasks grew harder and required integration across different design stages <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. Their proprietary libraries often became the de facto standard across the industry <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

The two leading companies in this space are [[major_eda_companies_and_their_market_presence | Cadence]] and [[major_eda_companies_and_their_market_presence | Synopsys]] <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Both are U.S.-based and publicly traded, with market capitalizations of around $34 billion and $36 billion, respectively <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. These companies are the result of a long series of acquisitions and have established alliances with major players like [[TSMC]] and [[Samsung Foundry]] to facilitate the transition of chips from design to manufacturing <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### Business Model
New fabless companies entering the semiconductor world likely need to acquire [[electronic_design_automation_eda_software | EDA software]] from these vendors, potentially paying millions for a bundle of tools <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Beyond just the [[electronic_design_automation_eda_software | EDA tools]], these companies also own a lot of intellectual property (IP) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. They generate revenue by licensing useful IP blocks for standard chip functions, such as I/O <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This business model, based on software subscriptions and IP licensing, results in high gross margins and strong cash flows, allowing them to invest heavily in R&D and extend their market advantages <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

### Emerging Alternatives
While [[major_eda_companies_and_their_market_presence | Cadence]] and [[major_eda_companies_and_their_market_presence | Synopsys]] hold a strong position, some companies are challenging them:
*   Google developed its own [[electronic_design_automation_eda_software | EDA tool]] for a recent YouTube chip <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   Chinese alternatives like Empyrean and Celixoff have gained attention due to the U.S.-China trade war <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   Open-source [[electronic_design_automation_eda_software | EDA tools]] are emerging, particularly for architectures like RISC-V <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
However, these efforts currently remain undeveloped and lag behind the market leaders <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## The Future of EDA
Exciting developments are on the horizon for [[electronic_design_automation_eda_software | EDA]]-enabled chip design:
*   **Machine Learning**: Programmers are applying machine learning to [[electronic_design_automation_eda_software | EDA software]], showing promising results <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This can help [[electronic_design_automation_eda_software | EDA tools]] find optimal wiring routes for chip circuits <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a> and simulate photo mask patterns during lithography <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **System-on-Chip (SoC) Designs**: Vendors are experimenting with new techniques to adapt to the industry trend of SoC designs <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

In conclusion, [[electronic_design_automation_eda_software | EDA software]] is a critical part of the semiconductor industry <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Without it, the cost of creating new chip designs would soar even faster, and today's advanced chips would not exist <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.