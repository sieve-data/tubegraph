---
title: Differential equations and their applications
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

Differential equations are fundamental mathematical constructs used to describe how systems change over time <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. The universe itself is often described in the [[differential_equations_as_a_language_of_physics | language of differential equations]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. They appear frequently in physics, especially in quantum mechanics, where matrix exponents play a prominent role <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Matrix Exponents: A Tool for Solving Differential Equations

A key operation used to solve important classes of differential equations involves exponentiating matrices <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This concept, while seemingly unusual, is extremely beautiful and useful <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Definition of Matrix Exponentiation

Matrix exponentiation, written as 'E' to the power 'A' 't' where 'A' is a matrix, is not a simple repeated multiplication of a constant 'E' <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Instead, its actual definition is related to the Taylor series for real number powers of 'E' <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

The Taylor series for e^x is:
```
e^x = 1 + x + x^2/2! + x^3/3! + ...
```
Mathematicians extended this polynomial to accommodate more "exotic inputs" like complex numbers and, for the purpose of differential equations, matrices <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This extension is either given the name 'exp' or, more commonly, abbreviated as 'E' to the power of the object being plugged in <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

For matrix exponentiation:
- The matrix must have the same number of rows and columns to allow for self-multiplication <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
- Powers of a matrix mean repeated matrix multiplication (e.g., A^2 = A * A) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
- Each term in the polynomial is scaled by one divided by a factorial, meaning each component of the matrix is multiplied by that number <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
- Matrices can be added term by term <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

Example: For the 2x2 matrix with negative pi and pi on its off-diagonal entries, the infinite sum of its matrix exponentiation approaches the negative identity matrix <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>, <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This is essentially the matrix version of Euler's famous identity <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Why Matrix Exponents? Solving Systems of Differential Equations

Mathematicians and physicists are interested in matrix exponents because they systematically solve certain types of differential equations <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. The definition of matrix exponentiation is heavily motivated by its utility in this context <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

## Applications of Differential Equations

### 1. The One-Dimensional Case (Exponential Growth)

The simplest example of a differential equation is the one-dimensional case: when a single changing value's rate of change is proportional to the value itself (dx/dt = r*x) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>, <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

This equation governs:
- Compound interest <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>
- Early stages of population growth <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>
- Early stages of an epidemic <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>

The solution to this equation is x(t) = x₀ * e^(rt), where x₀ is the initial condition <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>, <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. The exponential part (e^(rt)) acts on the initial condition to provide the solution <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

### 2. Romeo and Juliet: A System of Coupled Differential Equations

This example models the changing affections between two lovers, Romeo and Juliet, as a system of two coupled differential equations <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

- **Juliet's love (x):** The rate of change of her love is negative one times Romeo's love for her (dx/dt = -y) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Her feelings increase when he shows disinterest, and fade when he becomes too infatuated <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
- **Romeo's love (y):** The rate of change of his love is equal to Juliet's love (dy/dt = x) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. His affections decrease when she is mad and grow when she loves him <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

This system can be represented as a vector equation: d/dt [x y] = A [x y], where A is the matrix [0 -1; 1 0] <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. This matrix is a 90-degree rotation matrix <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>, meaning the rate of change (velocity vector) is always perpendicular to the current position vector <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. This implies circular motion around the origin at one radian per unit time <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

The solution for this system is a rotation matrix multiplied by the initial state <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. Importantly, applying the matrix exponentiation definition to the rotation matrix times time yields exactly this rotation matrix <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>, <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>. This demonstrates how matrix exponents provide a systematic way to solve such systems <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.

### 3. Schrodinger's Equation: Quantum Mechanics

Schrodinger's equation is the fundamental equation describing how systems in quantum mechanics change over time <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>, <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. It shares a similar form to the Romeo-Juliet example: the rate of change of a state vector equals a certain matrix times itself <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>, <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

The imaginary unit 'i' in Schrodinger's equation plays a role analogous to the rotation matrix in the Romeo-Juliet example, indicating that the rate of change of a state is, in a sense, perpendicular to that state <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>, <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. This implies that the evolution over time involves a kind of oscillation <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

### 4. Generalization: Other Systems

Systems of differential equations where the rate of change of a vector equals a matrix times itself can represent various phenomena beyond simple rotation <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. For instance, a different "Shakespearean" Romeo and Juliet model where both are inclined to get carried away by each other's feelings leads to a vector field where feelings can feed off each other and tend towards infinity or decrease depending on the initial state <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>, <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. The matrix exponent for such a system would describe a transformation that squishes along one diagonal while stretching along another <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

## Visualizing Differential Equations with Vector Fields

[[phase_space_and_visualization_of_differential_equations | Differential equations can be visualized using vector fields]] <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. The equation tells us that the velocity of a state is entirely determined by its position <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. To visualize this, at every point 'v' in the space, a little vector representing M times 'v' (the velocity) is drawn <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>, <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.

To understand how an initial condition evolves, one can imagine it "flowing" along this field, with its velocity always matching the vector at its current position <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>, <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. The matrix e^(Mt) then describes the transition from the start to the finish point after 't' units of time <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

## Matrix Exponentiation as a Solution

The solution to the differential equation d/dt (vector) = M * (vector) is given by (vector at time t) = e^(Mt) * (initial condition vector) <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>, <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This can be intuitively understood by taking the [[calculating_derivatives_and_their_applications | derivative]] of the matrix exponentiation's Taylor series:
1. Write out the polynomial for e^(Mt) multiplied by the initial condition vector <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
2. Take the derivative with respect to 't', applying the power rule to each term <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>.
3. The power rule conveniently cancels with the factorial terms <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>.
4. This leaves an expression where an extra 'M' can be factored out, showing that the derivative of the expression is M times the original expression, thus satisfying the differential equation <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>, <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

This demonstrates that matrix exponentiation provides an explicit solution to these systems of differential equations <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

Further understanding of this operation involves exploring its properties, particularly its relationship with eigenvectors and eigenvalues, which provide more concrete ways to compute it <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>, <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.