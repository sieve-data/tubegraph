---
title: Principle of Least Action
videoId: Q10_srZ-pbs
---

From: [[veritasium]] <br/> 

The [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] is a single simple rule that underpins all of physics, including classical mechanics, electromagnetism, quantum theory, and general relativity, extending even to the fundamental particles [00:00:00]. It can replace all other physical principles [00:00:19]. This concept challenges the conventional "local picture" or differential equation way of thinking about the universe [00:00:34], suggesting that a global optimization principle might be more fundamental [00:00:46]. It may even explain the behavior of life itself [00:00:30].

## The Brachistochrone Problem (Problem of Fastest Descent)

The journey to understanding the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] began with a simple problem: determining the shape of a ramp that allows a mass to slide from point A to point B in the fastest possible time [00:00:51]. This is known as the problem of fastest descent [00:01:03].

Initially, common sense might suggest a straight line between A and B [00:01:06]. However, bending the ramp downward at the start causes the mass to accelerate to a higher speed earlier, leading to a faster overall travel time despite covering a slightly longer distance [00:01:12]. The challenge is to find the shape that perfectly balances acceleration and path length to minimize travel time [00:01:24].

Galileo posited that the arc of a circle was the fastest shape, demonstrating its superiority over any polygon [00:01:32]. Yet, it was not the absolute fastest [00:01:39].

### Johann Bernoulli's Challenge

In June 1696, nearly 60 years after Galileo's work, Johann Bernoulli issued this problem as a challenge to the world's best mathematicians, largely motivated by a desire to prove his own intellectual superiority [00:01:43]. Initially, no solutions were submitted within the six-month deadline [00:01:57]. Gottfried Leibniz, a friend of Bernoulli's, persuaded him to extend the deadline to allow foreigners a chance [00:02:04]. The primary target of this challenge was Isaac Newton, widely considered the foremost mathematician [00:02:12].

On January 29, 1697, Newton received Bernoulli's challenge after a day's work as warden of the Mint [00:02:25]. Despite his irritation at being "dunned and teased by foreigners about mathematical things" [00:02:39], Newton found the problem too enticing. He solved it overnight by 4:00 AM, a feat that took Bernoulli two weeks [00:02:49]. Newton submitted his anonymous solution to the journal *Philosophical Transactions* [00:03:02]. Upon seeing it, Johann Bernoulli famously remarked, "I recognize the lion by his claw," indicating his immediate recognition of Newton's genius [00:03:15]. While Newton generally outshone Bernoulli, in this specific instance, Bernoulli's solution was considered more clever and creative [00:03:27].

## Fermat's Principle of Least Time

Bernoulli's ingenious solution drew inspiration from an ancient problem concerning how light travels [00:03:46].

### Early Conceptions of Light Paths

Hero of Alexandria, in the 1st century AD, observed that light traveling in a single medium (like air) always follows the shortest path [00:03:56]. This explains why, when light reflects off a surface, the angle of incidence equals the angle of reflection [00:04:07]. However, when light passes from one medium to another (e.g., air to water), it bends, or refracts, and does not follow the shortest path [00:04:18]. This phenomenon is why an object at the bottom of a swimming pool appears to be in a different location than it actually is when viewed from above [00:04:29].

Over the next 1,600 years, scientists developed Snell's Law, which mathematically describes refraction: the sine of the angle of incidence divided by the sine of the angle of refraction is a constant *n*, dependent on the two media [00:04:47]. However, the underlying reason for Snell's Law remained unknown [00:05:04].

### Pierre Fermat's Contribution

In 1657, Pierre Fermat, a judge by day and a passionate mathematician by night [00:05:09], became interested in the principle behind refraction. He hypothesized that perhaps it wasn't distance, but **time**, that light sought to minimize [00:05:34]. Proving this for refraction was challenging, as it required calculating the travel time for every possible path light could take by varying its intersection point at the boundary, and then demonstrating that light chooses the path of shortest total travel time [00:05:46].

Fermat initially hesitated due to the complexity, but five years later, he tackled the problem [00:06:01]. He successfully showed that Snell's Law naturally emerges as the path that minimizes light's travel time [00:06:18]. The constant *n* in Snell's Law was revealed to be the ratio of the speed of light in the first medium to the speed of light in the second medium [00:06:31]. Fermat regarded this discovery as "the most extraordinary, the most unforeseen, and the happiest calculation" of his life [00:06:42]. This was the first time an optimization principle was shown to govern a natural phenomenon, demonstrating that "nature does the best possible thing" [00:07:04].

## Bernoulli's Solution and the Cycloid

Bernoulli, aware of Fermat's principle of least time, cleverly applied it to solve the problem of fastest descent [00:07:18]. He transformed the mechanics problem of a sliding particle into an optics problem [00:07:26]. He imagined a ray of light accelerating as it passes through layers of increasingly dense media, where the speed of light corresponds to the velocity a falling object would achieve at a given height [00:07:35]. By making these layers infinitesimally thin, a continuous curve emerges [00:07:45].

Using the conservation of energy for a falling particle, the velocity (*v*) achieved at any height (*y*) is proportional to the square root of *y* (v ∝ √y) [00:08:01]. Bernoulli then applied Snell's Law to this model, where the speed of light in each layer was proportional to the square root of the "height" of that layer [00:08:49]. This led to the relationship: sin(θ₁) / √y₁ = sin(θ₂) / √y₂ [00:08:54]. Recognizing that this ratio must remain constant through all layers, he set it equal to *k*: sin(θ) / √y = k [00:09:06]. Bernoulli immediately recognized this equation as the equation of a **cycloid** [00:09:28].

A cycloid is the path traced by a point on the rim of a rolling wheel [00:09:35]. This curve is also known as a **brachistochrone curve** ("shortest time") [00:09:40]. The astonishing solution was that the fastest path from A to B is indeed an arc of a cycloid, not a circle [00:09:47].

### The Tautochrone Property

The cycloid possesses another surprising property: no matter where a mass is released along the curve, it will always reach the lowest point at the same time [00:09:59]. For this reason, it is also known as the **tautochrone curve** ("same time") [00:10:04].

Bernoulli celebrated his discovery, noting that he had solved "two important problems, an optical and a mechanical one," demonstrating that these "entirely separate fields of mathematics have the same character" [00:10:14]. This unification hinted at a deeper underlying principle.

## Maupertuis' Principle of Least Action

Around 40 years later, Pierre Louis de Maupertuis, one of Bernoulli's students, further explored the similarities between light and particle behavior [00:10:38]. He questioned why nature should prioritize minimizing time, suggesting there might be a more fundamental quantity being minimized that governs both light and particles [00:10:50].

In the 1740s, Maupertuis proposed this new fundamental quantity, which he called the **action** [00:11:07]. He defined it as the product of mass, velocity, and distance (mass × velocity × distance) [00:11:12]. His reasoning was that the action increases with greater travel distance, higher speed, and greater mass [00:11:18]. For a multi-segment journey, the total action is the sum of the action for each segment [00:11:29].

Maupertuis' central claim was that out of all possible trajectories, the path taken by an object is the one that minimizes the action [00:12:06]. In 1744, he wrote that this action is "the true expense of Nature, which she manages to make as small as possible" [00:12:17].

### Reception and Criticism

Maupertuis' revolutionary idea was met with ridicule and attack [00:12:32]. His friend Samuel Konig accused him of plagiarism and incorrect physics, claiming the idea originated from Leibniz [00:12:35]. Voltaire, once a close friend, wrote a 32-page pamphlet mocking Maupertuis, fueled in part by rumors of an affair between Maupertuis and Voltaire's lover [00:12:44]. While some simply ignored him [00:13:05], Maupertuis was largely forgotten in the history of physics [00:13:08].

This harsh treatment was somewhat justified because Maupertuis' principle lacked rigorous mathematical foundation [00:13:37]. There was no clear reason why nature should minimize "mass times velocity times distance" [00:13:46].

## Euler's Defense and Refinements

Despite the criticism, Leonhard Euler vehemently defended Maupertuis' principle [00:14:01].

### Mathematical Rigor

Euler's first step was to replace the sum in Maupertuis' definition of action with an integral, allowing for continuous changes in speed or direction [00:14:09]. He used this to find the path of a particle around a central mass, such as a planet orbiting a star [00:14:18]. This problem required finding the path with the smallest action among infinitely many possibilities, a task for which the mathematical tools of the time were inadequate [00:14:25].

Euler, a prolific mathematician, invented new methods to tackle such problems [00:14:54]. Through this arduous process, he discovered that the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] is valid only if the total energy is conserved and is the same for all paths considered [00:15:02]. These crucial conditions were unknown to Maupertuis [00:15:12]. Euler significantly improved the mathematical rigor of the principle and provided a specific example of its application [00:15:16].

## Lagrange's General Proof and Modern Formulation

The general proof of the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] came from Joseph-Louis Lagrange, a shy, mostly self-taught 19-year-old [00:15:51]. In 1754, Lagrange shared his results with Euler, who praised his work for elevating the theory to "the highest summit of perfection" [00:16:10]. Both mathematicians were strong proponents of the principle [00:16:24]. Around five years later, shortly after Maupertuis' death, Lagrange succeeded in providing a general proof [00:16:30].

### The General Approach (Calculus of Variations)

Euler and Lagrange developed a method to find the path of least action among infinite possibilities, similar to how one finds the minimum of a function in calculus [00:17:25]. In calculus, a function's minimum occurs where its derivative is zero, meaning a tiny step to the left or right results in no significant change in the function's value [00:17:37].

Similarly, for the path of least action, if a tiny variation (a "bump" or "flattening," represented by a small function *eta*) is added to the path, the action should remain essentially unchanged [00:17:51]. More precisely, the difference in action between the true path and a slightly varied path will be zero to first order [00:18:23]. This means that the first-order change in action, proportional to the deviation *eta*, must be zero [00:18:27]. This is because at a minimum, the function's change is proportional to *eta* squared or higher-order terms, not *eta* [00:18:50]. This relationship, where the variation of the action is zero (δS = 0), is a compact and general way to express the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] [00:19:24].

### Hamilton's Principle and the Lagrangian

Maupertuis' original action was the integral of mass times velocity over distance [00:19:36]. By substituting velocity as *ds/dt* (distance over time) and rearranging, the action can be rewritten as the integral of mass times velocity squared over time, which is twice the kinetic energy (2T) integrated over time [00:19:48].

Euler's condition that total energy (E = T + V, where T is kinetic energy and V is potential energy) must be conserved for all paths is crucial [00:20:03]. This allows kinetic energy (T) to be expressed as E - V [00:20:10]. Substituting this into the action integral leads to an expression where the variation of (T + E - V) integrated over time is zero [00:20:16].

Further simplification reveals that the variation of the integral of (T - V) over time is proportional to the negative of the total energy multiplied by the variation of time (-E δt) [00:20:51]. To make this equal to zero and obtain a true minimization principle, one must consider only paths that have the same travel time (i.e., no variation in time, δt = 0) [00:21:07].

This leads to the modern formulation of the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]]: the variation of kinetic energy minus potential energy (T - V) integrated over time is equal to zero [00:21:23].

This formulation was first written by William Rowan Hamilton in 1834, leading to the principle being named after him: **Hamilton's Principle** [00:22:07]. The quantity (T - V) is known as the **Lagrangian** (L) [00:22:18].

### Differences Between Maupertuis' and Hamilton's Principles:

| Feature           | Maupertuis' Principle                                | Hamilton's Principle                                   |
| :---------------- | :--------------------------------------------------- | :----------------------------------------------------- |
| Action Integral   | Over space (distance) [00:22:53]                    | Over time [00:22:51]                                   |
| Required Inputs   | Start and end point, same energy [00:23:05]         | Start and end point, start and end time [00:22:58]    |
| Variable Allowed  | Time can vary between paths [00:23:08]             | Energies can differ, time must be the same [00:23:10] |

Hamilton's Principle is the modern standard for writing the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] in almost all physics texts [00:22:33]. It describes how objects move over time, not just the shape of their path [00:22:40].

### Equivalence to Newton's Second Law

When applying Hamilton's Principle to a simple example, like a ball thrown straight up in the air, connecting two points in spacetime (y at t, y at t') [00:23:25], one can imagine infinitely many possible trajectories [00:23:43]. By defining a trial path as the true path (y(t)) plus a small variation (eta(t)) [00:24:04], and requiring that the first-order difference in action between these paths is zero [00:24:26], a curious differential equation emerges after computing the action integrals and using integration by parts [00:25:31].

This equation is: m (d²y/dt²) = -dV/dy [00:25:39].
Recognizing that -dV/dy is the force (F) and d²y/dt² is acceleration (a), this equation simplifies to **F = ma** [00:25:47].
Thus, the path that satisfies the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] is precisely the one that obeys [[newtons_second_law_and_variational_principles | Newton's Second Law]] [00:25:54].

This means the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] is equivalent to [[newtons_second_law_and_variational_principles | Newton's Second Law]], but it extends beyond classical mechanics [00:26:04]. Fermat's principle of least time is revealed to be a special case of the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] [00:26:14]. This single principle unifies seemingly disparate fields of physics, from light's behavior to the motion of pendulums and planets [00:26:21].

## The Euler-Lagrange Equation

While F=ma provides a way to solve mechanics problems using forces and vectors, the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] offers an alternative using energies and scalars [00:27:10]. While seemingly more complicated, Euler and Lagrange developed a method to simplify its application [00:27:38].

If the action is defined as the integral of the Lagrangian (L = T - V) over time [00:27:44], then the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] is satisfied whenever a specific differential equation, known as the **Euler-Lagrange equation**, is met [00:27:54].

The Euler-Lagrange equation allows one to solve any mechanics problem by simply writing down the kinetic and potential energy of the system and plugging them into this equation [00:28:00]. This approach is extremely powerful because it:
*   Works in multiple dimensions by solving the Euler-Lagrange equation for each coordinate [00:28:39].
*   Allows the use of "weird" or specialized coordinate systems (e.g., polar coordinates for rotational problems) that are better suited to the problem, providing the correct equations of motion more easily than with vectors [00:28:46].
*   Simplifies complex problems, such as a double pendulum, which would be extremely difficult to solve using force-based methods due to moving reference frames [00:29:04].

## Principle of Stationary Action

A crucial clarification regarding the name: while commonly called the "[[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]]", it is more accurately termed the **Principle of Stationary Action** [00:29:35]. Just as setting a derivative to zero in calculus doesn't guarantee a minimum (it could be a maximum or a saddle point), the principle demands a stationary point for the action [00:29:52]. Although it often results in a true minimum, it is not always the case [00:30:14]. The laws of motion derive from this demand for a stationary point, leading to the Euler-Lagrange equation [00:30:03].

## Broader Implications

The concept of action is far more fundamental than just classical mechanics [00:30:19]. Around the turn of the 20th century, action emerged as a key component in solving one of atomic physics' biggest problems: the UV catastrophe, which initiated the development of quantum theory [00:30:23]. The fact that action, rather than energy or force, appeared at this breakthrough moment hints at its profound significance [00:30:37].

The story of the [[principle_of_least_action_in_classical_and_quantum_mechanics | Principle of Least Action]] exemplifies how knowledge compounds, progressing steadily until it completely transforms our understanding of the world [00:31:02].