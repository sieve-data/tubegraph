---
title: Maxwells equations and vector calculus
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

Vector calculus provides the mathematical framework for understanding physical phenomena described by [[understanding_vector_fields | vector fields]], such as fluid flow, gravitational force, electric fields, and magnetic fields <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Key concepts in this framework, particularly [[Divergence in vector fields | divergence]] and [[Curl in vector fields | curl]], are essential for describing phenomena like electricity and magnetism through Maxwell's equations <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

## Understanding Vector Fields
A [[understanding_vector_fields | vector field]] assigns a vector (with magnitude and direction) to each point in space <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. These vectors might represent fluid velocities <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, gravitational force <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, or magnetic field strength <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. For visualization, vectors are often artificially shortened, with color indicating magnitude, to avoid clutter <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. While [[understanding_vector_fields | vector fields]] can change over time (e.g., wind gusts) and be three-dimensional, static, two-dimensional fields are often studied first to build intuition <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

A useful approach to understand a [[understanding_vector_fields | vector field]] is to imagine it representing a different physical phenomenon <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. For instance, considering a gravitational force field as a fluid flow can reveal insights <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The concepts of [[Divergence in vector fields | divergence]] and [[Curl in vector fields | curl]] are particularly well-understood when a [[understanding_vector_fields | vector field]] is visualized as fluid flow, even if it represents something else, like an electric field <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

### Divergence
[[Divergence in vector fields | Divergence]] measures how much an imagined fluid tends to flow out of or into a small region around a point in a [[understanding_vector_fields | vector field]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Positive Divergence:** Indicates a "source" where fluid appears to spring into existence <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, or where more fluid flows out than in <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Negative Divergence:** Indicates a "sink" where fluid seems to disappear <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, or where more fluid flows in than out <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   The [[Divergence in vector fields | divergence]] of a [[understanding_vector_fields | vector field]] yields a new function that outputs a single number, indicating how much a point acts as a source or sink <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

For an incompressible fluid, like water, its velocity [[understanding_vector_fields | vector field]] must have a [[Divergence in vector fields | divergence]] of zero everywhere <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Curl
[[Curl in vector fields | Curl]] measures the tendency of an imagined fluid to rotate around a point in a [[understanding_vector_fields | vector field]] <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Positive Curl:** Corresponds to regions where the rotation is clockwise <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Negative Curl:** Corresponds to regions where the rotation is counterclockwise <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   Even if vectors don't explicitly form a circle, a point can have non-zero [[Curl in vector fields | curl]] if flow is slower on one side and quicker on another, resulting in net rotational influence <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

While true [[Curl in vector fields | curl]] is a three-dimensional concept yielding a vector <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, its two-dimensional variant associates each point with a single number <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Maxwell's Equations
Maxwell's equations are a set of four fundamental equations that describe electricity and magnetism <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. They are written using the language of [[Divergence in vector fields | divergence]] and [[Curl in vector fields | curl]] <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### Gauss's Law (First Maxwell Equation)
The first equation, Gauss's law, states that the [[Divergence in vector fields | divergence]] of an electric field at a given point is proportional to the charge density at that point <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   This can be intuitively understood by imagining positively charged regions as "sources" of an electric fluid, and negatively charged regions as "sinks" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   In charge-free regions, the "electric fluid" would flow incompressibly, like water <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Divergence of Magnetic Field (Second Maxwell Equation)
Another crucial equation states that the [[Divergence in vector fields | divergence]] of the magnetic field is zero everywhere <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   This implies that if the magnetic field represented a fluid flow, it would be incompressible, with no sources or sinks, behaving like water <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   This equation also indicates that magnetic monopoles (isolated north or south poles of a magnet) do not exist, unlike positive and negative charges in an electric field <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Curl in Maxwell's Equations
The remaining two Maxwell's equations relate the change in one field to the [[Curl in vector fields | curl]] of the other field <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. These are primarily three-dimensional concepts, but they demonstrate how [[Divergence in vector fields | divergence]] and [[Curl in vector fields | curl]] are significant in contexts beyond fluid flow <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. The interplay described by these equations is what generates light waves <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Applications Beyond Physical Space
The concepts of [[Divergence in vector fields | divergence]] and [[Curl in vector fields | curl]] are useful even in contexts that don't initially seem spatial <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Dynamic Systems (Phase Space):** For example, tracking the population sizes of two species (e.g., predator-prey) can be visualized in a two-dimensional "phase space" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   Each point in this space (representing a pair of population sizes) can be associated with a vector indicating the rates of change for both variables, forming a [[understanding_vector_fields | vector field]] <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. These rates are often described by [[differential_equations_as_a_language_of_physics | differential equations]] <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   This "phase flow" helps conceptualize how starting states evolve over time <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
    *   Operations like [[Divergence in vector fields | divergence]] and [[Curl in vector fields | curl]] can inform whether population sizes converge, diverge, or exhibit cyclic patterns <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Notation and Underlying Connections
The [[Divergence in vector fields | divergence]] and [[Curl in vector fields | curl]] are commonly written using a notation that suggests a dot product or cross product with an upside-down triangle symbol (nabla, $\nabla$) <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. While often taught as a mnemonic trick, there is a real connection:
*   **Divergence and Dot Product:** The [[Divergence in vector fields | divergence]] can be seen as an average value of the dot product between a small "step vector" and the "difference vector" it causes in the output of the [[understanding_vector_fields | vector field]] over all possible step directions <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   If a step in a direction causes a change in the same direction, it corresponds to outward flow (positive divergence) <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
    *   If the change is in the opposite direction, it corresponds to inward flow (negative divergence) <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Curl and Cross Product:** Similarly, the [[Curl in vector fields | curl]] can be viewed as an average of the cross product between a step vector and the difference vector it causes <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
    *   If a step causes a change perpendicular to that step, it corresponds to a tendency for flow rotation <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.