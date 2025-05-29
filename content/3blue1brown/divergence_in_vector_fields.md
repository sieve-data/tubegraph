---
title: Divergence in vector fields
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

Divergence is a fundamental concept in vector calculus, primarily used to describe the nature of [[understanding_vector_fields | vector fields]]. It quantifies how much an imagined fluid tends to flow out of or into small regions at any given point in a vector field <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

## Understanding Divergence Through Fluid Flow

To intuitively grasp divergence, a common approach is to imagine the vectors in a [[understanding_vector_fields | vector field]] as representing the velocities of particles in a fluid <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

### Sources and Sinks
When a vector field is visualized as fluid flow, points where fluid appears to "spring into existence from nothingness" are considered **sources** <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Conversely, points where fluid seems to "disappear into nothingness" are called **sinks** <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

### Positive and Negative Divergence
*   **Positive Divergence**: Occurs at points where the imagined fluid tends to flow *out* of a small region <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. This means the point acts as a source, indicating spontaneous generation of fluid <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>, or that fluid flowing into a region is slower than the fluid flowing out <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
*   **Negative Divergence**: Occurs at points where more fluid flows *into* a small region than out of it <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. This signifies that the point acts as a sink <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

### Incompressible Fluids
For an actual physical fluid, such as water, if it is incompressible, its velocity [[understanding_vector_fields | vector field]] must have a divergence of zero everywhere <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. This constraint is crucial for solving real-world fluid flow problems <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

## Divergence as a Function
A [[understanding_vector_fields | vector field]] typically takes two-dimensional inputs and produces two-dimensional outputs <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. The divergence of that [[understanding_vector_fields | vector field]] creates a *new function* <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This new function takes a single two-dimensional point as its input, but its output is a single number <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>, which measures how much that point acts as a source or a sink <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. This behavior is analogous to a derivative <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

## Applications of Divergence
While the fluid flow analogy is helpful for intuition, divergence is significant for various other types of [[understanding_vector_fields | vector fields]] <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### [[maxwells_equations_and_vector_calculus | Maxwell's Equations]]
One prominent example is [[maxwells_equations_and_vector_calculus | Maxwell's equations]], which describe electricity and magnetism using the language of divergence and [[curl_in_vector_fields | curl]] <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
*   **Gauss's Law**: States that the divergence of an electric field at a given point is proportional to the charge density at that point <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. Conceptually, positively charged regions can be thought of as sources of an imagined fluid, and negatively charged regions as sinks <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>. In areas without charge, this imagined fluid would flow incompressibly, like water <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.
*   **Magnetic Field Divergence**: Another equation states that the divergence of the magnetic field is zero everywhere <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. This implies that if the magnetic field represented a fluid flow, that fluid would be incompressible, with no sources or sinks <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. This also suggests the non-existence of magnetic monopoles (isolated north or south poles of a magnet) <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.

### [[applications_of_divergence_and_curl_to_dynamic_systems | Dynamic Systems]]
Divergence can also be useful in contexts that are not inherently spatial, such as analyzing the behavior of [[applications_of_divergence_and_curl_to_dynamic_systems | dynamic systems]] <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. For example, tracking the population sizes of two species (e.g., predator and prey) <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
*   The state of such a system (the two population sizes) can be represented as a point in a two-dimensional "phase space" <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.
*   A [[understanding_vector_fields | vector field]] can be constructed where each point on the plane (each pair of population sizes) is associated with a vector indicating the rates of change for both variables <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.
*   This [[understanding_vector_fields | vector field]] visually represents how the system evolves over time <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.
*   Divergence can help determine if population sizes converge or diverge from particular values <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.

## Notation and Connection to Dot Product
The divergence of a [[understanding_vector_fields | vector field]] is commonly written as a dot product between the "nabla" operator (an upside-down triangle symbol, $\nabla$) and the vector field function <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.

While often introduced as a notational trick, there is a genuine connection between divergence and the dot product <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>. The dot product measures how aligned two vectors are <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. In the context of divergence:
*   Imagine taking a small step from one point in a [[understanding_vector_fields | vector field]] to another <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.
*   The dot product of this "step vector" with the "difference vector" (the change in the vector field's output caused by the step) tends to be positive in regions of positive divergence <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.
*   This is because if a step in a certain direction causes a change to the vector in that same direction, it corresponds to a tendency for outward flow <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.
*   Conversely, if these dot products tend to be negative (meaning the difference vector points opposite to the step vector), it corresponds to inward flow or negative divergence <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.
*   In essence, divergence can be thought of as an average value for this dot product of a step with the change it causes in the output, across all possible step directions <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.