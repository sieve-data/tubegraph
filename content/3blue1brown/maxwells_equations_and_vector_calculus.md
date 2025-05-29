---
title: Maxwells equations and vector calculus
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

[[Maxwells equations and electromagnetic waves|Maxwell's equations]] are a set of four fundamental equations that describe electricity and magnetism. These equations are expressed using the language of [[Divergence in vector fields|divergence]] and [[Divergence in vector fields|curl]], key concepts in [[Multivariable Calculus and Complex Analysis|multivariable calculus]] <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Vector Fields

A [[Vector fields and fluid flow|vector field]] associates each point in space with a vector, which has both magnitude and direction <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. These vectors can represent various physical phenomena, such as the velocities of particles in [[Vector fields and fluid flow|fluid flow]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, gravitational force <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, or magnetic field strength <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

For conceptual understanding, it is often helpful to imagine a [[Vector fields and fluid flow|vector field]], even if it represents something like gravitational force or an electric field, as defining a [[Vector fields and fluid flow|fluid flow]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This analogy helps in viscerally understanding ideas like [[Divergence in vector fields|divergence]] and [[Divergence in vector fields|curl]] <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. While vector fields in physics can change over time (dynamic) and be three-dimensional or higher, the discussion often simplifies to static, two-dimensional vector fields for clarity <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Divergence

The [[Divergence in vector fields|divergence]] of a [[Vector fields and fluid flow|vector field]] at a specific point indicates how much the imagined fluid tends to flow out of or into small regions near that point <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Positive [[Divergence in vector fields|Divergence]]**: Implies a "source," where fluid seems to originate from nothingness or where outward flow is greater than inward flow <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Negative [[Divergence in vector fields|Divergence]]**: Implies a "sink," where fluid seems to disappear <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

[[Divergence in vector fields|Divergence]] produces a new function that takes a 2D point as input and outputs a single number, measuring the extent to which that point acts as a source or a sink <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. For an incompressible fluid, its velocity [[Vector fields and fluid flow|vector field]] must have a [[Divergence in vector fields|divergence]] of zero everywhere <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Curl

The [[Divergence in vector fields|curl]] of a [[Vector fields and fluid flow|vector field]] at a given point describes how much the imagined fluid tends to rotate around that point <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Positive [[Divergence in vector fields|Curl]]**: Indicates a tendency for clockwise rotation <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Negative [[Divergence in vector fields|Curl]]**: Indicates a tendency for counterclockwise rotation <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Similar to [[Divergence in vector fields|divergence]], the 2D variant of [[Divergence in vector fields|curl]] associates each point with a single number representing the rotational tendency <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Maxwell's Equations and Vector Calculus Concepts

[[Maxwells equations and electromagnetic waves|Maxwell's equations]] are written in terms of [[Divergence in vector fields|divergence]] and [[Divergence in vector fields|curl]], illustrating how these concepts are crucial for describing electromagnetic phenomena <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

1.  **Gauss's Law for Electric Fields**: This equation states that the [[Divergence in vector fields|divergence]] of an electric field at a given point is proportional to the charge density at that point <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   **Intuition**: Positively charged regions behave like sources of an imagined fluid, and negatively charged regions act as sinks <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. In areas without charge, the "electric fluid" would flow incompressibly, like water <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

2.  **Gauss's Law for Magnetism**: This equation states that the [[Divergence in vector fields|divergence]] of the magnetic field is zero everywhere <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
    *   **Intuition**: If the magnetic field represented a fluid flow, that fluid would be incompressible, having no sources or sinks <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This also implies that magnetic monopoles (isolated north or south poles) do not exist, unlike positive and negative charges in an electric field <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

The remaining two [[Maxwells equations and electromagnetic waves|Maxwell's equations]] describe how one field's change depends on the [[Divergence in vector fields|curl]] of the other field <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. These interactions, which are inherently three-dimensional, are what give rise to [[Maxwells equations and electromagnetic waves|light waves]] <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Notation and Underlying Connections

Commonly, [[Divergence in vector fields|divergence]] is notated as a dot product involving the "nabla" operator (an upside-down triangle symbol), and [[Divergence in vector fields|curl]] is notated as a cross product with the same operator <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>, <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This notation is more than a mnemonic; it reflects a deep connection between [[Divergence in vector fields|divergence]] and the dot product, and between [[Divergence in vector fields|curl]] and the cross product <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>, <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

*   **[[Divergence in vector fields|Divergence]]**: Relates to the dot product of a small "step vector" with the change in the [[Vector fields and fluid flow|vector field]]'s output caused by that step <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. A positive dot product in this context corresponds to outward flow and positive [[Divergence in vector fields|divergence]] <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **[[Divergence in vector fields|Curl]]**: Relates to the cross product of the step vector with the change in the [[Vector fields and fluid flow|vector field]]'s output <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. A positive cross product implies a tendency for flow rotation and positive [[Divergence in vector fields|curl]] <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.