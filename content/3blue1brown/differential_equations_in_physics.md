---
title: Differential equations in physics
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

[[basics_and_significance_of_differential_equations | Differential equations]] are fundamental to describing the universe, particularly in physics <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. They appear frequently, especially in [[quantum_mechanics | quantum mechanics]], where matrix exponents play a prominent role <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Role of Matrix Exponents

Matrix exponents, while appearing to be "total nonsense" out of context, refer to a beautiful mathematical operation useful for [[solving_systems_of_differential_equations_using_matrices | solving systems of differential equations using matrices]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The notation `E` to the power `A` `t`, where `A` is a matrix, implies that the result is also a matrix <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Definition of Matrix Exponentiation

The definition of a matrix raised to an exponent is based on the infinite polynomial, or Taylor series, for `E` to the power `x` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. While for real numbers `E` to the power `x` is a theorem, for more exotic inputs like matrices, it serves as a definition <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

For a matrix `A` to be plugged into this polynomial, it must have the same number of rows and columns, allowing for standard matrix multiplication to compute its powers <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Each term in the polynomial is scaled by one divided by a factorial, meaning each component of the matrix is multiplied by that number <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Matrices can also be added term by term <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

Despite the infinite sum, the result generally approaches a stable value for any matrix <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

### Motivation for Matrix Exponents

Mathematicians and physicists use matrix exponents to solve specific problems <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. One key motivation is solving [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | ordinary differential equations]] (ODEs) where the rate of change of a vector is equal to a constant matrix multiplied by the vector itself <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Schrodinger's Equation

[[quantum_mechanics | Schrodinger's equation]] is a fundamental equation in [[quantum_mechanics | quantum mechanics]] that describes how quantum systems evolve over time <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. It shares a similar structure with simpler systems (like the Romeo-Juliet example discussed in the video), where the rate of change of a state vector is expressed as a certain matrix times itself <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

The state vector in Schrodinger's equation packages all relevant information about a system, such as particle positions and momenta <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. While more complex, it serves as a target example that simpler cases help build up to <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

The presence of the imaginary unit `i` in Schrodinger's equation indicates that the rate of change of a state is, in a sense, perpendicular to that state, leading to an oscillatory evolution over time <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

## Generalizing Solutions to Differential Equations

For a single changing value where its rate of change equals some constant times itself (a one-dimensional case), the solution is exponential growth, `e^(rt)` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This represents phenomena like compound interest or population growth <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

When generalizing to higher dimensions, for a changing vector whose rate of change is constrained to be some matrix times itself, the solution involves an exponential term acting on a given initial condition <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This exponential part produces a matrix that changes with time, which then acts on the initial condition vector <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. The definition of matrix exponentiation is heavily motivated by ensuring this fact is true <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

### Visualizing Differential Equations with Vector Fields

[[applications_of_phase_space_in_differential_equations | Differential equations]] can be visualized using a vector field <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This means drawing a little vector at every point in space, indicating the velocity of a state if it passes through that point <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. For equations where the rate of change of a state `v` equals `M` times `v`, we attach the vector `Mv` to each point `v` in space <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

To understand how an initial condition evolves, one can imagine it "flowing" along this vector field <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. The transition from the start to the finish is described by the matrix `e^(Mt)` <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. This confirms how matrix exponentiation provides a systematic way to solve such general equations without guessing <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

```
dt(X)/dt = M * X
X(t) = e^(Mt) * X_0
```
This equation is solved by `e^(Mt)` times the initial condition `X_0` <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. The derivative of `e^(Mt) * X_0` with respect to `t` is `M * (e^(Mt) * X_0)`, thus satisfying the differential equation <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.