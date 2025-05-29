---
title: Development and history of ASML lithography technology
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 

[[asml_lithography_machine_operation_and_precision | ASML machine]]s are renowned for their extreme precision, positioning wafers to within a few nanometers for DUV or [[development_of_uv_and_euv_lithography_technology | EUV]] exposure, a margin of error that is remarkably small given that a human hair is 50,000 to 100,000 nanometers wide and a virus is 20 to 300 nanometers wide <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. A fingernail grows approximately 1 nanometer per second <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Fundamentals of Optical Lithography

An optical lithography machine functions as a sophisticated camera, costing around $150 million <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Its primary purpose is to use high-energy light to transfer intricate chip design patterns onto a wafer, typically made of silicon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

The process involves several key steps and components:
1.  **Photoresist Application**: A light-sensitive polymer chemical, known as photoresist, is applied to the wafer using the spin-coating method <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
2.  **Lithography Exposure Tool**: After preparatory steps, the wafer enters the exposure tool <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
3.  **Sub-Components**: Inside the tool are the light source, condenser lens, photomask, and objective lens <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
    *   **Illumination System**: The light source and condenser lens form the illuminator, responsible for delivering light broadly, uniformly, and with sufficient intensity to transfer the pattern <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. [[asmls_rise_in_the_lithography_industry | ASML]] prioritizes illumination, dedicating multiple mirrors in its [[asml_and_highvolume_euv_systems | EUV machine]]s, even at the cost of power reduction <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
    *   **Photomask/Reticle**: The illuminated light passes through or reflects off the photomask (also known as a reticle), which holds the chip design pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. While early [[semiconductor industry | semiconductor industry]] masks held the entire design, modern designs use "reticles" representing a portion of the chip, though the terms are often used interchangeably <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Reticles are placed on a positioning table and handled by robots to compensate for natural errors <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
    *   **Objective Lens**: This lens collects, focuses, and shrinks the light image before it strikes the photoresist-coated wafer <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  **Pattern Formation**: Successful exposure creates a 3D relief of a part of the chip's design on the substrate, which can then be made permanent via etch processes <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Challenges in Wafer Positioning

The wafer and its stage present significant engineering challenges. A fully loaded 300-millimeter wafer stage weighs approximately 15 kilograms <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This platform must move wafers at extreme speeds, stop abruptly, and hold absolutely still with nanometer precision during exposure <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

Key requirements for precision:
*   **Overlay**: Machines need excellent "overlay," meaning the relative position of any pattern layer compared to others <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Overlay requirements can be just a few nanometers, and errors can compromise device functionality or cause short-circuits <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. These requirements become even stricter with multi-patterning, where multiple precisely positioned exposures create smaller lines <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Speed and Stability**: The wafer stage can accelerate up to 20 G-forces (20 times the force of gravity), which is significantly higher than a Formula 1 car or a jet fighter <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Despite these rapid movements, the system must avoid vibrations, which would disrupt precision targeting and cause errors <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## ASML's Historical Development

[[asmls_rise_in_the_lithography_industry | ASML]] originated from Philips in the Netherlands, drawing on Philips' extensive history in semiconductor manufacturing <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Early products were developed at Philips' NatLab ("Natuurkundig Laboratorium"), including the pioneering Silicon Repeater lithography machine <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Evolution of Wafer Stage Movement Systems

**Hydraulic Systems (Early Days)**
Some of Philips' first wafer steppers, such as the PAS 2000, used hydraulic linear motors to move wafer stages <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. These systems generated movement by pushing high-pressure oil through hoses and valves <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. While precise, hydraulics lacked reliability; any leak in a cleanroom fab would be catastrophic <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Despite efforts to build strong seals, customers rejected the product, contributing to [[asmls_rise_in_the_lithography_industry | ASML]]'s challenging early years <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. A high-profile lab incident involving a burst hydraulic oil pump prompted a shift to electrically-driven systems <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

**Electrically-Driven Systems (Leveraging Optical Disk [[role_of_technology_and_innovation_in_lithography | Technology]])**
Philips leveraged its experience from developing optical disk technologies, like the Compact Disc, to build the new system <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Their pursuit of a video gramophone led to replacing the physical stylus with a contact-less optical laser due to higher data density <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This required creating small, precise linear motors to control the unit reading reflected information from the disk <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

Linear motors convert electricity directly into movement without a rotor, utilizing the Lorentz Law (interaction of electric and magnetic fields) to generate motion forces <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. NatLab engineers realized this [[role_of_technology_and_innovation_in_lithography | technology]] could be applied to position silicon wafers, leading to successful systems known for their precise maneuvering <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### The TWINSCAN Platform

As the [[semiconductor industry | industry]] transitioned to larger (200mm to 300mm) and heavier wafers while simultaneously shrinking process nodes in the 2000s, [[asml_lithography_machine_operation_and_precision | ASML]] had to re-engineer its lithography machines <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This led to the creation of the TWINSCAN platform, [[asmls_rise_in_the_lithography_industry | ASML]]'s main brand of lithography machine <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

The TWINSCAN operates on a dual-stage cycle: measurement and exposure <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. It uses two wafer stages, each clamped and secured by electrostatic forces <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. The chuck minimizes direct contact to 2% of the wafer surface area using tens of thousands of burls, reducing contamination risk <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

Workflow within the TWINSCAN:
1.  **Wafer Loading**: A robot, the wafer handler, loads or unloads wafers <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
2.  **Measurement Stage**: The wafer starts on the measurement stage, where scans help computers align the wafer with the reticle for optimal focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
3.  **Stage Swap and Exposure**: The machine then swaps the stages, rotating the wafers <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The measured wafer moves under the lens, and the light source activates until the required dose of light exposure is achieved <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Reticle exchange can occur during the swap, though it necessitates a new reticle alignment step <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Wafer movements in the TWINSCAN are coordinated by the Control Architecture Reference Model (CARM) motion control platform, powered by FPGAs and process controllers <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Unlike prior machines that performed all steps sequentially on a single wafer, the dual-stage setup was a major engineering feat <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. It required reworking the tool's architecture to re-balance weight and mass on the machine's frame and managing vibrations from two simultaneous processes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The lens and metrology equipment, mounted on the metrology frame, are isolated from the main tool frame using air-bearings, which use highly pressurized gas to reduce friction <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

The measurement stage is crucial for throughput, not the exposure stage <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, a [[development_of_uv_and_euv_lithography_technology | DUV]] machine processing 175 wafers per hour spends only about 20 seconds of a 2-minute cycle on exposure; the rest is dedicated to measurement <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Just as a sushi master notes that "the sushi is 95% complete before the fish is brought out to me," the wafer is nearly ready before entering the exposure stage <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Thus, optimizing the measurement sequence is vital for [[asmls_rise_in_the_lithography_industry | ASML]] to deliver a competitive machine <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### TWINSCAN Product Categories

Today, the TWINSCAN brand includes several product categories:
*   **NXE**: Used for [[asml_and_the_commercialization_of_euv_lithography | EUV lithography]] <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. An NXE:3350 [[asml_and_highvolume_euv_systems | EUV machine]] can process 125 wafers per hour <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **NXT**: Uses 193-nanometer ArF [[development_of_uv_and_euv_lithography_technology | DUV]] light <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **XT**: Uses 248-nanometer KrF [[development_of_uv_and_euv_lithography_technology | DUV]] light <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Sophisticated [[development_of_uv_and_euv_lithography_technology | DUV]] machines can process 200-300 wafers per hour <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

The numbers in the machine names relate to their optics systems and lenses <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. Machines are built modularly to customer specifications, allowing for upgrades over decades of operation to meet evolving requirements <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Fine and Coarse Movement Systems

A typical lithography machine employs two distinct movement systems:
*   **Coarse Stage**: Transports the wafer between workstations <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Its motors are "long-stroke," designed for extended range (about 1 meter) and high speed <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Fine Stage**: Prioritizes precision over distance <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. It uses "short-stroke" actuators, often voice coil motors <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

These systems are often stacked (fine stage on top of coarse stage) to achieve the required wide range of movements, which can introduce weight issues as more stacking and movements become necessary <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## Evolution of Precision Movement Technologies

### Mechanical Systems (Early Machines)
Early machines, such as the Philips Wafer Stepper and Canon's FPA-2000 photolithography machine (for the 500 nanometer node, introduced in 1992), used mechanical guides (like rails) for wafer movement <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. However, these computer-controlled systems suffered from unexpected alignment errors due to friction, which accumulated into significant problems <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Over time, friction also wore down mechanical bearings, requiring expensive downtime and human intervention for replacement <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

### Aerostatic Systems (1990s - Early 2000s)
In response to mechanical system limitations, the [[semiconductor industry | industry]] adopted "aerostatic systems" in the 1990s and early 2000s <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. These systems created a thin film of extremely dry air between the wafer stage and a granite slab, akin to an air hockey puck <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This air cushioning reduced friction and vibrations from wafer stage movements <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

[[asmls_rise_in_the_lithography_industry | ASML]] used interferometers (lasers reflecting off a mirror on the stage) to track stage positioning <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Precision guidelines were so strict that additional calculations were needed to compensate for the refractive index of the air, which changed as the stage moved and could cause errors of up to 1 nanometer <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. While air-based systems performed well for many years, advancing lithography (especially [[asml_and_the_commercialization_of_euv_lithography | EUV]]) eventually required a vacuum environment, rendering air systems unviable <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

### Magnetic Levitation (Late 2000s - Present)
In preparation for vacuum requirements, [[asml_lithography_machine_operation_and_precision | ASML]] began transitioning to magnetic levitation for suspending wafer stages in the late 2000s <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

Current magnetic systems:
*   The wafer stage rests on a 1,400-kilogram magnet plate array containing over 2,200 magnets, precisely placed within 20 micrometers <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   1,457 of these magnets are arranged in a Halbach array, which strengthens the magnetic field on one side while canceling it on the other <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   For metrology, [[asml_lithography_machine_operation and precision | ASML]] switched from lasers bouncing off the sides of wafer stages to lasers firing down from a grid mounted above the stages <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. For NXT immersion systems (not in a vacuum), shorter laser travel distances (15 millimeters versus up to 300 millimeters previously) simplified air refractive index calculations and improved overlay <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

Challenges with magnetic designs include managing errant magnetic fields that could interfere with the wafer and cooling requirements that might involve umbilical cords or hoses impeding movement <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Proposals exist for a single mag-lev system to generate both short and long-stroke movements, potentially eliminating the stacked fine/coarse stage system and saving space and weight <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. However, current documentation still indicates separate electromagnetic motors for these distinct movements <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

## Role of Software

The increasing complexity and precision of [[asml_lithography_machine_operation_and_precision | ASML machine]]s have been significantly driven by the aggressive leveraging of [[role_of_software_in_asml_machine_development | software]] <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. From 1989 to 2000, the number of CPUs and sensors in [[asml_lithography_machine_operation_and_precision | ASML]]'s tools grew six and eight times, respectively <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. The 1989 PAS5000 stepper had approximately 200 million lines of source code, including comments, while the 2003 TwinScan had 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. The former CEO of [[asmls_rise_in_the_lithography_industry | ASML]] noted that the [[role_of_software_in_asml_machine_development | software]] team doubled in size every four years, indicating its critical role in the company's strong performance <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.