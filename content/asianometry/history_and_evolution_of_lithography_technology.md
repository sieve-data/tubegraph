---
title: History and evolution of lithography technology
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 

An optical lithography machine is essentially a $150 million camera that uses high-energy light to transfer a complex chip design pattern onto a wafer, typically made of silicon <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The precision required for these machines is astounding; for example, an ASML machine positions a wafer for DUV or [[the_evolution_of_euv_lithography | EUV]] exposure to within a few nanometers <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Lithography Workflow
The general workflow involves applying photoresist – a light-sensitive polymer chemical – onto the wafer using a spin-coating method <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. After preparatory steps, the wafer enters the lithography exposure tool <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Inside the tool, key sub-components include:
*   **Light source and Condenser Lens**: Together, these form the illumination system, which delivers light widely, evenly, and with adequate intensity to transfer the pattern <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Illumination is critical, with ASML dedicating multiple mirrors in its [[the_evolution_of_euv_lithography | EUV]] machine to this function, even at the cost of power reduction <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Photomask (or Reticle)**: This contains the chip design pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Initially, whole masks held the entire design, but as designs grew more complex, "reticles" (portions of the design) became common, and the terms are now used interchangeably <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The reticle is placed on a positioning table to compensate for errors <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Objective Lens**: This collects, focuses, and shrinks the light before it strikes the photoresist-coated wafer <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

The process results in a 3D relief of a portion of the chip's design, which can then be made permanent using etch processes <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Wafer Positioning Challenges
The wafer and its stage are substantial, with a 300mm wafer and stage weighing about 15 kilograms <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This platform must move wafers extremely quickly while also being capable of abrupt stops and holding absolutely still during exposure, with margins of only a few nanometers <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Machines require excellent "overlay," meaning the relative position of any pattern layer to others, which can be just a few nanometers as a percentage of feature size <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. These requirements become even stricter with multi-patterning, where multiple exposures create smaller lines <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

The wafer stage can accelerate up to 20 G-forces, three times the maximum force on a Formula 1 car <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Despite these rapid movements, the system must avoid vibrations, which would compromise precision and cause errors <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## [[evolution_of_lithography_and_optics_systems | Evolution of Lithography Movement Systems]]

### Early Systems and Hydraulic Motors
[[technological_advances_in_lithography_tools_by_asml | ASML]] originated from Philips in the Netherlands, drawing on Philips' long history in semiconductor development <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Philips' NatLab ("Natuurkundig Laboratorium") developed the pioneering lithography machine, the Silicon Repeater <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Early Philips wafer steppers, like the PAS 2000, used "hydraulic linear motors" to move wafer stages <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. These systems used high-pressure oil to generate movement <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. While precise, hydraulics lacked reliability due to the risk of oil leaks, which would be catastrophic in a cleanroom fab <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Despite strong seals, customers rejected these products, contributing to [[technological_advances_in_lithography_tools_by_asml | ASML]]'s difficult early years <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Following a lab incident involving a burst hydraulic oil pump, the team shifted to electrically-driven systems <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Electrically-Driven Systems
Philips leveraged its experience from developing precursors to optical disk technologies like the Compact Disc <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Their earlier work on video gramophones led to the replacement of physical styluses with contact-less optical lasers, requiring small, precise linear motors to read information from disks <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

NatLab engineers realized these linear motors could be applied to position silicon wafers <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Linear motors convert electricity directly into movement without a rotor, utilizing the Lorentz Law (interaction of electric and magnetic fields) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This approach proved highly successful, and [[technological_advances_in_lithography_tools_by_asml | ASML]] machines became known for their [[precision_movement_and_positioning_in_lithography | precise maneuvering]] <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Mechanical Guides and Aerostatic Systems
Some tools, like Canon's FPA-2000 photolithography machine (introduced in 1992 for the 500-nanometer process node), used mechanical guides akin to rails <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. However, these computer-controlled systems suffered from alignment errors due to friction, which also caused wear on mechanical bearings, leading to costly downtime for replacements <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

In the 1990s and early 2000s, the industry implemented "aerostatic systems" <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. This involved creating a thin film of extremely dry air between the wafer stage and a granite slab, similar to an air hockey table <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This air cushioning reduced friction and vibrations <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. For tracking stage positioning, [[technological_advances_in_lithography_tools_by_asml | ASML]] used interferometers, which are lasers reflecting off a mirror on the stage <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Additional calculations were needed to compensate for the air's refractive index, which changed with stage movement and could cause errors of up to 1 nanometer <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### Magnetic Levitation
While air-based systems performed well for years, the advancing cleanliness benchmarks, particularly for [[the_evolution_of_euv_lithography | EUV]], eventually necessitated a vacuum environment <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. As air systems are not viable in a vacuum, [[technological_advances_in_lithography_tools_by_asml | ASML]] began transitioning to magnetic levitation for suspending wafer stages in the late 2000s <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

In a 2017 design, the wafer stage rested on a 1,400-kilogram magnet plate array containing over 2,200 magnets, precision-placed to within 20 micrometers <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Of these, 1,457 magnets were arranged in a Halbach array, which strengthens the magnetic field on one side while canceling it on the other <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. For metrology, [[technological_advances_in_lithography_tools_by_asml | ASML]] shifted from lasers bouncing off the stage sides to lasers firing down from a grid mounted over the stages <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. For NXT immersion systems (which are not in a vacuum), metrology lasers now travel only 15 millimeters instead of up to 300 millimeters, simplifying air refractive index calculations and improving overlay <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. Challenges with magnetic levitation include dealing with errant magnetic fields interfering with the wafer and cooling requirements that might impede movement <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

### Fine and Coarse Movement Systems
Typical lithography machines employ two movement systems:
*   **Coarse Stage**: Transports wafers between workstations, using "long-stroke" motors designed for extended range (about 1 meter) and high speed <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Fine Stage**: Prioritizes precision over distance, using "short-stroke" actuators, often voice coil motors <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

These systems are often stacked, with the fine stage on top of the coarse stage, which can cause weight issues as more stacking is needed <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Proposals exist for single mag-lev systems to generate both short and long-stroke movements, eliminating the stacked design and saving space and weight <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## The TWINSCAN Platform
As the industry moved from 200mm to 300mm wafers and to smaller nodes in the 2000s, lithography machines needed re-engineering to handle larger, heavier wafers at the same speeds while processing smaller features <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. In response, [[technological_advances_in_lithography_tools_by_asml | ASML]] created the TWINSCAN platform, their main brand of lithography machine <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

The TWINSCAN operates on a dual-stage cycle: measurement and exposure <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. Two wafers are clamped on each stage using electrostatic forces <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
1.  **Measurement Stage**: The machine runs a series of scans to prepare wafer alignment relative to the reticle, ensuring good focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
2.  **Exposure Stage**: The stages swap, and the measured wafer goes under the lens for light exposure <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. During the swap, the machine can exchange the reticle <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Wafer movements in the TWINSCAN are coordinated by the Control Architecture Reference Model (CARM) motion control platform, powered by FPGAs and process controllers <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

Prior to TWINSCAN, lithography machines performed all measurement, alignment, and exposure steps sequentially on a single wafer <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The dual-stage setup was a major engineering feat, requiring the tool's architecture to be reworked to balance new weight and mass and handle vibrations from two simultaneous processes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This necessitated isolating the lens and metrology equipment (on the metrology frame) from the rest of the tool's main frame using air-bearings <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

A key factor for throughput benchmarks is the measurement stage, not exposure <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, a DUV machine processing 175 wafers per hour exposes each wafer for only 20 seconds of a 2-minute cycle, with the rest of the time spent on measurement <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The exposure stage adds economic value, but the wafer needs to be "pretty much complete" before exposure <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### TWINSCAN Product Categories
Today, the TWINSCAN name encompasses several product categories <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:
*   **NXE**: Used for [[the_evolution_of_euv_lithography | EUV lithography]] (e.g., NXE:3350 processes 125 wafers per hour) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **NXT**: Uses 193-nanometer ArF DUV light <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **XT**: Uses 248-nanometer KrF DUV light <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

The numbers in the machine names relate to their [[evolution_of_lithography_and_optics_systems | optics systems]] and lenses <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. These machines are modular, built to customer requirements like PCs, and are designed to receive upgrades over decades in customer fabs to keep up with modern demands <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

## The Role of Software
Software plays a crucial role in modern lithography. From 1989 to 2000, the number of CPUs and sensors in [[technological_advances_in_lithography_tools_by_asml | ASML]]'s tools grew six and eight times, respectively <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. The 1989 PAS5000 stepper had 200 million lines of source code, including comments, while the 2003 TwinScan had 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. This aggressive leveraging of software, with the team doubling in size every four years, is a key driver behind [[technological_advances_in_lithography_tools_by_asml | ASML]]'s strong performance <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.