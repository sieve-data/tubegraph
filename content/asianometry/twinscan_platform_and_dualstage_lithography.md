---
title: TWINSCAN platform and dualstage lithography
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 

[[ASML and highvolume EUV systems | ASML]] lithography machines are renowned for their incredible precision, positioning a wafer with nanometer-level accuracy for ultraviolet light exposure <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. To put this in perspective, a human hair is 50,000 to 100,000 nanometers wide, and a fingernail grows 1 nanometer per second <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The ability to move and stop a 15-kilogram wafer stage precisely to within a few nanometers, sometimes while accelerating at 20 G-forces, is a core challenge that the TWINSCAN platform addresses <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## How Optical Lithography Works

An optical lithography machine functions as a highly sophisticated camera, valued at approximately $150 million <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Its primary purpose is to transfer intricate chip designs onto a silicon wafer using high-energy light <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

The process involves several key steps and components within the lithography exposure tool <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>:
*   **Photoresist Application** The wafer is first coated with a light-sensitive polymer chemical called photoresist, typically applied using a spin-coating method <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Illumination System** This system consists of a light source and a condenser lens, designed to deliver light widely, evenly, and with adequate intensity to transfer the pattern <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. In [[Extreme Ultraviolet Lithography and its Challenges | EUV machines]], [[ASML and highvolume EUV systems | ASML]] utilizes multiple mirrors for illumination, despite significant power reduction <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Photomask (Reticle)** The illuminated light then interacts with a photomask, or reticle, which holds the chip design pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. While early masks contained the entire design, modern "reticles" represent a portion of the chip design, and the terms are often used interchangeably <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Reticles are placed on a positioning table and can be exchanged automatically by a robot <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Objective Lens** This lens collects and focuses the light, shrinking the image before it strikes the photoresist-coated wafer <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Pattern Transfer** If executed correctly, this process creates a 3D relief of a portion of the chip's design on the wafer, which can then be made permanent through etch processes <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Engineering Challenge: Precision Movement

The wafer and its stage are substantial, with a 300-millimeter wafer and stage weighing around 15 kilograms <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This platform must move wafers at high speeds, yet stop abruptly and hold perfectly still during exposure with a margin of error of only a few nanometers <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Key requirements for precision movement include:
*   **Overlay** This refers to the relative position of any pattern layer compared to others. Errors, even of a few nanometers (calculated as a percentage of feature size), can damage device capabilities or cause short-circuits <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Overlay requirements become even stricter with "multi-patterning," where multiple precise exposures create smaller lines <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Vibration Control** Despite accelerating to 20 G-forces (three times a Formula 1 car's maximum force), the system must execute movements without causing vibrations, which would compromise precision <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Historical Evolution Leading to TWINSCAN

[[ASMLs rise in the lithography industry | ASML]] originated from Philips in the Netherlands, inheriting a long history of semiconductor manufacturing <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Philips' NatLab ("Natuurkundig Laboratorium") developed pioneering machines like the Silicon Repeater <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Early Philips wafer steppers, such as the PAS 2000, used "hydraulic linear motors" for wafer stage movement <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. While precise, hydraulics lacked reliability; leaks in a cleanroom fab were devastating, and attempts to create strong seals made the devices bulky, contributing to [[ASMLs rise in the lithography industry | ASML]]'s challenging early years <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

Following a lab incident involving a burst hydraulic oil pump, the team shifted to electrically-driven systems <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. They leveraged Philips' experience with optical disk technologies, like the Compact Disc, which used contact-less optical lasers instead of physical styluses <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This required small, precise linear motors to control the reading unit <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

Linear motors convert electricity directly into movement without a rotor, utilizing the Lorentz Law and the interaction of electric and magnetic fields <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. NatLab engineers applied these principles to wafer positioning, leading to the highly precise maneuvering for which [[ASML and highvolume EUV systems | ASML]] machines are known <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

As the industry transitioned to larger 300-millimeter wafers and smaller process nodes in the 2000s <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>, machines needed re-engineering to accommodate heavier wafers at the same speeds and to process smaller features. This led to the creation of the TWINSCAN platform <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## The TWINSCAN Platform

The TWINSCAN platform is named for its dual-stage operation: **measurement** and **exposure** <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. During operation, two wafers are simultaneously present, one on each stage, clamped by electrostatic forces on a chuck with tens of thousands of burls to minimize contact and contamination risk <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

The workflow within the TWINSCAN is as follows:
1.  **Wafer Loading**: A robot, the wafer handler, loads or unloads wafers <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
2.  **Measurement Stage**: The first wafer undergoes a series of scans to prepare for alignment with the reticle, ensuring optimal focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
3.  **Stage Swap**: The machine swaps the stages, rotating the wafers. The measured wafer moves under the objective lens for exposure <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. During this swap, the reticle can be exchanged, though it requires a new alignment step <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
4.  **Exposure Stage**: The light source is activated until the required dose of light exposure is achieved <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

The entire wafer movement system is coordinated by the Control Architecture Reference Model (CARM) motion control platform, powered by FPGAs and process controllers <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

The dual-stage setup was a significant engineering feat. Prior to TWINSCAN, lithography machines performed all measurement, alignment, and exposure steps sequentially on a single wafer <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Implementing dual stages required:
*   **Architecture Rework**: Rebalancing the machine's frame to handle new weight and mass distribution <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Vibration Management**: Isolating the lens and metrology equipment (mounted on the metrology frame) from the main frame using air-bearings, which utilize highly pressurized gas to reduce friction <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Crucially, throughput benchmarks are primarily driven by the **measurement stage**, not the exposure stage <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, a DUV machine processing 175 wafers per hour spends only 20 seconds exposing each wafer out of a 2-minute cycle; the rest of the time is dedicated to measurement <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The precision of the measurement stage ensures the wafer is nearly complete before exposure, making its sequencing vital for competitive machine performance <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### TWINSCAN Today

Today, the TWINSCAN brand encompasses several product categories:
*   **NXE**: Machines performing [[Extreme Ultraviolet Lithography and its Challenges | EUV lithography]] <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For example, the NXE:3350 EUV machine can process 125 wafers per hour <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **NXT**: Machines using 193-nanometer ArF DUV light <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **XT**: Machines using 248-nanometer KrF DUV light <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Sophisticated DUV machines can process 200-300 wafers per hour <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

The numbers in the machine names relate to their optics systems and lenses <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. These machines are built in a modular fashion, allowing for upgrades to keep pace with modern requirements, as they are expected to operate in customer fabs for decades <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

## Wafer Movement Systems: Fine and Coarse

Lithography machines typically employ two distinct movement systems:
*   **Coarse Stage**: Transports the wafer between workstations. It uses "long-stroke" motors designed for extended range (around 1 meter) and high speed <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Fine Stage**: Prioritizes precision over distance. It uses "short-stroke" actuators, often voice coil motors, for minute adjustments <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

These systems are often stacked (fine stage on top of coarse stage) to achieve the required wide range of movements, which can introduce weight challenges <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## Evolution of Precision Movement Technologies

The evolution of precision movement in lithography machines reflects [[Development and history of ASML lithography technology | ASML]]'s continuous innovation:

*   **Mechanical Systems (Early Days)**: Early machines, like Philips Wafer Steppers or Canon's FPA-2000 (1992, for 500nm node), used mechanical guides (rails) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. However, friction caused alignment errors and wear, leading to expensive downtime and maintenance <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Aerostatic Systems (1990s-Early 2000s)**: The industry implemented "aerostatic systems" by creating a thin film of extremely dry air between the wafer stage and a granite slab, akin to an air hockey puck <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. This air cushioning reduced friction and vibrations <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
    *   **Metrology with Interferometers**: [[ASML lithography machine operation and precision | ASML]] used interferometers (lasers reflecting off a mirror on the stage) to track stage positioning <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
    *   **Refractive Index Compensation**: Calculations were needed to compensate for the air's refractive index, which changed with stage movement and could cause 1-nanometer errors <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Magnetic Levitation (Late 2000s)**: As [[Development of UV and EUV lithography technology | lithography]] advanced and [[Extreme Ultraviolet Lithography and its Challenges | EUV]] required vacuum environments, air systems became unviable <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. [[ASML and highvolume EUV systems | ASML]] transitioned to suspending wafer stages using magnetic levitation <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
    *   **Magnet Array**: The wafer stage sits on a 1,400-kilogram magnet plate array containing over 2,200 magnets, precisely placed within 20 micrometers <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
    *   **Halbach Array**: 1,457 of these magnets are arranged in a Halbach array, which strengthens the magnetic field on one side while canceling it on the other <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
    *   **Improved Metrology**: For NXT immersion systems (not in a vacuum), metrology lasers now fire downwards from a grid, reducing travel distance from 300 millimeters to 15 millimeters. This simplifies air refractive index calculations and improves overlay <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
    *   **Challenges**: Issues include errant magnetic fields interfering with the wafer and cooling requirements that might necessitate umbilical cords, impeding movement <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
    *   **Future Concepts**: There are proposals for a single mag-lev system to handle both short and long-stroke movements, eliminating the stacked fine/coarse stage system and saving space and weight <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. However, current documentation indicates separate electromagnetic motors are still used for these movements <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

## The Role of Software

Beyond the intricate mechanical and electromagnetic systems, software plays a critical role in [[ASML lithography machine operation and precision | ASML]]'s precision. From 1989 to 2000, the number of CPUs and sensors in [[ASML and highvolume EUV systems | ASML]]'s tools increased six and eight times, respectively <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. The 1989 PAS5000 stepper had 200 million lines of source code, while the 2003 TwinScan had 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. This aggressive leveraging of software, with the engineering team doubling in size every four years, is a key driver behind [[ASMLs rise in the lithography industry | ASML]]'s strong performance <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.