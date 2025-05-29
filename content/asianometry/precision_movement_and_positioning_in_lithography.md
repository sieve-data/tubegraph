---
title: Precision movement and positioning in lithography
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 

Precision movement and positioning are critical for semiconductor manufacturing, particularly in optical lithography. Modern lithography machines, such such as those by [[overview_of_asml_lithography_machines | ASML]], must position wafers with incredible accuracy to create microscopic features on chips <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

> [!INFO] Scale of Precision
> A human hair is approximately 50,000 to 100,000 nanometers wide <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
> A virus is about 20 to 300 nanometers wide <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
> A fingernail grows 1 nanometer each second <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
> [[overview_of_asml_lithography_machines | ASML]] machines must hit the exact right position to within a few nanometers <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## How Lithography Machines Operate

An optical lithography machine functions like a highly specialized camera, using high-energy light to transfer complex chip design patterns onto a wafer, typically made of silicon <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

The basic workflow involves:
1.  **Photoresist Application**: A light-sensitive polymer chemical called photoresist is applied to the wafer using a spin-coating method <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
2.  **Exposure Tool Entry**: The wafer then moves into the lithography exposure tool <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
3.  **Illumination System**: Inside, a light source and condenser lens (the illumination system) deliver light widely, evenly, and intensely <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. For example, [[euv_lithography_technology_and_its_challenges | ASML's EUV machine]] uses multiple mirrors for illumination <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
4.  **Photomask/Reticle**: The illuminated light passes through or bounces off a photomask (also called a reticle) which contains the chip design <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. An automatic robot handles mask exchanges <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
5.  **Objective Lens**: An objective lens collects, focuses, and shrinks the image <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
6.  **Wafer Exposure**: The light strikes the resist-coated wafer, creating a 3D relief of a portion of the chip's design <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This design is later made permanent with etch processes <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

Both the wafer and the reticle are placed on positioning tables to compensate for natural errors <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Challenges in Wafer Movement and Positioning
The wafer and its stage are heavy, with a 300-millimeter wafer and stage weighing about 15 kilograms <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
The platform must move these quickly, abruptly stop, and hold still during exposure stages <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
Key [[challenges_in_semiconductor_lithography | challenges]] include:
*   **Precision Overlay**: Machines need excellent "overlay," meaning the relative position of any pattern layer relative to others. This can be as precise as a few nanometers <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Errors damage device capabilities or cause short-circuits <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Multi-patterning**: Requirements become stricter for multi-patterning, where multiple exposures are used to create smaller lines <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **High Acceleration**: The wafer stage can accelerate up to 20 G-forces (twenty times the force of Gravity) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This is three times the maximum force on a Formula 1 car and twice that of a jet fighter <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Vibration Control**: Fast movements must be executed without causing vibrations, which would throw off precision <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## [[evolution_of_lithography_and_optics_systems | Evolution of Movement Systems]]

[[overview_of_asml_lithography_machines | ASML]] originated from Philips, with its first lithography machine, the Silicon Repeater, developed at Philips' NatLab in Eindhoven <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Hydraulic Linear Motors
Early Philips wafer steppers, like the PAS 2000, used hydraulic linear motors to move wafer stages <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. These systems used high-pressure oil to generate movement <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. While precise, they lacked reliability due to the risk of leaks in cleanroom environments, which semiconductor customers were unwilling to accept <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. A high-profile lab incident involving a burst hydraulic oil pump led the team to explore electrically-driven systems <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Electrically-Driven Linear Motors
Philips leveraged its experience in optical disk technologies, like the Compact Disc, to develop electrically-driven systems <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. These optical systems required small, precise linear motors to control the unit reading information from a disk <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

Linear motors directly convert electricity to movement without a rotor, utilizing the Lorentz Law's interaction between electric and magnetic fields <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. NatLab engineers applied this technology to position silicon wafers, leading to [[overview_of_asml_lithography_machines | ASML]] machines being known for their precise maneuvering <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Mechanical Guides
Canon's FPA-2000 photolithography machine, introduced in 1992, used mechanical guides (like rails) for wafer movement <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. These systems suffered from unexpected alignment errors due to friction, which also caused wear on mechanical bearings, leading to expensive downtime <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Aerostatic Systems
In the 1990s and early 2000s, the industry implemented "aerostatic systems" <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. These systems created a thin film of extremely dry air between the wafer stage and a granite slab, like an air hockey puck <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This air cushioning reduced friction and vibrations <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

For positioning, [[overview_of_asml_lithography_machines | ASML]] used interferometers (lasers reflecting off a mirror on the stage) <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Additional calculations were needed to compensate for the air's refractive index, which could throw off measurements by as much as 1 nanometer <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. Despite their effectiveness, air systems were not viable in the vacuum environments required for [[euv_lithography_technology_and_its_challenges | EUV lithography]] <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

### Magnetic Levitation Systems
In the late 2000s, in preparation for [[euv_lithography_technology_and_its_challenges | EUV]], [[overview_of_asml_lithography_machines | ASML]] began switching to suspending wafer stages using magnetic levitation (mag-lev) <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

The wafer stage sits atop a 1,400-kilogram magnet plate array containing over 2,200 magnets, precision-placed within 20 micrometers <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Of these, 1,457 magnets are arranged in a Halbach array, which strengthens the magnetic field on one side while canceling it on the other <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

For metrology (measurement) purposes, [[overview_of_asml_lithography_machines | ASML]] transitioned from lasers bouncing off the sides of wafer stages to lasers firing down from a grid mounted above the stages <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. For non-vacuum NXT immersion systems, the shorter travel distance of these lasers (15 millimeters versus up to 300 millimeters previously) simplified air refractive index calculations and improved overlay <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

Challenges with mag-lev include dealing with errant magnetic fields interfering with the wafer and cooling requirements that might impede movement <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Proposals exist to use a single mag-lev system for both short and long-stroke movements, eliminating the stacked fine/coarse stage system and saving space and weight, though separate motors are still commonly used <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## The [[overview_of_asml_lithography_machines | ASML]] TWINSCAN Platform

In the 2000s, as the industry moved from 200-millimeter to 300-millimeter wafers and smaller process nodes, [[overview_of_asml_lithography_machines | ASML]] developed the TWINSCAN platform <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This platform was engineered to accommodate larger, heavier wafers at high speeds while processing smaller features <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

The TWINSCAN is named for its dual-stage cycle: measurement and exposure <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. There is a wafer on each stage, clamped using electrostatic forces <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. The chuck uses tens of thousands of burls to reduce direct contact to only 2% of the wafer surface, minimizing contamination <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

The process involves:
1.  **Measurement Stage**: A wafer handler robot loads a wafer onto the measurement stage <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The machine performs scans to prepare for aligning the wafer with the reticle, ensuring focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
2.  **Stage Swap**: The machine swaps the stages, rotating the wafers <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
3.  **Exposure Stage**: The measured wafer moves under the lens, and the light source is activated for the required light exposure <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. During the swap, the reticle can be exchanged, though this requires a new alignment step <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

These wafer movements are coordinated by the Control Architecture Reference Model (CARM) motion control platform, powered by FPGAs and process controllers <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Unlike previous machines that ran steps sequentially on a single wafer, the TWINSCAN's dual-stage setup was a major engineering feat <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The tool's architecture had to be reworked to re-balance weight and mass and handle vibrations from two simultaneous processes <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This necessitated isolating the lens and metrology equipment on a separate metrology frame using air-bearings, which use highly pressurized gas to reduce friction <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Throughput benchmarks are primarily driven by the measurement stage, not the exposure stage <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. A [[overview_of_asml_lithography_machines | DUV machine]] processing 175 wafers per hour spends only about 20 seconds on exposure within a 2-minute cycle; the rest of the time is dedicated to measurement <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. As Jiro, the sushi master, noted, "the sushi is 95% complete before the fish is brought out to me" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. For [[overview_of_asml_lithography_machines | ASML]], perfecting the measurement sequence is crucial for competitive machines <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

Current TWINSCAN categories include:
*   NXE for [[euv_lithography_technology_and_its_challenges | EUV lithography]] <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   NXT for 193-nanometer ArF [[overview_of_asml_lithography_machines | DUV light]] <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   XT for 248-nanometer KrF [[overview_of_asml_lithography_machines | DUV light]] <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

An NXE:3350 [[euv_lithography_technology_and_its_challenges | EUV machine]] can process 125 wafers per hour, while sophisticated [[overview_of_asml_lithography_machines | DUV machines]] can handle 200-300 wafers <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The machines are modular and designed for upgrades, allowing them to run in customer fabs for decades <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

## Fine and Coarse Movement Systems
Lithography machines typically employ two movement systems <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>:
*   **Coarse Stage**: Transports wafers between workstations using "long-stroke" motors designed for extended range (about 1 meter) and high speed <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Fine Stage**: Prioritizes precision over distance, using "short-stroke" actuators, often voice coil motors <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
These systems are often stacked, with the fine stage on top of the coarse stage, which can lead to weight issues as more stacking is required <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## Role of Software
Software plays an increasingly significant role in the precision and performance of [[overview_of_asml_lithography_machines | ASML's]] tools <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. From 1989 to 2000, the number of CPUs and sensors in their tools grew six and eight times, respectively <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. The 1989 PAS5000 stepper had 200 million lines of source code, including comments, while the 2003 TWINSCAN had 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. This aggressive leveraging of software and corresponding team growth is a key driver behind [[overview_of_asml_lithography_machines | ASML's]] strong performance <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.