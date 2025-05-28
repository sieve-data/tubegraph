---
title: Poynting vector and energy flux in electrical circuits
videoId: bHIhgxav9LY
---

From: [[veritasium]] <br/> 

The conventional understanding of how electrical energy travels through circuits often involves [[misconceptions_about_electricity_in_circuits | misconceptions]] about electrons carrying energy directly through wires <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This article explains the true mechanism of energy transfer via electromagnetic fields, as described by the Poynting vector.

## The Problem with Conventional Understanding

A common, yet incorrect, analogy for electricity describes power lines as flexible plastic tubing where electrons act like a chain, being pushed and pulled by a power station <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. In this model, electrons running through a device like a toaster would encounter resistance, dissipate energy as heat, and toast bread <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

However, this model is flawed for several reasons:
*   There is no continuous conducting wire from a power station to a house; transformers introduce physical gaps where electrons cannot flow from one side to the other <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.
*   If electrons carried energy from the power station to a device, they would also carry energy back to the power station when flowing in the return direction <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. Energy flow is unidirectional from the source to the device <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

These [[misconceptions_about_electricity_in_circuits | misconceptions]] include the ideas that electrons themselves have potential energy, are pushed through a continuous loop, and dissipate their energy in the device <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. In reality, electrons do not carry the energy <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.

## Maxwell's Equations and the Nature of Light

A major breakthrough in understanding the universe occurred in the 1860s and 1870s when Scottish physicist James Clerk Maxwell realized that light consists of oscillating [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]] <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. These fields oscillate perpendicular to each other and are in phase <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. Maxwell developed the equations governing the behavior of these fields and waves, which are now known as [[applications_of_maxwells_equations_in_analyzing_circuits | Maxwell's equations]] <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

## Poynting's Contribution: Energy Flux

In 1883, John Henry Poynting, one of Maxwell's former students, considered the concept of local energy conservation <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. He posited that if energy is conserved in every tiny bit of space, its path of flow should be traceable <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. Just as sunlight's energy is stored and transmitted in the [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]] of light during its journey from the sun <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>, Poynting worked out an equation to describe energy flux – the amount of electromagnetic energy passing through an area per second <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

This equation is known as the **Poynting vector**, symbolized as **S** <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. Its formula is:

$S = \frac{1}{\mu_0} (E \times B)$ <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>

Where:
*   $\mu_0$ is the permeability of free space <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>
*   **E** is the electric field <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>
*   **B** is the magnetic field <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>
*   $E \times B$ is the cross product of the electric and magnetic fields <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

The direction of the energy flux (S) is determined by the right-hand rule applied to the cross product of E and B <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>: point fingers in the direction of the electric field, curl them towards the magnetic field, and the thumb points in the direction of energy flow <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>. This means energy flows perpendicular to both the electric and magnetic fields <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

Crucially, Poynting's equation applies not just to light, but to any instance where [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]] coincide <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. Anytime these fields are present together, there is a flow of energy calculable by the Poynting vector <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

## Energy Flow in a Simple DC Circuit

Consider a simple circuit with a battery and a light bulb <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
1.  **Field Propagation**: When the battery is connected, its [[electric_fields_and_surface_charges_in_circuits | electric field]] extends through the circuit at the speed of light <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>.
2.  **[[electric_fields_and_surface_charges_in_circuits | Surface Charges]] and Current**: This electric field pushes electrons, causing them to accumulate on some conductor surfaces (negatively charged) and deplete elsewhere (positively charged) <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. These [[electric_fields_and_surface_charges_in_circuits | surface charges]] create a small electric field *inside* the wires, causing electrons to drift slowly in one direction, forming the conventional current <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>. The drift velocity of electrons is extremely slow, around a tenth of a millimeter per second <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.
3.  **External Fields**: The charge on the surfaces of the conductors creates an electric field *outside* the wires <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. Simultaneously, the current *inside* the wires creates a magnetic field *outside* the wires <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.
4.  **Energy Flux**: The combination of these external [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]] in the space around the circuit results in a flow of energy, as predicted by Poynting's theory <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.
    *   Around the battery, the Poynting vector indicates energy flowing radially outwards, away from the battery <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
    *   Along the wires, energy flows to the right, from the battery towards the bulb <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
    *   At the light bulb's filament, the Poynting vector is directed inwards, indicating that energy is converging on the bulb from the surrounding field <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

Thus, energy takes many paths from the battery to the bulb, but in all cases, it is transmitted by the [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]] *outside* the wires <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>. Even though electrons move in two directions (away from and towards the battery), the Poynting vector shows that the energy flux only goes one way, from the battery to the bulb <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.

## Energy Flow in AC Circuits

The same analysis applies to [[alternating_current_ac_dynamics_and_energy_flow | alternating current (AC)]] sources <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. While the direction of current reverses every half cycle, both the electric and magnetic fields flip at the same time <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. This synchronous flipping ensures that the Poynting vector consistently points in the same direction—from the source to the bulb <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>.

This explains how energy is able to flow from power plants to homes via power lines <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. Inside the wires, electrons merely oscillate back and forth and do not carry the energy <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. Instead, it is the oscillating [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]] *outside* the wires that travel from the power station to the home, delivering the power <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>.

## Historical Validation: Undersea Telegraph Cables

The understanding that energy travels through fields, not just wires, was learned the hard way with the laying of undersea telegraph cables <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. The first Transatlantic cable, laid in 1858, suffered from enormous signal distortions and poor performance <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>. Signals sent over long distances under the sea became distorted and lengthened, making it difficult to differentiate pulses <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.

During this period, there was a debate among scientists <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>. William Thomson (Lord Kelvin) believed electrical signals moved like water through a tube, via the conductor <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. However, others like Oliver Heaviside and George Fitzgerald argued that the [[role_of_electric_and_magnetic_fields_in_energy_transfer | fields around the wires]] carried the energy and information <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>. This field-based view ultimately proved correct <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

The design of the submarine cable—a central copper conductor coated in an insulator and encased in an iron sheath—interfered with the propagation of electromagnetic fields <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>. The iron, though meant for strengthening, acted as a good conductor and increased the capacitance of the line <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. This historical event highlighted the importance of understanding [[implications_of_electromagnetic_fields_in_power_lines | electromagnetic field propagation]] for efficient energy transmission. This is why most power lines today are suspended high up, ensuring a large insulating gap of air from the ground, which also acts as a conductor <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.

## The Giant Circuit Problem

Consider a hypothetical circuit with a battery, a switch, a light bulb, and two wires each 300,000 kilometers long (the distance light travels in one second), connected to a bulb one meter away <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Assuming wires have no resistance and the bulb turns on immediately with current <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>, the question is how long it takes for the bulb to light up after the switch is closed.

The correct answer is almost instantaneously, approximately 1/C seconds <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>. This is because the [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric and magnetic fields]] propagate through the space around the wires <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>. While the wires are a light-second long, the light bulb is only one meter away from the battery, allowing the fields to reach it in a few nanoseconds <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. This quick propagation of fields is the limiting factor for the bulb turning on <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.

The energy that activates the bulb is not carried by electrons traveling all the way down the long wires, but by the rapidly propagating electromagnetic fields in the space surrounding the circuit <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>.

> [!NOTE] [[The misconception about electricity and how it flows | Misconception vs. Reality]]
> It is widely believed that electrons are "pumped" through wires and that customers "buy electrons" <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. However, this is incorrect. The energy is delivered by electromagnetic fields traveling through the space around the conductors, moving quite fast <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. Electrons in the wires only move a tiny distance, often barely at all <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.