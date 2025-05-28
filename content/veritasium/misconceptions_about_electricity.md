---
title: Misconceptions about electricity
videoId: bHIhgxav9LY
---

From: [[veritasium]] <br/> 

## The Circuit Thought Experiment

Imagine a giant circuit with a battery, a switch, a [[history_of_the_light_bulb|light bulb]], and two wires, each 300,000 kilometers long (the distance light travels in one second) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The wires extend halfway to the moon and back, connecting to a [[history_of_the_light_bulb|light bulb]] just one meter away from the switch <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A key question is: how long would it take for the [[history_of_the_light_bulb|bulb]] to light up after the switch is closed? <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a> Assuming the wires have no resistance and the [[history_of_the_light_bulb|light bulb]] turns on immediately when current passes through it <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Common Misconceptions About Electrical Energy Transmission

Traditional explanations of how electrical energy reaches homes often contain fundamental errors <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### The Electron Analogy (Incorrect)

A common analogy describes power lines as flexible plastic tubing with electrons acting like a chain inside <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. In this analogy, a power station pushes and pulls electrons back and forth 60 times a second (in the case of [[alternating_current_vs_direct_current|alternating current]]) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. When a device like a toaster is plugged in, electrons run through it, encountering resistance and dissipating their energy as heat, thereby toasting bread <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

While this story is easy to visualize, it is wrong <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Why the Analogy is Flawed

Several points contradict this common understanding:
*   **No Continuous Wire**: There isn't a continuous conducting wire from a power station to a house <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Physical gaps exist, for instance, in transformers where different coils of wire prevent electrons from flowing directly from one side to the other <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **One-Way Energy Flow**: If electrons carried energy from the power station to a device, they would also carry energy back when they flow in the return direction <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. However, energy only flows in one direction from the source to the load <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Electrons Don't Carry Potential Energy**: The fundamental misconception is that electrons themselves possess potential energy, are pushed or pulled through a continuous loop, and dissipate their energy in the device <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. In reality, the drift velocity of electrons is extremely slow, about a tenth of a millimeter per second <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## The Actual Mechanism: [[the_role_of_electromagnetic_fields_in_energy_transmission|Electromagnetic Fields]]

### Maxwell's Equations and Light

In the 1860s and 1870s, Scottish physicist James Clerk Maxwell made a significant breakthrough by realizing that light consists of oscillating electric and magnetic fields <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. These fields oscillate perpendicular to each other and in phase <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Maxwell's equations describe the behavior of these fields and waves <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Light transmits energy from its source to its destination via these [[the_role_of_electromagnetic_fields_in_energy_transmission|electromagnetic fields]] <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Poynting Vector and Energy Flux

In 1883, John Henry Poynting, one of Maxwell's former students, applied the principle of local energy conservation to trace the path of energy flow <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. He developed an equation, the Poynting vector (**S**), to describe energy flux – the amount of [[the_role_of_electromagnetic_fields_in_energy_transmission|electromagnetic energy]] passing through an area per second <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

The Poynting vector formula is:
**S** = (1/μ₀) * (**E** x **B**) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, where:
*   μ₀ is the permeability of free space <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **E** is the electric field <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **B** is the magnetic field <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **E** x **B** is the cross product of the electric and magnetic fields, indicating the direction of energy flow (using the right-hand rule) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The significance of Poynting's equation is that it applies whenever electric and magnetic fields coincide, not just for light <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Anytime these fields are present together, there is a calculable flow of energy <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Energy Flow in a Simple Circuit

Consider a battery connected to a [[history_of_the_light_bulb|light bulb]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>:
1.  **Electric Field Propagation**: When the battery is connected, its electric field extends through the circuit at the speed of light <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
2.  **Surface Charges and Internal Field**: This electric field causes electrons to accumulate on some conductor surfaces (negative charge) and be depleted elsewhere (positive charge) <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. These surface charges create a small electric field *inside* the wires, causing electrons to drift slowly in one direction, forming conventional current <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
3.  **External Fields**: The surface charges also create an electric field *outside* the wires, and the current inside creates a magnetic field *outside* the wires <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
4.  **Energy Flow via Fields**: With both electric and magnetic fields present in the space around the circuit, energy flows according to Poynting's theory <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Using the right-hand rule, it's found that energy flows radially outwards from the battery and along the wires <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
5.  **Energy Absorption**: At the [[history_of_the_light_bulb|light bulb]] filament, the Poynting vector is directed *inward* toward the [[history_of_the_light_bulb|bulb]], meaning the [[history_of_the_light_bulb|light bulb]] receives energy from the surrounding fields <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Energy takes many paths from the battery to the [[history_of_the_light_bulb|bulb]], but in all cases, it is transmitted by the [[the_role_of_electromagnetic_fields_in_energy_transmission|electromagnetic fields]] *around* the conductors, not by the electrons *within* them <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. This concept is [[counterintuitive_engineering_concepts|counterintuitive]] for most people <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Even in [[alternating_current_vs_direct_current|alternating current]] (AC) circuits, where electron direction reverses, both electric and magnetic fields flip simultaneously, so the Poynting vector (and thus energy flux) still points consistently from the source to the load <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This explains how energy flows from power plants to homes <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

## Historical Confirmation: Trans-Atlantic Cables

The distinction between energy carried by fields versus current became critically important with the laying of undersea telegraph cables <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. The first Trans-Atlantic cable, laid in 1858, only worked for about a month and suffered from enormous signal distortions <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Signals became distorted and lengthened over such long distances, making it hard to differentiate Morse code dots from dashes <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

A debate ensued among scientists:
*   William Thomson (Lord Kelvin) believed electrical signals moved through cables like water through a rubber tube <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   Others, like Oliver Heaviside and George Francis FitzGerald, argued that it was the [[the_role_of_electromagnetic_fields_in_energy_transmission|fields]] *around* the wires that carried the energy and information <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

The latter view proved correct <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The cable's central copper conductor was coated in an insulator and then encased in an iron sheath, which, as a good conductor, interfered with the propagation of [[the_role_of_electromagnetic_fields_in_energy_transmission|electromagnetic fields]] by increasing the line's capacitance <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This is why modern power lines are suspended high up, using a large insulating gap of air to separate the wires from the ground <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## Resolution of the Initial Question

Returning to the giant circuit light bulb question <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>: when the switch is closed, the [[history_of_the_light_bulb|light bulb]] turns on almost instantaneously, in roughly 1/C seconds <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

The common misconception is that the electric field needs to travel all the way down the long wires <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. However, what matters is what happens *around* the wires <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. The electric and magnetic fields propagate through the space around the circuit to the [[history_of_the_light_bulb|light bulb]], which is only one meter away, in a few nanoseconds <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. This rapid propagation of fields is the limiting factor for the [[history_of_the_light_bulb|bulb]] turning on <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

The [[history_of_the_light_bulb|bulb]] won't immediately receive the battery's full voltage, but a fraction dependent on the impedance of the lines and the [[history_of_the_light_bulb|bulb]] <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. This [[counterintuitive_engineering_concepts|counterintuitive]] understanding of electricity, that energy is delivered by traveling [[the_role_of_electromagnetic_fields_in_energy_transmission|electromagnetic waves]] around power lines, is not widely known despite being used every day <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.