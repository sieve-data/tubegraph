---
title: Anticounterfeiting measures in semiconductor manufacturing
videoId: 7epnv43jGV8
---

From: [[asianometry]] <br/> 

The presence of counterfeit semiconductors poses a significant risk in critical situations, as highlighted by incidents such as the 2020 F-16 ejection seat malfunction where fake microchips were discovered in an essential component [00:00:02]. While the exact role of these chips in that specific incident was unclear, it underscored the broader [[semiconductor_industrys_counterfeit_chip_problem | semiconductor industry's counterfeit chip problem]] [00:00:16].

## Defining Counterfeit Semiconductors

The definition of a counterfeit semiconductor can be broad, but the Department of Defense offers two simple definitions:
*   A previously used electronic part sold as new [00:01:03].
*   Unauthorized copies of an authentic electronic product [00:01:09].

The industry's more comprehensive taxonomy identifies a counterfeit semiconductor if it is [00:01:19]:
1.  An unauthorized copy [00:01:23].
2.  Does not conform to the original manufacturer's design, model, or performance standard [00:01:27].
3.  Not produced by the original manufacturer or its authorized contractors [00:01:34].
4.  Off-specification, already used, defective, or misleadingly labeled as new [00:01:40].
5.  Incorrectly marked or with wrong documentation [00:01:46].

## Scope of the Problem

Counterfeit semiconductors represent a substantial illegal business [00:01:53]. In 2019, the OECD estimated that the global volume of counterfeit and pirated products constituted up to 3.3% of total global trade, exceeding $500 billion [00:02:06].

Specific data points related to semiconductors include:
*   The Government-Industry Data Exchange Program (GIDEP) is a government counterfeit parts database, but its non-anonymous nature discourages reporting by victims [00:02:22].
*   The Electronic Resellers Association International (ERAI) tracked 504 reported semiconductor counterfeit cases in 2022, a decrease from 963 in 2021 and 797 in 2019 [00:02:34].
*   A November 2011 US Congressional committee investigation cited the Semiconductor Industry Association, estimating that counterfeiting cost the American semiconductor manufacturing industry over $7.5 billion annually in lost revenue and 11,000 jobs in 2010 [00:02:59].
*   In 2008, the Bureau of Industry Security identified 7,114 detected counterfeited microcircuit incidents across 387 companies within the defense industry, a significant increase from 3,400 reported incidents in 2005 [00:03:25].

Counterfeited semiconductors span various types, from microprocessors to analog, memory, and radio frequency chips, with resale values ranging from 11 cents to $500 [00:03:46].

## Incidents of Counterfeit Chips in the Military Supply Chain

Several incidents highlight the risks posed by counterfeit semiconductors in military applications:
*   **P8A Poseidon Aircraft**: An ice detection module on a P8A Poseidon plane contained a counterfeit Xilinx FPGA unit, which was discovered when the part physically fell out of its socket [00:04:12]. The module's manufacturer, BAE, had purchased 300 such FPGAs, with a California-based supplier testing only 50 of them [00:04:40]. The counterfeit chip was traced back to an affiliate of an electronics manufacturer in Shenzhen, China [00:04:53].

Defense Department contractors and commercial system integrators frequently face the challenge of needing to use older parts for repair and maintenance, as original manufacturers may have stopped production years ago [00:05:03]. This often necessitates sourcing from "offt shady secondhand supplier[s]" [00:05:37].

### Legal and Commercial Consequences

The US government places the responsibility for detecting and filtering out counterfeit chips on contractors [00:05:42]. The National Defense Authorization Act, signed by President Obama in January 2013, imposes civil and criminal penalties for this [00:05:53].
*   **Vision Tech Case**: Vision Tech, a Florida company, knowingly sold fake chips as trademarked military-grade goods, making nearly $16 million in sales [00:06:01]. Employees were instructed to falsely claim chips came from Europe instead of China and Hong Kong [00:06:10]. The company's administrative manager received a 38-month prison sentence for her involvement [00:06:32].

## Methods of Counterfeiting

### Recycling and Relabeling (80% of Incidents)
*   **Recycling**: This common method for counterfeit chips entering the supply chain involves harvesting components from scrap electronics [00:06:40]. The process includes:
    1.  Receiving scrap electronics [00:06:44].
    2.  Removing printed circuit boards [00:06:49].
    3.  Heating boards over an open flame to melt solder and loosen components [00:06:51].
    4.  Bashing boards to dislodge components [00:06:57].
    5.  Removing original markings through various methods [00:07:03].
    6.  Sorting, reprocessing, and applying new coats and markings to appear new [00:07:06].
    This process, combined with the inherent age of e-waste components, subjects them to immense damage and stress, often rendering them non-functional [00:07:15].
*   **Relabeling/Remarking**: This involves altering a chip's markings to mislead users about its capabilities or quality [00:07:30]. Actors acquire chips, wipe existing markings, and apply new ones to make them appear more premium or expensive [00:07:51]. This has real consequences, especially for components requiring enhanced specifications (e.g., military-grade chips hardened against radiation or temperature damage), where cheaper commercial parts might be swapped in [00:08:01]. Recycling and remarking together account for about 80% of total counterfeiting incidents [00:08:23].

### Unauthorized Overproduction by Foundries
*   Many semiconductor companies contract overseas foundries without third-party oversight [00:08:32]. A "bad foundry" might produce more chips than contracted, either to artificially inflate yield reports or to resell the excess production as counterfeits [00:08:45]. This allows the foundry to profit from a valuable design without investing in R&D [00:09:03].

### Unauthorized Clones
*   Third parties create clones of chips to avoid the expensive R&D of developing their own designs [00:09:37]. Design IP for these clones can be obtained through reverse engineering (e.g., using an electron microscope to analyze layers) or by illegally acquiring the chip's design IP at various stages of the design and manufacturing process [00:09:59]. While functionally similar, cloned chips often deviate from the original in technology and process, potentially leading to erratic behavior [00:10:32].

## [[methods_of_detecting_counterfeit_chips | Methods of Detecting Counterfeit Chips]]

Counterfeit chips often enter products because contractors lack documented supply chain history or fail to conduct thorough inspections [00:10:50]. There are two primary [[methods_of_detecting_counterfeit_chips | methods of inspecting potentially counterfeit chips]]:

### [[methods_of_detecting_counterfeit_chips | Physical Methods]]
These methods examine defects directly related to a chip's physical properties, including its exterior, shipping/packaging, connections, IC packaging, bonding wires, or die [00:11:16]. Techniques include:
*   External Visual Inspection (EVI) [00:11:32].
*   More invasive methods like X-ray [00:11:35].
*   De-lidding the chip to expose its internal components (often destructive) [00:11:35].

### [[methods_of_detecting_counterfeit_chips | Electrical Methods]]
These methods test for changes in a chip's component parameters (parametric tests) or whether the chip functions properly (functional tests) [00:11:46]. While often effective, they tend to be time-consuming and expensive [00:11:56].

Detecting counterfeits is challenging due to nuances, such as distinguishing normal physical defects from signs of remarking [00:12:04]. Balancing detection against financial and time concerns is crucial, leading to best practices that aim for high test coverage rather than total assurance [00:12:14].

## Proactive Anti-Counterfeiting Design Measures

To combat recycling and package remarking, fabulous designers can integrate "designed for counterfeit measures" (DfCM) into their chip designs [00:12:33].

*   **Unique ID**: A simple measure is to embed a unique, non-programmable ID into the chip that can be easily read throughout its lifetime [00:12:41].
*   **Physical Unclonable Feature (PUF)**: This creates a unique "fingerprint" for the chip [00:12:52]. An example is an Arbiter PUF, which uses random variables from the semiconductor fabrication process to produce a circuit [00:12:58]. When a signal ("challenge") is sent through, it generates a random but repeatable output, similar to a two-step authentication app [00:13:06].
    *   *Side Note*: Some blockchain proposals leverage PUFs with blockchain's traceability and immutability to track a chip's supply chain history [00:13:37].

While these advanced methods are effective, implementation can be prohibitively difficult due to cost, technical reasons, or lack of space on the chip [00:13:28]. These schemes require broad acceptance and collaboration among various industry players [00:13:50].

## Root Causes and Incentives

The primary reasons counterfeit chips, especially recycled ones, enter the supply chain are opportunity and incentive [00:14:00].
*   In 2019, only 17.4% of the world's electronic waste was documented as collected and recycled [00:14:06].
*   Harvesting and desoldering old chips from e-waste can cost as little as 10 cents per chip [00:14:20].
*   Certain types of chips can then be resold for $1 to $10 per chip, offering a potential profit of up to 100 times the harvesting cost [00:14:27].

This strong economic incentive, combined with massive imports of improperly managed e-waste from developed regions like the United States and Europe, fuels the counterfeit chip problem [00:14:37].

### Shifting E-Waste Management
Historically, most fake recycled and relabeled chips originated from China, where the majority of e-waste was processed [00:15:05]. However, in 2017, China banned the import of 24 types of solid waste, including plastic and e-waste [00:15:10]. While some e-waste is still smuggled into China, significant imports have been redirected to other countries. For instance, Thailand saw a 5.7-fold increase in e-waste imports in 2017 following China's ban [00:15:17].

The proper functioning of semiconductors is crucial for modern society, impacting everything from military equipment to vehicles [00:14:51]. A counterfeit chip can lead to serious harm [00:15:01].