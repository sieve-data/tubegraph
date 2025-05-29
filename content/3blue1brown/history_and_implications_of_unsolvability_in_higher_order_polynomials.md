---
title: History and implications of unsolvability in higher order polynomials
videoId: -RdOwhmqP5s
---

From: [[3blue1brown]] <br/> 

The question of how to compute the roots of a polynomial exactly is a fundamental one in mathematics and engineering <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. While for lower-degree polynomials, explicit formulas exist, the situation changes significantly for higher degrees.

## Solving Polynomials: From Quadratic to Quartic

For a quadratic function (degree 2), the well-known quadratic formula provides an exact solution for its roots <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>. This formula is incredibly useful and, for example, was estimated to have been used trillions of times in the production of the movie *Coco* for per-pixel calculations involving polynomially defined objects like spheres in computer graphics <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.

As the degree of the polynomial increases, finding exact solutions becomes trickier <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>:
*   **Cubic Polynomials (Degree 3)**: A formula exists for cubic polynomials <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
*   **Quartic Polynomials (Degree 4)**: A quartic formula also exists, but it is considered "a god-awful nightmare" and is rarely used in practice due to its complexity <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.

## The Unsolvability of the Quintic

Beyond degree 4, a profound mathematical result changes the landscape of polynomial root-finding. For polynomials with a degree of 5 or more, there is no analogous general formula <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>. More precisely, for a broad set of standard functions, it can be proven that no combination of these functions allows one to plug in the coefficients of a quintic (degree 5) polynomial and consistently obtain a root <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. This concept is known as the [[unsolved_problem_in_physics_and_math | unsolvability of the quintic]] <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

## Practical Implications

Despite the theoretical [[unsolved_problem_in_physics_and_math | unsolvability of the quintic]] by formula, in practice, this limitation "kind of doesn't matter" <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. This is because algorithms exist that can approximate solutions to these equations with any desired level of precision <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

One common and widely used algorithm for this purpose is [[newtons_method_for_solving_polynomials | Newton's Method]] <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. This iterative method involves:
1.  Starting with an initial guess (x0) <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
2.  Calculating a linear approximation of the function (a tangent line) at that guess <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.
3.  Determining where this tangent line crosses the x-axis to find an improved guess <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>.
4.  Repeating the process until the guess is extremely close to a true root <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.

This method, also often called the Newton-Raphson method due to Joseph Raphson's simpler version, is a common topic in calculus classes <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

It's important to note that the complexity of fractal patterns generated when applying [[newtons_method_for_solving_polynomials | Newton's Method]] in the complex plane for polynomials of degree three or higher (often called Newton's fractals) is "essentially unrelated" to the [[unsolved_problem_in_physics_and_math | unsolvability of the quintic]] <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>. The fractal complexity arises from the dynamics of the iterative process in the complex plane, not from the lack of a closed-form algebraic solution for the roots themselves.