---
title: Matrix exponentiation
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

[[Matrix exponentiation]] involves raising the mathematical constant 'E' to the power of a matrix (e.g., e<sup>At</sup>), where 'A' is a matrix and the result is also a matrix <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This operation, while initially appearing to be "total nonsense" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, is a powerful and elegant mathematical concept used to solve a significant class of differential equations <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Its utility extends deeply into physics, particularly in [[applications_of_matrix_exponentiation_in_quantum_mechanics | quantum mechanics]], where matrix exponents are frequently encountered <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> and play a prominent role in equations like Schrodinger's equation <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Defining Matrix Exponentiation

[[Matrix exponentiation]] is not a simple multiplication of the constant 'E' by itself multiple times <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Instead, its definition is rooted in the Taylor series (an infinite polynomial) for describing real number powers of 'E' <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

The Taylor series for e<sup>x</sup> is:
$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots $ <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>

Mathematicians became interested in plugging various mathematical objects, such as complex numbers and matrices, into this polynomial, even if they don't intuitively make sense as exponents <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. While some authors use the notation 'exp(A)' for such "exotic inputs," it is equally common to use the shorthand 'E' to the power of the object, like e<sup>A</sup> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. For real numbers, this equation is a theorem, but for matrices and other complex inputs, it serves as the definition <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

To compute `e^A` for a matrix 'A', the matrix must have the same number of rows and columns, allowing it to be multiplied by itself <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Matrix Powers**: Squaring a matrix means multiplying it by itself (A * A) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Cubing means multiplying the squared result by the original matrix again (A^2 * A) <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Powers here signify repeated [[matrixvector multiplication | multiplication]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. The zeroth power of a matrix is defined as the identity matrix <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Scalar Multiplication**: Each term in the polynomial is scaled by `1/n!`, which means multiplying each component of the matrix by that scalar <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Matrix Addition**: Matrices are added term by term <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Example of Matrix Exponentiation (Rotation)

Consider a 2x2 matrix with negative pi and pi on its off-diagonal entries:
$ A = \begin{pmatrix} 0 & -\pi \\ \pi & 0 \end{pmatrix} $ <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

When the infinite sum of its Taylor series is computed, it approaches a stable value of approximately negative one times the identity matrix <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This specific result is the matrix version of Euler's famous identity <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

In general, for any matrix 'A', as more terms are added to the Taylor series, the sum eventually converges to a stable value <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Motivation and Applications

The definition of [[matrix exponentiation]] arose from mathematicians and physicists seeking solutions to specific problems, rather than as an arbitrary starting point <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Two key motivations include modeling relationships and solving problems in [[applications_of_matrix_exponentiation_in_quantum_mechanics | quantum mechanics]] <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Systems of Differential Equations

[[Matrix exponentiation]] is primarily motivated by its use in solving systems of linear differential equations of the form:
$ \frac{d\vec{v}}{dt} = M\vec{v} $ <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>

Where $\vec{v}$ is a vector whose components change over time, and 'M' is a constant matrix.

#### Romeo and Juliet Example (Linear System)

Consider a system modeling the changing affections of Romeo (y) and Juliet (x) based on the following rules:
*   Juliet's love for Romeo (x) changes at a rate equal to negative one times Romeo's love for her (dy/dt = -y) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   Romeo's love for Juliet (y) changes at a rate equal to Juliet's love for him (dy/dt = x) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

This system can be written in vector form as:
$ \frac{d}{dt} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} $ <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>

The matrix $M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is a 90-degree rotation matrix <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
Geometrically, this means the velocity vector of the relationship (point (x,y)) is always perpendicular to its current position vector <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. This results in circular motion around the origin at one radian per unit time <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

The solution to this system, which predicts Romeo and Juliet's affections after 't' units of time, involves multiplying a general rotation matrix by their initial state <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>:
$ \begin{pmatrix} x(t) \\ y(t) \end{pmatrix} = \begin{pmatrix} \cos(t) & -\sin(t) \\ \sin(t) & \cos(t) \end{pmatrix} \begin{pmatrix} x_0 \\ y_0 \end{pmatrix} $ <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>, <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>

This specific form of the solution leads directly to [[matrix exponentiation]]. The claim is that solutions to such differential equations look like $e^{Mt} \cdot \vec{v}_0$, where $\vec{v}_0$ is the initial condition vector <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.

For the Romeo and Juliet example, computing $e^{Mt}$ where $M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ by plugging it into its Taylor series yields:
$ e^{Mt} = \begin{pmatrix} \cos(t) & -\sin(t) \\ \sin(t) & \cos(t) \end{pmatrix} $ <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>, <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>

This remarkable result shows that the abstract definition of [[matrix exponentiation]] precisely generates the rotation matrix derived from the geometric reasoning of the system <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.

#### [[applications_of_matrix_exponentiation_in_quantum_mechanics | Schrodinger's Equation]]

Schrodinger's equation, the fundamental equation describing how systems in [[applications_of_matrix_exponentiation_in_quantum_mechanics | quantum mechanics]] change over time, also takes the form of a differential equation solvable by [[matrix exponentiation]] <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. It states that the rate of change of a "state vector" (packaging all information about a system) equals a certain matrix times itself <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. The imaginary unit 'i' in Schrodinger's equation plays a similar role to the 90-degree rotation matrix in the Romeo-Juliet example, implying that the rate of change is "perpendicular" to the state, leading to oscillations <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

#### One-Dimensional Case ([[understanding_exponential_growth | Exponential Growth]])

The simplest case is a one-dimensional differential equation: $ \frac{dx}{dt} = rx $ <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
This equation describes phenomena like compound interest, population growth, or epidemics <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. Its solution is $x(t) = x_0 e^{rt}$, where $x_0$ is the initial condition <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This demonstrates that the exponential term ($e^{rt}$) acts on an initial condition to produce the solution <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. This concept generalizes to higher dimensions with matrix exponents.

## [[visualizing_matrix_exponents | Visualizing Matrix Exponents]] with Vector Fields

Systems of differential equations like $ \frac{d\vec{v}}{dt} = M\vec{v} $ can be [[visualizing_matrix_exponents | visualized]] using a vector field <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. At every point $\vec{v}$ in the state space, a vector $M\vec{v}$ is drawn, representing the velocity of a state passing through that point <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

To understand how an initial condition evolves, one can imagine it "flowing" along this vector field, with its velocity always matching the vector at its current position <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. The matrix $e^{Mt}$ effectively describes the transformation that takes any initial condition and evolves it along this flow for 't' units of time <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

For the 90-degree rotation matrix ($M = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$), the vector field consists of vectors perpendicular to the position vector, resulting in circular flow, which aligns with $e^{Mt}$ being a rotation matrix <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

For a different matrix, such as $M = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ (representing a more Shakespearean Romeo and Juliet scenario where both lovers feed off each other's feelings) <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>, the vector field shows flow away from the origin in some directions and towards it in others <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. The resulting $e^{Mt}$ matrix would then describe a transformation that squishes along one diagonal and stretches along another, becoming more extreme as 't' increases <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

### Proof Sketch

The reason $ \vec{v}(t) = e^{Mt} \vec{v}_0 $ solves the differential equation $ \frac{d\vec{v}}{dt} = M\vec{v} $ can be shown by differentiating the Taylor series definition of $e^{Mt}\vec{v}_0$ with respect to 't' <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>:

1.  Write out the full polynomial for $e^{Mt}$ and multiply by the initial condition vector $\vec{v}_0$ <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
2.  Take the derivative with respect to 't'. Since 'M' and $\vec{v}_0$ are constant, only the powers of 't' are differentiated <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>.
3.  The power rule $(t^n / n!) \rightarrow (n t^{n-1} / n!) = (t^{n-1} / (n-1)!)$ simplifies the factorial terms nicely <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>.
4.  Each term in the derivative will have an extra 'M' factored out, leading to $M$ times the original expression of $e^{Mt}\vec{v}_0$ <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.
5.  Thus, $ \frac{d}{dt}(e^{Mt} \vec{v}_0) = M (e^{Mt} \vec{v}_0) $, proving that it solves the equation <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

This proof sketch highlights the core idea, though a rigorous proof would also address the convergence of the infinite series <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.

## Further Exploration

Future discussions on [[matrix exponentiation]] often delve into its properties, particularly its relationship with eigenvectors and eigenvalues, which provide more concrete methods for computation <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. Another interesting extension is understanding what it means to raise 'E' to the power of the derivative operator <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.