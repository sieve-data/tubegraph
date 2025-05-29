---
title: Schrodingers equation and quantum mechanics
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

Matrix exponents play a prominent role in [[quantum_mechanics_basics_for_beginners | quantum mechanics]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This is largely due to Schrödinger's equation <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, which is a fundamental equation in [[quantum_mechanics_basics_for_beginners | quantum mechanics]] describing how systems change over time <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

## Nature of Schrödinger's Equation

While it may appear intimidating, Schrödinger's equation shares similarities with simpler systems of [[differential_equations_as_a_language_of_physics | differential equations]] <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

The equation focuses on a "state vector" (often represented by the symbol $\Psi$) <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. This vector packages all relevant information about a system, such as a particle's positions and momenta <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. The equation states that the rate at which this state vector changes is equal to a certain matrix multiplied by itself <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Analogy to Simpler Systems

For comparison, consider a two-dimensional system (like the "Romeo-Juliet" example) where the rate of change of a vector is equal to a matrix times itself <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Schrödinger's equation is a more complicated variation of this theme <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

While Schrödinger's equation has additional complexities <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>, it can be viewed as a more advanced version of these simpler examples <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

## Role of Matrix Exponents

In [[quantum_mechanics_basics_for_beginners | quantum mechanics]], the relevant matrices involved in Schrödinger's equation describe a kind of rotation <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. Often, this rotation occurs in a high-dimensional function space <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.

Matrix exponentiation is crucial for solving these types of [[differential_equations_as_a_language_of_physics | differential equations]] <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>, including Schrödinger's equation <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. Just as the solution to a one-dimensional [[differential_equations_as_a_language_of_physics | differential equation]] $dx/dt = rx$ is $x(t) = e^{rt}x_0$ <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>, <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>, the solution for a changing vector whose rate of change is a matrix times itself is also an exponential term acting on an initial condition <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>, <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

This means that solutions to Schrödinger's equation look like $e^{Mt}$ times some initial state, where $M$ is the relevant matrix <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>, <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

### The Imaginary Unit 'i'

The imaginary unit 'i', which appears prominently in Schrödinger's equation <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>, plays a role analogous to the rotation matrix seen in the Romeo-Juliet example <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>. Multiplication by 'i' also acts like a 90-degree rotation <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. This implies that the rate of change of a quantum state is, in a sense, "perpendicular" to that state, leading to an oscillatory evolution over time <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.

Many matrices found in [[quantum_mechanics_basics_for_beginners | quantum mechanics]] are linked to [[applications_of_quaternions_in_threedimensional_rotations_and_quantum_mechanics | quaternions]] <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. The general principle is that exponentiating an operation that performs a 90-degree rotation generates all other rotations in that same plane <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. Schrödinger's equation falls under this general idea <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.