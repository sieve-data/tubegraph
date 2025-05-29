---
title: Magnetic levitation and precision movement in lithography machines
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 
A human hair is approximately 50,000 to 100,000 nanometers wide, a virus is about 20 to 300 nanometers wide, and a fingernail grows 1 nanometer each second <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Within this incredibly small scale, an [[ASML lithography machine operation and precision|ASML]] machine must position a wafer for deep ultraviolet (DUV) or extreme ultraviolet (EUV) exposure with precision to within a few nanometers <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This extreme accuracy is achieved largely through the use of magnets to hold and move the wafer <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

An optical lithography machine functions as a sophisticated camera costing around $150 million, using high-energy light to transfer complex chip designs onto a wafer, typically made of silicon <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The process involves applying a light-sensitive polymer chemical called photoresist to the wafer using spin-coating <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The wafer then enters the lithography exposure tool, which contains a light source, condenser lens, photomask (or reticle), and objective lens <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The photomask holds the chip design pattern and is placed on a positioning table for precise movement <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Precision Challenges in Wafer Movement

The wafer and its stage are substantial, with a fully loaded 300-millimeter wafer stage weighing about 15 kilograms <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This platform must move these heavy stages extremely quickly, stop abruptly, and hold absolutely still during exposure, all while maintaining nanometer-level precision <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

Key precision requirements include:
*   **Overlay**: The relative position of any pattern layer relative to others must be precise, often just a few nanometers <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Errors can damage the device or cause short-circuits <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Multi-patterning**: When multiple exposures are used to create smaller lines, overlay requirements become even stricter <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Acceleration and Vibration Control**: The wafer stage can accelerate up to 20 G-forces, yet the system must execute these rapid movements without causing vibrations that could disrupt precision targeting <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Evolution of Movement Technologies

[[ASML lithography machine operation and precision|ASML]] originated from Philips in the Netherlands, inheriting their long history in semiconductor manufacturing <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Philips' NatLab developed the pioneering Silicon Repeater lithography machine <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Early [[development_and_history_of_asml_lithography_technology|ASML]] wafer steppers, like the PAS 2000, initially used hydraulic linear motors to move wafer stages <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. While precise, hydraulics lacked reliability due to the risk of oil leaks in cleanroom environments, making them unacceptable to customers <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

Following a lab incident involving a burst hydraulic oil pump, the team explored electrically-driven systems <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. They leveraged Philips' experience with optical disk technologies, specifically the creation of small, precise linear motors for contact-less optical lasers <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Linear motors convert electricity directly to movement using the Lorentz Law, which describes the interaction of electric and magnetic fields <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This application to wafer positioning proved highly successful, and [[ASML lithography machine operation and precision|ASML]] machines became known for their precise maneuvering <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

In the 1990s and early 2000s, the industry moved from mechanical guides, which suffered from friction and wear, to "aerostatic systems" <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. These systems used a thin film of dry air between the wafer stage and a granite slab, like an air hockey puck, to reduce friction and vibrations <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. Interferometers (lasers) tracked stage positioning, though air's refractive index required complex calculations to maintain nanometer precision <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.

## The Shift to Magnetic Levitation

As [[Extreme Ultraviolet Lithography and its Challenges|EUV lithography]] required a vacuum environment for cleanliness, air-based systems became unviable <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. In the late 2000s, [[ASML lithography machine operation and precision|ASML]] began transitioning to suspending their wafer stages using magnetic levitation <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

In a modern magnetic levitation system, the wafer stage rests on a 1,400-kilogram magnet plate array containing over 2,200 magnets, precisely placed within 20 micrometers <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Of these, 1,457 magnets are arranged in a Halbach array, which strengthens the magnetic field on one side while canceling it on the other <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

For metrology (position tracking) in these mag-lev systems, [[ASML lithography machine operation and precision|ASML]] switched from lasers bouncing off the sides of wafer stages to lasers firing down from a grid mounted over the stages <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. For non-vacuum NXT immersion systems, shorter laser travel (15 millimeters versus up to 300 millimeters previously) simplified air refractive index calculations and improved overlay <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

Challenges with magnetic levitation include dealing with errant magnetic fields that could interfere with the wafer and devising cooling solutions that don't impede movement <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. There are proposals to use a single mag-lev system for both short and long-stroke movements, eliminating the stacked fine/coarse stage system and saving space and weight <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. However, current documentation still indicates separate electromagnetic motors for these different movements <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

## TWINSCAN Platform and Coordinated Movement

[[ASML lithography machine operation and precision|ASML]]'s primary lithography machine is the TWINSCAN platform, named for its dual-stage cycle of measurement and exposure <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Each stage holds a wafer, clamped by electrostatic forces on a chuck with tens of thousands of burls to minimize contact and contamination <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

The TWINSCAN workflow:
1.  **Measurement Stage**: A robot loads the wafer <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The machine performs scans to prepare how to align the wafer relative to the reticle for optimal focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
2.  **Exposure Stage**: The machine swaps the stages, rotating the wafers <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The measured wafer moves under the lens for light exposure <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. During the swap, the reticle can also be exchanged <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

The TWINSCAN's wafer movements are coordinated by the Control Architecture Reference Model (CARM) motion control platform, powered by FPGAs and process controllers <a class="yt-timestamp" data-t="00:07:58">[00:08:01]</a>. Unlike prior lithography machines that ran all steps sequentially on a single wafer, the dual-stage setup was a significant engineering feat <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. It required reworking the tool's architecture to balance new weight and mass, and to handle vibrations from two concurrent processes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The lens and metrology equipment, mounted on a "metrology frame," are isolated from the main tool frame using air-bearings to cut friction <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

Throughput benchmarks highlight the importance of the measurement stage: a DUV machine processing 175 wafers per hour spends only 20 seconds on exposure within a 2-minute cycle; the rest of the time is dedicated to measurement <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. [[ASML lithography machine operation and precision|ASML]] recognizes that precise execution during the measurement stage is crucial for a competitive machine <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Coarse and Fine Movement Systems

Lithography machines typically employ two distinct movement systems:
*   **Coarse Stage**: Transports wafers between workstations. These use "long-stroke" motors designed for extended range (about 1 meter) and high speed <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Fine Stage**: Prioritizes precision over distance. These use "short-stroke" actuators, often voice coil motors <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

These systems are often stacked (fine stage on top of coarse stage) to achieve the wide range of required movements, which can cause weight issues <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## The Role of Software

Beyond mechanical and magnetic precision, software plays an immense role in managing these complex movements <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. From 1989 to 2000, the number of CPUs and sensors in [[ASML lithography machine operation and precision|ASML]]'s tools grew six and eight times, respectively <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. The 1989 PAS5000 stepper had 200 million lines of source code, while the 2003 TwinScan had 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. This aggressive [[role_of_technology_and_innovation_in_lithography|leveraging of software]] is a key driver behind [[ASML lithography machine operation and precision|ASML]]'s strong performance <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.