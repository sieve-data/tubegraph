---
title: Solving systems of differential equations using matrices
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

Matrix exponentiation, represented as `e` to the power `A` `t` (where `A` is a matrix), refers to a beautiful and useful operation that plays a significant role in mathematics and [[differential_equations_in_physics | physics]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This operation is primarily used to [[solving_differential_equations_with_examples | solve a very important class of differential equations]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. It is particularly common in quantum mechanics, where matrix exponents are widely used, notably in relation to Schrodinger's equation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Defining Matrix Exponentiation

Taking a matrix to an exponent might seem like nonsense out of context <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It is not a bizarre way to multiply the constant `E` by itself multiple times <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The [[basics_and_significance_of_differential_equations | actual definition is related to a certain infinite polynomial]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, known as its Taylor series, used for describing real number powers of `E` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

Mathematicians became interested in plugging various mathematical objects, including complex numbers and matrices, into this polynomial, even when they don't immediately make sense as exponents <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This operation is sometimes given the name `exp` when dealing with more exotic inputs, or more commonly, abbreviated as `E` to the power of the object being plugged in <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. While this equation is a theorem for real numbers, it acts as a definition for more complex inputs <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### How Matrices Are Used in the Polynomial
To plug a matrix into this polynomial:
*   The [[mathematical_representation_with_3x3_matrices | matrix has to have the same number of rows and columns]] <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This allows for repeated matrix multiplication to compute powers (squaring, cubing, etc.) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Each term in the polynomial is scaled by one divided by some factorial, which means multiplying each component of the matrix by that number <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   Matrices are added together term by term <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Example: Matrix with Negative Pi and Pi
Consider a 2x2 matrix with negative pi and pi off its diagonal entries <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. When computed through the infinite sum, the result approaches negative one times the identity matrix <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This is essentially the matrix version of Euler's famous identity <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. In general, no matter what matrix is used, the infinite sum eventually approaches a stable value <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Motivation: Solving Systems of Differential Equations

The primary motivation for matrix exponents comes from solving specific problems, particularly systems of differential equations <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### The Romeo and Juliet Example

A simple example involves the changing love between Romeo and Juliet <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Let `x` be Juliet's love for Romeo and `y` be his love for her. Their dynamic is described by:
*   `dx/dt = -y` (Juliet's love increases when Romeo is cool, decreases when he's infatuated) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
*   `dy/dt = x` (Romeo's love decreases when Juliet is mad, grows when she loves him) <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

This is a [[basics_and_significance_of_differential_equations | system of differential equations]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, where the challenge is to [[basics_and_significance_of_differential_equations | find explicit functions for x of t and y of t that make both of these expressions true]] <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, matching an initial set of conditions at time `t = 0` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

To solve this systematically without guessing, we can package `x` and `y` as coordinates of a single point in a 2D space, represented as a column vector `[x;y]` <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. The rate of change of this state, represented as a velocity vector `[dx/dt; dy/dt]`, can be written as a product of a matrix with the original vector `[x;y]` <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>:

`d/dt [x;y] = [[0, -1], [1, 0]] * [x;y]` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>

The matrix `[[0, -1], [1, 0]]` is a 90-degree rotation matrix <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. Geometrically, if a state's rate of change (velocity) is always perpendicular to its position, it implies circular motion around the origin <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Since the length of the velocity vector equals the length of the position vector, it rotates at one radian per unit time <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

The solution to predict where Romeo and Juliet end up after `t` units of time can be described by a general rotation matrix:

`[[cos(t), -sin(t)], [sin(t), cos(t)]]` <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>

Multiplying this matrix by their initial state `[x0;y0]` gives their state at time `t` <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

### How Matrix Exponents Provide the Solution

The solution to a system where the rate of change of a vector equals a matrix times itself (`d/dt **v** = M**v**`) looks like an exponential term acting on a given initial condition <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.

For the Romeo and Juliet system, the solution is `**v**(t) = e^(Mt) * **v**0` <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
When we compute `e^(Mt)` using its Taylor series definition for `M = [[0, -1], [1, 0]]`:
The successive powers of this matrix fall into a cycling pattern every four iterations <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. When all infinite terms are summed, the components of the resulting matrix are the Taylor series for sine and cosine <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
This computation results in exactly the rotation matrix `[[cos(t), -sin(t)], [sin(t), cos(t)]]` <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>, confirming that the analytic definition of matrix exponentiation aligns with the geometric understanding of the system.

This concept explains why `e^(M*pi)` for the 90-degree rotation matrix `M` with `t=pi` produces the negative identity matrix `[[-1, 0], [0, -1]]` <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. It's a rotation of 180 degrees in the state space <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

### Other Applications

*   **Schrodinger's Equation**: This fundamental equation in [[introduction_to_partial_differential_equations | quantum mechanics]] <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a> (`iħ dΨ/dt = HΨ`) also has the form where the rate of change of a state vector equals a matrix (or operator) times that state <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. The imaginary unit `i` plays a similar role to the rotation matrix in the Romeo-Juliet example, implying an oscillatory evolution over time <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.
*   **One-Dimensional Case**: The simplest example is `dx/dt = rx` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>, where a single changing value's rate of change is proportional to itself. This is solved by `x(t) = e^(rt) * x0`, where `x0` is the initial condition <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

## Visualizing Solutions with Vector Fields

Systems of differential equations like `d/dt **v** = M**v**` can be visualized using a vector field <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. At every point `**v**` in the space, a little vector `M**v**` is drawn, indicating the velocity a state would have if it passed through that point <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

To understand how an initial condition evolves, one can imagine it "flowing" along this field, with its velocity always matching the vector at its current position <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. The matrix `e^(Mt)` describes the transformation (or transition) from the initial state at time 0 to the final state at time `t` <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

For instance, a different set of equations for Romeo and Juliet, `dx/dt = x+y`, `dy/dt = x+y` (represented by `M = [[1, 1], [1, 1]]`), shows flow that causes feelings to either feed off each other towards infinity or rapidly diminish towards negative infinity <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. This visual intuition suggests that the resulting matrix `e^(Mt)` will squish along one diagonal and stretch along another <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>.

## Why `e^(Mt)` Solves the Equation

The solution `**v**(t) = e^(Mt) * **v**0` can be shown to satisfy the differential equation `d/dt **v** = M**v**` by differentiating the Taylor series definition of `e^(Mt)` <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

Taking the derivative of `e^(Mt) * **v**0` with respect to `t`:
1.  Write out the full polynomial definition.
2.  Apply the power rule to each term, which cancels out factorial terms.
3.  The result is an expression where each term has an extra `M` hanging on to it.
4.  This `M` can be factored out to the left, showing that the derivative of the expression is `M` times the original expression <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.
Thus, `e^(Mt)` acting on an initial condition `**v**0` indeed solves the system.

In subsequent discussions, properties of matrix exponentiation, its relationship with [[numerical_methods_for_solving_differential_equations | eigenvectors and eigenvalues]] <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>, and more concrete computational methods can be explored.