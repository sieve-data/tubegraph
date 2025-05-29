---
title: Definitions and Types of Counterfeit Semiconductors
videoId: 7epnv43jGV8
---

From: [[asianometry]] <br/> 

Counterfeit semiconductors pose a significant risk in critical situations, as evidenced by an F-16 ejection seat malfunction in 2020 where an investigation found counterfeit microchips within the sequencer [00:00:02]. While the exact role of these chips in that specific incident remained unclear, it highlighted the problem [00:00:16].

## Definitions of Counterfeit Semiconductors

The definition of a counterfeit semiconductor can be broad [00:00:54].

### Department of Defense (DoD) Definitions
A memo from the Department of Defense (DoD) provides two simple definitions [00:00:57]:
1.  A previously used electronic part sold as new [00:01:03].
2.  Unauthorized copies of an authentic electronic product [00:01:05].

### Industry Taxonomy
The industry uses a more comprehensive taxonomy, identifying a semiconductor as counterfeit if it meets any of the following criteria [00:01:19]:
1.  It is an unauthorized copy [00:01:21].
2.  It does not conform to the original manufacturer's design, model, or performance standard [00:01:27].
3.  It is not produced by the original manufacturer or its authorized contractors [00:01:34].
4.  It is off-specification, already used, defective, or misleadingly labeled as new [00:01:40].
5.  It is incorrectly marked or has wrong documentation [00:01:46].

## Types of Counterfeit Semiconductors

The types of counterfeited semiconductors span a wide range, including microprocessors, analog chips, memory, and radio frequency chips [00:03:46].

### Recycled Chips
Recycling is one of the most common ways counterfeit chips enter the supply chain [00:06:37]. The process typically involves [00:06:42]:
1.  Receiving scrap electronics [00:06:44].
2.  Cracking open casings and removing printed circuit boards [00:06:46].
3.  Heating circuit boards over an open flame to melt solder and loosen components [00:06:51].
4.  Bashing boards against a hard surface to make components fall out [00:06:57].
5.  Removing original markings from components using various methods [00:07:01].
6.  Sorting and reprocessing the components [00:07:06].
7.  Applying new coats and markings to make chips appear new [00:07:08].

These E-waste components are often old and worn out, and the harvesting process subjects them to further damage and stress, frequently rendering them non-functional [00:07:15]. Worldwide, in 2019, only 17.4% of electronic waste was formally collected and recycled, with the rest often harvested to produce fake semiconductor components [00:14:06]. Harvesting and de-soldering old chips from E-waste can cost as little as 10 cents per chip, while some chips can sell for $1 to $10, offering significant profit margins [00:14:20]. Historically, most fake recycled and relabeled chips originated from China due to the volume of E-waste directed there, though China's 2017 ban on solid waste imports has shifted some E-waste processing to other countries like Thailand [00:15:04].

### Relabeled or Remarked Chips
Relabeled or remarked chips are those that do not match their stated specifications [00:07:30]. Markings on chips provide information about their model, origin, and certifications [00:07:34]. Changing these markings misleads users about the chip's capabilities and quality [00:07:39]. This can involve wiping away original markings and adding new ones to make chips appear more premium or expensive [00:07:51]. This has consequences, especially in applications like military components that require hardening against radiation or temperature damage, where commercial parts might be substituted for more expensive, enhanced ones [00:08:01]. Together, recycling and remarking account for about 80% of all counterfeiting incidents [00:08:23].

### Foundry Overproduction
Many semiconductor companies contract out their chip production to foundries, often overseas and without third-party oversight [00:08:32]. Sometimes, a foundry may produce more chips than contracted for [00:08:45]. This might be to improve reported yield numbers or to illegally resell the excess production as counterfeits, benefiting from the design customer's significant R&D investment without incurring those costs themselves [00:08:51].

### Unauthorized Clones
Unauthorized clones are similar to foundry overproduction but involve a third party creating copies of chips to avoid the expensive R&D of developing their own designs [00:09:36]. This practice has historical parallels, such as East Germany and the Soviet Union cloning Western chips and computers [00:09:52].
Design IP for these clones can be obtained through [00:09:57]:
*   **Reverse engineering:** Using tools like electron microscopes to analyze the chip's layers [00:10:01]. This is more difficult for complex chips [00:10:07].
*   **Illegally acquiring design IP:** This can happen at any stage of the chip design and manufacturing process, for example, by copying RTL code from a design house [00:10:11].

Clone semiconductor counterfeits are harder to detect because they are often functionally similar to authentic parts [00:10:31]. However, they may deviate from the original in technology and process, leading to erratic behavior in practice [00:10:39].

## Factors Contributing to Counterfeit Entry

Fake chips often enter products when contractors lack documented supply chain history or fail to thoroughly inspect products [00:10:49]. For instance, in the case of a counterfeit FPGA in a P-8A Poseidon plane, the supplier should have more closely inspected the components purchased from their Chinese supplier [00:11:00].

Contractors, especially those in the defense sector, often face the challenge of needing to use older parts for repair and maintenance [00:05:03]. For instance, parts for an F-15 plane, introduced over 45 years ago, are no longer made by original suppliers [00:05:15]. This forces reliance on potentially "shady secondhand suppliers," making their situation understandable [00:05:37]. Nevertheless, the US government holds contractors responsible for detecting and filtering out these counterfeit chips, threatening civil and criminal penalties under laws like the National Defense Authorization Act signed in 2013 [00:05:44]. An example is Vision Tech in Florida, which knowingly sold fake chips, making nearly $16 million before legal action [00:06:01].

## [[Detection and Prevention of Counterfeit Semiconductors | Detection and Prevention of Counterfeit Semiconductors]]

Detecting potentially counterfeit chips involves two main methods [00:11:09]:
*   **Physical methods:** These look for defects related to the chip's physical properties, such as its exterior, packaging, connections, bonding wires, or die [00:11:16]. Techniques include external visual inspection (EVI), X-rays, or even de-capping the chip [00:11:31]. Some of these are destructive [00:11:40].
*   **Electrical methods:** These test for changes in the chip's component parameters (parametric tests) or whether the chip functions properly (functional tests) [00:11:46]. These are effective but time-consuming and expensive [00:11:56].

Ultimately, detecting counterfeits is a nuanced challenge, balancing the ability to distinguish normal physical defects from signs of tampering with financial and time constraints [00:12:02]. Best practices involve designing tests that provide high confidence rather than total assurance [00:12:17].

[[challenges_in_semiconductor_manufacturing | Fabless designers]] can also add "designed for counterfeit measures" to their chip designs [00:12:33]. Examples include:
*   **Unique IDs:** Programming a unique, non-programmable ID into the chip that can be easily read throughout its lifetime [00:12:41].
*   **Physical Unclonable Features (PUFs):** Creating a unique "fingerprint" for the chip using random variables from the semiconductor fabrication process, such as an Arbiter PUF [00:12:50]. This produces a random but repeatable output for a given challenge [00:13:06].