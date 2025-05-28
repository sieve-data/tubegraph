---
title: applications of calculus in physics
videoId: Q10_srZ-pbs
---

From: [[veritasium]] <br/> 

The principles of [[physics_and_aerodynamic_principles | physics]] are underpinned by a single simple rule, applicable from classical mechanics to electromagnetism, and from quantum theory to [[applications_of_noneuclidean_geometry_in_general_relativity | general relativity]], even to the fundamental particles of matter <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This rule, known as the principle of least action, relies heavily on calculus. While a classical mindset might prioritize a "differential equation way of thinking" about the universe <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, this video suggests that this perspective might be backwards <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, hinting at a more fundamental principle best expressed through calculus.

## The Problem of Fastest Descent (Brachistochrone Problem)

The journey to understanding this fundamental rule began with a simple problem: determining the shape of a ramp that would allow a mass to slide from point A to point B in the fastest possible time <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This is known as the problem of fastest descent, or the brachistochrone problem <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Common sense might suggest a straight line, but bending the ramp downwards initially allows the mass to accelerate to a higher speed earlier, reducing overall travel time despite a longer path <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Galileo believed the arc of a circle was the fastest path <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. However, in June 1696, Johann Bernoulli challenged the world's best mathematicians to find the true solution <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. [[development_of_calculus_by_isaac_newton | Isaac Newton]], then working as the warden of the Mint <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, solved the problem within a night of receiving it <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, demonstrating his mastery of calculus. Bernoulli's solution, which was considered more elegant, involved converting the mechanics problem into an optics problem, drawing inspiration from Fermat's Principle of Least Time <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This method implicitly uses calculus to derive the cycloid as the path of fastest descent <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## Fermat's Principle of Least Time

In the 17th century, Pierre Fermat became interested in why light refracts (bends when passing from one medium to another) <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. He proposed that light follows the path that minimizes travel time <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. To prove this for refraction, he needed to calculate the time for every possible path light could take by varying its intersection point with the boundary between media, then show that the actual path minimizes this time <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This "most extraordinary, the most unforeseen, and the happiest calculation" <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a> revealed that Snell's Law emerges directly from this minimization principle <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This was a foundational moment, demonstrating that nature obeys an "optimization principle" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>, a concept central to calculus applications.

## The Principle of Least Action

Building on Fermat's work, Pierre Louis de Maupertuis proposed a more fundamental quantity called "action" in the 1740s, defined as mass times velocity times distance <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. He hypothesized that physical systems follow paths that minimize this quantity, declaring it "the true expense of Nature, which she manages to make as small as possible" <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### Euler and Lagrange's Contributions

Maupertuis's initial formulation lacked mathematical rigor <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. [[history_of_physics_and_mathematics_discoveries | Leonhard Euler]] defended and improved the principle by replacing the sum in Maupertuis's action with an integral <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>, allowing for continuous changes in speed or direction. He also realized that the principle only works if the total energy is conserved and is the same for all paths considered <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. Euler's work required developing new mathematical tools to handle problems involving infinitely many possible paths <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

Joseph-Louis Lagrange, a self-taught mathematician, further "extolled the theory to the highest summit of perfection" <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a> by providing a general proof for the principle of least action around 1759 <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

### Solving for Minimal Action with Calculus

The general approach to finding the path of least action, pioneered by Euler and Lagrange, is analogous to finding the minimum of a function in calculus: by taking a derivative and setting it to zero <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. If a path has the least action, tiny variations to it should result in no change in action to the first order <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. This is because at a minimum, the slope (first derivative) is zero <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. This concept is expressed as:
$$
\delta S = S_{trial} - S_{true} = 0 \text{ (to first order)}
$$
<a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>

### Hamilton's Principle and the Lagrangian

William Rowan Hamilton reformulated the principle of least action in 1834 <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>, giving rise to "Hamilton's Principle." In this modern form, the action is defined as the integral of the kinetic energy (T) minus the potential energy (V) over time:
$$
S = \int (T - V) dt
$$
<a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>
The quantity (T - V) is called the Lagrangian (L) <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>. Hamilton's Principle states that the variation of the action is zero ($\delta S = 0$) <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. This requires specifying both start and end points, as well as start and end times <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.

Applying this calculus-based approach to a simple problem, such as a ball thrown in the air, reveals that the path minimizing the action is precisely the one that obeys [[development_of_calculus_by_isaac_newton | Newton's Second Law]] (F = ma) <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. This shows that the principle of least action is equivalent to [[development_of_calculus_by_isaac_newton | Newton's Second Law]] but provides a broader framework <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>.

## Unification and Power of the Lagrangian Approach

The principle of least action unifies disparate fields of physics <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>. Fermat's principle of least time for light is a special case of the principle of least action <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>. This single principle can describe everything from light reflection and refraction to planetary orbits and the motion of complex systems like a double pendulum <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>.

While solving problems using forces and vectors (as in [[development_of_calculus_by_isaac_newton | Newton's Laws]]) is possible, the Lagrangian approach, derived from calculus and the principle of least action, offers a powerful alternative <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>. By simply writing down the kinetic and potential energies and plugging them into the Euler-Lagrange equation, one can derive the correct equations of motion for any mechanics problem <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. This is particularly advantageous for complex systems or when using non-Cartesian coordinate systems (e.g., polar coordinates for rotating problems) <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>, where vector-based solutions become "very nasty" <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>.

It's important to note that while often called the "principle of least action," it is more accurately described as the "principle of stationary action" <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Setting the derivative to zero finds a stationary point, which may be a minimum, maximum, or saddle point, although it very often yields a true minimum <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.

The concept of action proved to be fundamental not just in classical mechanics but also in the development of quantum theory, appearing as a key part of the solution to problems like the UV catastrophe <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>. This highlights the profound and unifying role of calculus in understanding the physical world.

<br>
The language of most of [[physics_and_aerodynamic_principles | physics]] is [[development_of_calculus_by_iac_newton | calculus]] <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>. Learning calculus can provide intuition for building practical skills in math and [[physics_and_aerodynamic_principles | physics]] <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.