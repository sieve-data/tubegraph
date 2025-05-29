---
title: Curl and its physical representation
videoId: rB83DpBJQsE
---

From: [[3blue1brown]] <br/> 

Curl is a concept in vector calculus that helps describe the rotational tendency of a vector field <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is particularly well-understood when the vector field is imagined as representing fluid flow <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

## Vector Fields: A Foundation
A vector field associates each point in space with a vector, which includes both a magnitude and a direction <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. These vectors might represent:
*   Velocities of fluid particles <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>
*   Gravitational force <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>
*   Magnetic field strength <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>

For visualization, longer vectors are often artificially shortened to prevent clutter, with color sometimes used to indicate length <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. While vector fields in physics can change over time (e.g., wind, electric fields) <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>, this discussion primarily focuses on static, two-dimensional vector fields <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

A powerful technique for understanding a vector field is to imagine it representing a different physical phenomenon <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. For instance, considering gravitational force vectors as a fluid flow can reveal insights <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

## Intuition Behind Curl (Fluid Flow Analogy)
When interpreting a vector field as fluid flow, the curl at a given point quantifies how much the fluid tends to rotate around that point <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. If a small object, like a twig, were dropped into the fluid at that point and its center fixed, the curl indicates whether it would tend to spin <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.

*   **Positive Curl**: Regions where the fluid rotation is clockwise <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **Negative Curl**: Regions where the fluid rotation is counterclockwise <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.

It's not necessary for all surrounding vectors to point in a circular fashion for non-zero curl <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>. For example, if fluid flow is slow at the bottom of a region and quick at the top, it would result in a net clockwise influence and thus non-zero curl <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

While true curl is a three-dimensional concept that associates each point with a new vector characterizing rotation <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>, the two-dimensional variant associates each point with a single number <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.

## Applications Beyond Fluid Flow
The concept of curl is significant for various types of vector fields, not just fluid dynamics <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

*   **Maxwell's Equations**: These four fundamental equations describing electricity and magnetism are written using the language of divergence and curl <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>. The way an electric or magnetic field changes depends on the curl of the other field <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. The interaction described by these equations gives rise to light waves <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.
*   **Dynamic Systems (e.g., Population Models)**: Curl can also be applied to systems that don't initially seem spatial <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. For instance, tracking population sizes of two interacting species (like predators and prey) can be visualized as a vector field in a "phase space" <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. Each point (pair of population sizes) has a vector indicating the rates of change for both variables <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>. Operations like curl can help understand if there are cyclic patterns in the system and if those cycles are stable or unstable <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.

## Notation and Mathematical Connection
Commonly, the curl is written as a [[3d_cross_product_computations | cross product]] between an "upside-down triangle thing" (∇, also known as the nabla operator) and the vector field function <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>. This is more than just a mnemonic; there's a genuine connection between curl and the [[3d_cross_product_computations | cross product]] <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>.

The [[3d_cross_product_computations | cross product]] measures how perpendicular two vectors are <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>. The curl can be thought of as a kind of average of the [[3d_cross_product_computations | cross product]] between a small "step vector" (a tiny displacement from a point) and the "difference vector" (the change in the vector field's output caused by that step) <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>. If a step in some direction causes a change in the vector field that is perpendicular to that step, it corresponds to a tendency for flow rotation <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.