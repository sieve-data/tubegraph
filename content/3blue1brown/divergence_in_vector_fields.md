---
title: Divergence in vector fields
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

Divergence is a fundamental concept in [[vector_fields_and_fluid_flow | vector field]] analysis, particularly useful for understanding the behavior of such fields at specific points in space <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Understanding Vector Fields

A [[vector_fields_and_fluid_flow | vector field]] is created by associating each point in space with a vector, which possesses both magnitude and direction <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. These [[understanding_vectors | vectors]] can represent various physical phenomena, such as:
*   Velocities of fluid particles at each point <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   The force of gravity at different points in space <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   Magnetic field strength <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

While [[vector_fields_and_fluid_flow | vector fields]] in physics can change over time (e.g., wind gusts or changing electric fields), for conceptual understanding, it is often helpful to consider static, two-dimensional [[vector_fields_and_fluid_flow | vector fields]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Visualizing Divergence through Fluid Flow

A powerful approach to understanding [[vector_fields_and_fluid_flow | vector fields]] is to imagine them as representing a fluid flow <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This perspective allows for a visceral understanding of concepts like divergence and curl, even if the actual field describes something else, like an electric field <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

When viewing a [[vector_fields_and_fluid_flow | vector field]] as fluid flow, one might observe strange behaviors:
*   **Sources**: Points where the fluid appears to "spring into existence from nothingness" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Sinks**: Points where the fluid seems to "disappear into nothingness" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Defining Divergence

The **divergence** of a [[vector_fields_and_fluid_flow | vector field]] at a specific point indicates "how much this imagined fluid tends to flow out of or into small regions near it" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

*   **Positive Divergence**: Occurs at points acting as "sources," where there's a net outflow of fluid <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This can mean fluid is flowing away from the point, or that fluid flowing into it from one direction is slower than the fluid flowing out in another, implying spontaneous generation <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Negative Divergence**: Occurs at points acting as "sinks," where there's a net inflow of fluid <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

The divergence of a [[vector_fields_and_fluid_flow | vector field]] yields a new function that takes a 2D point as input and outputs a single number. This number quantifies how much that point behaves as a source or a sink <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. It is analogous to a derivative, as its output depends on the behavior of the field in a small neighborhood around the point <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

For an incompressible fluid, like water, its velocity [[vector_fields_and_fluid_flow | vector field]] must have a divergence of zero everywhere. This is a crucial constraint for real-world fluid flow problems <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Applications of Divergence

### Maxwell's Equations

Divergence is a cornerstone in [[maxwells_equations_and_vector_calculus | Maxwell's equations]], which describe electricity and magnetism <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

*   **Gauss's Law**: States that the divergence of an electric field at a given point is proportional to the charge density at that point <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This can be intuitively understood by imagining positively charged regions as "sources" and negatively charged regions as "sinks" of an electric fluid. In regions without charge, the fluid would flow incompressibly <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Divergence of Magnetic Field**: The divergence of the magnetic field is always zero everywhere <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. In terms of fluid flow, this means the magnetic field behaves like an incompressible fluid with no sources or sinks <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This physical interpretation implies the non-existence of magnetic monopoles (isolated north or south poles) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Non-Spatial Contexts: Population Dynamics

Divergence can also be applied to systems that don't initially appear spatial. For instance, in differential equations, the state of a system (e.g., population sizes of two species) can be represented as a point in a "phase space" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. A [[vector_fields_and_fluid_flow | vector field]] in this space can indicate the rates of change for these variables <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

The "phase flow" associated with this field conceptualizes how possible starting states evolve over time <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Operations like divergence can help inform about the system, for example, whether population sizes converge towards or diverge away from particular values <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Notational and Conceptual Connection

Divergence is commonly written using the "nabla" operator (∇) as a dot product with the [[vector_fields_and_fluid_flow | vector field]] function (∇ ⋅ F) <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. This is more than just a mnemonic; there is a genuine connection between divergence and the [[dot_products_and_vectors | dot product]] <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

The divergence can be thought of as a kind of average value for the [[dot_products_and_vectors | dot product]] of a small "step vector" (representing a tiny movement in the field) with the change it causes in the output vector <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. If a step in a certain direction causes a change to the [[understanding_vectors | vector]] in that same direction, it corresponds to a tendency for outward flow, indicating positive divergence <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Conversely, if the change is in the opposite direction, it indicates inward flow and negative divergence <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.