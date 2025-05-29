---
title: ASML lithography machine operation and precision
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 
An [[ASMLs role in semiconductor manufacturing | ASML]] machine must position a wafer for DUV or EUV exposure to within a few nanometers, which is the margin of error that inspired this video <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. A human hair is 50,000 to 100,000 nanometers wide, a virus is 20 to 300 nanometers wide, and a fingernail grows 1 nanometer each second <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The precision required is immense <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. The movement of the wafer is primarily achieved using magnets <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## How an Optical Lithography Machine Works
An optical lithography machine is a $150 million camera that uses high-energy light to transfer a complex chip design pattern onto a wafer, typically made of silicon <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

The process involves several steps:
1.  **Photoresist Application** A light-sensitive polymer chemical, called photoresist, is applied to the wafer using the spin-coating method <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
2.  **Lithography Exposure** After preparatory steps, the wafer enters the lithography exposure tool <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
3.  **Internal Components** Inside the tool are several sub-components:
    *   **Illumination System** Consisting of the light source and condenser lens, its job is to deliver light widely, evenly, and intensely enough to transfer the pattern <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. [[ASMLs role in semiconductor manufacturing | ASML]] dedicates multiple mirrors in its EUV machine to illumination, despite significant power reduction <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
    *   **Photomask/Reticle** The illuminated light then passes through or bounces off the photomask (also known as a reticle), which contains the chip design pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Early designs used a whole mask for the whole chip, but as designs grew more complex, "reticles" (portions of the design) became common, leading to interchangeable use of the terms <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The reticle is placed on a positioning table and can be exchanged by a robot to compensate for natural errors <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
    *   **Objective Lens** This lens collects, focuses, and shrinks the light <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  **Wafer Exposure** The light then strikes the resist-coated wafer, creating a 3D relief of a portion of the chip's design <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This design can later be made permanent using etch processes <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Precision Challenges
The wafer and its stage are heavy; a 300-millimeter wafer and stage weigh about 15 kilograms <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This platform must move extremely quickly, stop abruptly, and hold absolutely still during exposure, within nanometers of margin <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

Critical precision requirements include:
*   **Overlay** The relative position of any pattern layer relative to others, which can be just a few nanometers. Errors can damage the device or cause short-circuits <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Multi-patterning** Overlay requirements become even stricter when using multiple exposures to create smaller lines than previously possible <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Acceleration and Vibrations** The wafer stage can accelerate to 20 G-forces (twenty times the force of gravity), which is three times a Formula 1 car's maximum force or twice a jet fighter's <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Despite these fast movements, the system must not cause vibrations, which would throw off precision targeting <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## History of Movement Systems
[[ASMLs rise in the lithography industry | ASML]] evolved from Philips in the Netherlands, inheriting Philips' long history of building semiconductors <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Philips' NatLab in Eindhoven produced the pioneering Silicon Repeater lithography machine <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Hydraulic Linear Motors
Early Philips wafer steppers, like the PAS 2000, used "hydraulic linear motors" to move wafer stages <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. These systems used high-pressure oil pumps to generate movement <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. While precise, they lacked reliability. Leaks in a cleanroom fab would be devastating, and strong seals made the devices bulky, contributing to [[ASMLs rise in the lithography industry | ASML]]'s difficult early years <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. After a lab incident with a burst hydraulic oil pump, the team decided to explore electrically-driven systems <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Electrically-Driven Systems
Philips leveraged its experience from developing optical disk technologies like the Compact Disc <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. For video disks, they replaced the physical stylus with a contact-less optical laser, which required small, precise linear motors to control the unit reading information from the disk <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

Linear motors convert electricity directly to movement without a rotor, using the Lorentz Law to exploit interactions between electric and magnetic fields <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. NatLab engineers realized these same technologies could position silicon wafers, leading to [[ASMLs role in semiconductor manufacturing | ASML]] machines being known for their precise maneuvering <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### The TWINSCAN Platform
As the industry moved to 300-millimeter wafers and smaller nodes in the 2000s, lithography machines needed re-engineering to handle larger, heavier wafers at the same speeds while processing smaller features <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. To address these issues, [[ASMLs role in semiconductor manufacturing | ASML]] created the TWINSCAN platform <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

## Meet the TWINSCAN
The TWINSCAN operates on a dual-stage cycle: measurement and exposure <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### Operation
*   **Dual Stages** During operation, there is a wafer on each stage, clamped using electrostatic forces <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. The chuck has tens of thousands of burls to reduce direct contact to only 2% of the wafer surface, cutting contamination risk <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Wafer Handling** A robot, the wafer handler, loads and unloads wafers <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Measurement Stage** Wafers first go through the measurement stage, where the machine performs scans to prepare how to align the wafer relative to the reticle, ensuring good focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Stage Swap** The machine then swaps the stages, rotating the wafers <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The measured wafer moves under the lens for light exposure <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The downtime during the swap can be used to exchange the reticle, though this requires a new alignment step <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Control System** Wafer movements in the TWINSCAN are coordinated by the Control Architecture Reference Model (CARM) motion control platform, powered by FPGAs and process controllers in an external cabinet rack <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

### Engineering Feat
Prior lithography machines performed measurement, alignment, and exposure sequentially on a single wafer <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Implementing the dual-stage setup was a major engineering project <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It required reworking the tool's architecture to re-balance weight and mass, and to handle vibrations from two simultaneous processes <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The lens and metrology equipment, mounted on the metrology frame, had to be isolated from the tool's main frame using air-bearings, which use highly pressurized gas to reduce friction <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Importance of Measurement
Throughput benchmarks depend not on the exposure stage, but on the measurement stage <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, a DUV machine processing 175 wafers per hour spends only 20 seconds exposing each wafer during a 2-minute cycle; the rest of the time is spent on measurement <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. This highlights that while exposure adds economic value, precise measurement is crucial for a competitive machine <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### TWINSCAN Today
The TWINSCAN name encompasses several product categories today <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:
*   "NXE" machines perform [[ASML and the commercialization of EUV lithography | EUV lithography]] <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   "NXT" machines use 193-nanometer ArF DUV light <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   "XT" machines use 248-nanometer KrF DUV light <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

An NXE:3350 EUV machine can process 125 wafers an hour, while sophisticated DUV machines can do 200-300 wafers <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The numbers in the machine names relate to their optics systems and lens <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. Machines are built modularly to customer requirements, like PCs, to allow for upgrades over decades of use in fabs <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

## Fine and Coarse Movement Systems
A typical lithography machine contains two movement systems <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>:
*   **Coarse Stage** Transports the wafer between workstations <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. It uses "long-stroke" motors designed for extended range (about 1 meter) and high speed <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Fine Stage** Prioritizes precision over distance <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. It uses "short-stroke" actuators, often voice coil motors <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

These systems are often stacked (fine stage on top of coarse stage), which has caused weight issues as more stacking and movements are needed <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## Generating Movements: Technological Progress
Precision movement technologies within the machine have evolved significantly <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

### Mechanical Systems
Early machines, like old Philips Wafer Steppers, used mechanical systems such as hydraulic linear motors <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. Canon's FPA-2000 photolithography machine (1992) for the 500-nanometer process node used mechanical guides, similar to stacked rails <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. However, these computer-controlled systems suffered from unexpected alignment errors due to friction, which also caused wear on mechanical bearings, requiring expensive downtime and human intervention <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Aerostatic Systems
During the 1990s and early 2000s, the industry implemented "aerostatic systems" <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. This involved creating a thin film of extremely dry air between the wafer stage and a granite slab, akin to an air hockey table puck <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This air cushioning reduced friction and vibrations <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

For these machines, [[ASMLs role in semiconductor manufacturing | ASML]] used interferometers to track stage positioning, employing lasers reflecting off a mirror on the side of the stage <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Additional calculations were needed to compensate for the air's refractive index, which changed as the stage moved, causing unacceptable 1-nanometer errors <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. While air-based systems performed well for years, cleanliness benchmarks for EUV eventually necessitated a vacuum, rendering air systems unviable <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

### [[magnetic_levitation_and_precision_movement_in_lithography_machines | Magnetic Levitation]]
In preparation for vacuum environments, [[ASMLs role in semiconductor manufacturing | ASML]] began switching to suspending their wafer stages using [[magnetic_levitation_and_precision_movement_in_lithography_machines | magnetic levitation]] in the late 2000s <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

Key aspects of the [[magnetic_levitation_and_precision_movement_in_lithography_machines | magnetic levitation]] system:
*   The wafer stage rests on a 1,400-kilogram magnet plate array containing over 2,200 magnets, precision-placed to within 20 micrometers <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   1,457 of these magnets are arranged in a Halbach array, which strengthens the magnetic field on one side while canceling it on the other <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   For metrology, [[ASMLs role in semiconductor manufacturing | ASML]] shifted from lasers bouncing off the sides of wafer stages to lasers firing down from a grid mounted over the stages <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   For NXT immersion systems (not in a vacuum), metrology lasers travel a shorter distance (15 millimeters versus up to 300 millimeters previously), simplifying air refractive index calculations and improving overlay <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

Challenges include dealing with errant magnetic fields that interfere with the wafer and cooling requirements that might need umbilical cords impeding movement <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Proposals exist for a single mag-lev system to generate both short and long-stroke movements, eliminating the stacked fine/coarse stage system and saving space and weight, though current documentation still shows separate electromagnetic motors for these movements <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## Role of Software
The [[role of software in ASML machine development | role of software]] in [[ASMLs role in semiconductor manufacturing | ASML]]'s tools has grown significantly <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. From 1989 to 2000, the number of CPUs and sensors in [[ASMLs role in semiconductor manufacturing | ASML]]'s tools increased six and eight times, respectively <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. The 1989 PAS5000 stepper had 200 million lines of source code, while the 2003 TwinScan had 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. This aggressive leveraging of [[role of software in ASML machine development | software]], with the team doubling in size every four years, is likely a key driver behind [[ASMLs role in semiconductor manufacturing | ASML]]'s strong performance <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.