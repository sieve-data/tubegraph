---
title: Vector fields and fluid flow
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

A [[vector_fields_and_fluid_flow | vector field]] is formed by associating each point in space with a [[understanding_vectors | vector]], which possesses both magnitude and direction <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. These [[understanding_vectors | vectors]] can represent physical phenomena such as the velocities of fluid particles, the force of gravity, or magnetic field strength at various points in space <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

When visually representing vector fields, it's common to artificially shorten longer [[understanding_vectors | vectors]] to prevent clutter, often using color to indicate their relative length <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. While [[vector_fields_and_fluid_flow | vector fields]] in physics can change over time (e.g., wind gusts, changing electric fields) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, this discussion primarily focuses on static, two-dimensional [[vector_fields_and_fluid_flow | vector fields]], which can be thought of as describing steady-state systems <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Conceptualizing Vector Fields as Fluid Flow

A key insight in [[understanding_vectors | understanding vectors]] and [[vector_fields_and_fluid_flow | vector fields]] is to imagine one physical phenomenon as another <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. For instance, considering [[vector_fields_and_fluid_flow | vectors]] describing gravitational force as a fluid flow can reveal properties of the original force <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This approach is particularly effective for understanding the concepts of [[divergence_in_vector_fields | divergence]] and curl, even if the field describes something like an electric field <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Divergence

When a [[vector_fields_and_fluid_flow | vector field]] is interpreted as fluid velocity, [[divergence_in_vector_fields | divergence]] at a given point quantifies how much the fluid tends to flow out of or into small regions near that point <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

*   **Sources**: Points where fluid appears to spring into existence have a positive [[divergence_in_vector_fields | divergence]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This occurs when the flow out of a region is greater than the flow into it, indicating a spontaneous generation of fluid <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Sinks**: Points where fluid seems to disappear have a negative [[divergence_in_vector_fields | divergence]] <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This happens when the fluid flowing into a region is greater than the fluid flowing out <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

The [[divergence_in_vector_fields | divergence]] of a [[vector_fields_and_fluid_flow | vector field]] is a new function that takes a 2D point as input and outputs a single number, analogous to a derivative, indicating how much that point acts as a source or sink <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. For an actual physical, incompressible fluid (like water), the velocity [[vector_fields_and_fluid_flow | vector field]] must have a [[divergence_in_vector_fields | divergence]] of zero everywhere <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This is an important constraint for real-world fluid flow problems <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## Curl

For curl, the focus is on how much the fluid tends to rotate around a point <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. If a twig dropped at a point were to spin, that indicates non-zero curl <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

*   **Positive Curl**: Regions where the fluid rotation is clockwise <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Negative Curl**: Regions where the fluid rotation is counterclockwise <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Non-zero curl can occur even if not all [[understanding_vectors | vectors]] around a point are pointing in a rotational direction; for example, if flow is slow at the bottom and quick at the top, resulting in a net rotational influence <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. While true curl is a three-dimensional concept that associates each point with a new [[understanding_vectors | vector]] characterizing rotation, the two-dimensional variant associates each point with a single number <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Applications Beyond Fluid Flow

These concepts are significant for various [[vector_fields_and_fluid_flow | vector fields]] beyond literal fluid flow. [[maxwells_equations_and_vector_calculus | Maxwell's equations]], which describe electricity and magnetism, are written in the language of [[divergence_in_vector_fields | divergence]] and curl <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

*   **Gauss's Law**: States that the [[divergence_in_vector_fields | divergence]] of an electric field at a point is proportional to the charge density there <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This can be intuitively understood by imagining positively charged regions as sources of an imagined fluid and negatively charged regions as sinks <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   The [[divergence_in_vector_fields | divergence]] of a magnetic field is zero everywhere, implying that if it were a fluid flow, it would be incompressible with no sources or sinks <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This also suggests the non-existence of magnetic monopoles <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

[[divergence_in_vector_fields | Divergence]] and curl also arise in contexts that don't initially seem spatial, such as tracking population sizes in ecology <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. In this example, the two population sizes can be seen as a point in a two-dimensional "phase space" <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A [[understanding_vectors | vector]] at each point indicates the rates of change for both populations, visualizing how the system evolves over time <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. The "phase flow" associated with this field helps conceptualize how starting states evolve, and [[divergence_in_vector_fields | divergence]] and curl can provide insights into whether population sizes converge, diverge, or exhibit stable or unstable cyclic patterns <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

## Notation and Connections

The [[divergence_in_vector_fields | divergence]] is commonly written as a [[dot_products_and_vectors | dot product]] between the "nabla" operator (an upside-down triangle) and the [[vector_fields_and_fluid_flow | vector field]] function, while curl is written as a similar cross product <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. This is more than just a notational trick; there's a genuine connection between [[divergence_in_vector_fields | divergence]] and the [[dot_products_and_vectors | dot product]], and between curl and the cross product <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

*   The [[dot_products_and_vectors | dot product]] of a small "step" [[understanding_vectors | vector]] with the resulting change in the [[vector_fields_and_fluid_flow | vector field]]'s output tends to be positive in regions of positive [[divergence_in_vector_fields | divergence]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. In essence, [[divergence_in_vector_fields | divergence]] can be seen as an average value of this [[dot_products_and_vectors | dot product]] over all possible step directions <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   Similarly, the cross product of a step [[understanding_vectors | vector]] with the resulting change in the [[vector_fields_and_fluid_flow | vector field]]'s output tends to be positive in regions of positive curl <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. Curl represents an average of this cross product, where a step causing a perpendicular change in the [[understanding_vectors | vector]] corresponds to flow rotation <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.