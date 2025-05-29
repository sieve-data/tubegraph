---
title: Understanding vector fields
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

## Introduction to Vector Fields

A [[visualizing_mathematical_operations_using_vector_fields | vector field]] is created by associating each point in space with a vector, which includes both magnitude and direction <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. These vectors can represent various physical phenomena, such as the velocities of fluid particles <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, the force of gravity <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, or magnetic field strength <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

When drawing [[visualizing_mathematical_operations_using_vector_fields | vector fields]], it is common to artificially shorten longer vectors to prevent clutter, sometimes using color to indicate their relative length <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. While [[visualizing_mathematical_operations_using_vector_fields | vector fields]] in physics can change over time, such as wind or electric fields <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, this discussion focuses on static [[visualizing_mathematical_operations_using_vector_fields | vector fields]] that describe steady-state systems <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The focus here is also on two-dimensional [[visualizing_mathematical_operations_using_vector_fields | vector fields]], though they can exist in higher dimensions <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Conceptualizing Vector Fields through Analogy

Understanding a [[visualizing_mathematical_operations_using_vector_fields | vector field]] that represents one physical phenomenon can often be improved by imagining it as a different phenomenon <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. For example, considering gravitational force vectors as defining a fluid flow can reveal insights about the original force <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Similarly, thinking of fluid flow vectors as describing the downhill direction of a hill can be helpful <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This approach is particularly useful for intuitively grasping concepts like [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]], especially when the [[visualizing_mathematical_operations_using_vector_fields | vector field]] is interpreted as fluid flow <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Key Concepts: Divergence and Curl

### [[divergence_in_vector_fields | Divergence]] in Vector Fields

When a [[visualizing_mathematical_operations_using_vector_fields | vector field]] is visualized as fluid velocity, [[divergence_in_vector_fields | divergence]] measures how much this imagined fluid flows out of or into small regions around a point <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Sources**: Points where fluid seems to spontaneously appear have a positive [[divergence_in_vector_fields | divergence]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This also occurs if fluid flow out of a point is faster than flow into it <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Sinks**: Points where fluid seems to disappear have a negative [[divergence_in_vector_fields | divergence]] <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This happens if more fluid flows into a point than out of it <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

The [[divergence_in_vector_fields | divergence]] of a [[visualizing_mathematical_operations_using_vector_fields | vector field]] yields a new function that takes a 2D point as input and outputs a single number <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This number quantifies how much that point acts as a source or a sink <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. For an incompressible physical fluid like water, its velocity [[visualizing_mathematical_operations_using_vector_fields | vector field]] must have zero [[divergence_in_vector_fields | divergence]] everywhere <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### [[curl_in_vector_fields | Curl]] in Vector Fields

The [[curl_in_vector_fields | curl]] of a [[visualizing_mathematical_operations_using_vector_fields | vector field]] at a given point assesses the tendency of the fluid to rotate around that point <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Positive [[curl_in_vector_fields | curl]]**: Regions where rotation is clockwise <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Negative [[curl_in_vector_fields | curl]]**: Regions where rotation is counterclockwise <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
Non-zero [[curl_in_vector_fields | curl]] can exist even if vectors aren't uniformly pointing in a circular direction; for example, if flow is slow at the bottom and quick at the top, resulting in a net rotation <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. While proper [[curl_in_vector_fields | curl]] is a three-dimensional concept, often associating a point with a new vector, the two-dimensional variant associates each point with a single number <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Applications and Significance

Both [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]] are significant beyond fluid flow analogies, appearing in various scientific contexts <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Physics: Maxwell's Equations
Maxwell's equations, which describe electricity and magnetism, are written using the language of [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]] <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Gauss's Law**: States that the [[divergence_in_vector_fields | divergence]] of an electric field at a point is proportional to the charge density there <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This can be intuitively understood by imagining positive charges as fluid sources and negative charges as sinks <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Magnetic Field [[divergence_in_vector_fields | Divergence]]**: The [[divergence_in_vector_fields | divergence]] of the magnetic field is always zero <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, implying that if it were a fluid, it would be incompressible with no sources or sinks <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This also means magnetic monopoles do not exist <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Field Interdependence**: The changes in one field depend on the [[curl_in_vector_fields | curl]] of the other <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This back-and-forth relationship gives rise to light waves <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Non-Spatial Contexts: Dynamic Systems
[[divergence_in_vector_fields | Divergence]] and [[curl_in_vector_fields | curl]] are useful even in contexts that don't initially appear spatial <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. For example, in differential equations tracking population sizes of two species (e.g., predator-prey) <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>:
*   The system's state (two population sizes) can be considered a point in a two-dimensional "phase space" <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   A [[visualizing_mathematical_operations_using_vector_fields | vector field]] can represent the rates of change for both variables at each point in this phase space <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This [[visualizing_mathematical_operations_using_vector_fields | vector field]] visualizes how the system evolves over time <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   Operations like [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]] help understand system behavior, such as whether population sizes converge or diverge, or if cyclic patterns are stable <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Mathematical Connection and Notation

[[divergence_in_vector_fields | Divergence]] is commonly written as a dot product between the "nabla" (upside-down triangle) operator and the [[visualizing_mathematical_operations_using_vector_fields | vector field]] function <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. [[curl_in_vector_fields | Curl]] is similarly written as a cross product with the nabla operator <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This notation is more than a mnemonic; there is a real connection <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

### Geometric Intuition

Imagine taking a small step in a [[visualizing_mathematical_operations_using_vector_fields | vector field]] <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   The dot product of the step vector with the resulting change in the [[visualizing_mathematical_operations_using_vector_fields | vector field]]'s output tends to be positive where [[divergence_in_vector_fields | divergence]] is positive, indicating outward flow <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   The cross product of the step vector with the change in the [[visualizing_mathematical_operations_using_vector_fields | vector field]]'s output tends to be positive where [[curl_in_vector_fields | curl]] is positive <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. This corresponds to a tendency for flow rotation <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.