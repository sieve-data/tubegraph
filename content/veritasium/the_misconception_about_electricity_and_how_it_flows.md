---
title: The misconception about electricity and how it flows
videoId: bHIhgxav9LY
---

From: [[veritasium]] <br/> 

A common [[misconceptions_about_electricity_in_circuits | misconception about electricity in circuits]] is that electrons physically travel from a power source to a device, carrying energy with them. However, the true mechanism of electrical energy transmission involves electromagnetic fields surrounding the conductors, rather than the electrons themselves [0:01:17].

## The Giant Circuit Thought Experiment
Consider a theoretical circuit with a battery, a switch, a light bulb, and two wires each 300,000 kilometers long (the distance light travels in one second, halfway to the moon and back) [0:00:03]. The light bulb is placed one meter away from the switch [0:00:22]. The question posed is: after closing the switch, how long would it take for the bulb to light up? [0:00:24]

This experiment assumes wires with no resistance and an instantaneous turn-on for the bulb when current passes through it [0:00:40]. Many might intuitively believe the answer relates to the time it takes for something to travel the length of the wire, perhaps one second [0:00:30].

## Debunking the Electron Flow Model
The traditional explanation often taught is that power lines are like tubes, and electrons are like a chain pushed and pulled by a power station [0:01:29]. In this model, electrons run through a device like a toaster, encounter resistance, dissipate energy as heat, and then return to the power station [0:01:45].

However, this model is flawed for several reasons:
*   **No Continuous Conducting Wire** There are physical gaps and breaks in the line, such as in transformers, where electrons cannot flow from one side to the other [0:02:14].
*   **One-Way Energy Flow** If electrons carry energy from the power station to a device, they would also carry energy back when they flow in the opposite direction [0:02:34]. Yet, energy consistently flows only from the source to the device [0:02:50].
*   **Electron Movement** Electrons in power lines merely wiggle back and forth, especially in [[alternating_current_ac_dynamics_and_energy_flow | alternating current (AC)]] systems, and never actually travel a significant distance from the power plant to your home [0:01:11]. Their drift velocity is extremely slow, around a tenth of a millimeter per second [0:06:43].

These points highlight a fundamental [[misconceptions_about_electricity_in_circuits | misunderstanding]]: electrons themselves do not possess potential energy, they are not pushed through a continuous loop, and they do not dissipate their energy in the device [0:03:01].

## The True Mechanism: Electromagnetic Fields
The correct understanding of energy transfer in electrical circuits stems from breakthroughs in the 1860s and 1870s by Scottish physicist James Clerk Maxwell [0:03:22]. Maxwell realized that light is composed of oscillating electric and magnetic fields, governed by his famous Maxwell's equations [0:03:30].

In 1883, Maxwell's former student, John Henry Poynting, extended this understanding to the conservation of energy [0:03:57]. He posited that if energy is locally conserved, its path of flow should be traceable [0:04:02]. Just as the sun's energy travels to Earth stored in the electric and magnetic fields of light [0:04:13], electrical energy also travels through fields.

### The [[poynting_vector_and_energy_flux_in_electrical_circuits | Poynting Vector]]
Poynting developed an equation to describe energy flux (how much electromagnetic energy passes through an area per second) [0:04:26]. This is known as the [[poynting_vector_and_energy_flux_in_electrical_circuits | Poynting vector]], symbolized by **S** [0:04:37]. The formula is:

$$ S = \frac{1}{\mu_0} (E \times B) $$

Where:
*   $\mu_0$ is the permeability of free space [0:04:43].
*   **E** is the electric field [0:04:48].
*   **B** is the magnetic field [0:04:48].
*   **E x B** is the cross product of the electric and magnetic fields [0:04:50].

The cross product dictates that the direction of energy flow (the Poynting vector) is perpendicular to both the electric and magnetic fields [0:04:59]. This equation is universally applicable whenever electric and magnetic fields coincide, indicating a flow of energy [0:05:39].

### [[role_of_electric_and_magnetic_fields_in_energy_transfer | The Role of Electric and Magnetic Fields in Energy Transfer]] in Circuits
In a simple circuit with a battery and a light bulb:
1.  **Establishing Fields**: When the circuit is closed, the battery's electric field extends through the circuit at the speed of light [0:06:13]. This field causes electrons to accumulate on some conductor surfaces (negative charge) and deplete elsewhere (positive charge), creating [[electric_fields_and_surface_charges_in_circuits | surface charges]] [0:06:20].
2.  **Internal and External Fields**: These [[electric_fields_and_surface_charges_in_circuits | surface charges]] create a small electric field *inside* the wires, causing the slow drift of electrons (current) [0:06:34]. Crucially, the charges on the surfaces also create an electric field *outside* the wires, and the current inside the wires creates a magnetic field *outside* the wires [0:07:01].
3.  **Energy Flow via Fields**: The combination of these external electric and magnetic fields results in a flow of energy in the space around the circuit [0:07:10]. Using the right-hand rule with the Poynting vector, one can see that energy flows radially outwards from the battery [0:07:37] and along the wires towards the light bulb [0:07:49]. At the light bulb, the [[poynting_vector_and_energy_flux_in_electrical_circuits | Poynting vector]] is directed inwards, showing that the bulb receives energy from the surrounding fields [0:08:00].
4.  **Direction of Energy Flow**: Even though electrons may oscillate back and forth (especially in AC), the [[poynting_vector_and_energy_flux_in_electrical_circuits | Poynting vector]] consistently shows energy flux flowing in one direction—from the power source to the load [0:08:45]. This is true for both DC and [[alternating_current_ac_dynamics_and_energy_flow | AC circuits]] [0:09:29].

The energy is transmitted by the electric and magnetic fields and travels quite fast through the space around the conductors [0:08:32].

## Historical Validation: Undersea Telegraph Cables
The [[historical_misunderstanding_of_electrical_energy_transmission | historical misunderstanding of electrical energy transmission]] was critically exposed during the laying of the first Transatlantic telegraph cable in 1858 [0:10:13]. The cable experienced severe signal distortion and lengthening, making it hard to differentiate signals [0:10:25].

A debate ensued: William Thomson (Lord Kelvin) believed signals moved like water through a tube, while others, like Heaviside and Fitzgerald, argued that the fields *around* the wires carried the energy and information [0:10:47]. The latter view proved correct [0:11:05]. The cable's design, with a central copper conductor coated in an insulator and encased in an iron sheath, inadvertently interfered with the propagation of electromagnetic fields due to the iron's conductivity increasing the line's capacitance [0:11:07]. This is why modern power lines are suspended high up, maximizing the insulating air gap from the ground, which also acts as a conductor [0:11:27].

## Revisiting the Giant Circuit Question
Given this understanding, the answer to the giant circuit question is: the light bulb would turn on almost instantaneously, in roughly 1/C seconds [0:11:45]. This is because the electric and magnetic fields, which carry the energy, propagate through space at the speed of light. They reach the light bulb, which is only one meter away from the switch, in a few nanoseconds, not a second [0:12:16]. While the full voltage isn't immediately received, the turn-on is limited by the propagation of these fields [0:12:29].

In conclusion, the energy that powers your home is delivered not by electrons flowing through wires, but by [[implications_of_electromagnetic_fields_in_power_lines | traveling electromagnetic waves]] that propagate through the space *around* the conductors [0:13:20]. This fundamental principle is applied every time a light switch is flicked [0:13:30].