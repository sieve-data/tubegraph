---
title: Matrix exponentiation
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

Matrix exponentiation is a mathematical operation that involves raising the constant 'E' (Euler's number) to the power of a matrix, resulting in another matrix <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While placing a matrix in an exponent might initially seem nonsensical out of context <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, it represents a "beautiful operation" with significant utility <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

It is primarily used to solve an important class of differential equations <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Given that the universe is often described by differential equations, matrix exponents frequently appear in physics, especially in quantum mechanics <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This concept is closely related to Schrödinger's equation <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Definition

Matrix exponentiation is not a simple repetition of multiplying the constant 'E' by itself <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Instead, its definition is based on the infinite polynomial, or Taylor series, used to describe real number powers of 'E' <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

The Taylor series for $e^x$ is:
$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

Mathematicians became interested in [[complex_plane_and_exponential_functions | plugging various types of objects]] into this polynomial, including complex numbers and, for this purpose, matrices <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

When exotic inputs are used, some authors name this infinite polynomial 'exp' <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. However, it's also common to abbreviate it as 'E' to the power of the object being plugged in, such as a complex number or a matrix <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. While the equation for real numbers is a theorem, for more exotic inputs, it serves as a definition <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Matrix Operations in the Series

To perform matrix exponentiation, the matrix must be square (have the same number of rows and columns) <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This allows for repeated [[matrix_multiplication_and_transformations | matrix multiplication]] to compute matrix powers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Squaring a matrix**: Multiplying it by itself <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Cubing a matrix**: Multiplying the squared result by the original matrix <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Whole number powers**: Repeated [[matrix_multiplication_and_transformations | multiplication]] <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Zeroth power**: A matrix raised to the zeroth power is defined as the identity matrix <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

Each term in the polynomial is scaled by one divided by a factorial, which means multiplying each component of the matrix by that number <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Adding matrices together is done term by term <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

The infinite sum for matrix exponentiation generally converges to a stable value <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. For example, applying this to a 2x2 matrix with negative pi and pi on its off-diagonal entries results in approximately negative one times the identity matrix <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This is the matrix version of Euler's famous identity <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Motivation and Application

The definition of matrix exponentiation arose from the need to solve specific problems <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Two primary motivations are:
1.  **Relationships (Systems of Differential Equations)**: A whimsical example involves tracking the love of two individuals, Romeo and Juliet <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. Their changing affections can be modeled as a system of differential equations <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   Juliet's love for Romeo ($x$) changes at a rate equal to negative one times Romeo's love for her ($y$) (i.e., $dx/dt = -y$) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   Romeo's love for Juliet ($y$) changes at a rate equal to Juliet's love for him ($x$) (i.e., $dy/dt = x$) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   These rates of change are continuously influenced by each other <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
    *   This system can be written in vector form as a differential equation where the rate of change of a vector is equal to a certain [[matrix_vector_multiplication | matrix times itself]] <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
2.  **Quantum Mechanics (Schrödinger's Equation)**: Schrödinger's equation is a fundamental equation describing how quantum mechanical systems change over time <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. It takes the form where the rate of change of a state vector (packaging system information) equals a certain matrix multiplied by that state vector <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Matrix Exponentiation as a Solution to Differential Equations

### One-Dimensional Case
The simplest example relates to ordinary [[derivatives_of_exponential_functions | exponential functions]] and is a one-dimensional case: when a single changing value's rate of change equals some constant times itself ($dx/dt = rx$) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This describes phenomena like compound interest, population growth, or early epidemic stages <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. The derivative of $e^{rt}$ is $re^{rt}$ <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. The general solution for $x(t)$ is $x(t) = x_0 e^{rt}$, where $x_0$ is the initial condition <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. The exponential term acts on the initial condition to provide the solution <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

### Multi-Dimensional Case
In higher dimensions, where a changing vector's rate of change is constrained to be some matrix times itself ($dv/dt = Mv$) <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>, the solution similarly looks like an exponential term acting on a given initial condition <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. The exponential part in this case produces a matrix that changes with time, and the initial condition is a vector <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. The definition of matrix exponentiation is heavily motivated by ensuring this fact holds true <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

### Example: Romeo and Juliet System
The Romeo and Juliet system, described by $dv/dt = Mv$ with the matrix $M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>, has a solution of the form $e^{Mt} v_0$ <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

Geometrically, this matrix represents a 90-degree rotation <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. The equation $dv/dt = Mv$ implies that the velocity vector is always perpendicular to the position vector <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>, leading to circular motion around the origin at one radian per unit time <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. The general rotation matrix by $t$ radians is $\begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix}$ <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, so the solution is this rotation matrix multiplied by the initial state <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

When computing the matrix exponential $e^{Mt}$ for $M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ using its Taylor series:
*   Successive powers of the matrix cycle every four iterations <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   Summing these infinite terms shows that each component of the resulting matrix is a Taylor series for sine or cosine <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.
*   The result is exactly the rotation matrix: $e^{\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}t} = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix}$ <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.

This demonstrates that two different approaches (geometrical reasoning and Taylor series computation) yield the same solution <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>. This alignment provides confidence in matrix exponents as solutions to such systems <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

This also explains why the matrix with negative pi and pi off the diagonals, when exponentiated, produces the negative identity matrix <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. This specific matrix corresponds to a 90-degree rotation matrix multiplied by pi, which after $\pi$ units of time rotates everything 180 degrees, equivalent to multiplying by -1 <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. This is analogous to [[complex_plane_and_exponential_functions | Euler's identity with imaginary number exponents]] <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>, where multiplication by 'i' also acts as a 90-degree rotation <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.

Matrix exponentiation of objects that act as 90-degree rotations often generates all other rotations in that same plane <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>, a concept that appears with quaternions and matrices in quantum mechanics <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>. Schrödinger's equation describes a kind of rotation, typically in a function space, often as a combination of many different rotations <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. The imaginary unit 'i' in Schrödinger's equation plays a role similar to the rotation matrix in the Romeo-Juliet example, implying that the rate of change of a state is perpendicular to that state, leading to oscillation <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

## Visualization with Vector Fields

Matrix exponentiation can be visualized using a vector field <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. The equation $dv/dt = Mv$ means that the velocity of a state is determined by its position <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. To visualize this, a vector representing $Mv$ is drawn at every point $v$ in the space, indicating the velocity of a state passing through that point <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

To understand how any initial condition will evolve, one imagines it "flowing" along this field, with its velocity always matching the vector it is currently on <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. If $e^{Mt} v_0$ solves these systems, it means that the matrix $e^{Mt}$ describes the transformation of all possible initial conditions as they flow along this field for $t$ units of time <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

For the 90-degree rotation matrix example, the vector field shows circular flow, and $e^{Mt}$ indeed describes rotation <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>. For other matrices, like one describing Romeo and Juliet's relationship where feelings feed off each other (e.g., $dx/dt = y, dy/dt = x$), the flow field shows divergence along certain diagonals (unbounded growth) and convergence along others (decay) <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>. The resulting exponential matrix describes this squishing along one diagonal and stretching along another <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>.

### Proof Sketch

To demonstrate why $e^{Mt}v_0$ solves $dv/dt = Mv$:
1.  Write out the Taylor series for $e^{Mt}$ and multiply it by the initial condition vector $v_0$ <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
2.  Take the derivative of this expression with respect to time $t$ <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>.
3.  Since the matrix $M$ is constant, the power rule can be applied to each term <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>.
4.  The power rule naturally cancels out with the factorial terms in the denominator <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>.
5.  This leaves an expression where each term has an extra $M$ factored out to the left <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.
6.  Thus, the derivative of the expression is $M$ times the original expression, confirming it solves the equation <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

This sketch omits details regarding the convergence of the infinite series <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.

## Further Exploration

Future topics related to matrix exponentiation include its properties, especially its relationship with eigenvectors and eigenvalues, which offer more concrete ways to compute the operation <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. Another interesting concept is raising 'E' to the power of the derivative operator <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.