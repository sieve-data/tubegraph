---
title: Application of Calculus in Physics
videoId: Q10_srZ-pbs
---

From: [[veritasium]] <br/> 

Calculus plays a fundamental role in understanding and describing the universe, particularly through a single simple rule that underpins all of physics, from classical mechanics to electromagnetism, quantum theory, and general relativity <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This rule can even replace various principles and equations, unifying seemingly separate fields <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## The Problem of Fastest Descent

The journey into this unifying principle begins with a simple problem: determining the ramp shape that allows a mass to slide from point A to point B in the fastest possible time <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This is known as the problem of fastest descent <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Common sense might suggest a straight line, but bending the ramp allows the mass to accelerate to a higher speed earlier, potentially reaching the destination faster despite traveling a slightly longer path <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Galileo suggested the arc of a circle was fastest, proving it superior to any polygon <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. However, in June 1696, Johann Bernoulli challenged the world's best mathematicians to find the absolute fastest shape <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Isaac Newton famously solved it overnight, though Bernoulli's solution was arguably more elegant <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The correct shape is a cycloid, also known as a brachistochrone curve (Greek for "shortest time") <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This curve also possesses the surprising property that, regardless of the starting point, a mass released on it will reach the end in the same amount of time, earning it the name tautochrone curve (Greek for "same time") <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

## Principle of Least Time (Fermat)

Bernoulli's clever solution drew inspiration from the problem of how light travels <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Hero of Alexandria noted in the 1st century AD that in a single medium, light follows the shortest path <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. However, when light refracts, moving from one medium to another (like air into water), it bends and does not follow the shortest path <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Snell's Law describes this bending, but its underlying reason was unknown until Pierre Fermat in 1657 <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Fermat proposed that light minimizes not distance, but *time* <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. To test this for refraction, he needed to analyze every possible light path, varying the intersection point at the boundary, and compute the time for each to show light takes the shortest time <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Although initially hesitant due to the perceived complexity <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, Fermat later solved it, demonstrating that Snell's Law emerges as the minimizing path for light <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Fermat's Principle of Least Time was the first instance of an [[History of Physics and Mathematics | optimization principle]] being shown to govern nature <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

Bernoulli used Fermat's principle by converting the mechanical problem of a sliding particle into an optics problem <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. He imagined light traveling through layers of progressively less dense media, with its speed proportional to the square root of the distance fallen, analogous to an object gaining kinetic energy <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Applying Snell's Law to infinitesimally thin layers, he derived a constant ratio that he recognized as the equation of a cycloid <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

## Principle of Least Action (Maupertuis, Euler, Lagrange, Hamilton)

Around 40 years after Bernoulli's work, Pierre Louis de Maupertuis proposed a more fundamental quantity than time: "action" <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. He defined action as mass times velocity times distance, suggesting that nature minimizes this quantity <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. Maupertuis claimed that out of all possible trajectories, the path taken by a particle is the one that minimizes action <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Though initially ridiculed due to its lack of rigor and apparent arbitrary nature <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>, Maupertuis' idea laid the groundwork for what would become a cornerstone of physics.

### Euler's Contributions to Calculus and Action

Leonhard Euler vehemently defended Maupertuis' principle <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. His first key contribution was replacing the sum in Maupertuis' action with an integral <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>, allowing for the calculation of action when speed or direction changed continuously. He used this to find the path of a particle around a central mass, like a planet orbiting a star <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This problem required finding the path with the smallest action out of infinitely many possibilities <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>, necessitating the development of new mathematical tools <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Euler himself invented a new method for this <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. Through this process, Euler realized that the principle of least action only works if the total energy is conserved and is the same for all paths considered <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

### Lagrange's General Proof

Joseph-Louis Lagrange, a self-taught mathematician, provided a general proof for the principle of least action around 1759, a year after Maupertuis' death <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

The general approach developed by Euler and Lagrange to find the path with the least action is analogous to finding the minimum of a function in calculus <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. In calculus, one takes the derivative of a function and sets it to zero to find a minimum where the slope is horizontal <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Similarly, for the path of least action, if the path is varied infinitesimally (by adding a tiny function 'eta'), the action should essentially not change at first order <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. This means the difference in action between the optimal path and a trial path is zero to first order <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.

### Hamilton's Principle and the Euler-Lagrange Equation

The modern form of the principle of least action, known as Hamilton's Principle, was developed by William Rowan Hamilton in 1834 <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. Maupertuis' action (mass times velocity integrated over distance) can be rewritten using calculus principles:
*   Velocity is `ds/dt` (distance over time).
*   Substituting `ds = v dt` into the integral yields an integral of `mv^2` over time, which is twice the kinetic energy (T) <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   Given that total energy (E) is conserved (`E = T + V`, where V is potential energy), `T = E - V` <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   This transformation ultimately leads to the action being expressed as the integral of `(Kinetic Energy - Potential Energy)` (T - V) over time <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. This `(T - V)` term is called the Lagrangian (L) <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

Hamilton's Principle states that the variation of the integral of the Lagrangian (L) over time is zero <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. This implies that the true path taken by a system is the one for which the action is stationary (a minimum, maximum, or saddle point).

When applying this mathematical framework to a simple example, like a ball thrown vertically, and solving the integral variation using techniques like integration by parts, it is found that the path satisfying the principle of least action is precisely the one that obeys [[Newtons Second Law and Variational Principles | Newton's Second Law]] (F=ma) <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.

## Significance of the Euler-Lagrange Equation

The principle of least action, expressed through the Euler-Lagrange equation, unifies disparate fields of physics. Fermat's principle of least time is merely a special case <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>. This single principle can describe phenomena from light reflection and refraction to planetary orbits <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

While it might seem more complicated than using forces and vectors with [[Newtons Second Law and Variational Principles | Newton's Second Law]] <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>, the Euler-Lagrange equation simplifies solving complex mechanics problems <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>. One simply writes down the kinetic and potential energies, plugs them into the equation, and the correct equations of motion are derived <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. This approach is particularly powerful for systems with multiple dimensions or complex coordinate systems (e.g., using polar coordinates for rotational problems), where vector-based force calculations can be tricky <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>. For example, solving a double pendulum problem using forces is extremely hard, but relatively easy with kinetic and potential energy via the Lagrangian approach <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

It is important to note that while often called the "principle of least action," it is more accurately the "principle of stationary action" <a class="yt-timestamp" data-t="00:29:58">[00:29:58]</a>. This is because setting a derivative to zero in calculus finds stationary points, which can be minima, maxima, or saddle points, though it is very often a true minimum in physical systems <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.

Action also surfaced as a key part of the solution to the UV catastrophe, a major problem in atomic physics at the turn of the 20th century, hinting at its fundamental nature in the development of quantum theory <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>. The story of the principle of least action exemplifies how knowledge compounds, leading to profound shifts in how we understand the world <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.