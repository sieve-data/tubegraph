---
title: Curl in vector fields
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

[[Curl in vector fields | Curl]] is a fundamental concept in vector calculus, often discussed alongside [[divergence_in_vector_fields | divergence]]. It describes the tendency of a [[understanding_vector_fields | vector field]] to rotate around a given point <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. While the concept is best understood by imagining the [[understanding_vector_fields | vector field]] as representing fluid flow, it applies to various other physical phenomena <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

## Understanding Curl through Fluid Flow Analogy

When a [[understanding_vector_fields | vector field]] is conceptualized as describing the velocity of a fluid at each point in space <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>, [[Curl in vector fields | curl]] measures how much this imagined fluid tends to rotate around a particular point <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

*   **Rotation Tendency**: If a small object, like a twig, were dropped into the fluid and fixed at its center, [[Curl in vector fields | curl]] indicates whether it would tend to spin <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Direction of Rotation**:
    *   Regions where the rotation is clockwise are said to have positive [[Curl in vector fields | curl]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   Regions where the rotation is counterclockwise have negative [[Curl in vector fields | curl]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Net Rotational Influence**: Non-zero [[Curl in vector fields | curl]] can occur even if not all surrounding [[vectors_in_two_and_three_dimensions | vectors]] point in a rotational direction. For example, if flow is slow at the bottom of a region but quick at the top, it can still result in a net clockwise influence, indicating non-zero curl <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Dimensionality of Curl

While the visual intuition for [[Curl in vector fields | curl]] is often provided in two dimensions <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>, true, proper [[Curl in vector fields | curl]] is a three-dimensional idea <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. In three dimensions, each point in space is associated with a new [[vectors_in_two_and_three_dimensions | vector]] characterizing the rotation around that point, determined by a right-hand rule <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. However, for a two-dimensional analysis, [[Curl in vector fields | curl]] associates each point in 2D space with a single number <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Applications of Curl

Even though the intuition for [[Curl in vector fields | curl]] is often rooted in fluid dynamics, it holds significant importance in other areas of physics and mathematics.

### [[maxwells_equations_and_vector_calculus | Maxwell's Equations]]

[[Curl in vector fields | Curl]] is a key component in [[maxwells_equations_and_vector_calculus | Maxwell's equations]], which describe electricity and magnetism <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. The last two of these four equations illustrate how the change in one field (electric or magnetic) depends on the [[Curl in vector fields | curl]] of the other field <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This interrelationship is also what gives rise to light waves <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### [[applications_of_divergence_and_curl_to_dynamic_systems | Dynamic Systems]]

[[Curl in vector fields | Curl]] can also be useful in contexts that do not initially appear spatial <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. For instance, in analyzing [[applications_of_divergence_and_curl_to_dynamic_systems | dynamic systems]] like predator-prey population models, the "state" of the system (e.g., population sizes) can be represented as a point in a multi-dimensional "phase space" <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. The rates of change of these variables form a [[understanding_vector_fields | vector field]] in this phase space <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Operations like [[Curl in vector fields | curl]] can help understand the system's behavior, such as the presence of cyclic patterns or stable/unstable cycles <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## Notation and Connection to Cross Product

The [[Curl in vector fields | curl]] of a [[understanding_vector_fields | vector field]] function (F) is commonly written as a cross product with the "nabla" operator (∇), denoted `∇ x F` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. This notation is more than just a mnemonic; there is a real connection between [[Curl in vector fields | curl]] and the cross product <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

The cross product measures how perpendicular two [[vectors_in_two_and_three_dimensions | vectors]] are <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. In the context of [[Curl in vector fields | curl]], the cross product of a small "step" [[vectors_in_two_and_three_dimensions | vector]] with the resulting change in the [[understanding_vector_fields | vector field]]'s output tends to be positive in regions of positive [[Curl in vector fields | curl]] <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Conceptually, [[Curl in vector fields | curl]] can be thought of as an average of this "step [[vectors_in_two_and_three_dimensions | vector]] difference [[vectors_in_two_and_three_dimensions | vector]] cross product" <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. If a step in a certain direction leads to a change in the [[vectors_in_two_and_three_dimensions | vector]] perpendicular to that step, it corresponds to a tendency for flow rotation <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.