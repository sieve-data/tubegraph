---
title: Lumped element and distributed element models in electrical circuits
videoId: oI_X2cMHNe0
---

From: [[veritasium]] <br/> 

Analyzing complex electrical circuits can be simplified using different models, which abstract the underlying physics into manageable components. The two primary approaches discussed are the lumped element model and the distributed element model <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.

## The Lumped Element Model

The lumped element model is a common simplification used by scientists and engineers to analyze basic circuits <a class="yt-timestamp" data-t="15:05:08">[15:08:08]</a>. It simplifies complex physical interactions into discrete circuit elements <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.

### Core Idea
This model lumps together spread-out multi-particle and field interactions into a few discrete circuit elements <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. For instance, Ohm's law (voltage = current × resistance) is considered a macroscopic result of numerous microscopic interactions, including [[electric_fields_and_surface_charges_in_circuits | surface charges]], their [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric fields]], and countless electrons colliding with metal ions <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.

### Application
Every time a circuit diagram is drawn, the lumped element model is being used <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>. It's highly convenient because it avoids the need to solve complex [[applications_of_maxwells_equations_in_analyzing_circuits | Maxwell's equations]] in three dimensions for basic circuit analysis <a class="yt-timestamp" data-t="15:05:08">[15:08:08]</a>.

### Limitations
The lumped element model has limitations, especially in circuits with long wires or where [[role_of_electric_and_magnetic_fields_in_energy_transfer | fields]] between wires become significant <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>. It does not include circuit elements to indicate these important field interactions <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.

## The Distributed Element Model (Transmission Line Model)

When the [[role_of_electric_and_magnetic_fields_in_energy_transfer | fields]] between wires are crucial to the problem, the lumped element model is insufficient, and a more detailed approach, the distributed element model (specifically, a transmission line model), is required <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.

### Components
To account for these interactions, the model incorporates:
*   **Capacitors** down the wires: These capture the effect that charges on one wire have on the other <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>. For example, negative charges on one wire's surface will induce positive charges on the other's surface <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>.
*   **Inductors** down the wires: Since long wires create significant [[role_of_electric_and_magnetic_fields_in_energy_transfer | magnetic fields]] around them, inductors model their resistance to changes in current <a class="yt-timestamp" data-t="16:15:00">[16:15:00]</a>.
*   **Resistors**: While often assumed superconducting for simplicity in specific thought experiments, resistors can also be added to model the wire's inherent resistance <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>.

### How it Works
When a voltage is first applied across a capacitor, current flows as opposite charge builds up on its plates, acting like a short circuit in the short-time limit <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>. As one capacitor charges, the next one begins to charge, leading to a loop of current that expands outwards at roughly the speed of light <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>. This phenomenon is another way of describing the effect of the [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric field]] propagating between the wires <a class="yt-timestamp" data-t="17:16:00">[17:16:00]</a>.

### Characteristic Impedance
This model allows for the calculation of the **characteristic impedance** of the transmission lines <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>. This is defined as the resistance to alternating current that a source would encounter when sending a signal down the wires <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. It is calculated as the square root of inductance divided by capacitance (Z₀ = √(L/C)) <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>. Matching the load's resistance to the circuit's impedance maximizes power delivery <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>.

### Practical Implications
Simulations using software like Ansys HFSS, which provides a complete solution to [[applications_of_maxwells_equations_in_analyzing_circuits | Maxwell's equations]] in three dimensions, validate the predictions of the distributed element model <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. These simulations show the [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric field]] radiating out and generating current as it reaches the far wire <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. The [[poynting_vector_and_energy_flux_in_electrical_circuits | Poynting vector]] in these simulations demonstrates that energy is carried by the [[role_of_electric_and_magnetic_fields_in_energy_transfer | fields]] *outside* the wires and can propagate across gaps, not just along the wires <a class="yt-timestamp" data-t="14:12:00">[14:12:12]</a>.

The ability of a light bulb to turn on very quickly in a long circuit, regardless of its completeness, can be explained by the initial propagation of the [[role_of_electric_and_magnetic_fields_in_energy_transfer | electric field]] at the speed of light <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>. This phenomenon is accurately predicted by the distributed element model <a class="yt-timestamp" data-t="16:43:00">[16:43:00]</a>.