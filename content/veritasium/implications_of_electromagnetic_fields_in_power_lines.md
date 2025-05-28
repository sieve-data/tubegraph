---
title: Implications of electromagnetic fields in power lines
videoId: bHIhgxav9LY
---

From: [[veritasium]] <br/> 

A common thought experiment involves a giant electrical circuit with wires extending halfway to the moon, connected to a battery and a light bulb. The question is, how long would it take for the bulb to light up after closing the switch? The answer, which is almost instantaneous, challenges widespread [[misconceptions_about_electricity_in_circuits | misconceptions about electricity in circuits]] regarding how electrical energy is transmitted <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Debunking Traditional Views of Electrical Energy Transmission

For decades, the standard explanation for how electrical energy reached homes from power plants involved electrons being pushed through a continuous wire, encountering resistance, and dissipating their energy <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This model suggests that electrons themselves possess and transfer potential energy <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

However, this conventional explanation is inaccurate for several reasons <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>:
*   There are physical gaps in the grid, such as transformers, preventing a continuous flow of electrons from a power station to a home <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   In alternating current (AC) grids, electrons merely wiggle back and forth; they do not travel long distances <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Their drift velocity is extremely slow, around a tenth of a millimeter per second <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   If electrons carried energy, and current flows both ways in AC, energy should flow back to the power station, which does not happen <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Energy always flows in one direction, from source to load <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

The actual mechanism of energy transfer involves [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]].

## The Role of Fields: Maxwell and Poynting

A crucial breakthrough occurred in the 1860s and 1870s when Scottish physicist James Clerk Maxwell realized that light consists of oscillating [[electric_fields_and_surface_charges_in_circuits | electric and magnetic fields]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. His equations, now known as Maxwell's equations, describe the behavior of these fields and waves <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

In 1883, John Henry Poynting, a former student of Maxwell, further developed this understanding by considering the conservation of energy <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. He theorized that if energy is conserved locally, its path should be traceable <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Just as light carries energy from the sun stored in its [[electric_fields_and_surface_charges_in_circuits | electric and magnetic fields]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, Poynting derived an equation to describe energy flux (how much electromagnetic energy passes through an area per second) <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is known as the [[poynting_vector_and_energy_flux_in_electrical_circuits | Poynting vector (S)]], given by the formula S = (1/μ₀) * (E x B), where E is the electric field and B is the magnetic field <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

The cross product (E x B) indicates that energy flows perpendicular to both the [[electric_fields_and_surface_charges_in_circuits | electric and magnetic fields]] <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Importantly, Poynting's equation applies whenever [[electric_fields_and_surface_charges_in_circuits | electric and magnetic fields]] coincide, not just for light <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Energy Flow in Circuits

In a simple DC circuit (e.g., battery and light bulb):
*   When connected, the battery's [[electric_fields_and_surface_charges_in_circuits | electric field]] extends through the circuit at the speed of light <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   This field causes electrons to accumulate on some conductor surfaces (negative charge) and be depleted elsewhere (positive charge) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   These [[electric_fields_and_surface_charges_in_circuits | surface charges]] create a small [[electric_fields_and_surface_charges_in_circuits | electric field]] *inside* the wires, causing electron drift (current) <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   The [[electric_fields_and_surface_charges_in_circuits | surface charges]] also create an [[electric_fields_and_surface_charges_in_circuits | electric field]] *outside* the wires, and the current inside creates a [[magnetic_fields_and_their_effects | magnetic field]] *outside* the wires <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   This combination of [[electric_fields_and_surface_charges_in_circuits | electric and magnetic fields]] in the space around the circuit results in a flow of energy, as dictated by the [[poynting_vector_and_energy_flux_in_electrical_circuits | Poynting vector]] <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

Using the right-hand rule for the cross product, it can be shown that energy flows:
*   Radially outwards from the battery into the fields <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   Along the wires, generally to the right (towards the load) <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Directed *inward* toward the light bulb filament from all around it, indicating the bulb receives energy from the surrounding fields <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Therefore, energy is transmitted by the [[electric_fields_and_surface_charges_in_circuits | electric and magnetic fields]] *around* the conductors, not *by* the electrons within the conductors themselves <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This holds true for both DC and AC circuits; even when electron motion reverses in AC, both fields flip, ensuring the Poynting vector still points in the same direction, from source to load <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Historical Validation and Practical Implications

The understanding of energy transfer via fields, rather than current, was critical in addressing engineering challenges. A prime example is the first Transatlantic telegraph cable laid in 1858 <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. It suffered from severe signal distortion, making it almost unusable <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

William Thomson (Lord Kelvin) initially believed signals moved like water through a rubber tube <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. However, others like Oliver Heaviside and George Francis Fitzgerald correctly argued that the [[electric_fields_and_surface_charges_in_circuits | fields]] around the wires carried the energy and information <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. This proved to be the correct view <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

The problem with the telegraph cable was that its design, including an iron sheath intended for strength, interfered with the propagation of [[electric_fields_and_surface_charges_in_circuits | electromagnetic fields]] by increasing the line's capacitance <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This [[historical_misunderstanding_of_electrical_energy_transmission | historical misunderstanding of electrical energy transmission]] underscores why modern power lines are suspended high up, using a large insulating gap of air to separate the wires from the ground, as even damp earth acts as a conductor that can interfere with the fields <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

### Answering the Initial Question

Returning to the initial thought experiment of the giant circuit, the light bulb would turn on almost instantaneously, in roughly 1/c seconds <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This is because the energy is not carried *through* the long wires by electrons, but rather *around* the wires by the [[electric_fields_and_surface_charges_in_circuits | electric and magnetic fields]] <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. These fields propagate through the space to the light bulb, which is only one meter away, in mere nanoseconds <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. This rapid propagation of electromagnetic waves is the limiting factor for the bulb turning on <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

This phenomenon highlights a counter-intuitive aspect of everyday technology: the power delivered to our homes and devices comes from traveling [[electric_fields_and_surface_charges_in_circuits | electromagnetic waves]] around the power lines, not from electrons pumped through them <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.