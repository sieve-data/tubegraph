---
title: Overview of ASML lithography machines
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 

[[asmls_role_in_semiconductor_manufacturing | ASML's lithography machines]] are highly precise instruments designed to transfer intricate chip designs onto wafers, which are typically made of silicon <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. These machines operate with extreme accuracy, positioning a wafer for exposure to within a few nanometers <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. To put this into perspective, a human hair is about 50,000 to 100,000 nanometers wide, a virus is 20 to 300 nanometers wide, and a fingernail grows 1 nanometer each second <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Core Process of Optical Lithography

An optical lithography machine functions essentially as a $150 million camera <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The general workflow involves several steps:
1.  **Photoresist Application**: A light-sensitive polymer chemical called photoresist is applied onto the wafer using a spin-coating method <a class="yt-timestamp" data-t="00:00:55">[00:01:00]</a>.
2.  **Exposure**: The wafer then enters the lithography exposure tool <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Inside the tool, key sub-components facilitate the process:
    *   **Illumination System**: Composed of a light source and a condenser lens, this system delivers light widely, evenly, and with adequate intensity <a class="yt-timestamp" data-t="00:01:22">[00:01:28]</a>. [[asmls_euv_light_source_and_laser_mechanics | ASML's EUV machines]] use multiple mirrors for illumination, albeit at the cost of significant power reduction <a class="yt-timestamp" data-t="00:01:35">[00:01:39]</a>.
    *   **Photomask/Reticle**: The illuminated light passes through or reflects off the photomask (also known as a reticle), which contains the chip design pattern <a class="yt-timestamp" data-t="00:01:45">[00:01:51]</a>. In the early days, masks contained the whole design, but as designs grew more complex, "reticles" representing a portion of the chip design became standard, making the terms interchangeable <a class="yt-timestamp" data-t="00:01:54">[00:02:05]</a>.
    *   **Objective Lens**: This lens collects and focuses the light, shrinking the image <a class="yt-timestamp" data-t="00:02:22">[00:02:26]</a>.
3.  **Pattern Transfer**: The focused light strikes the photoresist-coated wafer, creating a 3D relief of a portion of the chip's design <a class="yt-timestamp" data-t="00:02:31">[00:02:35]</a>. This design can later be made permanent through etch processes <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Precision Challenges

The wafer and its stage are quite heavy, with a fully loaded 300-millimeter wafer stage weighing about 15 kilograms <a class="yt-timestamp" data-t="00:02:48">[00:02:52]</a>. The platform must move these stages extremely quickly, stop abruptly, and hold absolutely still during exposure, all within nanometer margins of error <a class="yt-timestamp" data-t="00:02:58">[00:03:11]</a>. Key challenges include:
*   **Overlay**: Ensuring precise relative positioning of pattern layers, which can be as tight as a few nanometers, as errors can damage the device or cause short-circuits <a class="yt-timestamp" data-t="00:03:19">[00:03:28]</a>. This becomes even stricter with multi-patterning, where multiple exposures create smaller lines <a class="yt-timestamp" data-t="00:03:36">[00:03:41]</a>.
*   **Acceleration and Vibrations**: The wafer stage can accelerate up to 20 G-forces (twenty times the force of gravity), which is more than a Formula 1 car or a jet fighter <a class="yt-timestamp" data-t="00:03:48">[00:04:02]</a>. Simultaneously, the system must execute these movements without causing vibrations, which would throw off precision <a class="yt-timestamp" data-t="00:04:02">[00:04:09]</a>.

## Evolution of Movement Systems

[[asmls_rise_in_the_photolithography_industry | ASML]], which evolved from Philips in the Netherlands, has a long history in [[technological_advances_in_lithography_tools_by_asml | semiconductor manufacturing]] <a class="yt-timestamp" data-t="00:04:15">[00:04:18]</a>. Their products, first developed at Philips' NatLab, include the pioneering Silicon Repeater lithography machine <a class="yt-timestamp" data-t="00:04:24">[00:04:34]</a>.

### Early Systems
Early Philips wafer steppers, such as the PAS 2000, utilized "hydraulic linear motors" for wafer stage movement <a class="yt-timestamp" data-t="00:04:34">[00:04:39]</a>. While precise, these hydraulic systems lacked reliability due to the risk of oil leaks, which would be devastating in a cleanroom fab. Strong seals were implemented, but the bulkiness and risk led to customer refusal, contributing to [[asmls_rise_in_the_photolithography_industry | ASML's early challenges]] <a class="yt-timestamp" data-t="00:04:48">[00:05:08]</a>.

Following a lab incident with a burst hydraulic oil pump, the team shifted to electrically-driven systems <a class="yt-timestamp" data-t="00:05:17">[00:05:22]</a>. This leveraged Philips' experience in optical disk technologies like the Compact Disc, where contact-less optical lasers replaced physical styluses <a class="yt-timestamp" data-t="00:05:26">[00:05:42]</a>. This required the creation of small, precise linear motors, which directly convert electricity to movement using the Lorentz Law <a class="yt-timestamp" data-t="00:05:49">[00:06:07]</a>. NatLab engineers applied these linear motor technologies to wafer positioning, leading to ASML machines being known for their precise maneuvering <a class="yt-timestamp" data-t="00:06:13">[00:06:21]</a>.

Mechanical guides, like those in Canon's FPA-2000 photolithography machine (introduced in 1992), also suffered from friction-induced alignment errors and wear over time, requiring expensive downtime for replacement <a class="yt-timestamp" data-t="00:11:34">[00:12:05]</a>.

### Aerostatic Systems
During the 1990s and early 2000s, the industry adopted "aerostatic systems" <a class="yt-timestamp" data-t="00:12:11">[00:12:14]</a>. These systems used a thin film of extremely dry air between the wafer stage and a granite slab, akin to an air hockey puck, to reduce friction and vibrations <a class="yt-timestamp" data-t="00:12:18">[00:12:27]</a>. ASML machines used interferometers (lasers) to track stage positioning, though compensating for the air's refractive index was necessary due to its effect on nanometer precision <a class="yt-timestamp" data-t="00:12:32">[00:12:53]</a>.

### Magnetic Levitation
As lithography advanced, especially with the need for a vacuum in [[overview_of_asmls_extreme_ultraviolet_lithography | EUV lithography]], air-based systems became unviable <a class="yt-timestamp" data-t="00:13:05">[00:13:11]</a>. In the late 2000s, [[asmls_rise_in_the_photolithography_industry | ASML]] began transitioning to magnetic levitation for suspending their wafer stages <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

Today's wafer stages sit on magnet plate arrays weighing 1,400 kilograms and containing over 2,200 magnets, precisely placed within 20 micrometers <a class="yt-timestamp" data-t="00:13:26">[00:13:32]</a>. Of these, 1,457 are arranged in a Halbach array, which strengthens the magnetic field on one side while canceling it on the other <a class="yt-timestamp" data-t="00:13:40">[00:13:46]</a>. Metrology (measurement) for these systems shifted from lasers bouncing off the sides of stages to lasers firing down from a grid mounted above the stages <a class="yt-timestamp" data-t="00:13:51">[00:13:55]</a>. For non-vacuum NXT immersion systems, shorter laser travel (15 millimeters versus 300 millimeters previously) simplified air refractive index calculations and improved overlay <a class="yt-timestamp" data-t="00:14:01">[00:14:11]</a>. Challenges with magnetic levitation include interfering magnetic fields and cooling requirements <a class="yt-timestamp" data-t="00:14:21">[00:14:28]</a>.

## The TWINSCAN Platform

The TWINSCAN platform is [[technological_advances_in_lithography_tools_by_asml | ASML's main brand of lithography machine]] <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Its name derives from its dual-stage cycle: measurement and exposure <a class="yt-timestamp" data-t="00:06:55">[00:07:02]</a>.

### Dual-Stage Operation
During operation, each of the two stages holds a wafer, clamped securely by electrostatic forces <a class="yt-timestamp" data-t="00:07:02">[00:07:06]</a>. The chuck uses tens of thousands of burls to reduce direct contact to only 2% of the wafer surface, minimizing contamination risk <a class="yt-timestamp" data-t="00:07:06">[00:07:11]</a>.
1.  **Measurement Stage**: A robot (wafer handler) loads the wafer <a class="yt-timestamp" data-t="00:07:18">[00:07:21]</a>. The machine then runs a series of scans to prepare for aligning the wafer with the reticle, ensuring good focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:32]</a>.
2.  **Stage Swap**: Once measurement is complete, the machine swaps the stages, rotating the wafers <a class="yt-timestamp" data-t="00:07:38">[00:07:41]</a>. The measured wafer moves under the lens for light exposure <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. During this swap, the machine can also exchange the reticle, though this requires a new alignment step <a class="yt-timestamp" data-t="00:07:50">[00:07:54]</a>.

The wafer movements are coordinated by the Control Architecture Reference Model (CARM) motion control platform, powered by FPGAs and process controllers <a class="yt-timestamp" data-t="00:07:58">[00:08:05]</a>.

### Engineering Feat
Prior to the TWINSCAN, [[technological_advances_in_lithography_tools_by_asml | lithography machines]] performed all measurement, alignment, and exposure steps sequentially on a single wafer <a class="yt-timestamp" data-t="00:08:12">[00:08:16]</a>. Pulling off the dual-stage setup was a major engineering project. It required reworking the tool's architecture to re-balance weight and mass, and to handle vibrations from two simultaneous processes <a class="yt-timestamp" data-t="00:08:22">[00:08:35]</a>. The lens and metrology equipment, mounted on a metrology frame, had to be isolated from the tool's main frame using air-bearings, which use highly pressurized gas to reduce friction <a class="yt-timestamp" data-t="00:08:35">[00:08:43]</a>.

Crucially, the measurement stage is the bottleneck for throughput, not the exposure stage <a class="yt-timestamp" data-t="00:08:50">[00:08:53]</a>. A DUV machine handling 175 wafers per hour spends only 20 seconds on exposure within a 2-minute cycle; the rest of the time is dedicated to measurement <a class="yt-timestamp" data-t="00:08:53">[00:09:04]</a>.

### TWINSCAN Product Categories
Today, the TWINSCAN name encompasses several product categories <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:
*   **NXE**: [[overview_of_asmls_extreme_ultraviolet_lithography | EUV lithography machines]]. The NXE:3350 can process 125 wafers per hour <a class="yt-timestamp" data-t="00:09:48">[00:10:02]</a>.
*   **NXT**: Machines using 193-nanometer ArF DUV (Deep Ultraviolet) light <a class="yt-timestamp" data-t="00:09:48">[00:09:56]</a>. Sophisticated DUV machines can process 200-300 wafers per hour <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **XT**: Machines using 248-nanometer KrF DUV light <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

The numbers in machine names correspond to their optics systems and lenses <a class="yt-timestamp" data-t="00:10:13">[00:10:17]</a>. Machines are built modularly to customer requirements, allowing for decades of operation and upgrades to meet modern demands, leading to high diversity within categories <a class="yt-timestamp" data-t="00:10:17">[00:10:34]</a>.

## Fine and Coarse Movement Systems

Typical lithography machines utilize two distinct movement systems <a class="yt-timestamp" data-t="00:10:38">[00:10:42]</a>:
*   **Coarse Stage**: Transports the wafer between workstations <a class="yt-timestamp" data-t="00:10:42">[00:10:46]</a>. It uses "long-stroke" motors designed for extended range (about 1 meter) and high speed <a class="yt-timestamp" data-t="00:10:46">[00:10:51]</a>.
*   **Fine Stage**: Prioritizes precision over distance <a class="yt-timestamp" data-t="00:10:56">[00:11:01]</a>. It uses "short-stroke" actuators, often voice coil motors <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

These systems are often stacked (fine stage on top of coarse stage), which has contributed to weight issues as more stacking and movements are required <a class="yt-timestamp" data-t="00:11:08">[00:11:16]</a>. Proposals exist for single magnetic levitation (mag-lev) systems to handle both short and long-stroke movements, eliminating the stacked fine/coarse stages to save space and weight <a class="yt-timestamp" data-t="00:14:33">[00:14:42]</a>, though current documentation still shows separate electromagnetic motors <a class="yt-timestamp" data-t="00:14:52">[00:14:56]</a>.

## The Role of Software

A significant, often underappreciated, aspect of ASML machines is the critical role of software <a class="yt-timestamp" data-t="00:15:19">[00:15:21]</a>. Between 1989 and 2000, the number of CPUs and sensors in ASML's [[technological_advances_in_lithography_tools_by_asml | tools]] grew six and eight times, respectively <a class="yt-timestamp" data-t="00:15:28">[00:15:35]</a>. The 1989 PAS5000 stepper had 200 million lines of source code, including comments, while the 2003 TwinScan boasted 1.25 billion lines <a class="yt-timestamp" data-t="00:15:35">[00:15:42]</a>. This aggressive leveraging of software, alongside significant team growth, is considered a key driver behind [[asmls_rise_in_the_photolithography_industry | ASML's strong performance]] <a class="yt-timestamp" data-t="00:15:55">[00:16:04]</a>.