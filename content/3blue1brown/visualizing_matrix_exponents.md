---
title: Visualizing matrix exponents
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

Matrix exponentiation, symbolized as 'E' to the power 'A' 't' where 'A' is a matrix, initially appears as "total nonsense" when taken out of context <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. However, it represents an extremely beautiful and useful mathematical operation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. It is primarily used to solve an important class of differential equations <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Given that the universe is often described by differential equations, [[matrix_exponentiation | matrix exponents]] frequently appear in physics, particularly in [[applications_of_matrix_exponentiation_in_quantum_mechanics | quantum mechanics]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

A key aspect of understanding [[matrix_exponentiation | matrix exponents]] is the ability to visualize what they are doing using "flow" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Defining Matrix Exponentiation

The term 'E' to the power 'A' 't' does not involve multiplying the constant 'E' by itself multiple times <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Instead, its definition is based on the infinite polynomial known as the Taylor series for describing real number powers of 'E' <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This polynomial is:
`e^x = 1 + x + x^2/2! + x^3/3! + ...` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

Mathematicians became interested in plugging various objects, such as complex numbers and [[matrix_exponentiation | matrices]], into this polynomial, even when these objects do not immediately make sense as exponents <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. While this equation is a theorem for real numbers, it serves as a definition for more complex inputs <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Some authors use the name 'exp' when plugging in "exotic inputs" like matrices, as a nod to its connection to exponential functions <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

To plug a matrix into this polynomial:
*   The matrix must have the same number of rows and columns (be a square matrix) <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   Matrix powers (squaring, cubing, etc.) mean repeated [[matrixvector_multiplication | matrix multiplication]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. For example, squaring means multiplying the matrix by itself <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, and cubing means multiplying the result by the original matrix again <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Raising a matrix to the zeroth power results in the identity matrix <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   Each term in the polynomial is scaled by one divided by a factorial, which means multiplying each component of the matrix by that number <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   Matrices are added term by term <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

As terms are added in the infinite sum, the result approaches a stable value <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. For instance, exponentiating a 2x2 matrix with negative pi and pi on its off-diagonal entries results in approximately negative one times the identity matrix <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This is essentially the matrix version of Euler's famous identity <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Motivation for Matrix Exponents

Mathematicians and physicists are interested in [[matrix_exponentiation | matrix exponents]] because they help solve specific types of problems <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Two examples that motivate [[matrix_exponentiation | matrix exponents]] are:
1.  **Relationships**: A system of differential equations describing the changing affections between two lovers, Romeo and Juliet <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
2.  **[[applications_of_matrix_exponentiation_in_quantum_mechanics | Quantum Mechanics]]**: [[applications_of_matrix_exponentiation_in_quantum_mechanics | Schrodinger's equation]], which describes how quantum systems evolve over time <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

### The Romeo and Juliet Example

This system involves two changing values: Juliet's love for Romeo (x) and Romeo's love for Juliet (y) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Their rates of change are defined as:
*   `dx/dt = -y` (Juliet's love increases when Romeo shows disinterest) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>
*   `dy/dt = x` (Romeo's love decreases when Juliet is angry, grows when she loves him) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>

This is a system of differential equations <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. The values can be packaged as coordinates of a single point in a 2D space, (x,y), representing their relationship as a column vector <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The rate of change of this state is a velocity vector <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

The system can be written as a [[matrix_vector_multiplication_explained | matrix-vector multiplication]]:
`d/dt [x y] = [[0 -1] [1 0]] * [x y]` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>

The matrix `[[0 -1] [1 0]]` is a 90-degree rotation matrix <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>, which can be understood by observing how it transforms the basis vectors <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. For this system, the velocity vector is always perpendicular to the position vector <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. This implies circular motion around the origin, rotating at one radian per unit time <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. A more general rotation matrix, `[[cos t -sin t] [sin t cos t]]`, describes this kind of rotation <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. To predict where Romeo and Juliet end up after 't' units of time, one multiplies this rotation matrix by their initial state <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

### Generalizing to Solve Differential Equations

The general form of the differential equation that [[matrix_exponentiation | matrix exponents]] solve is where the rate of change of a vector is equal to a constant matrix times the vector itself <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

**One-Dimensional Case Analogy**:
The simplest case is a single changing value `x`, where its rate of change equals some constant `r` times itself: `dx/dt = r*x` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This describes phenomena like compound interest or population growth <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. The solution is `x(t) = x0 * e^(rt)`, where `x0` is the initial condition <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. The exponential term acts on the initial condition to give a solution <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

**Higher Dimensions**:
In higher dimensions, for a changing vector whose rate of change is `d/dt (vector) = M * (vector)`, the solution looks like an exponential term acting on a given initial condition vector <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. The exponential part `e^(Mt)` produces a matrix that changes with time <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. The definition of [[matrix_exponentiation | matrix exponentiation]] is motivated by ensuring this fact is true <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

For the Romeo and Juliet system, the solution is `e^(Mt) * initial_vector`, where `M = [[0 -1] [1 0]]` <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. Computing `e^(Mt)` using the Taylor series:
*   Successive powers of `M` follow a cycling pattern every four iterations <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   When summing the infinite series, each component of the resulting matrix becomes a Taylor series for either sine or cosine (or negative sine) <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.
*   This computation yields exactly the rotation matrix `[[cos t -sin t] [sin t cos t]]` <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.

This demonstrates that two different ways of reasoning—geometric analysis and [[matrix_exponentiation | matrix exponentiation]] computation—lead to the same solution for the system <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>. The initial example of exponentiating the matrix with negative pi and pi on its off-diagonals to produce the negative identity matrix is explained: it's `e^(M*pi)`, effectively rotating 180 degrees <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. This is analogous to imaginary number exponents, where `e^(it)` describes rotation <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

### [[applications_of_matrix_exponentiation_in_quantum_mechanics | Schrodinger's Equation]]
[[applications_of_matrix_exponentiation_in_quantum_mechanics | Schrodinger's famous equation]] is a fundamental equation in [[applications_of_matrix_exponentiation_in_quantum_mechanics | quantum mechanics]] <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. It shares the form `d/dt (state_vector) = (matrix) * (state_vector)` <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. The relevant matrix in Schrodinger's equation describes a kind of rotation, often in a "function space" <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. The imaginary unit `i` in Schrodinger's equation plays a role similar to the 90-degree rotation matrix in the Romeo-Juliet example, communicating that the rate of change is perpendicular to the state, leading to oscillation over time <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

## Visualizing Matrix Exponents with Vector Fields

Systems of differential equations can be visualized using a vector field <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. The equation `d/dt (vector) = M * (vector)` means that at every point `v` in space, the velocity of a state passing through that point is `M` times `v` <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

To intuitively understand how an initial condition evolves, one can "flow" along this vector field, with the velocity always matching the vector at the current point <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. The [[matrix_exponentiation | matrix]] `e^(Mt)` describes this transition from the starting point to the final point after `t` units of time <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

For the 90-degree rotation matrix example, the vector field causes circular flow, which lines up with the rotation described by `e^(Mt)` <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>. In other examples, such as a different Romeo and Juliet system where feelings feed off each other, the vector field shows states either growing towards infinity or decreasing <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. In this case, `e^(Mt)` would describe a transformation that squishes along one diagonal while stretching along another <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

The property that `e^(Mt)` times an initial condition solves these systems can be demonstrated by taking the derivative of the Taylor series: applying the power rule cancels factorial terms, showing that the derivative of the expression is `M` times the original expression <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.

## Further Considerations

Understanding the properties of [[matrix_exponentiation | matrix exponentiation]], especially its relationship with eigenvectors and eigenvalues, can lead to more concrete methods for computation <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.