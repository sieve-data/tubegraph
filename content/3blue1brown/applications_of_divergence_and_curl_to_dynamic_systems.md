---
title: Applications of divergence and curl to dynamic systems
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

[[divergence_in_vector_fields | Divergence]] and [[curl_in_vector_fields | curl]] are fundamental concepts used to understand the behavior of vector fields <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While often introduced in the context of physical fields like fluid flow, they also provide powerful tools for analyzing dynamic systems where the "space" is more abstract, such as the phase space of a system of [[differential_equations_and_their_applications | differential equations]] <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

## Vector Fields and Dynamic Systems

A vector field associates each point in space with a vector, possessing both magnitude and direction <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Traditionally, these vectors might represent fluid velocities <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, gravitational force <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, or magnetic field strength <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While vector fields in physics can change over time (e.g., wind gusts or changing electric fields) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, static (steady-state) two-dimensional fields are often considered for foundational understanding <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

A key conceptual tool is to interpret a vector field that represents one physical phenomenon as if it represented a different one, such as fluid flow <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This analogy is particularly helpful for understanding [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]] viscerally <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

### Divergence and Curl in Brief

*   **[[divergence_in_vector_fields | Divergence]]**: For a fluid flow, the [[divergence_in_vector_fields | divergence]] at a point indicates how much the fluid tends to flow out of (source, positive [[divergence_in_vector_fields | divergence]]) or into (sink, negative [[divergence_in_vector_fields | divergence]]) small regions near it <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It's analogous to a [[calculating_derivatives_and_their_applications | derivative]] <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. For an incompressible fluid like water, the velocity vector field must have a [[divergence_in_vector_fields | divergence]] of zero everywhere <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **[[curl_in_vector_fields | Curl]]**: For a fluid flow, the [[curl_in_vector_fields | curl]] at a point measures how much the fluid tends to rotate around that point <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Clockwise rotation typically indicates positive [[curl_in_vector_fields | curl]], while counterclockwise indicates negative [[curl_in_vector_fields | curl]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Application to Dynamic Systems

Beyond physical fields, [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]] are highly relevant in contexts that do not initially appear spatial <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. A classic example studied in [[differential_equations_and_their_applications | differential equations]] involves tracking the population sizes of two interacting species, such as a predator and prey <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Phase Space and Phase Flow

1.  **System State as a Point**: The state of such a system at a given time—the two population sizes—can be represented as a point in a two-dimensional space known as the "phase space" <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
2.  **Rates of Change and Vector Fields**: The rates at which these populations change, based on factors like reproduction and predation, are typically described by a set of [[differential_equations_and_their_applications | differential equations]] <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. These equations define a vector field where each point in phase space (each pair of population sizes) is associated with a vector <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This vector indicates both how and how quickly the population sizes tend to change <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
3.  **Phase Flow Visualization**: This vector field represents a dynamic system that evolves over time, rather than a physical space <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The "flow" associated with this field is called the *phase flow*, offering a visual conceptualization of how different starting states evolve over time <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Insights from Divergence and Curl

For such dynamic systems, [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]] can provide critical insights into the system's behavior <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:

*   **Convergence or Divergence**: [[divergence_in_vector_fields | Divergence]] helps determine if population sizes converge towards a specific pair of numbers or diverge away from certain values <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   **Cyclic Patterns**: [[curl_in_vector_fields | Curl]] can reveal the presence of cyclic patterns in the system, such as population oscillations, and whether these cycles are stable or unstable <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

While other tools might be needed for a complete understanding of complex dynamic systems <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>, the conceptual framework provided by [[divergence_in_vector_fields | divergence]] and [[curl_in_vector_fields | curl]] is highly valuable for analyzing such systems <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. Understanding their computation and interpretation is crucial for their [[calculating_derivatives_and_their_applications | applications of derivatives in real-world phenomena]] <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.